---
title: "How to Kill the Code Review"
date: '2026-09-25T22:27:45+01:00'
category: webclip
summary: 'The essay argues that manual code review no longer scales with AI-generated code, and that human approval should move upstream to specs, constraints, and deterministic verification.'
tags: ["code-review", "ai-engineering", "bdd", "verification"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Kill the Code Review"
    url: "https://www.latent.space/p/reviews-dead?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/latent-space--how-to-kill-the-code-review.md"
    kind: repo
---

The piece argues that manual code review has become too slow for the volume and size of changes produced in AI-heavy teams. Instead of reading diffs after the fact, humans should define specs, constraints, and acceptance criteria before code is generated, then rely on deterministic verification.

## Reading notes

- Manual code review does not scale with the current pace of software changes, especially when AI increases both output and review burden.
- Code review is described as a historical approval gate that no longer fits the way software is built.
- The useful human checkpoint should move upstream to specs, plans, constraints, and acceptance criteria.
- Specs become the source of truth, and code becomes an artifact of the spec.
- Humans should review the contract the code must fulfill, not 500-line diffs.
- Verification should be deterministic through tests, type checks, contract checks, linters, and pass/fail artifacts.
- Verification criteria should be defined before code is written, not invented afterward.
- Behavior-driven development becomes more relevant because the spec is the primary artifact when agents write the code.
- Agents should work within narrow scopes, with escalation for sensitive changes such as auth logic, schema changes, or new dependencies.
- Coding and verification should be separated, with one agent producing code and another verifying it.
- The intended direction is to ship fast, observe everything, and revert faster.
