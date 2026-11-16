---
title: "GitHub - web-push-libs/web-push: Web Push library for Node.js"
date: '2026-11-16T03:53:01+00:00'
category: webclip
summary: 'This library sends Web Push messages from a backend, handles payload encryption, supports legacy GCM delivery, and exposes CLI and API helpers for VAPID and request details.'
tags: ["web-push", "nodejs", "vapid", "push-notifications"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "GitHub - web-push-libs/web-push: Web Push library for Node.js"
    url: "https://github.com/web-push-libs/web-push"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/github-com--web-push-lib-for-nodejs.md"
    kind: repo
---

This repository presents a Node.js library for sending Web Push messages from a backend. It says that push delivery must use the Web Push Protocol, and that payload data must be encrypted according to the Web Push encryption spec. It also says the module handles legacy browsers relying on GCM.

## Reading notes

- Install with npm using `npm install web-push --save`, or globally with `npm install web-push -g` for the command line tools.
- The common setup uses a GCM API key and VAPID keys, and VAPID keys should be generated only once.
- `sendNotification(pushSubscription, payload, options)` sends a push notification and can encrypt the payload automatically.
- `sendNotification()` can work without a payload, and without GCM or VAPID keys if the push service supports that.
- `generateVAPIDKeys()` returns URL-safe Base64 public and private keys, and the note says to store and reuse them.
- `setGCMAPIKey(apiKey)` sets the GCM API key used for future requests.
- `setVapidDetails(subject, publicKey, privateKey)` sets the app’s VAPID subject and keys for later calls.
- `encrypt(userPublicKey, userAuth, payload, contentEncoding)` encrypts the payload and returns the local public key, salt, and ciphertext.
- `getVapidHeaders(audience, subject, publicKey, privateKey, contentEncoding, expiration)` creates the headers needed for authorization and crypto key values.
- `generateRequestDetails(pushSubscription, payload, options)` builds the endpoint, method, headers, and body for a request.
- The browser support table lists Chrome, Edge, Firefox, Opera, Safari, and Samsung Internet Browser, with different support for push without payload, with payload, and VAPID.
- The help section points to MDN and the Service Worker Cookbook for examples.
- Tests run with `npm test`, and the prerequisites mention Java JDK or JRE.
