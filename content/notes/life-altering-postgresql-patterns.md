---
title: "Life Altering PostgreSQL Patterns"
date: '2026-09-25T17:54:07+01:00'
category: webclip
summary: 'The post collects PostgreSQL patterns that reduce operational pain: UUID keys, timestamps, restrictive foreign keys, schemas, enum tables, soft deletes, status logs, special rows, careful use of views, and JSON queries.'
tags: ["postgresql", "database-design", "sql-patterns"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Life Altering Postgresql Patterns"
    url: "https://mccue.dev/pages/3-11-25-life-altering-postgresql-patterns?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/mccue-dev--life-altering-postgresql-patterns.md"
    kind: repo
---

The post gathers PostgreSQL practices that make day-to-day work smoother in aggregate. It favors patterns that preserve data, reduce coordination, and make queries and debugging easier.

## Reading notes

- Use UUID primary keys because they do not require coordination with the database and are safe to share externally, despite random ordering and larger size.
- Add `created_at` and `updated_at` to tables so you can see when a row was created or last changed, and maintain `updated_at` with a trigger.
- Use `on update restrict on delete restrict` on foreign keys so deletes or key changes fail instead of removing referenced data.
- Use schemas as namespaces for tables, especially when an app has many tables.
- Model enums with tables when you want allowed values stored in the database and possibly extended with metadata.
- Name tables in the singular so queries stay closer to the row they are operating on.
- Name join tables mechanically by combining the table names when a more specific name is not obvious.
- Prefer soft deletes with a nullable timestamp when data should be marked as removed rather than erased.
- Represent changing statuses as a log of rows with a `valid_at` column so you can keep timing information and handle out-of-order events.
- Use a `latest` column with a unique partial index and trigger when you need quick access to the newest status row.
- Mark special rows with a nullable `system_id` so the system can reliably find them later.
- Use views sparingly because they are useful for wrapping queries but harder to change and can become hard to reason about when stacked.
- Use JSON mainly as a query result shape when you want to fetch related data in one trip and avoid cartesian products or N+1 problems.
