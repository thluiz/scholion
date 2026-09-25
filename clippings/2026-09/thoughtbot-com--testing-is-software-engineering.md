---
url: "https://thoughtbot.com/blog/testing-is-software-engineering?ref=dailydev"
captured_at: "2026-09-25T21:33:47+01:00"
title: "Testing is software engineering"
domain: "thoughtbot-com"
---

In software development, testing is often an afterthought. It’s something we get to if there’s time, or that we can put off on a QA team. But writing tests isn’t a separate discipline from engineering—it **is** engineering. Tests shape the design of your code, allow you to change it with confidence, and influence how future developers understand it. Thinking about tests as a first-class part development will make your job more like engineering and less like guesswork.

## [Tests improve code design](#tests-improve-code-design)

Writing tests is often your first opportunity to consider how the interface you’re building will look and feel from an external perspective. You lose that feedback if you write tests late, or rely on AI to generate them after the fact. It’s much easier to address that feedback early on than to get it from a colleague in PR review.

You don’t have to go full TDD, but the earlier you start writing tests, the better. If you’re not sure how to test something, listen to that feedback, and see if you can adjust your implementation to make it easier for you to test. Remember, **code that is hard to test is often code that is poorly designed.**

## [Tests give you confidence to change code](#tests-give-you-confidence-to-change-code)

Being able to trust the little green checkmark you get from CI is very [empowering](https://thoughtbot.com/blog/unlock-the-value-of-tests-in-understanding-your-codebase). You can more easily stay on top of dependency updates, make refactors, and build new features on top of existing work. Not being able to trust CI makes all those things harder—and thus your daily work more of a grind.

But even before you open a PR, having your key behaviors well tested enables you to make refactors and optimizations, while being assured that you haven’t broken anything. A test will give you feedback much faster than manually exercising your code—and is much less tedious—allowing you to iterate faster.

I think about it like this: **If I’d like to be notified if I break this in the future, I should write a test for it.**

## [Tests facilitate collaboration](#tests-facilitate-collaboration)

Thinking through [edge cases](https://thoughtbot.com/blog/testing-your-edge-cases) and [boundary values](https://thoughtbot.com/blog/debugging-at-the-boundaries) will often uncover hidden requirements in your task. What happens when a value is `nil`, or when the user clicks the back button, or when the API you’re calling is down? It’s possible that the tech lead or PM who wrote your ticket didn’t think of every possibility. Often **there’s a lot of work to be done to account for all the other paths aside from the happy one**. The earlier you start uncovering those requirements, the earlier on you can raise blockers, push back, or change course.

Especially in dynamic languages like Ruby and JavaScript, tests can serve as living documentation for how your interface behaves. If tests are written for humans to read, they can give you information about the return and input types much more quickly than if you had to read the implementation. They enable [cognitive compression](https://en.wikipedia.org/wiki/Chunking_\(psychology\)) by allowing you to only concern yourself with what something does, not how it does it.

And if your company has a dedicated QA or QE team, having a test suite you can trust will enable them to focus on more important things, like testing things which only humans can test.

## [Quality is an engineering outcome](#quality-is-an-engineering-outcome)

Quality isn’t something we tack on at the end. It’s not something we outsource. It’s a key part of software engineering. By taking testing seriously, and integrating it early on in your development process, you’ll design better software, be able to make changes with less stress, and uncover hidden requirements before they’re blockers. Much like how writing is thinking—[and writing well is thinking clearly](https://www.goodreads.com/quotes/320581-writing-is-thinking-to-write-well-is-to-think-clearly)—writing tests is thinking about your code, and **writing good tests is writing clear code.**
