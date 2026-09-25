---
title: "Why Rails 5 / Turbolinks 3.0 / Action Cable matter, and why @dhh was right all along"
date: '2026-09-25T21:50:34+01:00'
category: webclip
summary: 'The post argues that Rails 5 keeps the speed and defaults that made Rails attractive, while Turbolinks 3, Action Cable, and rails-api help Rails stay useful for both traditional apps and SPAs.'
tags: ["rails-5", "turbolinks", "action-cable", "single-page-apps"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why Rails 5 / Turbolinks 3.0 / Action Cable matter, and why @dhh was right all along"
    url: "https://www.amberbit.com/blog/2015/4/22/why-rails-5-turbolinks-3-action-cable-matter-and-why-dhh-was-right-all-along/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/amberbit-com--why-rails-5-turbolinks-3-action-cable-matter.md"
    kind: repo
---

Rails is presented as a framework that made it easy to build polished web apps quickly, and the post says that this advantage was larger than what many JavaScript-heavy SPA stacks offer. It argues that trend-driven choices often add complexity, slow development, and raise the learning curve, especially for less experienced developers.

## Reading notes

- Rails won developers and entrepreneurs because it made building polished web apps fast and simple.
- SPA stacks are described as slower to develop with and as introducing new problems to solve.
- In the early Rails days, small teams could ship working systems in a matter of weeks.
- Web development trends are treated with suspicion, since fashionable tools are often adopted before they are the right fit.
- The author says modern SPA-heavy stacks make feature work and maintenance slower than older Rails setups.
- Rails 5 is framed as adding Turbolinks 3.0, Action Cable, and rails-api into the framework.
- Turbolinks 3.0 is described as an evolutionary step that can update only parts of a page instead of replacing the whole page.
- Action Cable is presented as Rails support for real-time message passing with WebSockets.
- The post says WebSocket support matches real project needs, since several recent projects included real-time or chat features.
- rails-api is described as making slim, API-only Rails apps easier to build, which suits SPA backends.
- The author argues that bundled defaults can speed development without removing Rails flexibility.
- Turbolinks can still be disabled if it does not fit a project.
- The post says there will still be space for traditional server-rendered apps, so Rails is not going away soon.
- The closing advice is to question whether SPAs and extra abstraction layers are actually worth their cost.
