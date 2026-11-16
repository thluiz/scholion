---
title: "Fake REST APIs That We Can Use to Build Prototypes"
date: '2020-07-05T14:11:19+00:00'
category: webclip
summary: 'The page lists fake REST APIs and local tools for prototypes, comparing what each one supports, from CRUD endpoints and CORS to custom routes, auth, failures, and static files.'
tags: ["fake-rest-api", "prototypes", "mock-api", "backend"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Fake REST APIs That We Can Use to Build Prototypes"
    url: "https://dev.to/aumayeung/fake-rest-apis-that-we-can-use-to-build-prototypes-54dm"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--fake-rest-apis-for-prototypes.md"
    kind: repo
---

The page collects several fake REST APIs and local mock tools that can speed up prototype work by avoiding a custom backend. Some are ready-made services with fixed endpoints and data, while others let you define your own routes, responses, and server behavior.

## Reading notes

- JSONPlaceholder supports CRUD requests, CORS, and common endpoints such as comments, photos, albums, todos, and posts.
- Reqres supports Ajax requests and offers GET, POST, PATCH, and DELETE routes, mostly for user-related flows and fake authentication.
- json-server is a local Node package that uses fake JSON data to define routes and can be configured with custom routes, middleware, HTTPS, and static files.
- Fake it till you make it offers free and paid tiers, with more nesting, request parameters, custom fields, and support in the paid version.
- Beeceptor lets you create a hosted endpoint, inspect payloads, simulate responses and failures, capture requests in real time, and test latencies and timeouts.
- Fake Rest API provides mock endpoints with included data such as address, arrays, and e-commerce data, and also lets you add your own data.
- api-now is a local Node package with default datasets, file-based data input, routes for upload, login, todos, and images, and a login route that returns a JSON web token.
- Mocky lets you generate an endpoint with a custom response, including status code, body, and headers.
