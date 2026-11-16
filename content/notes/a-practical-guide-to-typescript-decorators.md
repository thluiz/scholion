---
title: "A practical guide to TypeScript decorators"
date: '2020-07-05T14:10:46+00:00'
category: webclip
summary: 'The article compares decorators in JavaScript and TypeScript, then shows class, method, property, accessor, parameter, auto-accessor, composition, and factory patterns with examples.'
tags: ["typescript", "decorators", "javascript", "advanced-patterns"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A practical guide to TypeScript decorators - LogRocket Blog"
    url: "https://blog.logrocket.com/a-practical-guide-to-typescript-decorators"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-logrocket-com--a-practical-guide-to-typescript-decorators.md"
    kind: repo
---

The article explains that decorators are a design pattern for wrapping something to change its behavior. It contrasts JavaScript and TypeScript support, notes that TypeScript 5.0 aligns with the stage three proposal, and points out that parameter decorators are not supported in the new model.

## Reading notes

- Decorators can be attached to classes, methods, properties, accessors, and parameters in TypeScript, while JavaScript currently only decorates class declarations and methods.
- TypeScript can type-check decorator parameters and return values, unlike JavaScript.
- The article shows how to set up a TypeScript project with Node.js, TypeScript, and ts-node.
- New-style decorators use a `Decorator` type with `target` and `context`, where `context` carries metadata such as `kind`, `name`, `access`, `private`, `static`, and `addInitializer`.
- A class decorator can return a new class or modify the prototype to add behavior such as `fuel` and `isEmpty()` to a `Rocket` class.
- A class decorator can also wrap an existing class method, as in the `logFuel` example around `addFuel`.
- Method decorators can wrap method calls to log deprecation warnings or alter invocation behavior.
- Property decorators have similar uses to method decorators, including deprecation and access tracking.
- Accessor decorators can target getters and setters, and one decorator can handle methods, getters, setters, and fields with shared deprecation logic.
- Auto-accessor fields compile to a getter and setter pair backed by a private property.
- Parameter decorators are described as part of the older model and are not supported in TypeScript 5.0.
- One use case is measuring execution time with `performance.now()` from Node.js `perf_hooks`.
- Decorator composition lets multiple decorators run on the same element, with order mattering.
- Decorator factories return decorators and allow configuration, such as `fill(value)` for fields or `Throttle(delay)` for methods.
- The article also shows a fuel check pattern that blocks `launch()` when `this.fuel` is below a minimum.
- The conclusion notes that libraries and frameworks such as TypeORM and Angular already provide many decorators, but understanding the mechanism is still useful.
