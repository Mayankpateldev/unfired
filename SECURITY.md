# Security and sensitive information

This starter has no hosted service, user accounts, telemetry, or external API calls. The CLI reads local files and writes user-selected local output. Only the latest source in the default branch is currently maintained; no long-term support or independent audit is claimed.

## Reporting

If GitHub private vulnerability reporting is enabled on the published repository, use **Security → Report a vulnerability**. Otherwise use GitHub's private platform reporting mechanism for exposed secrets or personal information. Do not put credentials, private data, or exploit details involving real systems in a public issue. A dedicated private maintainer address is not configured yet.

For an ordinary non-sensitive bug, open an issue with synthetic input and reproduction steps. We cannot promise a response deadline.

## Your local data

- `.unfired/` and `output/` are ignored by Git, but are not encrypted or access-controlled by this project. Protect your device and backups.
- The initializer does not overwrite existing tracker files. Commands refuse an output path that already exists.
- The CSV cleaner prefixes formula-like cells with an apostrophe as a basic spreadsheet-import precaution. This changes those values. Spreadsheet behavior varies; it is not a guarantee for every import program.
- Review any file before opening it in a spreadsheet or publishing it. Do not process employer/customer records without authorization.
- An aggregate report omits company/contact fields but still reveals application counts and timing context; it remains private by default.

If a secret leaks, notify its owner and revoke it promptly. Removing the working file is insufficient to erase prior commits or copies. Stop redistributing the affected material and coordinate a private cleanup.
