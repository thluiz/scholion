---
title: "The SAM (State - Action - Model) pattern"
date: '2016-06-03T15:25:14+00:00'
category: webclip
summary: 'SAM is presented as a reactive, functional pattern that separates business logic from the view, decouples backend APIs from the frontend, and replaces MVC with State as a further layer of separation.'
tags: ["sam-pattern", "mvc", "frontend-architecture", "state-machine"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The SAM (State - Action - Model) pattern - General Discussion, Blog Posts, Wiki | Elixir Forum"
    url: "https://elixirforum.com/t/the-sam-state-action-model-pattern/703"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/elixirforum-com--the-sam-state-action-model-pattern.md"
    kind: repo
---

SAM is described as a reactive, functional pattern for frontend architecture. It separates business logic from the view, decouples backend APIs from the frontend, and is said to work across web apps, native apps, and different protocols.

The page also frames SAM as a replacement for MVC. It says SAM is reactive rather than interactive, and that its main change is the introduction of State, which further separates the view from the model and treats the view as a State Representation.

## Reading notes

- SAM is a reactive and functional pattern.
- It separates business logic from the view.
- It strictly decouples backend APIs from the frontend.
- It is technology independent and can be used for web apps or native apps.
- It is protocol independent and can be implemented over HTTP, WebSockets, and other protocols.
- It aims to replace MVC.
- SAM is reactive, while MVC is generally implemented in an interactive way.
- SAM is not described as a reactive implementation of MVC.
- SAM introduces State to further decouple the View from the Model.
- The view is treated as a State Representation.
