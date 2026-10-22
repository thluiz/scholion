---
title: "Solutions Architect Tips - The 5 Types of Architecture Diagrams"
date: '2021-06-14T09:01:50-03:00'
category: webclip
summary: 'The article argues that architecture diagrams should match the audience and purpose. It outlines five types—flow, service, persona, infrastructure, and developer—and explains when to use each one.'
tags: ["architecture-diagrams", "solutions-architect", "software-design", "communication"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Solutions Architect Tips - The 5 Types of Architecture Diagrams - DEV Community"
    url: "https://dev.to/aws-builders/solutions-architect-tips-the-5-types-of-architecture-diagrams-3pl3"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-06/dev-to--solutions-architect-tips-5-types-architecture-diagrams.md"
    kind: repo
---

The article says architecture diagrams are not one-size-fits-all. A solutions architect should choose the diagram type according to the audience, whether that is technical teams, business people, executives, or developers. It starts from a flow diagram and then adapts it for other uses.

## Reading notes

- The flow diagram is the broadest option and shows the moving parts of a workflow, the connections between them, and how data flows through the system.
- The service diagram shows high-level connectivity, especially internal and external services, without detailing how each service works.
- The persona diagram focuses on actors in a workflow and the order of steps, with swim lanes and business assumptions to show how the solution addresses the business problem.
- The infrastructure diagram presents everything that has been implemented and works as a blueprint of the application, with an inventory of all pieces and their connections.
- The developer diagram adds implementation detail to the flow diagram so developers can build the solution without extra explanation.
- The author says different versions of the same design are useful at different stages, from pitching the idea to other architects and business stakeholders to supporting implementation and later updating the infrastructure view.
- The article recommends draw.io as the tool the author uses for building diagrams.
