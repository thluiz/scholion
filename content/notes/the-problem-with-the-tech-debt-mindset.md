---
title: "The problem with the tech debt mindset"
date: '2026-09-25T20:52:37+01:00'
category: webclip
summary: 'The episode argues that tech debt covers several different problems, from outdated choices to replatforming, and that teams need a clear, quantified way to balance maintenance against features.'
tags: ["tech-debt", "software-maintenance", "replatforming", "engineering-teams"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The problem with the tech debt mindset"
    url: "https://stackoverflow.blog/2024/07/23/the-problem-with-the-tech-debt-mindset/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/stackoverflow-blog--the-problem-with-the-tech-debt-mindset.md"
    kind: repo
---

The episode treats tech debt as a broad label for different kinds of work. Jon Bevan separates outdated technology choices, ongoing maintenance like dependency and language upgrades, and larger rearchitecting or replatforming efforts. He also says code is an asset, so teams need to balance keeping it healthy with shipping features and fixing bugs.

## Reading notes

- Tech debt can mean a once-good technology choice that is now out of date, a shortcut taken to ship faster, or a larger rearchitecting or replatforming effort later on.
- Maintenance work like dependency upgrades is distinct because it is needed to keep systems running.
- If teams postpone upgrades, later feature work can grow in scope because old choices can no longer be ignored.
- In one case, improving the scripting editor required upgrading Groovy, which raised backward-compatibility problems in a SaaS product that runs all the time.
- Moving away from Ratpack for Java 21 and virtual threads also required updating Gradle, Groovy, and plugins, which showed how upgrade work cascades.
- Bevan argues that code is an asset as well as a liability, and that its value can grow when more customers use the features it supports.
- To justify maintenance work, teams can point to slower delivery, engineer frustration, roadmap needs, and the business value unlocked by upgrades.
- He says some libraries and patterns brought real value at first but later became hard to maintain, especially when testing or team understanding suffered.
- He also emphasizes psychological safety, so engineers can say when a technology choice is painful or a bad fit without fear of being ignored or punished.
