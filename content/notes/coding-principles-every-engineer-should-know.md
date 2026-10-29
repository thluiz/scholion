---
title: "Coding Principles Every Engineer Should Know"
date: '2014-08-20T01:39:31-03:00'
category: webclip
summary: 'The author lists personal engineering principles: be paranoid, avoid leaky abstractions, keep designs simple, defer optimization, fix bugs at the root, question assumptions, think long term, care about code, and accept software trade-offs.'
tags: ["software-engineering", "coding-principles", "optimization", "software-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Coding Principles Every Engineer Should Know — Medium"
    url: "https://medium.com/@sschillace/coding-principles-every-engineer-should-know-b946b48cc946"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-08/medium-com--coding-principles-every-engineer-should-know.md"
    kind: repo
---

The author presents a set of personal engineering principles learned across his career. They focus on skepticism, simplicity, long-term thinking, and taking responsibility for the code you write and operate.

## Reading notes

- Be paranoid: do not trust systems, fixes, or your own understanding without checking them more than once.
- Do not lie to the computer: avoid leaky abstractions, undocumented side effects, and uses the system was not meant to support.
- Keep it simple: solve only what needs to be solved, because code is maintained much longer than it is created.
- Do not optimize too early: most optimization is never used, and it makes designs more complicated.
- When fixing a bug, try to remove the conditions that could let it happen again.
- Question assumptions constantly and ask what problem is really being solved.
- Think long term: rushed code and local shortcuts can slow future work.
- Care about your code and write it so it is readable and well designed.
- Accept the trade-off of cheap, fast, and right, and be clear about which compromise you are making.
- Stay curious and keep learning new things throughout your engineering career.
