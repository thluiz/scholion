---
title: "Release Workbox v5.0.0"
date: '2020-02-22T12:11:50+00:00'
category: webclip
summary: 'Workbox v5 shifts runtime bundling toward local builds, simplifies manifest injection, adds TypeScript support and new precaching and routing APIs, and renames several options with breaking changes.'
tags: ["workbox", "service-workers", "webpack", "typescript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Release Workbox v5.0.0 · GoogleChrome/workbox"
    url: "https://github.com/GoogleChrome/workbox/releases/tag/v5.0.0"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/github-com--release-workbox-v5-0-0.md"
    kind: repo
---

Workbox v5 centers on local bundles instead of relying on the CDN, simplifies precache injection, and adds TypeScript definitions for browser APIs. It also expands precaching controls, adds helpers for reading precached responses, and updates routing and broadcast behavior.

## Reading notes

- `generateSW` now creates a local bundle with only the runtime methods actually used in the service worker, optionally imported from a separate file or inlined.
- `InjectManifest` now runs the service worker source through webpack compilation, with optional webpack plugins applied through `webpackPlugins`.
- `workbox-webpack-plugin` no longer supports `glob` options for precache entries; webpack assets are now the source of generated manifest entries.
- `manifestTransforms` can now modify any part of the precache manifest, including adding, removing, or changing `revision` and `url` fields.
- The precache manifest is now inlined into the top-level service worker file instead of being stored in a separate external JavaScript file.
- `injectManifest` now replaces the `self.__WB_MANIFEST` placeholder instead of using a regular expression based replacement.
- Browser-facing Workbox packages are now written in TypeScript, and npm publishes type definitions for those APIs.
- Build tools now support `additionalManifestEntries` for adding precache entries such as versioned CDN URLs, with warnings for unversioned string entries.
- `GenerateSW` now supports `importScriptsViaChunks`, which includes named webpack chunks in the generated service worker.
- Precache entries can include optional `integrity` metadata for the `fetch()` request used to populate the cache.
- `workbox-window` adds `update()` to trigger a manual service worker update check.
- Navigation route options rename `blacklist` and `whitelist` to `denylist` and `allowlist`.
- `registerNavigationRoute()` is replaced by `createHandlerBoundToURL()` plus `NavigationRoute` and `registerRoute()` for the same app shell behavior.
- `workbox-broadcast-update` adds `generatePayload()` for customizing the message sent after a cached response changes.
- `copyResponse()` can clone a response while changing headers, status, or statusText.
- When precaching bypasses the HTTP cache, Workbox now uses `cache: 'reload'` on the request instead of adding `__WB_REVISION` to the outgoing network request.
- Development logging can now be disabled with the `__WB_DISABLE_DEV_LOGS` global.
- `matchPrecache()` and `createHandler()` make manual access to precached assets easier.
- `manifestTransforms` callbacks are now awaited, and `workbox-build` and `workbox-cli` can use `runtimeCaching` without precaching configuration.
- Breaking changes include removal of several old configuration options, renamed navigation options, package-specific plugin class names, `BroadcastChannel` removal in `workbox-broadcast-update`, removal of `generateSWString`, a higher Node minimum, `makeRequest()` removal in favor of `handle()`, and a webpack v4+ requirement for `workbox-webpack-plugin`.
