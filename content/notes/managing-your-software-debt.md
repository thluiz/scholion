---
title: "Managing your Software Debt"
date: '2016-04-11T10:57:21-03:00'
category: webclip
summary: 'The page groups software debt into technical, competence, and quality debt, and says maintenance costs, developer morale, and defect fixing get worse as debt grows. It points to pairing, refactoring, and agile practices as ways to reduce it.'
tags: ["technical-debt", "competence-debt", "quality-debt", "software-maintenance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Managing your Software Debt"
    url: "http://www.infoq.com/news/2014/03/managing-software-debt?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/infoq-com--managing-your-software-debt.md"
    kind: repo
---

Software debt appears in several forms. The page treats technical debt as the most familiar case, but it also adds competence debt and quality debt. It says these debts raise maintenance costs, depress developers, and can make organizations think about replacing a system.

## Reading notes

- Competence debt is the gap between what is in the codebase and how much of it the team understands.
- Competence debt grows over time, and it grows faster when a codebase stops changing.
- Pair programming can reduce both technical debt and competence debt by widening the areas each team member knows.
- Refactoring also helps with competence debt because changing a system reveals whether it is truly understood.
- When too few original developers remain, teams may believe the old system is impossible to maintain.
- Separate maintenance teams can increase technical and competence debt when domain knowledge and project backstory are lost.
- Sloppy or confusing code can push developers away and lower reuse across the codebase.
- Quality debt measures the effort needed to fix defects that exist in a software product at a given time.
- Technical debt concerns internal quality, while quality debt concerns the external quality that users see and experience.
- Quality debt gets harder to pay down as it ages, and unresolved defects can make later fixes harder.
- Suggested practices include Definition of Done, BDD or automated acceptance testing, continuous integration, automated testing, and not tolerating broken windows.
