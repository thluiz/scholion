---
url: "https://dev.to/svemaraju/notes-on-distributed-systems-3e4"
captured_at: "2026-11-16T01:06:24+00:00"
title: "Notes on Distributed Systems"
domain: "dev-to"
---

[![Cover image for Notes on Distributed Systems](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fyszwq67zzwpev6zo9ar1.jpg)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fyszwq67zzwpev6zo9ar1.jpg)

[![Srikanth](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F23695%2F129887f7-57e5-49b8-84ac-482361194daf.JPG)](https://dev.to/svemaraju)

[Srikanth](https://dev.to/svemaraju)

Posted on Jul 6, 2020 Edited on Jul 6, 2020

Notes from [Tim Berglund's lecture](https://learning.oreilly.com/videos/distributed-systems-in/9781491924914).

## [](#introduction)Introduction:

*   Collection of computers that looks to the users as a single one - Tannebaum.
*   Three characteristics: Computers operate concurrently. Computers fail independently. Computers do not share a common global clock (async).

#### [](#categories)Categories

Distributed Storage: Mongo, Cassandra, HDFS etc.  
Distributed Computing: Hadoop, Spark, Storm etc.  
Distributed Synchronization: NTP, vector clocks  
Distributed Consensus: Paxos (algorithm), Zookeper (tool)  
Distributed Messaging: Kafka (pub/sub)

## [](#whywhen-do-we-go-for-distributed-systems)Why/When do we go for Distributed Systems:

*   Coffee shop analogy is helpful in explaining scaling problems.
*   Distributed systems are hard.

#### [](#single-storage)Single Storage:

At low scale a single master storage works perfectly well (Taking orders on a single piece of paper, updating or adding new orders etc.)

#### [](#read-replication)Read replication

*   First strategy to scale system with single master storage.
*   Multiple replicas for read. Single instance for write, each write is copied to every replica. (Leader - Follower)
*   When things go wrong: replication can fail, replication is not simultaneous across every follower.
*   Consistency problem: Single storage is strongly consistent. Eventual consistency is tradeoff in real world for scalability.
*   Read replication solves for the problem of heavy read work load with relatively less write work load.

#### [](#sharding)Sharding

*   Sharding is usually a strategy used when read replication is no longer feasible.
*   Writes on a single Leader instance no longer able to keep up with the incoming workload. Need splitting up of write workload.
*   Split data into different sets which can be assigned to multiple Leaders. Each Leader will have multiple Followers.
*   Relational systems are hard to shard. NoSQL like MongoDB have baked in features that handle sharding.
*   All related data needs to be present in one shard for it to be accessed. For eg: A SaaS application can have shard based on Users - i.e. all data related to a group of users can be present within a shard.
*   Analytical queries like aggregation will not work well with shards. Queries need to read every shard to fetch all data. This is called Scatter-Gather. Efficiency is dependent on nature of data access patterns, too much scatter-gather is not good.

#### [](#consistent-hashing)Consistent Hashing

*   AWS Dynamo and Cassandra are designed to be scalable from ground up using a consistent hashing approach, may also be referred to as distributed hash tables.
*   Moving away from Leader-Follower pattern.
*   Each node has equal responsibilities - Read and Write.
*   Each node will be responsible for a certain range of data broken up by some unique key.
*   Data divided on the basis of hashing the unique key.
*   Hashing allows us to uniformly distribute the data across nodes.
*   Each node is aware of its own range, and the ranges of preceding and succeeding nodes.
*   Nodes can be added easily to handle scale.
*   For replication: Each data is replicated to preceding and succeeding nodes to allow redundancy. In case of replication failure there will be inconsistent data. We can configure the system to ensure an acceptable state of consistency. Formula for guaranteeing strong consistency: R + W > N. N is the number of replicas, W is the number of nodes that need to acknowledge at the time of write, R is the number of nodes that agree (have the same data) at the time of read. Depending on what we are looking for in the tradeoff we can modify the relationship between R, W and N. In case we are looking for low latency R + W may not be greater than N.
*   What if when there is not enough agreement? Entropy problem. This varies by implementation of the system.
*   When do we use a consistent hashing systems: When scale is extremely important problem to solve. Data model should be able to fit this system. Transactional data (Data that changes a lot.). Need for an always on system.

#### [](#cap-theorem)CAP Theorem

*   Consistency, Availability and Partition Tolerance.
*   Consistency: Read should always fetch the latest successful update.
*   Availability: The service should always be available to take requests.
*   Partition Tolerance: Network Partition i.e. certain parts of the distributed system lose connectivity with others. Unavoidable in real world. Distributed Systems should be tolerant to such partitions.
*   All three cannot be achieved at once.
*   P is non negotiable.
*   C and A need to be part of a trade off.
*   CP - System sacrifices availability for consistency (Banking)
*   CA - System sacrifices consistency for availability (Social Media)

#### [](#distributed-transactions)Distributed Transactions

*   ACID transactions (Atomic, Consistent, Isolated, Durable)
*   Atomic - transaction is complete fully or not at all i.e. no partial executions.
*   Consistency - not same as in CAP theorem. When a transaction is complete the database is not broken.
*   Isolation - parallel transactions on same data do not overlap. For eg: when a row is being updated, a simultaneous read will not see the updated data. In real world isolation not simple: there are 4 levels of isolation a relational database systems usually offer. Implementation details vary.
*   Durability - When a transaction is complete, you can read the updated data i.e. the data is stored in durable way.

Splitting the work (i.e. splitting a transaction):

*   Achieve parallel workloads.
*   Optimize for uneven workload.

Distributed transactions trade off Atomicity for higher throughput.

#### [](#distributed-computation)Distributed Computation

*   Scatter/Gather: Move the computation closer to the data. Moving data all to one place is expensive.
*   MapReduce (algorithm), Hadoop (batch processing tool), Spark (batch processing tool), Storm (stream processing tool / real time).

##### [](#mapreduce)MapReduce

*   All computation are performed in two functions: Map and Reduce.
*   Keep data where it is. (mostly)
*   Move the computation closer to the data.

##### [](#hadoop)Hadoop

*   Provides an interface to MapReduce.
*   Includes a distributed filesystem - HDFS.
*   Developed into an ecosystem. (HBASE, HIVE, PIG etc)
*   HDFS: Single Name Node (contains master information of where data is stored), Multiple Data Nodes. Data is stored as immutable blocks.
*   When to use? Huge data volume (Data doesn't fit on one node). Lower data velocity (low velocity i.e. analytical data.). Non-critical latency SLA. Not for realtime jobs.

##### [](#spark)Spark

*   Similar Scatter/Gather approach to MapReduce.
*   More general programming model (transform/action) which in concept is similar to MapReduce but has flexible and more support in performing varied actions.
*   Follows a more general data model (RDDs)
*   Storage agnostic

##### [](#storm)Storm

*   Real time stream processing.
*   At-least-once processing semantics.
*   Horizontally scalable, fault tolerance.
*   Developed to process Twitter feed.

##### [](#lambda-architecture)Lambda Architecture

*   When there is high rate of events that need to be stored and analyzed (both in batch and real time.)
*   Data is simultaneously streamed into a real time queue (distributed queue like Kafka) and also written into a long term storage for batch processing.
*   Input data (events) is immutable.
*   Functional programming paradigm for batch and stream processing.
*   Eventually analyzed data get written into a DB (data warehouse, NoSQL store.)
*   Name derived from lambda calculus relating to the functional paradigm.

#### [](#distributed-synchronization)Distributed Synchronization

*   Important when nodes don't agree on writes, for eg: find the last updated data.
*   Estimate the time: GPS, Network Time Protocol
*   Derive the time logically: vector clocks

##### [](#network-time-protocol)Network Time Protocol

*   Accurate clock on the internet to read from.
*   But network latency is variable
*   NTP measures and accounts for latency to provide accurate time.
*   Layers of Strata: Stratus 0 (atomic clock +/- 10ns latency to read), Stratus 1 (server attached to stratum 0, +/- 5us latency), Stratum 2 (servers that sync to stratum 1, present at some distance, +/- 10ms) and so on. Accuracy around 10 ms

##### [](#vector-clocks)Vector Clocks

*   A means of proving sequence of operations. (Not a means of telling time.)
*   We are concurrently modifying one value
*   Every actor tracks a sequence number.
*   When there is a conflict the application needs to resolve the conflict based on comparing sequence numbers in the conflicting data.
*   Explanation using a coffee place example - [https://riak.com/why-vector-clocks-are-easy/](https://riak.com/why-vector-clocks-are-easy/)
*   Vector clocks cannot get the sequence of operations wrong.
*   Complexity is pushed to the application (client)

#### [](#distributed-consensus)Distributed Consensus

*   We are looking for agreement between concurrent, async and failure prone processes.
*   4 requirements: Termination (every process must terminate in deciding a value), Validity (if all processes propose a value, then all processes decide that same value), Integrity (If a process decides a value, then that value must have been proposed by another process), Agreement (all processes must agree on the same eventually.)

##### [](#paxos-algorithm)Paxos Algorithm

*   Deterministic and fault tolerant consensus algorithm.
*   Useful in replicating a durable, mutable state ie for databases.
*   Guarantees a consistent result.
*   Read: If all or majority agree then we get a result, else we get a failure to read.
*   Write: The primary node (proposer) proposes a write to multiple nodes (acceptors) along with a sequence number. In positive scenario, the acceptors will reply with a promise to accept further writes only with a greater sequence number than the one they received. Proposer send an accept request with the same value and sequence number. Acceptors recheck and sends acceptance. In the conflict scenario, if one of the acceptors has a sequence number greater than one proposed it will send back a promise with that sequence number instead of the one proposed. The proposer will then re-evaluate and send back the accept request with the updated sequence number which is greater than the initial one, and hence the conflict is resolved with acceptors sending back the acceptance.
*   Other protocols: Raft, Blockchain (when people are lying to you intentionally)
*   Use cases: Lightweight transactions in Cassandra, Clustrix, BigTable's "Chubby" lock manager

#### [](#distributed-messaging)Distributed Messaging

*   Loosely coupling subsystems
*   Producer <-> Subscriber
*   Topics
*   Usually persistent over the short term
*   Challenges: If topic gets too big for a computer, then ordering of messages will be a problem. If one computer is not reliable enough, replication comes into the picture. How strongly can we guarantee a delivery?

##### [](#kafka)Kafka

*   Distributed message queue.
*   Horizontally scalable, fault tolerant, durable, fast.
*   Message: immutable array of bytes.
*   Topic: a feed of messages.
*   Producer: publishes messages to a topic.
*   Consumer: a single threaded process that subscribe to a topic.
*   Broker: one of the server in a Kafka cluster.
*   Topic Partitioning: Partition is decided on the basis of key of the message and a "partitioner" that gets assigned at the producer level. Consumers read from a defined partition. Order is maintained only within a partition.

##### [](#zookeper)Zookeper

*   Centralized service for maintaining configuration information, providing distributed synchronization etc.
*   Manages shared state. (Transaction control, lock management)
*   Written on Java, Data is in-memory (on-heap)
*   Leader-Follower model.
*   All nodes do read and write.
