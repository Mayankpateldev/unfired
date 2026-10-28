# Prove the behavior you advertise

Compatibility is a set of observed agreements under stated conditions. Start by naming a reference version, replacement version, environment, allowed observation scope, and the specific workflows covered.

## Build a useful fixture set

Use at least one happy path, empty input, malformed input, boundary value, unknown field, Unicode/encoding case, repeated operation, and relevant state transition. Not every category applies to every tool; document the reason for exclusions.

Expected results should come from public requirements, authorized observations, hand calculations, or independent review. Generating expectations with the replacement itself can preserve the same bug twice. Keep fixture IDs stable and inputs synthetic.

| Pitfall | A test that catches it |
| --- | --- |
| Rounding at the wrong step | A half-unit discount and tax case |
| Parsing CSV with a string split | A quoted comma and multiline field |
| Treating booleans as integers | A true/false numeric field input |
| Checking rules in the wrong order | Urgent ticket with a billing topic |
| Dropping unknown data silently | Extra column or unsupported format version |
| Testing only the response body | Status, content type, and malformed JSON checks |
| Making a migration irreversible | A round trip and source-preservation check |

The supplied labs and tests cover these examples. They are finite teaching cases; list gaps instead of claiming exhaustive coverage.

## Differential and golden checks

A differential check compares reference and replacement. A golden check compares each to an independent expected result. Use both where possible. Two implementations can agree on a wrong answer. Record actual outputs and unsupported cases in [the matrix](../templates/compatibility-matrix.md).

For a UI, compare task completion, keyboard flow, validation, and export. Screenshots alone do not prove correct persistence or calculations. For APIs, document the supported subset rather than “drop-in” unless client-level evidence supports that claim.

## Migration is part of the product

1. Obtain a source export the user is authorized to use; keep an untouched backup.
2. Inventory fields, relationships, attachments, permissions, and IDs.
3. Define mappings and explicit stop conditions for unsupported information.
4. Dry-run to a new destination; compare counts and representative values.
5. Test import/export or a semantic round trip where possible.
6. Ask the user to review intentional changes and losses.
7. Cut over only with a documented rollback and owner.

Use [the migration template](../templates/migration-plan.md). A converter that works on a toy fixture is not automatically ready for private production data or every vendor export.
