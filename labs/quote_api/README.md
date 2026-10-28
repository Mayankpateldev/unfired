# Lab 1: replace a small API without changing its contract

Goal: reproduce a visible pricing calculation with a different implementation. The teaching reference uses Decimal arithmetic; the replacement uses integer arithmetic. This is demonstration arithmetic, not tax, billing, or payment advice.

## Run

```bash
python3 -m labs.verify
python3 -m labs.quote_api.server --implementation reference --port 8765
```

In a second terminal:

```bash
curl -s http://127.0.0.1:8765/health
curl -s http://127.0.0.1:8765/v1/quote -H 'Content-Type: application/json' --data-binary @labs/quote_api/example-request.json
```

The example produces subtotal **3000**, discount **300**, taxable **2700**, tax **135**, total **2835**, and **3** units. Stop the reference with Ctrl-C. Start the replacement on the same port and repeat:

```bash
python3 -m labs.quote_api.server --implementation replacement --port 8765
```

Bindings are limited to `127.0.0.1`. This standard-library teaching server has no authentication, persistence, TLS, production concurrency guarantees, or deployment configuration. Do not expose it as a public service.

## Observe before reading code

Read [SPEC.md](SPEC.md), then answer with a synthetic request:

1. Does discount apply before tax?
2. How does a half-cent round?
3. Is a boolean accepted as a numeric quantity?
4. What happens with an empty list or an extra field?
5. Does HTTP success mean the same thing as a valid JSON body?

Record one row per experiment in [the observation template](../../templates/observation-log.md). Do not inspect a third party's traffic; this exercise operates against the supplied local server.

## Evidence and exercise

[fixtures.json](fixtures.json) contains 18 cases with explicit expected statuses and bodies, including invalid inputs. `labs.verify` checks **both** implementations against those expected outputs. HTTP tests separately check routing, malformed JSON, content type, body-size limits, and a successful result.

Change rounding in a copy of the replacement from half-up to truncation. The `tax-half-cent` and `discount-half-cent` cases should fail. Restore the implementation and run the suite. For a more advanced exercise, implement the contract in another language and replay the same JSON cases.

Known gap: the fixtures are finite. Query strings, authentication, localization, streaming, and real-world tax rules are outside this contract.
