---
title: "Software Engineering Splits in Three"
date: "2026-09-23T17:31:23+01:00"
category: webclip
has_commentary: false
summary: "AI collapses the cost of writing code and shifts the bottleneck to judgment, splitting software engineering into three tiers with different platforms, skills, and consulting models."
tags:
  - ai-assisted-coding
  - software-engineering
  - enterprise-it
  - consulting
sources:
  - title: "Software Engineering Splits in Three"
    url: "https://adventures.nodeland.dev/archive/software-engineering-splits-in-three/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/adventures-nodeland-dev--software-engineering-splits-in-three.md"
    kind: repo
---

AI-assisted coding didn't just speed up how software gets written. It moved the bottleneck from writing code to judging whether the code is correct, and that shift is splitting the software engineering market into three distinct tiers, each with its own economics, skills, and way of building.

Tier 1 (Big Tech and digital-native giants) treats AI as a force multiplier for senior engineers who review generated code and catch what fails at scale. Tier 2 (large enterprises like banks and insurers) leans on platforms with guardrails already built in and brings in fractional senior consultants for the judgment calls it can't staff internally. Tier 3 (small and mid-market businesses) gets custom software for the first time, built cheaply by local developers who work less like architects and more like plumbers. The three tiers used to run similar work at different pay scales; now the work itself diverges, closing off the career ladder that once let engineers move between them.

## Fichamento

- For decades enterprises had two bad options: build in-house (expensive, slow, reserved for core systems) or buy/outsource (senior rates paid for junior delivery, knowledge walking out the door when the contract ended).
- The real change is economic: the cost of turning a defined requirement into working code has collapsed, though someone still has to know if the implementation is correct, understand the business problem well enough to define the requirement, and maintain the system as the business evolves.
- The market splits into three tiers: Tier 1, where software is the product; Tier 2, large enterprises where software is critical but not the core business; Tier 3, small and mid-market businesses that couldn't afford custom software before.
- Tier 1 needs senior engineers to review AI-generated code and catch subtle bugs that pass tests but fail at scale; AI multiplies the same accountable team, it doesn't replace it.
- Tier 2 can't hire enough senior engineers to match Tier 1, so it relies on platforms designed with safe defaults, plus fractional senior consultants brought in for specific architectural decisions.
- Tier 3 becomes a real market for a new role, the "software plumber": local developers building custom tools for businesses that previously used only off-the-shelf products or nothing at all.
- Platform engineering and SRE both become more important, not less: the platform is the safety net for code shipped faster than humans can reason about it, and SRE becomes the layer that catches what passes review but breaks in production.
- The talent pipeline is at risk. If junior developers no longer do the ticket work that used to teach them judgment, organizations lose their internal path to producing future senior engineers.
- The old consulting model of billing hours of implementation is being replaced by fractional senior expertise: paying for judgment quality, not implementation time.
- Cheaper custom software changes the buy-vs-build calculus. Some integrations and internal tools that weren't worth building before now are, but the deciding question shifts from "can we afford to build this" to "do we have the judgment to build and maintain it well."
