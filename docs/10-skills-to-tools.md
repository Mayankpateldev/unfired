# Turn experience into an original free tool

Do not try to recreate years of a company's software in a weekend. Extract the general user problem you understand, then solve a small version from public requirements. Your experience helps you choose better questions; it does not authorize copying protected implementation details.

## Map a skill to a public problem

| Experience | General problem you understand | Small original project | Proof it helps |
| --- | --- | --- | --- |
| Customer support | People repeat confusing setup steps | A task checklist with troubleshooting notes | Someone completes setup without coaching |
| Sales operations | User-owned exports are inconsistent | Local CSV normalization | A synthetic messy export becomes usable |
| Engineering | Small tools fail on bad inputs | A CLI with clear validation | Malformed fixtures produce useful errors |
| Data analysis | Reports hide unclear field meanings | An editable data dictionary | A tester correctly explains sample columns |
| Project management | Decisions disappear in meeting notes | A decision index for structured Markdown | A user finds the source of a sample decision |
| Design | Forms make basic tasks difficult | An accessible task prototype | A keyboard user completes the main flow |
| Technical writing | Instructions assume too much knowledge | A tested quickstart | A new user runs it on a clean machine |
| Quality assurance | Edge cases break normal workflows | Synthetic test fixtures and bug reports | A reproducible failure is fixed |

## A one-page worksheet

1. List three tasks you can explain using general skills and public information.
2. Choose one where users can provide their own non-sensitive input.
3. Write the task as `input → transformation → output`.
4. Find public references. Record them in [provenance](../templates/provenance.md).
5. Ask willing users whether the output would save effort. Do not assume they want an entire replacement platform.
6. Implement a deterministic baseline, an export path, and one meaningful failure check.
7. Ask a new user to run it. Measure the specific task with consent; do not generalize from a tiny trial.

Example: `authorized UTF-8 CSV → normalize headers, trim cells, remove exact duplicates → new CSV`. This repository includes that baseline in [the toolkit](../tools/README.md).

## Decide where AI belongs

Some work needs structured rules; some benefits from drafting or classification. Before adding a model, compare three versions: manual work, deterministic automation, and AI assistance. Use synthetic or explicitly authorized examples. Check correctness, time including review, cost per task, sensitive-data exposure, and failure recovery.

Keep a simple evaluation table:

| Case | Expected result | Baseline result | AI result | Human correction | Cost/time notes |
| --- | --- | --- | --- | --- | --- |
| Synthetic case 1 | Write before testing | Record actual output | Record actual output | Record needed changes | Include review effort |

If the baseline already solves the task, shipping it is a good outcome. If a model helps, keep credentials outside Git, explain the data flow, cap optional usage, and document when humans must check the result. There is no need to label a tool “AI-powered” to make it valuable.

## Give users a practical exit

Provide setup instructions, clear error messages, editable source, an open-format export, and a stated maintenance status. Compete through usability and trust. A free tool people can understand and leave is a concrete contribution to their independence.
