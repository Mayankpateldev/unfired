#!/usr/bin/env python3
"""Check local document targets and project/lab registries without networking."""

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
    required = {"id", "name", "status", "user", "task", "mvp", "acceptance", "excludes",
                "category", "kind", "effort", "start_here"}
    categories = {"api", "web", "file-format", "workflow", "desktop", "hardware"}
    if catalog.get("schema_version") != 2:
        errors.append("project catalog must use schema version 2")
    for project in catalog["projects"]:
        if not required.issubset(project):
            errors.append(f"catalog entry missing fields: {project.get('id', '?')}")
            continue
        if project["id"] in ids:
            errors.append(f"duplicate catalog id: {project['id']}")
        ids.add(project["id"])
        if project["status"] not in {"proposal", "initial-implementation"}:
            errors.append(f"invalid catalog status: {project['id']}")
        if not project["acceptance"] or not project["excludes"]:
            errors.append(f"catalog needs acceptance and exclusions: {project['id']}")
        if project["category"] not in categories or project["kind"] not in {"tool", "proposal", "teaching-lab"}:
            errors.append(f"invalid category or kind: {project['id']}")
        if project["kind"] == "proposal" and project["status"] != "proposal":
            errors.append(f"proposal must not claim implementation status: {project['id']}")
        if not (ROOT / project["start_here"]).is_file():
            errors.append(f"missing catalog entry point: {project['id']}")
    lab_catalog = json.loads((ROOT / "labs/catalog.json").read_text())
    lab_ids = set()
    for lab in lab_catalog["labs"]:
        if lab["id"] in lab_ids or lab["kind"] != "synthetic-teaching-lab":
            errors.append(f"duplicate or invalid teaching lab: {lab['id']}")
        lab_ids.add(lab["id"])
        if not lab["fixtures"]:
            errors.append(f"lab needs fixtures: {lab['id']}")
        for relative in [lab["readme"], lab["spec"], *lab["fixtures"]]:
            if not (ROOT / relative).is_file():
                errors.append(f"lab {lab['id']} missing {relative}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Checked {len(files)} Markdown files, {len(ids)} project entries, and {len(lab_ids)} labs; local targets exist.")
    print("External URLs, Markdown anchors, and factual accuracy are not checked by this script.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
