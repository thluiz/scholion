---
url: "https://medium.com/@leo_hetsch/building-a-ride-sharing-app-with-elixir-and-phoenix-channels-part-2-659aa2f24808"
captured_at: "2026-11-16T17:51:39+00:00"
title: "Building a Ride Sharing App with Elixir and Phoenix Channels — Part 2"
domain: "medium-com"
---

Member-only story

Building a Ride Sharing App with Elixir and Phoenix Channels — Part 2
Léonard Hetsch
10 min read
·
May 20, 2020

This is the second part of a tutorial about building a small ride-sharing backend with Elixir and the Phoenix framework. Feeling lost? You might want to read part 1 first.

In the previous part, we bootstrapped the project with the authentication endpoint. Now, we’re going to dive into the main feature: real-time matching between Drivers and Riders.

Phoenix Channels allows us to send real-time messages between senders and receivers over HTTP. We’ll usually do it through a websockets connection, although the library also supports long polling. Clients connect to a socket, much like they would with a “native” websockets server. They can then publish and receive messages from other connected clients. The server — in our case, the Phoenix application — acts as the orchestrator, handling all incoming and outgoing messages.

Phoenix uses the concept of “topics” to route messages to the right channel. After a client connects to a socket, it can join one or many topics. The same client can then publish messages to those…
