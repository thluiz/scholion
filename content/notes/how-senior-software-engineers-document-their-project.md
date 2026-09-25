---
title: "How Senior Software Engineers Document Their Project"
date: '2026-09-25T00:25:18+01:00'
category: webclip
summary: 'The article argues that ADRs help teams record architectural changes, their impact, and what was learned, so future developers can understand decisions and avoid relying on memory.'
tags: ["software-documentation","adr","architecture","team-process"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How Senior Software Engineers Document Their Project"
    url: "https://dev.to/koladev/how-senior-software-engineers-document-their-project-1nf4?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--how-senior-software-engineers-document-their-project.md"
    kind: repo
---

The article says software engineers often dislike documentation, but documenting project decisions is what helps teams remember why an architecture was chosen. It presents ADRs, or Architectural Decision Records, as a way to track changes, impacts, and lessons learned.

It also says ADRs can live in a repository, Notion, or JIRA, and that linking changes to issues can help teams remember technical decisions months or years later.

## Reading notes

- The text argues that documenting architecture decisions helps because memory fails over time.
- ADR means Architectural Decision Record and serves to record the change made, its impact, and what was learned.
- The author compares the ADR to a personal diary, but used by the team.
- The text says that documenting changes helps other developers understand why a choice was made, including those who join the project later.
- The author describes a fintech project in which the team moved fast and did not prioritize scalability planning.
- He says that, in researching, he found ADR as a documentation convention that he liked.
- The text shows an ADR template with context, problem, decision factors, options considered, decision outcome, consequences, confirmation, pros and cons, and more information.
- It also states that this type of document can be kept in the project repository, in Notion, or in JIRA.
- The author reports that, at the previous company, they used GitLab issues and linked each change to a branch to track the reasons for the changes.
- The conclusion of the text reinforces that ADRs help team leaders, colleagues, and people who arrive later understand past technical decisions.
