---
title: "Leader Election in Distributed Systems"
date: '2026-11-26T00:35:42+00:00'
category: webclip
summary: 'Explains pros and cons of leader election, how Amazon uses lease‑based mechanisms and sharding, how systems behave under leader failure, and concrete best practices.'
tags: ["distributed-systems", "leader-election", "fault-tolerance", "leases"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Leader Election in Distributed Systems"
    url: "https://aws.amazon.com/builders-library/leader-election-in-distributed-systems/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/aws-amazon-com--leader-election-in-distributed-systems-aws.md"
    kind: repo
---

The article describes leader election as assigning special responsibilities to a single component in a distributed system, such as coordinating work, owning mutations to data, or handling all requests. It outlines benefits like simpler reasoning, centralized concurrency control, easier consistency, and performance gains from a single coherent cache, but also costs such as single points of failure, scaling and trust bottlenecks, and deployment complications. Amazon often prefers alternatives like workflow services, idempotent APIs, and optimistic locking when they provide similar advantages without leader election’s risks, and when it does use leaders it frequently limits their scope with sharding, as in DynamoDB, Amazon EBS, and Amazon EFS.

Amazon mainly uses lease-based leader election, implemented over a shared database where a leader must periodically heartbeat to retain the lease, and candidates can take over when heartbeats stop. They avoid relying on globally synchronized time, using only local elapsed durations and being careful about how time is measured so assumptions about durations hold even with issues like clock drift or leap seconds. Making sure leaders only do work while they truly hold the lock is described as the hardest part, because slow or lossy networks and garbage collection pauses can cause leaders to overestimate remaining lease time. Amazon prefers battle-tested clients such as DynamoDB and ZooKeeper locking libraries instead of custom protocols. The text illustrates usage in RDBMS deployments with a write leader, in Amazon EBS primaries that order I/O for volume regions (with followers taking over on failure, similar to DynamoDB, Amazon QLDB, and Kinesis), and in the Kinesis Client Library using leases so each shard has a single processing owner.

The article emphasizes reasoning about leader failure and work handoff, ensuring work is made durable before being reported as complete, and using idempotency so new leaders can safely re-drive tasks. It notes that distributed systems cannot guarantee exactly one leader at all times, only that there is usually one, with possible intervals of zero or multiple leaders. Systems built around idempotent operations can accept periods with two leaders and use weaker election mechanisms, whereas systems that require at most one leader everywhere need stronger, always-correct and consistent election with careful handling of network partitions. Amazon’s best practices include frequent lease or lock checks, considering network slowness, timeouts, retries, and garbage collection effects, avoiding background-only heartbeating, maintaining metrics on leader capacity and load, keeping auditable records of leadership changes, and modeling and formally verifying algorithms with tools like TLA+.

## Reading notes

- Leader election gives one process, host, thread, object, or person special capabilities in a distributed system, such as assigning work, mutating data, or handling all requests.
- Using a single leader can improve efficiency, reduce coordination overhead, simplify architectures, and lower operational complexity.
- A leader centralizes concurrency control, reduces partial failure cases, and offers a single location for logs and metrics.
- Because a leader sees all state changes, it can more easily provide clients with consistent behavior.
- A system with a leader can cache data once at the leader, improving performance or reducing cost through a single consistent cache.
- Writing software that assumes one leader is often simpler than quorum-based approaches, since code can ignore concurrent modifications from peers.
- A leader is a single point of failure: if the system mismanages a bad leader, overall availability can be lost.
- Leader-based designs hit a single scaling point in both data volume and request rate, and growing beyond one leader often demands full re-architecture.
- A leader also concentrates trust; if it behaves incorrectly without checks, it can cause wide-ranging system issues with high blast radius.
- Practices like partial deployments, one-box tests, A/B testing, blue/green, and incremental rollouts with automatic rollback can be harder to apply in leader-elected systems.
- Choosing a leader’s scope carefully, such as through sharding, can alleviate some disadvantages by giving each data item a leader while having many leaders overall.
- Sharding, used by DynamoDB, Amazon EBS, Amazon EFS, and other systems, brings more design complexity and requires thoughtful decisions about how to partition data.
- Amazon considers alternatives such as AWS Step Functions for workflows, idempotent APIs, and optimistic locking before adopting leader election.
- Leader election can be implemented via consensus algorithms like Paxos, systems like ZooKeeper, custom hardware, or lease-based mechanisms.
- Leases are Amazon’s most common election mechanism because they are conceptually straightforward, relatively easy to implement, and include built-in fault tolerance.
- Lease implementations typically use a single database storing the current leader and require periodic heartbeats from the leader to retain its lease.
- When a leader fails to heartbeat within a configured time, other candidates can attempt to acquire the lease and become leader.
- Amazon avoids depending on synchronized clocks for ordering or coordination, even with EC2 time sync, and uses time only for human-facing purposes.
- Leases depend on local elapsed time, not global wall-clock time agreed among servers, which reduces reliance on time synchronization.
- The DynamoDB lock client provides concrete examples of leader election using leases.
- Correct lease and locking implementations are subtle and require careful understanding of how servers measure elapsed time.
- If a timing mechanism occasionally reports time moving backwards, assumptions about duration-based leases can be broken.
- Working with durations helps avoid issues from global clock problems such as leap seconds or clock drift under high CPU load.
- A central challenge in lease-based systems is ensuring leaders perform work only while they truly hold the lock.
- Leaders on slow or lossy networks must not assume they still hold leases longer than they actually do.
- Garbage collection pauses between lock checks and performing work can invalidate timing assumptions and lead to incorrect behavior.
- Hardening systems against slow networks and GC pauses often becomes the most significant practical challenge in leader-based designs.
- DynamoDB and ZooKeeper both offer simple lease-based locking clients suited for fault-tolerant leader election.
- Amazon teams generally avoid writing custom leader election systems and instead prefer widely used, thoroughly tested client libraries.
- Many systems using traditional RDBMSs employ leader election to choose a main database for writes and sometimes for reads.
- Database leader selection is sometimes automated but is often handled manually by operators.
- Amazon EBS stripes reads and writes over multiple storage servers and uses leader election to select primaries that order I/O for regions of a volume.
- In EBS, if a primary fails, follower replicas take over using the same leader election mechanism.
- DynamoDB, Amazon QLDB, and Kinesis apply similar leader-based techniques to ensure consistency and performance without heavy coordination on the data path.
- The Kinesis Client Library uses leases to ensure each Kinesis shard has exactly one owner process, simplifying scale-out stream processing.
- System design must address what happens if a leader fails mid-task and how a replacement leader can complete or redo that work.
- If a leader fails before persisting its results durably, designers must verify that the system’s behavior is still correct under that data loss.
- Many workloads separate making work durable from announcing completion, and Amazon systems always persist before signaling completion, or else they accept some data loss.
- Idempotent operations let new leaders safely re-run work that might already be partially or fully done but not acknowledged.
- Amazon views leadership as a role that moves between servers or processes, rather than a permanent property of a single node.
- In distributed systems, it is impossible to strictly guarantee exactly one leader at all times; during failures there can be no leader or multiple leaders.
- When two leaders can exist, system behavior depends on whether their actions remain correct or only affect efficiency.
- Systems with idempotent work can often tolerate periods of dual leadership while maintaining correctness, though possibly with extra work.
- Such systems can emphasize higher availability and rely on weaker leader election mechanisms.
- Systems that require at most one leader globally are more complex, because their leader election process must always be correct and consistent.
- These stricter systems must ensure the old leader truly loses leadership before a new leader becomes active, which is harder than it seems.
- Distinguishing between a failed leader and one still working in another network partition is difficult in distributed environments.
- Amazon requires leader-elected systems to explicitly handle edge cases where a supposed failure is actually a partition or delay.
- Best practices include checking remaining lease time or lock status frequently, especially before performing operations with external side effects.
- Designers must account for slow networks, timeouts, retries, and garbage collection pauses, which can cause leases to expire earlier than the code anticipates.
- Heartbeating leases solely from a background thread is discouraged because it can introduce correctness problems when that thread cannot interrupt work after expiration or dies while work continues, or vice versa.
- Systems should expose reliable metrics comparing potential leader throughput against actual work done, and teams should review these metrics and plan scaling before hitting capacity limits.
- It should be easy to determine which host is currently leader and to reconstruct leadership history through logs or audit trails.
- Amazon advocates modeling and formally verifying distributed algorithms, for example with TLA+, to uncover subtle, rare, and hard-to-observe bugs related to leader election assumptions.
- Amazon treats leader election as one of several patterns for building fault-tolerant, operable systems, alongside idempotency and optimistic locking.
- Teams focus on understanding both the guarantees and the limitations of chosen leader election protocols, rather than assuming properties that the protocols do not provide.
- In some systems, a backing database is used so that if two leaders both mistakenly believe they hold a lease, they still interact with shared state in a controlled way that preserves correctness.
- The article notes further reading about leases and distributed locking, including general guidance on distributed locking and research on lock services and lease-based cache consistency.

## Related notes

- [Leader and Followers](/notes/leader-and-followers-distributed-systems-pattern/)
- [Heartbeats in Distributed Systems](/notes/heartbeats-in-distributed-systems/)
- [Catalog of Patterns of Distributed Systems](/notes/catalog-of-patterns-of-distributed-systems/)
- [Notes on Distributed Systems](/notes/notes-on-distributed-systems/)
- [Why Distributed Systems Are Hard](/notes/why-distributed-systems-are-hard/)
