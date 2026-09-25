---
title: "Delivering Angular apps in online vs. offline modes"
date: "2026-09-23T19:11:29+01:00"
category: webclip
has_commentary: false
summary: "A tutorial on making an Angular app work offline through service workers and caching, plus two ways to detect connectivity changes and notify the user."
tags:
  - angular
  - pwa
  - offline-first
sources:
  - title: "Delivering Angular apps in online vs. offline modes - LogRocket Blog"
    url: "https://blog.logrocket.com/delivering-angular-apps-online-vs-offline-modes/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-logrocket-com--delivering-angular-apps-online-vs-offline-modes.md"
    kind: repo
---

The tutorial builds an Angular PWA that keeps working when a user loses connectivity, using Angular's built-in service worker rather than a custom caching layer. Running `ng add @angular/pwa` wires up the service worker package, a root provider, a `ngsw-config.json` file, a web manifest, and the icon set a PWA needs, all in one command.

Caching behavior lives entirely in `ngsw-config.json`. `assetGroups` covers static files like HTML, CSS, and JS; `dataGroups` covers API calls, each with its own strategy, max age, and timeout. The worked example adds a `dataGroups` entry for the JSONPlaceholder posts endpoint with both a "performance" and a "freshness" cache strategy, then confirms the behavior directly: load the app once online so the service worker populates the cache, then go offline and refresh, and the same data loads from cache instead of failing.

## Reading notes

- The browser's own `navigator.onLine` property, wrapped in a small Angular service with `online`/`offline` event listeners, is enough to build a reactive online-status stream that a component subscribes to and surfaces through a snack bar notification.
- `navigator.onLine` only reflects network interface state, not real internet access. `ng-connection-service` addresses that gap by periodically sending an HTTP request to a heartbeat URL, so it can tell network connectivity and actual internet access apart.
- `ConnectionState` from `ng-connection-service` exposes two separate booleans: `hasNetworkConnection` (based on browser online/offline events) and `hasInternetAccess` (based on the heartbeat check), letting an app distinguish "no network" from "network up, server unreachable."
- The full setup, service worker config plus either detection method, is tested by building with `ng build` and serving through `http-server`, then toggling the browser's offline mode in devtools.
