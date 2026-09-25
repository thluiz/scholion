---
title: "The Dual Nature of Events in Event-Driven Architecture"
date: '2026-09-25T22:46:04+01:00'
category: webclip
summary: 'The article argues that events in event-driven systems serve two purposes at once: they trigger actions and carry data. Good event design must keep both the business reason and the changed state in view.'
tags: ["event-driven-architecture", "events", "kafka", "schema-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Dual Nature of Events in Event-Driven Architecture"
    url: "https://www.reactivesystems.eu/2024/10/31/the-dual-nature-of-events-in-eda.html?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/reactivesystems-eu--the-dual-nature-of-events-in-event-driven-architecture.md"
    kind: repo
---

The article says events in event-driven architecture have a dual role. They trigger actions and they carry data. Because of that, event design has to balance the needs of software engineers and data teams instead of treating events as only one or the other.

## Reading notes

- Events between services can sit anywhere between pure trigger and data carrier, from a type that alone explains what happened to an event that includes all properties of the changed entity.
- The author calls the data-heavy end of this spectrum “wide events,” while noting that other names exist for the same idea.
- From a software engineer or DDD perspective, events should express the business process as a sequence of distinct triggers, using properly named event types and only the data related to each event.
- From a data engineer perspective, the stream is treated as state, so one event type per topic and a shared schema make it easier to ingest and model the data.
- If design focuses only on data, the system can lose the reason for the event and collapse collaboration into data replication.
- If design focuses only on triggers, later uses like data warehousing, bootstrapping new services, or local projections may require adding wide events later.
- The author’s view is that an event must contain its business reason, must include the data changed in that event, and can include a complete snapshot if it stays small enough.
- The event stream should be designed like an API, because event payloads are hard to remove and should not lock the domain model too tightly.
- The recommended approach is to use carefully designed wide events and keep the reason in the event itself or in a header.
- The example sequence given is BookingUpdated with reasons such as SeatSelected, PaymentReceived, and TicketIssued.
