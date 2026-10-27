---
title: "Technical debt 101"
date: '2014-07-13T21:48:38-03:00'
category: webclip
summary: 'The article argues that technical debt is a conscious design trade-off, not simply bad code, and that neglecting quality creates long-term costs, legacy code, and cultural damage.'
tags: ["technical-debt", "legacy-code", "software-development", "engineering-culture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Technical debt 101 — Medium"
    url: "https://medium.com/@joaomilho/festina-lente-e29070811b84"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-07/medium-com--technical-debt-101.md"
    kind: repo
---

The article argues that technical debt should mean a deliberate choice to postpone a design decision when the team understands the cost and the future refactoring path. It separates that from writing bad code, which is presented as a different problem tied to weak quality control, weak management, and poor software culture.

It also says that legacy code is hard to fix because it usually lacks tests, which makes refactoring risky and slow. Big rewrites are treated as an unreliable answer to a cultural problem, so the more realistic path is to improve the current code base in cycles, with tests, planning, and a broader change in how the company values quality.

## Reading notes

- Technical debt is a conscious trade-off made when the team delays a design decision with a clear understanding of the cost and the refactoring path.
- The article says the debt analogy works only when the choice is deliberate; it does not apply to simply writing bad code.
- Bad code is linked to poor quality control, weak oversight, and a management culture that pushes short-term delivery.
- Legacy code is described as code without tests, because tests are what let teams change behavior quickly and verify the result.
- Refactoring bad code is hard because adding tests on top of tightly coupled code is itself difficult.
- Big rewrites are presented as a technical answer to a cultural problem and are often unrealistic.
- The suggested response is to improve the existing code base in cycles, add tests, split monolithic parts, and plan data migrations carefully.
- The article frames neglecting quality as a cultural issue that can hurt strategy and make the company less attractive to good developers.
