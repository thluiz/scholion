---
title: "How to make your Express.js APIs 9x faster with Encore.ts"
date: '2026-09-24T23:59:37+01:00'
category: webclip
summary: 'The guide shows how to migrate an Express.js app to Encore.ts to gain type-safe APIs, a Rust runtime, and a 9x performance boost, with partial or complete migration.'
tags: ["express-js","encore-ts","typescript","performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to make your Express.js APIs 9x faster with Encore.ts"
    url: "https://dev.to/encore/how-to-make-your-expressjs-apis-9x-faster-with-encorets-1ke2?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--how-to-make-your-express-js-apis-9x-faster-with-encore-ts.md"
    kind: repo
---

Encore.ts is presented as an open source backend framework for TypeScript that helps migrate an Express.js app toward type-safe APIs and higher performance. The article says Encore.ts has no npm dependencies, includes built-in backend features, and can be self-hosted or used with Encore Cloud.

It then compares Express.js and Encore.ts across migration paths and features. A quick forklift migration can wrap an existing router as a catch-all handler and give partial performance gains, while a full migration unlocks distributed tracing, architecture diagrams, API client generation, and the full 9x speedup. The rest of the guide walks through APIs, microservice communication, authentication, request validation, error handling, static files, template rendering, testing, databases, and logging.

## Reading notes

- The text presents Encore.ts as an open source backend framework for TypeScript designed for robust and type-safe backends.
- The central proposal is to migrate an Express.js app to Encore.ts to obtain typed APIs and a 9x performance gain.
- The article states that Encore.ts has zero npm dependencies, includes ready-to-use features, and can be run in any service that accepts Docker containers or on Encore Cloud Platform.
- Encore.ts runtime runs in Rust, uses an asynchronous multithreaded event loop, and the text attributes to this 9x more requests per second and 80% less response latency compared to Express.js.
- In the quick migration, the text proposes wrapping the existing HTTP router in a catch-all handler to move the application all at once and then gradually extract endpoints into Encore.ts.
- This approach gives an immediate partial gain, but prevents fully taking advantage of distributed tracing, automatic diagrams, API documentation, and client generation while everything continues passing through the generic handler.
- In the full migration, the goal is to fully replace the dependency on Express.js and start using all the features and the full performance gain of Encore.ts.
- The feature comparison covers APIs, communication between services, authentication, request validation, error handling, static files, templates, tests, database, and logging.
- In APIs, the text shows that Express.js uses `app.get` and similar methods, while Encore.ts uses `api` with a typed schema and also supports raw endpoints when it is necessary to access the underlying HTTP request.
- In microservice communication, the text says that calls between services in Encore.ts look like local calls, but are converted into real HTTP calls with trace data.
- In authentication, the text explains that Encore.ts uses `auth: true`, `authHandler` and `getAuthData` to identify the authenticated user.
- In validation, the text states that Encore.ts automatically validates headers, query params and body from the schema and returns error 400 when the payload does not match what is expected.
- In errors, the text says that throwing exceptions generates 500 and that `APIError` allows returning specific codes.
- In static files and templates, the text shows native support for `api.static` and the use of `api.raw` to serve dynamic HTML.
- In tests, the text states that Encore.ts endpoints can be called directly in tests and run with `encore test`.
- In database, the text says that Encore.ts provisions databases automatically, uses migrations and provides methods such as `.query`, `.queryRow` and `.exec`.
- In logging, the text highlights native support for structured logging integrated with distributed tracing.
