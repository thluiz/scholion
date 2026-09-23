---
title: "We Need to Talk About Technical Debt"
date: "2026-09-23T17:29:31+01:00"
category: webclip
has_commentary: false
summary: "Argues technical debt and bad code are not the same thing: debt is a deliberate, repayable trade-off, bad code is a skills gap. Unpaid debt compounds into a rewrite."
tags:
  - technical-debt
  - software-engineering
  - css
  - refactoring
sources:
  - title: "We Need to Talk About Technical Debt ◆ 24 ways"
    url: "https://24ways.org/2016/we-need-to-talk-about-technical-debt/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/24ways-org--we-need-to-talk-about-technical-debt.md"
    kind: repo
---

Harry Roberts argues that technical debt and bad code get conflated, and that conflation is the problem. Technical debt, in his definition, is a deliberate and strategic decision: shipping something imperfect now in exchange for a benefit otherwise unattainable, with the intention of paying it back later. Bad code is different. It isn't a decision at all, just work done without knowing or caring that a better way existed.

He frames debt through a borrowing analogy: good debt (a mortgage, a student loan, a business loan) secures the means to pay itself back; bad debt (a loan shark, a payday loan) doesn't. Applied to code, a hacked-in CSS theme to close a big client is good debt only if the team goes back and builds theming properly afterward. Skip the repayment and every subsequent theme request piles hacks on top of hacks, until a full rewrite becomes unavoidable, at a cost higher than disciplined repayment would have taken.

## Fichamento

- Technical debt, by definition, is entered into knowingly and strategically. Debt doesn't happen by accident.
- Example: a team hacks a client-requested theme into a CSS architecture never built for theming, in exchange for closing a big sale. That decision is technical debt.
- After delivery there are two paths: pay off the debt by building theming properly, or ignore the repayment and keep hacking each new theme on top of the last.
- Good debt (mortgage, student loan, business loan) secures the means to repay itself; bad debt (loan shark, payday loan) doesn't.
- `!important` is Roberts's example of bad technical debt in CSS: seconds to write, weeks to refactor out, and it sets a precedent for the next hack.
- Bad code is distinct from technical debt. It isn't a deliberate trade-off, it's not knowing or caring that a better way exists, a skills gap rather than a judgment call.
- Unpaid debt compounds: what would have cost days of refactoring becomes weeks of rewriting once the codebase is unwieldy enough to force a teardown.
