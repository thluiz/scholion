---
title: "How to publish a PWA on the Google Play store"
date: '2026-11-16T18:51:08+00:00'
category: webclip
summary: 'The post explains what a PWA needs, then walks through packaging a Gatsby-based PWA as a Trusted Web Activity, generating asset links, and submitting the app to Google Play.'
tags: ["pwa", "google-play", "trusted-web-activity", "gatsby"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to publish a PWA on the Google Play store"
    url: "https://dev.to/jumpalottahigh/how-to-publish-a-pwa-on-the-google-play-store-2bid"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--how-to-publish-a-pwa-on-google-play-store.md"
    kind: repo
---

The post first sketches the basic idea of a PWA and the requirements behind it, then shows how to package an existing Gatsby app for Google Play using a Trusted Web Activity. It also notes that tools like Workbox, Android Studio, and pwa2apk can simplify the process.

## Reading notes

- PWAs are presented as web apps with performance, offline access, HTTPS, and installability benefits.
- A PWA needs a manifest file and a service worker, with the manifest defining app metadata such as icons, colors, and name.
- Service workers are described as scripts that can intercept requests and serve content offline after the first visit.
- Workbox is suggested as an easier way to set up a service worker than building everything from scratch.
- Modern frameworks like Gatsby, Create React App, and Vue CLI can help create PWAs with little manual work.
- The author’s project, fpvtips.com, is run as a Gatsby PWA and the source code is open on GitHub.
- To publish the PWA on Google Play, the post recommends installing Android Studio and paying the Google developer fee.
- The approach uses the GoogleChromeLabs svgomg-twa boilerplate and changes values such as applicationId, hostName, launchUrl, name, themeColor, and backgroundColor.
- A signed APK is created in Android Studio, with a keystore generated the first time.
- The SHA256 certificate fingerprint is obtained with keytool and then used in Google Digital Asset Links to generate an assetlinks.json file.
- The assetlinks.json file is placed under .well-known at the site root and published live.
- The APK is uploaded in Google Play Console, where required app information must be completed before review.
- The post mentions waiting for review before the app becomes available and suggests Android Asset Studio for generating images.
- It also says that building an App Bundle instead of an APK can resolve an asset optimization warning.
