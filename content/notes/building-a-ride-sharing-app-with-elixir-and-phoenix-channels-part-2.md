---
title: "Building a Ride Sharing App with Elixir and Phoenix Channels — Part 2"
date: '2026-11-16T17:51:39+00:00'
category: webclip
summary: 'The tutorial moves from authentication to the app’s main feature: real-time matching between drivers and riders. It introduces Phoenix Channels, sockets, websockets, and topic-based message routing.'
tags: ["elixir", "phoenix-channels", "websockets", "ride-sharing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a Ride Sharing App with Elixir and Phoenix Channels — Part 2"
    url: "https://medium.com/@leo_hetsch/building-a-ride-sharing-app-with-elixir-and-phoenix-channels-part-2-659aa2f24808"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--building-a-ride-sharing-app-with-elixir-and-phoenix-channels-part-2.md"
    kind: repo
---

The second part of the tutorial shifts from the authentication endpoint to the main feature of the ride-sharing backend: real-time matching between drivers and riders. It explains how Phoenix Channels handles messages over HTTP, usually through a websocket connection, with the Phoenix app acting as the orchestrator for incoming and outgoing traffic.

## Reading notes

- The post is the second part of a tutorial about a small ride-sharing backend built with Elixir and Phoenix.
- The previous part covered the project bootstrap and the authentication endpoint.
- This part focuses on real-time matching between drivers and riders.
- Phoenix Channels sends real-time messages between senders and receivers over HTTP.
- It is usually used through websockets, but it also supports long polling.
- Clients connect to a socket, similar to a native websocket server.
- Connected clients can publish and receive messages from other clients.
- The server, here the Phoenix application, acts as the orchestrator for incoming and outgoing messages.
- Phoenix uses topics to route messages to the correct channel.
- After connecting to a socket, a client can join one or more topics.
- The same client can then publish messages to those topics.
