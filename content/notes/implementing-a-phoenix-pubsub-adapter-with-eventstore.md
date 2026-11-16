---
title: "Implementing a Phoenix PubSub Adapter with EventStore"
date: '2020-07-05T14:10:38+00:00'
category: webclip
summary: 'The post shows how to build a Phoenix PubSub adapter on EventStore, trading speed for persistence and node decoupling, and explains the callbacks, metadata, and serialization needed to route broadcasts across nodes.'
tags: ["phoenix-pubsub", "eventstore", "elixir", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Implementing a Phoenix PubSub Adapter with EventStore"
    url: "https://erlang-solutions.com/blog/how-to-write-a-phoenix-pubsub-adapter-tutorial-example-based-on-eventstore.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/erlang-solutions-com--implementing-a-phoenix-pubsub-adapter-with-eventstore.md"
    kind: repo
---

The post explains how to back Phoenix PubSub with EventStore so nodes can exchange messages through a shared database instead of Erlang distribution. It highlights two main gains from this approach: broadcasts are persisted for replay or auditing, and multiple nodes can run without configuring Erlang node connectivity.

It also describes the main costs: storage is required and each broadcast adds a database round-trip, so the design fits lower-throughput messaging better than high-speed delivery. The article then walks through the adapter callbacks, the GenServer setup, the use of event metadata for source and destination nodes, and the pluggable serializer used to preserve message data and type fidelity.

## Reading notes

- EventStore is used as the PubSub backend to distribute messages across nodes through PostgreSQL.
- The approach avoids Erlang distribution and keeps broadcasts in a persistent event log.
- The adapter is presented as a proof of concept, with no load tests performed.
- A Phoenix PubSub adapter must implement callbacks such as node_name, child_spec, broadcast, and direct_broadcast.
- Phoenix PubSub subscriptions use Elixir Registry, while the adapter is responsible for delivering messages to other nodes.
- The adapter is implemented as a GenServer that joins the PubSub supervision tree.
- The PubSub name is kept separate from the adapter name because they serve different roles.
- broadcast appends an event to EventStore, and direct_broadcast adds destination_node and source_node metadata.
- source_node is stored for auditing, while destination_node is used to route delivery.
- Serialization is pluggable, and the default serializer base64-encodes term_to_binary output.
- The serializer is needed because EventStore stores JSON and JSON does not preserve atom and string distinctions.
- The adapter subscribes to $all so it can receive events from the store.
- A transient subscription is used because earlier messages are not needed.
- A unique id is stored in state so the adapter can skip dispatching messages it originated itself.
- The event metadata includes source_id, dispatcher, and any destination_node needed for routing.
- When events come back from EventStore, the adapter deserializes them and calls Phoenix.PubSub.local_broadcast for the intended subscribers.
