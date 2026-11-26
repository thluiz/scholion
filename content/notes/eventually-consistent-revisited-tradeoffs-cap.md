---
title: "Eventually Consistent - Revisited"
date: '2026-11-25T16:19:41+00:00'
category: webclip
summary: 'Explains consistency models in large-scale distributed systems, the CAP trade-offs, and how eventual consistency and its variants support availability, performance, and fault tolerance.'
tags: ["distributed-systems", "consistency-models", "eventual-consistency", "cap-theorem"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Eventually Consistent - Revisited"
    url: "https://www.allthingsdistributed.com/2008/12/eventually_consistent.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/allthingsdistributed-com--eventually-consistent-revisited-tradeoffs-cap.md"
    kind: repo
---

The article examines how large-scale distributed systems, such as Amazon's infrastructure services, must balance strict requirements for availability, performance, and durability against the limits imposed by replication and network partitions. Using the CAP theorem as a backdrop, it explains why systems operating at global scale often relax consistency and adopt eventual consistency and its variants, and how these choices affect application developers.

It distinguishes client-side views of consistency from server-side replication behavior, defines several consistency models, and relates them to quorum-style replication parameters (N, W, R). It also discusses how real systems, including RDBMSs and Amazon's Dynamo, use these ideas to tune inconsistency windows and trade-offs among consistency, availability, and performance.

## Reading notes

- Amazon's core cloud services (S3, SimpleDB, EC2) are built as large, globally distributed systems that must meet strict demands on security, scalability, availability, performance, and cost while serving millions of customers continuously.
- At very large scale, rare events become inevitable, so distributed-system designs must anticipate low-probability failures, especially when using replication for performance and availability.
- Replication helps achieve performance and availability but exposes customers to consistency effects, especially when services adopt an eventual consistency model.
- The author aims to describe background principles for large-scale replication and the trade-offs between high availability and data consistency that guide Amazon's system design.
- Early distributed databases in the 1970s focused on distribution transparency and often preferred failing the whole system over exposing distributed behavior to clients.
- In the mid-1990s, with large Internet systems, designers re-examined these practices and started treating availability as a key property that needed to be traded against something else.
- Eric Brewer's CAP formulation states that a shared-data system cannot simultaneously provide data consistency, availability, and partition tolerance; only two of the three are achievable at once.
- Formal work by Seth Gilbert and Nancy Lynch confirmed that in partition-tolerant systems, strong consistency and availability cannot both be guaranteed.
- Systems without partition tolerance can achieve consistency and availability using transactional protocols, but this assumes clients and storage fail together so partitions are not observable.
- In large distributed systems, network partitions must be assumed, so designers must choose between prioritizing availability with weaker consistency or prioritizing consistency at the cost of availability.
- If a system emphasizes consistency, client developers must handle cases where operations such as writes are rejected because the system is unavailable to maintain guarantees.
- If a system emphasizes availability, writes are often accepted even during partitions, but subsequent reads may temporarily miss recent updates, and developers must decide whether slightly stale data is acceptable.
- The ACID notion of consistency differs from these distributed consistency models; it refers to application-level invariants (such as account balances) holding after a transaction, often enforced partly by the developer and integrity constraints.
- The client-side consistency discussion assumes a large-scale, highly distributed storage system treated as a black box that guarantees durability and availability.
- Three independent processes (A, B, C) read and write objects in the storage system, and client-side consistency describes when these processes observe each other's updates.
- Strong consistency means that after an update completes, all subsequent reads by any process return the new value.
- Weak consistency provides no immediate guarantee that reads will see the latest update and introduces an "inconsistency window" between an update and the point when all observers will reliably see it.
- Eventual consistency is a form of weak consistency where, if no new updates occur, all replicas will eventually return the last updated value, with the window size influenced by communication delays, load, and replication fan-out.
- DNS is cited as a widely used eventual consistency system, where updates propagate according to configured patterns and caching, so clients eventually see changes.
- Causal consistency ensures that if process B learns from A that an update occurred, B will see that update on subsequent accesses, and B's writes will supersede A's; processes without this causal link follow normal eventual consistency behavior.
- Read-your-writes consistency guarantees that a process always sees its own most recent updates and never older values; this is framed as a special case of causal consistency.
- Session consistency offers read-your-writes guarantees within the lifetime of a session, but if a session ends due to failures, a new session does not inherit these guarantees.
- Monotonic read consistency ensures that once a process has observed a particular value, it will not later see an older value for that object.
- Monotonic write consistency guarantees that a single process's writes are applied in order, so its updates are serialized; systems lacking this are described as very difficult to program against.
- Variants such as monotonic reads and read-your-writes can be combined (for example, with session-level guarantees) and are often the most helpful properties in eventual consistency systems.
- Whether any given combination of these client-side guarantees is necessary depends on the application's tolerance for inconsistent or stale data.
- Eventual consistency is common beyond large-scale NoSQL systems; traditional RDBMSs with primary-backup replication often use asynchronous log shipping, which yields windows where a promoted backup can serve stale data.
- RDBMS features that allow reads from backups to improve scalability are presented as a classical case of eventual consistency, with inconsistency windows tied to log shipping intervals.
- On the server side, consistency behavior can be characterized using N (replica count), W (write acknowledgments required), and R (replicas read per operation).
- If W+R>N, read and write sets overlap and strong consistency can be guaranteed; for synchronous primary-backup RDBMS with N=2, W=2, R=1, every read gets a consistent value.
- In asynchronous primary-backup setups where N=2, W=1, R=1, reads from the backup can return stale data because R+W=N, so strong consistency is not guaranteed.
- Quorum-style configurations suffer from unavailability when writes cannot reach W replicas; for example, with N=3 and W=3, if only two nodes are reachable, write operations must fail.
- Distributed storage systems with high availability and performance often use N>2, with N=3 (W=2, R=2) common for fault-tolerance-focused configurations.
- Systems that serve very high read loads may use many replicas (N in tens or hundreds) with R=1 to return a result from any single replica, while setting W=N prioritizes consistency at the cost of more frequent write failures.
- Some systems concerned with fault tolerance but not strict consistency use W=1 for minimal durability and propagate updates lazily to remaining replicas using epidemic-style protocols.
- The choice of N, W, and R should reflect the dominant workload path; R=1, W=N favors read performance, while W=1, R=N makes writes very fast but weakens durability and increases the possibility of conflicting writes.
- Weak or eventual consistency arises when W+R<=N, because reads and writes may not overlap, leading to possible reads from replicas that have not yet received updates.
- In systems with heavy read replication, setting R>1 in an eventual consistency configuration offers little benefit if the read set may still miss the updated replicas.
- In more complex data models (such as returning sets of objects instead of single key-value pairs), determining the correct latest result is harder, and lazy propagation is used, defining an inconsistency window until all replicas are updated.
- Achieving read-your-writes, session consistency, or monotonic reads often depends on how consistently a client is routed to the same server that manages its protocol state.
- Sticky sessions, where a client repeatedly interacts with the same server, make it easier to ensure read-your-writes and monotonic reads but complicate load balancing and fault tolerance.
- Clients themselves can enforce read-your-writes and monotonic reads by tagging writes with versions and discarding values from reads that carry older version numbers.
- Network partitions are described as situations where subsets of storage nodes cannot reach each other, yet separate groups of clients can still access each subset.
- In majority quorum schemes, only the partition containing a majority of the replica set can continue to accept writes and serve consistent reads, while the minority partition becomes unavailable.
- Although partitions are not constant, they occur inside and between data centers and must be planned for in the system design.
- Some applications cannot tolerate any partition-induced unavailability and must allow progress on both sides, assigning new storage nodes to continue accepting writes and later merging divergent state.
- Amazon's shopping cart is given as an example of a write-always system that continues to accept cart updates during partitions and relies on the cart application to help merge carts when connectivity is restored.
- Amazon's Dynamo is presented as a key-value store that makes consistency, durability, availability, and performance trade-offs explicit and tunable for each application instance, often across multiple data centers.
- The article concludes that inconsistency must be tolerated both to improve performance under high concurrency and to keep partitions from making live nodes unusable under majority rules.
- Whether inconsistency is acceptable depends on the application, and developers must understand the specific guarantees provided by storage systems when building against them.
- Practical refinements to eventual consistency, including session-level consistency and monotonic reads, can give developers more predictable behavior without sacrificing high availability.
- Many applications can work within eventual consistency guarantees, and some Web applications rely on user-perceived consistency where the inconsistency window is shorter than the typical interval between user page loads.
- The author emphasizes that global-scale systems require careful tuning of durability, availability, and performance, and that controlling the length of the inconsistency window is one of the key design levers available.
