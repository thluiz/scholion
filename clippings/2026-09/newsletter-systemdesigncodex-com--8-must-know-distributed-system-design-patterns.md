---
url: "https://newsletter.systemdesigncodex.com/p/8-must-know-distributed-system-design?ref=dailydev"
captured_at: "2026-09-25T18:10:12+01:00"
title: "8 Must-Know Distributed System Design Patterns"
domain: "newsletter-systemdesigncodex-com"
---

Distributed Systems are important for building scalable, fault-tolerant, and highly available systems.

However, they introduce challenges such as managing the state, handling failures, and communication between services. To address these challenges, developers rely on well-established design patterns.

Let’s look at the most popular patterns:

The Ambassador Pattern focuses on offloading non-business-critical tasks from the main application to a helper service, known as the "ambassador."

*   The ambassador acts as a proxy between the application and external services or infrastructure components.
    
*   It manages tasks that are orthogonal to the core business logic, ensuring that the main service remains lightweight.
    

*   Simplifies the main application by removing repetitive tasks.
    
*   Improves observability with centralized logging and monitoring.
    
*   Enhances resiliency with features like automatic retries and circuit breaking.
    

In microservices architectures, an ambassador service can handle retries and timeouts when calling external APIs, ensuring the main service isn’t bogged down by such concerns.

The **Circuit Breaker Pattern** is a resiliency pattern used to prevent cascading failures in distributed systems. It monitors calls to a service and "trips" (stops requests) when the failure rate exceeds a predefined threshold.

*   When a service call fails repeatedly, the circuit breaker transitions to an **open state**, rejecting further requests.
    
*   After a cooldown period, it transitions to a **half-open state** to test if the service has recovered.
    
*   If successful, the circuit closes; otherwise, it remains open.
    

*   Protects services from overwhelming downstream dependencies.
    
*   Improves system stability by isolating failing components.
    
*   Enables faster recovery by reducing unnecessary traffic to struggling services.
    

An e-commerce platform can use a circuit breaker to prevent the order processing service from repeatedly calling an unresponsive payment gateway, preserving system resources.

Command Query Responsibility Segregation (CQRS) separates read and write operations into distinct models, optimizing each for its respective tasks.

*   The command model handles writes (e.g., creating or updating data).
    
*   The query model handles reads, often using precomputed, denormalized views for efficient querying.
    

*   Improves scalability by separating workloads for reads and writes.
    
*   Enables different data models and technologies for each operation.
    
*   Simplifies complex business logic by focusing on one responsibility per model.
    

An online store can use CQRS to handle high-volume read operations (product catalog browsing) separately from write operations (order placement).

Sharding splits a monolithic database into multiple smaller partitions, or shards, distributed across different servers. Each shard contains a subset of the data.

*   Data is partitioned based on a key (e.g., user ID or geographical region).
    
*   Each shard operates independently, handling its own subset of data.
    

*   Improves horizontal scalability by distributing workload across multiple servers.
    
*   Reduces single-point failures, as the failure of one shard doesn’t affect others.
    
*   Enhances performance by minimizing contention for resources.
    

A social media platform can shard user data by region, ensuring that localized traffic spikes don’t overwhelm the entire database.

The Sidecar Pattern involves deploying auxiliary components alongside the main service container. These sidecar containers handle cross-cutting concerns such as service discovery, logging, monitoring, or configuration management.

*   The main service and its sidecar container share the same host or pod (in Kubernetes).
    
*   The sidecar interacts with the main service through local communication mechanisms, such as shared memory or a local network.
    

*   Decouples auxiliary tasks from the main service, simplifying its development.
    
*   Enables consistent implementation of shared concerns across multiple services.
    
*   Facilitates microservices deployments by bundling related functionality.
    

A sidecar container can handle log aggregation for a microservice, sending logs to a centralized monitoring platform without impacting the service itself.

The **Publish/Subscribe (Pub/Sub)** pattern enables asynchronous communication between publishers (producers) and subscribers (consumers).

*   Publishers send messages to a **topic** or **event stream**.
    
*   Subscribers listen to the topic and process messages as they arrive.
    
*   A message broker (e.g., Kafka, RabbitMQ) manages the topics and ensures delivery.
    

*   Decouples producers and consumers, allowing independent scaling.
    
*   Supports real-time data streaming and event-driven architectures.
    
*   Enables multiple consumers to process the same event for different purposes.
    

An IoT platform can use Pub/Sub to collect data from sensors (publishers) and process it in real time using analytics services (subscribers).

In distributed systems, some tasks (e.g., managing shared resources or coordination) require a leader node. The Leader Election Pattern ensures that only one node assumes this role at a time.

*   Nodes in the system participate in a leader election process, often using consensus algorithms like Raft or Paxos.
    
*   Once elected, the leader coordinates tasks until it fails or resigns.
    

*   Prevents conflicts by ensuring a single source of truth.
    
*   Simplifies task coordination in distributed environments.
    
*   Enables fault tolerance by re-electing a new leader in case of failure.
    

A distributed database can use leader election to manage write operations, ensuring consistency across replicas.

**Event Sourcing** captures state changes as a series of immutable events rather than storing the current state directly. These events can be replayed to reconstruct the system’s state.

*   Each state change (event) is appended to an **event store**.
    
*   Consumers (e.g., query models) use these events to build views or perform analytics.
    

*   Provides a complete audit log of all state changes.
    
*   Supports replaying events for debugging or rebuilding state.
    
*   Simplifies implementation of CQRS, as the event store can feed the query model.
    

A financial application can use event sourcing to track every transaction, ensuring a reliable audit trail for compliance and reconciliation.

👉 **So - which patterns have you used?**

[Leave a comment](https://newsletter.systemdesigncodex.com/p/8-must-know-distributed-system-design/comments)

Here are some interesting articles I’ve read recently:

*   [Stop Pretending You Do Continuous Integration (Here’s What It Really Means)](https://open.substack.com/pub/akoskm/p/stop-pretending-you-do-continuous?r=1m1f9z&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) by [Akos Komuves](https://open.substack.com/users/50223467-akos-komuves?utm_source=mentions)
    
*   [Event Sourcing is like Time traveling](https://newsletter.systemdesignclassroom.com/p/event-sourcing-is-like-time-traveling?r=1m1f9z&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) by [Raul Junco](https://open.substack.com/users/98661477-raul-junco?utm_source=mentions)
    
*   [Building React Components: Turning UI Designs Into React Components](https://thetshaped.dev/p/building-react-components-turning-ui-designs-into-react-components?r=1m1f9z&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) by [Petar Ivanov](https://open.substack.com/users/10269058-petar-ivanov?utm_source=mentions)
    
*   [7 Cache Eviction Strategies You Should Know](https://blog.algomaster.io/p/7-cache-eviction-strategies?r=1m1f9z&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) by [Ashish Pratap Singh](https://open.substack.com/users/83602743-ashish-pratap-singh?utm_source=mentions)
    

**That’s it for today! ☀️**

Enjoyed this issue of the newsletter?

Share with your friends and colleagues.

[Share](https://newsletter.systemdesigncodex.com/p/8-must-know-distributed-system-design?utm_source=substack&utm_medium=email&utm_content=share&action=share)
