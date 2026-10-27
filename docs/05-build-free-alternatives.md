# Build a free alternative people actually want

The goal is to make a useful workflow accessible. Start with a user problem, not a former employer's implementation or a promise to replace an entire platform.

## A repeatable two-week experiment

1. **Day 1–2: listen.** Talk to three potential users who freely agree. Ask what task they repeat, what input they own, what output they need, and what goes wrong today. Do not collect confidential records.
2. **Day 3: scope.** Choose one user, one input, and one output. Write a [project proposal](../templates/project-proposal.md). Document your public sources in a [provenance record](../templates/provenance.md).
3. **Day 4–7: implement.** Use a local script or small application. Prefer ordinary file formats and synthetic fixtures. Build error handling and export before optional AI features.
4. **Day 8–10: test.** Ask users to perform the task without coaching. Note where they struggle. Verify empty inputs, malformed data, Unicode, privacy, accessibility where relevant, and destructive-action protections.
5. **Day 11–12: document.** State setup, limits, costs, dependency licenses, data handling, backup/restore, and how to leave the tool.
6. **Day 13–14: share.** Release a small demo with synthetic data, invite specific feedback, and decide whether the need justifies maintenance.

The schedule is optional. A job search, health, and income can take priority.

## Pick a small first tool

| Need | First slice | Leave out initially |
| --- | --- | --- |
| Clean exports | Normalize a CSV and remove exact duplicates | Connectors, accounts, enrichment |
| Prepare weekly updates | Summarize a local structured tracker | Automatic sending and private integrations |
| Reuse checklists | Render a Markdown checklist from a template | Workflow engines and approval automation |
| Track applications | Local entries, next action, CSV export | Scraping jobs and automated applications |

The first two slices are available in [the CLI](../tools/README.md). Other ideas are in [the catalog](../projects/README.md).

## Definition of done

- A new user can complete the advertised task from a clean checkout.
- Inputs and outputs are documented and exportable in an open format.
- Examples contain synthetic data. Tests cover a meaningful failure and the main result.
- There is no requirement for a paid service to run the core feature.
- Any hosted or AI option has an explicit cost and data-handling description.
- License, dependency notices, source provenance, limitations, and a support route exist.
- Claims match actual capabilities. A prototype is labelled a prototype.

## Compete on trust

Offer clear migration from authorized user exports, predictable behavior, a small installation, and honest limitations. Publish comparisons only when reproducible and current; describe the exact feature and version tested. Do not impersonate competitors, copy branding, or suggest affiliation.

Remember that free software can still cost time and money to operate. Say “free source and local execution” when that is what you provide. Your [maintenance plan](07-community-and-sustainability.md) is part of the product.
