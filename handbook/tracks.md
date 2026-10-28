# Six tracks for studying and rebuilding systems

“Anything” is a direction for curiosity, not a promise that every system is suitable or permitted to copy. Choose a track, a narrow workflow, and a clear source record. This repo ships software labs; desktop and hardware work below are project routes, not supplied implementations.

## Web applications and interfaces

Start with one task, such as entering a form and exporting the result. Record fields, defaults, validation, keyboard interactions, loading/empty/error states, and persistence. On a site you own or have permission to inspect, browser DevTools can help explain the requests behind a visible action. Network exports may contain session tokens and private data; do not publish raw captures.

Write a state table, design an original interface, and test the task with keyboard input. Match necessary behavior and accessibility, not copied artwork, wording, or branding. First deliverable: a tested form with local storage and an open export. See [Chrome's Network tutorial](https://developer.chrome.com/docs/devtools/network).

## APIs and protocols

Specify method, path, headers, schema, defaults, error status/body, pagination, retries, idempotency, and ordering. Observe only authorized endpoints within permitted limits. Begin with the [local Quote API](../labs/quote_api/README.md), where no external authorization is needed.

A response body alone is insufficient: clients may depend on status, encoding, required fields, and state. First deliverable: contract fixtures plus a replacement passing them. Do not claim protocol-wide compatibility from a small endpoint suite.

## File formats and data portability

Obtain a user-owned or licensed export. Record encoding, delimiters, schema/version, identifiers, nested data, ordering, and unknown fields. Test Unicode, quotes, multiline values, empty records, and duplicate IDs. Preserve the source and reject unsupported data when omission would be silent.

First deliverable: a converter with expected output and semantic round-trip tests. Use [the board-format lab](../labs/board_format/README.md). A real migration must also account for attachments, access rights, relationships, and retention.

## Business workflows and automation

Interview a willing user about a repeated task. Build a decision table from public or original requirements: trigger, conditions, precedence, action, exception, human review. Keep generated outputs as previews until a person approves real actions.

First deliverable: a local rules engine with a documented fallback and tests for conflicting rules. Use [the ticket-routing lab](../labs/ticket_triage/README.md). Measure review effort and errors before choosing optional AI. Do not automate consequential decisions about people from a toy example.

## Desktop software and owned binaries

Prefer a command-line interface, public plugin format, or documented file export before inspecting internals. For an exercise in binary understanding, compile your own tiny program or use a training binary whose license permits the activity. Record source/license, compiler, build flags, architecture, and hash. Use strings, symbols, or a disassembler to compare a hypothesis with behavior, then write an original specification.

First deliverable: a short report and a reimplementation of your own small program's input/output behavior. [Ghidra's official repository](https://github.com/NationalSecurityAgency/ghidra) is a reference for analysis tooling. This track supplies no commercial-software crack, license-check bypass, protected-content extraction, or exploit exercise.

## Hardware, repair, and physical systems

Begin with a low-voltage educational device you own and are authorized to study, a public datasheet, and a non-destructive goal. Document connectors, signal levels, publicly specified interfaces, measurements, and uncertainty. Preserve original firmware/configuration where permitted and record changes. Seek experienced supervision where needed.

First deliverable: a repair note, public-interface adapter design, or simulation grounded in a datasheet. The repository includes no hardware implementation or firmware image. Mains-powered, battery-modifying, medical, automotive, and other safety-critical work needs specialist review and is outside these starter exercises. Ownership alone does not settle all firmware or circumvention rights.

For every track, use [provenance](../templates/provenance.md), [a contract](../templates/behavior-contract.md), [compatibility evidence](../templates/compatibility-matrix.md), and [a release gate](../templates/rebuild-release.md).
