---
title: "Using HTML, CSS, and JavaScript to Create OBS Plugins for Your Live Streaming Sessions"
date: '2020-04-13T02:40:14+00:00'
category: webclip
summary: 'The author explores using OBS''s Browser source to build plugins with HTML, CSS, and JavaScript instead of C++. He shares a Preact and HTM template that runs from a local web server and supports live reloading.'
tags: ["obs", "browser-source", "preact", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using HTML, CSS, and JavaScript to Create OBS Plugins for Your Live Streaming Sessions"
    url: "https://dev.to/horusgoul/using-html-css-and-javascript-to-create-obs-plugins-for-your-live-streaming-sessions-45ij"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--using-html-css-and-javascript-to-create-obs-plugins.md"
    kind: repo
---

The page says OBS plugins do not need to be written in C++. It introduces the Browser source as a way to point OBS to a URL or local HTML file and build a dynamic viewer experience with web technologies.

The author chose Preact, HTM, and plain CSS because the stack works without a build step. After building a first plugin that shows the latest posts from a dev.to profile, they published a template repository for making OBS plugins or web apps from a local server.

## Reading notes

- OBS Browser source can load a URL or local HTML file inside an internal browser with modern web capabilities.
- The author rejected C++ for this use case because it would be overkill.
- The chosen stack is Preact, HTM, and plain CSS.
- The stack works without a build step.
- The first plugin shown in the article loads the latest posts from the author's dev.to profile.
- The author published a template repository named `HorusGoul/preact-obs-plugin`.
- The template can be used to build OBS plugins or web apps.
- The dependencies are loaded from CDNs.
- The setup uses `npx serve` for a local web server.
- The author recommends `npx live-server` for development because it reloads the site when files change.
