---
title: "We handed testing to AI. Here is what stayed human."
date: '2026-11-12T12:32:27+00:00'
category: webclip
summary: 'The team used AI to absorb rising QA load as development sped up, tester headcount fell, and review before QA weakened. AI now executes most tests, but humans still decide what to test and make the final verdict.'
tags: ["ai-testing", "qa", "software-delivery"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "We handed testing to AI. Here is what stayed human."
    url: "https://highimpactengineering.substack.com/p/we-handed-testing-to-ai-here-is-what"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/highimpactengineering-substack-com--we-handed-testing-to-ai-here-is-what-stayed-human.md"
    kind: repo
---

The article describes a QA bottleneck that grew as coding sped up. With more tickets, fewer testers, and less peer review before QA, the team had to use AI to keep validation moving.

The setup shifts execution to an agent, but leaves planning and judgment with people. The QA engineer picks what to test, reviews evidence, asks for more scenarios, and keeps the final call. The author says this has helped, but does not see it as sustainable without better systems around QA.

## Reading notes

- Manual validation became the new bottleneck as code generation and ticket throughput increased.
- The same team delivered more tickets after switching from Cursor to Claude, while PRs merged per month roughly doubled.
- QA headcount fell from 2.5 people to 2.
- A larger share of PRs reached QA without another developer review.
- A QA engineer built a Claude-based toolkit that sorts the queue, maps affected areas, runs tests, and proposes how to spend the session.
- The QA engineer decides what to test and keeps the final verdict.
- The agent checks acceptance criteria through the cheapest available evidence first and only then uses the browser.
- The setup asks what would falsify each claim and probes edge cases.
- The agent does about 75–85% of hands-on test execution on a ticket, but it cannot move work to Done or file bugs without approval.
- Fully automated testing of low-risk tickets has not happened yet.
- Shift-left requirement testing has been abandoned because the team is too busy.
- Bugs found and fixed rose sharply in September and October.
- The author expects QA to become more about building quality systems around agents than about adding more testers.
