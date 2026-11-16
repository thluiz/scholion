---
title: "Why Distributed Systems Are Hard"
date: '2026-11-16T04:36:58+00:00'
category: webclip
summary: 'Denise Yu traces how cloud, microservices, and growing data needs made distributed systems unavoidable, then explains latency, partial failures, CAP, and the human factors that shape resilient design.'
tags: ["distributed-systems", "cap-theorem", "microservices", "human-factor"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why Distributed Systems Are Hard"
    url: "https://infoq.com/presentations/distributed-systems-complexity-human-factor"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/infoq-com--why-distributed-systems-are-hard.md"
    kind: repo
---

Denise Yu argues that distributed systems became unavoidable as software, data, and teams grew more complex. She links cloud computing, horizontal scaling, and microservices to the need to handle latency, partial failures, and design choices that affect resilience.

## Reading notes

- Microservices often turn one team into the operator of a large distributed system.
- Distributed systems became more important as software moved from cost center to business differentiator.
- Customer data, analytics, machine learning, and caches increased the need for distributed storage and retrieval.
- Vertical scaling eventually hits financial and hardware limits, so cloud systems made horizontal scaling practical.
- Horizontal distribution is used for scalability, availability, and lower latency.
- Shared-nothing design and message passing reduce shared-memory assumptions.
- Local computing and distributed computing differ because of latency, memory access, and partial failures.
- Networks are unreliable, latency is not zero, bandwidth is finite, and topology can change.
- Message delivery can fail through spoofing, drops, corruption, and partitions.
- CAP is about trade-offs under partition events, not a simple choice of any two properties.
- Consistency is not binary, and different definitions imply different guarantees.
- Availability depends on whether clients can keep updating data when connected to a node.
- Partition tolerance is unavoidable unless the system has only one node.
- During a partition, a system can either keep serving both sides and lose linearizability or pause writes and lose availability.
- Hardware failures, software pauses, and shared-host resource contention can look like network outages.
- The FLP result and consensus limits shape the way distributed systems are managed.
- Leader-follower designs, leader election, failover, and consensus rules are used to contain uncertainty.
- More fault tolerance usually means more complexity.
- Woods’ Theorem is used to describe how a system’s complexity reduces the accuracy of any single mental model.
- Incident reviews should be blameless and should focus on learning rather than fault.
- Counterfactuals are not useful as incident findings because they are hypothetical.
- Human operators are adaptable and are part of the system’s resilience.
