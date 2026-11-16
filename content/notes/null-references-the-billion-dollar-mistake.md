---
title: "Null References: The Billion Dollar Mistake"
date: '2026-11-16T02:13:31+00:00'
category: webclip
summary: 'Tony Hoare explains why null references were introduced for convenience in ALGOL W, why they require constant checking, and why their cost and risk make them a long-standing design mistake.'
tags: ["null-references", "programming-languages", "type-checking", "software-safety"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Null References: The Billion Dollar Mistake"
    url: "https://infoq.com/presentations/Null-References-The-Billion-Dollar-Mistake-Tony-Hoare"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/infoq-com--null-references-the-billion-dollar-mistake.md"
    kind: repo
---

Tony Hoare says null references were added in 1965 because they were easy to implement, but he treats that decision as a costly mistake. The talk connects null checking, bounds checking, and type checking to a broader argument that language designers should take responsibility for preventing errors in the programs people write.

## Reading notes

- Null references were introduced in ALGOL W for ease of implementation, not because they were a sound design choice.
- Array bounds checks add cost, but they prevent undetected errors and became standard in later mainstream languages.
- Pointer-based designs can cause serious failures when values are used as addresses by mistake.
- Hoare argues that type checking can prevent whole classes of errors and that customers usually chose safety once they saw the tradeoff.
- He describes null as something that forces checks on every reference and sees non-null references as a later correction.
- He says language designers should accept responsibility for user mistakes and design languages that make correctness easier to prove.
- He links reliability, analysis, and formal verification to safer programming language design.
- He also connects unsafe library functions in C, especially gets, to buffer overflows and the growth of malware.
