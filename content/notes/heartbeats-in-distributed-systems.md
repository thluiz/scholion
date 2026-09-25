---
title: "Heartbeats in Distributed Systems"
date: '2026-07-07T00:22:59+01:00'
category: webclip
summary: 'Explains how heartbeat messages help distributed systems detect alive, failed, or slow nodes, and compares push, pull, gossip, and quorum-based approaches.'
tags: ["distributed-systems", "heartbeats", "failure-detection", "gossip"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Heartbeats in Distributed Systems"
    url: "https://arpitbhayani.me/blogs/heartbeats-in-distributed-systems/?lid=4fnwkhygnsw8"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-07/arpitbhayani-me--heartbeats-in-distributed-systems.md"
    kind: repo
---

Heartbeats are periodic signals that let one component in a distributed system know another is still alive. The article frames them as a basic tool for failure detection, then shows how interval, timeout, and transport choices shape the trade-off between fast detection and false alarms.

It also compares push and pull models, fixed timeouts, phi accrual, gossip-based membership, and quorum handling during network partitions. Real systems like Kubernetes, Cassandra, and etcd use these ideas in different ways.

## Reading notes

- A heartbeat is a small periodic message that usually carries a timestamp, a sequence number, or an identifier.
- The receiver tracks when the last heartbeat arrived and treats a node as failed when it stops hearing from it within the expected window.
- Short intervals detect failures faster, but increase network traffic and sensitivity to brief congestion or pauses.
- Timeouts need to balance quick failure detection against transient delays; the article suggests using multiple missed heartbeats and sizing timeout to network round-trip time.
- In a push model, the node sends its own heartbeat to the monitor on a fixed schedule.
- In a pull model, the monitor checks a health endpoint on each node instead of waiting for heartbeats to arrive.
- Push is limited when the node is unresponsive or cannot initiate outbound connections.
- Pull gives the monitor more control, but increases load when many nodes are checked regularly.
- A fixed-timeout detector is simple, but can produce false positives in variable-latency networks.
- The phi accrual detector uses historical arrival times to produce a continuous suspicion level instead of a binary alive/dead result.
- Gossip distributes failure detection across nodes, with each node exchanging membership information with random peers.
- Gossip scales better than centralized monitoring, but information spreads gradually and different nodes can temporarily disagree.
- TCP offers reliability, while UDP is lighter and often acceptable when missing a few heartbeats is tolerable.
- Network topology matters, so local, same-datacenter, and remote nodes may need different interval and timeout settings.
- Network partitions can cause split-brain if both sides keep operating independently.
- Quorum-based handling prevents minority partitions from accepting writes or staying leader.
- Kubernetes node updates, pod liveness and readiness probes, Cassandra gossip, and etcd Raft heartbeats are cited as real-world uses.
