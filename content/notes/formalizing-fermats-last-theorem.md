---
title: "Formalizing Fermat's Last Theorem"
date: '2026-09-25T21:44:27+01:00'
category: webclip
summary: 'Anthropic says Claude produced the first end-to-end computer-checked proof of Fermat’s Last Theorem in 11 days, showing how large proofs can be formalized and verified with Lean.'
tags: ["fermat-s-last-theorem", "lean", "formal-verification", "ai-research"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Formalizing Fermat's Last Theorem"
    url: "https://www.anthropic.com/research/formalizing-fermats-last-theorem?utm_source=tldrai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/anthropic-com--formalizing-fermats-last-theorem.md"
    kind: repo
---

Anthropic says Claude worked largely autonomously for 11 days to produce the first complete computer-checked proof of Fermat’s Last Theorem in Lean. The post frames this as a verification milestone rather than a new mathematical result, and argues that formalization could make large proofs easier to check and review.

## Reading notes

- Fermat’s Last Theorem states that no positive integers a, b, c satisfy aⁿ + bⁿ = cⁿ for any n > 2.
- The first proof, by Andrew Wiles in 1995, took 129 pages and months of verification.
- Formalizing a proof means rewriting it so a computer can check each step automatically.
- Claude produced 13 million lines of Lean and proved 29,500 intermediate theorems.
- The proof follows a simplified version of Wiles’s proof from Darmon, Diamond, and Taylor.
- Human input was limited to occasional high-level guidance from Tianyi Peng.
- The effort succeeded with Prove2Me, which kept a DAG of theorem statements, separated statements from proofs, and helped with search and reuse.
- The finished proof was checked by Lean and uses only Lean’s three standard axioms.
- Kevin Buzzard says the result suggests autoformalization can help check the mathematical corpus and reduce the burden on referees.
- The post says formalized proofs may become common alongside human-readable write-ups.
