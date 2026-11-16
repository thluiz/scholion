---
title: "Stop mocking fetch"
date: '2020-07-05T14:10:33+00:00'
category: webclip
summary: 'The article argues that mocking clients or fetch in tests lowers confidence and adds setup noise. It recommends using MSW to keep tests close to real requests while sharing handlers across tests and development.'
tags: ["msw", "testing", "fetch", "react"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Stop mocking fetch"
    url: "https://kentcdodds.com/blog/stop-mocking-fetch"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/kentcdodds-com--stop-mocking-fetch.md"
    kind: repo
---

The article argues that mocking a client or `window.fetch` can hide bugs in request shape, headers, and auth. It also adds duplicated backend setup across tests and reduces confidence in integration-level behavior.

## Reading notes

- Mocking the client makes it harder to know whether the client is being used correctly, especially if the client API changes.
- Mocking `window.fetch` gives more confidence than mocking the client, but still leaves gaps around headers and authentication details.
- Reimplementing backend behavior inside tests creates setup noise and duplicate work.
- A single fetch mock function can simulate backend behavior and keep most happy-path tests simple.
- MSW intercepts requests and lets tests use server handlers that resemble the real backend.
- The same handlers can be reused in browser development, which helps when endpoints are missing, broken, or unreachable.
- The article suggests colocating only the test-specific parts and using runtime handlers for edge cases and failures.
