---
title: "Zero-downtime Postgres migrations - the hard parts"
date: '2015-06-05T09:35:34-03:00'
category: webclip
summary: 'A Postgres migration caused 15 seconds of API downtime because adding a foreign key locked a heavily used referenced table. The post explains why and lists ways to reduce lock-related downtime.'
tags: ["postgres", "database-migrations", "locking", "downtime"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Zero-downtime Postgres migrations - the hard parts"
    url: "https://gocardless.com/blog/zero-downtime-postgres-migrations-the-hard-parts/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/gocardless-com--zero-downtime-postgres-migrations-the-hard-parts.md"
    kind: repo
---

The post describes an unexpected API outage during a planned schema migration. The migration renamed empty tables and recreated foreign key constraints, but a long-running read on a heavily used referenced table caused the foreign key change to wait on an `AccessExclusive` lock, and API requests piled up behind it.

It then explains the locking behavior behind this case and gives ways to avoid similar outages, including reducing long-running queries, using `lock_timeout`, splitting schema changes into smaller steps, and keeping Postgres updated.

## Reading notes

- Zero-downtime schema changes still depend on lock behavior in Postgres.
- Renaming empty tables was not the source of the outage.
- Dropping and recreating foreign key constraints looked safe because the tables being changed were empty.
- Adding a foreign key takes `AccessExclusive` locks on both the constrained table and the referenced table.
- If that lock is blocked, queued conflicting operations also wait behind it.
- A slow read on the referenced table caused the migration to block.
- The `ALTER TABLE` statement itself was fast once it could run.
- The waiting lock blocked read and write queries from the API.
- Long-running queries and transactions should be removed where possible.
- Analytics queries should run against an asynchronously updated replica.
- `log_min_duration_statement` and `log_lock_waits` can help find problematic queries.
- Migration scripts should set `lock_timeout` to a tolerable pause.
- Breaking schema changes into smaller steps shortens DDL transactions.
- Keeping Postgres current can improve locking behavior.
