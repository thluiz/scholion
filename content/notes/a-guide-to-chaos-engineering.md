---
title: "A guide to chaos engineering"
date: "2026-09-23T19:16:50+01:00"
category: webclip
has_commentary: false
summary: "A short overview of chaos engineering for product managers: deliberately breaking a system to find its weak points before real users do, with Netflix's Chaos Monkey as the reference case."
tags:
  - chaos-engineering
  - reliability
  - product-management
sources:
  - title: "A guide to chaos engineering - LogRocket Blog"
    url: "https://blog.logrocket.com/product-management/what-is-chaos-engineering/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-logrocket-com--a-guide-to-chaos-engineering.md"
    kind: repo
---

Chaos engineering injects failures into a system on purpose, then watches how it responds, to surface weaknesses before they reach users. The piece frames this as a product manager's tool, not only an engineering one: the data from a chaos experiment feeds directly into what gets prioritized next.

Netflix is the reference case. Chaos Monkey, part of its Simian Army suite, randomly disables production instances to force the streaming service to prove it can absorb that kind of failure without users noticing. The piece credits that practice with meaningfully improving Netflix's resilience and treats it as the benchmark other companies now measure against.

## Fichamento

- Recommended practice is to start small, with low-risk experiments simulating minor failures, and build up from there rather than testing worst-case scenarios first.
- Chaos experiments are meant to run inside CI/CD, as continuous resilience testing, not as a one-off exercise.
- Named tools beyond Chaos Monkey: Gremlin, for running controlled chaos experiments across infrastructure and applications, and LitmusChaos, an open-source framework scoped to Kubernetes environments.
- Cross-team collaboration and a data-driven case for the practice are named as what overcomes internal resistance to deliberately breaking things in production.
