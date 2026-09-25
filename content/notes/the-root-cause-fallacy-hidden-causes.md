---
title: "The Root Cause Fallacy: Hidden Causes"
date: '2026-09-25T20:31:55+01:00'
category: webclip
summary: 'The article argues that failures in complex systems rarely have one root cause. Five Whys can help, but it should be used to identify several contributing causes and weigh their impact.'
tags: ["root-cause-analysis", "five-whys", "complex-systems", "causality"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Root Cause Fallacy: Hidden Causes"
    url: "https://read.perspectiveship.com/p/the-root-cause-fallacy?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/read-perspectiveship-com--the-root-cause-fallacy-hidden-causes.md"
    kind: repo
---

The article argues that looking for a single root cause in a complex failure is too simple. In the example of a 3 AM database crash, the outage came from several contributing factors, and the useful response is to examine how each one helped cause the failure.

Five Whys can still be a starting point, but the author says it should not stop at one answer. The better approach is to think in terms of multiple causes, rate their contribution, and fix the highest-impact problems first.

## Reading notes

- The system crash example shows that the database running out of memory was only one part of the failure.
- Monitoring failed to alert developers, which meant the problem was not caught early.
- The scaling policy did not work, so overflow was not prevented.
- The query was not optimised and sped up memory use.
- The article says complex systems rarely fail for a single reason.
- Five Whys asks for one answer at each step, which fits the brain’s preference for simplicity but can miss the full picture.
- The author suggests inversion as a way to think about success, since success also comes from multiple contributing factors.
- The practical advice is to weigh causes by contribution and fix based on impact.
