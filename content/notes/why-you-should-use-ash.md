---
title: "Why you should use Ash?"
date: '2025-06-27T00:40:30+01:00'
category: webclip
summary: 'The chapter argues that Ash is worth learning because it centralizes domain logic, reduces duplication, and helps teams manage growing complexity, onboarding, and long-term maintenance.'
tags: ["ash", "phoenix", "domain-modeling", "declarative-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why you should use Ash? | devCarrots"
    url: "https://devcarrots.com/blog/why-you-should-use-ash/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-06/devcarrots-com--why-you-should-use-ash.md"
    kind: repo
---

The chapter argues for Ash by comparing it with vanilla Phoenix over the life of a project, not just at the start. The authors say Ash becomes more valuable as systems grow, because it keeps domain rules in one place and reduces the pressure of scattered custom code.

## Reading notes

- Some objections to Ash come from its small but growing community, such as fewer tutorials, harder-to-read documentation, and fewer experts.
- The authors say Ash’s creator and core team are active in the Elixir Forum and that support has been fast.
- They treat Ash’s new concepts, declarative style, and perceived magic as part of its design, not as flaws.
- Their main comparison is not starting a project, but managing it as it matures with more complexity.
- In their experience, vanilla Phoenix made later onboarding harder because key knowledge stayed in long-term contributors’ heads.
- Ash gives each resource a clearer structure, and the describe macro helps document resource information.
- They say Ash lowers code duplication by making resources a single source of truth for migrations, APIs, validations, and policy logic.
- They also argue that using one resource definition for multiple outputs reduces maintenance over time.
- The chapter presents Ash’s declarative approach as a way to define what is needed and let the framework handle the implementation details.
