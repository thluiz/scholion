---
title: "Designing with OTP Applications in Elixir"
date: '2016-04-11T13:41:35-03:00'
category: webclip
summary: 'The post breaks Domain Scraper into separate OTP applications, argues for independent restart boundaries, and shows an umbrella setup that wires Twitter fetching and the unshortening pool together through streams.'
tags: ["elixir", "otp", "umbrella-application", "supervision-tree"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Designing with OTP Applications in Elixir"
    url: "http://learningelixir.joekain.com/designing-with-otp-applications-in-elixir/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/learningelixir-joekain-com--designing-with-otp-applications-in-elixir.md"
    kind: repo
---

The post describes how the author rethinks Domain Scraper as several independent OTP applications instead of one coarse-grained tree. Twitter fetching, the unshortening pool, and aggregation are treated as separate components so each one can fail and restart on its own.

It then shows the first prototype steps in a new umbrella application, including a supervised Twitter app and a server that builds a fetch-and-parse stream. The unshortening pool is copied over next, and the pieces can already be chained in `iex`, though the full automatic wiring and a second fetcher are still left for later.

## Reading notes

- The author moves from restarting the whole tree on failure to giving each major component its own restart boundary.
- Fetcher -> Decoupler, Unshortening Pool, and Aggregator are treated as separate OTP applications.
- `PoolUtil.map_through_pool` can accept data from multiple clients, so the pool does not need exclusive access.
- The prototype is rebuilt as an umbrella application with a supervised `Twitter` child app.
- `Twitter.Server` starts the fetcher and parser, configures ExTwitter, and returns the resulting stream.
- The unshortening pool is reused from the previous iteration.
- The pipeline works in `iex`, but the pool size needed to be increased for slower URL resolution.
- The design is not yet fully assembled automatically, and the author plans to add a Reddit fetcher next.
