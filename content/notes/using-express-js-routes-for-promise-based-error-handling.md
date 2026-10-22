---
title: "Using Express.js Routes for Promise-based Error Handling"
date: '2021-08-04T12:25:27-03:00'
category: webclip
summary: 'The article compares three ways to handle promise-based responses and errors in Express routes, then proposes a promise middleware that centralizes response handling while still allowing special cases like redirects and streams.'
tags: ["express-js", "promise-handling", "middleware", "error-handling"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using Express.js Routes for Promise-based Error Handling | Toptal"
    url: "https://www.toptal.com/express-js/routes-js-promises-error-handling?utm_campaign=Toptal%20Engineering%20Blog&utm_medium=email&_hsmi=146444123&_hsenc=p2ANqtz-_y50iEQ9NYud-e3vXiuxiGpG2qBFu9jj6kUqLJX1qmsoA_LUTciVzFJEb7_DPZfqczP6_pyAdoWsDnxnoG6L1JS-MlWA&utm_content=146444123&utm_source=hs_email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-08/toptal-com--using-express-js-routes-for-promise-based-error-handling.md"
    kind: repo
---

The article starts from a typical Express app where each route repeats `.then()` and `.catch()` logic, which becomes hard to maintain as the number of routes grows. It then compares utility functions and error middleware with a custom promise middleware that attaches `res.promise()` and centralizes response handling.

## Reading notes

- Express does not support promise-based route handlers by default, so many tutorials lead developers into repeating response and error logic in each route.
- A small example app uses a `usersRouter`, a `userService`, and promise-returning service methods to show the repeated pattern in route handlers.
- The first alternative is to extract response and error handlers into utility functions, which removes some duplication but still requires imports and per-route wiring.
- The second alternative is to send errors to Express error middleware with `next`, but route handlers still need separate success handling and explicit `.catch(next)` calls.
- The proposed approach adds `res.promise()` through middleware, letting routes pass either a promise, a function, or a value and centralizing success and error handling.
- The app keeps error middleware for synchronous failures, and those errors are forwarded into the same centralized handling path with `Promise.reject()`.
- `res.promise()` is presented as optional, since direct response handling is still useful for redirects and stream piping.
- The redirect example uses `async`/`await` to fetch a URL and still sends errors through `res.promise()`.
- The stream example pipes an image response directly and notes that stream errors need separate handling depending on when they occur.
- The article says the pattern can also be extended to customize status codes, content type, and error formatting, while keeping route logic in one place.
