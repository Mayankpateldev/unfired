# Find the right kind of help

| Need | Where to go | What to include |
| --- | --- | --- |
| A reproducible bug | [GitHub issues](https://github.com/Mayankpateldev/unfired/issues) | Command, environment, synthetic input, expected/actual result |
| Help understanding a lab | [Discussions](https://github.com/Mayankpateldev/unfired/discussions) | Lab, step, what you tried, and a redacted error |
| A new rebuild idea | Project-proposal issue template | One user, one workflow, source basis, and acceptance criteria |
| A documentation or translation improvement | Documentation issue or PR | Page, specific friction, proposed change, and reviewer where needed |
| Exposed secrets or a sensitive vulnerability | [SECURITY.md](SECURITY.md) | Use a private route; do not copy sensitive content into an issue |
| Immediate employment questions | [Recovery guide](docs/01-first-72-hours.md) | Consult official local agencies or qualified advisers for individual cases |

This is a volunteer project, not a job-placement service, legal clinic, emergency support service, or staffed production helpdesk. No response-time commitment is offered. Keep resumes, identity records, finances, customer information, and employer documents out of public issues.

Before reporting a tool problem, run `python3 -m labs.verify`, `python3 -m unittest discover -s tests -v`, and `python3 scripts/check_repo.py`. The HTTP tests require local loopback ports. Do not weaken your environment's network protections to run a lab; use an environment where you are authorized to bind loopback.
