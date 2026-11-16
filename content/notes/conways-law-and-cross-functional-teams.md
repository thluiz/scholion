---
title: "Conway's Law and Cross-Functional Teams"
date: '2020-02-22T12:11:50+00:00'
category: webclip
summary: 'The article explains Conway’s Law as the way organizations shape the systems they build, then argues that team structure can reduce communication problems and improve knowledge sharing when teams are reorganized around products.'
tags: ["conways-law", "cross-functional-teams", "software-engineering", "team-structure"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Conway's Law and Cross-Functional Teams - Kill All Defects"
    url: "https://web.archive.org/web/20200808054233id_/https://killalldefects.com/2020/01/30/conways-law-and-cross-functional-teams/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--conways-law-and-cross-functional-teams.md"
    kind: repo
---

Conway’s Law says organizations produce designs that mirror their communication structures. The article applies this to software teams, arguing that separate teams often lead to separate systems or modules, and that parallel work can create artificial boundaries in code.

## Reading notes

- Conway’s Law describes how organizational structure shapes the systems and code teams produce.
- When a department has several teams, the result often becomes several separate systems or modules that communicate only sparingly.
- Work done in parallel can introduce artificial boundaries such as new methods, classes, or projects.
- The law is presented as a natural effect of software development, not as something simply good or bad.
- Separating work into different systems can help teams divide labor, work in parallel, and manage complex enterprises.
- The article lists downsides such as slower performance, increased complexity, misunderstandings between teams, less knowledge sharing, new bug classes from system interactions, code duplication, and more failure points.
- It also lists upsides such as larger-scale growth, parallel work, specialist focus, and services adapting while keeping the same external interface.
- The article suggests using Conway’s Law deliberately by moving people and projects between teams when communication problems appear.
- Putting people close together can improve communication, shared understanding of domain logic, and technical knowledge.
- Organizing teams by product instead of technology can make shared domain work easier to coordinate.
- If teams are split by technology, problems may get handed from one group to another without anyone discussing the real system assumptions.
- The article says smaller functional groups can help organizations with diverse engineering technologies.
- It closes by warning against restructuring for appearance alone and by saying Conway’s Law should be considered when knowledge sharing and system communication are failing.
