---
title: "Our journey to F#: bye-bye fluent syntax"
date: '2026-11-16T04:38:43+00:00'
category: webclip
summary: 'The post replaces a C#-style fluent builder with an F# design based on discriminated unions and an execute function, so shared logging, error handling, and rollback live in one place.'
tags: ["f-sharp", "discriminated-unions", "builder-pattern", "error-handling"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Our journey to F#: bye-bye fluent syntax"
    url: "https://planetgeek.ch/2020/07/16/our-journey-to-f-bye-bye-fluent-syntax"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/planetgeek-ch--our-journey-to-f-bye-bye-fluent-syntax.md"
    kind: repo
---

The post shows how the author moved from a fluent builder style in C# to a simpler F# runner design. Instead of chaining methods, the steps are modeled as a discriminated union and passed to an execution function, which keeps the common logic in one place and reduces syntax noise.

## Reading notes

- In C#, the preferred builder style uses fluent syntax for defining test setup, complex test data, or compensation steps.
- In F#, the same fluent style works but feels awkward because it depends on classes, extension methods, and many dots.
- The alternative design uses a discriminated union to represent steps and a function to execute them.
- Each union case carries the data needed for that specific step.
- Shared functionality such as logging, error handling, and rollback is handled inside `execute`.
- Dependencies that are used by most steps, such as `operationId`, `logger`, and `sendRollbackMessage`, are passed to `execute`.
- Dependencies and data used by a single step are passed directly to that step.
- The resulting call is shorter than the fluent C# version, though IntelliSense helps less.
- The author mentions computation expressions as another possible approach but does not use them because the runners are nested in `async` workflows.
