---
title: "The 80/20 Guide to Express Error Handling"
date: '2026-09-27T00:38:55+01:00'
category: webclip
summary: 'Explains how Express error-handling middleware centralizes HTTP error responses, how `next()` routes async failures to handlers, and how `wrapAsync()` makes async/await errors work cleanly.'
tags: ["express", "error-handling", "async-await", "nodejs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The 80/20 Guide to Express Error Handling"
    url: "http://thecodebarbarian.com/80-20-guide-to-express-error-handling.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/thecodebarbarian-com--80-20-guide-to-express-error-handling.md"
    kind: repo
---

Express error-handling middleware centralizes HTTP error response logic so you do not have to repeat `try/catch` and status-code handling in every route. The post shows that error handlers are middleware with four arguments, must come last in the chain, and only receive errors passed through `next()`.

## Reading notes

- A small number of endpoints can use local `try/catch`, but that approach becomes hard to maintain across many routes.
- Changing a response code or adding dev-only stack traces is easier when error handling is centralized.
- Error-handling middleware is identified by four arguments and runs only when an error is present.
- Errors thrown asynchronously will crash the server unless they are passed to `next()`.
- Route handlers can accept `next()` and use it to forward async errors.
- Error handlers must be defined after the other middleware, or Express will not reach them.
- `async` functions return promises, so a helper like `wrapAsync()` can call `.catch(next)` and send async failures to the error chain.
- Separate handlers can map different error types to different HTTP responses, such as assertion errors to 400 and database errors to 503.
- The overall goal is to keep error handling out of business logic and let middleware decide how to answer the request.
