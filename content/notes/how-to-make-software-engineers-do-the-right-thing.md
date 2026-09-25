---
title: "How to Make Software Engineers Do the 'Right Thing'"
date: '2026-09-25T09:04:25+01:00'
category: webclip
summary: 'The text proposes priorities for creating a culture of responsibility in engineering teams: logging bugs, doing blameless RCAs, keeping CI green, monitoring logs, and reinforcing continuous improvement.'
tags: ["software-engineering","team-culture","software-quality","ci"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Make Software Engineers Do the 'Right Thing'"
    url: "https://hackernoon.com/how-to-make-software-engineers-do-the-right-thing?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/hackernoon-com--how-to-make-software-engineers-do-the-right-thing.md"
    kind: repo
---

The text argues that teams should build a culture of ownership and accountability so engineers treat quality and stability as priorities, not side work. It says this starts with recording and tracking production bugs, writing blameless RCAs, keeping CI green, and monitoring system health.

It also says these practices need repetition, clear ownership, public alerts, and team-wide responsibility. Over time, the goal is a culture where fixing alerts, broken builds, and bugs is treated as the team’s highest priority.

## Reading notes

- Defends that the foundation is creating a culture of ownership and accountability, and that this needs to start immediately.
- Says teams often do not record or prioritize bugs and defects in production, which makes it hard to discuss trade-offs between quality, stability, and new features.
- Proposes RCAs or incident reports for important issues, with a blameless focus, transparency, learning, and autonomy.
- States that technical debt is at the root of many problems and that RCAs help prioritize fixes and follow-ups over other work.
- Argues that a continuous and green build in CI is essential, and that flaky tests should be excluded until they are fixed, with clear ownership over them.
- Says system health and logs require effort from the whole team, with agreed thresholds, alerts in a public channel, and active response to problems.
- Recommends documenting the principles, running a workshop with the team, aligning with product and stakeholders, and continuously pushing for improvement.
- Lists as next steps improving tests, speeding up builds, reducing handoffs, shifting quality left, collaborating better with product and design, and measuring quality, uptime, and cycle time.
