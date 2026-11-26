---
title: "Please stop calling databases CP or AP"
date: '2026-11-25T16:18:22+00:00'
category: webclip
summary: 'Kleppmann argues that strict CAP definitions rarely match real systems, making CP/AP labels misleading; instead we should drop CAP shorthand and use precise consistency and availability models.'
tags: ["distributed-systems", "cap-theorem", "consistency-models", "databases"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Please stop calling databases CP or AP — Martin Kleppmann’s blog"
    url: "https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/martin-kleppmann-com--please-stop-calling-databases-cp-or-ap.md"
    kind: repo
---

Martin Kleppmann argues that the CAP theorem, taken in its formal sense, is too narrow and misunderstood to meaningfully classify databases as CP or AP. CAP’s strict definitions of consistency (linearizability) and availability, its single-register model, and its focus on network partitions ignore many practical concerns such as latency, other kinds of faults, and richer operations. When those strict definitions are applied, many real systems turn out to be neither CAP-consistent nor CAP-available, so forcing them into CP/AP buckets distorts both the theorem and the systems. He suggests abandoning CP/AP labels and instead learning the broader literature on consistency, availability and fault-tolerance in order to reason about trade-offs with more precise terminology.

## Reading notes

- Jeff Hodges recommends using CAP to critique systems, leading many practitioners to label systems as CP, AP, or CA, but Kleppmann disagrees with using CAP that way.
- As a theorem, CAP depends on precise definitions from the original proof, not on informal marketing uses of “consistency” or “availability”.
- In CAP, consistency actually means linearizability, a strong guarantee unrelated to the C in ACID; linearizability’s informal rule is that later operations must not see an older state than already-observed operations.
- CAP-availability requires that every request to any non-failed node returns a non-error response, a stronger condition than typical notions of high availability or low downtime.
- Partition tolerance in CAP corresponds to operating over an asynchronous network that can delay or drop messages, which matches real networks and is not an optional property.
- CAP’s model covers a single read-write register and does not speak about multi-object transactions unless they can be reduced to one register.
- The only fault considered in the CAP theorem is a network partition between nodes; other failure modes such as crashes, disk issues, or software bugs lie outside its scope.
- CAP is silent on latency, even though users usually care about timely responses; CAP-available systems are allowed to respond arbitrarily slowly and still count as available under the theorem.
- If a system uses different meanings of consistency or availability than the CAP proof, the theorem no longer applies, and it cannot legitimately be used to justify design choices.
- Linearizability requires the system to behave as if there is a single up-to-date copy of the data, regardless of replication or caching, which demands significant coordination.
- Even modern CPUs do not provide linearizable access to RAM by default; programmers need explicit memory barriers, and checking linearizability empirically is difficult.
- In a replicated two-datacenter setup, a network partition forces a choice: continue accepting writes in both datacenters and lose linearizability, or direct all operations to one side and lose CAP-availability on the other.
- A system that sacrifices CAP-availability can still keep the application running if clients can be shifted to the side that remains consistent and reachable.
- Real-world availability SLAs (e.g., percent of successful responses within a latency bound) can be satisfied by both CAP-available and CAP-unavailable designs.
- Multi-datacenter systems often choose asynchronous replication and hence non-linearizable semantics primarily to avoid wide-area latency, not just to handle partitions.
- Standard single-leader replication in relational databases is not CAP-available, because clients that cannot reach the leader cannot write, even if they can read from followers.
- Allowing reads from asynchronous followers makes such systems non-linearizable, so they are neither CAP-consistent nor CAP-available under the theorem’s definitions.
- Snapshot isolation and MVCC implementations typically forgo linearizability to increase concurrency; PostgreSQL’s SSI offers serializability but still not linearizability, and Oracle provides weaker guarantees than that.
- ACID branding does not imply CAP-consistency, since ACID’s “consistency” is a different concept than linearizability.
- Under strict CAP definitions, many popular systems end up as neither CP nor AP, effectively just “P”, even though this label is rarely used because it sounds undesirable.
- MongoDB, with single-leader shards, is not CAP-available, and empirical testing has shown it can return non-linearizable reads even under its strongest consistency settings.
- Dynamo-style systems like Riak, Cassandra, and Voldemort can be CAP-available when configured with R=W=1, but quorum configurations (R+W>N) lose CAP-availability on the minority side of a partition.
- Quorum configurations in these systems do not reliably guarantee linearizability due to features like sloppy quorums and read repair, which can produce edge cases such as resurrected deletes or broken quorum assumptions.
- These systems are widely and successfully used despite not fitting cleanly into CP or AP categories, and their classification can depend on operation type or configuration.
- ZooKeeper is often described as a CP system due to its consensus-based protocol, but its default read behavior does not provide linearizability.
- By default, each ZooKeeper client reads from its connected server node without ensuring that node is fully up to date, gaining speed at the cost of CAP-consistency.
- ZooKeeper can provide linearizable reads when clients explicitly issue a `sync` before reading, but this is not the default because it reduces performance.
- For writes, ZooKeeper requires a majority quorum; nodes in the minority side of a partition cannot process writes, so writes are not CAP-available even though nodes are alive.
- ZooKeeper’s read-only mode allows minority-side nodes to continue serving reads without quorum, making read operations CAP-available in that mode.
- In its default configuration, ZooKeeper is neither CAP-consistent nor CAP-available; with `sync` it becomes CP for some operations, and with read-only mode it behaves like AP for reads.
- Labeling ZooKeeper as simply “not consistent” under CAP mischaracterizes it, because it actually offers strong guarantees including atomic broadcast and causal consistency.
- ZooKeeper’s guarantees exceed basic sequential consistency and combine stronger session guarantees than read-your-writes, monotonic reads, or consistent prefix alone.
- As a result, ZooKeeper exemplifies a system that does not fit cleanly as AP or CP even in the presence or absence of partitions, and more fine-grained models like PACELC are not necessarily more helpful for classification.
- The difficulty of classifying real datastores as clearly AP or CP suggests that these categories are the wrong abstraction for describing systems.
- Within a single system, different operations can have different consistency behavior, which a single CP/AP label cannot capture.
- Many real systems are neither CAP-consistent nor CAP-available, yet developers avoid calling them just “P”, even though such designs can be entirely reasonable.
- Trying to force systems into CP/AP buckets encourages people to quietly redefine consistency or availability so that CAP appears to apply, which voids the theorem’s relevance.
- Reducing a system’s behavior to CP or AP loses important subtleties in fault-tolerance, latency, programming model, and operational behavior that strongly affect design.
- ZooKeeper’s read-only AP mode still preserves a total order of historical writes, which is a much stronger guarantee than the AP behavior of Riak or Cassandra; lumping them together is misleading.
- Eric Brewer later pointed out that CAP was originally intended as a way to start a discussion about trade-offs, not as a precise classification scheme for data systems.
- Since 2000, the ecosystem of distributed data systems and consistency models has grown richer, so CAP has outlived its usefulness as a central framework.
- To replace CP/AP labels, Kleppmann recommends learning more detailed concepts from the literature, rather than adopting a single new slogan.
- Doug Terry’s paper using baseball to explain variants of eventual consistency is suggested as an accessible introduction to finer-grained consistency levels.
- Kleppmann’s Hermitage project explores transaction isolation levels, which relate to but differ from replica consistency.
- Work by Peter Bailis and collaborators connects replica consistency, isolation, and availability, and explains consistency hierarchies widely referenced in discussions.
- The post includes numerous references to research papers and suggests using them to deepen understanding rather than relying on oversimplified theorems.
- Kleppmann mentions his own book as a secondary route for those unwilling to read original papers, and he recommends a specific book for learning to use ZooKeeper correctly.
- He closes by encouraging readers to patiently build an understanding of trade-offs in distributed systems architecture, and explicitly asks them to stop using CP/AP language because it no longer makes sense for modern systems.
