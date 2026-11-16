---
title: "Prepare your Angular web app to grow: keep it performant and consistent from the beginning"
date: '2020-02-22T12:11:53+00:00'
category: webclip
summary: 'The article argues that Angular apps should be built with lazy loading, state management, OnPush change detection, container-presentational components, and schematics so they stay easier to expand and maintain.'
tags: ["angular", "performance", "state-management", "schematics"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Prepare your @angular web app to grow: keep it performant and consistent from the beginning"
    url: "https://dev.to/julianobrasil/prepare-your-angular-web-app-to-grow-keep-it-performant-and-consistent-from-the-beginning-50kp"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--prepare-your-angular-web-app-to-grow-performant-consistent.md"
    kind: repo
---

The article says Angular’s opinionated structure is a good starting point, but an app can become slow and hard to maintain if it grows without deliberate architectural choices. It focuses on practices that help an Angular web app stay healthy as features and complexity increase.

## Reading notes

- Lazy load feature modules so users do not download the whole app up front, and use preloading only as a UX choice.
- Treat lazy loading as a user-experience measure, not as security, because real protection belongs on the back end.
- Use state management to keep shared information consistent across views and to preserve form data when users navigate away and return.
- Prefer established state libraries such as NGRX, NGXS, or Akita instead of building a custom global store from scratch.
- Use `ChangeDetectionStrategy.OnPush` to limit unnecessary view updates, especially in heavy components with many subcomponents.
- Organize components as container and presentational components so data access stays separated from rendering concerns.
- Keep presentational components focused on `@Input()` and `@Output()` data flow, while containers talk to APIs and global state.
- Use Angular CLI schematics to reduce boilerplate and make repeated project structures faster to create.
- Custom schematics can generate feature modules, components, routing, and related setup in a much shorter time than manual creation.
