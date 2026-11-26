---
title: "Herding elephants: lessons learned from sharding Postgres at Notion"
date: '2026-11-25T16:16:29+00:00'
category: webclip
summary: 'Notion describes why and how they sharded their Postgres monolith: partitioning by workspace, capacity planning, migration strategy with audit logs, and lessons learned.'
tags: ["postgresql", "sharding", "scalability", "database-migrations"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Herding elephants: lessons learned from sharding Postgres at Notion"
    url: "https://www.notion.com/blog/sharding-postgres-at-notion"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/notion-com--herding-elephants-lessons-from-sharding-postgres.md"
    kind: repo
---

Notion describes the multi‑month effort behind a brief scheduled maintenance window in which they migrated from a single Postgres monolith to a horizontally sharded fleet. Growing usage pushed their original database past soft limits (notably VACUUM stalls and looming TXID wraparound), making sharding unavoidable. They chose application‑level sharding, partitioning all tables reachable from `block` by workspace ID into 480 logical shards across 32 physical databases, then executed a double‑write, backfill, and verification migration using an audit log rather than logical replication. The team shares specific capacity planning decisions, routing design, and migration safeguards, along with retrospective lessons on timing, downtime, and key design.

## Reading notes

- Product growth created billions of new blocks, files, and spaces, overloading a single Postgres instance that had handled five years and four orders of magnitude of growth.
- On‑call engineers increasingly faced CPU spikes, and even catalog‑only schema migrations became risky on the monolith.
- Industry warnings about premature sharding highlighted maintenance burden, application constraints, and architectural lock‑in, but at Notion’s scale sharding became inevitable.
- The practical trigger was Postgres `VACUUM` stalling, blocking reclamation of dead tuples and raising the risk of TXID wraparound, which would halt all writes to protect data.
- Vertical scaling via ever‑larger RDS instances proved unsustainable, as maintenance processes degraded before hardware limits were hit.
- The team chose application‑level sharding, preferring explicit control over data layout rather than opaque clustering in systems like Citus or Vitess.
- They first decided which tables to shard, starting from the core `block` table and including all tables reachable from it via foreign keys to keep related data colocated.
- Keeping related entities (such as comments and discussions) on a different physical database from their parent blocks risked inconsistencies because cross‑database transactions are not atomic.
- Since Notion is organized around team workspaces, they partitioned data by workspace ID, using the workspace UUID as the partition key.
- Every block belongs to exactly one workspace, and most user operations target a single workspace, which reduces cross‑shard joins when sharding by workspace ID.
- Capacity planning considered IOPS limits of AWS instance types and disks, target per‑table and per‑database size ceilings, instance count, and cost behavior.
- They targeted at least 60K total IOPS, capped per‑table size around 500 GB and per‑database size at 10 TB, and wanted linear cost growth with the ability to scale compute and storage separately.
- The final design used 480 logical shards spread evenly across 32 physical Postgres databases, with each logical shard implemented as a schema.
- Each schema (logical shard) contained its own copies of sharded tables like `block`, `collection`, and `space`, giving 480 instances of each sharded table.
- They chose 480 logical shards because this number has many divisors, allowing future redistribution across different host counts while keeping shards evenly balanced.
- Using 512 shards would have forced host counts that are powers of two, requiring doubling physical hosts when scaling while maintaining even shard distribution.
- Instead of using Postgres native table partitioning with a parent `block` table per database, they created separate tables like `schema001.block`, `schema002.block`, and so on.
- Avoiding native partitioned tables simplified routing so the application directly maps workspace ID to both physical database and logical shard without another partition layer.
- The routing mapping from workspace IDs to shards lives in the application, which serves as the single source of truth for directing queries.
- Their migration framework followed four phases: double‑write, backfill historical data, verify correctness, and finally switch reads to the new system.
- They evaluated three double‑write options: direct dual writes, logical replication, and an audit log plus catch‑up process.
- Directly writing to both databases was rejected because partial failures could easily create inconsistencies between the monolith and shards.
- Logical replication was tested but could not handle `block` write volume during the initial snapshot step.
- They adopted an audit log: writes are recorded into a log table, and a catch‑up script replays those changes into the sharded databases, with freedom to modify data on the way.
- As a contingency, they implemented a reverse audit log and replay script so that, if needed, writes made to the shards could be applied back to the monolith.
- Once double‑writes were working, they ran a backfill to move existing data, using an `m5.24xlarge` instance with 96 CPUs, which took around three days in production.
- The backfill logic checked version information so that older records would not overwrite more recent updates already written to the shards.
- A combination of continuous catch‑up from the audit log and backfill processing ensured the sharded databases converged to match the monolith’s state.
- Verification started only after shards were up to date, focusing on confirming data correctness rather than just completion.
- A verification script sampled contiguous ranges of UUIDs starting from a seed, comparing records in the monolith and the corresponding shard copies without scanning entire tables.
- Before switching reads, the team introduced dark reads that fetched from both the old and new databases, discarded shard results, and logged discrepancies.
- Dark reads increased API latency but provided higher confidence that read behavior would be correct after the switch‑over.
- Migration and verification logic were written by different engineers to reduce the chance that a shared implementation bug would undermine verification.
- Looking back, they would have preferred to shard earlier rather than wait until the monolith was heavily stressed and VACUUM issues had appeared.
- High monolith load prevented them from using logical replication to populate partition keys like workspace ID, since backfilling that column on the monolith would have added too much strain.
- Instead, they backfilled workspace IDs on the fly during writes to the shards, which demanded a custom catch‑up script tailored to that behavior.
- The switch‑over was bottlenecked by double‑write throughput, since they had to let the catch‑up script finish propagating writes while the service was down.
- They believe dedicating additional effort to optimize the catch‑up script to complete within tens of seconds could have enabled a hot swap with no downtime.
- In the sharded design, tables use a composite key of `id` (the old primary key) plus `space_id` (the partition key), which complicates application code.
- Since they needed a full table scan anyway, they now think they could have introduced a new combined key in a single column and avoided passing `space_id` throughout the application.
- Despite these regrets, the sharding project materially improved performance for users and showcased effective coordination under time pressure.
- The post closes with an invitation to engineers who balance urgent execution with long‑term design considerations to join the company.
