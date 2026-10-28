# Lab 3: rebuild a workflow from rules

Goal: replace a small routing workflow with transparent local rules before considering AI. This is an offline preview using synthetic support records; it sends no messages and changes no external tickets.

```bash
python3 -m labs.ticket_triage labs/ticket_triage/fixtures/input.json --out output/triage.json
python3 -m labs.verify
```

The four sample tickets route once each to billing, human review, technical, and general. Compare [input.json](fixtures/input.json) with [expected.json](fixtures/expected.json).

## Observe the order of decisions

An urgent refund goes to human review, even though the topic is billing. The first matching rule matters. Unknown topics reach a documented fallback rather than disappearing. Read [SPEC.md](SPEC.md), then draw the decision table yourself.

## Your exercise

1. Add a synthetic urgent technical ticket and specify the expected result before running it.
2. Remove the urgent-first rule in a copy. Demonstrate a meaningful failing test.
3. Add a new topic through a proposal that updates the contract, fixture, implementation, and documentation together.
4. Compare this deterministic baseline with any optional AI classifier on an authorized evaluation set. Include review time, wrong routes, cost, and privacy in the comparison.

Known limits: no natural-language classification, production support guarantees, dispatch, escalation timers, integrations, or private customer data handling. The lab's `urgent` flag is supplied explicitly; it does not detect emergencies from text.
