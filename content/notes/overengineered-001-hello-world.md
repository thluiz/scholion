---
title: "Overengineered #001: Hello World"
date: '2026-09-25T18:40:52+01:00'
category: webclip
summary: 'The post rebuilds Hello World as a distributed Elixir app: UDP broadcast finds nodes on startup, and node monitoring triggers greetings when peers join the cluster.'
tags: ["elixir", "distributed-systems", "udp-broadcast", "node-monitoring"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Overengineered #001: Hello World"
    url: "https://papers.vincy.dev/overengineered-001-hello-world"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/papers-vincy-dev--overengineered-001-hello-world.md"
    kind: repo
---

The article turns a simple Hello World into a distributed Elixir setup. It starts with UDP broadcast for node discovery, then uses node monitoring so each node greets new peers when they join the cluster.

## Reading notes

- The series starts by taking simple problems and building unnecessarily complex solutions for learning and fun.
- The example project is an Elixir app with a supervision tree and GenServers started on application boot.
- Node auto-discovery is implemented without manual `Node.connect/1` calls.
- UDP broadcast is used to send discovery packets to the local network on port 45826.
- A `NodeManager` GenServer opens a UDP socket, broadcasts the current node, and listens for packets.
- The node name is sent with a `node::` prefix so the app can ignore unrelated UDP traffic.
- `:net_kernel.monitor_nodes(true)` is used so the app receives `:nodeup` and `:nodedown` messages.
- A `Greeter` GenServer sends a greeting when it receives `:nodeup` and logs greetings from other nodes.
- The result is a multi-node Hello World where nodes discover each other and exchange greetings automatically.
- The post says the approach is overkill and points to `libcluster` for a more robust clustering mechanism.
