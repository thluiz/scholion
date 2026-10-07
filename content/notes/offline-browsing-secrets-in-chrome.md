---
title: "Offline Browsing Secrets In Chrome"
date: '2015-01-28T09:58:29-03:00'
category: webclip
summary: 'The post explains Chrome’s Offline Cache Mode, how it shows cached pages when a request fails offline, how to enable it, and its limits around POST, AppCache, and static resources.'
tags: ["chrome", "offline-cache", "browser-features"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Offline Browsing Secrets In Chrome"
    url: "http://addyosmani.com/blog/offline-mode-chrome/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-01/addyosmani-com--offline-browsing-secrets-in-chrome.md"
    kind: repo
---

Chrome already has an offline mode through Offline Cache Mode. When a page was previously cached and the browser cannot reach the network, Chrome can show the stored copy instead of a failure page. The post also notes related flags in Chrome 37, including auto-reloading offline pages once the browser is back online.

## Reading notes

- Chrome’s Offline Cache Mode was implemented behind flags and can show stale cached content when an offline request fails.
- The feature works on desktop and Chrome for Android.
- To enable it in Chrome 35, open about:flags, enable Offline Cache Mode, relaunch Chrome, disconnect from the web, and load a page you visited before.
- In Chrome stable 35, there is no warning that a cached version exists before the page is shown.
- POST requests are not handled or queued.
- The feature does not work well with AppCache.
- It is most useful for offline viewing of static resources such as HTML, CSS, JavaScript, and images.
- In Chrome 37, the browser is being tested with offline mode enabled by default and a “Show saved copy” button for pages found in the stale cache.
- Another experimental flag, Offline Auto-Reload Mode, tracks pages that failed offline and reloads them when the browser comes back online.
- A second flag, Only Auto-Reload Visible Tabs, limits that behavior to visible tabs.
