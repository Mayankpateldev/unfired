#!/usr/bin/env python3
"""Generate a source-first project dossier, not an implementation. SPDX-License-Identifier: MIT."""

import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ("api", "web", "file-format", "workflow", "desktop", "hardware")


def scaffold(name, category, out):
    if not re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", name) or len(name) > 64:
        raise ValueError("name must be a lowercase hyphen-separated slug, at most 64 characters")
    if category not in CATEGORIES:
        raise ValueError("unknown category")
    out = Path(out)
    files = {
        "README.md": f"# {name}\n\nStatus: draft dossier; no implementation or compatibility claim.\n\nCategory: {category}.\n\nDescribe one user, one input, and one output. Fill SPEC.md, PROVENANCE.md, OBSERVATIONS.md, COMPATIBILITY.md, and RELEASE-CHECKLIST.md before proposing a release.\n\nLicense: MIT; preserve third-party rights and notices separately.\n",
        "SPEC.md": "# Public behavior contract\n\n## Problem and user\n\nTODO\n\n## Inputs, validation, outputs, and errors\n\nTODO\n\n## Ordering, rounding, encoding, and state\n\nTODO\n\n## Explicit exclusions\n\nTODO\n",
        "OBSERVATIONS.md": "# Observations\n\nUse synthetic inputs and permitted sources only.\n\n| ID | Source / permission | Input | Observed output | Hypothesis | Confidence |\n| --- | --- | --- | --- | --- | --- |\n",
        "COMPATIBILITY.md": "# Compatibility\n\nStatus: untested. No compatibility claim.\n\n| Case ID | Requirement | Expected output / status | Actual result | Result |\n| --- | --- | --- | --- | --- |\n\n## Unsupported behavior\n\nTODO\n\n## Migration and rollback\n\nTODO\n",
        "PROVENANCE.md": (ROOT / "templates/provenance.md").read_text(encoding="utf-8"),
        "RELEASE-CHECKLIST.md": (ROOT / "templates/rebuild-release.md").read_text(encoding="utf-8"),
        "fixtures/README.md": "# Fixtures\n\nAdd small synthetic inputs and independently specified expected outputs. Do not derive every expected result from the replacement implementation. Record source and rights for any externally obtained material.\n",
        "tests/README.md": "# Tests to implement\n\nAdd runnable tests for the main result, errors, edge cases, and data-preserving migration. No placeholder passing tests are generated. A dossier is not a finished tool.\n",
        "LICENSE": (ROOT / "LICENSE").read_text(encoding="utf-8"),
        ".gitignore": ".env\n.env.*\nprivate/\noutput/\n__pycache__/\n",
    }
    # Exclusive directory creation prevents accidentally replacing an existing project.
    out.mkdir(parents=True, exist_ok=False)
    for relative, text in files.items():
        path = out / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return len(files)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name")
    parser.add_argument("--category", choices=CATEGORIES, required=True)
    parser.add_argument("--out", required=True, type=Path, help="a new directory; existing directories are refused")
    args = parser.parse_args()
    try:
        count = scaffold(args.name, args.category, args.out)
    except (OSError, UnicodeError, ValueError) as exc:
        parser.exit(2, f"Error: {exc}\n")
    print(f"Created {count} dossier files. Status: draft; implementation and verification still required.")


if __name__ == "__main__":
    main()
