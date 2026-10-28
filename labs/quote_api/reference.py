"""Teaching reference using Decimal arithmetic. SPDX-License-Identifier: MIT."""

from decimal import Decimal, ROUND_HALF_UP


def quote(payload):
    bad = (400, {"error": "invalid_request"})
    if not isinstance(payload, dict) or set(payload) - {"items", "discount_bps", "tax_bps"}:
        return bad
    items = payload.get("items")
    if not isinstance(items, list) or not 1 <= len(items) <= 50:
        return bad
    for field in ("discount_bps", "tax_bps"):
        amount = payload.get(field, 0)
        if type(amount) is not int or not 0 <= amount <= 10000:
            return bad
    subtotal = Decimal(0)
    units = 0
    for item in items:
        if not isinstance(item, dict) or set(item) != {"sku", "quantity", "unit_cents"}:
            return bad
        if not isinstance(item["sku"], str) or not 1 <= len(item["sku"].strip()) <= 64:
            return bad
        quantity, price = item["quantity"], item["unit_cents"]
        if type(quantity) is not int or not 1 <= quantity <= 1000:
            return bad
        if type(price) is not int or not 0 <= price <= 1000000:
            return bad
        subtotal += Decimal(price) * quantity
        units += quantity
    rounded = lambda value: int(value.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    discount = rounded(subtotal * payload.get("discount_bps", 0) / 10000)
    taxable = int(subtotal) - discount
    tax = rounded(Decimal(taxable) * payload.get("tax_bps", 0) / 10000)
    return 200, {"subtotal_cents": int(subtotal), "discount_cents": discount,
                 "taxable_cents": taxable, "tax_cents": tax,
                 "total_cents": taxable + tax, "units": units}
