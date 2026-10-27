# Learn toward a deliverable

Choose one path for four weeks. Budget about five hours a week to start; adapt to your circumstances. These are project plans, not promises of employment. No paid course or AI subscription is required.

| Path | Week 1 | Week 2 | Week 3 | Week 4 | Proof of work |
| --- | --- | --- | --- | --- | --- |
| Python automation | Files, functions, errors, Git basics | CSV, JSON, command-line input | Tests, validation, documentation | Help one tester run it | A CSV utility with synthetic fixtures |
| Web development | Semantic HTML and CSS | JavaScript forms and state | Accessible keyboard flows and local storage | Test on phone and desktop | A local job tracker with export |
| Data and operations | Define a business question and data dictionary | Validate a synthetic dataset | Summarize in SQL or a script | Explain findings and limitations | A reproducible operations report |
| Product and design | Interview three willing users | Sketch one workflow and test assumptions | Prototype and test the main task | Publish a redacted case study | A tested flow and acceptance criteria |
| Technical writing and QA | Reproduce an existing setup | Identify confusing steps and edge cases | Write a guide and bug reports | Ask another person to follow it | A merged docs contribution or test report |

## Start with these resources

- [MDN Learn web development](https://developer.mozilla.org/en-US/docs/Learn_web_development): a web learning route for beginners.
- [Python tutorial](https://docs.python.org/3/tutorial/): suited to people who already understand basic programming. Absolute beginners can start with the official [Python beginner guide](https://www.python.org/about/gettingstarted/).
- [Pro Git](https://git-scm.com/book/en/v2): reference for commits, branches, and collaboration.
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html): relational data exercises.
- [W3C accessibility tutorials](https://www.w3.org/WAI/tutorials/): usable forms, structure, and interaction.
- [GitHub open-source guides](https://opensource.guide/how-to-contribute/): contributing beyond code.

External resources are not bundled or relicensed here. Versions and availability can change. See [source notes](sources.md).

## Learn AI without outsourcing judgment

For any workflow, write down its input, expected output, cost ceiling, failure modes, and review step. First build a deterministic baseline. If you add an AI feature, compare it against that baseline on a small synthetic evaluation set. Record wrong answers as well as useful ones. Provide a non-AI fallback where possible.

Exercise: ask a model to explain a failing synthetic CSV test. Inspect its proposed change, run the tests, and describe why the result is correct. Do not merge code you cannot explain. Generated code and text require provenance, license, and accuracy review just like other contributions.

## The completion rule

Finish when a new person can run the work from the README, complete its main task, export the result, and explain one limitation. Add it to your [evidence sheet](../templates/resume-evidence.md). Pick the next learning topic only after that.
