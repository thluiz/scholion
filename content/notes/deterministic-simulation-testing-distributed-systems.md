---
title: "Deterministic Simulation Testing"
date: '2026-11-17T16:33:20+00:00'
category: webclip
summary: 'Article shows how deterministic, tick-driven simulation of clock, network, disk and processes lets you reproduce gray failures, inject seeded faults, and check distributed-system correctness, not just availability.'
tags: ["distributed-systems", "testing", "fault-injection", "simulation"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Deterministic Simulation Testing"
    url: "https://martinfowler.com/articles/deterministic-simulation-testing.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/martinfowler-com--deterministic-simulation-testing-distributed-systems.md"
    kind: repo
---

Deterministic simulation testing addresses why subtle bugs in distributed systems evade conventional tests and even powerful chaos tools. The article argues that the hardest failures stem from gray failures and nondeterministic interleavings of time, threads, network, and disk. By running the whole cluster on a single thread against simulated clock, network, and storage, tests can control progress explicitly, inject faults reproducibly using seeded randomness, and check client-visible histories for correctness properties like linearizability.

A concrete Java implementation, Tickloom, demonstrates the approach. Core protocol logic runs single-threaded on a `tick()` loop, talks only to abstract `Network`, `FileIO`, and `Clock` interfaces, and uses custom non-blocking futures. Simulation swaps in in-memory implementations of these interfaces, enabling precise control of message delivery, delays, partitions, disk durability, and crashes. Strict coding rules and architectural fitness functions keep the core deterministic, while production adapters can use real threads and I/O as long as they funnel completions back through the tick loop.

## Reading notes

- Standard unit and integration tests focus on component logic and happy-path interactions, but they do not capture what clients observe when partial failures overlap with in-flight requests.
- In distributed environments, assumptions about reliable networks and clean failures break down; components experience partial crashes, pauses, asymmetric partitions, packet loss, and localized latency spikes.
- These gray failures create rare event interleavings that break otherwise robust systems, and traditional tests cannot reliably generate such degraded conditions on demand.
- Chaos engineering validates availability under disruption by killing nodes or disturbing traffic, asking whether service stays up and recovers.
- Correctness differs from availability: a system can remain responsive while returning stale or corrupted data that break its advertised consistency guarantees.
- The article uses a three-node quorum store example to show how a network partition can cause a client to read stale data even though a write has already been acknowledged.
- Jepsen focuses on correctness from the client's perspective by injecting faults into a live system, recording operation histories, and checking these against claimed semantics.
- Live fault injection helps find bugs but makes them hard to reproduce because of random fault schedules and execution nondeterminism.
- Even with a seeded random fault schedule, live runs differ due to wall-clock timing, OS thread scheduling, and network or disk behavior, leading to different execution traces.
- Four main external nondeterminism sources are identified: system clock, thread scheduling, network timing, and disk timing, each changing when events become visible.
- Timeouts and retries depend on clocks whose behavior varies between runs, so the same code can see different elapsed times and cross or miss a timeout boundary.
- OS-level thread scheduling inside and across processes alters which handler runs first, so concurrent operations can observe different states in different runs.
- Network buffering, congestion, retransmission, and routing cause messages to be delivered in different orders or with different delays, changing read outcomes.
- Disk writes complete at OS page cache time, not necessarily when data is durable, so identical crashes can yield different recovery data depending on flush timing.
- Internal sources like unseeded randomness or iteration over unordered collections also add nondeterminism but can be controlled by coding rules rather than simulation.
- Real systems make progress because CPU, network card, and disk independently advance, and tests do not directly control these progress mechanisms.
- Deterministic simulation replaces real infrastructure with simulated clock, processes, network, and disk, all advanced only when the test calls `tick()`.
- In the simulated world, the test decides when time advances, which process runs, when messages are delivered, and when writes become durable.
- This explicit control makes it straightforward to model both hard failures (crashes, partitions) and routine slowdowns like latency spikes.
- Tickloom is introduced as a Java library that implements deterministic simulation for teaching and testing distributed systems, inspired by FoundationDB and TigerBeetle.
- The design centers on single-threaded execution: each process runs on one thread in both production and test, driven by an explicit `tick()` loop.
- The `Tickable` interface abstracts components whose progress is controlled; calling `tick()` advances their internal work without blocking.
- The main tick thread must not block, so all network and storage calls are asynchronous, with a custom future that avoids blocking methods and background threads.
- Production network code uses Java NIO for non-blocking sockets, and blocking file operations run on a background thread but report back as events processed during ticks.
- Protocol code talks to the network via an abstract `Network` interface and a `Message` record, rather than using sockets directly.
- `Network.send()` is asynchronous, queuing outbound messages; incoming messages are delivered to processes by calling their `onMessage()` method.
- There are two `Network` implementations: `SimulatedNetwork` for tests and `NioNetwork` for production, both honoring the same non-blocking contract.
- `SimulatedNetwork` tracks `NetworkLink`s between process pairs and associates them with partitions, packet loss configurations, congestion windows, and fault rules.
- When sending, the simulated network checks whether a link is partitioned, matches a fault rule, or should drop packets, discarding messages accordingly.
- Messages that are not dropped are enqueued with a computed delivery tick and sequence number in a priority queue for deterministic FIFO ordering.
- On each `tick()`, the simulated network increments its internal tick counter, applies any dynamic fault changes, and delivers all messages due for that tick.
- Messages due at the same tick are delivered in the order they were enqueued, by routing them to the destination `Process` via `deliver` and `onMessage()`.
- Processes communicate exclusively through the shared network using `ProcessId` identifiers, both in production and simulation.
- A process gets a `Network` instance in its constructor and registers itself so the network can route messages to it.
- Message handling is structured via a map from `MessageType` to handler functions; subclasses provide handlers through `initialiseHandlers()`.
- The `QuorumReplica` process demonstrates a set of handlers for client requests and internal quorum protocol messages.
- When `onMessage()` runs, it checks process state, logs or handles uninitialized states, and dispatches to the appropriate message-type handler on the main thread.
- Handlers execute to completion on the single thread, send messages through the network, and receive responses later as separate messages.
- Timeouts are modeled as tick-based counters rather than relying on wall-clock time or monotonic clocks to keep behavior deterministic.
- The `Timeout` class maintains a tick count since start and marks itself expired when the configured duration in ticks has elapsed.
- Processes use a Request Waiting List pattern to track in-flight requests associated with their own `Timeout` instances.
- When a request is added, the waiting list creates and starts a tick-based timeout and stores it along with the callback.
- On each tick, the waiting list advances all timeouts, determines which requests expired, and completes them with a `TimeoutException`.
- The `QuorumReplica` example uses a quorum write where a client send is coordinated by one replica that waits for a majority of acknowledgments or a timeout.
- In simulation, a test can build a three-node `Cluster` of quorum replicas, configure timeouts in ticks, and set up network isolation and delays between replicas.
- A test isolates one replica and delays a specific link so that the acknowledgment always arrives after the coordinator's timeout, causing the write to fail deterministically.
- The `Cluster` test helper encapsulates building nodes with a shared simulated network, advancing process clocks, and ticking clients, servers, and networks in order.
- Test code drives simulation with `tickUntil`, which loops, ticking the cluster until a condition is met or a maximum tick limit is reached, instead of sleeping.
- By adjusting network delay relative to timeout, the test can ensure that a write consistently fails or consistently succeeds across runs.
- Injecting random faults in simulation uses a seeded pseudorandom number generator to ensure repeatable fault schedules.
- `SimulationDecisions` encapsulates probabilities for issuing client requests, injecting faults, and periodic network healing, all driven by a `Random` instance.
- Helper methods in `SimulationDecisions` choose fault types, target nodes, and delays using the shared seed-based random source.
- `SimulationRunner` wires up `SimulationDecisions` with a cluster size and clients, using the provided seed to initialize the random generator.
- During each tick in `runClusterFor`, the runner increments a tick counter, injects random faults if conditions hold, ticks the cluster, and may issue a client request.
- `FaultInjectingSimulationRunner` implements `injectRandomFaults` by occasionally resetting network conditions or introducing faults like node isolation, pair partitions, link delays, and drop rules.
- Using a fixed seed produces the same sequence of faults, and because execution is deterministic, the same client-visible history is produced on reruns.
- Recording structured logs of injected faults and per-tick events helps diagnose bugs by examining exact interleavings, even without rerunning with a debugger.
- In production, each tick corresponds to a fixed real-time interval (e.g., 10ms or 100ms), so long-running tests take real time to exercise timeouts and retries.
- Simulation advances ticks in a tight loop without waiting for wall-clock time, letting long logical durations be explored in seconds.
- This fast-forward capability allows a large number of fault combinations and rare interleavings to be tested practically.
- Correctness checking uses client-visible histories of operations to validate invariants like linearizability through external checkers.
- A Jepsen-like format records each operation as an `:invoke` followed by an `:ok`, `:fail`, or timeout event, including process id, function, and value.
- After a simulated run with faults, the `SimulationRunner` feeds the recorded history to a `ConsistencyChecker` configured for a linearizable register.
- If the checker flags a violation, the saved seed can reproduce the exact faulty execution sequence for debugging.
- File system simulation follows the same pattern as the network, with an asynchronous `FileIO` interface abstracting file operations.
- `FileIO` methods like `read`, `write`, `sync`, `size`, `truncate`, and `close` return futures instead of blocking.
- A completed write future indicates data is visible to subsequent reads, while a completed sync future guarantees durability across crashes.
- In tests, `SimulatedFileIO` wraps a `SimulatedFile` and schedules operations in a queue advanced on `tick()`.
- `SimulatedFile` keeps separate `visible` and `durable` byte arrays, modeling written-but-unsynced data versus on-disk durable data.
- Reads and writes operate on `visible` data, and `sync()` copies `visible` to `durable` to commit changes.
- Simulating a crash resets `visible` back to `durable`, discarding any unsynced writes and enabling deterministic crash/recovery tests.
- `SimulatedFileIO` methods enqueue closures that perform operations on `SimulatedFile` and complete futures when `tick()` drains the queue.
- The `tick()` implementation processes only operations queued before the tick, ensuring callbacks triggered by completions run on later ticks.
- The system uses a custom `TickCompletableFuture` instead of Java's `CompletableFuture` to avoid blocking calls and background executors.
- Standard futures risk deadlocking the tick loop via `get()` or `join()`, and asynchronous combinators can reintroduce thread scheduling nondeterminism.
- `TickCompletableFuture` exposes non-blocking composition and forbids execution on background threads, preserving the single-threaded model.
- Deterministic simulation requires architectural buy-in: core logic must be single-threaded and interact with infrastructure through well-defined interfaces from the beginning.
- Interfaces like `Network`, `FileSystem`, `FileIO`, and `Clock` form a seam between the deterministic core and the operating system.
- Production implementations behind this seam can use threads, executors, and real clocks, as long as results are delivered back to the core via the tick loop.
- Six coding rules are proposed to keep the core deterministic: no direct system clock calls, no unseeded randomness, no threads or standard futures, no direct I/O, no iteration over unordered collections, and no cross-thread callbacks into the core.
- To keep iteration order stable, core state uses `LinkedHashMap` and `LinkedHashSet` instead of unordered hash-based collections when iterating.
- Cross-thread callbacks are explicitly forbidden; background I/O threads may not complete futures or call into protocol code directly.
- `IOThread` is cited as an example where the background disk thread enqueues completions, which the main thread processes during `tick()`.
- Automated architectural fitness functions enforce these rules rather than relying on human discipline.
- Static fitness tests using ArchUnit (e.g., `DeterminismRulesTest`) run on every build to ensure core packages do not violate determinism constraints.
- Static analysis cannot see which thread executes lambdas at runtime, so runtime checks are added to enforce thread confinement for futures.
- `TickCompletableFuture` records the owning thread and throws exceptions if `complete`, `fail`, or `whenComplete` are called from a different thread.
- Once static and runtime checks ensure determinism, the seeded fault-injecting simulation and correctness checker together act as a holistic fitness function for distributed correctness.
- The single-threaded design does not necessarily degrade production performance; many distributed systems are I/O bound and benefit from this event-loop style.
- Single-threaded event loops with asynchronous, batched I/O reduce locking and context switching and are used by systems like Redis, FoundationDB, and TigerBeetle.
- The main trade-off is that protocol handlers on the tick thread must avoid blocking or long CPU work, and scaling across cores is done by running multiple processes.
- Structuring the core around deterministic simulation can make protocols easier to write and evolve, since logic is plain single-threaded code decoupled from low-level OS concerns.
- The approach encourages heavy use of random fault scenarios as a safety net during evolution, turning these tests into a fitness function for future changes.
- Deterministic simulation is also presented as a powerful tool for learning and teaching distributed systems.
- With libraries like Tickloom in place, LLMs can serve as a natural-language interface to generate executable scenario tests from descriptions or textbook diagrams.
- The article mentions using an LLM to translate a linearizability anomaly scenario from "Designing Data-Intensive Applications" into a Tickloom test that models link delays and partitions.
- Executable simulation harnesses make it easier to explore tricky corner cases that are usually only drawn as diagrams, supporting deeper understanding.
