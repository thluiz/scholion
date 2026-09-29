---
title: "How to Build a PWA in Vanilla JavaScript"
date: '2020-05-29T19:15:54-03:00'
category: webclip
summary: 'The post outlines a basic PWA built with plain JavaScript, a manifest, a service worker and an Express server. It ends with a cached app that can be accessed offline and checked with Lighthouse.'
tags: ["pwa", "service-worker", "express", "offline"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Build a PWA in Vanilla JavaScript ← Alligator.io"
    url: "https://alligator.io/js/vanilla-pwa/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-05/alligator-io--how-to-build-a-pwa-in-vanilla-javascript.md"
    kind: repo
---

The article starts a three-part series on building a Progressive Web App with the Web Push API and cron-schedule. In this first part, it covers the front end, the web app manifest, the service worker, and a simple Express setup, using only JavaScript.

## Reading notes

- The app is meant to remind the author to take pills every day, even when the browser is not open.
- A manifest is generated for the app and placed in a public folder with icons and basic metadata.
- The example app is called Temporas.
- The page registers a service worker from index.html.
- The service worker caches index.html and manifest.json during install.
- Fetch requests are intercepted so cached files are served when available.
- The app is served through Express instead of opening public/index.html directly.
- The server uses body-parser for JSON and serves the public folder as static content.
- Running the app from localhost lets it keep working from the service worker cache after the server is stopped.
- The author recommends disabling service worker caching while developing new features.
- Lighthouse is suggested for testing the PWA.
- The app must be served over HTTPS to count as a PWA and to be installable.
