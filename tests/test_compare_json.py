import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("compare_json", ROOT / "tools/compare_json.py")
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


class ComparisonTests(unittest.TestCase):
    def test_comparison_is_strict_and_reports_no_values(self):
        self.assertEqual(tool.compare({"a": 1, "b": 2}, {"b": 2, "a": 1}), [])
        self.assertEqual(tool.compare(True, 1), [{"path": "", "kind": "type_mismatch"}])
        self.assertEqual(tool.compare(1, 1.0), [{"path": "", "kind": "type_mismatch"}])
        differences = tool.compare({"a/b~": ["SECRET", None], "missing": None}, {"a/b~": ["OTHER"], "extra": 1})
        self.assertIn({"path": "/a~1b~0/0", "kind": "value_mismatch"}, differences)
        self.assertIn({"path": "/a~1b~0/1", "kind": "missing_item"}, differences)
        self.assertIn({"path": "/missing", "kind": "missing_key"}, differences)
        self.assertIn({"path": "/extra", "kind": "extra_key"}, differences)
        self.assertNotIn("SECRET", json.dumps(differences))

    def test_read_rejects_duplicate_keys_and_nonfinite_numbers(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "input.json"
            for content in ('{"x":1,"x":2}', '{"x":NaN}', '{"x":Infinity}', '{"x":1e999}'):
                path.write_text(content)
                with self.assertRaises(ValueError):
                    tool.read_json(path)

    def test_cli_exit_codes_and_overwrite_protection(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            expected, actual = base / "expected.json", base / "actual.json"
            expected.write_text('{"count":1}')
            actual.write_text('{"count":2}')
            output = base / "report.json"
            cmd = [sys.executable, str(ROOT / "tools/compare_json.py"), str(expected), str(actual), "--out", str(output)]
            result = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertFalse(json.loads(output.read_text())["equal"])
            previous = output.read_text()
            result = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(output.read_text(), previous)
            actual.write_text(expected.read_text())
            cmd[-1] = str(base / "matching-report.json")
            result = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
