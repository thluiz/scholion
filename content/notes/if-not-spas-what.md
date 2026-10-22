---
title: "If not SPAs, What?"
date: '2020-11-02T00:16:26-03:00'
category: webclip
summary: 'The article maps four alternatives to SPA-centric development: opinionated full-stack frameworks, Turbolinks, server-side-state frameworks, and small progressive-enhancement libraries.'
tags: ["spas", "web-frameworks", "progressive-enhancement", "server-side-rendering"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "If not SPAs, What? - macwright.com"
    url: "https://macwright.com/2020/10/28/if-not-spas.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-11/macwright-com--if-not-spas-what.md"
    kind: repo
---

The article groups current alternatives to SPA development into four directions: opinionated full-stack JavaScript frameworks, Turbolinks-style partial page loading, server-side-state frameworks, and small progressive-enhancement libraries. It presents them as different attempts to reduce client-side complexity without returning to the old API-first frontend model.

## Reading notes

- Opinionated full-stack JavaScript frameworks such as Remix, RedwoodJS, and Blitz.js try to reconnect routes and data loading, reduce client-side fetching by default, and make status codes and caching more explicit.
- Next.js is described as close to that category, but still largely unopinionated about the data layer, so many sites using it still rely on a separate API stack.
- The article notes that these projects are backed by companies or foundations, which may help avoid burnout and abandonment in open source projects.
- Turbolinks is presented as a small layer on top of server-rendered apps that replaces full page reloads with AJAX-driven partial updates and smoother navigation.
- Its appeal is the ratio of user-experience gain to added complexity: it changes very little while removing the visual blink of full transitions.
- Server-side-state frameworks like Laravel Livewire, Stimulus Reflex, and Phoenix LiveView shift more interaction logic to the server and aim to let developers write little or no JavaScript.
- These tools rely heavily on WebSockets or close server-client coupling and apply server-computed UI changes on the client side.
- The article frames them as the opposite of the “frontend plus agnostic API layer” pattern because they accept mutable server state instead of avoiding it.
- Modest progressive-enhancement tools such as Stimulus, Alpine, htmlx, and some Web Components are described as small additions for existing pages.
- Their limitation is that they assume knowledge of JavaScript and the DOM, which many developers may no longer have in depth.
