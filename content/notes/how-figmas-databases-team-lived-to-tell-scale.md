---
title: "How Figma’s databases team lived to tell the scale"
date: '2026-11-25T16:19:47+00:00'
category: webclip
summary: 'Figma describes how it moved from vertical partitioning on RDS Postgres to a custom horizontal sharding stack using colos, logical sharding via views, and a DBProxy query engine.'
tags: ["databases", "horizontal-sharding", "postgres", "scalability"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "How Figma’s databases team lived to tell the scale"
    url: "https://www.figma.com/blog/how-figmas-databases-team-lived-to-tell-the-scale/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/figma-com--how-figmas-databases-team-lived-to-tell-scale.md"
    kind: repo
---

Figma’s database traffic grew nearly 100x since 2020, forcing the team to move beyond a single large RDS Postgres instance and later multiple vertically partitioned databases. Vertical partitioning relieved CPU pressure and bought time, but large multi‑terabyte tables and IOPS limits on RDS meant some tables outgrew a single database. The team chose to stay on Postgres and RDS, avoiding risky migrations to NewSQL or NoSQL, and designed a horizontally sharded architecture tailored to Figma’s relational model and rapid growth constraints.

They introduced horizontal sharding as a multi‑year investment, separating logical sharding at the application layer from physical sharding across database instances. Logical sharding, implemented with Postgres views and routed through a new DBProxy layer, let them test behavior, roll out gradually, and roll back quickly before any physical shard splits. DBProxy parses and plans queries, routes them by shard key, supports limited scatter‑gather, and enforces a constrained SQL subset discovered via “shadow planning” on live traffic. Sharding uses a few key identifiers (UserID, FileID, OrgID) and hash‑based routing to spread load evenly, with related tables grouped into colocations (“colos”) so most joins and transactions stay single‑shard. A dynamic topology service encodes logical and physical layouts and propagates changes to DBProxy in under a second. After about nine months of work, Figma shipped its first horizontally sharded table in September 2023 with minimal availability impact and no latency regressions, and now plans to shard all tables and later reassess whether to keep evolving its in‑house RDS sharding or adopt an external solution.

## Reading notes

- Since 2020, Figma’s database stack traffic grew almost 100x, turning database scaling into a major technical challenge even as it signaled business growth.
- Initially, Figma ran a single large Postgres database on AWS; by late 2022 they had a distributed RDS Postgres setup with caching, read replicas, and around a dozen vertical partitions.
- Vertical partitioning split groups of related tables (for example, Figma files or organizations) into separate databases, which gave incremental scaling headroom with relatively low complexity.
- Over time they expanded monitoring from CPU to many bottlenecks, using historical data and load‑testing to find limits on CPU, IO, table size, and write volume per shard.
- Some tables reached several terabytes and billions of rows, causing reliability issues during Postgres vacuum operations and pushing against RDS IOPS limits on high‑write tables.
- Vertical partitioning could not address single tables that became too big, because its smallest unit is one table, so they needed a more powerful scaling mechanism.
- The team set goals such as minimizing application‑developer impact, enabling future scale‑outs without more app‑layer changes, and avoiding months‑long backfills of large tables.
- They prioritized approaches that allowed incremental rollout, preserved rollback paths after sharding, maintained strong data consistency without complex double‑writes, and leveraged existing Postgres and RDS expertise.
- During evaluation, they examined CockroachDB, TiDB, Spanner, and Vitess, but rejected them due to the need for complex dual‑store migrations and the loss of in‑house RDS Postgres expertise under a tight timeline.
- NoSQL options were also ruled out because Figma’s backend relies on a complex relational data model that would require widespread application rewrites.
- Instead, they decided to build horizontal sharding on top of their existing vertically partitioned RDS Postgres, focusing on a narrower feature set tailored to Figma’s use cases.
- To keep scope manageable, they chose not to support atomic cross‑shard transactions, relying instead on making product logic resilient to partial commit failures.
- Their colocation strategy minimized application changes by aligning shard boundaries with how product code already accessed related data.
- They ensured backwards compatibility between sharded and unsharded Postgres so they could roll back to unsharded databases if unforeseen issues appeared.
- Horizontal sharding was framed as their most complex database project, but previous incremental scaling efforts gave them enough time to invest in it.
- Once a table is sharded at the application layer, it can be spread over any number of physical shards, with further splits done transparently and with minimal downtime.
- Compared to vertical partitioning, horizontal sharding removes capacity limits by allowing data for a table to be distributed across many machines.
- Sharding introduces new challenges: some SQL queries become inefficient or unsupported, application code must carry shard keys, and schema changes must stay synchronized across shards.
- In a horizontally sharded system, Postgres can no longer enforce foreign keys or globally unique indexes across shards.
- Transactions that span shards can partially succeed, so they must design product behavior to tolerate scenarios where some writes complete and others fail.
- They expected full adoption of horizontal sharding to take years and chose to derisk by first sharding a simple, high‑traffic table in production.
- Sharding one high‑traffic table early would both validate the approach and extend capacity on a heavily loaded database.
- Even the reduced feature set for the first sharded table still took roughly nine months of work from design to production deployment.
- Their approach introduced “colos,” where groups of related tables share a shard key and layout, giving developers a clearer abstraction over sharded data.
- Logical sharding was separated from physical sharding, allowing them to test sharded behavior safely before moving data across hosts.
- They built a DBProxy service in Go that sits between application services and PGBouncer, intercepting queries and routing them to the right databases.
- DBProxy also implements dynamic load‑shedding, request hedging, observability improvements, and a lightweight query planner/executor for sharded queries.
- A “shadow application readiness” framework was added to model how real production traffic would behave under different shard keys, guiding product teams on required refactors.
- For data movement, they adopted full logical replication instead of filtered logical replication, copying entire datasets and then restricting operations per shard.
- Choosing a shard key became a central design decision, since queries need the key for efficient routing and many constraints depend on it.
- Figma’s product model includes file metadata, organization metadata, comments, and versions, reflecting many relationships in the underlying schema.
- There was no single sharding key that worked well for all tables, and introducing a universal composite key would have required adding columns, backfilling all tables, and refactoring logic.
- They instead chose a small set of shard keys such as UserID, FileID, and OrgID, which could cover almost all tables.
- Within a colo, tables that share a shard key can participate in cross‑table joins and full transactions as long as queries stay on one sharding key.
- Since most existing application code already worked within such boundaries, this design limited how many changes developers had to make to adopt sharding.
- Many chosen shard keys were based on auto‑increment IDs or Snowflake‑style timestamped IDs, which would have produced hotspots if used directly for shard assignment.
- Migrating IDs to more randomized values would have required expensive data migrations, so they instead routed based on a hash of the shard key to balance data distribution.
- Hashing the shard key improves uniformity but makes range scans on keys less efficient because sequential keys map to different shards; this was acceptable because such queries were rare for them.
- To lower rollout risk, they decoupled logical sharding (how the app sees data) from physical sharding (how data is stored), letting each be tested independently.
- Under logical sharding, all reads and writes behave as if they target multiple shards, but data is still stored on a single database host.
- Once logical sharding proves reliable, they perform the physical sharding operation, which copies data to multiple backends and reroutes queries there.
- Logical and physical sharding together allow minimal downtime migrations since the logical behavior is already validated before any data movement.
- Before horizontal sharding, services connected directly to PGBouncer; sharding needs more sophisticated parsing and planning, which led to building DBProxy in between.
- DBProxy’s query engine converts SQL to an AST, determines logical shard IDs, and then maps them to physical databases, rewriting queries as needed.
- For single‑shard queries, the engine extracts the shard key and routes the entire query to one physical database, letting Postgres handle the rich query semantics.
- Queries lacking shard keys require scatter‑gather: the engine fans out the query to all shards, then aggregates results, which can become complex and expensive for aggregations and joins.
- Heavy use of scatter‑gather undermines the scalability benefits of sharding, because each such query touches every shard and behaves like the unsharded case in terms of load.
- Fully supporting arbitrary SQL would have made DBProxy’s engine as complex as Postgres itself, so they limited the query language to a subset guided by real traffic.
- A “shadow planning” framework allowed teams to propose sharding schemes, then run the logical planner on production queries and log plans to Snowflake for offline analysis.
- Using shadow planning data, they identified a subset that covered about 90% of query patterns while avoiding the hardest planning cases.
- For example, they allow range scans and point queries broadly, but only allow joins when both tables are in the same colo and the join is on the sharding key.
- To implement logical shards without moving data, they evaluated separate databases or schemas, but these would have required physical changes even for purely logical rollout.
- They chose to represent logical shards with Postgres views, each view filtering the base table’s rows by a hash range over the shard key.
- All reads and writes go through these shard views, making the system behave as if the underlying table was already physically sharded.
- Each shard view is served via its own connection pooler that still points to the original unsharded instance, giving the illusion of multiple shards.
- Feature flags in the query engine allowed them to gradually direct traffic through the views and quickly revert to the base table configuration when needed.
- Load tests using a sanitized production query set showed that using views added minimal overhead in most cases and under 10% overhead in worst cases.
- A shadow reads framework sent live reads through both view‑based and direct paths, comparing correctness and performance, which confirmed that views were safe to adopt.
- DBProxy needs an understanding of table and database topology to route queries, especially once logical and physical sharding are decoupled.
- They replaced a simple static mapping file used for vertical partitioning with a richer topology system encoding shard keys, shard IDs, and mappings to logical and physical databases.
- The topology service updates DBProxy with changes in under a second, while changes remain backwards compatible so they are not on the critical path for availability.
- Having distinct logical and physical topology layers allows them to run fewer physical databases in non‑production environments while mirroring production’s logical layout.
- The topology library enforces invariants such as mapping each shard ID to exactly one physical database, which is key to correctness as the system evolves.
- For physical sharding, they reused much of the vertical partitioning failover machinery but adapted it for 1‑to‑N moves and new failure modes where only some databases succeed.
- Earlier vertical partitioning work had already addressed many risky failover aspects, letting them move faster on the first horizontal shard migration.
- They shipped the first horizontally sharded table in September 2023, with only about ten seconds of partial availability on primaries and no impact on replicas.
- After the first cutover, they observed no regressions in latency or availability attributable to sharding.
- The team initially focused on relatively simple shards drawn from their highest write‑rate databases to extend runway safely.
- Upcoming work includes sharding more complex databases with many tables and thousands of application call sites touching them.
- Their long‑term plan is to horizontally shard every table at Figma, which they expect will also yield reliability gains, cost benefits, and better developer velocity.
- They list future challenges such as supporting schema updates on sharded tables, globally unique ID generation for sharded primary keys, and atomic cross‑shard transactions for critical workflows.
- Additional future needs include distributed globally unique indexes that are not limited to indexes including the shard key, and an ORM that works naturally with sharding.
- They also aim for fully automated reshard operations that can perform shard splits with minimal manual intervention.
- Once they have more capacity and experience, they plan to reassess whether to continue with in‑house RDS‑based sharding or consider mature NewSQL or managed solutions.
- The article closes by noting that their horizontal sharding journey is ongoing, inviting readers interested in such projects to consider joining Figma’s databases team.
