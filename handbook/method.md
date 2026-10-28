# Observe → specify → rebuild → verify

Reverse engineering starts with a question about behavior. An open alternative turns that understanding into an original, maintainable implementation. An entire product is rarely the right first scope.

## 1. Define one useful outcome

Write: “A [user] can take [input they own] and obtain [output they need].” Example: a volunteer can export task cards, convert them into an open schema, and preserve titles, states, and labels. This is more testable than “replace every task-management platform.”

Before starting, check [existing projects](existing-projects.md). An importer, documentation fix, or missing export feature may help users sooner than a new platform.

## 2. Establish sources and access

Record public standards, documentation, your original research, licensed examples, and any permitted observations. Note version, date, and source conditions in [provenance](../templates/provenance.md). Access to an account does not automatically grant every kind of copying, automation, or redistribution permission.

If rights are unclear, work on the supplied synthetic labs or a public standard while the affected part is reviewed. General professional skills are useful; confidential implementation details stay out. See [independent development](../docs/06-independent-development.md) and [WIPO's explanation of trade-secret variation](https://www.wipo.int/en/web/trade-secrets).

## 3. Observe behavior deliberately

Use [an observation log](../templates/observation-log.md). Change one thing at a time. Record the exact input, output, visible state change, environment, and uncertainty. Include empty, malformed, boundary, repeated, Unicode, and reordered inputs where relevant.

Distinguish three kinds of statements:

| Kind | Example | What supports it |
| --- | --- | --- |
| Observation | An urgent ticket is shown in the human-review queue | A recorded synthetic case |
| Hypothesis | Urgency takes precedence over topic | Multiple cases, including a conflicting topic |
| Design choice | Our replacement will allow an export | Our own requirements, not a claim about a reference |

Do not infer invisible architecture from one screen. A similar output can be produced by different implementations.

## 4. Write a behavior contract

Use [the contract template](../templates/behavior-contract.md). Define inputs, outputs, defaults, error shapes, ordering, encoding, rounding, state transitions, and unsupported behavior. Convert claims into acceptance criteria. Unknown behavior is marked unknown instead of guessed.

For a team, the observation/specification contributor can hand a source-filtered contract to an implementer. Record who saw what. Separation can help provenance, but a checklist or the phrase “clean room” is not legal clearance.

## 5. Implement the smallest useful slice

Choose ordinary formats and minimal dependencies. Keep the first version local if possible. Write your own code from the contract. Preserve notices for reused licensed components. Add an export early. Prefer deterministic rules before introducing optional AI.

## 6. Compare against independent expectations

Create golden fixtures with expected outputs before running the replacement. Include examples that would catch an appealing wrong solution: truncation instead of rounding, splitting CSV by commas, or matching a topic before checking urgency. The [labs](../labs/README.md) demonstrate all three.

Test the exact claim you intend to make. “Passes 18 specified cases” is honest; “100% compatible” requires far more evidence. Keep unsupported cases visible in [a compatibility matrix](../templates/compatibility-matrix.md).

## 7. Migrate and release

Back up the source, dry-run on synthetic data, check fields and counts, preserve IDs, document losses, and plan rollback. A replacement that silently drops data has not completed the user's task. Finish with setup instructions, license, costs, maintenance limits, and [a release gate](../templates/rebuild-release.md).

## Stop or rescope when

The only available input is confidential; access or reuse is unauthorized; the workflow depends on an unreviewed safety-critical claim; tests cannot distinguish success from appearance; or nobody can maintain the result. A smaller, clearly sourced contribution is still progress.
