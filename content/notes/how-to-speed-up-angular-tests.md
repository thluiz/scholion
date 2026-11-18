---
title: "How to Speed Up Angular Tests"
date: '2019-12-29T01:39:33+00:00'
category: webclip
summary: 'The article says Angular tests are slow because dependencies and components are reloaded for every test. It recommends loading them once per spec file with a shared helper to make unit tests much faster.'
tags: ["angular-tests", "test-speed", "testing", "angular"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Speed Up Angular Tests"
    url: "https://dev.to/aumayeung/how-to-speed-up-angular-tests-5e5h"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--how-to-speed-up-angular-tests.md"
    kind: repo
---

Angular tests are slow by default because many dependencies are injected and the tested components are reloaded for each test. The article says this can make runs last 30 minutes or more, so the fix is to load the dependencies once per test file and reuse them.

## Reading notes

- Create a shared `spec-helper.spec.ts` file and define a `beforeTest` function there.
- Inside `beforeAll`, reset the testing module, configure `TestBed` with the app components, modules, and providers, and compile the components once.
- After compilation, override `TestBed.resetTestingModule` so Angular does not reset the testing module again.
- Import that helper in spec files and call `beforeTest`.
- This setup makes unit tests run much faster, from about 30 minutes to a few seconds.
- It also reduces the need to repeat dependencies in every test file and lowers the risk of missing a dependency in a test module.
