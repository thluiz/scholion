---
title: "Communicating Technical Debt"
date: '2026-11-16T01:59:30+00:00'
category: webclip
summary: 'The post explains technical debt with a debt-and-interest analogy, then shows how to discuss it with business stakeholders using trust, data, metrics, and a concrete remediation plan.'
tags: ["technical-debt", "software-quality", "business-stakeholders"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Communicating Technical Debt"
    url: "https://dev.to/integerman/communicating-technical-debt-3gbd"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--communicating-technical-debt.md"
    kind: repo
---

The post frames technical debt as an obligation that saves time up front but creates ongoing costs in time, quality, risk, performance, security, and morale. It argues that business stakeholders need this translated into metrics and concrete consequences they can evaluate.

## Reading notes

- Technical debt is defined as taking temporary advantage of something while taking on an obligation to pay it back.
- The principal is the time saved during initial implementation, and the interest is the extra time, quality, and risk cost paid until the debt is resolved.
- Technical debt can help in the short term, but it can become harmful over time.
- The author lists penalties such as increased development time, quality debt, poor application performance, security vulnerabilities, and lower morale.
- Product management and business stakeholders are presented as partners, not adversaries, and conversations about code need trust, respect, and collaboration.
- To talk with business stakeholders, the author recommends improving mutual understanding, maintaining professionalism, using both data and anecdotal evidence, identifying top-priority debt items, and having flexible plans and time estimates.
- The post says technical debt is not always the developer's fault and uses farming and soil depletion as an analogy for repeated work without time to recover.
- Sometimes business can accept long-term damage when short-term delivery matters more, such as when a product must be finished or later replaced.
- The author recommends using metrics from issue tracking, time tracking, source control, code analysis, test coverage, CI/CD, and performance monitoring.
- Useful figures include defects by area, time to complete a feature, time spent on development versus support, unit test coverage over time, code smells, and incoming errors.
- The author recommends code analysis tools such as SonarQube, SonarCloud, and NDepend to prioritize and visualize problem areas.
- Communication should match the scale of the issue, from a short email to a report or slide deck.
- The message should stay concise, fit the audience's communication style, and present a remedy plan with expected resources, timing, and risks.
