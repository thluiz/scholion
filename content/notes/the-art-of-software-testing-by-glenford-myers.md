---
title: "The Art of Software Testing by Glenford Myers"
date: '2020-08-26T19:31:12+00:00'
category: webclip
summary: 'Yegor Bugayenko says the book remains a key reference in software testing, mainly because Chapter 2 reframes testing as finding errors and sets a completion criterion based on detecting a predefined number of bugs.'
tags: ["software-testing", "glenford-myers", "test-completion-criteria"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Art of Software Testing by Glenford Myers"
    url: "https://yegor256.com/2014/08/22/art-of-software-testing.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--the-art-of-software-testing-by-glenford-myers.md"
    kind: repo
---

The article treats *The Art of Software Testing* as an important but partly outdated book. It says most chapters can be skimmed, while Chapter 2 carries the core ideas that still matter for testing and software engineering.

## Reading notes

- The book has three editions, and the author considers it one of the top books in software testing despite some outdated content.
- Most of the eleven chapters are not worth close reading because their material is either covered better elsewhere or is too dated.
- Chapter 3 has an eleven-page checklist for code reviewers, but it is not comprehensive and is no match for *Code Complete*.
- Chapter 5 covers unit testing, but the article says *Growing Object-Oriented Software, Guided by Tests* is a better source today.
- The book’s most valuable part is Chapter 2, which focuses on the psychology of testing.
- Myers argues that testing is meant to find errors, not to demonstrate that software works correctly.
- The article highlights two linked ideas: testing aims to execute a program with the intent of finding errors, and a test case fails when it produces correct results without finding any errors.
- The author says these ideas should change how testers approach their work, pushing them to try to break software rather than confirm it.
- Myers also says a program cannot be tested into being error-free and that finding all errors is impractical or impossible.
- For test completion, the article favors using detection of a predefined number of errors as the stopping criterion.
- It says this idea can work in real projects, even if teams often resist it at first.
- The article closes by treating Chapter 2 as the foundation of the book and saying the software testing industry still works against those principles.
