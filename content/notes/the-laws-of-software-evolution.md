---
title: "The Laws of Software Evolution"
date: '2026-09-25T21:17:14+01:00'
category: webclip
summary: 'The page summarizes Lehman’s view that software keeps changing, grows more complex, and is shaped by past choices, while distinguishing S-, P-, and E-programs and outlining an idealized development lifecycle.'
tags: ["software-evolution", "software-engineering", "lehman-laws", "software-architecture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Laws of Software Evolution"
    url: "https://swizec.com/blog/the-laws-of-software-evolution/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/swizec-com--the-laws-of-software-evolution.md"
    kind: repo
---

Lehman’s paper is presented as an early account of why software keeps evolving and why software engineering is distinct from programming. The page says he classifies programs into S-, P-, and E-programs, sketches an ideal lifecycle that does not match practice, and names five laws that still fit experience.

## Reading notes

- Large programs are described as never complete because adding functionality to existing systems often feels easier than starting over.
- Lehman is credited with separating programming from software engineering by arguing for a discipline with insight, theory, models, methodologies, techniques, and tools.
- S-programs map inputs to outputs against a fixed specification and can be fully verified.
- P-programs are defined by business rules and real-world usefulness, but their correctness depends on external criteria.
- E-programs combine P- and S-programs into software that mechanizes a human endeavor or system and keeps adapting over time.
- The ideal development cycle is listed as requirements, top-level design, recursive component design, implementation of the specs, integration, deployment, and then maintenance.
- The page says this ideal cycle does not match practice because specification, coding, integration, and deployment are usually interleaved and overlapped.
- The five laws named on the page are continuing change, increasing complexity, the fundamental law, conservation of stability, and conservation of familiarity.
- Continuing change means software is never done and must adapt to new requirements, environmental changes, and feedback.
- Increasing complexity means software becomes more complex unless work is done to manage that complexity.
- The fundamental law says the system as a whole can be measured and understood statistically even when local decisions are made from limited knowledge.
- Conservation of stability says output rate stays constant, so adding people is needed just to keep the same pace as maintenance grows.
- Conservation of familiarity says growing software becomes more constrained by past choices and large changes become more disruptive as the user base grows.
