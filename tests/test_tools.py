import contextlib
import csv
from decimal import Decimal
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("unfired", ROOT / "tools" / "unfired.py")
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


class ToolTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)

    def fixture(self, text):
        path = self.base / "input.csv"
        path.write_text(text, encoding="utf-8")
        return path

    def test_runway_example(self):
        result = tool.runway(Decimal(9000), Decimal(2500), Decimal(500), Decimal(1000))
        self.assertIn("4.0 months", result)

    def test_runway_zero_gap_and_no_spendable_cash(self):
        self.assertIn("No cash depletion", tool.runway(Decimal(10), Decimal(5), Decimal(5), Decimal(0)))
        self.assertIn("0.0 months", tool.runway(Decimal(10), Decimal(5), Decimal(0), Decimal(10)))
        with self.assertRaises(ValueError):
            tool.runway(Decimal(10), Decimal(5), Decimal(0), Decimal(11))

    def test_cli_rejects_invalid_money(self):
        for value in ("NaN", "Infinity", "-1", "nonsense", "1e1000"):
            result = subprocess.run([sys.executable, str(ROOT / "tools/unfired.py"), "runway", "--cash", value,
                                     "--monthly-costs", "100"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2, value)
            self.assertNotIn("Traceback", result.stderr)

    def test_workspace_preserves_user_edits(self):
        self.assertEqual(len(tool.init_workspace(self.base)), 3)
        tracker = self.base / "applications.csv"
        tracker.write_text("my private entries", encoding="utf-8")
        self.assertEqual(tool.init_workspace(self.base), [])
        self.assertEqual(tracker.read_text(), "my private entries")

    def test_clean_unicode_quotes_multiline_duplicates_and_formula(self):
        path = self.fixture('\ufeff Full Name , Note \n Ana ,"hello, world"\n Ana ,"hello, world"\n Zoë ,"two\nlines"\n =SUM(A1) , @cmd \n , \n')
        text, before, after = tool.clean_csv(path)
        rows = list(csv.reader(io.StringIO(text)))
        self.assertEqual((before, after), (5, 3))
        self.assertEqual(rows, [["full_name", "note"], ["Ana", "hello, world"], ["Zoë", "two\nlines"], ["'=SUM(A1)", "'@cmd"]])

    def test_bad_csv_is_rejected(self):
        for content in ("", "Name,name\na,b\n", "!!!,OK\na,b\n", "a,b\none\n", 'a,b\n"unterminated,b\n'):
            with self.subTest(content=content):
                with self.assertRaises((ValueError, csv.Error)):
                    tool.clean_csv(self.fixture(content))

    def test_refuses_overwrite_and_same_input_path(self):
        path = self.fixture("a,b\nx,y\n")
        with self.assertRaises(FileExistsError):
            tool.write_new(path, "replacement")
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as result:
            tool.main(["csv-clean", str(path), "--out", str(path)])
        self.assertEqual(result.exception.code, 2)
        self.assertEqual(path.read_text(), "a,b\nx,y\n")

    def test_snapshot_omits_sensitive_fields(self):
        report = tool.tracker_report(self.fixture("company,status,notes\nSECRET NAME,Applied,SECRET NOTE\nOTHER,interview,PRIVATE\n"))
        self.assertIn("Total tracked opportunities: 2", report)
        self.assertIn("| applied | 1 |", report)
        for secret in ("SECRET NAME", "SECRET NOTE", "OTHER", "PRIVATE"):
            self.assertNotIn(secret, report)

    def test_snapshot_empty_and_invalid_states(self):
        self.assertIn("Total tracked opportunities: 0", tool.tracker_report(self.fixture("status\n")))
        for content in ("company\nExample\n", "status,status\napplied,applied\n", "status\nunknown\n"):
            with self.assertRaises(ValueError):
                tool.tracker_report(self.fixture(content))

    def test_fresh_checkout_end_to_end(self):
        cli = [sys.executable, str(ROOT / "tools/unfired.py")]
        result = subprocess.run(cli + ["init"], cwd=self.base, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        output = self.base / "nested" / "clean.csv"
        result = subprocess.run(cli + ["csv-clean", str(ROOT / "examples/messy-contacts.csv"), "--out", str(output)],
                                cwd=self.base, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(list(csv.reader(io.StringIO(output.read_text())))), 3)
        report = self.base / "report.md"
        result = subprocess.run(cli + ["report", str(self.base / ".unfired/applications.csv"), "--out", str(report)],
                                cwd=self.base, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Total tracked opportunities: 0", report.read_text())


if __name__ == "__main__":
    unittest.main()
