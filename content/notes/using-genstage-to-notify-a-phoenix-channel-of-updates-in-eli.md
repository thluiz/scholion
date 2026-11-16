---
title: "Using GenStage to Notify a Phoenix Channel of Updates in Elixir"
date: '2020-07-05T14:11:26+00:00'
category: webclip
summary: 'The post explores using GenStage to notify a Phoenix channel about model updates, first as an observer pattern, then by separating a notification center producer from a channel consumer.'
tags: ["genstage", "phoenix-channel", "observer-pattern", "elixir"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using GenStage to Notify a Phoenix Channel of Updates in Elixir"
    url: "https://web.archive.org/web/20201108121502id_/http://learningelixir.joekain.com/using-gen-stage-to-notify-a-channel/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--using-genstage-to-notify-a-phoenix-channel-of-updates-in-eli.md"
    kind: repo
---

The post walks through replacing a GenEvent-based update notification setup with GenStage. It describes a producer that receives update events, a consumer that broadcasts them to a Phoenix channel, and the demand-based flow between them.

## Reading notes

- The author starts from a previous GenEvent example and wants to use GenStage to notify a Phoenix channel of new events.
- The goal is to decouple the controller that updates the model from the channel that broadcasts changes to web clients.
- The first attempt makes the channel a GenStage consumer and adds init/1 and handle_events/3 so it can receive update events.
- A producer module is then built to accept notifications, manage demand, and dispatch events to consumers.
- The author experiments with tests for start_link, notify, and subscriber behavior, then revises them to focus on external behavior rather than implementation details.
- The producer implementation is refined to handle queued events and outstanding demand.
- The post notes that a BroadcastDispatcher is needed when there can be multiple subscribers.
- The author later realizes the architecture was confused, renames the producer role to NotificationCenter, and separates the consumer that broadcasts to the channel.
- The final setup uses subscribe_to in the consumer init/1 so it automatically connects to the named notification center.
- The conclusion says the exercise clarified GenStage’s queueing and demand model and points to Flow and a Domain Scrapper rewrite as next steps.
