# Choose one useful rebuild

The catalog contains **24 entries: four initial implementations and 20 proposals**. The working entries are the CSV cleaner and three synthetic teaching labs. They do not claim external commercial-product compatibility. All other entries require user validation and implementation.

Start with [the method](../handbook/method.md), [the curriculum](../handbook/curriculum.md), and [a project dossier](../tools/README.md). The machine-readable registry is [catalog.json](catalog.json).

| Project | Category | Status | First slice |
| --- | --- | --- | --- |
| [CSV Cleanroom](../tools/README.md) | file-format | initial tool | Normalize UTF-8 headers, trim cells, deduplicate rows |
| [Application Board](../templates/project-proposal.md) | web | proposal | Local entries with next action, CSV import/export |
| [Invoice Draft](../templates/project-proposal.md) | workflow | proposal | Local customer-entered line items and printable draft |
| [Scope Letter](../templates/project-proposal.md) | workflow | proposal | Markdown scope, milestones, exclusions, and handover |
| [Handover Kit](../templates/project-proposal.md) | workflow | proposal | Local templates for steps, access owners, and recovery |
| [Decision Notes](../templates/project-proposal.md) | workflow | proposal | Manual Markdown decision tags to an index |
| [Data Dictionary](../templates/project-proposal.md) | file-format | proposal | Generate editable field-name and sample-type documentation |
| [Checklist Pack](../templates/project-proposal.md) | workflow | proposal | Markdown checklist renderer with editable local templates |
| [Plain Diff](../templates/project-proposal.md) | desktop | proposal | Readable additions/deletions with downloadable plain text |
| [Accessibility Notes](../templates/project-proposal.md) | web | proposal | Local checklist with evidence and remediation notes |
| [Time Box](../templates/project-proposal.md) | desktop | proposal | Offline timer and optional local session notes |
| [Service Catalog](../templates/project-proposal.md) | workflow | proposal | Static Markdown offers with input, output, limits, and handover |
| [Quote API Compatibility](../labs/quote_api/README.md) | api | working teaching lab | Two arithmetic implementations and a loopback HTTP server |
| [Board Export Bridge](../labs/board_format/README.md) | file-format | working teaching lab | Strict CSV and versioned JSON converter |
| [Transparent Ticket Routing](../labs/ticket_triage/README.md) | workflow | working teaching lab | Deterministic local JSON routing preview |
| [Portable Form](../projects/briefs/portable-form.md) | web | proposal | Accessible fields with local save and JSON export |
| [Markdown Knowledge Shelf](../templates/project-proposal.md) | desktop | proposal | Local Markdown index and plain-text search |
| [Event Log Reader](../templates/project-proposal.md) | file-format | proposal | JSONL validation and summary with row errors |
| [Public API Adapter](../projects/briefs/public-api-adapter.md) | api | proposal | Adapter against a local mock and public contract |
| [Availability Rules](../templates/project-proposal.md) | workflow | proposal | Offline slot generation from explicit timezone and busy intervals |
| [Design Token Bridge](../templates/project-proposal.md) | file-format | proposal | Documented JSON tokens to CSS variables |
| [CLI Behavior Notebook](../templates/project-proposal.md) | desktop | proposal | Original tiny program plus input/output cases |
| [Sensor Interface Notes](../templates/project-proposal.md) | hardware | proposal | Datasheet-based simulator and measurement notebook |
| [Export Completeness Audit](../projects/briefs/export-audit.md) | file-format | proposal | Compare two supplied synthetic export manifests |

## Fuller starting briefs

[Portable Form](briefs/portable-form.md), [Export Completeness Audit](briefs/export-audit.md), and [Public API Adapter](briefs/public-api-adapter.md) each include implementation steps, acceptance criteria, suggested tests, exclusions, and risks. They remain proposals.

## Before choosing

Ask whether a real user needs the result, whether an existing project already solves it, whether sources and use are permitted, whether the output is portable, and whether someone can maintain it. Choose a narrow task rather than a brand to retaliate against.

Hardware and desktop analysis are included as learning routes and proposals. No firmware, hardware implementation, proprietary source, or unauthorized product capture is bundled. A green test for a teaching lab is not a production-readiness certificate.
