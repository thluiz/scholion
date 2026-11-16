---
title: "Distributed Phoenix Chat with PubSub PG2 adapter"
date: '2026-11-16T03:43:59+00:00'
category: webclip
summary: 'The article explains how Phoenix nodes are clustered with BEAM, how pg2 groups processes across nodes, and how Phoenix uses PubSub.PG2Server to broadcast chat messages between servers.'
tags: ["phoenix", "pubsub", "pg2", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Distributed Phoenix Chat with PubSub PG2 adapter · Poeticoding"
    url: "https://poeticoding.com/distributed-phoenix-chat-with-pubsub-pg2-adapter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/poeticoding-com--distributed-phoenix-chat-with-pubsub-pg2-adapter.md"
    kind: repo
---

The article shows how to cluster Phoenix Chat nodes with the BEAM communication protocol, then uses `pg2` to group processes across nodes and inspect how Phoenix broadcasts chat messages in a distributed app. It contrasts this approach with Redis PubSub, which is easy to set up but introduces a single point of failure and extra server maintenance.

## Reading notes

- The BEAM lets Elixir nodes connect directly, so one node can talk to remote processes on another node after `Node.connect/1`.
- `pg2` is an Erlang module for process grouping across multiple nodes.
- A `pg2` group keeps track of member PIDs and monitors them locally.
- When a process exits, `pg2` removes it from the group.
- `pg2` does not provide a direct broadcast function, so messages are sent by enumerating group members one by one.
- In Phoenix, the `Phoenix.PubSub.PG2` adapter is configured by default in a new app.
- Each Phoenix node starts a local `PubSub.PG2Server` and registers it in the `{:phx, Chat.PubSub}` group.
- The group members are the `PubSub.PG2Server` PIDs, not the user socket processes.
- A message is broadcast locally first, then forwarded once to the remote `PubSub.PG2Server`, which rebroadcasts it to browsers on that node.
- The article ends by noting that manual node connection is a problem for production, and points to libcluster for automatic clustering.
