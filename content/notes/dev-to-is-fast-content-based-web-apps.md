---
title: "Dev.to is the perfect demonstration of how content-based web apps should be developed"
date: '2026-11-16T01:08:55+00:00'
category: webclip
summary: 'The post argues that Dev.to feels unusually fast because it serves server-rendered HTML and uses InstantClick to preload linked pages, making it a model for content-heavy web apps.'
tags: ["dev.to", "server-rendered-html", "instantclick", "frontend-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dev.to is the perfect demonstration of how content-based web apps should be developed"
    url: "https://dev.to/bigi/dev-to-is-the-perfect-demonstration-of-how-content-based-web-apps-should-be-developed-5fa4"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--dev-to-is-fast-content-based-web-apps.md"
    kind: repo
---

The post says Dev.to feels extremely fast because it behaves like a local app and not like a typical site on the internet. The author traces that speed to server-rendered HTML plus InstantClick, then uses that example to argue for content-based web apps that keep page navigation server-driven.

## Reading notes

- The author was moving away from Medium and started trying Dev.to after seeing it recommended.
- Dev.to felt so fast during signup and profile editing that it seemed local rather than remote.
- The site serves full HTML from the server instead of using a React-style frontend framework.
- Hovering links preloads pages, and clicking replaces the current HTML while using history.pushState().
- The author identifies InstantClick as the mechanism behind this behavior.
- The post argues that content-based sites, including blogs and e-commerce sites, should follow this model.
- The author says the industry spent years improving server-side performance, but heavyweight client frameworks reduce those gains.
- The main counterargument the author accepts for React is organizational: component-based frontend work scales better for big teams.
- Traditional MVC view systems and jQuery frontends are described as hard to maintain at scale.
- The proposed workflow keeps component-based frontend development, but builds static HTML pages from components and lets the backend render those prebuilt pages with variables.
- In that workflow, the frontend team can mock backend data during development, and CI rebuilds page HTML when components change.
- The author still allows local component interactions and AJAX, but says full page navigation should stay with anchor links, InstantClick, and server-rendered pages.
