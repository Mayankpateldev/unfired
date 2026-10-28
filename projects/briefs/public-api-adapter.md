# Proposal: Public API Adapter

Status: proposal, no implementation. Category: API. User: a developer maintaining one documented integration. Scope: a narrow supported subset, not a generic clone of a service.

## First version

Choose one publicly documented resource with permitted use, or create a synthetic local resource first. Define an original stable client interface. Implement against a local mock, with configurable credentials supplied outside Git only if an authorized external integration is later added.

## Steps

1. Record the exact documentation version, use conditions, and supported endpoints.
2. Specify input/output schema, authentication assumptions, pagination, errors, timeouts, and retries.
3. Build a local mock with fixed synthetic responses.
4. Implement the adapter without logging tokens or whole private payloads.
5. Test successful, empty, malformed, unauthorized, rate-limited, and timeout responses.
6. Document unsupported endpoints and a source/export migration path.

## Acceptance

Fixtures replay without external credentials. The adapter distinguishes an empty success from a failed request. Retries are bounded and only occur for documented safe cases. Pagination cannot loop forever on a repeated token. Unknown response fields are handled according to an explicit preservation/rejection rule. No integration claim is made until tested against an authorized target and version.

## Exclusions and risks

No undocumented access, credential sharing, access-control bypass, scraping outside allowed scope, automatic mutation, or claim of vendor affiliation. A mock proves the local contract, not live compatibility. Start with [the API lab](../../labs/quote_api/README.md), [the method](../../handbook/method.md), and [provenance](../../templates/provenance.md).
