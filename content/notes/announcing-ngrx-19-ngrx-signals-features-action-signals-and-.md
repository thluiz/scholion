---
title: "Announcing NgRx 19: NgRx Signals Features, Action Signals, and more!"
date: '2026-09-25T00:40:25+01:00'
category: webclip
summary: 'NgRx 19 adds new Signals features, a signalMethod utility, dev-mode mutation checks, and Store support for dispatching actions from signal changes, and recommends NgRx Signals for local state.'
tags: ["ngrx","angular-signals","state-management","signals"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Announcing NgRx 19: NgRx Signals Features, Action Signals, and more!"
    url: "https://dev.to/ngrx/announcing-ngrx-19-ngrx-signals-features-action-signals-and-more-2b35?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--announcing-ngrx-19-ngrx-signals-features-action-signals-and-.md"
    kind: repo
---

NgRx 19 introduces updates to NgRx Signals, support for dispatching actions when signals change, and a recommendation to use NgRx Signals as the default local state library for Angular apps. It also announces workshops, a new docs site, and upgrade guidance for Angular 19, TypeScript 5.5, and RxJS.

## Reading notes

- Version 19 brings improvements to NgRx Signals, which was already stable since v18 and received updates to improve the development experience.
- The new `withProps` allows defining props when creating a SignalStore, organizing dependencies in one place, and integrating resources such as `resource` and `linkedSignal`.
- The `signalMethod` utility offers a way to handle side effects using only signals, with flexible input, without requiring injection context, and with explicit tracking of the parameter signal.
- In development mode, `patchState` now applies deep freeze to the state to prevent mutations and preserve immutable updates.
- NgRx Store now accepts dispatch of actions that read signals, executing initially and whenever the observed signal changes, with extra care outside the injection context.
- The text says that NgRx Signals has become the recommended library for local state in Angular applications, with a suggestion to start with SignalStore in new projects and migrate to `@ngrx/signals` in existing projects.
- The publication also announces workshops from the NgRx team, a new documentation site, and deprecation/breaking changes with a migration guide for version 19.
- To update, the text informs minimum versions of Angular, Angular CLI, TypeScript, and RxJS and shows the `ng update` commands for `@ngrx/store@19` and `@ngrx/signals@19`.
