---
url: "https://medium.com/better-programming/use-localstorage-to-store-data-on-the-browser-d10f8363dda5"
captured_at: "2026-11-16T05:48:29+00:00"
title: "How To Use LocalStorage to Store Data in the Browser | by John Au-Yeung | Better Programming"
domain: "medium-com"
---

Member-only story

JavaScript
Programming
Software Development
React
Nodejs
How To Use LocalStorage to Store Data in the Browser
Storing data in the browser gets easier
John Au-Yeung
5 min read
·
Jan 14, 2020

Photo by chuttersnap on Unsplash

Storing data in a browser is something we do often for web apps. Often, we need to store some temporary data that’s user-specific on the browser. We can do this with the browser’s local-storage capabilities.

With local storage, we store data on the browser as strings. It’s a key value–based storage medium, allowing us to get data by keys and also setting values with the key as the identifier. All data is stored as strings. If a piece of data is not a string, then it’ll be converted to a string before being stored.

Once they’re saved, they’re there as long as we don’t delete the data. We can remove data by its key or remove them all at the same time. Every app that’s hosted on the same domain can access the data, so we can host multiple web apps under the same domain and still get the same data in all the apps.

This means we can easily modularize apps into smaller apps, and we won’t have a problem with browser data access as long as all the apps are hosted in the same domain.

Unlike cookies, local-storage data has no expiration time, so it’ll still be there if we don’t do anything to delete it.
