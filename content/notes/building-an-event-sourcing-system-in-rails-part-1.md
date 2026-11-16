---
title: "Building an Event Sourcing System in Rails, Part 1: What is Event Sourcing?"
date: '2026-11-16T19:50:08+00:00'
category: webclip
summary: 'Event Sourcing stores every data change as an immutable event, keeps events in chronological order, and uses them as the source of truth to rebuild system state later.'
tags: ["event-sourcing", "rails", "immutable-events", "version-control"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building an Event Sourcing System in Rails, Part 1: What is Event Sourcing?"
    url: "https://dev.to/isalevine/building-an-event-sourcing-system-in-rails-part-1-what-is-event-sourcing-46db"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--building-an-event-sourcing-system-in-rails-part-1.md"
    kind: repo
---

Event Sourcing is presented as a design pattern in which each change to data becomes an immutable event stored in chronological order. Those events are kept as a permanent history, and the current system state is derived from them.

## Reading notes

- Changes to data are stored as Event objects.
- The Events have a fixed chronological order that can be replayed.
- The Events cannot be changed or deleted for as long as they might be needed.
- The example app centers on creating and destroying a User model.
- The basic flow is that the client sends a request, the server creates and saves a User, and then saves an Event with the request and created User details.
- Martin Fowler describes version-control systems like Git as a common example of Event Sourcing.
- In that comparison, the commit log is the event store and the working copy is the system state.
- For Rails, the article points to Kickstarter’s minimal Event Sourcing example and Arkency’s RailsEventStore library.
- From the author’s experience, immutability means avoiding `ActiveRecord.destroy` and designing for permanence, such as using a `deleted` field.
- Saving event payloads can expose sensitive data if they are stored outside auth features like `has_secure_password`.
- Because events become the principal source of truth, naming and organizing event objects becomes more important and must be future-proof.
- The next article will cover setting up a Rails app, building the BaseEvent class architecture, and implementing `Events::User::Created` and `Events::User::Destroyed`.
