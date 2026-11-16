---
title: "Architecture vs. Design"
date: '2026-11-16T03:40:46+00:00'
category: webclip
summary: 'Fairbanks defines software architecture as the subset of design details needed to reason about likely failures. Architecture is the model used to exclude irrelevant details and focus on risks.'
tags: ["software-architecture", "software-design", "models", "risk"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "George Fairbanks - Architecture vs. Design"
    url: "https://georgefairbanks.com/blog/software-architecture-vs-design"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/georgefairbanks-com--architecture-vs-design.md"
    kind: repo
---

Fairbanks explains software architecture as a kind of software design, but one defined by its role in reasoning about risks and failures. A design detail is architectural only when it helps explain how the system avoids a failure the developer is worried about.

## Reading notes

- Software architecture is presented as a subset of software design.
- The point of architectural thinking is to reason about possible failures.
- Because software is complex and time is limited, developers build models instead of trying to understand everything.
- The model should focus on the risks that are possible or likely.
- Different kinds of software lead to different risks, such as security and request spikes for websites, or memory leaks and portability for embedded software.
- Architectural details are the details included in the model because they help reason about those risks.
- Other design details may be needed to build the system, but they are not architectural if they do not support reasoning about failure risks.
- A design detail is architectural if it can be traced back to avoiding a failure risk.
- The cited definition says software architecture is the set of structures needed to reason about the system, including software elements, relations among them, and properties of both.
