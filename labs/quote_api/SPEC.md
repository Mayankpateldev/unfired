# Quote API contract v1

This contract is original educational material. A basis point is 1/100 of one percent; the lab uses integer basis points to specify rates precisely.

## Transport

- `GET /health` → 200, `{"status":"ok"}`.
- `POST /v1/quote` → validated quote result or 400, `{"error":"invalid_request"}`.
- Unknown paths handled by GET/POST → 404, `{"error":"not_found"}`.
- POST bodies over 65,536 bytes → 413, `{"error":"request_too_large"}`.
- A non-negative Content-Length and a UTF-8 JSON body are required for the quote route. Malformed bodies → 400.
- Handled responses have an `application/json` content type. Other HTTP methods are outside this teaching contract.

## Request

Object with `items` and optional `discount_bps` and `tax_bps`. No unknown fields. `items` is an array of 1–50 objects, each with exactly:

| Field | Rule |
| --- | --- |
| sku | String with 1–64 characters after trimming; used only for validation |
| quantity | Integer 1–1,000; booleans excluded |
| unit_cents | Integer 0–1,000,000; booleans excluded |

Each optional rate defaults to 0 and must be an integer 0–10,000, booleans excluded. Duplicate SKUs are allowed and counted as separate lines. JSON object key order has no semantic meaning. The interface accepts no currency code; values are abstract minor units, not an actual currency conversion.

## Calculation and output

1. `subtotal_cents = sum(quantity × unit_cents)`.
2. `discount_cents = round_half_up(subtotal_cents × discount_bps / 10000)`.
3. `taxable_cents = subtotal_cents − discount_cents`.
4. `tax_cents = round_half_up(taxable_cents × tax_bps / 10000)`.
5. `total_cents = taxable_cents + tax_cents`.
6. `units = sum(quantity)`.

Return these six integer fields with HTTP 200. Inputs are non-negative, so half-up rounding means an exact half is rounded upward. Round the discount and tax separately, once each. No per-line rounding, currency symbols, timestamps, or random IDs.

## State and scope

Stateless calculations only. No money moves. No customer account, invoice, jurisdiction, price list, tax determination, authentication, or payment processing. Expected fixtures are concrete checks against this contract, not a certification of production financial correctness.
