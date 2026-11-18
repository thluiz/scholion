---
title: "Introduction to Service Workers in JavaScript"
date: '2019-07-20T08:36:28+00:00'
category: webclip
summary: 'The post explains what service workers do in Progressive Web Apps, how they register and run, which browser events they handle, and how they cache resources and update versions.'
tags: ["service-workers", "progressive-web-apps", "cache-api", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Introduction to Service Workers in JavaScript"
    url: "https://dev.to/attacomsian/introduction-to-server-workers-in-javascript-1epa"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--introduction-to-service-workers-in-javascript.md"
    kind: repo
---

The post describes service workers as a core part of Progressive Web Apps. They sit between the web app, the browser, and the network, letting developers intercept requests, cache resources, and support offline use and push notifications.

## Reading notes

- Service workers run on a separate thread, so they are non-blocking, but they cannot access the DOM, cookies, XHR, or web storage APIs.
- They are fully asynchronous and rely heavily on promises.
- They only run over HTTPS and cannot be used in private browsing mode.
- Browser support should be checked with `if ('serviceWorker' in navigator)`.
- Registration happens after the page loads with `navigator.serviceWorker.register('/sw-worker.js')`.
- The registration lifecycle has three steps: download, install, activate.
- After a first visit, the service worker file is downloaded and installation is attempted immediately.
- Its functionality becomes available only after the user visits another page or refreshes the current page.
- The browser emits `install`, `activate`, `fetch`, `push`, and `sync` events inside the service worker.
- `install` can be used to cache resources with the Cache API.
- `fetch` can return a cached response when one exists, or fetch the resource from the network.
- New network responses can also be cloned and stored in the cache.
- `activate` can be used to remove outdated cache resources.
- Updating a service worker means uploading a new version of the file on the server; the browser detects even a one-byte change.
