<div align="center">

<img src="assets/unfired-banner.svg" alt="Unfired. Understand how it works. Build it open." width="100%">

# UNFIRED

**Understand how it works. Build it open. Make it accessible.**

An open-source movement for studying useful systems, rebuilding their behavior independently, and giving people tools they can own.

[Start building](handbook/README.md) · [Run the labs](labs/README.md) · [Choose a project](projects/README.md) · [Learn](handbook/curriculum.md) · [Layoff support](docs/01-first-72-hours.md)

[![Checks](https://github.com/Mayankpateldev/unfired/actions/workflows/checks.yml/badge.svg)](https://github.com/Mayankpateldev/unfired/actions/workflows/checks.yml)
![MIT](https://img.shields.io/badge/license-MIT-96f56a)
![Dependencies](https://img.shields.io/badge/Python_dependencies-zero-96f56a)
![Stage](https://img.shields.io/badge/stage-working_labs_%2B_project_incubator-ffba69)

</div>

## The idea

Years of learning do not disappear when a role ends. Use that experience to understand a problem, study observable behavior through permitted sources, and build an original alternative that people can run, inspect, modify, and leave with their data.

**Observe → specify → rebuild → verify → share.**

The scope includes applications, APIs, file formats, business workflows, desktop tools, and public hardware interfaces. The [six tracks](handbook/tracks.md) explain how to start and what evidence each needs. We welcome people in any employment situation. Layoff recovery remains a dedicated track, rather than the whole project.

## Start in five minutes

Clone once, then run from the repository root. Python 3.10+; no packages, account, paid model, or API key required for the labs.

```bash
git clone https://github.com/Mayankpateldev/unfired.git
cd unfired

# Compare reference/replacement behavior and replay the migration/workflow fixtures.
python3 -m labs.verify

# Run behavioral, HTTP, round-trip, overwrite, and scaffold tests.
python3 -m unittest discover -s tests -v

# Validate local document links and the project/lab registries.
python3 scripts/check_repo.py
```

The fixture replay should report **20/20 checks passed**. It proves agreement on the supplied teaching cases, not universal compatibility with an external product. HTTP tests open loopback ports; restricted environments must allow local loopback binding.

## Three working rebuild labs

| Lab | Run / try | What it teaches |
| --- | --- | --- |
| [API compatibility](labs/quote_api/README.md) | `python3 -m labs.quote_api.server --implementation replacement --port 8765` | HTTP contracts, errors, rounding, and two implementation strategies |
| [File-format migration](labs/board_format/README.md) | `python3 -m labs.board_format from-csv labs/board_format/fixtures/cards.csv --out output/board.json` | Unicode, quoted fields, schema versions, and data-preserving round trips |
| [Workflow reconstruction](labs/ticket_triage/README.md) | `python3 -m labs.ticket_triage labs/ticket_triage/fixtures/input.json --out output/triage.json` | Rule precedence, human-review routing, and explicit fallbacks |

All three have written contracts, synthetic inputs, expected outputs, implementations, and tests. They are original educational systems created here, not commercial products we have reverse-engineered. The API server is a loopback teaching service, not a production billing or tax service. File commands refuse existing output paths; use a new path to rerun.

## Turn an idea into a reviewable project

```bash
python3 tools/new_project.py my-open-tool --category workflow --out output/my-open-tool
```

This generates ten dossier files: scope, contract, observations, compatibility, provenance, release checklist, fixture/test instructions, license, and ignore rules. It is clearly marked **draft**, with no pretend implementation or passing placeholder tests. Replace `workflow` with `api`, `web`, `file-format`, `desktop`, or `hardware` as appropriate.

Follow [the method](handbook/method.md), choose from [24 scoped catalog entries](projects/README.md), and use the [12-week curriculum](handbook/curriculum.md) to fill skill gaps. The catalog contains **four initial implementations** (the CSV cleaner and three teaching labs) and **20 proposals**. Proposals are not finished software.

## What to read next

| You want to… | Go here | Leave with |
| --- | --- | --- |
| Understand how to study a system | [Rebuild method](handbook/method.md) | Observations separated from hypotheses |
| Pick a domain | [Six tracks](handbook/tracks.md) | One narrow workflow and a first deliverable |
| Choose tools | [Tools and primary references](handbook/tools.md) | A tool for a specific question |
| Prove a replacement works | [Compatibility and migration](handbook/compatibility.md) | Golden cases, a matrix, and rollback steps |
| Use AI without trusting guesses | [AI workflow](handbook/ai-workflow.md) | A reviewed implementation and honest evaluation |
| Understand open-source tradeoffs | [Licensing guide](handbook/licensing.md) | A deliberate reuse policy and notices |
| Release something maintainable | [Release guide](handbook/release.md) | Setup, export, costs, support limits, and handover |
| Contribute to an existing alternative | [Existing projects](handbook/existing-projects.md) | A useful gap before starting a new platform |
| Recover after a layoff | [First 72 hours](docs/01-first-72-hours.md), [90-day plan](docs/09-90-day-plan.md) | Immediate next steps and a sustainable plan |

## What makes a rebuild useful

A clear user problem. Public or authorized sources. Original implementation. Reproducible behavior checks. Open export. A practical migration and exit. Honest costs and maintenance limits.

Use your skills and public knowledge; keep employer code, confidential designs, customer records, credentials, and unauthorized captures out. Whether a particular reverse-engineering activity is permitted depends on the source, agreements, rights, and location. [Independent-development guidance](docs/06-independent-development.md) explains the project process; it does not give blanket legal clearance.

## Recovery tools are still here

```bash
python3 tools/unfired.py init
python3 tools/unfired.py runway --cash 9000 --monthly-costs 2500 --monthly-income 500 --reserve 1000
python3 tools/unfired.py csv-clean examples/messy-contacts.csv --out output/clean-contacts.csv
python3 tools/unfired.py report .unfired/applications.csv --out output/search-summary.md
```

See [tool documentation](tools/README.md), [job-search materials](docs/03-job-search.md), and [four-week learning paths](docs/04-learning-paths.md). `.unfired/` and `output/` are ignored by Git here but are not encrypted. Do not commit personal records. Cash scenarios are simplified planning aids, not personalized financial guidance.

## Build the movement

Read [the manifesto](community/manifesto.md). Start with one lab, one observation, one bug fix, one translation, or one useful project proposal. [Contributing](CONTRIBUTING.md) explains how research, design, QA, writing, and code fit together. [Support](SUPPORT.md), [governance](GOVERNANCE.md), and [the roadmap](ROADMAP.md) explain what to expect.

[Find issues](https://github.com/Mayankpateldev/unfired/issues) · [Join Discussions](https://github.com/Mayankpateldev/unfired/discussions) · [Use the launch kit](community/launch-kit.md) · [See the completeness audit](docs/11-completeness-audit.md)

Useful releases and respectful sharing can attract contributors. No viral reach, users, partnerships, job outcomes, or customer savings are claimed or guaranteed. Free local source does not mean unlimited free hosting.

## License

[MIT](LICENSE) covers this repository's original code, guides, fixtures, templates, and artwork. Commercial reuse is permitted with the required notice. MIT does **not** require downstream modifications to remain open. External materials and linked projects retain their own terms. See [licensing choices](handbook/licensing.md).

Source-review notes: [docs/sources.md](docs/sources.md). Working project name: Unfired; trademark clearance is not established. Version 0.2 broadens the original recovery kit into a rebuild handbook and lab collection; it does not claim to deliver every possible replacement product.
