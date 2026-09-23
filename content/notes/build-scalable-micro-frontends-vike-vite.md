---
title: "How to build scalable micro-frontends with Vike and Vite"
date: "2026-09-23T19:09:39+01:00"
category: webclip
has_commentary: false
summary: "A tutorial pairing Vike's server-side rendering with vite-plugin-federation to share a component across independent Vue and React apps at runtime."
tags:
  - vite
  - micro-frontends
  - javascript
sources:
  - title: "How to build scalable micro-frontends with Vike and Vite - LogRocket Blog"
    url: "https://blog.logrocket.com/build-scalable-micro-frontends-vike-vite/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-logrocket-com--build-scalable-micro-frontends-vike-vite.md"
    kind: repo
---

The tutorial walks through combining Vike, the SSR/SSG framework formerly known as vite-plugin-ssr, with vite-plugin-federation to build micro-frontends. Vike alone renders pages on the fly or pre-builds them at build time; it doesn't share components across independently deployed apps by itself, so the federation plugin does that part by exposing a module from one Vite app and consuming it from another at runtime.

The worked example builds two projects: a standalone Vite + Vue app that exposes a Card component through `remoteEntry.js`, and a Vike-react app that imports that same component as `remoteApp/Card`. Each app keeps its own framework, build process, and deploy path; only the exposed module crosses the boundary.

## Fichamento

- Vike is pitched on being zero-config by default while still giving control where it matters, and on working across React, Vue, Svelte, or other frameworks rather than locking a project into one.
- Bati, Vike's scaffolding tool, lets a new project pick CSS library, auth method, database, and data-fetching library at creation time, as an alternative to Vike's own bare-bones starter.
- The remote app has to be started on a fixed port (`--port 5001 --strictPort`) rather than Vite's default, because the host app needs a stable URL to find `remoteEntry.js`.
- Federation config on both sides has to disable `modulePreload` and target `esnext`, since module federation needs to control module loading itself and depends on modern JS features.
- The post flags Nx or Turborepo as an option for consolidating multiple micro-frontends into one repository, to simplify dependency management, while noting that fit depends on the project.
