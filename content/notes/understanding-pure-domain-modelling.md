---
title: "Understanding Pure Domain Modelling"
date: "2026-09-23T18:19:19+01:00"
category: webclip
has_commentary: false
summary: "Argues that domain experts default to describing their existing system rather than the real domain, and proposes asking 'what would you do without a system?' to get past that bias."
tags:
  - domain-driven-design
  - software-architecture
  - requirements
sources:
  - title: "Understanding Pure Domain Modelling: Bridging the Gap Between Existing Systems and the Real Domain"
    url: "https://bartwullems.blogspot.com/2024/07/understanding-pure-domain-modelling.html?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/bartwullems-blogspot-com--understanding-pure-domain-modelling.md"
    kind: repo
---

Bart Wullems names a bias he keeps running into during domain modelling workshops: domain experts describe the domain in terms of the system they already use, not the business itself. He recounts a full workshop where the result turned out to be a model of the existing system, not the real business needs it was meant to capture.

He calls the alternative "pure domain modelling": building a conceptual model of the business as close to reality as possible, deliberately set apart from any existing system or technology.

## Reading notes

- Domain experts anchored to their current system tend to describe the domain the way it's implemented, which constrains the model to that system's existing limitations and design choices.
- Business rules absent from the current system get left out of the model even when they matter, because experts describe what the system does rather than what the business actually needs.
- Familiarity breeds resistance: experts favor structures they already know even when those structures are suboptimal for the real domain.
- Wullems cites Udi Dahan's line that users don't describe requirements, they describe workarounds, as the underlying pattern behind the bias.
- His proposed fixes include interviews framed around "what would you do if there was no system," documenting and challenging assumptions inherited from the current system, incremental modelling that starts from high-level concepts, and Domain-Driven Design practices like Event Storming and ubiquitous language to keep the model anchored to the real domain.
- The question he says he always asks in these workshops: what would you do if there was no system available?
