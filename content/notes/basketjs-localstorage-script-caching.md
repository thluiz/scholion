---
title: "Basket.js: A JavaScript Loader With LocalStorage-based Script Caching"
date: '2013-01-18T20:14:58-03:00'
category: webclip
summary: 'Basket.js loads scripts with a small stub, caches them in localStorage, and reloads them through XHR when needed. The post says this can be faster than the browser cache and suggests future experiments with FileSystem API, IndexedDB, and App Cache.'
tags: ["javascript", "localstorage", "script-caching", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Basket.js: A JavaScript Loader With LocalStorage-based Script Caching"
    url: "http://badassjs.com/post/40850339601"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/badassjs-com--basketjs-localstorage-script-caching.md"
    kind: repo
---

Basket.js loads a small stub first, then checks whether other scripts are already cached in localStorage. If they are missing or expired, it fetches them with XHR and stores them for later loads.

## Reading notes

- Basket.js caches JavaScript files in localStorage instead of depending on the browser cache.
- The post says this approach is faster, citing tests from Google and Bing.
- It uses a Promise-based API built on RSVP.js to require scripts and inject them into the page.
- The author suggests trying a FileSystem API version to compare performance with localStorage.
- The post says IndexedDB was tried already and was slower than localStorage.
- It also suggests combining the idea with App Cache so an app can work offline with a small HTML stub that loads everything else from storage.
