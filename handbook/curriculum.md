# A 12-week path from observation to an open release

Treat weeks as modules, not deadlines. About five hours per module is a starting budget; adjust scope and pace. Someone already experienced can skip to a deliverable they cannot yet demonstrate.

| Module | Learn and practice | Deliverable | Completion check |
| --- | --- | --- | --- |
| 1 | Git, local files, source permissions, synthetic data | A fork, short scope, provenance record | Another person can understand the task and sources |
| 2 | Controlled observation and boundary inputs | Observation log with five contrasting cases | Observations are distinguished from hypotheses |
| 3 | Schemas, validation, error behavior, precision | Behavior contract for one workflow | Every advertised output has an acceptance criterion |
| 4 | HTTP request/response behavior | [Quote API lab](../labs/quote_api/README.md) notes and one added fixture | A deliberate rounding bug is detected |
| 5 | CSV, JSON, encoding, schema versions | [Board-format lab](../labs/board_format/README.md) round trip | Unicode, multiline text, IDs, and order survive |
| 6 | Decision tables and rule precedence | [Routing lab](../labs/ticket_triage/README.md) extension | Urgent and unknown cases still follow the contract |
| 7 | User interviews and existing alternatives | A small project proposal | A willing user confirms the task is useful |
| 8 | Independent implementation and simple architecture | A runnable core slice | It works without paid APIs or hidden manual fixes |
| 9 | Compatibility testing and negative cases | Fixtures and a compatibility matrix | A new reviewer reproduces the result |
| 10 | Portability and rollback | Migration plan and dry run | Original data survives; unsupported fields stop the migration |
| 11 | Usability, documentation, privacy, licensing | A fresh-user setup run and notices | Setup, task, export, and removal are understandable |
| 12 | Versioning, release, support, contribution | A bounded release and honest case study | Scope and limitations match what actually runs |

## Skills by role

- **Research/product:** observe, interview, write requirements, and identify uncertainty.
- **Developer:** implement a contract, validate inputs, handle errors, and provide export.
- **QA:** create counterexamples, independent expected results, and reproducible reports.
- **Design/accessibility:** test the main task and build an original usable interface.
- **Writer/translator:** help a new person complete setup and understand limitations.
- **Maintainer:** review provenance, license, reproducibility, release, and handover.

## Free primary learning references

[Python tutorial](https://docs.python.org/3/tutorial/) for people with basic programming familiarity; [Python beginner guidance](https://www.python.org/about/gettingstarted/) for starting out; [MDN Learn](https://developer.mozilla.org/en-US/docs/Learn_web_development) for the web; [Pro Git](https://git-scm.com/book/en/v2) for collaboration; and [W3C accessibility tutorials](https://www.w3.org/WAI/tutorials/) for usable interaction.

Do not spend the whole period watching courses. Each module ends with an artifact someone else can inspect. A learning route does not guarantee employment or make a person immune to changing work.
