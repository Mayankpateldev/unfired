# Lab 2: recover portable data from a documented export

Goal: understand a schema, preserve its information, and prove a round trip. The format is invented for this exercise; it does not claim compatibility with a named task-management product.

```bash
python3 -m labs.board_format from-csv labs/board_format/fixtures/cards.csv --out output/board.json
python3 -m labs.board_format to-csv output/board.json --out output/board-roundtrip.csv
python3 -m labs.verify
```

Choose new output names when repeating the commands. Existing files are refused. Original input is never modified. Files are loaded into memory; this is a small-file exercise.

## What to inspect

Read the CSV fixture in a text editor. It includes commas, quotes, Unicode, a multiline title, and labels encoded as a JSON array inside one CSV cell. Guessing `split(',')` is insufficient. Write observations, then compare them with [SPEC.md](SPEC.md).

The converter is strict: an unknown field, version, invalid state, malformed label list, or duplicate ID causes rejection. This protects against silent data loss. The expected JSON fixture is stored independently in [expected.json](fixtures/expected.json).

## Your exercise

1. Add a synthetic card with non-Latin text and multiple labels.
2. Convert CSV → JSON → CSV → JSON.
3. Compare semantic values, card order, labels, and IDs. CSV whitespace/quoting bytes can differ without data loss.
4. Add an unknown column. Confirm conversion fails rather than silently dropping it.
5. Write a migration note listing preserved and unsupported fields, source backup, and rollback.

CSV output preserves field values, including formula-like titles. It is an interchange file, not a spreadsheet-sanitized export. Use a text editor or import fields explicitly as text; do not assume quoting alone prevents spreadsheet formula execution.

No task service is contacted. There are no attachments, comments, users, or permissions in this teaching schema. Real migrations need a field-by-field inventory and separate authorization for personal data.
