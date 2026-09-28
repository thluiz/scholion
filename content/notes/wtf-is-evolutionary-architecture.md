---
title: "WTF is Evolutionary Architecture?"
date: '2022-08-14T17:46:36-03:00'
category: webclip
summary: 'The page defines evolutionary architecture as guided, incremental change across dimensions, using prioritised concerns, fitness functions, and observability to keep change predictable rather than chaotic.'
tags: ["evolutionary-architecture", "fitness-functions", "sre", "gitops"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "WTF is Evolutionary Architecture?"
    url: "https://blog.container-solutions.com/wtf-is-evolutionary-architecture"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-08/blog-container-solutions-com--wtf-is-evolutionary-architecture.md"
    kind: repo
---

Evolutionary architecture treats change as continuous. The text links this to cloud computing and Agile, where systems and architectures have no fixed end state and are improved incrementally.

Predictability comes from focusing on the right architectural concerns, making the relevant dimensions visible, and using fitness functions as guard rails. In practice, the page connects this to triggered scans, continual monitoring, GitOps, and SRE so teams can change systems without losing control.

## Reading notes

- Evolutionary architecture supports guided, incremental change across multiple dimensions.
- Cloud computing raises the cost of not changing, so staying constant becomes a risk.
- Agile and cloud-based architecture both point toward continuous improvement rather than a completion point.
- Change should still be predictable, so teams need practices that keep architecture under control.
- The first practice is prioritising architectural concerns, especially the ones that matter most to the business.
- Security can outrank other concerns such as timeliness in regulated sectors.
- Architectural diagrams are only snapshots, so the text argues for considering a wider spectrum of dimensions.
- Many competing forces affect architecture at any given time, and making them visible helps teams choose appropriately.
- Fitness functions act as guard rails and help show whether architecture is degrading.
- Triggered fitness functions include tests, code-quality scans, security scans, and integration tests.
- Continual fitness functions include scripts that keep collecting information, feed dashboards, trigger notifications, and generate reports over time.
- One change in a system can affect another part, so fitness functions should anticipate knock-on effects.
- In microservice architectures, integration tests can confirm that architectural concerns still hold after changes such as replacing AWS API Gateway with Kong.
- GitOps is presented as a practice that makes architectural change as simple as updating configuration in a git-based repository.
- Top-down architectural instructions can slow progress, while teams should be able to architect their own domains.
- SRE helps make systems observable and gives visibility across what teams build.
- With fitness functions and SRE in place, team autonomy becomes easier because changes can be trusted not to degrade the architecture.
