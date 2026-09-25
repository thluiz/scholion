---
title: "Cohesion vs. Coupling"
date: '2026-09-25T21:16:41+01:00'
category: webclip
summary: 'Explains cohesion as the internal focus of a module or system, and coupling as the external dependence between things, especially how changes in one place affect another.'
tags: ["software-engineering", "cohesion", "coupling"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Cohesion vs. Coupling"
    url: "https://theburningmonk.com/2024/12/cohesion-vs-coupling/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/theburningmonk-com--cohesion-vs-coupling.md"
    kind: repo
---

Cohesion is described as the internal focus of a module or system, measured by how well its parts work together toward one purpose. Coupling is described as the external relationship between things, especially how much one system must change when another changes.

## Reading notes

- In a module, cohesion is the degree to which its functions belong together.
- An Authenticator module is used as an example of high cohesion because its functions all support authentication.
- A Utils module is presented as an example of low cohesion because it can become a place for unrelated helper functions.
- In a system, cohesion is the extent to which services or subsystems work together toward one goal.
- A service with clear boundaries and responsibilities is described as having high cohesion.
- A user service that handles authentication, account management, and notifications is given as an example of low cohesion because its responsibilities overlap.
- Coupling is framed as change propagation, or how much System B must change when System A changes.
- The text says coupling appears in many forms, including data format dependency.
- Temporal coupling is described as linking one service’s availability to another service’s availability.
- Temporal coupling can lead to cascade failures and calls for retries, exponential backoff, fallbacks, and chaos engineering.
