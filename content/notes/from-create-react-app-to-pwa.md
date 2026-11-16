---
title: "From create-react-app to PWA"
date: '2020-02-22T12:11:50+00:00'
category: webclip
summary: 'The post shows how to turn a Create React App project into a PWA by enabling the service worker, editing the manifest, adding routing, splitting code with React.lazy, and deploying on Netlify.'
tags: ["pwa", "create-react-app", "react", "netlify"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "From create-react-app to PWA"
    url: "https://blog.johnnyreilly.com/2020/01/from-create-react-app-to-pwa.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-johnnyreilly-com--from-create-react-app-to-pwa.md"
    kind: repo
---

The post argues that PWAs offer a single web-based app experience across devices, with offline use, home screen access, splash screens, and notifications. It also says they can reduce the cost and complexity of building separate web, Android, and iOS apps, even though PWAs are more complicated than normal web apps.

## Reading notes

- Create React App already includes support for PWAs, so a TypeScript React app can be created with `npx create-react-app pwa-react-typescript --template typescript`.
- Turning the app into a PWA means changing `serviceWorker.unregister()` to `serviceWorker.register()` in `index.tsx`.
- The service worker caches static assets, supports offline use, and uses a cache-first strategy for local assets and navigation requests.
- `create-react-app` uses Workbox to handle caching and offline behavior with default strategies.
- The post notes that this setup gives little room for custom configuration if the defaults are not enough.
- A PWA also needs installability, an app name, an icon, and a splash screen, all of which are already included in the default setup.
- The app name is changed in `index.html` and `manifest.json`, and the manifest defines metadata such as icons, `start_url`, `display`, `theme_color`, and `background_color`.
- Custom icons can be added by placing files in `public`, updating `manifest.json`, and changing the Apple touch icon link in `index.html` for older Apple devices.
- The app is then split into pages with `react-router-dom`, adding `Home` and `About` components and updating the test to look for the About link.
- Code splitting is added with `React.lazy` and `Suspense`, so routes load only when needed.
- After code splitting, the build produces multiple chunk files instead of one growing main bundle.
- The final step is deploying the app on Netlify from GitHub, using the default deploy settings and HTTPS so the service worker can run.
- The author then checks the deployed app with Google Chrome Developer Tools audit, which gives a good result.
