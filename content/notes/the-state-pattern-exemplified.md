---
title: "The State Pattern Exemplified"
date: '2026-11-16T07:48:47+00:00'
category: webclip
summary: 'The article explains the State Pattern as a way to encapsulate an object''s internal state, model finite state machines, and keep transition logic out of the context class, using a toaster implemented in TypeScript.'
tags: ["state-pattern", "finite-state-machines", "typescript", "design-patterns"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The State Pattern Exemplified"
    url: "https://web.archive.org/web/20200704133122id_/https://dev.to/alfki/the-state-pattern-exemplified-4cbe"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--the-state-pattern-exemplified.md"
    kind: repo
---

The article presents the State Pattern as a behavioral design pattern that encapsulates internal state so an object can change its behavior through clear transitions. It uses a toaster as a finite state machine example and shows how separate state classes keep transition logic out of the main context class.

## Reading notes

- The State Pattern is described as a behavioral pattern used for communication and delegation problems.
- It fits finite state machines because only one state is active at a time and transitions happen through external input.
- A toaster is used as the example FSM, with states for Idle, Bread Inserted, Toasting, and Bread Ejected.
- The toaster transitions follow a fixed sequence: insert bread, pull lever, eject bread, remove bread.
- The article notes that no direct transition exists from Idle to Toasting.
- A `ToasterOperations` interface defines the toaster methods: `insertBread`, `pullLever`, `ejectBread`, and `removeBread`.
- A `Toaster` class implements the interface, but the action logic is delegated to the current state.
- An abstract `ToasterState` base class throws `Error` for invalid operations.
- Concrete state classes override only the allowed transition methods and return the next state instance.
- The `Toaster` object stores the current state in a local variable and replaces it after each valid transition.
- Invalid calls, such as `ejectBread()` while in `Idle`, throw `Invalid operation`.
- The article says this keeps the state logic clean and makes the toaster class easier to extend.
