---
title: "CORS in Phoenix"
date: '2015-07-19T10:40:41-03:00'
category: webclip
summary: 'Explains why SPAs need a backend, how Phoenix serves as a JSON API, what CORS is, and how Phoenix plugs can add CORS headers while handling pre-flight OPTIONS requests.'
tags: ["cors", "phoenix", "single-page-applications", "api"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "CORS in Phoenix"
    url: "http://www.leighhalliday.com/cors-in-phoenix"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/leighhalliday-com--cors-in-phoenix.md"
    kind: repo
---

The page says that single page applications depend on a backend for data, authentication, and permissions, and that Phoenix works well as a JSON API for a JavaScript front end. It then introduces CORS as the browser agreement that allows requests across domains, including the pre-flight OPTIONS request that checks which methods are allowed.

## Reading notes

- SPAs are presented as relying on a backend to fetch and send data, and the API also handles authentication and permissions.
- Phoenix is described as a strong JSON API for JavaScript front ends, built in Elixir.
- CORS is defined as the mechanism that lets resources be requested from another domain, using request and response headers.
- Modern browsers can send a pre-flight request before the main request to confirm whether it will be permitted.
- In Phoenix, CORS can be handled with plugs such as CORSPlug or Corsica, added to the `:api` pipeline.
- A problem appears when OPTIONS requests return 404 because no matching route exists, so the plug is never called.
- The fix shown is to define `options` routes for the relevant endpoints so the plug can intercept the request correctly.
