---
title: "The Future Of Software Engineering with Anthropic"
date: '2026-09-25T21:50:01+01:00'
category: webclip
summary: 'Roundtable on how AI is changing software engineering: closed-loop development, test-first workflows, evolving code review, long-horizon agents, and the limits of adoption in regulated settings.'
tags: ["software-engineering", "ai-coding", "anthropic", "developer-tools"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Future Of Software Engineering with Anthropic"
    url: "https://www.akashbajwa.co/p/the-future-of-software-engineering"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/akashbajwa-co--future-of-software-engineering-with-anthropic.md"
    kind: repo
---

The roundtable focuses on how AI is reshaping software engineering through Claude Code, closed-loop development, and a shift toward test-first work. Participants describe agents handling bug triage, PR generation, comments, review, and internal tooling, while human work moves toward planning, verification, and steering.

The discussion also centers on what still blocks wider use: long-horizon tasks, context management, permissioning, sandboxing, and regulated deployment. The room sees coding tools as the first area of displacement, while business software remains harder to replace.

## Reading notes

- Claude Code started as a rough terminal UI in late 2024 and grew organically by showing value.
- Closed-loop workflows matter because agents can triage bugs, check evals, and open fix PRs with little human touch.
- Test cases are increasingly defined first, then agents build against them.
- Teams use two layers of evals: regression evals on every PR and frontier evals for new capabilities.
- Forced adoption is discouraged; competitions and hackathons are preferred over top-down mandates.
- Human code review is changing as AI review layers get stronger and quick approvals become common.
- Comments are being kept more often because later agent sessions can use them.
- Higher review standards still apply to destructive actions and core infrastructure.
- Long-running agent tasks remain hard to observe and control.
- Sandboxing is coming back as remote coding agents and sandbox-per-session setups become more practical.
- Human-authored context files help, while stale or agent-generated context can hurt.
- Hiring is increasingly about willingness to experiment at the bleeding edge and knowing model limits.
- Internal tools for incident management, auth, project tracking, and small utilities are being replaced first.
- Business-facing software is stickier because compelling AI-native replacements are still scarce.
- AI makes prioritization harder because more internal rebuilds now feel feasible.
- Good code now has to be readable for both humans and AI.
- The group expects more asynchronous background agents that can run for hours or days.
- Regulated workflows still depend on human-in-the-loop products rather than autonomous agents.
- The main bottlenecks are permissioning, sandboxing, context, and deployment rather than raw model capability.
