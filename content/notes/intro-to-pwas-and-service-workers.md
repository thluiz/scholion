---
title: "Intro to PWAs and Service Workers"
date: '2026-11-16T00:46:15+00:00'
category: webclip
summary: 'The article defines PWAs, compares native, hybrid, and PWA apps, and shows how service workers enable offline support, caching, and the service worker lifecycle.'
tags: ["progressive-web-apps", "service-workers", "offline-support"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Intro to PWAs and Service Workers"
    url: "https://dev.to/thisdotmedia/intro-to-pwa-and-service-workers-15d4"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--intro-to-pwas-and-service-workers.md"
    kind: repo
---

Progressive Web Apps are presented as web apps that behave like native phone apps and can be installed on the home screen. The article says PWAs load faster because of service workers and are cheaper and quicker to develop than native or hybrid apps.

## Reading notes

- PWAs are described as regular web apps that can show an “Add to Home Screen” message and be installed on a phone.
- The article compares native, hybrid, and PWA apps, saying native apps are expensive because separate Android and iOS apps must be built.
- Hybrid apps are described as using one stack to create builds for Android and iOS, with access to device hardware through plugins.
- PWAs are described as cheaper to develop, quick to build, and able to work offline.
- A service worker is described as a background script separate from the website.
- The article says service workers can cache network requests, cache API calls, handle network requests, support background sync, receive push notifications, cache static assets, and make apps work offline.
- The service worker cannot directly access or interact with the DOM.
- The lifecycle starts with registering the service worker through `navigator.serviceWorker.register('/sw.js')`.
- The article suggests waiting for the window load event before registering, while noting that this can delay registration.
- During installation, the `install` event can use `event.waitUntil()` to keep the worker in the install phase until caching finishes.
- The example shows opening a cache with `caches.open(web_cache)` and adding files with `cache.addAll(filesToCache)`.
- In Chrome, the article says to check installation through DevTools under the Application tab and the service worker section.
- Activation can happen when there is no existing service worker, when `self.skipWaiting()` is called, when the user leaves the page, or after a set period of time.
- An active service worker can be checked on the registration object through `registration.active`.
- A service worker can become redundant if installation fails, activation fails, or a new worker replaces the existing active worker.
