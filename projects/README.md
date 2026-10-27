# Free-tool project catalog

The machine-readable [catalog](catalog.json) contains 12 starting points. **These are scoped proposals, not a claim that 12 products exist.** `csv-cleaner` has an initial CLI implementation; all other entries need validation and implementation.

Every proposal names a user task, a small first version, acceptance criteria, and explicit exclusions. Start by copying [project-proposal.md](../templates/project-proposal.md) and [provenance.md](../templates/provenance.md).

Choose using five questions: do real users want it; can we build it independently; can it run affordably; can users export their work; can someone maintain it? Do not choose a target because you want to punish a former employer.

For the first release, prefer local utilities that process user-owned files. Defer account systems, payment handling, medical/legal/financial decision engines, and critical infrastructure. Those require support and review capacity this starter does not have.
