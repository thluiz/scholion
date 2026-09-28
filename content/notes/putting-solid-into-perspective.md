---
title: "Putting SOLID into Perspective"
date: '2022-08-16T11:31:23-03:00'
category: webclip
summary: 'The post treats SOLID as a useful but limited heuristic, not a set of rules, and compares it with CUPID and other design tools like RDD, GRASP, DRY, code smells, and Tell, Don’t Ask.'
tags: ["solid", "software-design", "heuristics", "oop"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Putting SOLID into Perspective – The Shade Tree Developer"
    url: "https://jeremydmiller.com/2022/08/10/putting-solid-into-perspective/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-08/jeremydmiller-com--putting-solid-into-perspective.md"
    kind: repo
---

The post argues that SOLID should be seen as a sometimes helpful heuristic for thinking about design, not as a universal standard for judging code. It says each principle has some value in specific situations, but all of them are too vague or too context-dependent to work well as hard rules. The author also says CUPID is worth reading, especially for its emphasis on staying within the idioms of the language, toolset, and codebase.

## Reading notes

- SRP is tied to cohesion, but it is too vaguely worded to be a reliable rule.
- OCP can help when thinking about extension and change, especially in frameworks, but it is not always the simplest choice.
- LSP is mainly useful as a warning against leaky abstractions and hidden implementation assumptions.
- ISP matters most when designing APIs for other developers and for keeping interfaces focused on a single role.
- DIP is treated as overblown when applied too broadly, even if abstractions are useful in some cases.
- CUPID is presented as a philosophical starting point, with a strong emphasis on idiomatic code.
- Responsibility Driven Design is described as the author’s most useful design tool.
- GRASP, especially Information Expert, helps assign responsibilities in code.
- Command Query Separation is used to keep code predictable and limit state mutation.
- DRY is useful against harmful duplication, but abstractions created to remove duplication can become worse than the duplication itself.
- A-Frame Architecture is recommended as a way to separate business logic from infrastructure without overcomplicating abstractions.
- Code smells and anti-patterns are presented as warning signs that call for attention rather than automatic condemnation.
- Tell, Don’t Ask is treated as a shorthand for improving encapsulation and coupling.
