---
title: "PWA: Create a New Update Available Notification using Service Workers"
date: '2020-07-05T14:11:26+00:00'
category: webclip
summary: 'The post explains how to notify users when a cached PWA has a newer version, using service worker update checks, cache strategies, and an update-found hook while keeping fast offline-first loading.'
tags: ["service-workers", "progressive-web-app", "cache-busting"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "PWA: Create a New Update Available Notification using Service Workers | by Simon Wicki | Progressive Web Apps | Medium"
    url: "https://medium.com/progressive-web-apps/pwa-create-a-new-update-available-notification-using-service-workers-18be9168d717"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--pwa-create-a-new-update-available-notification-using-service.md"
    kind: repo
---

The post explains that PWAs can load instantly through HTTP caching, but that offline-first setups cache the resources needed to launch the app, including index.html. It describes how to keep the fast cached experience while still letting users know when a newer version has been cached.

## Reading notes

- PWAs improve the web experience and can load an app instantly through HTTP caching.
- Offline-first means caching all resources needed to launch the web app, including index.html.
- The browser does not keep a cached version forever; Chrome treats long max-age values as 24 hours.
- The article outlines three files in the setup: index.html, service-worker.js, and app code that listens for update availability.
- It lists common cache strategies such as networkOnly, cacheOnly, fastest, networkFirst, and cacheFirst.
- In most cases, the choice is between loading instantly from cache or checking the network first and falling back to cache.
- To notify users about a newer cached version while keeping fast loading, the setup hooks into onupdatefound in the Service Worker.
- The Service Worker checks the hash of service-worker.js, so even a small change in that file counts as a new version.
- The example uses Ionic 3 to show a toast when an update is available.
- A caveat is that hosting services may add max-age headers automatically, especially for service-worker.js.
- The post mentions a Firebase Hosting configuration and notes that the public folder points to ./platforms/browser/www/ in the Ionic 3 setup.
