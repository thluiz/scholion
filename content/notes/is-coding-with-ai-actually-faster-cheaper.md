---
title: "Is Coding with AI Actually Faster and Cheaper?"
date: '2026-11-23T18:47:03+00:00'
category: webclip
summary: 'Article reviews recent studies on AI coding agents, showing higher coding activity and some task-level speedups, unclear total cost savings, and strong influence of agent capability over token price.'
tags: ["ai-coding", "software-development-productivity", "developer-tools", "economics-of-ai"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Is Coding with AI Actually Faster and Cheaper?"
    url: "https://dev.to/sylwia-lask/is-coding-with-ai-actually-faster-and-cheaper-2810"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--is-coding-with-ai-actually-faster-cheaper.md"
    kind: repo
---

The article examines empirical research on how AI coding agents affect software development speed and cost. Large-scale GitHub data shows big increases in coding activity and smaller gains in releases, with no clear rise in app usage. Experimental and observational studies find modest productivity improvements on tasks, though results vary and expectations often exceed measured gains. Research on cost suggests that time saved in implementation can be offset by auditing and verification, and that the capability of AI agents tends to matter more economically than raw token prices.

## Reading notes

- The author’s personal impression is that AI speeds up writing code and can make work less stressful, but has not dramatically accelerated the whole delivery process in large, established systems.
- MIT and Wharton economists analyzed data from over 500,000 GitHub developers, finding about +240% coding activity (commits), +30% software releases, and no overall increase in marketplace app usage associated with autonomous coding agents.
- The gap between the surge in commits and the smaller rise in releases suggests that more coding does not automatically translate into proportionally more shipped software.
- The author notes growing complexity around AI security, observing that organizational focus on security has increased and contributes to the overall workload.
- Multiple studies report mixed but generally positive productivity effects for individual developers using AI assistance, with no evidence of “10x developers” across the board.
- Cui et al. (Management Science, 2026) report a 26.08% increase in the number of completed tasks when using AI assistance.
- A METR study from July 2025 found developers were 19% slower with AI for the measured tasks, contradicting their expectation that AI would make them 24% faster.
- Despite being slower in METR’s experiment, participants still believed after the study that AI had sped them up, illustrating a mismatch between perceived and measured productivity.
- METR’s February 2026 update suggests newer tools are likely more helpful, but the follow-up could not reliably quantify speedups because of participant selection.
- A Science paper (January 2026) estimated a 3.6% increase in quarterly coding activity on GitHub associated with AI.
- Borg et al. (June 2026) observed a median 30.7% reduction in implementation time in their observational phase when AI was involved.
- The author concludes that several studies indicate real gains on specific tasks, but these are far from the dramatic productivity multipliers sometimes claimed.
- Regarding overall cost, DORA’s 2025 research and a March 2026 follow-up suggest that time saved on implementation is often reallocated to auditing and verifying AI-generated code.
- DORA’s findings imply that while the distribution of work across the pipeline can change, the net effect on total cost of software delivery remains uncertain.
- The author expresses skepticism about fully autonomous multi-agent pipelines (AI coding, reviewing, and testing) for mission-critical domains such as financial software.
- On token costs, the author initially expected that savings from faster coding would be eaten by model usage, especially when using expensive models indiscriminately.
- Potluri et al. (September 2026) and Steffen Herbold (October 2026) both conclude that the effectiveness of AI agents can outweigh token price in determining economic outcomes.
- Potluri’s analysis indicates that highly capable models that solve more tasks can generate substantial estimated savings, whereas less capable, cheaper models can become expensive when frequent failures force repeated attempts.
- Herbold simulated 432 scenarios combining developers and AI agents, taking into account salaries, token costs, supervision needs, bugs, and technical debt.
- In Herbold’s simulations, teams with highly capable agents were usually cheaper than teams without AI, while results with less capable agents were mixed.
- Herbold’s work suggests agent capability drives costs more than token price because better performance reduces the burden of checking and fixing AI-generated work.
- Both Potluri and Herbold rely on benchmarks, economic modeling, and simulations, so their results indicate conditions under which savings can exceed token costs rather than directly measuring real-world commercial projects.
- Overall, the available evidence supports the idea that AI can make coding faster and potentially cheaper at the task level, but there is still limited proof that the total cost of building, delivering, securing, and maintaining software has fallen across the industry.
- The author invites readers to compare these findings with their own experience and share whether AI has genuinely made their teams faster and cheaper.
