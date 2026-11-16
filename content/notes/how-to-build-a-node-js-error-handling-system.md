---
title: "How to Build a Node.js Error-handling System"
date: '2026-11-16T06:06:11+00:00'
category: webclip
summary: 'The article separates operational and programmer errors, recommends async/await with a custom Error hierarchy, and shows a centralized handler with logging, alerts, and graceful shutdown.'
tags: ["nodejs", "error-handling", "express", "logging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Best Practices for Node.js Error-handling | Toptal®"
    url: "https://toptal.com/nodejs/node-js-error-handling"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/toptal-com--how-to-build-a-node-js-error-handling-system.md"
    kind: repo
---

The article argues that Node.js error handling should distinguish operational errors from programmer errors. It recommends async/await over callbacks, a custom Error base class with useful fields, and a centralized component that handles logging, alerts, and monitoring.

## Reading notes

- Node.js developers can struggle with chaotic code, and proper error handling reduces debugging time while supporting larger applications.
- Operational errors are runtime problems that should be handled, while programmer errors are bugs in the code that need to be fixed.
- Callbacks can create nested error checks and callback hell, so promises or async/await are a better fit.
- Extending the built-in Error object can add useful information such as HTTP status codes and a clearer description.
- A centralized error-handling component helps avoid duplicated logic and can send logs, notifications, and monitoring events.
- In Express, async route errors can be forwarded to error-handling middleware, and Express 5 automatically passes rejected promises from async handlers.
- A custom logger can format output, support multiple levels, and write to different destinations depending on the environment.
- Structured logs can be paired with observability tools such as Datadog, New Relic, or OpenTelemetry.
- Programmer errors should cause the process to crash and restart cleanly with a tool such as PM2.
- Unhandled promise rejections and uncaught exceptions should be captured so the application can log the issue and shut down gracefully.
- The article presents error handling as an essential part of both development and production, not an optional extra.
