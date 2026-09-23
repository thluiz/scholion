---
title: "My New Angular Coding Style"
date: "2026-09-23T17:47:59+01:00"
category: webclip
has_commentary: false
summary: "Kevin Kreuzer documents the coding style his team converged on after rewriting a large codebase around Angular Signals: standalone by default, no lifecycle hooks, inject() over constructors, often no constructor at all."
tags:
  - angular
  - signals
  - frontend-architecture
  - typescript
sources:
  - title: "My new Angular Coding Style - Angular Experts"
    url: "https://angularexperts.ch/blog/new-angular-coding-style?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/angularexperts-ch--my-new-angular-coding-style.md"
    kind: repo
---

Kevin Kreuzer rewrote a large Angular codebase around Signals and Signal-based APIs, and documents the coding conventions that emerged from it, marking each as either a widely-recommended best practice or his team's own preference. Angular 19 makes standalone components the default (with a compiler flag, strictStandalone, that errors on any non-standalone component, directive, or pipe), and Kreuzer treats full adoption of the signal APIs (signals, computed, signal inputs, signal queries) as the baseline for a codebase that wants to be ready for Zoneless Angular, where Zone.js-driven change detection goes away in favor of granular, signal-driven updates.

The more opinionated calls follow from committing to signals fully. Since signals need an initial value at field creation, initialization logic that used to live in a constructor mostly disappears, and effects or the newer afterRender/afterNextRender hooks can be assigned directly to private class fields instead of being wired up inside a constructor body, leaving many of his components with no constructor at all. He also argues for replacing async pipes with toSignal() conversions before binding data in templates (RxJS still handles the HTTP layer) and for replacing TypeScript's private keyword, a compile-time-only restriction, with JavaScript's # private field syntax, which is enforced at runtime.

## Fichamento

- Angular 19 makes standalone components the default and adds a strictStandalone compiler flag that errors on any component, directive, or pipe that isn't standalone.
- Kreuzer treats full adoption of the signal APIs (signals, computed signals, signal inputs, signal queries) as foundational, framing it as both a reactivity improvement and preparation for Angular's move to Zoneless change detection.
- Zoneless readiness in practice: build with signals and OnPush change detection even while still running inside Zone.js; an app built that way runs the same with Zone.js removed later.
- Traditional lifecycle hooks like ngOnInit and ngAfterViewInit become largely unnecessary once state derives from computed() and effect() instead of imperative hook callbacks; his worked example replaces an ngOnChanges-based even/odd check with a two-line computed().
- He recommends inject() over constructor-based dependency injection: it preserves correct typing with injection tokens, works inside composable helper functions (not just class constructors), and removes the need to pass injected services through super() in subclasses. Trade-off flagged: switching can break unit tests that mock dependencies without TestBed.
- His most opinionated claim: full adoption of inject() plus signal-based field initialization makes constructors nearly unnecessary, since effects and afterRender/afterNextRender can be assigned directly as private class fields instead of being set up in a constructor body.
- He argues for dropping the async pipe entirely once a codebase is signals-first, converting RxJS streams to signals with toSignal() before they reach the template, while still using RxJS to handle the underlying HTTP/stream logic.
- He recommends JavaScript's # private field syntax over TypeScript's private keyword: private is erased at compile time and unenforced in the emitted JavaScript, while # stays genuinely inaccessible from outside the class at runtime.
