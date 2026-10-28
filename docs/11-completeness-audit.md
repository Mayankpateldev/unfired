# Completeness audit: why v0.1 felt unfinished

The original repository delivered a recovery kit but did not adequately implement the broader request: a movement for understanding systems and building open alternatives. The gaps were in scope and practical evidence, not just file count.

| Gap in v0.1 | Delivered in v0.2 | How to inspect it |
| --- | --- | --- |
| README led with job loss rather than rebuilding | Repositioned front page with build, lab, learning, and recovery routes | [README](../README.md) |
| No end-to-end observation/specification process | A rebuild method and six domain tracks | [Method](../handbook/method.md), [tracks](../handbook/tracks.md) |
| No API compatibility example | Original reference, replacement, HTTP server, contract, 18 golden cases | [API lab](../labs/quote_api/README.md) |
| No migration implementation | Strict CSV ↔ versioned JSON converter with expected output and round-trip tests | [Format lab](../labs/board_format/README.md) |
| No workflow reconstruction example | Deterministic local routing with precedence, fallback, and expected output | [Workflow lab](../labs/ticket_triage/README.md) |
| Project creation was a blank-page task | Ten-file draft dossier generator with overwrite protection | [Scaffolder instructions](../tools/README.md) |
| Too little evidence for compatibility and exit | Observation, contract, matrix, migration, case-study, and release templates | [Templates](../templates/README.md) |
| No reusable result comparator | Strict JSON comparison with mismatch exit codes, pointer paths, and overwrite protection | [Comparator usage](../tools/README.md) |
| Learning was disconnected from rebuilding | Twelve modules tied to concrete deliverables | [Curriculum](../handbook/curriculum.md) |
| Catalog was narrow and mostly generic | 24 categorized entries, three fuller proposal briefs, and separate lab registry | [Projects](../projects/README.md), [lab registry](../labs/catalog.json) |
| Little guidance on AI evaluation and reuse tradeoffs | AI workflow, tool references, licensing, and existing-project pointers | [Handbook index](../handbook/README.md) |
| Contribution and maintenance expectations were scattered | Support routes, governance stages, research/review sequence | [Support](../SUPPORT.md), [governance](../GOVERNANCE.md), [contributing](../CONTRIBUTING.md) |

## Verification

`python3 -m labs.verify` checks 18 API fixtures plus the board expected-output/round-trip and routing expected-output cases. The unit suite covers HTTP behavior, rounding, file preservation, invalid schemas, rule precedence, private-workspace behavior, and scaffold validation. `scripts/check_repo.py` checks local document targets and both registries. GitHub Actions runs the same unit suite and repository check on Python 3.10 and 3.14.

## What remains honestly unfinished

The 20 proposed products are not implemented. No commercial product has been fully reverse-engineered by these labs. No hardware lab, production SaaS, vendor-specific migration, user-validation study, independently audited clean-room implementation, translation review, benchmark, or funded support program is claimed. Those are distinct projects requiring actual work and evidence.

Version 0.2 supplies a coherent method and runnable foundations for the movement. A file list, unchecked idea, or passing toy fixture is not counted as a finished customer product.
