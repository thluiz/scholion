---
title: "LICENSE to kill your PWA"
date: '2026-11-16T02:27:32+00:00'
category: webclip
summary: 'A PWA broke because a precached `.LICENSE` asset returned 404 on IIS. The cause was terser-webpack-plugin extracting license comments into a file the server did not serve correctly.'
tags: ["pwa", "webpack", "terser-webpack-plugin", "iis"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "LICENSE to kill your PWA"
    url: "https://blog.johnnyreilly.com/2020/01/license-to-kill-your-pwa.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-johnnyreilly-com--license-to-kill-your-pwa.md"
    kind: repo
---

The post explains how a PWA kept serving an old cached version because pre-caching failed on a missing `.LICENSE` file. The failure came from a `404` on IIS, where the extracted license asset was not configured to be served.

## Reading notes

- A `bad-precaching-response` error appeared when the app tried to load `/static/js/6.20102e99.chunk.js.LICENSE?__WB_REVISION__=e2fc36`.
- The server had a `.LICENSE` file at that location, but IIS did not support that file type correctly.
- The file was created by the build, which scraped license comments from bundled files into `6.20102e99.chunk.js.LICENSE`.
- The problem was traced to `terser-webpack-plugin`, which extracts license files by default.
- The app was an ejected `create-react-app` project, so the build settings could be changed.
- The fix was to set `extractComments: false` in `TerserPlugin` inside `webpack.config.js`.
- A later update says the plugin behavior should change to emit `.LICENSE.txt` files by default, which would be friendlier to IIS and similar servers.
