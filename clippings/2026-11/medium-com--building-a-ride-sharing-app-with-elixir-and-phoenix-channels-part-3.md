---
url: "https://medium.com/@leo_hetsch/building-a-ride-sharing-app-with-elixir-and-phoenix-channels-part-3-811a7999465f"
captured_at: "2026-11-16T17:52:02+00:00"
title: "Building a Ride Sharing App with Elixir and Phoenix Channels — Part 3"
domain: "medium-com"
---

Member-only story

Building a Ride Sharing App with Elixir and Phoenix Channels — Part 3
Léonard Hetsch
6 min read
·
May 22, 2020

In the first two parts of this tutorial, we built the foundations to allow Riders to request a Ride, and Drivers to accept them. This was all done by leveraging features from Phoenix Channels.

In this last part, we’re going to use another feature of Channels, called Presence, to display nearby Drivers on the map. From the official documentation:

Phoenix Presence is a feature which allows you to register process information on a topic and replicate it transparently across a cluster. It’s a combination of both a server-side and client-side library which makes it simple to implement. A simple use-case would be showing which users are currently online in an application.

And this use-case is precisely what we are going to implement now. Since all Drivers join a channel for a given location — remember, using geohash topics— we can use Presence to track Drivers on the app. This way, we can keep an ever-fresh vision of the “state” of Drivers and their current location, to display them on the map.
