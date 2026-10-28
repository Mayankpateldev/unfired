"""Strict CSV/JSON card interchange. SPDX-License-Identifier: MIT."""

import csv
import io
import json
import re

FIELDS = ["id", "title", "state", "labels"]


def validate(cards):
    if type(cards) is not list:
        raise ValueError("cards must be an array")
    ids = set()
    for card in cards:
        if type(card) is not dict or set(card) != set(FIELDS):
            raise ValueError("every card needs exactly id, title, state, and labels")
        identifier = card["id"]
        if type(identifier) is not str or not re.fullmatch(r"[a-zA-Z0-9_-]{1,64}", identifier) or identifier in ids:
            raise ValueError("card IDs must be unique, non-empty ASCII identifiers")
        ids.add(identifier)
        if type(card["title"]) is not str or not card["title"].strip() or len(card["title"]) > 200:
            raise ValueError("title must have 1–200 characters and contain non-whitespace text")
        if type(card["state"]) is not str or card["state"] not in {"todo", "doing", "done"}:
            raise ValueError("state must be todo, doing, or done")
        labels = card["labels"]
        if type(labels) is not list or any(type(label) is not str or not label.strip() or len(label) > 40 for label in labels):
            raise ValueError("labels must be non-empty strings of at most 40 characters")
        if len(set(labels)) != len(labels):
            raise ValueError("labels must be unique within a card")
    return cards


def from_csv(text):
    reader = csv.reader(io.StringIO(text.lstrip("\ufeff"), newline=""), strict=True)
    rows = list(reader)
    if not rows or rows[0] != FIELDS:
        raise ValueError("CSV header must be id,title,state,labels in that order")
    cards = []
    for row in rows[1:]:
        if len(row) != 4:
            raise ValueError("each CSV row must have four fields")
        card = dict(zip(FIELDS, row))
        card["labels"] = json.loads(card["labels"])
        cards.append(card)
    return {"format": "unfired-board", "version": 1, "cards": validate(cards)}


def to_csv(document):
    if type(document) is not dict or set(document) != {"format", "version", "cards"}:
        raise ValueError("document needs exactly format, version, and cards")
    if document["format"] != "unfired-board" or type(document["version"]) is not int or document["version"] != 1:
        raise ValueError("unsupported format or version")
    cards = validate(document["cards"])
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(FIELDS)
    for card in cards:
        writer.writerow([card["id"], card["title"], card["state"], json.dumps(card["labels"], ensure_ascii=False)])
    return output.getvalue()
