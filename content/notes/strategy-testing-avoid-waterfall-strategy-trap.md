---
title: "Strategy testing: avoid the waterfall strategy trap with iterative refinement"
date: '2026-09-25T17:17:01+01:00'
category: webclip
summary: 'The chapter argues that strategy testing should happen before rollout, on a narrow slice, to refine details, track real impact, and avoid a waterfall approach that hides whether the strategy works.'
tags: ["strategy-testing", "iterative-refinement", "engineering-strategy", "rollout"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Strategy testing: avoid the waterfall strategy trap with iterative refinement."
    url: "https://lethain.com/testing-strategy-iterative-refinement/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/lethain-com--strategy-testing-avoid-waterfall-strategy-trap.md"
    kind: repo
---

The chapter says strategy testing should happen before rollout, usually in the early development stage, so you can see whether the strategy will achieve its goal at an acceptable cost. It argues that narrow testing helps refine the details that often cause reasonable strategies to fail, especially when pressure is applied too early.

## Reading notes

- Test the strategy before finalizing it, and focus on the narrowest, deepest slice that can show whether the approach works.
- Use metrics that measure impact, not adoption, such as reduced customer impact or improved traffic.
- Treat failure as a sign of friction or poor ergonomics, not a default resistance to change.
- Keep refining until you have confidence in the details or know the strategy needs a different direction.
- Separate the roles of sponsor and guide when testing requires coordination and escalation.
- The sponsor should unblock decisions, push through old beliefs, marshal support, tell the story to stakeholders, prevent strategy overload, keep pace, and notice when the phase should change.
- The guide should translate the strategy into concrete tests, find blockers, escalate often, track goals and workstreams, and maintain pace.
- The sponsor must be authorized to decide and must respond quickly to escalations.
- The guide must be able to work at pace with good judgment and without being derailed by organizational friction.
- The testing phase needs a weekly meeting with sponsor, guide, and key contributors.
- Those meetings should be debugging-heavy and presentation-light, with progress tracked through learning and decisions that change the test.
- Strategies that skip testing often sound right but do not produce results.
- A strategy that only creates pressure without a concrete plan is a common failure pattern.
- Identify whether the strategy is moving real numbers and whether there is a clear way to debug and recover when it is not.
- If a strategy has skipped testing and is struggling, pause it, write a new strategy, and make sure the new one is tested.
- If an official pause is hard, use an indirect pause to create room for testing without forcing a public defeat.
- Testing exposes missing details that turn a directionally correct strategy into one that works.
