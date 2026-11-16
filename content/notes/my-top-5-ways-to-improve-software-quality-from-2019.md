---
title: "My Top 5 Ways to Improve Software Quality from 2019"
date: '2026-11-16T08:00:30+00:00'
category: webclip
summary: 'The author highlights five quality practices from 2019: praise preventive work, spend more time on code review, use pinning tests, compare legacy and new code in production, and make technical debt visible to non-developers.'
tags: ["software-quality", "code-review", "technical-debt", "testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "My Top 5 Ways to Improve Software Quality from 2019 - Kill All Defects"
    url: "https://web.archive.org/web/20200314110847id_/https://killalldefects.com/2019/12/31/top-five-takeaways-for-improving-software-quality/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--my-top-5-ways-to-improve-software-quality-from-2019.md"
    kind: repo
---

The post presents five practices the author used in 2019 to improve software quality. It argues that teams should recognize preventive work, invest more time in code review, use pinning tests to preserve behavior, test new code scientifically in production, and explain technical debt in terms that business and product managers can understand.

## Reading notes

- Praise people who take active steps to prevent defects, not only those who fix urgent problems.
- Spend more time on code review to catch more issues, understand changes better, and create teaching moments.
- Use two reviewers per merge request, ideally one more senior and one more junior.
- Ask engineers how they know a commit works and does not create other issues, so they prepare better test plans.
- Use pinning tests to lock current behavior in place, especially for calculation or transformation code.
- Snapshot tests in Jest can serve as a compact form of pinning test, but they should not replace more specific behavioral tests.
- Use Scientist to compare legacy and new implementations in production while keeping users on the legacy result if the new code fails.
- Log errors from the experimental path and remove Scientist only after the new version is reliable.
- Technical debt needs a way to be communicated to product and business management.
- The author suggests discussing debt as a measurable problem with trends, impact, risk, and priorities.
