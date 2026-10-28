# Proposal: Portable Form

Status: proposal, no implementation. Category: web. User: a volunteer organizer preparing a small local form. This is an original workflow brief, not a claim to replace a named form platform.

## First version

Build a single-device form editor with text, multiline text, checkbox, and single-choice fields. Save the form definition locally. A preview allows keyboard completion, validates required fields, and exports a versioned JSON response. Use invented sample responses only.

## Steps

1. Ask willing organizers to describe one non-sensitive collection task.
2. Define field IDs, allowed types, defaults, validation, schema version, and export.
3. Implement an original accessible interface without external scripts or account requirements.
4. Store locally with a visible explanation and an explicit clear-data action.
5. Test refresh recovery, keyboard flow, required fields, Unicode, and full export.
6. Document the single-device limit and how users can remove their data.

## Acceptance

A new user can create a three-field form, complete it by keyboard, reload without losing the definition, and export all field IDs and answers. Invalid required fields show connected explanatory errors. Export is versioned; unknown field types fail rather than disappear. No network request is required for the core flow.

## Exclusions and risks

No public collection endpoint, authentication, multi-user sync, payments, encryption claim, or sensitive-data suitability. Browser storage may be cleared or accessible to other device users. Before any hosted collection feature, design and review privacy, abuse controls, access, retention, and operational support separately.

Suggested tests: empty form; duplicate field ID; Unicode; unknown schema version; import/export round trip; storage unavailable; screen-reader labels; keyboard-only task. Start with [a project dossier](../../tools/README.md), [the web track](../../handbook/tracks.md), and [provenance](../../templates/provenance.md).
