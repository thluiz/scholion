---
title: "Why Auto Increment Is A Terrible Idea"
date: '2015-05-29T11:39:33-03:00'
category: webclip
summary: 'The post argues that serial integers expose growth, make enumeration easy, and can clash across tables, while UUIDv4 offers stable, non-predictable primary keys with practical PostgreSQL support.'
tags: ["uuid", "primary-keys", "postgresql", "database-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why Auto Increment Is A Terrible Idea"
    url: "https://www.clever-cloud.com/blog/engineering/2015/05/20/Why-Auto-Increment-Is-A-Terrible-Idea/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/clever-cloud-com--why-auto-increment-is-a-terrible-idea.md"
    kind: repo
---

The post argues for UUIDs as primary keys instead of serial integers. It says primary keys should be stable and indexable, and that serial IDs disclose information, make entity enumeration easy, and are not unique across tables.

It also says UUIDv4 solves those issues because it is random, hard to enumerate, and can be generated without talking to the database. The text notes that PostgreSQL supports UUIDs, but also says serial IDs may still be acceptable when storage is tight, primary keys are not exposed, and performance constraints are strong.

## Reading notes

- Primary keys need to provide a stable, indexable reference to an entity.
- Semantic keys come from entity attributes, while technical keys are created when the row is inserted.
- Relational databases often use serial IDs because entities can change.
- A serial ID can reveal the number of rows by looking at the current sequence value.
- Primary keys are often exposed in URLs, so serial IDs can disclose growth outside the database.
- Incrementing IDs make it easy to enumerate rows in a table.
- The same serial value can exist in different tables, which can cause mistakes when deleting rows.
- Changing sequence start values or increments does not remove the information leak.
- UUIDs are 128-bit values with a hexadecimal textual form.
- UUIDv4 uses randomness and the database constraint catches the rare collision.
- UUIDv4 makes enumeration difficult, hides table size, and can be generated without database access.
- Generating entities without a round trip to the database makes code simpler and easier to test.
- Serial IDs are 32-bit integers and can overflow.
- PostgreSQL supports the `uuid` type and can generate UUIDv4 with `uuid-ossp` or `pgcrypto`.
- UUIDs can be too large when storage is tight, and random indexes reduce locality and can hurt insert performance.
- The post presents UUIDs as a safe default when the environment is not especially constrained.
