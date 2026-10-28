#!/usr/bin/env python3
"""Strict structural JSON comparison with value-free diagnostics. SPDX-License-Identifier: MIT."""

import argparse
import json
import math
from pathlib import Path


def compare(expected, actual, pointer=""):
    differences = []

    def add(path, kind):
        differences.append({"path": path, "kind": kind})

    def child(path, part):
        return path + "/" + str(part).replace("~", "~0").replace("/", "~1")

    if type(expected) is not type(actual):
        add(pointer, "type_mismatch")
    elif isinstance(expected, dict):
        for key in sorted(expected.keys() - actual.keys()):
            add(child(pointer, key), "missing_key")
        for key in sorted(actual.keys() - expected.keys()):
            add(child(pointer, key), "extra_key")
        for key in sorted(expected.keys() & actual.keys()):
            differences.extend(compare(expected[key], actual[key], child(pointer, key)))
    elif isinstance(expected, list):
        for index in range(max(len(expected), len(actual))):
            path = child(pointer, index)
            if index >= len(actual):
                add(path, "missing_item")
            elif index >= len(expected):
                add(path, "extra_item")
            else:
                differences.extend(compare(expected[index], actual[index], path))
    elif expected != actual:
        add(pointer, "value_mismatch")
    return differences


def read_json(path):
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON object key")
            result[key] = value
        return result

    def reject_constant(value):
        raise ValueError("non-finite JSON numbers are unsupported")

    def finite_float(value):
        number = float(value)
        if not math.isfinite(number):
            raise ValueError("non-finite JSON numbers are unsupported")
        return number

    return json.loads(Path(path).read_text(encoding="utf-8-sig"), object_pairs_hook=unique_object,
                      parse_constant=reject_constant, parse_float=finite_float)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("expected", type=Path)
    parser.add_argument("actual", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    try:
        differences = compare(read_json(args.expected), read_json(args.actual))
        report = json.dumps({"equal": not differences, "differences": differences}, indent=2) + "\n"
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("x", encoding="utf-8") as stream:
            stream.write(report)
    except (OSError, ValueError, UnicodeError, RecursionError) as exc:
        parser.exit(2, f"Error: {exc}\n")
    print("MATCH" if not differences else f"MISMATCH: {len(differences)} structural differences")
    return 0 if not differences else 1


if __name__ == "__main__":
    raise SystemExit(main())
