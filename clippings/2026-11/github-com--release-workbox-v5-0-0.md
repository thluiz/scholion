---
url: "https://github.com/GoogleChrome/workbox/releases/tag/v5.0.0"
captured_at: "2026-11-16T02:32:10+00:00"
title: "Release Workbox v5.0.0 · GoogleChrome/workbox"
domain: "github-com"
---

## Overview of Workbox v5

We're happy to announce the release of Workbox version 5! This release introduces a lot of new features, as well as some breaking changes.

If you're already using Workbox, the best place to get up to speed is the [guide to migrating from v4 to v5](https://developers.google.com/web/tools/workbox/guides/migrations/migrate-from-v4).

One example migration, with commentary, can be found in [this GitHub commit](https://github.com/GoogleChromeLabs/so-pwa/commit/b1ecae0bc12b923506b4199dcabf4f15ca2a924e).

## 🎉 What's New?

### A shift towards local Workbox bundles & away from the CDN

While our immediate plan is to continue publishing copies of the Workbox runtime code to our CDN, in v5, the `generateSW` mode of our build tools will create a local bundle of exactly the Workbox runtime methods you end up using in your service worker. Depending on the value of `inlineWorkboxRuntime`, this bundle will either be imported from a separate file, or inlined directly in your top-level service worker.

Under the hood, we use [Rollup](https://rollupjs.org/guide/en/) to create this optimized bundle, optionally minifying it and generating sourcemaps, depending on the configuration.

See [#2064](https://github.com/GoogleChrome/workbox/issues/2064) for more details.

If you're using the `workbox-webpack-plugin`'s `InjectManifest` mode, the service worker file you specify via `swSrc` will end up being run through a `webpack` compilation process, optionally applying any compilation plugins configured via the `webpackPlugins` parameter. This should simplify the development flow described in the [Using Bundlers (webpack/Rollup) with Workbox](https://developers.google.com/web/tools/workbox/guides/using-bundlers) guide.

See [#1513](https://github.com/GoogleChrome/workbox/issues/1513) for more details.

You can continue using `importScripts('http://storage.googleapis.com/workbox-cdn/releases/5.0.0/workbox-sw.js')` and relying on `[workbox-sw](https://developers.google.com/web/tools/workbox/modules/workbox-sw)` to dynamically pull in the Workbox runtime code that you need in v5, but we expect that using a custom bundle will lead to smaller runtime payloads (as well as work around issues with [asynchronous imports](https://developers.google.com/web/tools/workbox/modules/workbox-sw#avoid_async_imports)), and we encourage developers to consider switching off of the CDN.

### Changes to the webpack precache manifest

Before v5, `workbox-webpack-plugin` would generate a list of entries to precache based on two distinct sources: the set of assets in a `webpack` compilation, along with an optional additional set of files matched via `glob` patterns. Most `webpack` developers did not use the `glob`\-related options (since the `webpack` compilation would normally include all the assets that they cared about), but at the same time, some helpful configuration options for manipulating or post-processing the precache manifest only applied to entries created via those `glob` patterns.

In v5, the `glob`\-related configuration options are no longer supported. The `webpack` asset pipeline is the source of all the automatically created manifest entries. (Developers who have files that exist outside of the `webpack` asset pipeline are encouraged to use, e.g., `[copy-webpack-plugin](https://github.com/webpack-contrib/copy-webpack-plugin)` to get those files into the `webpack` compilation.)

Beyond that, options for post-processing the precache manifest can now be used to manipulate entries that originate from the `webpack` asset pipeline. `manifestTransforms`, in particular, can be used to make arbitrary changes to _any_ aspect of the precache manifest, including adding entries, deleting them, and changing their `revision` or `url` fields as needed. The current `webpack` compilation will be passed in to the callback function in case you need information from there to determine how to manipulate entries.

Here's an example of using `manifestTransforms` to perform extensive post-processing of a precache manifest:

const manifestTransform \= (originalManifest, compilation) \=> {
  // If anything needs to be propagated to webpack's list
  // of compilaiton warnings, add the message here:
  const warnings \= \[\];

  const manifest \= originalManifest.map((entry) \=> {
    // entry has size, revision, and url fields.

    // Add a CDN prefix to certain URLs.
    // (alternatively, use modifyURLPrefix)
    if (entry.url.endsWith('.jpg')) {
      entry.url \= \`https://examplecdn.com/${entry.url}\`;
    }

    // Remove revision when there's a match for your hashed URL pattern.
    // (alternatively, just set dontCacheBustURLsMatching)
    if (entry.url.match(/\\.\[0\-9a\-f\]{6}\\./)) {
      delete entry.revision;
    }

    // Exclude assets greater than 1MB, unless they're JPEGs.
    // (alternatively, use maximumFileSizeToCacheInBytes)
    if ((entry.size \> 1024 \* 1024) && !entry.url.endsWith('.jpg')) {
      warnings.push(\`${entry.url} will not be precached because it is too big.\`);
      return null;
    }

    return entry;
  }).filter(Boolean); // Exclude any null entries.

  // When manually adding in additional entries, make sure you use a URL
  // that already includes versioning info, like the v1.0.0 below:
  manifest.push({
    url: 'https://examplecdn.com/third-party-code/v1.0.0/index.js',
  });

  return {manifest, warnings};
};

Helpers that implement common manifest transformations, like `maximumFileSizeToCacheInBytes`, `dontCacheBustURLsMatching` and `modifyURLPrefix`, are also supported for `webpack` assets.

See [#1591](https://github.com/GoogleChrome/workbox/issues/1591) and [#1854](https://github.com/GoogleChrome/workbox/issues/1854).

Additionally, in v5, the precache manifest is inlined into the top-level service worker file, and not stored in a separate, external JavaScript file.

### Simplified injectManifest placeholder replacement

Prior to v5, manifest injection worked by using a regular expression to find the correct location in the source service worker file to replace with the array of manifest entries. This could be brittle, and it was hard to customize, since the replacement step assumed you were using a `RegExp` that had capture groups.

This is simplified in v5, and using the `injectManifest` mode just checks for a placeholder variable and performs the equivalent of string replacement to inject the full manifest in its place. This variable is `self.__WB_MANIFEST` by default.

Your `swSrc` file in v4 might have looked like `precacheAndRoute([]);`

In v5, you should change this to `precacheAndRoute(self.__WB_MANIFEST);`

`self.__WB_MANIFEST` was chosen as the default replacement because self should always be defined in the service worker global scope, and it is unlikely to conflict with any user-created variables. If you need a different replacement, it can be configured via the `injectionPoint` option.

See [#2059](https://github.com/GoogleChrome/workbox/issues/2059) for more details.

### TypeScript support

All browser-based Workbox packages are now written in TypeScript and type definitions have been published to npm. TypeScript users (as well as users with TypeScript-aware code editors) can now get type checking for all browser-exposed Workbox APIs. (There are no TypeScript definitions for the various Workbox build tools at this time.)

To get type definitions for any Workbox APIs, you can import the package as described in our guide on [Using Bundlers (webpack/Rollup) with Workbox](https://developers.google.com/web/tools/workbox/guides/using-bundlers). For example:

import {registerRoute} from 'workbox-routing';
import {CacheFirst} from 'workbox-strategies';
import {Plugin as ExpirationPlugin} from 'workbox-expiration';

registerRoute(
  /\\.(?:png|gif|jpg|jpeg|svg)$/,
  new CacheFirst({
    cacheName: 'images',
    plugins: \[
      new ExpirationPlugin({
        maxEntries: 60,
        maxAgeSeconds: 30 \* 24 \* 60 \* 60, // 30 Days
      }),
    \],
  }),
);

Note, we've historically published our Workbox source modules with the `.mjs` extension as a way [to disambiguate them from classic scripts](https://v8.dev/features/modules#mjs) and the examples in our documentation that reference file paths always use `.mjs`.

However, since TypeScript [does not currently support importing .mjs files](https://github.com/Microsoft/TypeScript/issues/27957) we publish both `.js` and `.mjs` files to npm. TypeScript users wanting to import an individual module should be able to reference it by omitting the extension (which will then default to the `.js` file).

import {registerRoute} from 'workbox-routing';
import {CacheFirst} from 'workbox-strategies';
import {Plugin as ExpirationPlugin} from 'workbox-expiration';

If you encounter any problems with the type definitions or importing the source files via TypeScript, please let us know by [opening an issue on GitHub](https://github.com/GoogleChrome/workbox/issues/new).

### additionalManifestEntries option in build tools

All of the build tools (`generateSW` and `injectManifest` modes in `workbox-build`, `workbox-cli`, and `workbox-webpack-plugin`) now support a new option: `additionalManifestEntries`. \[[#2124](https://github.com/GoogleChrome/workbox/pull/2124)\] It can be set to a list of additional precache manifest entries that go beyond what would normally be included as part of your build (such as CDN URLs), and is a shortcut to something that is otherwise possible via the `manifestTransforms` option.

Before using this feature, please keep in mind that `workbox-precaching` requires one of two things from each entry in order to keep precached content up to date:

*   The URL contains versioning information, and therefore the contents will never change. E.g. '[https://example.com/v1.0.0/index.js](https://example.com/v1.0.0/index.js)', or '[https://example.com/index.hashValue.js](https://example.com/index.hashValue.js)'
*   You include a `revision` field alongside an unversioned URL, providing versioning information that is updated each time new contents are deployed to that URL. E.g. `{url: https://example.com/index.js, revision: hashOfIndexJsContents}`

The precache manifest entries generated by Workbox's built tools can automatically add in `revision` fields for you, but when using `additionalManifestEntries`, it's up to you to ensure that you only add in versioned URLs, or that you include a `revision` field that will always change whenever the corresponding URL changes.

To ensure that developers are aware of this, passing in string values in the `additionalManifestEntries` will result in a non-fatal warning message, asking you to confirm that your URLs are versioned. To avoid this message, pass in an object with a `revision: null` property instead of a string, like `{url: http://example.com/v1.0.0/index.js, revision: null}`.

### importScriptsViaChunks in workbox-webpack-plugin's GenerateSW mode

A new option, `importScriptsViaChunks`, is supported in the `GenerateSW` mode of the webpack plugin. \[[#2131](https://github.com/GoogleChrome/workbox/pull/2131)\] Passing in one or more chunk names will cause the corresponding script files to be included in the generated service worker, via `[importScripts()](https://developer.mozilla.org/en-US/docs/Web/API/WorkerGlobalScope/importScripts)`.

Because of the way script caching works with `importScripts()`, developers should ensure that their chunks' filenames include a hash, so that changes to a chunk's contents will result in new filename.

### Support for subresource integrity metadata in precaching requests

Precache manifest entries can now include an optional property, `integrity`. If provided, that value will be treated as the [integrity metadata](https://fetch.spec.whatwg.org/#concept-request-integrity-metadata) for in the `fetch()` request used to populate the precache. \[[#2141](https://github.com/GoogleChrome/workbox/pull/2141)\]

There is currently no option in the Workbox build tools for generating this metadata; it's left as an exercise to developers to use the `manifestTransforms` option to post-process the generated precache manifests and add in `integrity` properties, with [appropriate values](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity#Using_Subresource_Integrity), to the entries that need that [extra validation](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity).

### update(), to force a service worker update check

A new `update()` method has been added to `workbox-window`. When called, it will invoke the `update()` method on the underlying `ServiceWorkerRegistration` object. \[[#2136](https://github.com/GoogleChrome/workbox/pull/2136)\]

Calling this method is optional, as browsers will automatically check for service worker updates whenever there's a navigation request to a new page, along with a few other scenarios. However, as described in [this guide](https://developers.google.com/web/fundamentals/primers/service-workers/lifecycle#manual_updates), manually requesting a service worker update can be useful for long-lived, single-page apps.

### Navigation route changes

Two options that were previously supported for navigation routes, `blacklist` and `whitelist` have been renamed `denylist` and `allowlist`.

`workbox-routing` previously supported a method, `registerNavigationRoute()`, that, under the hood, did two things:

1.  Detected whether or not a given `fetch` event had a `[mode of 'navigate'](https://fetch.spec.whatwg.org/#concept-request-mode)`.
2.  If so, responded to that request using the contents of a previously cached, hardcoded URL, regardless of the URL being navigated to.

This is a common pattern to use when implementing the [App Shell architecture](https://developers.google.com/web/fundamentals/architecture/app-shell).

The second step, generating a response by reading from the cache, falls outside of what we see as the responsibilities of `workbox-routing`. Instead, we see it as functionality that should be part of `workbox-precaching`, via a new method, `createHandlerBoundToURL()`. This new method can work hand-in-hand with the existing `NavigationRoute` class in `workbox-routing` to accomplish the same logic.

If you're using the `navigateFallback` option in one of the build tool's "generate SW" mode, then the switchover will happen automatically. If you previously configured either the `navigateFallbackBlacklist` or `navigateFallbackWhitelist` options, please change those to `navigateFallbackDenylist` or `navigateFallbackAllowlist`, respectively.

If you're using "inject manifest" mode or just writing the service worker yourself, and your Workbox v4 service worker calls `registerNavigationRoute()` directly, then you'll have to make a change to your code to get the equivalent behavior.

// v4:
import {getCacheKeyForURL} from 'workbox-precaching';
import {registerNavigationRoute} from 'workbox-routing';

const appShellCacheKey \= getCacheKeyForURL('/app-shell.html');
registerNavigationRoute(appShellCacheKey, {
  whitelist: \[...\],
  blacklist: \[...\],
});

// v5:
import {createHandlerBoundToURL} from 'workbox-precaching';
import {NavigationRoute, registerRoute} from 'workbox-routing';

const handler \= createHandlerBoundToURL('/app-shell.html');
const navigationRoute \= new NavigationRoute(handler, {
  allowlist: \[...\],
  denylist: \[...\],
});
registerRoute(navigationRoute);

You no longer need to call `getCacheKeyForURL()`, as `createHandlerBoundToURL()` will take care of that for you.

### workbox-broadcast-update

A `generatePayload()` configuration option has been added to the `BroadcastCacheUpdate` and `BroadcastUpdatePlugin` classes that allows developers to customize the message that gets sent to the window when a cached response has been updated.

The `generatePayload()` function is called with the same arguments as the `[cacheDidUpdate()](https://developers.google.com/web/tools/workbox/guides/using-plugins#custom_plugins)` plugin callback, and its return value will be used as the message payload. Here's an example that adds the `Last-Modified` header value of the updated response to the payload:

new BroadcastUpdatePlugin({
  generatePayload({request, newResponse}) {
    return {
      url: request.url,
      lastModified: newResponse.headers.get('Last-Modified'),
    };
  },
});

### New copyResponse method

A `copyResponse()` method has been added that can be used to clone a response and modify its `headers`, `status`, or `statusText`. \[[#2193](https://github.com/GoogleChrome/workbox/pull/2193)\]

Here's an example that adds a custom header to indicate that a response came from the cache (and not the network):

const newResponse \= copyResponse(oldResponse, (responseInit) \=> {
  responseInit.headers.set('X-Cache', 'hit');
  return responseInit;
});

### Changes to the precaching network requests

If `workbox-precaching` needs to bypass the HTTP cache when requesting a URL, it will now set `cache: 'reload'` on the outgoing `Request`, which in turns sets the appropriate `Cache-Control` headers. \[[#2176](https://github.com/GoogleChrome/workbox/pull/2176)\]

Previously, bypassing the HTTP cache was done by adding in a `__WB_REVISION=...` URL query parameter to the outgoing network request, meaning that backend web servers would see requests for URLs containing those query parameters. With this change in place, requests for URLs with `__WB_REVISION=...` should no longer be seen in HTTP server logs.

Please note that this change _only_ applies to outgoing HTTP requests used to populate the precache, and _does not apply to cache keys_. The keys for some entries created by `workbox-precaching` still include the `__WB_REVISION=...` parameter, and it's still a [best practice](https://developers.google.com/web/tools/workbox/modules/workbox-precaching#reading_precached_assets_directly) to call `getCacheKeyForURL()` to determine the actual cache key, including the `__WB_REVISION` parameter, if you need to access precached entries using the Cache Storage API directly.

### Control over development logging

A new `__WB_DISABLE_DEV_LOGS` global has been added. Set it to `false` to disable all logging in development mode. \[[#2284](https://github.com/GoogleChrome/workbox/pull/2284)\]

### New helper methods to read precached responses

Two new methods (`matchPrecache()` and `createHandler()`) have been added to make it easier to manually access precached assets. \[[#2254](https://github.com/GoogleChrome/workbox/pull/2254)\]

### All build tools

Any `manifestTransform` callbacks are now treated as being `[async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)`, and each callback will be `await`\-ed by the build tools. If you supply multiple transforms, they will still be run sequentially, in the same order. \[[#2195](https://github.com/GoogleChrome/workbox/pull/2195)\]

This should not be a breaking change, as you can continue providing non-`async` callback functions, and they will still work as before.

### workbox-build and workbox-cli

As part of a general refactoring of how the options passed to all of our build tools are parsed \[[#2191](https://github.com/GoogleChrome/workbox/pull/2191)\], using precaching in the `generateSW` mode of `workbox-build` and `workbox-cli` is no longer mandatory. You can now use the `runtimeCaching` options without configuring the `glob`\-related options, and your generated service worker will just contain the corresponding runtime caching routes.

If you don't configure the `glob`\-related options _and_ you don't use `runtimeCaching`, that will lead to a build error.

## ⚠️ Breaking Changes

### All Build Tools

*   A number of [`workbox-build`](https://developers.google.com/web/tools/workbox/reference-docs/latest/module-workbox-build), [`workbox-cli`](https://developers.google.com/web/tools/workbox/modules/workbox-cli), and [`workbox-webpack-plugin`](https://developers.google.com/web/tools/workbox/reference-docs/latest/module-workbox-webpack-plugin) configuration parameters are no longer supported, following the general outlines of the changes described above. For instance, `generateSW` will always create a local Workbox runtime bundle for you, so the `importWorkboxFrom` option no longer makes sense. Please consult the relevant tool's documentation for the list of supported options.
    
*   `navigationRouteWhitelist` has been renamed `navigationRouteAllowlist`, and `navigationRouteBlacklist` has been renamed `navigationRouteDenylist`. The functionality is otherwise identical.
    

### All Plugin classes

All `Plugin` classes have been renamed to be package-specific, e.g. `ExpirationPlugin`, `CacheableResponsePlugin`, etc. If you're using one of the Workbox build tools in `generateSW` mode to create your service worker, this change will be handled for you automatically. If you use one of the plugins in a manually created service worker, you'll need to explicitly change instances of `Plugin` to the correct revised class name. \[[#2187](https://github.com/GoogleChrome/workbox/pull/2187)\]

### workbox-broadcast-update

The `workbox-broadcast-update` package no longer uses `BroadcastChannel`, even in cases when the browser supports it. Instead it uses `postMessage()` to message window clients. \[[#2184](https://github.com/GoogleChrome/workbox/issues/2184)\]

This change was made because `postMessage()` messages are [automatically buffered](https://www.chromestatus.com/feature/5751307839209472) by the window to handle cases where the service worker sends a message before the code running on the window is ready to receive it. `BroadcastChannel` has no such buffering, and thus you're more likely to miss message when using it.

If you're currently listening for `BroadcastChannel` messages in your code running on the window, you'll now need to listen for `message` events on the `[ServiceWorkerContainer](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerContainer)`:

navigator.serviceWorker.addEventListener('message', (event) \=> {
  console.log(event.data);
})

Note: `workbox-window` users should not need to make any changes, as its internal logic has been updated to listen for `postMessage()` calls.

### workbox-build

*   The `generateSWString` mode has been removed. We expect the impact of this to be minimal, as it was primarily used internally by `workbox-webpack-plugin`.
    
*   The minimum required version of node has been increased to `v8.0.0`. This also applies to build tools that use `workbox-build`, like `workbox-cli` and `workbox-webpack-plugin`.
    

### workbox-routing

*   See the earlier "Navigation route changes" section.

### workbox-strategies

*   Removal of `makeRequest()` in favor of `handle()`. Calling `makeRequest()` is mostly equivalent to calling `handle()` on one of the `workbox-strategy` classes. The differences between the two methods were so slight that keeping both around did not make sense. Developers who called `makeRequest()` should be able to switch to using `handle()` without any further change. \[[#2123](https://github.com/GoogleChrome/workbox/pull/2123)\]

### workbox-webpack-plugin

*   This plugin requires now requires `webpack` v4 or higher.

## 🐛 What's Fixed?

### All build tools

*   If the `swSrc` file has an associated sourcemap, we now update that to account for the injected manifest. \[[#2239](https://github.com/GoogleChrome/workbox/pull/2239)\]

### workbox-broadcast-update

*   Added a check to wait for the resulting client to load on navigation requests before broadcasting any update messages. \[[#2210](https://github.com/GoogleChrome/workbox/pull/2210)\]

### workbox-precaching

*   Fixed a bug where the result of the `cacheWillUpdate()` plugin callback was not being `await`\-ed. \[[#2287](https://github.com/GoogleChrome/workbox/pull/2287)\]

### workbox-routing

*   Pass `matchCallback` string/number return values through to `handlerCallback`. \[[#2134](https://github.com/GoogleChrome/workbox/pull/2134)\]
*   Fixed a `ReadableStream` bug in development mode in Safari. \[[#2268](https://github.com/GoogleChrome/workbox/pull/2268)\]

### workbox-webpack-plugin

*   When using multiple instances of `workbox-webpack-plugin` in the same compilation, assets created by those other instances will now be excluded from each others' precache manifest. \[[#2182](https://github.com/GoogleChrome/workbox/pull/2182)\]

### workbox-window

*   Added the `isUpdate` property to the `controlling` event, which was documented but not actually implemented. \[[#2114](https://github.com/GoogleChrome/workbox/pull/2114)\]
*   The `message` event listener is now added earlier, inside of the constructor rather than the `register()` method. \[[#2211](https://github.com/GoogleChrome/workbox/pull/2211)\]

## 🙏 Thanks!

A sincere thank you to everyone who tested Workbox v5, and in particular to the following folks who filed bugs and made contributions to the code. (Apologies if we've missed anyone—it's been a long process!)

### Code Contributions

*   [@azizhk](https://github.com/azizhk)
*   [@jaulz](https://github.com/jaulz)

### Bug Reports

*   [@derekdowling](https://github.com/derekdowling)
*   [@emillundstrm](https://github.com/emillundstrm)
*   [@lukas2005](https://github.com/lukas2005)
*   [@kaykayehnn](https://github.com/kaykayehnn)
