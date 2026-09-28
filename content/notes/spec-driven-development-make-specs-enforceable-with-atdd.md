---
title: "Spec-Driven Development: Make Specs Enforceable with ATDD"
date: '2026-09-28T14:33:42+01:00'
category: webclip
summary: 'The page argues that Markdown specs alone do not enforce behavior. Acceptance tests, especially in ATDD, combine specification and verification so code must satisfy the expected outcome.'
tags: ["spec-driven-development", "atdd", "acceptance-tests", "ai-agents"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Spec-Driven Development: Make Specs Enforceable with ATDD"
    url: "https://journal.optivem.com/p/spec-driven-development-make-specs"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/journal-optivem-com--spec-driven-development-make-specs-enforceable-with-atdd.md"
    kind: repo
---

The page says current “spec-driven development” tools rely on Markdown specs that agents can ignore, while acceptance tests make the spec enforceable because they fail until the system satisfies them. It places ATDD in that role and describes the Red step as the point where the test is written before system code exists.

## Reading notes

- Spec-driven development tools such as Kiro, GitHub’s spec-kit, and Tessl use Markdown documents as specs, but the code is not checked against them.
- Birgitta Böckeler is cited as finding that agents do not always follow the instructions in those specs.
- The problem is framed as a Markdown file that cannot be run against the code, so a person must inspect the code manually.
- The page contrasts this with acceptance tests, which have existed since Extreme Programming and were described again in Continuous Delivery.
- An acceptance test is presented as both the spec and the check, because it describes the required behavior and fails until the behavior exists.
- The text says an agent can ignore a Markdown file, but it cannot ignore a test that does not pass.
- Acceptance tests are described as using a DSL, with system drivers talking to the UI or API and external-system drivers talking to dependent systems such as an ERP.
- In ATDD, the Red step is where the test is written before any system code exists.
- When an AI agent does the work, the Red step is split into four small steps and a human reviews each one.
- In the example, an online order starts with agreed acceptance criteria, including calculating base price from unit price and quantity.
- The test is written in the DSL vocabulary, using `placeOrder().withQuantity(...)`.
