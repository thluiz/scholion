---
title: "A Few Things I Do Every Time I Start A New Gatsby Site"
date: '2026-11-16T00:47:00+00:00'
category: webclip
summary: 'The author says he updates starter dependencies, prefers Yarn, adds a lang attribute for accessibility, and installs plugins for CSP and offline caching when starting a Gatsby site.'
tags: ["gatsby", "yarn", "accessibility", "plugins"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A Few Things I Do Every Time I Start A New Gatsby Site"
    url: "https://dev.to/shelob9/a-few-things-i-do-every-time-i-start-a-new-gatsby-site-5gd"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--a-few-things-i-do-every-time-i-start-a-new-gatsby-site.md"
    kind: repo
---

The author keeps a checklist for new Gatsby sites. He updates starter dependencies right away, switches package scripts to Yarn, adds a lang attribute to the html element, and installs plugins for Content Security Policy and offline caching.

## Reading notes

- He upgrades all dependencies to the latest versions before working with a starter, using yarn upgrade-interactive --latest.
- He prefers Yarn over npm, replaces "npm run" with "yarn" in package.json, and deletes package.lock.
- He checks starters with the aXe accessibility extension and often finds that the html element is missing a lang attribute.
- He says this can be fixed with Helmet by passing htmlAttributes={{ lang: 'en' }}.
- He adds Gatsby plugins for Content Security Policy and offline caching.
- He links to an article about PWAs and Gatsby and asks readers what else they do when starting a Gatsby site.
