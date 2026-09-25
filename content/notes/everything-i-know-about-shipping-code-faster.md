---
title: "Everything I Know About Shipping Code Faster"
date: '2026-09-25T21:56:02+01:00'
category: webclip
summary: 'The post argues that shipping faster comes from finding code paths quickly, keeping diffs small, testing in batches, reducing reviewer friction, and protecting focus from interruptions.'
tags: ["software-engineering", "code-review", "productivity", "workflow"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Everything I Know About Shipping Code Faster"
    url: "https://www.developing.dev/p/everything-i-know-about-shipping?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/developing-dev--everything-i-know-about-shipping-code-faster.md"
    kind: repo
---

The post says faster shipping starts before writing code, by finding the right place to change things quickly. It then treats small diffs, faster testing, smoother review, and fewer interruptions as the main ways to land working code sooner.

## Reading notes

- Be fluent in code search so you can find where to make changes in minutes instead of reading unfamiliar code for hours.
- Know who knows what in large codebases, by asking around or checking git blame, and use that to get up to speed faster.
- Learn how to query data yourself so you do not wait on other people for simple answers.
- Write smaller, focused diffs because larger changes take longer to write, test, review, merge, and are less likely to catch bugs.
- Batch related test plans so you can test a stack of commits once instead of paying the testing cost for each change.
- Use feature flags to gate changes while you work, then verify the release on a small population when you turn the flag on.
- Reuse existing test plans from git blame when you are working in unfamiliar code paths.
- Make review easier by pointing out what to scrutinize, adding relevant context, and using clear diff titles.
- Aim to get code approved on the first review by preempting feedback, testing thoroughly, and discussing ambiguous parts in advance.
- Use clear descriptions for code changes so other people can understand what you are doing and why.
- Protect deep focus by using noise-canceling headphones, clustering meetings, working when interruptions are lower, and reducing notifications.
- Audit your workflow for slow steps like builds, tests, and queries, then build tools that remove those bottlenecks.
- Fill waiting time with small tasks like cleanup, replying to pings, or querying data instead of sitting idle.
- The author ties these habits to extra time for growth and says he also worked more hours than average.
