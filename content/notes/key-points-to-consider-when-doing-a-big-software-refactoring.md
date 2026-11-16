---
title: "Key points to consider when doing a big software refactoring"
date: '2016-07-15T13:12:50+00:00'
category: webclip
summary: 'The post says a big refactoring needs clear business goals, progress tracking, team motivation, prioritization, test coverage, test performance, and sponsor commitment to avoid becoming endless.'
tags: ["refactoring", "software", "cto"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Key points to consider when doing a big software refactoring « Plataformatec Blog"
    url: "https://blog.plataformatec.com.br/2016/07/key-points-to-consider-when-doing-a-big-software-refactoring"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-plataformatec-com-br--key-points-to-consider-when-doing-a-big-software-refactoring.md"
    kind: repo
---

The post argues that a big software refactoring should be treated as a structured project, with clear goals, planning, prioritization, and a defined end. It also stresses that the work affects motivation, delivery speed, and the ability to keep improving safely.

## Reading notes

- Set clear business goals before starting, or stakeholders may not stay committed.
- Measure refactoring progress in a structured way, as with other project work.
- Keep the team motivated by showing progress, planning small deliverables, and considering developer rotation.
- Choose an approach, either improving code when touching bad parts or selecting targets proactively.
- When goals are clear, prioritize the parts that help make those goals real.
- When refactoring a whole codebase, use complexity and churn to decide what to tackle first.
- Parts with high complexity and frequent change are better candidates than ugly parts that rarely need changes.
- Treat the refactoring as a project with a beginning, middle, and end.
- Keep good test coverage so the refactoring does not create more bugs than improvements.
- Make sure the test suite is fast enough, because refactoring depends on running tests continuously.
- Secure sponsor commitment, since long refactoring work can slow feature delivery for weeks or months.
