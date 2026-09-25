---
title: "You're getting your last mile wrong"
date: '2026-09-25T17:28:47+01:00'
category: webclip
summary: 'The article argues that software teams should treat production delivery as part of development from the start, so projects stay potentially shippable instead of facing costly last-mile delays and bugs.'
tags: ["software-delivery", "devops", "product-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "You're getting your last mile wrong"
    url: "https://makemeacto.substack.com/p/youre-getting-your-last-mile-wrong?r=lcru6&ref=dailydev&triedRedirect=true"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/makemeacto-substack-com--youre-getting-your-last-mile-wrong.md"
    kind: repo
---

The article says teams often spend most of their time building in simplified environments and leave production delivery for the end, when setup becomes harder, slower, and more failure-prone. It argues that Agile and DevOps are often reduced to rituals, while the real principle is to make software potentially shippable at every stage.

It recommends reversing the usual order of operations by thinking about production before writing code, then setting up repositories, CI, environments, and CD early. For personal projects, it adds that early idea validation should come first, but once a project is worth committing to, delivery capabilities should be part of the initial work.

## Reading notes

- Teams often focus on building first and only later discover the work needed to ship to production.
- The last mile includes delivery pipelines, production environments, and assumptions that break under real deployment conditions.
- Agile is presented as requiring software to be potentially shippable at every increment.
- DevOps is described as treating development and delivery as connected parts of software engineering.
- The proposed sequence is to prepare production concerns early: repository, tests, CI, environments, and CD.
- Observability, alerting, and dogfooding are suggested as early additions.
- For personal projects, the article recommends early validation of the idea before investing in delivery setup.
- Once a personal project is worth continuing, delivery capabilities should be set up before moving deeper into implementation.
