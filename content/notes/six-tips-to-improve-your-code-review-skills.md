---
title: "Six tips to improve your code review skills"
date: '2021-03-02T13:43:09-03:00'
category: webclip
summary: 'The article says code review works best when reviewers test changes locally, ask questions instead of making blunt statements, praise good work, label comments, separate blocking from non-blocking issues, and add extra explanation to reduce review rounds.'
tags: ["code-review", "pull-requests", "feedback"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Six tips to improve your code review skills - DEV Community"
    url: "https://dev.to/n_tepluhina/six-tips-to-improve-your-code-review-skills-95a"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-03/dev-to--six-tips-to-improve-your-code-review-skills.md"
    kind: repo
---

The article argues that code review can improve a codebase and align a team’s coding skills, but only when it is used carefully. It warns that reviews can hurt people, create conflict, and slow delivery if they are handled badly.

## Reading notes

- Test the branch locally and inspect the changes, because that supports smoke testing and can reveal architecture issues that are not obvious from reading the diff.
- Ask questions instead of writing blunt judgments, since the author may have a valid reason for the choice.
- Praise specific good practices when they appear, and avoid empty praise.
- Prefix comments with labels such as question, suggestion, or nitpick so the author understands the intent.
- Mark comments as blocking or non-blocking to separate merge blockers from minor preferences.
- Add explanatory comments or even a patch when a change needs more context, so the review can move faster.
