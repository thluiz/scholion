---
title: "Micro And Macro Software Architectures, Why You Need Both"
date: "2026-09-23T19:08:24+01:00"
category: webclip
has_commentary: false
summary: "Draws the line between macro architecture decisions a company makes once for everyone and micro architecture decisions each team makes for itself, and argues both need to be explicit."
tags:
  - software-architecture
  - microservices
  - engineering-organization
sources:
  - title: "Micro And Macro Software Architectures, Why You Need Both"
    url: "https://blog.learnly.dev/micro-and-macro-software-architectures-why-you-need-both?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-learnly-dev--micro-and-macro-software-architectures.md"
    kind: repo
---

Zaid Qureshi splits architecture decisions into two levels. Macro architecture covers what applies to every service a company builds: the data lake, logging infrastructure, authentication and authorization. Micro architecture is what a single team decides for itself, usually language, framework, and database choice, as long as it isn't already locked in at the macro level. The post's case is that a company needs both written down, not left implicit, so engineers know where their freedom actually starts and stops.

Locking too much into macro architecture has a cost he names directly: a company that mandates a single programming language for everything can block engineers from picking the right tool for a given job, and that kind of rigidity tends to show up later as stale technology and harder hiring.

## Fichamento

- Micro-frontends are the example he uses for where micro architecture pays off: once integration and security are fixed at the macro level, each team can pick its own stack, its own deploy cadence, and its own branching strategy without touching the rest of the system.
- Not every architecture decision has a clean answer. He expects teams to sometimes pick the "least bad" option and revisit it later, rather than hold out for a perfect one.
- The process matters as much as the decision: architecture choices should be discussed with the whole team from the start, so no one is boxed in by decisions made without them.
