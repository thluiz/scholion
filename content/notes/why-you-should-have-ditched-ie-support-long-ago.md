---
title: "Why you should have ditched IE support long ago..."
date: '2020-09-07T20:03:12-03:00'
category: webclip
summary: 'The post argues that IE support is no longer worth the cost because IE lacks key JavaScript, Web API, CSS, and HTML features, and many sites already break or refuse to support it.'
tags: ["internet-explorer", "web-development", "browser-support", "css"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why you should have ditched IE support long ago... - DEV Community 👩‍💻👨‍💻"
    url: "https://dev.to/areknawo/why-you-should-have-ditched-ie-support-long-ago-1jj9"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/dev-to--why-you-should-have-ditched-ie-support-long-ago.md"
    kind: repo
---

The post argues that supporting Internet Explorer is no longer a practical default for new work. It points to IE's long decline, its lack of support for modern JavaScript, Web APIs, and important CSS features, and the way many sites already behave poorly or block access in IE.

## Reading notes

- IE was released by Microsoft in 1995, reached more than 90% market share in the early 2000s, and later fell to about 1.5%.
- Microsoft released Edge in 2015 and later planned a Chromium-based version of Edge.
- Supporting IE 11 can require giving up modern ES6 features, or relying on tools such as Babel and polyfills that add complexity or bloat.
- IE lacks support for Fetch API, Web Notifications, and WebRTC, and its WebGL access uses the nonstandard "experimental-webgl" identifier.
- CSS support is incomplete for Flexbox, Grid, CSS variables, and viewport units, even if processing tools like PostCSS can help.
- On the author's site, IE breaks ads, the newsletter box, Disqus comments, and AJAX page transitions because of unsupported ES6 template literals.
- YouTube works in IE but uses an older interface.
- GitHub warns that the browser is unsupported, and parts of the interface appear broken.
- CodePen shows a large unsupported-browser dialog.
- CSS-Tricks remains readable, but styles are off and some elements disappear.
- Slack and Trello do not allow login, and Apple's homepage has a broken layout in IE.
- The post concludes that IE support should matter less unless a site targets a very broad or specific audience, and that keeping support only makes sense when it costs nothing or limits nothing.
