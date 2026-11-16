---
title: "Distributed Agreement on Random Order – Fun with Lamport Timestamps"
date: '2026-11-16T20:09:35+00:00'
category: webclip
summary: 'Explains Lamport timestamps and shows, via an Elixir multi-leader actor system, how nodes can eventually agree on a total order of events and use it as a deliberately wasteful sentence shuffler.'
tags: ["distributed-systems", "lamport-timestamps", "elixir", "actor-model"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Distributed Agreement on Random Order – Fun with Lamport Timestamps"
    url: "https://deque.blog/2018/09/13/distributed-agreement-on-random-order-fun-with-lamport-timestamps/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/deque-blog--distributed-agreement-random-order-lamport-ts.md"
    kind: repo
---

The article introduces Lamport timestamps as a simple algorithm to obtain a total order of events in a distributed multi-leader system without synchronized clocks. Each node maintains a logical counter, timestamps its local events, and updates its clock on receipt of replicated events so that all nodes can later sort logs by (time, origin) to get a consistent, causality-respecting history.

To illustrate this, the author builds an intentionally wasteful distributed sentence shuffler in Elixir. Words of a sentence are inserted as events across several worker processes (actors). Workers replicate their event logs via pub/sub, apply Lamport’s rules to update clocks and logs, and later return their histories sorted by timestamp and origin. This causes all workers to eventually agree on the same random ordering of the sentence’s words. The post walks through the Elixir actor implementation (init, handling add and get_history, processing replication_log), then shows an example shuffled sentence and a unit test asserting convergence. It closes by pointing to Lamport’s original paper, vector clocks, and related consensus work like Zookeeper Atomic Broadcast and Raft.

## Reading notes

- Introduces the challenge of ordering events in distributed systems when clocks cannot be accurately synchronized between devices.
- States the goal: in a multi-leader cluster, all nodes should eventually agree on a total order of events that matches causality.
- Defines causal constraints: within a node, earlier-processed events must come before later ones; across nodes, if a node knew about E1 when processing E2, E1 must be ordered before E2.
- Presents Lamport timestamps (Lamport clocks) as a simple algorithm that achieves such a total order.
- Describes the core algorithm: each node keeps a logical clock counter and increments it on event reception before tagging events with the current clock and origin.
- Explains replication: when sending an event replica, nodes transmit the event together with its timestamp and origin.
- On receiving a replicated event, a node sets its clock to one plus the maximum of its current clock and the event’s timestamp, then logs the event.
- Notes that after some time, all nodes have the same set of logged events, and sorting them by time and then origin yields a total order.
- Mentions that the full implications for ordering and causality are better covered by Wikipedia and Lamport’s original paper.
- Proposes an absurd example: using Lamport timestamps to shuffle the words of a sentence in a distributed multi-leader in-memory data store.
- Defines the data store behavior: workers process insertion commands for words, and writes are distributed across multiple nodes.
- Observes that if all nodes agree on insertion order for words, they effectively agree on an ordering of the sentence’s words.
- Emphasizes that this yields a random-looking shuffle of the sentence that all workers eventually share, despite being inefficient and lacking strong randomness properties.
- Lists the needed infrastructure: multiple worker replicas, a load balancer to dispatch insertions, and a pub/sub messaging system for log replication.
- Describes the workflow: requests go through the load balancer to workers, which publish replication logs via pub/sub to other workers asynchronously.
- Notes that, at the end, the load balancer queries each worker for its event history and can verify that they agree.
- Chooses Elixir as the language to implement this architecture and calls the task and architecture “stupid” and “perfect” respectively.
- Summarizes Elixir as a dynamically typed functional language on top of the Erlang BEAM VM, inheriting Erlang’s actor model, fault tolerance, and parallelism.
- Highlights similarities between Elixir and Clojure, including focus on data manipulation and macros for metaprogramming.
- States that Elixir’s easy actor instantiation makes it a good fit for the over-engineered shuffling algorithm.
- Gives an informal description of actors in Elixir: lightweight asynchronous processes with private state and garbage collection that communicate solely via messages.
- Analogizes actors to object instances whose methods are replaced by message passing and responses.
- Outlines the plan: implement worker actors that maintain known events and communicate via messages.
- Lists the messages workers must handle: add to insert a new word, get_history to return seen events, and replication_log to receive replicated logs.
- Notes that workers must also emit replication_log messages and maintain a logical clock to apply Lamport timestamps.
- Shows the worker init function that subscribes to the replication log topic and initializes state with a name, clock set to 1, and an empty event log.
- Explains that the event log captures what the worker believes happened, with entries storing payload, time, and origin.
- Presents the LogEntry struct with origin, time, and event fields as the type for log entries.
- Mentions that a more complete constructor would retrieve old history for workers started after events began, but this is omitted for simplicity.
- Introduces GenServer callbacks as the way actors handle specific message types, focusing on handle_call for synchronous requests.
- For get_history, shows a handle_call callback that takes the message, the sender, and the worker state.
- Inside get_history, the worker sorts its event log by timestamp and origin to compute the ordered history of events.
- Explains that handle_call returns a three-element tuple: response tag, reply payload (the sorted log), and the (unchanged) worker state.
- Concludes that get_history returns the worker’s view of the history without altering its state.
- For add, shows handle_call matching on {:add, event}, receiving a word as event payload.
- Describes constructing a new LogEntry tagged with the worker’s name as origin and its current clock as time, plus the event word.
- Updates the worker state by incrementing the logical clock and prepending the new log entry to the event log.
- Broadcasts the new log entry on the replication topic via pub/sub so that other workers can update their logs.
- Replies with :ok from handle_call to signal successful handling of the add request along with the updated worker state.
- For replication_log, presents a handle_info callback that matches messages of the form {:replication_log, logEntry}.
- Explains that because replication uses broadcast, the handler first checks if the log entry’s origin matches the worker’s name.
- If the worker is the emitter, it leaves the state unchanged; if not, it applies Lamport’s rule by updating the clock to max(current, logEntry.time) + 1.
- Appends (prepends in code) the replicated log entry to the worker’s event log when it comes from another worker.
- Returns a :noreply tuple from handle_info, indicating no reply is sent but the state may change.
- Notes that handle_info is used instead of handle_call for these asynchronous replication messages, following GenServer conventions.
- Indicates that some implementation details are omitted but full worker code is available in a linked gist.
- Adds that the only remaining elements are the pub/sub messaging layer and the load balancer, for which existing Elixir libraries like Phoenix.PubSub are used.
- States that small wrapper code around these libraries provides the needed infrastructure and links to another gist for this part.
- Points to a GitHub repository containing the complete project implementation.
- Provides an example sorted event log after sending a specific sentence to the system, showing word, origin PID, and logical time for each entry.
- Translates that example log into a concrete shuffled sentence, demonstrating how the random order looks from the worker’s perspective.
- Notes that this is just one sample shuffle and invites readers to try the code themselves using the GitHub project.
- Emphasizes that the key behavior is eventual agreement: regardless of the particular random order, all workers converge on the same sequence.
- Shows a unit test using Eventually.assertUntil, which periodically fetches histories from all workers and checks that they are equal.
- Interprets the passing test as evidence that the distributed shuffling algorithm achieves eventual consistency in ordering.
- Describes the result as a “buzzword compliant” distributed sentence shuffler based on Lamport timestamps.
- Encourages readers to read Lamport’s paper “Time, Clocks, and the Ordering of Events in a Distributed System,” praising its quality.
- Mentions that ordering notions from the paper are broadly useful in distributed systems, for example via vector clocks that detect concurrent updates.
- Notes that vector clocks help resolve write conflicts in distributed systems but can have their own issues, referencing a Cassandra-related critique.
- Cites another application in Lamport’s paper: implementing a replicated state machine with a limited, non–fault-tolerant consensus algorithm.
- Acknowledges that this older approach is superseded by more robust protocols like Zookeeper Atomic Broadcast and Raft.
- Closes by inviting readers to both read Lamport’s paper and try Elixir, expressing confidence they will find value in both.
