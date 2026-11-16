---
title: "3 Types of Toxic Software Projects"
date: '2026-11-16T04:30:37+00:00'
category: webclip
summary: 'The article says software teams should stop projects whose value no longer justifies their cost, whether they were misstarted, have become harder than expected, or are unused code that only adds complexity.'
tags: ["software-projects", "code-complexity", "yagni", "sunk-cost-fallacy"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "3 Types of Toxic Software Projects"
    url: "https://fluentcpp.com/2020/03/10/3-types-of-toxic-software-projects"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/fluentcpp-com--3-types-of-toxic-software-projects.md"
    kind: repo
---

The article groups toxic software projects into three cases: projects that should never have been started, projects that become harder and costlier than expected, and projects that remain in the codebase without being used. In each case, the main point is to reassess value against cost and stop when the project no longer justifies the complexity it adds.

## Reading notes

- Software teams have more possible work than available time, so choosing what not to do matters for productivity and code quality.
- A project can be toxic when it is started for the wrong reason or when the feature is no longer needed.
- A project can also be toxic when the team realizes, too late, that the development does not match the real business case.
- The sunk cost fallacy can keep people working on a bad project because stopping would mean admitting a mistake.
- When a project no longer makes sense, the article recommends throwing away the work rather than finishing it just because time has already been spent.
- A project can become toxic when development uncovers unexpected dependencies, performance problems, misunderstood requirements, or widespread test impact.
- The article says project decisions should follow the current value/cost ratio, which changes as new information appears.
- If the remaining work costs more than the value it would bring, the article argues for discarding the work already done.
- The article extends YAGNI to existing code: if a piece of code is not used, remove it instead of keeping it for possible future use.
- Unused code still adds present-day cost because it complicates nearby development and can affect tests.
- The article closes by saying code that does not exist is easier to understand than code that stays unused in the codebase.
