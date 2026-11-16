---
url: "https://medium.com/@leo_hetsch/building-a-ride-sharing-app-with-elixir-and-phoenix-channels-part-1-17bbd292aec4"
captured_at: "2026-11-16T06:07:47+00:00"
title: "Building a Ride Sharing App with Elixir and Phoenix Channels — Part 1 | by Léonard Hetsch | Medium"
domain: "medium-com"
---

Member-only story

Building a Ride Sharing App with Elixir and Phoenix Channels — Part 1
Léonard Hetsch
7 min read
·
May 19, 2020

Real-time is everywhere now. It doesn’t matter which kind of application you want to build — a chat, a shared documents service like Google Docs, a social mobile app with push notifications, a live game, or a live news feed, real-time features are more and more needed in modern applications.

Elixir/OTP is a really good platform whenever you want to build backend systems with real-time features, thanks to the Erlang VM foundations. A famous example of applications using such real-time features are ride-sharing applications like Uber or Lyft. A driver checks in on his phone, and riders can request for a ride, before being — hopefully — matched with the closest driver, everything happening in real-time, sometimes in a matter of seconds.

In this tutorial, we will see together how to create a simple prototype for a ride sharing application with Elixir and the Phoenix framework, using some of its real-time communication features like Channels and Presence.

For the sake of simplicity, we will build a basic web app, allowing users to check in and share their current location, and riders to request for a ride. The web app will contain a map with real-time positions of drivers operating in the area.

The Domain model
