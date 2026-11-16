---
title: "Monitoring WebSocket disconnections in Phoenix"
date: '2026-11-16T06:07:14+00:00'
category: webclip
summary: 'The post shows how to run cleanup code when a Phoenix WebSocket closes by spawning monitored tasks, placing the tasks supervisor before the endpoint, and using a small init/1 trick to capture the socket process.'
tags: ["phoenix", "websocket", "elixir", "supervision"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Monitoring WebSocket disconnections in Phoenix | by Xavier Noria | Medium"
    url: "https://medium.com/@fxn/monitoring-websocket-disconnections-in-phoenix-bbe24f54d996"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--monitoring-websocket-disconnections-in-phoenix.md"
    kind: repo
---

The post explains a way to run actions when a Phoenix WebSocket closes, such as logging the disconnection or decreasing a gauge. The approach uses monitors and a small hack so that a socket can trigger work on disconnect.

## Reading notes

- Each WebSocket in Phoenix is managed by a dedicated process, and when that socket closes, the process terminates and its monitor receives a :DOWN message.
- The monitor is very cheap because it waits on receive until the monitored process terminates, so the overhead is negligible.
- The monitor is run as a supervised task that traps exits so it can finish its callback during shutdown.
- Tasks under a supervisor are not restarted because the default restart strategy is :temporary, but the supervisor still helps the application start and stop in an orderly way.
- Trapping exits matters because supervisors send exit signals to children during shutdown, and without trapping them the monitor processes would be killed immediately.
- The tasks supervisor must start before the endpoint, so it is already running when sockets are accepted.
- On shutdown, children stop in reverse order, so by the time the tasks supervisor stops, the endpoint and all sockets are already down.
- When a process terminates, all its monitors are notified at once, so the monitors already have their :DOWN messages in their mailboxes when shutdown begins.
- Running on_connect/2 inside connect/2,3 does not work because that callback process dies when it returns, and the socket process exists only after the connection is accepted.
- The workaround is to use self() in init/1 of MyAppWeb.UserSocket, so the socket process can be monitored there.
- The post mentions an alternative design with one GenServer that monitors all sockets, but prefers the simpler per-socket task approach for error isolation, parallelism, and controlled shutdowns.
