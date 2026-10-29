---
title: "Phoenix: The difference between web and lib"
date: '2016-01-25T08:48:15-03:00'
category: webclip
summary: 'Phoenix has two code locations, `web` and `lib`. The key difference is that `web` is hot reloaded on each request, while `lib` is suited to state that lives beyond a request lifecycle.'
tags: ["phoenix", "elixir", "otp", "hot-reload"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Phoenix: The difference between web and lib"
    url: "http://keathley.io/elixir/phoenix/2016/01/14/phoenix-directories.html?utm_campaign=elixir_radar_33&utm_medium=email&utm_source=RD+Station"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/keathley-io--phoenix-the-difference-between-web-and-lib.md"
    kind: repo
---

Phoenix has two distinct places for code, the `web` directory and the `lib` directory. The post says the main difference is hot reloading: code in `web` is recompiled on the next request after a change, while `lib` is not treated that way.

That difference maps to state management. `web` is the right place for code that only needs to manage state during one request, and `lib` is the right place for code that manages state outside a request lifecycle, such as Supervisors, Agents, or GenServers. This fits the idea that Phoenix is just an OTP application, with web components as one part of the application.

## Reading notes

- `web` and `lib` are the two code locations Phoenix distinguishes.
- `web` is hot reloaded, so a file change is picked up on the next web request.
- The code layout should follow state management needs.
- `web` suits state that lasts only for a request.
- `lib` suits state that lasts beyond a request, including Supervisors, Agents, and GenServers.
- Phoenix is presented as an OTP application, not as a framework bound to a strict request/response cycle.
