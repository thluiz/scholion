---
title: "Angular 2 First App Post-Mortem"
date: '2016-02-07T22:50:27-03:00'
category: webclip
summary: 'The author says Angular 2 is powerful but complex, with strong reactive programming support, improved dependency injection, and a promising router, while also noting tooling gaps, type-system limits, and a heavy payload.'
tags: ["angular-2", "reactive-programming", "dependency-injection", "router"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Angular 2 First App Post-Mortem — Medium"
    url: "https://medium.com/@MikeRyan52/angular-2-first-app-post-mortem-b2b2b3618828#.j00nfhe78"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/medium-com--angular-2-first-app-post-mortem.md"
    kind: repo
---

The post-mortem says Angular 2 is powerful but often complex to use. The author highlights reactive programming with RxJS and Redux, the async pipe, improved dependency injection, the new router, and the advantages of TypeScript, while also pointing to documentation gaps, type-definition mismatches, and app weight.

## Reading notes

- Angular 2 lets the author use RxJS, Redux, and observables throughout the app, including route state and change detection.
- The async pipe makes it easier to connect observable state to templates and component updates.
- Splitting components into wrapper and pure components, along with OnPush change detection, reduces unnecessary checks.
- Dependency injection is better than Angular 1’s string-based approach, with tokens, type-based bindings, and hierarchical injectors.
- TypeScript runtime metadata loses precision for interfaces, generics, and arrays, which limits what can be injected by type.
- Community type definitions can mismatch real libraries, causing runtime errors that are hard to debug.
- The new Component Router is usable for light routing needs but still lacks features like route errors, 404 handling, and data resolution.
- The author recommends TypeScript over ES5 or vanilla ES2015 because Angular 2 relies heavily on decorators and documentation is sparse outside TypeScript.
- Angular 2 is presented as heavier than Angular 1 in both complexity and initial payload size, even if its template language is more explicit and safer.
