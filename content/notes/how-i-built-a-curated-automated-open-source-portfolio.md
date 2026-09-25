---
title: "How I Built a Curated, Automated Open Source Portfolio"
date: '2025-10-22T11:20:11+01:00'
category: webclip
summary: 'The author describes building an automated open source portfolio because manual tracking became stale. The system uses a Node.js script and GitHub Actions to collect only selected contributions under strict filters.'
tags: ["open-source", "github-actions", "nodejs", "automation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How I Built a Curated, Automated Open Source Portfolio - DEV Community"
    url: "https://dev.to/adiatiayu/how-i-built-a-curated-automated-open-source-portfolio-18o0?"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-10/dev-to--how-i-built-a-curated-automated-open-source-portfolio.md"
    kind: repo
---

The author explains why manual contribution tracking failed and how that led to a curated portfolio built to track open source work automatically. The portfolio is designed to capture progress, milestones, and shareable contribution history while avoiding stale spreadsheets and abandoned tools.

## Reading notes

- Manual tracking through a Google Sheet or a dedicated GitHub repository became outdated and unusable over time.
- The portfolio is meant to record progress and present contributions to potential collaborators or employers.
- The author decided to automate the process with the GitHub API after the idea came up during a family vacation.
- The project was built on a phone using a smartphone, the GitHub mobile app, a mobile browser, and Gemini 2.5 Flash.
- The portfolio follows four filters: only activity outside personal repositories, no private repositories, no bot-authored routine PRs, and a separate category for collaborations.
- Collaborations include comments on issues or PRs where the author discussed, helped, or explained something without submitting a formal review.
- The system uses a Node.js script to fetch GitHub activity and applies smart syncing with both incremental updates and full synchronizations.
- GitHub Actions runs daily incremental updates and monthly full syncs, then commits the generated Markdown reports back to the repository.
- The final output is a set of quarterly Markdown reports with statistics and top contributed projects.
- The author says the main lesson from vibe coding is that the human still has to be the architect and the critical reviewer of AI-generated code.
- The author plans to keep refining the logic and checking that the code remains simple, efficient, and aligned with the portfolio’s ethical rules.
