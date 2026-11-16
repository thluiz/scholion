---
title: "Event sourcing: The single source of truth"
date: '2026-11-16T02:38:52+00:00'
category: webclip
summary: 'The article contrasts CRUD with event sourcing, where data is built by appending events. It argues this makes history recoverable, synchronization easier, and the event store a single source of truth.'
tags: ["event-sourcing", "crud", "data-synchronization", "single-source-of-truth"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Event sourcing: The single source of truth"
    url: "https://roelofjanelsinga.com/articles/event-sourcing-single-source-truth"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/roelofjanelsinga-com--event-sourcing-the-single-source-of-truth.md"
    kind: repo
---

Event sourcing is presented as a different way to handle application data, centered on appending events instead of overwriting current state. The post uses blog post publishing, updating, and deleting to show how the event list preserves earlier states and can be shared across applications.

It argues that this makes the event store a single source of truth because any application can read the same chronological event history and rebuild the current state from it. The author also says an aggregate root can use past events to decide what new events to record, which helps keep multiple applications synchronized.

## Reading notes

- CRUD applications work with create, read, update, and delete, while event sourcing focuses on creating and reading by appending to existing state.
- A published blog post can be represented as a recorded event, and the trigger date becomes the publishing date.
- Updates and deletions are recorded as new events, while the old version of the blog post remains in the database.
- Because events are stored chronologically, it is possible to look back and see what the data looked like before.
- A second application can ask for all events related to a resource and then append new events to its own state.
- This shared event history keeps the state the same across applications and lowers server load.
- An aggregate root can read past events and use them to decide how to react to a new command.
- The article gives the example of recording a pageview and, after the third view, also recording that related blog posts were emailed to the visitor.
- The author says event sourcing avoids uncertainty because the current state can be recreated from the list of appended events.
