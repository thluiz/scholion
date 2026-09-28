---
title: "MQTT for Elixir"
date: '2022-07-25T11:43:22-03:00'
category: webclip
summary: 'The article shows how to use MQTT in an Elixir setup for embedded devices, with a sensor process publishing temperature data and a LiveView dashboard subscribing and sending commands.'
tags: ["mqtt", "elixir", "embedded-iot", "liveview"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "MQTT for Elixir - DEV Community"
    url: "https://dev.to/emqx/mqtt-for-elixir-3gdf"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/dev-to--mqtt-for-elixir.md"
    kind: repo
---

The article presents MQTT as an alternative to HTTP for embedded and IoT communication in Elixir. It explains the broker-based pub/sub model, then builds a simple sensor application that publishes temperature readings and listens for interval changes.

## Reading notes

- MQTT is described as a messaging protocol for device communication, using a lightweight binary protocol over TCP/IP and fitting unreliable networks.
- The protocol uses pub/sub, so clients connect to a broker instead of a server.
- A broker such as EMQX can also offer WebSockets, authentication and authorization, streaming to databases, and custom routing rules.
- The sensor example is an ordinary Mix application that can be turned into a Nerves app.
- The sensor module starts an MQTT client, subscribes to `commands/#{clientid}/set_interval`, and schedules periodic ticks.
- On each tick, it generates a `{Timestamp, Temperature}` tuple and publishes it to `reports/#{clientid}/temperature`.
- The dashboard is a Phoenix LiveView app that also acts as an MQTT client.
- It subscribes to `reports/#` and publishes interval commands to `commands/#{id}/set_interval`.
- Incoming temperature reports are converted into a chart rendered with Contex.
- The form on the dashboard sends a new interval to the device topic and updates the charting process state.
- The article notes that retained command messages let a restarted device receive the last configured interval on reconnect.
