---
title: "Things I Wished More Developers Knew About Databases"
date: '2026-06-29T09:49:45+00:00'
category: webclip
summary: 'The article lists database pitfalls developers often miss, from networking and ACID tradeoffs to isolation anomalies, clock skew, latency, migrations, sharding, and scaling surprises.'
tags: ["databases", "consistency", "transactions", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Things I Wished More Developers Knew About Databases"
    url: "https://rakyll.medium.com/things-i-wished-more-developers-knew-about-databases-2d0178464f78"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-06/rakyll-medium-com--things-i-wished-more-developers-knew-about-databases.md"
    kind: repo
---

The article collects database lessons for application developers who are not specialized in databases. It argues that many failures come from networking, transaction semantics, isolation tradeoffs, ordering assumptions, clock differences, and scale effects that are easy to miss in everyday application work.

## Reading notes

- Network problems are likely a smaller share of outages than many people assume, but they still happen through hardware, topology, configuration, power failures, and other causes.
- ACID is a useful shorthand, but databases interpret it differently and some systems trade durability or other guarantees for performance.
- Consistency and isolation vary widely across databases, and weaker isolation can be faster while allowing races and anomalies.
- Optimistic locking can work when exclusive locks are hard to hold.
- Data anomalies include write skews, not only dirty reads and data loss.
- Database ordering may differ from the order in which code appears to run, especially with non-blocking calls and concurrency.
- Application-level sharding can be implemented as a layer in front of the database, not only inside application services.
- Auto-incremented IDs can create contention, partition hotspots, and replication problems in distributed systems.
- Stale reads can still be useful for analytics, approximate aggregates, and lock-free read-only work.
- Clock skew exists between machines, clocks, and time sources, and systems like Spanner use bounded time intervals to preserve correctness.
- Latency should be measured as both database latency and client-perceived latency.
- Performance should be evaluated per transaction or query, not only through broad throughput numbers.
- Nested transactions can create confusing rollback behavior and are best avoided.
- Transactions should not depend on mutable application state, because retries can change the values they use.
- Query planners can help explain query behavior and performance issues.
- Online migrations are possible but involve dual writes, phased reads, backfills, and careful cutover.
- Database growth introduces new unpredictability in capacity, hotspots, network behavior, and deployment choices.
