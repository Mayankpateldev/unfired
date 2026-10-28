# Migration and rollback plan

- User-owned source export and authorization:
- Source backup and integrity check:
- Field mapping, types, encodings, and identifiers:
- Preserved information:
- Intentionally transformed information and user approval:
- Unsupported fields and stop conditions:
- Dry-run commands and expected counts:
- Destination validation and representative manual checks:
- Cutover owner and steps:
- Rollback trigger and exact restore steps:
- Retention/deletion plan for private working files:
- User documentation and handover:

Prefer a new destination. Never destroy the only source copy or silently omit unsupported data.
