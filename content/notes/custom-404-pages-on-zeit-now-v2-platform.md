---
title: "Custom 404 Pages on Zeit Now v2 Platform"
date: '2026-11-16T18:59:06+00:00'
category: webclip
summary: 'The page argues that custom 404 pages improve branding and help users recover, then shows how to replace Now v2''s default 404 by adding a 404 page and route rules in now.json.'
tags: ["404-page", "now-v2", "static-site", "routing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Custom 404 Pages on Zeit Now v2 Platform"
    url: "https://dev.to/khrome83/custom-404-pages-on-zeit-now-v2-platform-4h2o"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--custom-404-pages-on-zeit-now-v2-platform.md"
    kind: repo
---

The page argues that a custom 404 page helps a site look polished, reflect its brand, and give users a way to recover when they hit a missing page. It contrasts simple 404 pages with more useful ones that keep navigation, search, suggestions, and status links available.

## Reading notes

- A custom 404 page can express the site's brand and include small playful details.
- The dev.to 404 page is minimal and only links back home.
- GitHub's 404 page adds a pop culture reference and tracks mouse movement for a parallax effect.
- Useful 404 pages should help users recover instead of leaving them stuck.
- Consistent navigation, a secondary search, suggestions, status links, and some brand messaging are presented as helpful 404 features.
- Zeit Now v2 ships with a default 404 page that fits the Zeit brand but gives the user no help.
- To replace it, the author creates a `404.vue` page in Gridsome so the build outputs `404.html`.
- `now.json` controls the build process and routing on Now.
- The example configuration uses a static build and then adds routes.
- The routes send normal traffic to the destination directory, expose the filesystem, and catch unfound paths.
- The last route sends missing requests to `404.html` and returns the correct 404 status.
- The final page keeps the header and footer and uses an illustration from unDraw.io.
