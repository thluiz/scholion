---
title: "33/60 Days System Design Questions"
date: 2026-09-23T14:47:00+01:00
category: webclip
summary: "A daily.dev system design prompt: an order service that only stores current state can't reconstruct a billing dispute, and the post argues event sourcing is the real fix, not a patch."
tags: ["system-design", "event-sourcing", "software-architecture", "postgres"]
has_commentary: false
sources:
  - title: "33/60 Days System Design Questions"
    url: "https://daily.dev/posts/EMnXrcVUC?utm_source=notification&utm_medium=email&utm_campaign=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-07/daily-dev--33-60-days-system-design-questions.md"
    kind: repo
---

A daily.dev post from Joud Awad, day 33 of a 60-day system design series, frames a concrete failure: an order service backed by Postgres stores only current state, so every overwritten row erases how an order got there. A billing dispute surfaces the gap directly, with two orders sharing an ID and different totals and no way to reconstruct what happened.

## Reading notes

- The failure case: an order service taking 200 writes/sec, backed by Postgres storing current state only, with every UPDATE overwriting the previous row and no audit log, event history, or replay.
- The trigger: a billing dispute over Order #8471, where the current schema can't reconstruct what actually happened to that order over time.
- Four options are on the table: event sourcing (append-only log, state derived by replaying events), change data capture streaming Postgres row changes to Kafka, a trigger-based audit_log table, and dual-write to both a current-state table and a separate events table.
- The post treats event sourcing as the only option that gives full replay and projection flexibility, framing CDC, audit tables, and dual-write as patches rather than a real source of truth.
- The [CQRS](/notes/cqrs/) note covers the pairing this scenario assumes: event sourcing fits naturally with a separated read/write model, since state changes are stored as a sequence of events rather than as current state.
