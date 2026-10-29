---
title: "ServiceWorker: Revolution of the Web Platform"
date: '2015-10-27T12:01:08-03:00'
category: webclip
summary: 'The article argues that ServiceWorker is a major web-platform addition, enabling request interception, offline access, push notifications, background sync, and finer caching control.'
tags: ["serviceworker", "offline", "web-platform", "caching"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "ServiceWorker: Revolution of the Web Platform"
    url: "https://ponyfoo.com/articles/serviceworker-revolution"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-10/ponyfoo-com--serviceworker-revolution-of-the-web-platform.md"
    kind: repo
---

ServiceWorker is presented as one of the most significant additions to the web platform since AJAX. It can intercept requests before they are dispatched, deliver responses from the client side, and enable offline access, push notifications, background sync, and add-to-home-screen behavior.

## Reading notes

- ServiceWorker is described as the evolution of AppCache, replacing its confusing declarative model with a programmatic JavaScript API.
- It runs on the client side, outside the scope of a single page, and has no DOM access.
- The article notes that it depends heavily on promises and requires HTTPS on deployed sites.
- Registration uses a feature test so older browsers keep working, and the worker script is registered from the main client code.
- Scope depends on the registration path, so a worker registered at `/service-worker.js` can cover the whole origin.
- The lifecycle includes `installing`, `installed`, `activating`, `activated`, and `redundant`.
- During `install`, the worker can prefill caches with resources needed for offline use.
- During `activate`, older cache versions can be removed by deleting keys with outdated prefixes.
- Once activated, the worker receives `fetch` events for network requests from the site.
- A basic strategy is to pass requests through to the network with `fetch(event.request)`.
- Non-`GET` requests are usually left to the network.
- One strategy is network first with cache fallback, which favors fresh content but helps mainly when the site is fully offline.
- Another strategy is cache first with network refresh, which improves repeat visits but can serve stale content briefly.
- The article mentions `postMessage` as a way to update the UI after cached content has been refreshed.
- The implementation shown uses cache first, then network, storing successful network responses back into the cache.
- When the network fails, the worker can return a fallback response.
- For images, it can return cached placeholder assets.
- For gravatars, it can return a specific cached fallback image.
- For HTML requests on the same origin, it can return an `/offline` page.
- For same-origin JSON requests in the single-page app, it can return a JSON offline view that the app interprets.
- The article closes by saying repeat visits can avoid requests entirely and reduce load time and page weight substantially.
