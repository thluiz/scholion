---
title: "Mistakes we made adopting event sourcing (and how we recovered)"
date: '2026-11-16T18:50:35+00:00'
category: webclip
summary: 'The team describes several mistakes made while adopting event sourcing, then explains how they corrected the architecture by separating event history from current state, using direct transactions, and relying on Ports and Adapters.'
tags: ["event-sourcing", "arquitetura-de-software", "ports-and-adapters", "cqrs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Mistakes we made adopting event sourcing (and how we recovered)"
    url: "http://natpryce.com/articles/000819.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/natpryce-com--mistakes-we-made-adopting-event-sourcing.md"
    kind: repo
---

The team describes how they adopted an event-sourced architecture for a system that needed an accurate history of information and analysis for fraud detection. They made early design mistakes, but were able to recover because their architecture and tests let them change course without disrupting the whole system.

## Reading notes

- They first stored the current relational state alongside the event history, but command handlers both recorded events and updated that relational model, so the entity state could not be rebuilt from events and migrations became costly.
- They initially confused event-driven and event-sourced architecture, which led them to treat events as triggers for other components instead of as records of what happened in the past.
- They used the event store as a message bus, added notifications for subscriptions, and ended up with technical events in the history that users did not need to see.
- They also leaned on eventual consistency too early by exposing the event store over HTTP, which prevented ACID processing and pushed consistency mechanisms into the application.
- They caught the mistakes early in an architecture wizengamot, before the live event history had been affected.
- They replaced HTTP between command processors and the event store with direct database connections and serialisable transactions.
- They kept HTTP only for peripheral services that maintain read-optimised views that may be eventually consistent, such as daily reports and business metrics.
- They stopped using notifications to trigger activity and returned to REST, especially HATEOAS, for passing data and control between components.
- They changed command handling so the application computes current state from the event history when an entity is loaded, while treating the persisted projection as a read-through cache.
- They still keep projections for loading active entities and for other uses, and those projections are updated by events.
- They replaced the relational model with JSON blobs serialised from the domain model, which can be discarded and rebuilt if the persisted state becomes incompatible with the application.
- They also maintain projections for reporting in the background on a regular schedule.
- The rework was straightforward because the application used Ports and Adapters, which hid entity loading behind a port interface.
- A colleague changed the app to compute current state from event history in about one hour, and the change went live by the end of the day.
- Their functional tests were written around the domain and could run against the in-memory model, HTTP services, or the browser, which helped preserve behaviour while the architecture changed.
- The tests also enforce the architectural boundaries by making it hard to put business logic in technical adapter layers.
- The article concludes that mistakes are inevitable when adopting a new architecture, so the architecture must also support recovery from those mistakes.
