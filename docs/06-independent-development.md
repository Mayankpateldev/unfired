# Independent development and provenance

Your general skills can inform a new project. Employer-owned code, protected business information, customer records, and confidential implementations are different. This project accepts original work grounded in public sources or material you have permission to use.

WIPO explains that trade-secret rules and exceptions vary by legal system; independent development or reverse engineering can be relevant in some settings. That is not blanket permission for a particular product or agreement. Read [WIPO's trade-secret overview](https://www.wipo.int/en/web/trade-secrets) and get qualified advice where rights are uncertain.

## Accepted foundations

- Public standards and documentation, with URLs and review dates.
- Properly licensed code and data, with required notices and compatibility review.
- Your original requirements derived from voluntary user research.
- Authorized input/output observations where terms and local rules permit them.
- Synthetic examples and user-owned exports provided with permission.

## Keep out of this repository

- Former employer source code, internal prompts, runbooks, private designs, non-public architecture, customer lists, logs, and documents.
- Code reconstructed from confidential implementation details, including from memory. General professional skills are not permission to reproduce protected specifics.
- Private credentials, leaked repositories, unauthorized scraping, access-control bypasses, or circumvention instructions.
- Customer data or another person's story without consent.
- Copied product text, artwork, screenshots, or branding without appropriate rights.

## A practical process

1. Describe the user-visible task independently, not by listing confidential implementation details.
2. Record each source and its access conditions in [provenance.md](../templates/provenance.md).
3. Where practical, separate public-source specification research from implementation, especially if a contributor previously worked on a similar proprietary system.
4. Write original code and synthetic tests. Preserve dependency licenses and attribution.
5. Ask a reviewer to check provenance, public claims, and accidental confidential details.
6. If rights are uncertain, pause the affected contribution and obtain appropriate review before release. Build a different, clearly sourced task in the meantime.

This reduces avoidable risk; it does not establish legal clearance. Contracts, copyright, patents, trademarks, trade secrets, and anti-circumvention rules can apply independently. This project does not offer legal conclusions about any particular company's product.

## If something sensitive is posted

Do not quote or redistribute it. Remove public access where possible, notify maintainers using a private GitHub reporting route if configured, and contact the relevant credential owner to revoke exposed secrets. Deleting a file in a later commit does not erase Git history or existing copies. See [SECURITY.md](../SECURITY.md).
