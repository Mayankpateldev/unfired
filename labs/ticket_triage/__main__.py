import argparse
import json
from pathlib import Path

from labs.common import dump, write_new
from .rules import route


def main():
    parser = argparse.ArgumentParser(description="Preview deterministic routing for a local synthetic ticket export.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    try:
        output = route(json.loads(args.input.read_text(encoding="utf-8")))
        write_new(args.out, dump(output))
    except (OSError, UnicodeError, ValueError) as exc:
        parser.exit(2, f"Error: {exc}\n")
    print("Created a routing preview. No ticket was sent or modified.")


if __name__ == "__main__":
    main()
