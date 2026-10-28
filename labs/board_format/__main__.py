import argparse
import csv
import json
from pathlib import Path

from labs.common import dump, write_new
from .codec import from_csv, to_csv


def main():
    parser = argparse.ArgumentParser(description="Convert the documented synthetic board export without data loss.")
    parser.add_argument("direction", choices=("from-csv", "to-csv"))
    parser.add_argument("input", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    try:
        text = args.input.read_text(encoding="utf-8")
        output = dump(from_csv(text)) if args.direction == "from-csv" else to_csv(json.loads(text))
        write_new(args.out, output)
    except (OSError, ValueError, UnicodeError, csv.Error) as exc:
        parser.exit(2, f"Error: {exc}\n")
    print("Converted to a new local file. Source preserved.")


if __name__ == "__main__":
    main()
