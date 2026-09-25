---
title: "AI Writes Code Faster. Your Job Is Still to Prove It Works."
date: "2026-09-23T17:30:44+01:00"
category: webclip
has_commentary: false
summary: "Osmani's framework for code review after AI: solo devs lean on tests as a safety net, teams need a PR Contract stating intent, proof, risk, and where to focus review."
tags:
  - code-review
  - ai-coding
  - software-engineering
  - pull-requests
sources:
  - title: "AI writes code faster. Your job is still to prove it works. | AddyOsmani.com"
    url: "https://addyosmani.com/blog/code-review-ai/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/addyosmani-com--ai-writes-code-faster-your-job-is-still-to-prove-it-works.md"
    kind: repo
---

Addy Osmani argues AI didn't eliminate code review. It made the burden of proof explicit. Solo developers ship at inference speed, trusting automated tests as the safety net and reviewing only the parts that matter. Teams still require a human sign-off, because review is also how they transfer context and assign accountability for a change someone else may have to debug later.

His core framework is the PR Contract: state intent, show proof it works, name the risk tier and which parts AI generated, and flag where review attention should go. Without that, a pull request doesn't ship faster. It just moves the work downstream to whoever reviews it.

## Reading notes

- By early 2026, over 30% of senior developers report shipping mostly AI-generated code, and logic errors show up about 75% more often in that code.
- Solo devs "trust the vibe": review only the key parts, and lean on automated tests (often targeting >70% coverage) as the real backstop.
- The PR Contract has four parts: what/why in 1-2 sentences, proof it works (tests passed, manual steps, screenshots, or logs), risk tier plus which parts were AI-generated, and 1-2 areas where the author wants human focus.
- Team metrics move together as AI adoption rises: PRs run about 18% larger, incidents per PR are up about 24%, and change failure rates are up about 30%.
- Security stays non-negotiable for human review: about 45% of AI-generated code carries security flaws, with logic errors at 1.75x and XSS vulnerabilities at 2.74x the rate of human-written code.
- The OCaml maintainers rejected a 13,000-line AI-generated pull request: nobody had the bandwidth to review a change that size, regardless of code quality.
- Well-configured AI reviewers catch 70-80% of low-hanging issues, freeing humans for architecture and business logic; badly configured ones just produce "text noise" developers learn to ignore.
