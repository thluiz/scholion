---
title: "Node.js Best Practices — Caching and REST"
date: '2020-09-09T18:03:48-03:00'
category: webclip
summary: 'The page recommends Redis caching for Express apps, monitoring and logging at the server level, setting NODE_ENV to production for caching and template performance, and using REST-style HTTP routes and methods.'
tags: ["node-js", "redis", "rest", "express"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Node.js Best Practices — Caching and REST - The Web Dev"
    url: "https://thewebdev.info/2020/08/13/node-js-best-practices%e2%80%8a-%e2%80%8acaching-and-rest/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/thewebdev-info--node-js-best-practices-caching-and-rest.md"
    kind: repo
---

The page says Node apps should be written well to avoid problems later. It focuses on Redis caching for Express, server-wide monitoring and logging, the performance impact of NODE_ENV, and REST-aligned routes and HTTP methods.

## Reading notes

- Redis can be used to cache Express responses and speed up the app.
- The example installs Redis, changes its systemd setting, restarts the service, and adds the redis NPM module.
- A cache middleware checks Redis for an `id`, returns cached data when it exists, and calls the database-backed handler when it does not.
- Server or virtual machine monitoring and logging can help watch for issues from the app.
- `NODE_ENV=production` enables caching, so development should avoid it when fresh data is needed.
- In production, Express caches views and does less Pug template work, which frees CPU for other tasks.
- The page shows how to set `NODE_ENV` in Linux, macOS, Windows, and by prefixing the node command.
- REST routes should match HTTP methods, with `POST`, `GET`, `PATCH`, and `DELETE` used for article creation, listing, retrieval, updates, and removal.
- When getting an item by ID, the ID should appear at the end of the route.
