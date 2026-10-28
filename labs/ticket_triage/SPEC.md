# Routing workflow contract v1

Input: JSON array of objects with exactly `id`, `topic`, `urgent`. Empty arrays are valid.

- `id`: unique string, 1–64 characters, containing non-whitespace text. Preserve the original value.
- `topic`: string up to 80 characters. Trim and lowercase for matching; empty and unknown topics use the fallback.
- `urgent`: JSON boolean, not a string or integer.
- Reject malformed input and duplicate IDs before producing a file. No partial output.

Evaluate rules in this order:

| Order | Condition | Queue | Priority | Reason |
| --- | --- | --- | --- | --- |
| 1 | urgent is true | human_review | high | urgent_flag |
| 2 | topic is billing, payment, or refund | billing | normal | billing_topic |
| 3 | topic is bug, outage, or technical | technical | normal | technical_topic |
| 4 | Otherwise | general | normal | fallback |

Output object: `routes` array in input order, each containing `id`, `queue`, `priority`, `reason`; plus `counts` containing billing, technical, general, and human_review, including zeros. Counts must sum to the number of input tickets. Do not include free text or invent severity from a topic. Execution is stateless and preview-only.
