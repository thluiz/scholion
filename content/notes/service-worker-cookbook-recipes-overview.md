---
title: "ServiceWorker Cookbook"
date: '2019-07-06T21:24:22+00:00'
category: webclip
summary: 'Overview page listing practical service worker "recipes" for caching, offline behavior, push notifications, messaging, and other advanced browser capabilities.'
tags: ["service-worker", "offline", "push-notifications"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "ServiceWorker Cookbook"
    url: "https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--service-worker-cookbook-recipes-overview.md"
    kind: repo
---

The Service Worker Cookbook is introduced as a set of working, practical examples that show how to use service workers in modern web sites. Developers are encouraged to open the browser console to see `fetch` events and messages explaining what each recipe’s service worker is doing. The project was created by Mozilla, with contributions from the wider developer community, and its source code is available on GitHub.

The page catalogs many recipes, including multiple caching and offline strategies, different Web Push notification use cases, communication patterns between pages and service workers, and examples where the service worker acts as a proxy, virtual server, analytics logger, or dependency injector.

## Reading notes

- The cookbook is described as a collection of practical, working service worker examples aimed at modern web sites.
- Developers are advised to use Developer Tools to observe `fetch` events and see what each recipe’s service worker does.
- Mozilla is credited as the creator, with additional contributors listed via GitHub.
- All source code for the recipes is hosted on GitHub, and contributions and requests are explicitly welcomed.
- Image attributions for the Caching strategies category are credited to lorempixel.com.
- "Network or cache" shows a service worker that prefers fresh network content but falls back to cached content if the network is slow.
- "Cache only" provides a service worker that always serves responses from cache on `fetch` events.
- "Cache and update" serves cached responses quickly while also updating the cached entry from the network.
- "Cache, update and refresh" extends cache-and-update by automatically updating the UI when the network response completes.
- "Embedded fallback" serves built-in fallback content when requested resources are missing.
- "Push and Retrieve Payload" demonstrates sending push notifications and then retrieving a payload after a notification arrives.
- "Push Payload" shows sending push notifications that already contain a payload, using a string example and mentioning other possible data formats.
- "Push Rich" covers rich notifications, including language, vibration pattern, and associated image, and points to the Notifications API spec for more parameters.
- "Push Simple" is described as the simplest Web Push API example, sending notifications even when the page is closed.
- "Push Tag" uses a notification tag so newer notifications replace older ones, keeping only current or collapsed notifications.
- "Push Quota" is for experimenting with browser quota policies by sending many notifications and comparing behavior based on tab state and user interaction.
- "Push Clients" shows how to control service worker clients when a push-generated notification is clicked, including focusing or reopening the app tab.
- "Push Subscription" demonstrates push notifications with subscription management.
- "Immediate Claim" shows how a service worker can immediately take control of the page without waiting for a navigation.
- "Message Relay" illustrates communication between a service worker and a page, and relaying messages between multiple pages.
- "Fetching Remote Resources" presents two standard methods for loading remote resources and an approach using a service worker as proxy middleware.
- "Live Flowchart" is listed as a recipe without additional description in this text.
- "Offline Fallback" shows serving cached content when the user is offline.
- "Offline Status" caches critical resources for offline use and informs users that they can go offline while keeping the same experience.
- "JSON Cache" fetches a JSON file during service worker installation and caches all listed resources, also using immediate claim for faster activation.
- "Local Download" lets users "download" a file that was generated on the client side.
- "Virtual Server" demonstrates a service worker behaving like a remote server.
- "API Analytics" gathers API usage data in the service worker and uploads it periodically via the sync API, separate from the UI layer.
- "Load balancer" includes network logic in the service worker to select the best content provider based on server availability.
- "Cache from ZIP" shows how to cache content extracted from a zip file.
- "Dependency Injection" presents a service worker acting as a dependency injector to avoid hard-wiring dependencies in high-level components.
- "Request Deferrer" enqueues requests while offline in an outbox-like buffer and performs them once the connection returns.
- "Cache then Network" covers methods for returning network requests from either cache or network.
- "Render Store" demonstrates a cache of interpolated templates, following an NGA recommendation, to avoid repeated model fetching and rendering on later requests.
