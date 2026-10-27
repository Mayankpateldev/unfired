# Provenance: initial CSV cleaner

- Date: 2026-10-27.
- Need: normalize an authorized CSV export locally without a subscription.
- Implementation: original Python standard-library program prepared with AI assistance; human maintainer review is invited before release.
- API references: [Python csv](https://docs.python.org/3/library/csv.html), [argparse](https://docs.python.org/3/library/argparse.html), and [pathlib](https://docs.python.org/3/library/pathlib.html).
- Runtime dependencies: Python standard library only; no vendored dependencies or third-party code.
- Test data: invented names, reserved example domains, and synthetic edge cases.
- Proprietary observations or materials: none used.
- Known limits: comma-separated UTF-8 input; whole file loaded into memory; trims cells and changes formula-like values with an apostrophe; not a full spreadsheet sanitization guarantee.
- Rights review: no specific competing product or proprietary implementation was studied. This record does not assert universal IP clearance.
