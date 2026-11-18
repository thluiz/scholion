---
title: "Some thoughts on the economics of programming"
date: '2025-08-06T11:02:32+00:00'
category: webclip
summary: 'Argues that huge tech successes stem more from timing and market position than specific processes, and that rising legacy code costs can quietly destroy otherwise profitable software businesses.'
tags: ["software-economics", "legacy-code", "code-quality", "big-tech"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Some thoughts on the economics of programming"
    url: "https://blog.ploeh.dk/2022/10/03/some-thoughts-on-the-economics-of-programming"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-ploeh-dk--economics-of-programming-legacy-code-costs.md"
    kind: repo
---

The text questions the idea that specific development processes or technologies explain Big Tech success, using Microsoft and its little‑remembered Microsoft Solutions Framework as an example. Massive profits come from revenues vastly exceeding costs, often due to market timing and strong products rather than process alone, and correlation between a famous process and success does not imply causation.

It then contrasts Big Tech with typical software companies whose revenues are only modestly higher than costs. For these, rising software development costs, often driven by messy legacy code, can eventually overtake revenue even if the system has historically made money. The author recounts work with a fully digital service company whose stagnant revenue and escalating costs, rooted in a severely degraded legacy code base, preceded its closure. The argument is that relying on past profitability of legacy systems can breed complacency, and that developers have a responsibility to fight codebase decay because increasing costs may become visible to business stakeholders only when the situation is already critical.

## Reading notes

- A story about a highly successful software company is introduced to set up the idea that people tried to copy its "special" development process.
- The company and process are revealed as Microsoft and Microsoft Solutions Framework, which the author believes had little to do with Microsoft's success.
- The text lists fashionable technologies and practices (microservices, monorepos, Kubernetes, DevOps, serverless) to question whether such elements are truly the source of major company success.
- A conceptual chart illustrates a company whose revenue is vastly higher than costs, highlighting that software development costs can be almost negligible relative to profits.
- The author emphasizes that real companies have many non‑software costs and income streams, but uses the simplified chart to focus on net value from software.
- The gap between revenue and cost is defined as profit or net value, which is the real driver of success.
- The text asks whether cost management or specific processes are the main causes of such large profits, and answers that this is unlikely when costs are so small compared to revenue.
- Examples are given: Google outperformed early search engines, Microsoft beat OS/2 and competitors in PC software, Amazon built a large web shop early, Apple shipped accessible GUIs and later launched the iPhone at a fitting time.
- The author notes that these narratives are simplified and acknowledges earlier smartphones like Pocket PC Phone Edition and other precursors.
- Execution quality is recognized as a factor in success, but the author stresses that many competent companies still fail.
- The text argues that timing and circumstances can matter more, and sometimes success may come despite only mediocre execution.
- Readers are warned against confusing correlation with causation when attributing success to processes or technologies used by Big Tech.
- The author urges skepticism about adopting tools or processes solely because large tech companies use them.
- A widely shared quip is cited that treats "legacy" as dismissive engineer jargon for software that actually earns money.
- The author sees this attitude as implying that caring about code quality is frivolous compared to writing revenue‑generating code, and labels this a false dichotomy.
- A second chart depicts a more typical situation where revenue starts at about twice the cost but costs grow faster and eventually surpass revenue.
- The text argues that many software organizations can be sustainably profitable if they find a market and execute well, but rising costs threaten that position.
- For companies with only moderate profit margins, faster‑growing costs can eventually push them into losses even if revenue remains steady.
- The chart is interpreted as showing that historical profitability of a system does not guarantee future profitability when costs keep climbing.
- The author states that if the cost curve is mainly driven by increasing software development expenses, the business is in serious danger.
- A case from the author's consulting experience is described, involving a successful digital service company with many developers and consistent past profits.
- Around the time the author engaged with the company, external market pressure demanded many new features, but developers were stuck in analysis paralysis.
- After helping them move forward, the team discovered the full extent of the legacy codebase problems.
- The CEO is quoted as having been aware they had legacy code but surprised at how severe the situation was.
- In this example, revenue stayed flat while costs rose, contributing to the company eventually shutting down.
- The author concludes that this fully digital business, built entirely on software, was likely undone by its legacy codebase despite a good business idea.
- The conclusion states that software is meant to create value, mainly through profits or savings, and that considering value is a professional concern.
- The text warns against focusing too narrowly on immediate or past value, as this can lead to complacency about legacy systems.
- Legacy code can generate money initially, yet the main risk is that maintenance and change costs keep rising over time.
- The author notes that by the time non‑technical stakeholders notice these growing costs, the situation may already be difficult to correct.
- This leads to the claim that software developers have a responsibility to address messy codebases rather than dismiss quality concerns as elitist.
