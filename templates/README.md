# Templates for the whole rebuild

| Stage | Template | Use it to |
| --- | --- | --- |
| Choose | [Project proposal](project-proposal.md) | State one user, task, scope, costs, and acceptance criteria |
| Source | [Provenance](provenance.md) | Record rights, sources, dependencies, and assistance |
| Observe | [Observation log](observation-log.md) | Separate facts, hypotheses, and counterexamples |
| Specify | [Behavior contract](behavior-contract.md) | Define inputs, outputs, errors, and exclusions |
| Verify | [Compatibility matrix](compatibility-matrix.md) | Record exact cases and supported claims |
| Move data | [Migration plan](migration-plan.md) | Preserve source information and plan rollback |
| Release | [Rebuild release gate](rebuild-release.md) | Check reproducibility, license, export, costs, and maintenance |
| Explain | [Case study](case-study.md) | Show evidence, differences, limits, and lessons |

Generate a new project dossier with `python3 tools/new_project.py my-tool --category api --out output/my-tool`. Fill the draft before implementing. Templates do not confer permission, verify behavior, or create a finished application by themselves.

For recovery work, use [weekly-plan.md](weekly-plan.md), [resume-evidence.md](resume-evidence.md), [outreach.md](outreach.md), [applications.csv](applications.csv), and [budget.csv](budget.csv) in a private workspace. Regional guidance uses [regional-resource.md](regional-resource.md).
