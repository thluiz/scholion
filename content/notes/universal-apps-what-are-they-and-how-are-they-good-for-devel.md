---
title: "Universal Apps: What are they and how are they good for developers?"
date: '2014-06-30T10:04:50-03:00'
category: webclip
summary: 'The article explains Windows 8.1 and Windows Phone 8.1 Universal apps as a shared-code approach for two Microsoft platforms, while still encouraging platform-specific UI. It also lists benefits such as shared state, shared entitlement, and shared in-app purchases.'
tags: ["universal-apps", "windows-8-1", "windows-phone-8-1", "shared-code"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Universal Apps: What are they and how are they good for developers? - Neowin"
    url: "http://www.neowin.net/news/universal-apps-what-are-they-and-how-are-they-good-for-developers"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/neowin-net--universal-apps-what-are-they-and-how-are-they-good-for-devel.md"
    kind: repo
---

The article presents Universal apps as Microsoft’s answer to fragmented mobile development across Windows 8.1 and Windows Phone 8.1. It says the approach lets developers share most code and assets in a shared project while still building a UI suited to each form factor, because phone and tablet use differ.

## Reading notes

- Universal apps are described as a Windows-only solution for Windows 8.1 and Windows Phone 8.1, not as a way to run the same app on iOS or Android.
- In Visual Studio, a Universal app solution includes separate Windows and Windows Phone projects plus a shared project for common code and assets.
- The article says a single UI for phone and tablet is technically possible, but usually a poor choice because the devices are used differently.
- Developers are encouraged to build an optimized UI for each platform while still sharing user controls, data templates, and assets.
- One benefit is shared state: settings and files stored in RoamingSettings or RoamingFolder can sync across devices if kept below 100 KB.
- Another benefit is shared entitlement: if a user buys the app on one platform, the corresponding app on the other platform can be downloaded for free.
- Durable in-app purchases are shared across phone and tablet or PC, while consumable purchases stay tied to the device where they were bought.
