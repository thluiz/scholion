---
title: "Building a Progressive Web App and Deploying it"
date: '2026-11-16T01:29:25+00:00'
category: webclip
summary: 'The article explains what a progressive web app is, how to add a service worker, cache pages for offline access, create a manifest, check the app with Lighthouse, deploy it on Netlify, and submit it to the PWA Store.'
tags: ["progressive-web-apps", "service-worker", "lighthouse", "netlify"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a Progressive Web App and Deploying it"
    url: "https://dev.to/kgprajwal/building-a-progressive-web-app-and-deploying-it-10p7"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--building-a-progressive-web-app-and-deploying-it.md"
    kind: repo
---

The article says a progressive web app combines web capabilities with an app-like experience and highlights advantages such as speed, offline access, and lower data usage. It then walks through adding a service worker, caching pages, creating an offline page, and adding a manifest.

It also covers testing with Lighthouse, deploying the app by building it and uploading the build folder to Netlify, and then checking the published app for installability and offline behavior. The last step is submitting the app to the PWA Store after passing the Lighthouse checks.

## Reading notes

- PWA is presented as a way to combine web and native features in one application.
- The listed advantages are speed, easier access, offline access, better OS integration, and less data usage.
- The service worker is registered from index.html and runs in the background.
- The service worker code caches index.html and offline.html.
- The install event stores the URLs in Cache Storage.
- The fetch event returns the network response when possible and falls back to offline.html.
- The activate event removes old cache entries.
- The article suggests testing with npm start, Chrome DevTools, Update on reload, and Clear site data.
- The offline page is a simple HTML page with minimal styling and an offline message.
- The manifest.json includes name, short_name, icon, start_url, display, theme_color, and background_color.
- Lighthouse is used to assess the quality of the web application.
- The deployment step uses npm run build and Netlify drag-and-drop deployment.
- After deployment, the app can be checked for offline behavior and installability.
- The app is then submitted to the PWA Store after passing the Lighthouse PWA check.
