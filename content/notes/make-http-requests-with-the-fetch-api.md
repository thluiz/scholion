---
title: "Make HTTP Requests with the Fetch API"
date: '2020-04-20T21:22:36+00:00'
category: webclip
summary: 'The article explains how fetch makes client-side HTTP requests easier than XMLHttpRequest, how to send GET, POST, and file-upload requests, and how to read response data and status information.'
tags: ["fetch-api", "http-requests", "response-object", "client-side"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Make HTTP Requests with the Fetch API"
    url: "https://dev.to/aumayeung/make-http-requests-with-the-fetch-api-mmk"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--make-http-requests-with-the-fetch-api.md"
    kind: repo
---

The article says the Fetch API replaced the older XMLHttpRequest approach for client-side HTTP requests because it is promise-based and easier to use. It also introduces standardized Request and Response objects, along with related definitions for CORS and HTTP origin header semantics.

## Reading notes

- Fetch starts with `fetch`, which takes a required resource path and can also receive an optional `init` object.
- The promise from `fetch` resolves to a `Response`, even when the HTTP status is 404 or 500; in those cases, `ok` is `false`.
- `fetch` does not receive cross-site cookies, and it only sends cookies when the `credentials` option is set.
- A simple request can call `response.json()` and then log the resulting JavaScript object.
- The second argument can include `method`, `headers`, `body`, `mode`, `credentials`, `cache`, `redirect`, `referrer`, `referrerPolicy`, `integrity`, `keepalive`, and `signal`.
- A POST request can send JSON in `body` and set `Content-type` to `application/json; charset=UTF-8`.
- A file can be taken from a file input and sent in the request body, with the header adjusted to the server being used.
- `Response` and `Body` provide methods such as `error`, `redirect`, `formData`, `json`, `text`, `arrayBuffer`, and `blob`.
- Useful response properties include `headers`, `ok`, `redirect`, `status`, `statusText`, `url`, and `body`.
- The article concludes that Fetch is better than XMLHttpRequest because it handles many request types, supports text and binary bodies, and works well with other promises.
