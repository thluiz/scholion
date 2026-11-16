---
title: "Organizing LiveView Logic with Presentation Models"
date: '2020-07-05T14:10:31+00:00'
category: webclip
summary: 'The post argues that a LiveView can keep presentation state and interaction logic in a separate Presentation Model, making the view thinner and the behavior easier to test with plain values.'
tags: ["phoenix-liveview", "presentation-model", "testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Organizing LiveView Logic with Presentation Models"
    url: "https://hostiledeveloper.com/2020/06/19/organizing-liveview-logic-with-presentation-models.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/hostiledeveloper-com--organizing-liveview-logic-with-presentation-models.md"
    kind: repo
---

The post says Phoenix LiveView is a good fit for smart interfaces, but the tutorial example is too tied to one view to be a pattern you would ship. It recommends separating presentation state from core business logic so the LiveView stays small and the transformations stay testable.

## Reading notes

- The author treats LiveView logic as a separate presentation layer, distinct from the app’s core business logic.
- The example search view stores zip, stores, and loading state, and the data it receives can be further decorated for display.
- The main benefit of extracting a functional core is simpler separation of concerns and easier testing.
- The article proposes a Presentation Model to hold presentation state and behavior independently of the GUI controls.
- The flow splits into preparing a query, setting loading state, running the query asynchronously, then updating results and clearing loading.
- The Presentation Model is initialized with a one-argument search function and rejects functions with the wrong arity.
- Tests cover creating the model, preparing a query, executing a query, and handling the empty-results case.
- The module keeps three main operations: store the zip, set loading true, and run the search while filling stores and info.
- The updated LiveView delegates state changes to the Presentation Model and renders from presentation_model fields.
- The author says this makes the LiveView easier to test because the behavior is concentrated in plain, pure functions.
