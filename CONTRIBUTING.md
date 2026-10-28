# Contribute one useful thing

You do not need a job title, layoff story, or programming background to help. Start with a confusing instruction, a reproducible bug, a translation, an accessibility improvement, or one well-scoped tool proposal.

For rebuild work, begin with [the handbook](handbook/README.md), [the labs](labs/README.md), and [the templates](templates/README.md). Project stages and decision-making are in [GOVERNANCE.md](GOVERNANCE.md); questions belong in the routes listed in [SUPPORT.md](SUPPORT.md).

1. Check existing issues before starting a large change.
2. Describe the user problem and proposed acceptance criteria. Use the issue templates.
3. Make a small branch, such as `codex/improve-csv-errors`, in your fork.
4. Use only original or appropriately licensed material. Complete a [provenance record](templates/provenance.md) for new tools or substantial external material.
5. Run `python3 -m labs.verify`, `python3 -m unittest discover -s tests -v`, and `python3 scripts/check_repo.py`. HTTP tests need permission to open loopback ports.
6. Review your staged diff for secrets, private tracker data, and confidential employer material.
7. Open a pull request with what changed, why it helps, how it was checked, and any limitations.

Contributions are made under the [MIT license](LICENSE). By submitting, you confirm you have the right to contribute the material under those terms. Third-party material needs its own attribution and license review. No CLA is currently required.

## For a new rebuild

Submit a problem and source record before a large implementation. Add an observation log, behavior contract, synthetic fixtures with independently reasoned expectations, compatibility matrix, migration/rollback plan, and release checklist. The [scaffolder](tools/README.md) creates a draft dossier. Label unsupported behavior and keep proposed features distinct from working commands. Use the [case-study template](templates/case-study.md) to explain the result.

## Useful reviews

Review the advertised behavior, main result, failure handling, private data paths, source provenance, and ease of setup. Run examples with synthetic data. For factual legal or benefits changes, require an official source, location, review date, and a clear scope. Do not turn individual employment disputes into public case files.

## AI-assisted contributions

Disclose substantial AI assistance in your PR. You remain responsible for correctness, originality, license compatibility, and understanding the change. Do not upload private employer or customer information to an AI service. Generated tests should catch meaningful failures; they should not just restate the implementation.

## Translation

Create `docs/translations/<language-code>/` with the source document path and revision date. Keep official resource links and scope notes. Ask a second fluent speaker to review. Translation is not localization of legal rules; country guidance needs independent sourcing.

## Support expectations

Use issues for reproducible bugs and documentation questions. Volunteer capacity varies. Do not post resumes, medical information, finances, identity numbers, private messages, credentials, or employment contracts. Follow the [code of conduct](CODE_OF_CONDUCT.md).
