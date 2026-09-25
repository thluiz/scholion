---
title: "Fragments: February 13"
date: "2026-09-23T16:05:41+01:00"
category: webclip
has_commentary: false
summary: "Martin Fowler collects notes from a Thoughtworks retreat: senior developers staying relevant with LLMs, cognitive debt outpacing technical debt, and the drift toward supervisory programming."
tags:
  - llm
  - cognitive-debt
  - software-engineering
  - ai-agents
sources:
  - title: "Fragments: February 13"
    url: "https://martinfowler.com/fragments/2026-02-13.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/martinfowler-com--fragments-2026-02-13.md"
    kind: repo
---

Martin Fowler posts a batch of notes from the Thoughtworks Future of Software Development Retreat and The Pragmatic Summit. The thread running through all of them is what happens to programmers once LLM agents take over more of the coding itself.

## Reading notes

- Senior developers at the retreat stayed optimistic about their own relevance. Hands-on practice with LLMs converted more skeptics than argument did, and some who'd drifted away from coding found agents brought them back to it.
- Mid-level developers face the roughest transition: they built their careers before LLMs existed, but haven't yet reached the experience seniors have to drive agents effectively.
- Margaret-Anne Storey's concept of cognitive debt extends Fowler's own technical-debt metaphor. A student team he taught lost track of why design decisions were made even while the code still ran, accumulating cognitive debt faster than technical debt. Fowler reframes it: the cruft here is ignorance of the system, paid down only by investing in understanding, a dynamic close to what [Elmar Chavez calls the slow erosion of an engineer's own skill](/notes/the-slow-and-quiet-cognitive-atrophy/).
- Developer Experience and Agent Experience turn out to overlap almost completely, per Laura Tacho, though Fowler notes the irony: leadership is suddenly willing to invest in tooling clarity for agents that it never bothered building for humans.
- IDEs still need humans to judge when a task goes to an LLM and when a deterministic feature does it better, such as orchestrating a built-in rename/refactor tool instead of asking a model to rewrite the whole codebase.
- Team shape is an open question too: instead of one programmer driving many agents, two humans driving a fleet of agents together might combine the benefits of pairing with higher throughput.
- External research cited backs a warning: AI adoption pushes people to work faster and longer without being asked, and the initial productivity surge can give way to workload creep, cognitive fatigue, and burnout. Camille Fournier ties this to a cost managers already know, the mental fatigue of constant context-switching.
