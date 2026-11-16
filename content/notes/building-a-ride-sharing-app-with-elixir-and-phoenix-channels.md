---
title: "Building a Ride Sharing App with Elixir and Phoenix Channels — Part 1"
date: '2020-07-05T14:10:40+00:00'
category: webclip
summary: 'The post introduces a tutorial for a simple ride-sharing prototype in Elixir and Phoenix, centered on real-time channels, presence, driver check-in, rider requests, and live map positions.'
tags: ["elixir", "phoenix-channels", "real-time", "ride-sharing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a Ride Sharing App with Elixir and Phoenix Channels — Part 1 | by Léonard Hetsch | Medium"
    url: "https://medium.com/@leo_hetsch/building-a-ride-sharing-app-with-elixir-and-phoenix-channels-part-1-17bbd292aec4"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--building-a-ride-sharing-app-with-elixir-and-phoenix-channels.md"
    kind: repo
---

The post frames real-time features as increasingly necessary in modern applications and presents Elixir/OTP as a strong platform for backend systems with real-time communication. It uses ride-sharing apps as an example, where driver check-ins and rider requests need to be matched in real time.

## Reading notes

- Real-time features are now needed in many kinds of applications, including chat, shared documents, social mobile apps, live games, and live news feeds.
- Elixir/OTP is presented as a good platform for backend systems with real-time features because of the Erlang VM foundations.
- Ride-sharing apps such as Uber and Lyft are given as a familiar example of real-time matching between drivers and riders.
- The tutorial will build a simple ride-sharing prototype with Elixir and Phoenix.
- The example will use Phoenix Channels and Presence for real-time communication.
- The basic web app will let users check in and share their current location.
- Riders will be able to request a ride.
- The app will include a map showing real-time positions of drivers operating in the area.
