---
title: "Yagni"
date: '2015-05-26T14:41:06-03:00'
category: webclip
summary: 'Yagni says not to build a capability now if you will not need it yet. Fowler frames it as a simple-design practice, weighing build cost, delay, carry, and repair costs against future uncertainty.'
tags: ["yagni", "extreme-programming", "simple-design", "technical-debt"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "bliki: Yagni"
    url: "http://martinfowler.com/bliki/Yagni.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/martinfowler-com--yagni.md"
    kind: repo
---

Yagni means “You Aren’t Gonna Need It.” Fowler presents it as an Extreme Programming mantra tied to simple design and warns against building presumptive features before they are needed. The point is to delay work until the capability is actually required, especially when future needs are uncertain.

## Reading notes

- Yagni is the practice of avoiding capabilities that software does not need yet.
- It is connected to XP simple design and contrasts with heavy up-front planning.
- The startup example shows that waiting on piracy pricing avoids building something six months early.
- Building a presumptive feature can create build cost, delay cost, carry cost, and repair cost.
- Even if the future need is real, early work can delay more urgent features and revenue.
- A useful test is to imagine the refactoring needed later to add the capability when it is actually needed.
- Small decisions, like adding fields, methods, or lookup tables only when needed, also follow the same principle.
- Yagni applies to extra complexity for future features, not to refactoring or other work that makes code easier to change.
- Practices like self-testing code and continuous delivery support the flexible code base that makes Yagni workable.
- Fowler says Yagni failures can be costly, but they are harder to spot than the cases where Yagni saves effort.
