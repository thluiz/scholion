---
title: "Did contexts kill Phoenix?"
date: "2026-09-23T18:36:05+01:00"
category: webclip
has_commentary: false
summary: "Argues that Phoenix's contexts layer, meant to enforce domain-driven boundaries, raised the barrier to entry enough to slow the framework's adoption relative to Rails."
tags:
  - elixir
  - phoenix
  - software-architecture
sources:
  - title: "Did contexts kill Phoenix? · Arrowsmith Labs"
    url: "https://arrowsmithlabs.com/blog/did-contexts-kill-phoenix"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-06/arrowsmithlabs-com--did-contexts-kill-phoenix.md"
    kind: repo
---

Phoenix rates as one of the most admired web frameworks in the Stack Overflow developer survey, yet twelve years in it remains niche next to Rails. A tweet the author keeps returning to blames the architectural shift introduced in Phoenix 1.3: contexts, the layer that groups related schemas and functions into named domains like `Accounts` or `Blog`. Google Trends shows interest declining from mid-2017, right after that release.

Contexts follow domain-driven design in theory: expose to the web layer only the functions a business domain actually needs. In practice, naming a context forces beginners to commit to a domain boundary before they know what the app even needs, and the author has watched contexts fill up with thin wrapper functions around `Repo` calls, adding indirection without much architectural payoff on small projects.

## Fichamento

- Nothing technically forces contexts; a controller can call `Repo` directly, but the docs imply everything should route through one.
- The author has taught thousands of Phoenix beginners and reports contexts as a consistent, recurring source of confusion.
- Rails users pick one name (the model); Phoenix users pick two (the model and the context), adding mental overhead the author calls unnecessary friction.
- On greenfield projects, the app's real domain boundaries often aren't clear yet, so naming a context means committing early to structure that later turns out wrong.
- The proposed fixes: better tooling that automates context boilerplate, stronger conventions to cut the bikeshedding, or a beginner mode that defers the complexity.
