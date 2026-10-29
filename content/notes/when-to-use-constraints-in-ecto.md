---
title: "When to Use Constraints in Ecto"
date: '2016-03-30T14:48:17-03:00'
category: webclip
summary: 'The post explains when Ecto validations are enough and when database constraints are needed, showing that constraints give stronger guarantees for uniqueness, ordering, and overlap, but can reduce flexibility and user experience.'
tags: ["ecto", "constraints", "validations", "postgresql"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "NathanMLong.com - When to Use Constraints in Ecto"
    url: "http://nathanmlong.com/2016/03/when-to-use-constraints-in-ecto/?utm_campaign=elixir_radar_42&utm_medium=email&utm_source=RD+Station"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-03/nathanmlong-com--when-to-use-constraints-in-ecto.md"
    kind: repo
---

The post distinguishes validations from constraints by where they run: validations happen in application code, while constraints are checked by the database when data is inserted or updated. It uses event records to show which rules fit each approach and when both are needed.

## Reading notes

- Blank names can be handled with a validation, because the application can detect an empty string.
- Uniqueness should be enforced with a database constraint, since a pre-insert query can race with another insert.
- `end_time > start_time` can be checked with a validation and a check constraint, because the validation catches many cases and the constraint covers race conditions.
- The post suggests `optimistic_lock` if the real issue is updating from stale data.
- Overlap between events is presented as a rule that only the database can reliably check.
- Ecto can map database constraint violations to user-friendly error messages in changesets.
- Constraints are best for rules that must never be broken.
- Validations should catch as many errors as possible first, because database constraints fail one at a time and can make form correction tedious.
