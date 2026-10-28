# Tools with a specific job

Start with Python, Git, and a text editor. Add a tool only when an unanswered question needs it. Follow the official installation and permission instructions; the repository does not install any of these for you.

| Question | Tool/reference | Useful output | Scope note |
| --- | --- | --- | --- |
| What request follows an action? | [Chrome Network panel](https://developer.chrome.com/docs/devtools/network) | Request method, path, payload, response | Use your own or authorized system; raw captures can contain secrets |
| Can I repeat a request? | [curl tutorial](https://curl.se/docs/tutorial.html) | Reproducible local request | The supplied lab commands target loopback only |
| What data shape is this? | [Python csv](https://docs.python.org/3/library/csv.html), [json](https://docs.python.org/3/library/json.html) | Parsed fields and validation | Avoid delimiter guessing and unsafe code execution |
| What changed in behavior? | [Python unittest](https://docs.python.org/3/library/unittest.html), [difflib](https://docs.python.org/3/library/difflib.html) | Passing/failing case and readable diff | Golden expectations need independent reasoning |
| How is an owned training binary structured? | [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | An analysis note and hypothesis | Use original/licensed training material; no bypass exercise is supplied |
| What is on my authorized test network? | [Wireshark documentation](https://www.wireshark.org/docs/) | A scoped protocol observation | Capture only traffic you are permitted to inspect; do not publish secrets |
| Can I document and review a change? | [Pro Git](https://git-scm.com/book/en/v2) | A small commit and reviewable diff | Check staged data before public push |
| Can a keyboard/screen reader user finish? | [W3C WAI tutorials](https://www.w3.org/WAI/tutorials/) | A task test and specific barriers | A checklist alone is not accessibility certification |

## Included utilities

- `python3 -m labs.verify`: replay the three labs against checked-in expectations; exit nonzero on a mismatch.
- `python3 tools/new_project.py demo-tool --category api --out output/demo-tool`: generate a ten-file draft dossier, refusing an existing directory.
- `python3 tools/compare_json.py EXPECTED ACTUAL --out output/comparison.json`: strict JSON comparison with pointer-path diagnostics; see [usage and exit codes](../tools/README.md).
- `python3 tools/unfired.py --help`: original private-workspace, runway, CSV-cleaning, and tracker-report commands.
- `python3 scripts/check_repo.py`: local document-target, catalog, and lab-registry checks. It does not validate every external URL or factual claim.

Tool descriptions and primary references reviewed 2026-10-27. Versions, installation requirements, licenses, and availability can change. No affiliation, endorsement, or security audit is claimed.
