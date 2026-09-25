---
title: "Fascinating Dependency Injection"
date: '2026-09-25T21:52:04+01:00'
category: webclip
summary: 'The article explains Angular dependency injection as a hierarchical lookup tied to the DOM, then shows how providers, factory functions, and tokens can reduce boilerplate and solve dynamic and shared-state cases.'
tags: ["angular", "dependency-injection", "providers", "factory-functions"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Fascinating Dependency Injection"
    url: "https://www.angularspace.com/fascinating-dependency-injection/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/angularspace-com--fascinating-dependency-injection.md"
    kind: repo
---

Angular dependency injection is presented as a hierarchical system tied to the DOM, where the same token can resolve to different instances depending on context. The article then shows how different provider strategies and factory-based resolution can be used to keep code flexible, reduce boilerplate, and handle cases that are awkward with inputs alone.

## Reading notes

- DI is described as a hierarchical lookup system, not a simple pool of objects, and the nearest element injector is checked first.
- Each rendered HTML element gets its own `ElementInjector`, which explains why the same `ElementRef` can refer to different native elements in different places.
- If a token is not found in the current injector, Angular walks up through parent injectors, then the root injector, then the platform injector, and finally the `NullInjector`.
- This lookup behavior is compared to JavaScript prototype inheritance.
- A class can be provided with the shorthand `providers: [SomeService]`, which is equivalent to `useClass`.
- `useValue` is shown as a way to provide environment data through DI while keeping type safety.
- `useExisting` can expose only a limited shell API while delegating to a fuller third-party service.
- `useFactory` can choose an implementation at runtime, such as returning different logger services depending on the environment.
- A factory can also use `ActivatedRoute` and query parameters to choose between an `IncomeService` and an `ExpensesService` for a component.
- Abstract classes are used as DI tokens for transaction services because interfaces disappear at compile time.
- A shared registration form can be passed through a custom injection token instead of an input, preserving stronger typing and avoiding input-related complexity.
- If a child component only ever appears inside one parent, it can inject the parent component directly and access the parent’s form.
- A global loading text can be provided through an optional injection token so consumers can override the default text without affecting explicit component input values.
- The article closes by framing these DI patterns as underused but useful for large Angular applications.
