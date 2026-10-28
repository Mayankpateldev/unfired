"""Original rules from SPEC.md; no external service or AI. SPDX-License-Identifier: MIT."""


def route(tickets):
    if type(tickets) is not list:
        raise ValueError("input must be a ticket array")
    seen, routes = set(), []
    counts = {name: 0 for name in ("billing", "technical", "general", "human_review")}
    for ticket in tickets:
        if type(ticket) is not dict or set(ticket) != {"id", "topic", "urgent"}:
            raise ValueError("tickets require exactly id, topic, and urgent")
        identifier, topic = ticket["id"], ticket["topic"]
        if type(identifier) is not str or not identifier.strip() or len(identifier) > 64 or identifier in seen:
            raise ValueError("ticket IDs must be unique strings of 1–64 characters")
        if type(topic) is not str or len(topic) > 80 or type(ticket["urgent"]) is not bool:
            raise ValueError("topic must be a string up to 80 characters; urgent must be boolean")
        seen.add(identifier)
        topic = topic.strip().lower()
        if ticket["urgent"]:
            queue, priority, reason = "human_review", "high", "urgent_flag"
        elif topic in {"billing", "payment", "refund"}:
            queue, priority, reason = "billing", "normal", "billing_topic"
        elif topic in {"bug", "outage", "technical"}:
            queue, priority, reason = "technical", "normal", "technical_topic"
        else:
            queue, priority, reason = "general", "normal", "fallback"
        counts[queue] += 1
        routes.append({"id": identifier, "queue": queue, "priority": priority, "reason": reason})
    return {"routes": routes, "counts": counts}
