#!/usr/bin/env python3
"""Check local Markdown/SVG links and project catalog shape without networking."""

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {".git", ".unfired", "output", "__pycache__", ".venv"}


def main():
    errors = []
    files = [p for p in ROOT.rglob("*.md") if not EXCLUDED.intersection(p.relative_to(ROOT).parts)]
    for path in files:
        text = path.read_text(encoding="utf-8")
        targets = re.findall(r"\]\(([^)]+)\)", text) + re.findall(r'<img\s+src="([^"]+)"', text)
        for raw in targets:
            target = unquote(raw.split("#", 1)[0])
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            if not (path.parent / target).exists():
                errors.append(f"{path.relative_to(ROOT)}: missing local link {raw}")
    catalog = json.loads((ROOT / "projects/catalog.json").read_text())
    ids = set()
    required = {"id", "name", "status", "user", "task", "mvp", "acceptance", "excludes"}
    for project in catalog["projects"]:
        if not required.issubset(project):
            errors.append(f"catalog entry missing fields: {project.get('id', '?')}")
        if project["id"] in ids:
            errors.append(f"duplicate catalog id: {project['id']}")
        ids.add(project["id"])
        if project["status"] not in {"proposal", "initial-implementation"}:
            errors.append(f"invalid catalog status: {project['id']}")
        if not project["acceptance"] or not project["excludes"]:
            errors.append(f"catalog needs acceptance and exclusions: {project['id']}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Checked {len(files)} Markdown files and {len(ids)} catalog entries; local targets exist.")
    print("External URLs, Markdown anchors, and factual accuracy are not checked by this script.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
