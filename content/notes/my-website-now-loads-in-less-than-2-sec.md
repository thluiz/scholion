---
title: "My website now loads in less than 2 sec! Here's how I did it! ⚡"
date: '2020-07-05T10:19:22-03:00'
category: webclip
summary: 'The author says the portfolio loads in 1.8 seconds with a 94 Lighthouse score, and lists ten performance tips focused on DOM size, payloads, images, redirects, preloading, preconnecting, and minification.'
tags: ["web-performance", "lighthouse", "frontend-optimization", "image-optimization"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "My website now loads in less than 2 sec! Here's how I did it! ⚡ - DEV"
    url: "https://dev.to/cmcodes/my-website-now-loads-in-less-than-2-sec-here-s-how-i-did-it-hoj"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-07/dev-to--my-website-now-loads-in-less-than-2-sec.md"
    kind: repo
---

The post says the portfolio website loads in 1.8 seconds and reaches a Lighthouse performance score of 94. It then presents ten tips aimed at reducing load time and improving web performance, with examples from the author’s own site.

## Reading notes

- Keep the DOM tree small because large DOM trees increase memory use, slow loading, and make rendering more expensive.
- Keep network payloads low by deferring requests, minifying and compressing assets, and compressing JPEG images to 85.
- Avoid GIFs for static or animated content; use PNG or WebP for static images and MPEG4 or WebM video for animation.
- Preload key requests so CSS and other needed resources start earlier.
- Avoid multiple redirects because each redirect adds another network request and slows loading.
- Use preconnect to establish early connections to important third-party origins.
- Encode images efficiently by compressing them, using image CDNs, serving responsive images, and lazy loading images.
- Minify JavaScript to reduce payload size and parsing time.
- Minify CSS and use shorthand values where possible, such as reducing #000000 to #000.
- Resize images so they are no larger than what is rendered on screen, and use responsive images, image CDNs, or SVG for icons.
