---
title: "12 Hard Truths About Coding I Learned the Hard Way After 10+ Years"
date: "2026-09-23T13:49:10+01:00"
category: webclip
has_commentary: false
summary: "Twelve lessons from a decade of coding: estimates are guesses, seniority means more meetings, and almost every failed project traces back to a communication problem."
tags:
  - software-engineering
  - career
  - communication
sources:
  - title: "12 Hard Truths About Coding I Learned the Hard Way After 10+ Years - DEV Community"
    url: "https://dev.to/canro91/12-hard-truths-about-coding-i-learned-the-hard-way-after-10-years-124j?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-06/dev-to--12-hard-truths-about-coding.md"
    kind: repo
---

The author got fired from a first job, took down a database with a bad query, and got rejected by a FAANG. In the post, he frames most of the twelve lessons that followed as failures of communication.

## Reading notes

- Estimates are guesses. The problem shows up when your guess doesn't overlap with everyone else's guess.
- Splitting a four-day task into smaller pieces shows progress; grinding on the whole thing in silence doesn't.
- A quick pull request demonstrating an idea beats a long document nobody reads.
- Coding is the smallest part of shipping. Deployment, testing, adoption, support, and follow-up come after.
- Seniority trades coding time for meetings: 1-on-1s, retrospectives, sprint planning, poker estimation. A good day leaves 1-2 hours of uninterrupted coding.
- Working on legacy code is what teaches people to value tests, whatever the flavor (unit, integration, TDD, BDD).
- Refactoring nobody asked for should either become part of an estimated task or get put explicitly on the sprint plan.
- Debates over frameworks and tools (Entity Framework vs. stored procedures, this or that "best practice") waste time that tools don't deserve.
- Code style and best practices should be automated. That's work for a machine.
- Projects fail from communication problems more than from tooling choices, even on projects using the newest stack.
- A production database got deleted once from using the wrong settings file in the wrong environment, because nobody had asked, nobody had told, and no guardrail existed in the code.
- Premature optimization and plain laziness get lumped together under the same advice against writing just-in-case code for a problem that hasn't happened yet.
