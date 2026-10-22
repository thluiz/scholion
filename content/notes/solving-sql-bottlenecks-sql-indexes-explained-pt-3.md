---
title: "Solving Bottlenecks With SQL Indexes and Partitions"
date: '2021-06-14T09:27:08-03:00'
category: webclip
summary: 'Explains when SQL indexes help range queries, when wildcards defeat them, how B-tree depth and fragmentation affect reads, and how partitioning changes maintenance and query plans.'
tags: ["sql-indexes", "b-tree", "partitioning", "query-performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Solving SQL Bottlenecks (SQL Indexes Explained, Pt. 3) | Toptal"
    url: "https://www.toptal.com/database/sql-indexes-explained-pt-3?utm_campaign=Toptal%20Engineering%20Blog&utm_medium=email&_hsmi=126740665&_hsenc=p2ANqtz-9sS4sxGELfMUlRjNSgmtXMXH8FExvKOAQPwnRqCPjUk1Y_p4P7LiYeMwsSmiKIbx6Ocs7MQ43xErIaSfXjdA6pHjrtlA&utm_content=126740665&utm_source=hs_email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-06/toptal-com--solving-sql-bottlenecks-sql-indexes-explained-pt-3.md"
    kind: repo
---

The article shows that indexes help most when a query narrows the search range and can follow the order of indexed values. It contrasts proper range predicates with expressions that block index use, and it shows how wildcard placement in LIKE changes whether the index can stop early or must be scanned in full.

## Reading notes

- Range queries benefit from indexes when they reduce the possible values of one or more columns.
- A predicate that applies a function to the column can prevent the RDBMS from using the index efficiently.
- Rewriting a date equality condition as a true range query lets the engine use the sorted index entries.
- `LIKE '%son'` can require scanning the whole index or table, depending on how many rows match.
- `LIKE 'Rob%'` can use the index to find the first matching entry and stop when the prefix no longer matches.
- For indexed range queries, the read cost is described as B = D + 1 + R, where D is B-tree depth and R is returned rows.
- Only the B-tree depth changes with table size in that estimate, so smaller depth helps most when result sets are small.
- Index fragmentation grows over time as inserts, updates, and deletes split blocks and leave them half-full.
- Reindexing restores physical order, but it can require locking and is best done during off-peak hours.
- Deleting historical rows can make fragmentation worse and increase the need for reindexing.
- Partitioning can limit active data and make maintenance easier.
- Global indexes cover all partitions but are not partition-aware, so dropping a partition still requires rebuilding affected index data.
- Globally partitioned indexes let the index follow the table partitioning, so dropping a partition can be handled without downtime.
- Local indexes live inside each table partition and avoid the drawbacks of global partitioned indexes.
- Local indexes work well when most queries touch only one or a few partitions.
- Local indexes can be slower for queries that must search across every partition, such as looking up a client and hotel across the whole reservation history.
- The article closes by pointing to related topics such as caching, non-B-tree indexes, clustered indexes, functional indexes, partial indexes, and other partitioning strategies.
