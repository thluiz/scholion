---
title: "Finding modules in a big ball of mud"
date: '2026-09-25T21:15:40+01:00'
category: webclip
summary: 'The post argues that tangled code is normal and that modules should be found by reading dependency graphs, matrices, and domain neighborhoods rather than forcing an early architecture.'
tags: ["software-engineering", "architecture", "dependency-graph", "domain-driven-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Finding modules in a big ball of mud"
    url: "https://swizec.com/blog/finding-modules-in-a-big-ball-of-mud/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/swizec-com--finding-modules-in-a-big-ball-of-mud.md"
    kind: repo
---

The post says a big ball of mud is a normal starting point when software is already working, and that trying to lock in the wrong architecture too early can make things worse. It recommends looking for natural module boundaries in dependencies and in the business domain.

## Reading notes

- A tangled codebase is presented as something to expect once the software works, not as proof of failure.
- A wrong architecture can create more pain than no architecture, as shown by the microservice example that became hard to change and was eventually thrown away.
- Code can be viewed as a dependency graph at different levels, from functions to systems, with boxes for units of code and lines for their connections.
- A dependency matrix can make structure and messiness visible by showing where connections cluster or spread evenly.
- Dense internal connections with few external ones point to natural modules.
- Some module boundaries cut across existing boxes, especially when shared implementation hides separate concerns.
- Whiteboards and paper help when deciding whether similar code should stay together or split apart.
- The post ties good architecture to the business domain and to domain driven design.
- Event storming is described as a way to uncover events, commands, actors, and business processes with stakeholders.
- The goal is a core business logic module with separate interfaces for different actors so the system feels obvious and simple.
