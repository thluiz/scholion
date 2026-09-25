---
title: "Testing is software engineering"
date: '2026-09-25T21:33:47+01:00'
category: webclip
summary: 'The page argues that testing is part of engineering, not an afterthought. It says tests improve design, make changes safer, surface hidden requirements, and help teams collaborate.'
tags: ["testing", "software-engineering", "code-design", "collaboration"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Testing is software engineering"
    url: "https://thoughtbot.com/blog/testing-is-software-engineering?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/thoughtbot-com--testing-is-software-engineering.md"
    kind: repo
---

Writing tests is presented as part of engineering work, not as a separate discipline or a task to defer to the end. The page says tests shape code design, support safer changes, and help future developers understand the software.

## Reading notes

- Tests give early feedback on the interface you are building and are easier to address before review or late-stage changes.
- If something is hard to test, the code is often poorly designed, so testability can reveal problems in the implementation.
- A trusted CI checkmark lets you handle dependency updates, refactors, and new features with more confidence.
- Tests make future changes faster because they give feedback sooner than manual checking and are less tedious.
- Writing a test is framed as the right move when you want to be notified if something breaks later.
- Thinking through edge cases and boundary values can uncover hidden requirements in the task.
- Tests can act as living documentation for inputs, returns, and behavior, especially in dynamic languages like Ruby and JavaScript.
- A reliable test suite lets QA or QE teams focus on cases that only humans can test.
- Quality is described as an engineering outcome, and writing good tests is treated as writing clear code.
