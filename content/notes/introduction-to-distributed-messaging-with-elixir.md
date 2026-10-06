---
title: "Introduction to Distributed Messaging with Elixir"
date: '2015-05-25T21:39:32-03:00'
category: webclip
summary: 'The article shows how Elixir’s Erlang heritage lets nodes connect, make remote calls, and exchange messages across machines while handling latency and failure in distributed systems.'
tags: ["elixir", "distributed-systems", "messaging", "erlang"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Introduction to Distributed Messaging with Elixir - Reactive.TIPS - The Official Blog of Reactive.IO"
    url: "http://www.reactive.io/tips/2015/02/07/introduction-to-distributed-messaging-with-elixir/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/reactive-io--introduction-to-distributed-messaging-with-elixir.md"
    kind: repo
---

Elixir inherits distributed messaging from Erlang, so nodes can connect across racks, data centers, and oceans. The article uses that to show how real-time software can keep growing beyond hardware boundaries while dealing with latency and failure.

## Reading notes

- Two IEx nodes can be started with different `sname` values, pinged with `Node.ping/1`, and checked with `Node.list/0`.
- A function compiled on one node can be called from another node with Erlang’s `:rpc.call/4`.
- The tutorial builds separate `Server` and `Client` applications that talk to each other natively.
- The server keeps a stack and a subscriber list, and registers itself globally with `:global.register_name/2` so other nodes can find it.
- The client connects to the server with `:global.whereis_name/1`, subscribes to updates, and logs stack changes in a separate process.
- Pushing, popping, requesting the stack, and unsubscribing are all sent as messages across nodes.
- The same setup works in real time whether the nodes are on one machine or on different cities or continents.
