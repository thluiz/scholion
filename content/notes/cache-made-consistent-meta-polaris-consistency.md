---
title: "Cache made consistent"
date: '2026-11-25T16:13:59+00:00'
category: webclip
summary: 'Meta describes how it measures and improves cache consistency at massive scale using Polaris for observability and a targeted consistency tracing approach to debug invalidation bugs.'
tags: ["distributed-systems", "caching", "observability", "meta-infra"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Cache made consistent"
    url: "https://engineering.fb.com/2022/06/08/core-infra/cache-made-consistent/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/engineering-fb-com--cache-made-consistent-meta-polaris-consistency.md"
    kind: repo
---

The post explains why cache invalidation is hard in practice and why cache consistency matters for user-facing correctness, using Meta’s large TAO and Memcache deployments as context. It introduces a mental model of dynamic caches as stateful services whose state changes on both reads and writes, making race conditions common and full logging impractical. Meta improved TAO’s consistency from six to ten nines by building Polaris, a generic client-style observability service that measures client-visible consistency violations across timescales, and by adding a focused consistency tracing library that records only mutations in the small window where invalidation and cache fills can race. A concrete bug example shows how this tooling reduced diagnosis from weeks to minutes. The post closes with ongoing work toward near-perfect consistency, better handling of disaggregated secondary indices, read-time consistency improvements, and a high-level consistency API for distributed systems.

## Reading notes

- Caches are ubiquitous across devices and infrastructure, including phones, browsers, CDNs, and DNS, and they reduce latency, scale read-heavy workloads, and lower cost.
- Meta runs some of the largest cache deployments, such as TAO and Memcache, and has improved TAO’s cache consistency from 99.9999 percent to 99.99999999 percent by at least one measurement.
- The post focuses on caches with active invalidations; pure TTL-based freshness without invalidations is explicitly out of scope.
- Cache invalidation is defined as actively invalidating stale cache entries when the source-of-truth data (for example, a database) mutates.
- If invalidation is mishandled, the cache can hold values that permanently diverge from the source of truth.
- Cache invalidation requires an external actor, like a client or pub/sub system, to inform the cache that a mutation occurred.
- A simple race example shows how a cache fill reply with old data can arrive after an invalidation with newer data, leaving the cache indefinitely inconsistent.
- Version fields can support conflict resolution by preventing older data from overwriting newer data, but eviction can remove the version knowledge and undermine this approach.
- The difficulty of cache invalidation stems both from complex protocols and from the challenge of monitoring and understanding inconsistencies in production.
- The authors compare designing a consistent cache to designing Paxos: having a protocol on paper differs from building a system that operates reliably in production.
- Cache inconsistencies can be nearly as harmful as database data loss and, from a user’s perspective, may look indistinguishable from losing data.
- A TAO messaging example shows a split-brain scenario where inconsistent cache replicas after reshuffling a user’s primary message store left messages split across regions, so no single region contained a complete history.
- The post proposes a mental model where caches are stateful services within distributed state machines; correct state transitions yield correct behavior, while flawed transitions cause problems.
- Static caches with immutable data and no invalidations (such as a simplified CDN) are a much simpler case than dynamic caches.
- Databases mutate state through writes and replication and typically log almost every state change, which aids anomaly diagnosis.
- Dynamic caches like TAO and Memcache mutate data on both read (cache fills) and write (invalidations) paths, enabling many possible race conditions.
- Cache data is not durable, so important versioning information for conflict resolution can be lost through eviction.
- This combination of non-durability and read/write mutation introduces a wide variety of race conditions.
- At Meta’s scale, exhaustive logging of cache state changes is considered almost impractical, because cache fills dominate the workload.
- TAO serves more than one quadrillion queries per day; even with a 99 percent hit rate, over 10 trillion cache fills per day would generate excessive logging load.
- Logging every state change in such a cache would flip a read-heavy workload into a very write-heavy logging workload.
- Debugging distributed caches is especially hard because of both the system’s complexity and the lack of full state-change logs.
- Despite these challenges, Meta reports improving TAO’s consistency from six to ten nines, and the remainder of the post explains the methodology behind this improvement.
- The first step in addressing cache invalidation is to measure cache consistency and detect inconsistent entries without allowing false positives.
- False positives in consistency alerts are considered dangerous, because engineers may learn to ignore a noisy signal, undermining trust in the metric.
- Precision is required to measure consistency up to more than 10 nines and to quantify improvements after fixes.
- Meta built Polaris, a service that focuses on anomalies visible to clients and measures violations of client-observable invariants.
- Polaris treats the target stateful system as a black box, interacting only as a client and assuming no internal knowledge, which allows it to be reused for many systems.
- At Meta, Polaris has dozens of integrations and commonly monitors invariants like “cache should eventually be consistent with the database,” especially with asynchronous invalidation.
- For caches, Polaris acts as a cache server to receive invalidation events, then queries cache replicas as a client to check for inconsistencies after each event.
- If Polaris sees a replica with an older version than the invalidation event, it flags the sample as inconsistent and rechecks it later against the same host.
- Polaris reports consistency at multiple timescales such as one, five, or ten minutes, and only counts a sample as inconsistent once it remains inconsistent across a timescale boundary.
- The multi-timescale architecture enables internal queues, backoff, and retries, and it is described as essential to avoiding false positives.
- When Polaris sees an invalidation but the cache reports no value for the key, the situation is ambiguous: it might indicate inconsistency or simply that a later deletion occurred.
- Disambiguating such cases requires bypassing the cache and querying the database, which is compute-intensive and risky because it can increase load on the database that the cache is meant to protect.
- To limit database impact, Polaris delays these cache-bypassing checks until a sample crosses a reporting timescale and remains inconsistent despite retries.
- True permanent inconsistencies and racing writes on the same key are rare, so retries usually resolve ambiguity without extra database queries.
- Polaris tags its queries so cache servers can indicate whether they have seen and processed the associated invalidation event.
- This extra bit of information lets Polaris distinguish transient inconsistencies caused by lag from situations where a stale value remains after processing the latest invalidation.
- Polaris exposes metrics like “N nines of cache writes are consistent in M minutes,” tying the earlier TAO 10-nines claim specifically to a five-minute timescale.
- For TAO, Polaris reports that 99.99999999 percent of cache writes are consistent within five minutes, meaning fewer than one in ten billion writes is inconsistent after that interval.
- Polaris runs as an independent service so that its scalability is decoupled from the target production service and its workload.
- Increasing the number of measured nines is possible by raising Polaris throughput or aggregating data over longer windows.
- In practice, cache systems have complex topologies with multiple upstreams, regions, and dependencies, even though diagrams often depict them as a single box.
- Many operational events, such as promotions, shard moves, recoveries, network partitions, or hardware failures, can cause cache inconsistencies.
- Because full logging of every data change is impractical, the authors seek a narrower place and time where logging yields maximum benefit for diagnosing inconsistencies.
- They focus on the perspective of a single cache server, which mainly needs to know whether it received and processed invalidations correctly and whether items became inconsistent afterward.
- A space-time diagram of the earlier race example highlights a limited window after a client write during which invalidation and cache fills can race at the cache host.
- Once past this window, the cache enters a quiescent state in terms of writes; fills may continue in volume but do not have the same consistency implications.
- Meta implemented a stateful tracing library that logs and traces cache mutations only within this narrow race window where inconsistencies can emerge.
- The tracing system covers cache evictions, and even missing logs can indicate that an invalidation never arrived.
- This tracing capability is embedded in major cache services and in the invalidation pipeline, giving coverage along the critical paths.
- The library buffers an index of recently modified data to decide whether subsequent cache state changes should be traced.
- It also supports code tracing, revealing the precise code path taken by each traced query when diagnosing issues.
- This approach has reportedly uncovered many flaws and offers a more systemic and scalable way to diagnose cache inconsistencies.
- A concrete bug example describes a system where each piece of data is versioned to support ordering and conflict resolution.
- In that system, they observed the cache containing metadata value 0 at version 4 while the database had metadata value 1 at version 4, and the inconsistency persisted indefinitely.
- Such a state should not occur given the versioning logic, so the team needed a detailed timeline to understand how it happened.
- Consistency tracing provided a complete sequence of steps leading to the inconsistent cache state.
- In the system, a rare operation updates two database tables (metadata and version) transactionally.
- According to the trace, the cache first filled old metadata and then a write transaction atomically updated both database tables.
- Next, in a second round, the cache filled the new version data, interleaving with the ongoing database transaction in a small race window.
- The authors state that this interleaving is not the underlying bug, because the invalidation logic is supposed to restore consistency afterward.
- Later, the cache invalidation attempted to update the cache entry with the new metadata and version, which usually succeeds.
- In this case, the invalidation encountered a rare transient error on the cache host, triggering an error handler.
- The error handler used logic like `drop_cache(key, version)` to drop items whose version is less than the specified version.
- Because the cached item already had the latest version, that error handler call did nothing, leaving stale metadata indefinitely in cache.
- The real bug was therefore in the error-handling code, which failed to correct the inconsistent item when the version matched.
- The description notes that the real scenario was more intricate, involving database replication and cross-region communication, and required a precise sequence of events to manifest.
- The bug was extremely rare and buried behind interleaved operations and transient errors, which would historically have been very hard to root-cause.
- The authors claim that in the past, tracing down such a bug might have taken weeks for an expert engineer, assuming it was found at all.
- In this incident, Polaris detected the anomaly and raised an alarm immediately, and consistency tracing let on-call engineers find the root cause in under 30 minutes.
- The post concludes with goals to push cache consistency as close to 100 percent as physically possible across Meta’s caches.
- Future work areas include addressing consistency challenges for disaggregated secondary indices and improving cache consistency at read time.
- Meta is also working on a high-level consistency API for distributed systems, compared conceptually to C++’s `std::memory_order`, but oriented toward distributed environments.
