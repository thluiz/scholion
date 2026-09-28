---
title: "Do you really need a Staging environment?"
date: '2022-05-25T10:17:06-03:00'
category: webclip
summary: 'The article weighs staging against faster, simpler release flows and argues that staging often adds cost, complexity, and delay. It keeps value mainly for hard data workflows and complex infrastructure.'
tags: ["staging", "continuous-delivery", "feature-flags", "observability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Do you really need a Staging environment? 🚢"
    url: "https://refactoring.fm/p/do-you-need-staging?utm_source=email&s=r"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-05/refactoring-fm--do-you-really-need-a-staging-environment.md"
    kind: repo
---

The article examines staging as a shared environment for testing before release and argues that it often creates more cost and complexity than value. Its main critique is that staging is hard to keep close to production and tends to slow releases by adding extra steps and batching changes.

It also outlines ways to reduce reliance on staging, including remote dev environments, preview links for QA, feature flags, observability, and making staging optional. It still sees staging as useful when teams face complex data workflows or complex infrastructure.

## Reading notes

- Staging is described as a safe space for testing software in an environment close to production before release.
- The article says staging is often unreliable because it is hard and expensive to keep it aligned with production data and infrastructure.
- It says staging slows delivery by adding an extra release level and encouraging batched releases.
- Faster releases are linked to stronger feedback loops, more frequent deployments, and smaller atomic releases.
- Remote dev environments can make development environments closer to production and reduce the need for staging.
- Preview links can replace some staging use for QA and product testing, especially for frontend work.
- Feature flags let teams deploy code before turning features on for users and can reduce release risk.
- Observability and testing in production are presented as important whether or not staging exists.
- Staging can be made optional when most changes can go straight to production but some cases still need testing first.
- The article keeps staging for complex data workflows, such as restricted data, migrations, and large data changes.
- It also keeps staging for complex infrastructure with many services, where full dev parity is hard to reproduce locally.
