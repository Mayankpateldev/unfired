# Unfired local toolkit

Run from the repository root with Python 3.10+. Only the Python standard library is used. No installation, network requests, telemetry, or AI service is involved. Input files are loaded into memory; use small files, not huge datasets.

For the runnable local API, migration, and workflow examples, see [the three labs](../labs/README.md). The API lab opens a loopback HTTP listener; the file utilities described here make no network calls.

## Scaffold an original rebuild project

```bash
python3 tools/new_project.py demo-tool --category api --out output/demo-tool
```

Creates ten draft dossier files in a new directory, including contract, observation, compatibility, provenance, release, fixture/test instructions, MIT license, README, and ignore rules. Categories: api, web, file-format, workflow, desktop, hardware. Names must be lowercase hyphen-separated slugs, at most 64 characters. Existing directories are refused. No implementation or passing placeholder tests are generated; fill the dossier and implement the task yourself.

## Compare independent expected and actual JSON

After converting the board fixture with the command in [the format lab](../labs/board_format/README.md):

```bash
python3 tools/compare_json.py labs/board_format/fixtures/expected.json output/board.json --out output/comparison.json
```

Exit code **0** means a structural match; **1** means differences; **2** means invalid input or a file error. Existing reports are refused. Duplicate object keys and non-finite numbers are rejected. Object-key order is ignored, array order matters, and types are strict (`1`, `1.0`, and `true` differ). No ignored fields, numeric tolerances, timestamp normalization, or binary-file comparison is implied.

The report contains JSON Pointer paths and difference kinds, but no input values. The empty path means the document root; `~` and `/` in keys are escaped. Field names and counts can still reveal information, so reports remain private by default. A matching JSON result is evidence for that output only; it does not prove complete API or product compatibility.

## Private workspace

```bash
python3 tools/unfired.py init
```

Creates `.unfired/applications.csv`, `.unfired/budget.csv`, and `.unfired/weekly-plan.md` in your current directory. Running it again preserves existing files. `.gitignore` excludes this directory in this repository; if you move files elsewhere, that protection does not automatically follow. Files are ordinary unencrypted text.

## Runway scenario

```bash
python3 tools/unfired.py runway --cash 9000 --monthly-costs 2500 --monthly-income 500 --reserve 1000
```

Formula: `(cash - reserve) / (monthly costs - monthly income)` when the gap is positive. Non-negative finite amounts only; reserve must not exceed cash. Decimal values use a period, without currency symbols or thousands separators. The CLI prints a scenario, not tax, benefit, debt, or investment advice. See [the planning guide](../docs/02-runway-and-income.md).

## CSV cleaner: a small free alternative

```bash
python3 tools/unfired.py csv-clean examples/messy-contacts.csv --out output/clean-contacts.csv
```

Accepts UTF-8 (with optional BOM), comma delimiters, a header, and equally sized rows. It lowercases headers and replaces punctuation/spacing with underscores, trims cell edges, drops all-empty rows, and removes duplicate rows after transformation. It preserves the first occurrence's order. It refuses empty/colliding normalized headers and malformed rows.

Formula-like values beginning with `=`, `+`, `-`, or `@` after trimming receive a leading apostrophe, including negative numbers. This intentionally changes values and is a basic import precaution, not a guarantee for all spreadsheet programs. Choose a different tool if you need lossless values, type inference, other encodings/delimiters, huge files, or automatic merge semantics. No enrichment, external uploads, or contact verification occurs.

The synthetic example has three input rows and two unique output rows. Names and addresses are invented. [Provenance](../examples/provenance-csv-cleaner.md).

## Job-search snapshot

```bash
python3 tools/unfired.py report examples/applications.csv --out output/demo-summary.md
python3 tools/unfired.py report .unfired/applications.csv --out output/private-summary.md
```

Requires unique headers including `status`. Allowed states: `researching`, `applied`, `conversation`, `interview`, `offer`, `closed`; surrounding spaces/case are normalized. Unknown or empty statuses are rejected. Header-only trackers produce a zero-count report.

The report is a current-state aggregate. It does not validate other tracker fields, calculate conversion rates, identify overdue follow-ups, or reconstruct weekly activity. Company names, roles, dates, URLs, and notes are omitted. Counts may still be private; keep generated reports private unless deliberately sharing.

## File protection and errors

All output files must be new paths. Existing files, including input files and symlink targets at the output path, are refused. Parent directories are created automatically. Errors exit with code 2. Input content is never modified. This is not an encryption, anonymization, or comprehensive data-sanitization system.
