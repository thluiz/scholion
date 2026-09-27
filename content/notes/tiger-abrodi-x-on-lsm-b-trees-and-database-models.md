---
title: "Tiger Abrodi (@TAbrodi) on X"
date: '2024-01-10T18:07:29+00:00'
category: webclip
summary: 'The author says the book is exceptional and reflects on LSM trees, B trees, relational versus document databases, and when to study topics more deeply before writing about them.'
tags: ["lsm-trees", "b-trees", "database-models", "replication"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Tiger Abrodi (@TAbrodi) on X"
    url: "https://x.com/TAbrodi/status/1745145352045375612?s=20"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2024-01/x-com--tiger-abrodi-x-on-lsm-b-trees-and-database-models.md"
    kind: repo
---

The post says the reader is midway through the book and pausing to make sure the material is understood deeply. It focuses on data structures and database models, especially the contrast between relational and document systems, and on how LSM trees and B trees work in practice.

## Reading notes

- The author has been reading about LSM and B trees and says the book is exceptional.
- Graphs are described as flexible and useful for many-to-many relationships such as social networks.
- Relational databases are associated with complex transactions, data integrity, consistent structure, and analytics or reporting.
- Document databases are associated with large volumes of unstructured or semi-structured data, rapidly changing models, and horizontal scalability with high read and write throughput.
- The author notes that horizontal scaling for SQL has become easier with modern tools.
- LSM trees are described as involving a memtable in memory, flushing to SSTables on disk, immutable sorted SSTables, background merging and compaction, and reads that check the memtable before SSTables.
- Bloom filters are mentioned as a way to speed up lookups in SSTables.
- B trees are described as easier to understand than to build.
- The key benefit of B trees is reading in O(log n) time instead of linear time.
- B trees use Write-Ahead Logging to reduce corruption during crashes.
- Latches and lightweight locks are mentioned for concurrency control.
- The author summarizes LSM as better for write-heavy databases and B trees as the choice otherwise.
- The post says the author wants to write a deeper post after implementing B and LSM trees from scratch or after finishing Database Internals.
- The author also wants to study replication thoroughly and keep digging into topics like data warehousing at a high level while choosing where to go deep.
