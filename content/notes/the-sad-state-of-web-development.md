---
title: "The Sad State of Web Development"
date: '2016-01-12T19:22:31-03:00'
category: webclip
summary: 'The author argues that modern web development has become over engineered, especially in the Node, frontend, and SPA ecosystems, and says most apps should avoid framework-heavy rewrites.'
tags: ["web-development", "nodejs", "frontend", "single-page-apps"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Sad State of Web Development — Medium"
    url: "https://medium.com/@wob/the-sad-state-of-web-development-1603a861d29f#.o7914kcgv"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/medium-com--the-sad-state-of-web-development.md"
    kind: repo
---

The author says web development went off track around 2015, when the JavaScript and Node communities multiplied tooling, plugins, and dependencies into systems that are hard to install and harder to update. He extends that complaint to frontend tooling, where Babel, PostCSS, React, and SPA thinking are presented as examples of unnecessary complexity.

He argues that most products do not need a full single-page app, because only a small portion of an app usually needs highly complex UI. For the rest, he recommends using backend frameworks like Rails, Django, Play Framework, or Phoenix and bringing in newer frontend tools only for the pages that truly need them.

## Reading notes

- Web development is presented as having become over engineered, especially in the JavaScript and Node ecosystem.
- Node.js and npm are described as creating a large dependency and plugin burden, with fragile updates and poor semver discipline.
- Frontend tools written in Node are said to have imported that same complexity into frontend work.
- Babel is criticized for becoming a plugin-heavy system that does little out of the box.
- PostCSS is criticized for requiring too many plugins and configuration choices before doing useful work.
- React is described as being used for problems that could be solved with much simpler UI work, and as spreading into pages that do not need it.
- The author argues against building single-page apps for most projects.
- He says most apps should use server-side frameworks for the bulk of the work and reserve newer frontend tools for the few pages with complex UI.
