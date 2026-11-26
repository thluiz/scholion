---
title: "Caching challenges and strategies"
date: '2026-11-26T00:32:34+00:00'
category: webclip
summary: 'AWS article describing when to use caches, trade-offs of local vs external and inline vs side caches, and concrete practices for TTLs, errors, security, and resilience.'
tags: ["caching", "distributed-systems", "system-design", "aws"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Caching challenges and strategies | AWS Builder Center"
    url: "https://aws.amazon.com/builders-library/caching-challenges-and-strategies/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/aws-amazon-com--caching-challenges-and-strategies-aws-builder.md"
    kind: repo
---

AWS teams describe how services can become dependent on caches: a cache added to fix latency, cost, or throttling issues quietly turns into a critical component, so cache outages or cold states can overload downstream systems and cause wider outages.

They outline when caching is appropriate, how to choose between local and external and between inline and side caches, and specific practices for sizing, TTLs, error handling, security, and evolving cache data formats.

## Reading notes

- Caches often start as an optimization for slow or expensive dependencies but can become critical; a cold or unavailable cache can suddenly shift traffic to dependencies and trigger outages.
- The core risk comes from modal behavior: performance and load patterns differ depending on whether data is cached, and unexpected shifts between modes can be dangerous.
- Caching is useful when a dependency’s latency or throughput is a concern and when repeated requests reuse the same data so that a high hit ratio is achievable.
- If requests mostly use unique queries with per-request results, cache hit rates stay low and a cache brings little benefit.
- Teams must assess how tolerant their service and its clients are to eventual consistency, because cached data inevitably drifts from the source.
- Data that changes slowly can be stored longer in caches, while faster-changing data needs shorter cache durations.

- Local, in-process caches are easy to add, incur no extra operational fleet, and are often the first approach when introducing caching.
- A common pattern is an in-memory hash table managed in application logic or built into a caching client (such as an HTTP client with integrated caching).
- Local caches suffer from cache coherence issues across servers; clients may see newer data on one request and older data on another depending on which server responds.
- Downstream load stays proportional to the number of servers because each server’s local cache generates misses independently, which can still overload dependencies.
- Emitting metrics for hits, misses, and downstream request counts helps reveal whether a local cache is actually protecting dependencies.
- New servers with empty local caches can cause cold start bursts, especially during deployments or fleet-wide cache flushes.
- Request coalescing, where only one request fetches an uncached item while others wait, mitigates both coherence and cold cache problems.

- External caches (for example, Memcached or Redis) centralize cached values, reducing cross-server inconsistency compared to purely local caches.
- Because all servers share an external cache, aggregate load on dependencies is lower and no longer scales linearly with fleet size.
- External caches avoid per-server cold starts during deployments because the cache fleet stays warm as servers roll.
- They typically provide more storage than per-process memory, so space-related evictions happen less often.
- External caches add system complexity and operational effort, since the cache fleet itself must be monitored, managed, and scaled.
- The cache fleet’s availability profile may differ from the backing dependency and can be lower if it requires maintenance windows or lacks zero-downtime upgrades.

- Service code must handle cache fleet or node failures and cache get/put errors; a naïve fallback to the dependency during a cache outage can overload and brown out that dependency.
- One strategy is combining an external cache with a local cache so the local cache serves as a fallback when the external cache is unavailable.
- Another strategy is to apply load shedding and cap the request rate sent to dependencies, limiting blast radius during cache issues.
- Teams test behavior with caching disabled to confirm that protections against dependency brownouts actually function.

- As traffic grows, cache fleets approach request rate or memory limits and must scale; teams identify leading metrics like CPU to trigger scaling alarms.
- Load tests with realistic traffic are used to determine capacity limits and configure alarm thresholds, such as CPU thresholds for Redis.
- Adding cache capacity must avoid outages or mass data loss; some cache technologies cannot scale clusters without downtime, and some clients lack consistent hashing.
- Teams thoroughly test adding and removing cache nodes in non-production environments because client implementations of consistent hashing and node discovery can vary.

- Cached data is treated similarly to persistent storage; new software versions must be able to read entries written by older versions, and old versions must handle newer formats gracefully.
- Serialization logic must avoid uncaught exceptions on unexpected formats, otherwise “poison pill” entries can repeatedly crash or disrupt consumers.
- Simply discarding entries with format mismatches can trigger mass refreshes, which spike downstream traffic and increase throttling or brownout risk.
- Issues around serialization formats and rollback safety tie into the broader topic of safe deployments and cache compatibility across versions.

- Caches lack features like conditional writes or full transactions, so cache update code must prevent leaving entries in invalid or inconsistent states when multiple nodes update the same keys.

- Inline (read-through/write-through) caches hide cache management behind the data access API, so clients use a single uniform interface.
- With inline caches, caching can be enabled, disabled, or adjusted without changing client code, and cache logic is removed from application code paths.
- HTTP caching is cited as an attractive inline option because there are many client libraries, proxy servers, and CDN-based solutions.
- The transparency of inline caches can hurt availability because clients cannot easily react when an inline cache becomes unavailable; from their perspective, the underlying dependency seems to fail.
- If an external HTTP cache fleet (for example, Varnish) in front of a REST service fails, calling services see failures as if the REST service itself were down.
- Inline caches must be built into or closely coupled with the protocol or service; where no such integrated option exists, teams would have to build their own client or proxy to gain inline behavior.

- Cache design involves selecting TTLs (expiration policy), cache size, and eviction policy; absolute time-based TTL per object is a common approach.
- TTL choices reflect how stale data can be for clients and how static the underlying data is, since more static data can have longer TTLs.
- Cache size is estimated from expected traffic and object popularity distribution to achieve a high hit ratio.
- LRU is described as the most common eviction policy when capacity is reached.

- Since models may not match real traffic, teams track metrics for cache hits and misses, total cache size, and downstream request counts.
- Cache sizing and TTL values should not be arbitrary “one-time” choices; teams revisit and validate these settings based on observed behavior.
- Real-world outages have occurred because initial TTL and size choices were never reconsidered or tuned.

- A resilience pattern uses two TTLs: a soft TTL to trigger refresh attempts and a hard TTL as a maximum lifetime for cached data.
- When a refresh at soft TTL fails because the dependency is unavailable, the client continues serving the current cached value until the hard TTL expires.
- AWS IAM clients are given as an example of using separate soft and hard TTLs.
- The same soft/hard TTL pattern combined with backpressure helps manage dependency brownouts: when a dependency signals backpressure, callers rely on cached data and only request uncached items.
- Callers maintain this behavior until the dependency removes backpressure, helping the downstream service recover while upstream services stay available.

- Error handling strategy is an important design choice: one option is to serve the last known good cached value when the dependency returns errors, potentially using the soft/hard TTL scheme.
- Another option is a negative cache: cache error responses for some TTL and propagate errors to clients instead of refetching repeatedly.
- Which strategy to use depends on whether it is better for clients to see stale data or explicit errors for that use case.
- Regardless of the choice, the cache should hold something on error paths; otherwise, persistent errors cause repeated attempts and can worsen or trigger outages.
- AWS teams observed incidents where ignoring negative cache entries led to higher failure rates because services kept hitting an already failing dependency.

- Security aspects include verifying encryption and transport security for external cache fleets, especially where sensitive data is stored.
- Some cache fleets historically lacked encryption at rest or in transit; using services like Amazon ElastiCache for Redis can mitigate this with built-in encryption options.
- Caches can be vulnerable to poisoning attacks, where an attacker exploits protocol flaws to insert malicious values that all subsequent requests will read.
- Caches are also exposed to side-channel timing attacks because responses for cached entries are faster, revealing information about other clients’ request patterns.

- The “thundering herd” problem occurs when many clients request the same uncached resource simultaneously or when new servers with empty caches join the fleet.
- This burst of misses can overload dependencies and cause throttling or brownouts.
- Request coalescing is used so that only one in-flight request fetches an uncached value while others share its result, limiting duplicate work.
- Some cache libraries and inline caches such as Nginx or Varnish support request coalescing natively, and it can also be built atop existing cache solutions.

- Amazon teams emphasize validating that a cache is justified with concrete improvements in cost, latency, or availability and that data can be reused across requests.
- They recommend treating cache fleets like any other critical infrastructure: monitor hit rates and resource usage, set alarms, and verify that scaling can occur without downtime or invalidation.
- Cache size, TTLs, and eviction policies should be tuned empirically using metrics and tests, not left as guesses.
- Services must be resilient when caches are unavailable or cold, even if that means limited availability to prevent dependency brownouts; load tests with caches disabled help confirm this behavior.
- Teams consider encryption, transport security, poisoning, and timing side-channel risks whenever cached data is introduced.
- Cache object formats should be versioned and deserializers written to handle older versions safely while avoiding poison pills and large-scale cache invalidations.
- Handling downstream errors includes possibly using negative caching with different TTLs so that repeated failing requests do not overload dependencies.

## Related notes

- [Cache made consistent](/notes/cache-made-consistent-meta-polaris-consistency/)
- [Caching things every Programmer must know](/notes/caching-things-every-programmer-must-know/)
- [How key-based cache expiration works](/notes/how-key-based-cache-expiration-works/)
- [Eventually Consistent - Revisited](/notes/eventually-consistent-revisited-tradeoffs-cap/)
- [Catalog of Patterns of Distributed Systems](/notes/catalog-of-patterns-of-distributed-systems/)
- [Notes on Distributed Systems](/notes/notes-on-distributed-systems/)
- [Why Distributed Systems Are Hard](/notes/why-distributed-systems-are-hard/)
