---
title: "Distributed PubSub in Elixir"
date: '2026-09-25T18:40:12+01:00'
category: webclip
summary: 'The article builds a local PubSub with Registry, then extends it to a clustered setup with pg and libcluster so each node relays messages to local subscribers.'
tags: ["elixir", "pubsub", "distributed-systems", "registry"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Distributed PubSub in Elixir"
    url: "https://papers.vincy.dev/distributed-pubsub-in-elixir?utm_medium=email&utm_source=elixir-radar"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/papers-vincy-dev--distributed-pubsub-in-elixir.md"
    kind: repo
---

The article walks through building a PubSub in Elixir from a local Registry-based version to a distributed version. It uses a named process registry for local subscriptions, then adds a per-node GenServer and pg group membership so each cluster node forwards messages to its own subscribers.

It also shows clustering with libcluster and LocalEpmd for local nodes, and tests the system with multiple IEx nodes and clients subscribed to different topics. The article ends by noting that the example is for learning only and that Phoenix.PubSub is the production-ready option.

## Reading notes

- PubSub is described as an asynchronous publish/subscribe pattern where a publisher broadcasts to a topic and subscribers consume the message.
- The local implementation is named Hermes and starts from a Registry with duplicate keys so multiple processes can subscribe to the same topic.
- `Registry.register/3` is used to subscribe a process to a topic, and `Registry.dispatch/3` is used to iterate over the registered processes and send them a message.
- The app supervisor starts the Registry so subscriptions are available when the application boots.
- `Hermes.subscribe/1` registers the current process, and `Hermes.publish/2` broadcasts to every subscriber registered under the topic.
- A single-node version works in IEx, but connected nodes do not share the Registry, so publishing on one node does not reach subscribers on another.
- Erlang `:pg` is introduced as a process-group mechanism that can include processes from different nodes under a shared group name.
- The article uses libcluster with the LocalEpmd strategy so nodes discover and connect to each other automatically.
- A `Hermes.PGServer` GenServer starts `:pg` and joins the group `{:hermes, Hermes.PubSub}`.
- `Hermes.publish/2` is changed to send a broadcast message to the remote `Hermes.PGServer` processes in the group, while also broadcasting locally.
- `Hermes.PGServer` handles `{:broadcast_to_local, topic, message}` by calling `Hermes.broadcast_local/2`.
- A simple `Client` GenServer subscribes to a topic and prints any received message.
- The final test uses three nodes, Alice, Bob, and Carol, with clients split across `:"user.created"` and `:"user.updated"` topics.
- Messages published on one node are received by subscribers on the matching topic across the cluster.
- The article states that the implementation is a toy example for learning and recommends Phoenix.PubSub for production.
