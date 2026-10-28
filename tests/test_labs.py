import csv
from copy import deepcopy
import http.client
import importlib.util
import json
from pathlib import Path
import random
import subprocess
import sys
import tempfile
import threading
import unittest

from labs.board_format.codec import from_csv, to_csv
from labs.quote_api import reference, replacement
from labs.quote_api.server import make_server
from labs.ticket_triage.rules import route
from labs.verify import verify

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("new_project", ROOT / "tools/new_project.py")
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


class LabTests(unittest.TestCase):
    def test_all_golden_cases_match_independent_expectations(self):
        results = verify()
        self.assertGreaterEqual(len(results), 20)
        self.assertEqual([name for name, passed in results if not passed], [])

    def test_decimal_and_integer_rounding_agree_across_rates(self):
        rng = random.Random(20261027)
        for _ in range(150):
            request = {"items": [{"sku": "fixture", "quantity": rng.randint(1, 1000), "unit_cents": rng.randint(0, 1000000)}],
                       "discount_bps": rng.randint(0, 10000), "tax_bps": rng.randint(0, 10000)}
            self.assertEqual(reference.quote(request), replacement.quote(request))

    def test_board_unicode_multiline_roundtrip_and_expected_values(self):
        text = (ROOT / "labs/board_format/fixtures/cards.csv").read_text(encoding="utf-8")
        document = from_csv(text)
        self.assertEqual(from_csv(to_csv(document)), document)
        self.assertIn('"and" Unicode: Zoë', document["cards"][1]["title"])
        self.assertEqual(document["cards"][2]["title"], "Write a note\non two lines")

    def test_board_rejects_unknown_version_duplicates_and_lossy_schema(self):
        base = json.loads((ROOT / "labs/board_format/fixtures/expected.json").read_text(encoding="utf-8"))
        for edit in (lambda d: d.update(version=True), lambda d: d.update(version=2),
                     lambda d: d["cards"].append(d["cards"][0]),
                     lambda d: d["cards"][0].update(extra="would be lost"),
                     lambda d: d["cards"][0].update(labels=["same", "same"]),
                     lambda d: d["cards"][0].update(state=[])):
            document = deepcopy(base)
            edit(document)
            with self.assertRaises(ValueError):
                to_csv(document)
        for text in ('id,title,state,labels\na,Name,todo,not-json\n', 'id,title\na,b\n',
                     'id,title,state,labels\na,Name,todo,[],extra\n'):
            with self.assertRaises((ValueError, csv.Error)):
                from_csv(text)

    def test_empty_board_is_valid(self):
        document = {"format": "unfired-board", "version": 1, "cards": []}
        self.assertEqual(from_csv(to_csv(document)), document)

    def test_urgent_rule_wins_and_unknown_topic_has_fallback(self):
        output = route([{"id": "a", "topic": "refund", "urgent": True},
                        {"id": "b", "topic": "unknown", "urgent": False}])
        self.assertEqual(output["routes"][0]["queue"], "human_review")
        self.assertEqual(output["routes"][1]["reason"], "fallback")
        self.assertEqual(sum(output["counts"].values()), 2)
        self.assertEqual(route([])["routes"], [])

    def test_triage_rejects_ambiguous_or_duplicate_tickets(self):
        good = {"id": "a", "topic": "bug", "urgent": False}
        for tickets in ([good, good], [dict(good, urgent="false")], [dict(good, private_note="private")],
                        [dict(good, id=[])], [None], {}):
            with self.assertRaises(ValueError):
                route(tickets)

    def test_scaffold_validates_slug_and_preserves_existing_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "demo"
            self.assertEqual(generator.scaffold("demo-tool", "api", destination), 10)
            self.assertIn("draft dossier", (destination / "README.md").read_text())
            (destination / "SPEC.md").write_text("my requirements")
            with self.assertRaises(FileExistsError):
                generator.scaffold("demo-tool", "api", destination)
            self.assertEqual((destination / "SPEC.md").read_text(), "my requirements")
            for name in ("../escape", "Bad Name", "a--b", "-invalid", "x" * 65):
                with self.assertRaises(ValueError):
                    generator.scaffold(name, "api", Path(tmp) / "invalid")
            self.assertFalse((Path(tmp) / "invalid").exists())

    def test_file_commands_use_new_paths_and_preserve_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = ROOT / "labs/board_format/fixtures/cards.csv"
            target = Path(tmp) / "board.json"
            commands = [sys.executable, "-m", "labs.board_format", "from-csv", str(source), "--out", str(target)]
            result = subprocess.run(commands, cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            original = target.read_text()
            result = subprocess.run(commands, cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(target.read_text(), original)
            triage = subprocess.run([sys.executable, "-m", "labs.ticket_triage", "labs/ticket_triage/fixtures/input.json",
                                     "--out", str(Path(tmp) / "triage.json")], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(triage.returncode, 0, triage.stderr)


class HttpContractTests(unittest.TestCase):
    def test_both_servers_obey_the_http_contract(self):
        for implementation in ("reference", "replacement"):
            with self.subTest(implementation=implementation):
                server = make_server(implementation, 0)
                thread = threading.Thread(target=server.serve_forever, daemon=True)
                thread.start()
                try:
                    def request(method, path, body=None, headers=None):
                        client = http.client.HTTPConnection("127.0.0.1", server.server_port, timeout=5)
                        try:
                            client.request(method, path, body, headers or {})
                            response = client.getresponse()
                            self.assertTrue(response.getheader("Content-Type").startswith("application/json"))
                            return response.status, json.loads(response.read())
                        finally:
                            client.close()
                    self.assertEqual(request("GET", "/health"), (200, {"status": "ok"}))
                    self.assertEqual(request("POST", "/missing", "{}"), (404, {"error": "not_found"}))
                    self.assertEqual(request("POST", "/v1/quote", "not-json"), (400, {"error": "invalid_request"}))
                    self.assertEqual(request("POST", "/v1/quote", "{}", {"Content-Length": "65537"}),
                                     (413, {"error": "request_too_large"}))
                    payload = {"items": [{"sku": "demo", "quantity": 2, "unit_cents": 1250}]}
                    self.assertEqual(request("POST", "/v1/quote", json.dumps(payload)), reference.quote(payload))
                finally:
                    server.shutdown()
                    server.server_close()
                    thread.join(timeout=5)


if __name__ == "__main__":
    unittest.main()
