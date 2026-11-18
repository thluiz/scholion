---
title: "Building a Ride Sharing App with Elixir and Phoenix Channels — Part 3"
date: '2020-07-05T14:10:40+00:00'
category: webclip
summary: 'This part uses Phoenix Presence to track drivers by geohash topic and show nearby drivers on the map, keeping the app’s view of driver state and location up to date.'
tags: ["phoenix-channels", "phoenix-presence", "elixir", "ride-sharing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a Ride Sharing App with Elixir and Phoenix Channels — Part 3"
    url: "https://medium.com/@leo_hetsch/building-a-ride-sharing-app-with-elixir-and-phoenix-channels-part-3-811a7999465f"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--building-a-ride-sharing-app-with-elixir-and-phoenix-channels-part-3.md"
    kind: repo
---

This part of the tutorial adds Phoenix Presence to the ride-sharing app so it can display nearby drivers on the map. The idea is to track drivers who join a channel for a given location and keep a fresh view of their current state and position.

## Reading notes

- The first two parts already established ride requests and driver acceptance using Phoenix Channels.
- This part introduces Presence as another Channels feature.
- The official documentation describes Phoenix Presence as a way to register process information on a topic and replicate it across a cluster.
- Presence combines a server-side and client-side library.
- A simple use case for Presence is showing which users are currently online.
- The app applies that same idea to drivers.
- Drivers join a channel for a given location using geohash topics.
- Presence is used to track those drivers in the app.
- The result is an up-to-date view of driver state and current location for the map.
