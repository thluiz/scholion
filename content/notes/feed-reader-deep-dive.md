---
title: "Lighthouse - The feed reader for finding actionable content"
date: '2025-10-28T19:08:55+00:00'
category: webclip
summary: 'The article maps the feed-reader landscape by deployment and business model, explains where each type stores data and fetches feeds, and shows when hosted, self-hosted, on-device, or browser-extension readers fit best.'
tags: ["feed-readers", "rss", "product-landscape", "self-hosted"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Lighthouse - The feed reader for finding actionable content"
    url: "https://lighthouseapp.io/blog/feed-reader-deep-dive"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-10/lighthouseapp-io--feed-reader-deep-dive.md"
    kind: repo
---

The article classifies feed readers by deployment model and business model, then explains how each category handles setup, storage, feed fetching, availability, and functionality. It also points out that hosted products are usually the most polished, while self-hosted options give the most control.

## Reading notes

- Feed readers have existed for more than 20 years and help users consume content from many sources in one place, especially when there is content overload.
- The article says it classifies feed readers along two axes: deployment model and business model.
- Deployment model covers local, browser extension, self-hosted, and hosted.
- Business model covers free, one-time payment, and SAAS.
- Browser extensions store data locally, fetch feeds on the device, and can integrate deeply with the browser.
- On-device products are installed on a phone or computer, store data locally, and fetch feeds on that device.
- Self-hosted products are open source and free, run on a server, store data on the server, and make it available through a web interface.
- Hosted products are managed services that require an account, store data on company servers, and usually offer the most polished experience and the most complete feature sets.
- The article says many self-hosted or hosted products provide APIs, which lets native apps such as ReadKit or Fiery Feeds connect to them.
- It notes that newsletters can sometimes be added to feed readers through services that convert newsletters into RSS feeds.
- NetNewsWire stores data on-device by default, can sync via iCloud or other products, and supports AppleScript.
- Fiery Feeds can sync via iCloud and other products, and its main distinguishing feature is customization.
- Reeder stores data on-device, can sync via iCloud, and its main distinguishing feature is a unified timeline that includes RSS, podcasts, social media, and more.
- FreshRSS is self-hosted, offers WebSub, supports themes and extensions, and is translated into more than 15 languages.
- Miniflux is self-hosted, focuses on staying simple and fast, and also has a hosted version.
- Folo is a free hosted product with apps for major platforms, newsletter support, website-to-feed conversion, and AI summaries.
- Feedly is described as the most widely known feed reader and has a free plan.
- Inoreader also has a free plan and includes social media support, automation, AI features, and integrations.
- Readwise Reader is described as strong in the reading experience and also supports PDFs and eBooks.
- Tiny Tiny RSS is mentioned as an honorable mention, but its maintainer announced that he will stop working on it.
- Lighthouse is described as a beta product that focuses on articles over feeds and has a separate inbox for curating articles.
- The article compares feed readers with news aggregators and reading lists, saying those categories can be simpler for some use cases.
- It recommends choosing a category first, then comparing products, and notes that OPML import and export make switching easy.
