# Use AI to accelerate work you can verify

AI can draft a specification, suggest edge cases, explain public documentation, or propose an implementation. It cannot establish rights, prove equivalence, or take responsibility for correctness. No AI service is required for this repository's tools or labs.

## A reviewable sequence

1. **Research input:** provide public references or an original synthetic observation log. Keep secrets, private employer material, and other people's data out.
2. **Specification:** ask for explicit assumptions, unknowns, schema, errors, and boundaries. Review before requesting code.
3. **Fixture design:** write expected results independently. Ask AI for counterexamples and compare them with the contract.
4. **Implementation:** use the contract as the input. Review the code, dependencies, network calls, and data paths.
5. **Verification:** run tests and inspect failure output. Require an explanation of why the result is right.
6. **Release:** disclose substantial assistance and remaining limitations. Record provenance and license review.

## Prompts to adapt

**Observation review**

> Using only this public specification and synthetic log, separate observed facts from hypotheses. Identify missing boundary cases. Do not invent internals, permissions, source behavior, or data.

**Implementation**

> Implement only this contract with the standard library. Preserve input files, reject unsupported values explicitly, and make outputs exportable. Explain rounding, ordering, and error behavior. Do not add external APIs or telemetry.

**Test review**

> Find a plausible wrong implementation that would still pass these tests. Suggest a minimal synthetic case with an independently reasoned expected output that detects it. Do not derive every expected output from the implementation.

**Release review**

> Compare README claims to the actual commands, fixtures, and results below. List unsupported claims, missing setup steps, data-loss risks, and unfinished work. Do not label proposals as working software.

## Decide whether a model improves the product

Start with a deterministic baseline. Compare task correctness, human correction effort, elapsed time, optional API cost, data exposure, and recovery from failure. Use a held-out set of authorized or synthetic cases. Publish the scope and failures, not a sweeping “better than” claim.

A script that reliably solves the task can be the finished result. Optional AI features need clear configuration, credentials outside Git, usage limits, an explanation of what leaves the device, and a useful fallback. No benchmark or model comparison has been run by this starter project.
