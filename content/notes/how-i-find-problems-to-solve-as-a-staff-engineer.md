---
title: "How I Find Problems to Solve as a Staff Engineer"
date: '2026-09-23T18:06:33+01:00'
category: webclip
summary: 'Lalit Maganti says staff engineers find useful problems by absorbing day-to-day complaints, waiting for evidence to accumulate, and pressure-testing common shapes before building anything.'
tags: ["staff-engineering", "problem-finding", "product-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How I Find Problems to Solve as a Staff Engineer - Lalit Maganti"
    url: "https://lalitm.com/post/find-problems-staff-engineer/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/lalitm-com--how-i-find-problems-to-solve-as-a-staff-engineer.md"
    kind: repo
---

Lalit Maganti describes problem-finding as an ongoing habit rather than a separate strategic exercise. He listens to the complaints and requests that surface in everyday work, follows them until the underlying need becomes clear, and looks for patterns that connect several cases into one larger problem.

He also argues for patience. A request that sounds urgent once may fade, repeat in other teams, or reveal a different shape after more evidence appears. Before building, he tests whether the idea is real, useful, and worth the effort, sometimes with a prototype or RFC, and is willing to stop, park the work, or let someone else implement it.

## Reading notes

- He finds problems by absorbing the stream of day-to-day noise instead of trying to think strategically at a blank page.
- He listens to how people describe what slows them down, then keeps digging until he understands the root issue rather than the requested solution.
- He watches team workflows and bugs firsthand when a problem seems worth exploring.
- He talks with people who have a broader view of the organization so he can spot patterns earlier.
- He avoids moving too fast because a request from an eager team can turn out to be less important than it first appeared.
- He lets unresolved problems accumulate so the same issue can appear in more than one place and become easier to prioritize.
- He looks for the common shape behind several requests, such as the need to personalize Perfetto without forcing one workflow on everyone.
- He treats a common shape as a hypothesis, not proof, and checks it before committing.
- He uses prototypes, RFCs, conversations, and talks to pressure-test ideas before building.
- He is willing to stop, delay, or split an idea when the evidence shows it needs a different solution.
- He says finding and shaping the right problem can matter even when he does not personally implement the solution.
- He sees the process as a loop: solving useful problems leads other people to bring him into related conversations earlier.
