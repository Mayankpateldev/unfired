# Proposal: Export Completeness Audit

Status: proposal, no implementation. Category: file-format. User: someone moving their own records between systems. Task: compare two manifests before trusting a migration.

## First version

Accept source and destination JSON manifests containing a schema version and an array of record IDs with a declared field-name set. Report missing/extra IDs, missing/extra field names, and counts. Make no network calls. Do not modify either manifest.

## Steps

1. Define the manifest schema and explain that it contains identifiers and field names, not full customer records.
2. Reject malformed versions, duplicate IDs, and unknown fields.
3. Compare IDs as sets while producing deterministically sorted output.
4. Distinguish “missing,” “extra,” and “not compared”; do not treat counts alone as proof.
5. Write a machine-readable report to a new path and an exit code suitable for CI.
6. Add a handover note explaining how the user creates authorized manifests and protects their identifiers.

## Acceptance

A fixture with one missing source record, one extra destination record, and one missing field reports each exactly once. Equal counts with different IDs still fail. Unknown versions and duplicate IDs stop the comparison. Existing output files and inputs remain untouched. A clean case has an explicit pass result.

## Exclusions and risks

No account connection, automatic deletion, record-value comparison, attachment verification, or universal vendor support. A passing manifest comparison does not prove equal values or permissions. Identifiers can still be private. Start with [the format lab](../../labs/board_format/README.md) and [migration guidance](../../handbook/compatibility.md).
