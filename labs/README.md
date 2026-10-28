# Learn by rebuilding observable behavior

Three runnable labs teach the workflow: observe → specify → implement → compare → migrate → release. These are original teaching systems created for this repository. They are not reverse-engineered commercial products, production services, or proof of compatibility with any external vendor.

Use Python 3.10+, from the repository root. No dependencies or paid APIs.

```bash
python3 -m labs.verify
python3 -m unittest discover -s tests -v
```

| Lab | You learn | What runs today | Start |
| --- | --- | --- | --- |
| Quote API | Requests, errors, rounding, and response compatibility | Two implementations, loopback HTTP server, 18 golden cases | [API lab](quote_api/README.md) |
| Board export | Schema inference, encodings, lossless migration, round trips | CSV ↔ versioned JSON converter with synthetic fixtures | [Format lab](board_format/README.md) |
| Ticket routing | Rule precedence, boundary cases, deterministic alternatives to AI | Offline routing preview and expected-output fixture | [Workflow lab](ticket_triage/README.md) |

## Choose your mode

- **First-time learner:** read the contract and run the fixtures before editing anything.
- **Behavior researcher:** inspect the API reference's HTTP outputs using synthetic requests; record observations without reading its implementation first.
- **Implementer:** use only the contract and fixtures to write your own replacement in another file or language.
- **Reviewer:** introduce a deliberate mismatch, prove a check fails, restore the fix, and record unsupported cases.

The supplied reference and replacement were authored in the same contribution using different arithmetic approaches. This is a teaching comparison, not an independently audited clean-room separation. For a real project, record who saw which sources and what permission applies.

All fixtures and specifications are original synthetic material, MIT licensed. Standard-library API references are in [the tool guide](../handbook/tools.md). No third-party product captures, credentials, or private data are bundled.

## Finish with evidence

For each lab, write one observation, one hypothesis, one falsifying edge case, and one stated limitation. Use [the case-study template](../templates/case-study.md). Passing these small fixtures shows conformance to the documented examples; it does not prove complete equivalence to a real-world system.
