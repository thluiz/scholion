---
title: "A Farewell to FRP - Making signals unnecessary with The Elm Architecture"
date: '2016-05-10T15:02:19-03:00'
category: webclip
summary: 'Elm 0.17 introduces subscriptions, which make web sockets, time, and other external events fit The Elm Architecture more simply and remove the need to learn signals, addresses, and ports first.'
tags: ["elm-0-17", "subscriptions", "the-elm-architecture", "signals"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A Farewell to FRP - Making signals unnecessary with The Elm Architecture"
    url: "http://elm-lang.org/blog/farewell-to-frp"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-05/elm-lang-org--farewell-to-frp-making-signals-unnecessary.md"
    kind: repo
---

Elm 0.17 adds subscriptions so components can wait for messages while library code handles resource management behind the scenes. The post argues that this makes Elm easier to learn and use, and that signals, addresses, and ports can be replaced by simpler concepts.

## Reading notes

- Subscriptions let a component wait for messages such as time updates, location changes, and web socket messages.
- In the clock example, `Time.every` sets up a subscription that sends new times into `update` every second.
- In the web socket example, `WebSocket.send` sends messages and `WebSocket.listen` subscribes to incoming messages.
- The Elm WebSocket package opens the connection when someone subscribes and closes it when no one needs it.
- Queuing, reconnecting, and other connection handling happen behind the scenes.
- The post says most code stays the same in 0.17 and the upgrade plan covers the needed changes.
- The author says signals are no longer necessary for everyday Elm programming.
- The scheduler and effect managers support this model, and subscriptions are part of a broader emphasis on concurrency.
- The release also prepares for commands and subscriptions across web platform APIs and custom backends such as GraphQL, Elixir Phoenix, and Firebase.
