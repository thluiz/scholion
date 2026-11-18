---
url: "https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/"
captured_at: "2026-11-18T12:01:30+00:00"
title: "ServiceWorker Cookbook"
domain: "web-archive-org"
---

## Introduction

The Service Worker Cookbook is a collection of working, practical examples of using service workers in modern web sites.

**Tip:** Open your Developer Tools console to view `fetch` events and informative messages about what each recipe's service worker is doing!

## Attribution

The Service Worker Cookbook was created by [Mozilla](https://mozilla.com/) with [contributions](https://github.com/mozilla/serviceworker-cookbook/graphs/contributors) from developers like you. All source code is [available on GitHub](https://github.com/mozilla/serviceworker-cookbook). Contributions and requests welcome.

Attribution of pictures in Caching strategies category can be found at [lorempixel.com](http://lorempixel.com/).

## Recipes

### [Network or cache](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/strategy-network-or-cache.html)

The service worker in this recipe tries to retrieve the most up to date content from the network but if the network is taking too much, it will serve cached content instead.

### [Cache only](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/strategy-cache-only.html)

The recipe provides a service worker always answering from cache on `fetch` events.

### [Cache and update](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/strategy-cache-and-update.html)

The recipe provides a service worker responding from cache to deliver fast responses and also updating the cache entry from the network.

### [Cache, update and refresh](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/strategy-cache-update-and-refresh.html)

The recipe provides a service worker responding from cache to deliver fast responses and also updating the cache entry from the network. When the network response is ready, the UI updates automatically.

### [Embedded fallback](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/strategy-embedded-fallback.html)

The recipe provides a service worker serving an embedded content fallback in case of missing resources.

### [Push and Retrieve Payload](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/push-get-payload.html)

Send push notifications and retrieve a payload once a notification is received.

### [Push Payload](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/push-payload.html)

Send push notifications with a payload. This recipe shows how to send and receive a string, but data can be extracted from a Push message in a variety of formats (string, ArrayBuffer, Blob, JSON).

### [Push Rich](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/push-rich.html)

Show rich push notifications, defining the language of the notification, a vibration pattern, an image to associate to the notification. See [https://notifications.spec.whatwg.org/#api](https://notifications.spec.whatwg.org/#api) for the other parameters you can set (e.g. a set of actions that can be activated from the notification).

### [Push Simple](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/push-simple.html)

Simplest example of Web Push API usage. Send notifications to users even when your page is not open.

### [Push Tag](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/push-replace.html)

Use the notification tag to replace old notifications with new ones. Allows you to show only up-to-date information to your users or collapse multiple notifications into a single one.

### [Push Quota](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/push-quota.html)

Experiment with the quota management policies of different browsers. Try sending many notifications (visible or invisible) and see what happens if you keep the tab open vs close it, or if you click on some notifications vs you click on none of them.

### [Push Clients](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/push-clients.html)

Control the clients of a service worker when the user clicks on a notification generated from a push event. Allows you to focus the tab of your app or even re-open it if it was closed.

### [Push Subscription](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/push-subscription-management.html)

This recipe shows how to use push notifications with subscription management.

### [Immediate Claim](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/immediate-claim.html)

This recipe shows how to have the service worker immediately take control of the page without waiting for a navigation event.

### [Message Relay](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/message-relay.html)

This recipe shows how to communicate between the service worker and a page and shows how to use a service worker to relay messages between pages.

### [Fetching Remote Resources](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/fetching.html)

This recipe shows 2 standard ways of loading a remote resource and one way to use service worker as a proxy middleware.

### [Live Flowchart](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/live-flowchart.html)

### [Offline Fallback](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/offline-fallback.html)

This recipe shows how to serve content from the cache when the user is offline.

### [Offline Status](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/offline-status.html)

This basic recipe illustrates caching critical resources for offline use and then notifying the user that they may go offline and enjoy the same experience.

### [JSON Cache](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/json-cache.html)

This recipe illustrates fetching a JSON file during service worker installation and adding all resources to cache. This recipe also immediately claims the service worker for faster activation.

### [Local Download](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/local-download.html)

Allow a user to "download" a file that's been generated on the client side.

### [Virtual Server](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/virtual-server.html)

This recipe shows a service worker acting like a remote server.

### [API Analytics](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/api-analytics.html)

Perform API usage logging without interfering with the UI layer by adding a service worker to gather the usage and use the sync API to upload gathered data from time to time.

### [Load balancer](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/load-balancer.html)

This recipe shows a Service Worker containing network logic to dynamically select the best content provider accordingly to server availability.

### [Cache from ZIP](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/cache-from-zip.html)

This recipe illustrates how to cache contents from a zipfile.

### [Dependency Injection](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/dependency-injector.html)

This recipe shows how a Service Worker can act as a dependency injector, avoiding _hard wiring_ dependencies for high level components.

### [Request Deferrer](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/request-deferrer.html)

This recipe shows how to enqueue requests while in offline in an _outbox-like_ buffer to perform the operations once the connection is regained.

### [Cache then Network](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/cache-then-network.html)

This recipe illustrates methods to return network requests from either the cache or network.

### [Render Store](https://web.archive.org/web/20190716183620id_/https://serviceworke.rs/render-store.html)

The recipe demonstrates one recommendation from the [NGA](https://wiki.mozilla.org/Gaia/Architecture_Proposal#Render_store). A cache containing the interpolated templates in order to avoid model fetching and render times upon successive requests.
