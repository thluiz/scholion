---
title: "Guts of Phoenix websocket channels"
date: '2015-12-11T18:29:36-03:00'
category: webclip
summary: 'The post breaks Phoenix channels into transport, channel, and PubSub layers, then explains how Cowboy, GenServers, ETS, and PG2 move messages between clients and nodes.'
tags: ["phoenix-channels", "websocket", "pubsub", "erlang"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Guts of Phoenix websocket channels"
    url: "http://zohaib.me/guts-of-phoenix-channels/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-12/zohaib-me--guts-of-phoenix-websocket-channels.md"
    kind: repo
---

The post explains Phoenix channels as three linked parts: transport, channel, and PubSub. Transport handles the socket connection and message flow, Cowboy maintains the raw websocket connection, channel code handles incoming and outgoing messages through GenServer logic, and PubSub distributes broadcasts across subscribed sockets and nodes.

## Reading notes

- Transport sits between the socket layer and the channel, receives client messages, passes them to the channel, and sends channel messages back to the client.
- Phoenix includes websocket and long polling transports, and the transport layer keeps the channel API independent from the protocol used below it.
- The design is meant to stay extensible, so a new protocol would mainly require a new transport and endpoint configuration.
- Cowboy handles the raw websocket connection and implements the websocket handler callbacks that Phoenix plugs into.
- `Phoenix.Endpoint.CowboyWebSocket` acts as the bridge between Cowboy and `Phoenix.Transports.WebSocket`.
- `Phoenix.Transports.WebSocketSerializer` turns JSON into `Phoenix.Socket.Message` and serializes replies back to JSON.
- The channel has two parts: the developer-written channel behavior and the GenServer spawned by Phoenix to consume it.
- The channel process communicates with the transport and listens for broadcasted messages that should be sent to clients.
- When a transport message arrives, the channel calls `handle_in`; when a broadcast reaches it, the channel calls `handle_out`.
- PubSub broadcasts messages to all sockets subscribed to a topic, including across multiple nodes.
- Phoenix uses PG2 named process groups to coordinate distributed topic membership.
- `Phoenix.PubSub.PG2Server` forwards messages for a topic to local subscribers on a node.
- `Phoenix.PubSub.Local` stores local channel GenServer pids in ETS and sends broadcasts to those local processes.
- The post says the local PubSub reduces node-to-node traffic compared with sending every broadcast directly through the distributed group.
- It also notes a later optimization for 2 million websocket connections: PubSub was split into a pool of GenServers with separate ETS tables so subscriptions could be sharded and the PubSub would not become a bottleneck.
