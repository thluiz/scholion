---
title: "How To Make Your PWA Offline On Demand"
date: '2020-07-05T14:10:45+00:00'
category: webclip
summary: 'The article describes an on-demand offline approach for a PWA: lazy-load all content, save it in IndexedDB, cache app assets with a service worker, and switch services between online and offline modes.'
tags: ["pwa", "offline-mode", "indexeddb", "service-worker"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How To Make Your PWA Offline On Demand"
    url: "https://web.archive.org/web/20200527171555id_/https://dev.to/daviddalbusco/how-to-make-your-pwa-offline-on-demand-5dee"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--how-to-make-your-pwa-offline-on-demand.md"
    kind: repo
---

The article explains how the author’s PWA was made available offline on demand, using a Spotify- or Netflix-like model where users download content only when they ask for it. The implementation keeps the app editable offline and lets local changes be uploaded again when the user returns online.

## Reading notes

- The chosen approach makes the application’s content available offline only when requested, instead of keeping the whole app offline all the time.
- The offline flow starts by lazy-loading all slide content and assets before anything is cached or stored locally.
- Workbox is used in the service worker to cache images with separate strategies for regular and third-party sources.
- Deck data is saved locally in IndexedDB with the deck identifier as the storage key.
- A global offline state lets the app use an offline service or an online service without changing the higher layers of the application.
- When online, the app reads from Firestore; when offline, it reads from IndexedDB.
- App assets such as icons and fonts are listed in a JSON file and cached by calling the Service Worker from the app context.
- After caching is complete, the app switches to offline mode.
- The same architecture allows local content to remain editable while offline.
- When the user goes back online, the app uploads local content from IndexedDB and transfers local assets to remote storage.
