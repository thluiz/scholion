---
title: "Wiping the tech debt out with immutable code"
date: '2020-10-25T21:09:26-03:00'
category: webclip
summary: 'The post argues that technical debt keeps growing and proposes immutable code as a way to reset it by rewriting isolated components instead of incrementally patching them.'
tags: ["technical-debt", "code-maintenance", "elixir"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Wiping the tech debt out with immutable code"
    url: "https://no-kill-switch.ghost.io/wiping-the-tech-debt-out-with-immutable-code/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-10/no-kill-switch-ghost-io--wiping-the-tech-debt-out-with-immutable-code.md"
    kind: repo
---

The post argues that code maintenance keeps getting harder and that efforts to reduce technical debt are costly, temporary, and uncertain. It suggests resetting debt by rewriting code when a team is unhappy with it, instead of updating it in place.

## Reading notes

- Technical debt tends to grow, while efforts to reduce it are expensive, temporary, hard to justify, and not guaranteed to work.
- Immutable code means rewriting code whenever a bug, change, or new framework makes that piece worth replacing.
- This approach only makes sense for limited, well-isolated components.
- The code should be organized around business domain entities, not around old implementation.
- Composition should stay as flat as possible, without many visible layers.
- Components should interact through well-defined interfaces based on the domain model.
- Components should be fine-grained.
- Dependencies should be avoided except for the interfaces, including data-level dependencies.
- The model is presented as suitable for seasoned teams with high agility.
- The risks include fluid code state, a strong need for mature deployment and testing, dependence on good domain modeling, more cross-component interactions, and possible refactoring without enough sponsor control.
- The benefits include less tribal knowledge, easier upgrades, more willingness to touch legacy code, and more opportunities to remove dead code.
- Elixir is presented as a language that fits this style because of GenServer processes, hot code swapping, concise functional code, and message-based communication.
