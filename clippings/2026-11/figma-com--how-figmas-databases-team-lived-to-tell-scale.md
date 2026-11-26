---
url: "https://www.figma.com/blog/how-figmas-databases-team-lived-to-tell-the-scale/"
captured_at: "2026-11-25T16:19:47+00:00"
title: "How Figma’s databases team lived to tell the scale"
domain: "figma-com"
---

Vertical partitioning was a relatively easy and very impactful scaling lever that bought us significant runway quickly. It was also a stepping stone on the path to horizontal sharding.

Figma’s database stack has grown almost 100x since 2020. This is a _good_ problem to have because it means our business is expanding, but it also poses some tricky technical challenges. Over the past four years, we’ve made a significant effort to stay ahead of the curve and avoid potential growing pains. In 2020, we were running a single Postgres database hosted on AWS’s largest physical instance, and by the end of 2022, we had built out a distributed architecture with caching, read replicas, and a dozen vertically partitioned databases. We split groups of related tables—like “Figma files” or “Organizations”—into their own vertical partitions, which allowed us to make incremental scaling gains and maintain enough runway to stay ahead of our growth.

[![One large database silo connected to two smaller ones.](https://cdn.sanity.io/images/599r6htc/regionalized/5c8ad1394a1cf21fc39adf7ca3d9f317c8b98b80-2120x1000.png?w=2120&h=1000&q=75&fit=max&auto=format)](https://www.figma.com/blog/how-figma-scaled-to-multiple-databases/)

Despite our incremental scaling progress, we always knew that vertical partitioning could only get us so far. Our initial scaling efforts had focused on reducing Postgres CPU utilization. As our fleet grew larger and more heterogeneous, we started to monitor a range of bottlenecks. We used a combination of historical data and load-testing to quantify database scaling limits from CPU and IO to table size and rows written. Identifying these limits was crucial to predicting how much runway we had per shard. We could then prioritize scaling problems before they ballooned into major reliability risks.

The data revealed that some of our tables, containing several terabytes and billions of rows, were becoming too large for a single database. At this size, we began to see reliability impact during Postgres vacuums, which are essential background operations that keep Postgres from running out of transaction IDs and breaking down. Our highest write tables were growing so quickly that we would soon exceed the maximum IO operations per second (IOPS) supported by Amazon’s Relational Database Service (RDS). Vertical partitioning couldn’t save us here because the smallest unit of partitioning is a single table. To keep our databases from toppling, we needed a bigger lever.

## [Scaffolding for scale](#scaffolding-for-scale)

We outlined a number of goals and must-haves to tackle short-term challenges while setting us up for smooth long-term growth. We aimed to:

*   **Minimize developer impact:** We wanted to handle the majority of our complex relational data model supported by our application. Application developers could then focus on building exciting new features in Figma instead of refactoring large parts of our codebase.
*   **Scale out transparently:** As we scale in the future, we don’t want to have to make additional changes at the application layer. This means that after any initial upfront work to make a table compatible, future scale-outs should be transparent to our product teams.
*   **Skip expensive backfills:** We avoided solutions that involve backfilling large tables or every table at Figma. Given the size of our tables and Postgres throughput constraints, these backfills would have taken months.
*   **Make incremental progress:** We identified approaches that could be rolled out incrementally as we de-risked major production changes. This reduced the risk of major outages and allowed the databases team to maintain Figma’s reliability throughout the migration.
*   **Avoid one-way migrations:** We maintained the ability to roll back even after a physical sharding operation is completed. This reduced the risk of being stuck in a bad state when unknown _unknowns_ occur.
*   **Maintain strong data consistency:** We wanted to avoid complex solutions like double-writes that are challenging to implement without taking downtime or compromising on consistency. We also wanted a solution that would allow us to scale out with near-zero downtime.
*   **Play to our strengths:** Since we were operating under tight deadline pressure, whenever possible, we favored approaches that could be rolled out incrementally on our fastest growing tables. We aimed to leverage existing expertise and technology.

## [Exploring our options](#exploring-our-options)

There are many popular open source and managed solutions for horizontally sharded databases that are compatible with Postgres or MySQL. During our evaluation, we explored CockroachDB, TiDB, Spanner, and Vitess. However, switching to any of these alternative databases would have required a complex data migration to ensure consistency and reliability across two different database stores. Additionally, over the past few years, we’ve developed a lot of expertise on how to reliably and performantly run RDS Postgres in-house. While migrating, we would have had to rebuild our domain expertise from scratch. Given our very aggressive growth rate, we had only months of runway remaining. De-risking an entirely new storage layer and completing an end-to-end-migration of our most business-critical use cases would have been extremely risky on the necessary timeline. We favored known low-risk solutions over potentially easier options with much higher uncertainty, where we had less control over the outcome.

NoSQL databases are another common scalable-by-default solution that companies adopt as they grow. However, we have a very complex relational data model built on top of our current Postgres architecture and NoSQL APIs don’t offer this kind of versatility. We wanted to keep our engineers focused on shipping great features and building new products instead of rewriting almost our entire backend application; NoSQL wasn’t a viable solution.

Given these tradeoffs, we began to explore building a horizontally sharded solution on top of our existing vertically partitioned RDS Postgres infrastructure. It didn’t make sense for our small team to re-implement a generic horizontally sharded relational database in-house; in doing so, we’d be competing with tools built by the likes of large open source communities or dedicated database vendors. However, because we were tailoring horizontal sharding to Figma’s specific architecture, we could get away with providing a much smaller feature set. For example, we chose not to support atomic cross-shard transactions because we could work around cross-shard transaction failures. We picked a colocation strategy that minimized the changes required at the application layer. This allowed us to support a subset of Postgres that was compatible with the majority of our product logic. We also were able to easily maintain backwards compatibility between sharded and unsharded postgres. If we ran into unknown _unknowns_, we could easily [roll back to unsharded](https://www.figma.com/blog/how-figma-scaled-to-multiple-databases/#the-logical-choice) Postgres.

## [The path to horizontal sharding](#the-path-to-horizontal-sharding)

Even with these narrower requirements, we knew horizontal sharding would be our largest and most complex database project to date. Luckily, our incremental scaling approach over the past few years bought us the runway to make this investment. In late 2022, we set out to unlock nearly infinite database scalability, and horizontal sharding—the process of breaking up a single table or group of tables and splitting the data across multiple physical database instances—was the key. Once a table is horizontally sharded at the application layer, it can support any number of shards at the physical layer. We can always scale out further by simply running a physical shard split. These operations happen transparently in the background, with minimal downtime and no application level changes required. This capability would allow us to stay ahead of our remaining database scaling bottlenecks, removing one of the last major scaling challenges for Figma. If vertical partitioning let us accelerate to highway speeds, horizontal sharding could remove our speed limits and let us fly.

![A data silo on the left that breaks out into two other data silos on the right.](https://cdn.sanity.io/images/599r6htc/regionalized/5b69dc237c2ee309a970a0ab656d02e62f136c26-2160x1440.png?w=804&h=536&q=75&fit=max&auto=format)

Vertical partitioning

![A data silo on the left that breaks out into two other data silos on the right, then four other silos.](https://cdn.sanity.io/images/599r6htc/regionalized/8903764c609f32287e38bd435f18b304d586efb0-2160x1440.png?w=804&h=536&q=75&fit=max&auto=format)

Horizontal sharding

Horizontal sharding was an order of magnitude more complex than our previous scaling efforts. When a table is split across multiple physical databases, we lose many of the reliability and consistency properties that we take for granted in ACID SQL databases. For example:

*   Certain SQL queries become inefficient or impossible to support.
*   Application code must be updated to provide enough information to efficiently route queries to the correct shard(s) wherever possible.
*   Schema changes must be coordinated across all shards to ensure the databases stay in sync. Foreign keys and globally unique indexes can no longer be enforced by Postgres.
*   Transactions now span multiple shards, meaning Postgres can no longer be used to enforce transactionality. It is now possible that writes to some databases will succeed while others fail. Care must be taken to ensure product logic is resilient to these “partial commit failures” (imagine moving a team between two organizations, only to find half their data was missing!).

We knew achieving full horizontal sharding would be a multi-year effort. We needed to de-risk the project as much as possible while delivering incremental value. Our first goal was to shard a relatively simple but very high traffic table in production as soon as possible. This would prove the viability of horizontal sharding while also extending our runway on our most loaded database. We could then continue building additional features as we worked to shard more complex groups of tables. Even the simplest possible feature set was still a significant undertaking. End to end, it took our team roughly nine months to shard our first table.

## [Our unique approach](#our-unique-approach)

Our horizontal sharding work built on what many others do, but with some unusual design choices. Here are a few highlights:

*   **Colos**: We horizontally sharded groups of related tables into colocations (which we affectionately call “colos”), which shared the same sharding key and physical sharding layout. This provided a friendly abstraction for developers to interact with horizontally sharded tables.
*   **Logical sharding:** We separated the concept of “logical sharding” at the application layer from “physical sharding” at the Postgres layer. We leveraged views to perform a safer and lower cost logical sharding rollout before we executed a riskier distributed physical failover.
*   **DBProxy query engine:** We built a DBProxy service that intercepts SQL queries generated by our application layer, and dynamically routes queries to various Postgres databases. DBProxy includes a query engine capable of parsing and executing complex horizontally sharded queries. DBProxy also allowed us to implement features like dynamic load-shedding and request hedging.
*   **Shadow application readiness:** We added a “shadow application readiness” framework capable of predicting how live production traffic would behave under different potential sharding keys. This gave product teams a clear picture of what application logic needed to be refactored or removed to prepare the application for horizontal sharding.
*   **Full logical replication**: We avoided having to implement “filtered logical replication” (where only a subset of data is copied to each shard). Instead, we copied over the entire dataset and then only allowed reads/writes to the subset of data belonging to a given shard.

## [Our sharding implementation](#our-sharding-implementation)

One of the most important decisions in horizontal sharding is which shard key to use. Horizontal sharding adds many data model constraints that revolve around the shard key. For example, most queries need to include the shard key so that the request can be routed to the right shard. Certain database constraints, like foreign keys, only work when the foreign key is the sharding key. The shard key also needs to distribute data evenly across all shards to avoid hotspots that cause reliability issues or impact scalability.

Figma lives in the browser, and many users can collaborate in parallel on the same Figma file. This means that our product is powered by a fairly complex relational data model capturing file metadata, organization metadata, comments, file versions, and more.

We considered using the same sharding key for every table, but there was no single good candidate in our existing data model. To add a unified sharding key, we would have had to create a composite key, add the column to every table’s schema, run expensive backfills to populate it, and then substantially refactor our product logic. Instead, we tailored our approach to Figma’s unique data model and selected a handful of sharding keys like UserID, FileID, or OrgID. Almost every table at Figma could be sharded using one of these keys.

We introduced the concept of colos, which provide a friendly abstraction for product developers: Tables within a colo support cross-table joins and full transactions when restricted to a single sharding key. Most application code already interacted with the database this way, which minimized the work required by application developers to make a table ready for horizontal sharding.

![Three data silos, each containing blocks for "users table" and "user favorites table."](https://cdn.sanity.io/images/599r6htc/regionalized/8610966e627e683caaff88094d9dd8b75efa1a3b-2160x1440.png?w=804&h=536&q=75&fit=max&auto=format)

Tables sharded by UserID and by FileID are each colocated together

![Three data silos, each containing blocks for "files table" and "file comments table."](https://cdn.sanity.io/images/599r6htc/regionalized/53ad07418b852f047bf1f19719c63dbf2d211cc3-2160x1440.png?w=804&h=536&q=75&fit=max&auto=format)

Once we picked our sharding keys, we needed to ensure that there would be an even distribution of data across all backend databases. Unfortunately, many of the sharding keys that we had picked used auto-incrementing or Snowflake timestamp-prefixed IDs. This would have resulted in significant hotspots where a single shard contained the majority of our data. We explored migrating to more randomized IDs, but this required an expensive and time-consuming data migration. Instead, we decided to use the hash of the sharding key for routing. As long as we picked a sufficiently random hash function, we would ensure a uniform distribution of data. One downside of this is that range-scans on shard keys are less efficient, since sequential keys will be hashed to different database shards. However, this query pattern is not common in our codebase, so it was a trade-off we were willing to live with.

### [The “logical” solution](#the-logical-solution)

To de-risk the horizontal sharding rollout, we wanted to isolate the process of preparing a table at the application layer from the physical process of running a shard split. To do this, we separated “logical sharding” from “physical sharding.” We could then decouple the two parts of our migration to implement and de-risk them independently. Logically sharding gave us confidence in our serving stack with a low-risk, percentage-based rollout. Rolling back logical sharding when we found bugs was a simple configuration change. Rolling back a physical shard operation is possible, but it requires more complex coordination to ensure data consistency.

Once a table is logically sharded, all reads and writes will act as if the table is already horizontally sharded. From a reliability, latency, and consistency perspective, we appear to be horizontally sharded, even though the data is still physically located on a single database host. When we are confident that logical sharding is working as expected, we then perform the physical sharding operation. This is the process of copying the data from a single database, sharding it across multiple backends, then re-routing read and write traffic through the new databases.

![Two data silos with blocks for logical and physical shards.](https://cdn.sanity.io/images/599r6htc/regionalized/fc28f4926b31d5e5b9cc97a8fc622ac5788ca865-2160x1440.png?w=804&h=536&q=75&fit=max&auto=format)

Four logical shards on two physical shards

### [The query engine that could](#the-query-engine-that-could)

To support horizontal sharding, we had to significantly re-architect our backend stack. Initially, our application services talked directly to our connection pooling layer, PGBouncer. However, horizontal sharding required much more sophisticated query parsing, planning, and execution. To support this, we built out a new golang service, DBProxy. DBProxy sits between the application layer and PGBouncer. It includes logic for load-shedding, improved observability, transaction support, database topology management, and a lightweight query engine.

![The application layer flows to DB Proxy, PG Bouncer, and then to the database.](https://cdn.sanity.io/images/599r6htc/regionalized/2af44a9d935f95fa08d003b61041270b30d1bb07-2160x1440.png?w=804&h=536&q=75&fit=max&auto=format)

The query engine is the heart of DBProxy. Its main components are:

*   A query parser reads SQL sent by the application and transforms it into an Abstract Syntax Tree (AST).
*   A logical planner parses the AST and extracts the query type (insert, update, etc) and logical shard IDs from the query plan.
*   A physical planner maps the query from logical shard IDs to physical databases. It rewrites queries to execute on the appropriate physical shard.

![A query that flows to "where" and then leads to "shard\_key" and "other\_col."](https://cdn.sanity.io/images/599r6htc/regionalized/1547e54a020e816921f740b12b71f2b64f415652-1056x1584.png?w=528&h=792&q=75&fit=max&auto=format)

Query parser

![A query that flows to "where" that then leads to "shard\_key" and "other\_col." Those then flow to "logical select."](https://cdn.sanity.io/images/599r6htc/regionalized/f01e5c7bb39a8b73ef5f44c4d944ebb4d1ab5872-1056x1584.png?w=528&h=792&q=75&fit=max&auto=format)

Logical planner

![A diagram showing the logical select plan that leads to logical single shard plan; then a physical select plan that leads to physical single shard query.](https://cdn.sanity.io/images/599r6htc/regionalized/451db126da5358fff366445be34f74bf5bdb6a2c-1056x1584.png?w=528&h=792&q=75&fit=max&auto=format)

Physical planner

Think of **“scatter-gather”** like a database-wide game of hide-and-seek: You send out your query to every shard (scatter), then piece together answers from each (gather). Fun, but overdo it, and your speedy database starts feeling more like a snail, especially with complex queries.

Some queries are relatively easy to implement in a horizontally sharded world. For example, single-shard queries are filtered to a single shard key. Our query engine just needs to extract the shard key and route the query to the appropriate physical database. We can “push down” the complexity of the query execution into Postgres. However, if the query is missing a sharding key, our query engine has to perform a more complex **“scatter-gather.”** In this case, we need to fan out the query to all shards (the scatter phase) and then aggregate back results (the gather phase). In some cases, like complex aggregations, joins, and nested SQL, this scatter-gather can be very complex to implement_._ Additionally, having too many scatter-gathers would impact horizontal sharding scalability. Because the queries have to touch every single database, each scatter-gather contributes the same amount of load as it would if the database was unsharded.

![Four data shards, one of which is connected to DB Proxy.](https://cdn.sanity.io/images/599r6htc/regionalized/c172a28efe8b2e0630f782c44cd6371526ec3187-2160x1440.png?w=804&h=536&q=75&fit=max&auto=format)

![Four database shards that flow from DB Proxy.](https://cdn.sanity.io/images/599r6htc/regionalized/9475e44f3d4db830253dacf7144d96d8bdac0e13-2160x1440.png?w=804&h=536&q=75&fit=max&auto=format)

If we supported full SQL compatibility, our DBProxy service would have begun to look a lot like the Postgres database query engine. We wanted to simplify our API to minimize DBProxy’s complexity, while also reducing the work required for our application developers, who would have to re-write any unsupported queries. To determine the right subset, we built out a “shadow planning” framework, which allowed users to define potential sharding schemes for their tables and then run shadow the logical planning phase on top of live production traffic. We logged the queries and associated query plans to a Snowflake database, where we could run offline analysis. From this data, we picked a query language that supported the most common 90% of queries, but avoided worst-case complexity in our query engine. For example, all range scan and point queries are allowed, but joins are only allowed when joining two tables in the same colo and the join is on the sharding key.

### [A view of the future](#a-view-of-the-future)

We then needed to figure out how to encapsulate our logical shards. We explored partitioning the data using separate Postgres databases or Postgres schemas. Unfortunately, this would have required physical data changes when we logically sharded the application, which was just as complex as doing the physical shard split.

Instead, we chose to represent our shards with Postgres views. We could create multiple views per-table, each corresponding to the subset of data in a given shard. This would look like: `CREATE VIEW table_shard1 AS SELECT * FROM table WHERE hash(shard_key) >= min_shard_range AND hash(shard_key) < max_shard_range).` All reads and writes to the table would be sent through these views.

By creating sharded views on top of our existing unsharded physical databases, we could logically shard before we performed any risky physical reshard operations. Each view is accessed via its own sharded connection pooler service. The connection poolers still point to the unsharded physical instance, which gives the appearance of being sharded. We were able to de-risk the rollout of sharded reads and writes gradually via feature flags in the query engine and roll back at any time within seconds by just rerouting traffic back to the main table. By the time we ran our first reshard, we were confident in the safety of the sharded topology.

![An unsharded databases with views of four different shards.](https://cdn.sanity.io/images/599r6htc/regionalized/654e4ee15b6ee16b9208ad020eb2ae654b34d0a8-2160x1440.png?w=804&h=536&q=75&fit=max&auto=format)

By creating multiple views in an unsharded database, we can query the views as if the data was already physically sharded.

Of course, relying on views also introduced added risks. Views add a performance overhead and in some cases could fundamentally change how the Postgres query planner optimizes queries. To validate that approach, we collected a query corpus of sanitized production queries and ran load tests with and without views. We were able to confirm that views would only add a minimal performance overhead in most cases, and less than 10% in the worst cases. We also built out a shadow reads framework which could send all live read traffic through views, comparing the performance and correctness of view versus non-view queries. We were then able to confirm that views were a viable solution with minimal performance impact.

### [Tackling our topology](#tackling-our-topology)

To perform query routing, DBProxy has to understand the topology of our tables and physical databases. Because we had separated the concept of logical versus physical sharding, we needed a way to represent these abstractions within our topology. For example, we need to be able to map a table (users) to its shard key (user\_id). Similarly, we needed to be able to map a logical shard ID (123) to the appropriate logical and physical databases. With vertical partitioning, we relied on a simple, hard-coded configuration file that mapped tables to their partition. However, as we moved towards horizontal sharding, we required something more sophisticated. Our topology would change dynamically during shard splits and DBProxy needed to quickly update its state to avoid routing requests to the wrong database. Because every change to topology is backwards compatible, these changes are never in the critical path for our site. We built out a database topology that encapsulated our complex horizontal sharding metadata and could deliver real-time updates in under a second.

![A topology library that leads to a square (S3) and a cylinder (ETCD).](https://cdn.sanity.io/images/599r6htc/regionalized/8db2e5fe21409fc4c47fc77909a0f8f8f33383e6-2160x1440.png?w=804&h=536&q=75&fit=max&auto=format)

Having a separate logical and physical topology allowed us to also simplify some of our database management. For example, in our non-production environments, we can keep the same logical topology as production, but serve the data from many fewer physical databases. This saves costs and reduces complexity without having too many changes across environments. The topology library also allowed us to enforce invariants across our topology (e.g. every shard ID should be mapped to exactly one physical database) that were critical to maintaining the correctness of our system as we built out horizontal sharding.

### [The physical sharding operation](#the-physical-sharding-operation)

Once a table is ready for sharding, the last step is the physical failover from unsharded to sharded databases. We were able to reuse much of the same logic for horizontal sharding, but there were a few notable differences: Instead of moving data from 1 to 1 database, we were going from 1 to N. We needed to make the failover process resilient to new failure modes where the sharding operation could succeed on only a subset of our databases. Still, many of the riskiest components had already been de-risked during vertical partitioning. We were able to move much faster towards our first physical sharding operation than would have otherwise been possible.

## [We’ve come a long way](#we-ve-come-a-long-way)

When we started this journey, we knew that horizontal sharding would be a multi-year investment into Figma’s future scalability. We shipped our first horizontally sharded table in September 2023. We successfully failed over with only ten seconds of partial availability on database primaries and no availability impact on replicas. We saw no regressions in latency or availability after sharding. Since then we’ve been tackling relatively simple shards from our highest write rate databases. This year, we’ll shard increasingly complex databases, which have dozens of tables and thousands of code call-sites.

To remove our last scaling limits and truly take flight, we will need to horizontally shard every table at Figma. A fully horizontally sharded world will bring many other benefits: improved reliability, cost savings, and developer velocity. Along the way, we’ll need to solve all of these problems:

*   Support for horizontally sharded schema updates
*   Globally unique ID generation for horizontally sharded primary keys
*   Atomic cross-shard transactions for business critical use-cases
*   Distributed globally unique indexes (currently unique indexes are only supported on indexes including the sharding key)
*   An ORM model that increases developer velocity and is seamlessly compatible with horizontal sharding
*   Fully automated reshard operations that can run shard splits with the click of a button

Once we’ve bought ourselves sufficient runway, we will also reassess our original approach of in-house RDS horizontal sharding. We started this journey 18 months ago with extremely tight timeline pressure. NewSQL stores have continued to evolve and mature. We will finally have bandwidth to reevaluate the tradeoffs of continuing down our current path versus switching to an open source or managed solution.

We’ve made a lot of exciting progress on our horizontal sharding journey, but our challenges are just beginning_._ Stay tuned for more deep dives into different parts of our horizontal sharding stack. If you’re interested in working on projects like this, please reach out! We’re [hiring](https://www.figma.com/careers/).

We couldn’t have shipped horizontal sharding without these current and former databases team members: Anna Saplitski, David Harju, Dinesh Garg, Dylan Visher, Erica Kong, Gordon Yoon, Gustavo Mezerhane, Isemi Ekundayo, Josh Bancroft, Junhson Jean-Baptiste, Kevin Lin, Langston Dziko, Maciej Szeszko, Mehant Baid, Ping-Min Lin, Rafael Chacon Vivas, Roman Hernandez, Tim Goh, Tim Liang, and Yiming Li.

We’d also like to thank all of our cross-functional partner teams, especially Amy Winkler, Braden Walker, Esther Wang, Kat Busch, Leslie Tu, Lin Xu, Michael Andrews, Raghav Anand, and Yichao Zhao.
