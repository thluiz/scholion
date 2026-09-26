---
title: "System Design — Tips"
date: '2025-05-17T22:09:32+00:00'
category: webclip
summary: 'A practical list of system design choices for scalability, availability, latency, and reliability, with examples showing when to use caches, queues, sharding, replication, and other patterns.'
tags: ["system-design", "scalability", "availability", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "System Design — Tips - Javarevisited - Medium"
    url: "https://medium.com/javarevisited/system-design-tips-62c26366cf48"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-05/medium-com--system-design-tips.md"
    kind: repo
---

The post collects system design tips around core trade-offs: understand functional and non-functional requirements, pick an architecture, and then choose patterns for scale, caching, storage, availability, security, and communication. It also pairs each choice with a concrete scenario such as read-heavy, write-heavy, low-latency, or globally distributed systems.

## Reading notes

- Define both functional and non-functional requirements before choosing the design.
- Choose between monolith and microservices, and consider layered architecture for separation of concerns.
- Scale horizontally, vertically, and with load balancing.
- For databases, balance normalization and denormalization, choose SQL or NoSQL based on the data, and use sharding when needed.
- For distributed locks, set a TTL, renew locks when necessary, and use tools like Redis, ZooKeeper, or etcd.
- Use caching and CDNs to reduce latency and database load.
- Build for fault tolerance with redundancy, failover, backup, and recovery.
- Secure the system with authentication, authorization, encryption, firewalls, and intrusion detection.
- Monitor performance and keep logs for debugging and analysis.
- Use RESTful APIs for stateless services and message queues for asynchronous communication.
- For low-latency video delivery, combine cache and CDN, with multi-region CDN for scale.
- For read-heavy systems, cache popular data with TTL.
- For write-heavy systems, use message queues and background workers.
- Use NoSQL for unstructured data, SQL for ACID transactions, and object storage for videos, images, and files.
- Use a load balancer for high availability and an API gateway for microservices.
- Add indexes for faster queries, checksum algorithms for integrity, data lakes or append-only databases for analytics and audit trails, and data replication for fault tolerance.
- Use WebSockets for real-time chat, heartbeats for failure detection, consistent hashing for cluster scaling, gossip protocol for decentralized updates, eventual consistency for availability, pagination for large lists, and autoscaling for traffic spikes.
