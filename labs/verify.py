"""Replay checked-in expectations, fail on disagreement, and print case IDs."""

import csv
import json
from pathlib import Path
import sys

from labs.board_format.codec import from_csv, to_csv
from labs.quote_api import reference, replacement
from labs.ticket_triage.rules import route

ROOT = Path(__file__).resolve().parent


def verify():
    results = []
    cases = json.loads((ROOT / "quote_api/fixtures.json").read_text(encoding="utf-8"))
    for case in cases:
        expected = case["expected_status"], case["expected_body"]
        actual = reference.quote(case["request"]), replacement.quote(case["request"])
        results.append((f"quote-api/{case['id']}", all(result == expected for result in actual)))
    board = from_csv((ROOT / "board_format/fixtures/cards.csv").read_text(encoding="utf-8"))
    expected_board = json.loads((ROOT / "board_format/fixtures/expected.json").read_text(encoding="utf-8"))
    results.append(("board-format/expected-and-roundtrip", board == expected_board and from_csv(to_csv(board)) == board))
    tickets = json.loads((ROOT / "ticket_triage/fixtures/input.json").read_text(encoding="utf-8"))
    expected_routes = json.loads((ROOT / "ticket_triage/fixtures/expected.json").read_text(encoding="utf-8"))
    results.append(("ticket-triage/expected-routes", route(tickets) == expected_routes))
    return results


def main():
    try:
        results = verify()
    except (OSError, ValueError, KeyError, csv.Error) as exc:
        print(f"Lab verification error: {exc}", file=sys.stderr)
        return 1
    for name, passed in results:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    print(f"{sum(passed for _, passed in results)}/{len(results)} checks passed.")
    return 0 if all(passed for _, passed in results) else 1


if __name__ == "__main__":
    sys.exit(main())
