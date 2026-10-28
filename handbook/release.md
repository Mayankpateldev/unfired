# Turn a promising rebuild into a usable release

A public folder is a start. A release should let a new person complete the promised task and understand the costs and limits.

## Four gates

| Gate | Evidence | Do not advance if |
| --- | --- | --- |
| Discover | One user problem, sources, permissions, observations | Inputs depend on confidential or unauthorized material |
| Specify | Contract, error behavior, fixtures, explicit exclusions | Expected behavior is too vague to test |
| Verify | Reproducible implementation, compatibility evidence, migration dry run | Data silently disappears or only the author can run it |
| Release | Setup, license, costs, maintenance, export, rollback | Claims exceed the tested scope |

Use [the release checklist](../templates/rebuild-release.md). A release can be a small CLI, converter, adapter, documentation contribution, or repair guide. It need not be a hosted SaaS platform.

## Required README content for a tool

State the user and task; working command; supported environment; sample input/output; storage and network behavior; export; non-destructive defaults; limitations; license; maintainers; support expectations; and version. Make optional paid services optional in reality, not just in wording.

## Handover and maintenance

Keep a list of dependencies, update procedure, test commands, release steps, known issues, backup/restore, and what to do if maintainers leave. Make unmaintained status visible. Do not promise urgent support unless a real support arrangement exists.

## Earn sustainably

People can pay for installation, migration, training, maintenance, or support around an open tool. Write scope, handover, price, and revision limits before doing client work. Do not promise that unpaid open-source effort will produce income. Benefits and reporting rules vary; consult the relevant agency about work or earnings.

The movement benefits from honest, small releases that people can keep using. A polished announcement cannot substitute for setup, export, or a working acceptance test.
