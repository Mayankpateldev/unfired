"""Replacement using integer arithmetic against SPEC.md. SPDX-License-Identifier: MIT."""


def quote(payload):
    def reject():
        return 400, {"error": "invalid_request"}

    def integer_in(value, low, high):
        return type(value) is int and low <= value <= high

    if type(payload) is not dict:
        return reject()
    if not set(payload).issubset({"items", "discount_bps", "tax_bps"}):
        return reject()
    discount_rate = payload.get("discount_bps", 0)
    tax_rate = payload.get("tax_bps", 0)
    if not all(integer_in(rate, 0, 10000) for rate in (discount_rate, tax_rate)):
        return reject()
    records = payload.get("items")
    if type(records) is not list or not 1 <= len(records) <= 50:
        return reject()
    totals, quantities = [], []
    for record in records:
        if type(record) is not dict or set(record) != {"sku", "quantity", "unit_cents"}:
            return reject()
        sku = record["sku"]
        if type(sku) is not str or not 1 <= len(sku.strip()) <= 64:
            return reject()
        if not integer_in(record["quantity"], 1, 1000) or not integer_in(record["unit_cents"], 0, 1000000):
            return reject()
        totals.append(record["quantity"] * record["unit_cents"])
        quantities.append(record["quantity"])
    subtotal = sum(totals)
    discount = (subtotal * discount_rate + 5000) // 10000
    taxable = subtotal - discount
    tax = (taxable * tax_rate + 5000) // 10000
    return 200, dict(subtotal_cents=subtotal, discount_cents=discount, taxable_cents=taxable,
                     tax_cents=tax, total_cents=taxable + tax, units=sum(quantities))
