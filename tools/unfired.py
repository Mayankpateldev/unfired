#!/usr/bin/env python3
"""Unfired: dependency-free local tools. SPDX-License-Identifier: MIT."""

import argparse
from collections import Counter
import csv
from decimal import Decimal, InvalidOperation
import io
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {"researching", "applied", "conversation", "interview", "offer", "closed"}


def money(value):
    try:
        result = Decimal(value)
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError("use a non-negative decimal amount") from exc
    if not result.is_finite() or result < 0 or result > Decimal("1e15"):
        raise argparse.ArgumentTypeError("amount must be finite and between 0 and 1e15")
    return result


def runway(cash, monthly_costs, monthly_income, reserve):
    if reserve > cash:
        raise ValueError("reserve cannot exceed cash")
    usable = cash - reserve
    gap = monthly_costs - monthly_income
    lines = [f"Usable cash: {usable:.2f}", f"Monthly gap: {gap:.2f}"]
    if gap > 0:
        lines.append(f"Estimated runway: {usable / gap:.1f} months")
    else:
        lines.append("No cash depletion in this constant-income/constant-cost scenario.")
    lines.append("One currency; excludes taxes, timing, shocks, and benefit eligibility.")
    return "\n".join(lines) + "\n"


def write_new(path, content):
    """Exclusive creation refuses existing files, including symlinks."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="") as stream:
        stream.write(content)


def init_workspace(base):
    base = Path(base)
    base.mkdir(parents=True, exist_ok=True)
    created = []
    for name in ("applications.csv", "budget.csv", "weekly-plan.md"):
        try:
            write_new(base / name, (ROOT / "templates" / name).read_text(encoding="utf-8"))
        except FileExistsError:
            continue
        created.append(name)
    return created


def read_table(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.reader(stream, strict=True))
    if not rows or not rows[0]:
        raise ValueError("CSV needs a header row")
    width = len(rows[0])
    for number, row in enumerate(rows[1:], start=2):
        if len(row) != width:
            raise ValueError(f"CSV row {number} has {len(row)} fields; expected {width}")
    return rows


def safe_cell(value):
    value = value.strip()
    # This precaution changes values; it is intentionally always enabled.
    if value.startswith(("=", "+", "-", "@")):
        return "'" + value
    return value


def clean_csv(path):
    rows = read_table(path)
    headers = [re.sub(r"[^\w]+", "_", cell.strip().lower()).strip("_") for cell in rows[0]]
    if any(not header for header in headers) or len(set(headers)) != len(headers):
        raise ValueError("headers must be non-empty and unique after normalization")
    seen = set()
    cleaned = []
    for row in rows[1:]:
        row = tuple(safe_cell(cell) for cell in row)
        if any(row) and row not in seen:
            cleaned.append(row)
            seen.add(row)
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(headers)
    writer.writerows(cleaned)
    return output.getvalue(), len(rows) - 1, len(cleaned)


def tracker_report(path):
    rows = read_table(path)
    headers = rows[0]
    if len(set(headers)) != len(headers) or "status" not in headers:
        raise ValueError("tracker requires unique headers including 'status'")
    index = headers.index("status")
    counts = Counter()
    for number, row in enumerate(rows[1:], start=2):
        status = row[index].strip().lower()
        if status not in STATUSES:
            raise ValueError(f"unknown status on row {number}; use a documented tracker state")
        counts[status] += 1
    lines = ["# Job-search snapshot", "", f"Total tracked opportunities: {sum(counts.values())}", "",
             "| Current status | Count |", "| --- | ---: |"]
    lines.extend(f"| {status} | {counts[status]} |" for status in sorted(STATUSES))
    lines.extend(["", "A snapshot of current entries, not weekly activity or conversion rates.",
                  "No company, contact, URL, dates, or free-text notes are included.",
                  "Counts can still be sensitive. Review before sharing.", ""])
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("init", help="create private trackers in .unfired without overwriting")
    budget = commands.add_parser("runway", help="simple constant cash-flow scenario")
    for flag in ("cash", "monthly-costs", "monthly-income", "reserve"):
        budget.add_argument("--" + flag, type=money, required=flag in {"cash", "monthly-costs"}, default=Decimal(0))
    for command, help_text in (("csv-clean", "normalize a UTF-8 comma-separated file"),
                               ("report", "aggregate current application statuses")):
        sub = commands.add_parser(command, help=help_text)
        sub.add_argument("input", type=Path)
        sub.add_argument("--out", type=Path, required=True, help="new output path; existing files are refused")
    args = parser.parse_args(argv)
    try:
        if args.command == "init":
            created = init_workspace(Path.cwd() / ".unfired")
            print("Created: " + ", ".join(created) if created else "Existing workspace preserved; no files overwritten.")
            print("Keep .unfired private. Files are not encrypted.")
        elif args.command == "runway":
            print(runway(args.cash, args.monthly_costs, args.monthly_income, args.reserve), end="")
        elif args.command == "csv-clean":
            content, before, after = clean_csv(args.input)
            write_new(args.out, content)
            print(f"Read {before} rows; wrote {after}. Formula-like cells prefixed with an apostrophe.")
        else:
            write_new(args.out, tracker_report(args.input))
            print("Wrote aggregate tracker snapshot. Review before sharing.")
    except (OSError, UnicodeError, csv.Error, ValueError, InvalidOperation) as exc:
        parser.exit(2, f"Error: {exc}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
