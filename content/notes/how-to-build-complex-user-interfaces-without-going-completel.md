---
title: "How to build complex user interfaces without going completely insane"
date: '2017-06-10T14:32:38-03:00'
category: webclip
summary: 'The article recommends delaying state updates in dialogs, separating model data from UI state, and favoring integration tests over unit tests when building complex web interfaces.'
tags: ["user-interface", "state-management", "integration-testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to build complex user interfaces without going completely insane"
    url: "https://medium.freecodecamp.com/3-tips-to-keep-in-mind-while-developing-complex-ui-in-web-b56312310390"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-06/medium-freecodecamp-com--how-to-build-complex-user-interfaces-without-going-completel.md"
    kind: repo
---

The article argues that complex UIs become easier to manage when temporary edits stay in component state until the user saves them, so the application state only changes after confirmation. It also says business data and UI state should remain separate, with validation logic living in the model rather than in view code.

## Reading notes

- Keep temporary edits in a component’s internal state and update the application state only when the user presses Save.
- This approach lets the dialog be discarded without changing the stored record and can avoid exposing temporary values to other users.
- Keep model data and UI-related data separate instead of mixing business logic into view components.
- Put rules such as whether a task can be saved into the model, then use that model method in the view.
- Prefer integration testing over unit testing when choosing how to test features in a complex web app.
- For bugs, write a failing test first, fix the code, and then verify that the test no longer fails.
