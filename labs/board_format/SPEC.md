# Unfired Board format v1

## CSV representation

UTF-8, optional leading BOM, comma delimiter, standard CSV quoting. Header must be exactly `id,title,state,labels`, in that order. Every record has four fields; an empty board has only the header.

| Field | Rule |
| --- | --- |
| id | Unique ASCII identifier, 1–64 letters/digits/underscores/hyphens |
| title | String of 1–200 characters containing non-whitespace text; preserve exact value |
| state | Exactly `todo`, `doing`, or `done` |
| labels | JSON array of unique non-empty strings, each at most 40 characters and containing non-whitespace text |

## JSON representation

An object with exactly `format`, `version`, and `cards`:

```json
{"format":"unfired-board","version":1,"cards":[{"id":"a","title":"Example","state":"todo","labels":[]}]}
```

`version` must be integer 1, not boolean. Each card contains exactly the four documented fields with the same rules. Preserve card and label order, IDs, Unicode, quotes, commas, and embedded newlines. Unknown keys and versions are rejected to prevent loss.

## Compatibility claim

The converter supports this schema only. Round-trip equality refers to semantic data, not identical CSV quoting, BOM, or line-ending bytes. Attachments, relationships, comments, dates, and user permissions are outside the format. It is not a drop-in importer for any external vendor.
