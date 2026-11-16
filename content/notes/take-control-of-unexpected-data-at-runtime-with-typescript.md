---
title: "Take control of unexpected data at runtime with TypeScript"
date: '2026-11-16T02:48:48+00:00'
category: webclip
summary: 'The article shows how TypeScript type definitions can be paired with runtime validators to catch bad config and API data, then contrasts exception-based handling with Result and Either workflows.'
tags: ["typescript", "runtime-validation", "runtypes", "io-ts"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Take control of unexpected data at runtime with TypeScript - LogRocket Blog"
    url: "https://blog.logrocket.com/using-typescript-to-stop-unexpected-data-from-breaking-your-app"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-logrocket-com--take-control-of-unexpected-data-at-runtime-with-typescript.md"
    kind: repo
---

The article argues that TypeScript helps at compile time, but runtime data can still be wrong. It uses bad config files and API responses to show why runtime validation matters, then compares exception-based handling with Result- and Either-based flows.

## Reading notes

- TypeScript can catch many mistakes at compile time, but runtime data can still break an app.
- A typo in a config file can pass compilation and fail only when the program runs.
- `runtypes` lets the app validate unknown data against a declared record before using it.
- The `check` method turns unexpected config into a caught `ValidationError`.
- API responses can also disagree with type definitions, so runtime checks help during testing and QA.
- With `runtypes`, a fetched todo can be parsed and validated before its fields are accessed.
- The article shows that fields may be omitted if the app does not need them, and nullable fields can be modeled explicitly.
- It then presents errors as data with a `Result` type that separates success from failure.
- `Result` keeps validation outcomes in the value flow instead of relying only on exceptions.
- `io-ts` uses `Either`, which carries a left error value and a right success value.
- The article shows how `Either` can be composed in a pipeline to transform validated purchase data into a receipt.
- It presents Elm as an example of a language that aims to avoid runtime exceptions by requiring validation of external data.
- The conclusion says the right approach depends on the app: simple scripts may crash, while long-running apps benefit from recovery or data-based errors.
