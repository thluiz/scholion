---
title: "Is LiveView Overhyped?"
date: '2022-03-18T07:39:34-03:00'
category: webclip
summary: 'The author argues LiveView is heavily promoted but not technically overhyped. He frames it as a useful, well-chosen trade-off for many web apps, while noting limits around offline use, latency, connectivity, and fallback behavior.'
tags: ["liveview", "phoenix", "elixir", "web-ui"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Underjord | Is LiveView Overhyped?"
    url: "https://underjord.io/is-liveview-overhyped.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-03/underjord-io--is-liveview-overhyped.md"
    kind: repo
---

The author says LiveView is useful, powerful, and interesting for building web UI, but it is not best for everything. He treats the main objections as real trade-offs, especially offline use, latency, poor connectivity, and graceful degradation, while arguing that the enthusiasm around it is mostly warranted.

## Reading notes

- LiveView is useful, powerful, and a very interesting approach for building web UI, but it is not best for everything.
- Offline-first apps are a major mismatch for LiveView, unless only some parts are handled with it.
- WebSocket round trips add latency, so it is a poor fit for games and other latency-sensitive apps.
- For server-backed interactions, LiveView can have lower latency than full HTTP request-response flows and can push events from the server.
- LiveView sends diffs and usually less data than a normal JSON payload for the same change, but it still sends more than doing the work on the client.
- On poor connections, persistent WebSocket sessions may be more fragile than plain HTTP requests, though the author has not seen major problems in practice.
- By default, LiveView renders a normal page if the WebSocket cannot be established, but forms do not fully fall back without extra work.
- The author thinks LiveView has been promoted a lot, yet the community has discussed its trade-offs from the start.
- The article concludes that LiveView is not a panacea, but it is a compelling tool that helps the author build faster with fewer frustrations.
