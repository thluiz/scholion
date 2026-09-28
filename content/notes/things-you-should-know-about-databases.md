---
title: "Things You Should Know About Databases"
date: '2022-06-29T10:03:02-03:00'
category: webclip
summary: 'A primer on RDBMS indexes and transactions, explaining why indexes speed reads, how B+ trees organize them, and how isolation levels shape consistency and read anomalies.'
tags: ["databases", "rdbms", "indexes", "transactions"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Things You Should Know About Databases"
    url: "https://architecturenotes.co/things-you-should-know-about-databases/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-06/architecturenotes-co--things-you-should-know-about-databases.md"
    kind: repo
---

This post sets out the two main topics the author thinks matter most when working with RDBMSs: indexes and transactions. It explains why indexes help when data grows beyond what can be scanned quickly, and why transaction isolation matters when several operations touch the same data.

## Reading notes

- Indexes are described as data structures that reduce lookup time at the cost of storage, memory, and slower writes because they must be kept up to date.
- The post says indexing becomes necessary when data grows large enough that scanning rows or reading the whole dataset from disk takes too long.
- A useful index stores the location of matching rows for a chosen column, letting the database find relevant data faster than a full table scan.
- The article emphasizes that index leaf nodes are compact and easier to cache, which helps speed access to the underlying rows.
- B-trees and B+trees are presented as the main tools for handling scale because they keep tree depth uniform and make lookup grow logarithmically.
- The linked list structure between leaf nodes is used to support fast updates and allow forward and backward traversal.
- On transactions, the post defines a transaction as a unit of work that should either complete fully or not happen at all.
- It focuses on isolation and describes non-repeatable reads, dirty reads, and phantom reads as the main read phenomena to watch for.
- REPEATABLE READ is described as keeping a consistent view after the first read and protecting against dirty and non-repeatable reads.
- SERIALIZABLE is presented as the most restrictive mode, running queries one at a time and requiring retry logic because concurrent queries can fail.
- READ COMMITTED gives each read its own committed snapshot and can still allow phantom reads.
- READ UNCOMMITTED allows reading uncommitted data and can therefore produce dirty reads.
