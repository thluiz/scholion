---
title: "What types of features typically lead to lots of tech debt?"
date: '2020-07-05T14:10:34+00:00'
category: webclip
summary: 'The discussion points to features that are rushed, one-off, tightly coupled to specific cases, or added for organizational needs. A/B testing and prototype-like work also tend to add complexity.'
tags: ["technical-debt", "feature-development", "ab-testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What types of features typically lead to lots of tech debt?"
    url: "https://dev.to/ben/what-types-of-features-typically-lead-to-lots-of-tech-debt-p46"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--what-types-of-features-lead-to-tech-debt.md"
    kind: repo
---

The thread focuses on feature requests that create technical debt when they force rushed patches, special-case handling, or extra complexity around the existing system. Comments also single out work that is tightly tied to specific customers, vendors, products, or internal organizational requirements, because those changes are harder to generalize and maintain.

## Reading notes

- Features unlike anything already implemented often require new infrastructure and time that the team may not have.
- Features that are almost the same as existing ones, but with important differences, can lead to duplicated code or hacks.
- One-off requests for a special check or a quick exception often become permanent code.
- Requests driven by urgency, small exceptions, or “we will worry about it later” tend to hide complexity.
- Features tied to specific customers, vendors, products, events, or hardware can break when the scope expands.
- Organizational requirements that are outside the app’s normal usage can become a lasting burden.
- A/B testing is described as useful when done well, but it adds complexity and coordination that can create debt.
- “Example” versions and prototypes can turn into debt when they become the final product.
