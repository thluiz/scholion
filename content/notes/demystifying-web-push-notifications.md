---
title: "Demystifying Web Push Notifications"
date: '2023-12-12T18:51:31+00:00'
category: webclip
summary: 'The post breaks web push into subscription, delivery, and service worker handling, then shows how VAPID keys, backend storage, and client-side registration fit together.'
tags: ["web-push", "service-worker", "vapid-keys", "push-notifications"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Demystifying Web Push Notifications"
    url: "https://pqvst.com/2023/11/21/web-push-notifications"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/pqvst-com--demystifying-web-push-notifications.md"
    kind: repo
---

The post explains web push as a browser-vendor push service that sits between the app and the browser. The client creates a subscription and sends it to the backend, the backend sends a push message to the vendor service, and the browser handles the notification in a service worker. It also points to a minimal Node.js example on GitHub.

It then covers the pieces needed to make this work in practice. VAPID keys are required on the main browsers, especially Chrome and Safari, and the post recommends generating them with a tool. On the server, the `web-push` library handles encoding and encryption, while subscriptions must be stored so they survive server restarts. On the client, the app requests notification permission, registers the service worker, subscribes through `pushManager`, and posts the subscription to the backend. The post also notes that `event.waitUntil` keeps the service worker alive while handling pushes, that service workers do not auto-reload during local development, and that clickable notifications need explicit `notificationclick` handling in the service worker.

## Reading notes

- Web push uses a browser vendor push service between the app and the browser.
- The flow has three steps: create a subscription, send a notification, and handle it in a service worker.
- A subscription includes a browser-specific endpoint and encryption keys.
- Safari uses an Apple endpoint, Chrome uses a Google endpoint, and Firefox uses a Mozilla endpoint.
- VAPID keys are required for web push to work on the main browsers.
- Chrome and Safari require an `applicationServerKey` when subscribing.
- The post recommends generating VAPID keys with a tool instead of doing it manually.
- On the server, the `web-push` library handles crafting web push messages in Node.js.
- The backend must store subscriptions, or they are lost when the server restarts.
- Broadcast notifications can be sent by looping through saved subscriptions and calling `sendNotification`.
- Invalid subscriptions can be removed after errors, such as revoked permissions or expired subscriptions.
- The service worker listens for `push` events and calls `showNotification` with the received payload.
- `event.waitUntil` is used so the browser keeps the service worker alive until the work finishes.
- The client requests notification permission before trying to enable push notifications.
- The client registers the service worker, checks for an existing subscription, or creates a new one with `pushManager.subscribe`.
- The subscription is sent to the backend after it is found or created.
- The service worker does not reload automatically when the page reloads during local development.
- Clickable notifications need a `notificationclick` handler that closes the notification and focuses or opens the target tab.
