---
title: "Notes on Distributed Systems"
date: '2020-08-26T19:31:26+00:00'
category: webclip
summary: 'The page condenses a lecture on distributed systems, covering scaling strategies, CAP tradeoffs, distributed transactions, computation, synchronization, consensus, and messaging tools such as Hadoop, Spark, Paxos, and Kafka.'
tags: ["distributed-systems", "scaling", "consensus", "messaging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Notes on Distributed Systems"
    url: "https://dev.to/svemaraju/notes-on-distributed-systems-3e4"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--notes-on-distributed-systems.md"
    kind: repo
---

The page collects lecture notes on distributed systems and groups them by topic: storage, computation, synchronization, consensus, and messaging. It frames distributed systems through concurrency, independent failure, and the lack of a global clock, then walks through common tools and tradeoffs in each area.

## Reading notes

- Distributed systems are presented as collections of computers that look like a single system to users, with concurrent operation, independent failure, and no shared global clock.
- Read replication uses one write instance and multiple read replicas, but replication lag can create consistency problems, so eventual consistency is often accepted for scale.
- Sharding splits data across multiple leaders when one write leader can no longer keep up, but relational systems are harder to shard and scatter-gather queries become costly.
- Consistent hashing is described as the basis for systems like Dynamo and Cassandra, where each node handles a range of keys and data is replicated to neighboring nodes.
- The consistency tradeoff is summarized with R + W > N, where read and write quorum sizes determine whether strong consistency is guaranteed.
- CAP theorem is used to distinguish consistency, availability, and partition tolerance, with partition tolerance treated as unavoidable.
- Distributed transactions split work to improve throughput, but they trade atomicity for higher parallelism.
- Scatter/gather moves computation closer to data, and the page contrasts MapReduce, Hadoop, Spark, and Storm by batch or stream processing use.
- Hadoop is described as fitting very large, mostly analytical workloads, with HDFS, a single NameNode, and immutable blocks.
- Spark is presented as a more general programming model with transform and action, while Storm is used for real-time stream processing with at-least-once semantics.
- Lambda architecture combines real-time streaming into a queue with long-term storage for batch analysis, then writes analyzed data into a warehouse or NoSQL store.
- Network Time Protocol estimates time by accounting for network latency, while vector clocks track sequence numbers to resolve conflicts in concurrent updates.
- Distributed consensus is defined around termination, validity, integrity, and agreement, and Paxos is described as a deterministic fault-tolerant algorithm for durable mutable state.
- Kafka is introduced as a distributed message queue with topics, producers, consumers, brokers, and partition-based ordering.
- Zookeeper is described as a centralized service for configuration and distributed synchronization, with shared state and a leader-follower model.
