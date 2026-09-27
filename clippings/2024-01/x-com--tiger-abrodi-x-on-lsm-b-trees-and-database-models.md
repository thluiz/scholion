---
url: "https://x.com/TAbrodi/status/1745145352045375612?s=20"
captured_at: "2024-01-10T18:07:29+00:00"
title: "Tiger Abrodi (@TAbrodi) on X"
domain: "x-com"
---

🧵 I'm halfway through, and can already say, this is exceptional.

I'm pausing for a few days to make sure I've understood most of what I read at a deep level. 🥰

I spent some time today digging deep into LSM and B trees.

Already went over the different ways to structure data. Graphs are extremely flexible, good when you've much many to many relationships e.g. social networks. 😄

---

Document versus Relational is where things get interesting.

Relational:

- Applications requiring complex transactions and data integrity (e.g., banking systems).
- Systems where data structure is consistent and not frequently changing.
- Scenarios where data analytics and reporting are a priority.

Document:

- Applications dealing with large volumes of unstructured or semi-structured data (e.g., content management systems, catalogs).
- Projects with rapidly evolving data models or feature development.
- Systems that prioritize horizontal scalability and high read/write throughput.

Although, horizontal scaling for SQL has gotten better or easier to do with the modern tools we have.

---

LSM is a bit confusing, because it's not just a data structure, but there is a background process happening.

1. Write to Memtable. (kept sorted, in memory)
2. After certain size, flush to SSTable.
3. SSTables are immutable and sorted. (on disk)
4. New writes go to new Memtable.
5. Merging and Compaction: Background process periodically merges smaller SSTables into larger ones. Compaction removes redundant or obsolete data.
6. Read operation: Checks the memtable first, then looks through SSTables, usually starting with the most recent.

And oh yeah, Bloom Filters can be used here to speed up the look up process. A quick way to get an answer if a key is in the SSTables.

---

B Trees weren't too hard to grasp. Building them will be hard surely. A video on Youtube where a guy from Fullstack Academy broke it down so simply. Astonishing when people teach and it just digests.

I guess the highlight is O(log n) when reading instead of linear time. So when input grows, the effort of looking up grows slowly and not linearly.

B Trees use Write-Ahead Logging (WAL) to prevent corruption during crashes. Recording changes before applied to the tree itself.

For concurrency control, they use latches and lightweight locks.

---

LSM vs B Trees?

Concisely: LSM for write heavy DBs, otherwise go with B Trees.

I do want to write an in depth post about this. I think I'll get around to it when I've implemented B and LSM trees from scratch.

Or after I finish the book Database Internals.

This way, the blog posts I write after finishing this book can be, e.g., database models, replication, etc.

More generalized things rather than very specific.

---

I wanna continue for a day or two revising and digging deeper. Replication very thoroughly for sure!

There are things like data warehousing which are good to understand at a high level, but be pragmatic and know where you wanna dig deep. It's foolish to overload our brains after all.
