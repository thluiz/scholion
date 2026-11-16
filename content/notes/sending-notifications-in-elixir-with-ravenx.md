---
title: "Sending notifications in Elixir with Ravenx"
date: '2026-11-16T06:16:23+00:00'
category: webclip
summary: 'The article presents Ravenx as a library for dispatching notifications in Elixir through multiple strategies, with configurable per-strategy, module, and per-dispatch settings, plus synchronous or asynchronous sending.'
tags: ["elixir", "notifications", "ravenx", "strategy-pattern"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Sending notifications in Elixir with Ravenx | by Óscar de Arriba | Acutario | Medium"
    url: "https://medium.com/acutario/sending-notifications-in-elixir-with-ravenx-1f2502a1f272"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--sending-notifications-in-elixir-with-ravenx.md"
    kind: repo
---

The article explains Ravenx as a library built for Acutario’s Elixir app to handle notification dispatching across multiple services such as e-mail, Slack, and push notifications. It uses strategies with a standard interface, so the notification logic stays abstracted from the outside and new strategies can be added later.

It also describes three configuration layers, global, module-based, and particular, and shows that they are merged with the priority Global < Module < Particular. Ravenx can send notifications synchronously or asynchronously, supports macros for defining notification modules, and lets anyone implement custom strategies. It does not handle dispatch scheduling.

## Reading notes

- Ravenx was created while building a new version of Acutario in Elixir to handle notification dispatching issues.
- The library aims to send notifications to multiple services, including e-mail, Slack, and mobile push notifications.
- Ravenx is organized around strategies, each with a standard interface for sending notifications.
- Current strategies mentioned are Slack webhooks and e-mail through bamboo strategies.
- The article says new strategies can be implemented to send notifications to other systems and platforms.
- Configuration can be defined globally, through a configuration module, or as a particular configuration at dispatch time.
- A configuration module has one function per strategy, receives the payload, and returns a map with strategy-specific settings.
- Particular configuration is passed when dispatching a notification, for settings created right before sending.
- When multiple configurations are present, the priority is Global < Module < Particular.
- Ravenx can send notifications synchronously or asynchronously, and asynchronous sending uses a Task under the hood.
- The library defines a macro to generate notification modules for dispatching one notification through multiple strategies.
- Those modules must define get_notifications_config/1, which returns a Keyword list with strategies and payloads.
- Custom strategies can be integrated by implementing the required interface and registering the strategy modules.
- Ravenx does not manage dispatch scheduling or limit the amount of notifications sent simultaneously.
- The author says the library helps organize and reuse notification code while avoiding repetition.
