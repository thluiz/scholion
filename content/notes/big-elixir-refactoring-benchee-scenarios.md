---
title: "A Big Elixir Refactoring"
date: '2026-11-16T20:09:56+00:00'
category: webclip
summary: 'Author describes refactoring Benchee’s nested map data model into explicit Scenario structs, highlighting simple, decoupled Elixir code and ease of incremental change.'
tags: ["elixir", "refactoring", "benchee", "software-design"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "A Big Elixir Refactoring"
    url: "https://devonestes.com/a-big-elixir-refactoring"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--big-elixir-refactoring-benchee-scenarios.md"
    kind: repo
---

The author recounts a substantial refactoring of the Benchee benchmarking library to support future features like optional memory measurements. The original deeply nested map data structure was replaced with a list of explicit structs representing newly named domain concepts such as Scenario and Scenario Context. This change aimed to simplify evolution of the data model and avoid widespread changes when adding fields. The work proceeded through exploratory spikes, design discussion with Tobi, and two pull requests that introduced the new structs and then migrated modules incrementally. The experience reinforced the author’s view that Elixir encourages simple, decoupled code, making large refactorings feel straightforward and almost mechanical.

## Reading notes

- The author’s goal was to refactor someone else’s Elixir code in Benchee to make it easier to add a future feature that required a new data model and clearer domain naming.
- Before refactoring, Benchee’s main data structure was a deeply nested map that worked well for recursive job processing but made format changes difficult because many functions iterated over it with `Enum.map/2`.
- They wanted the data structure to support optionally tracking memory usage information, which would be hard to add cleanly with the existing nested map.
- As a newcomer to the codebase, the author felt this central data structure represented important concepts but lacked clear names.
- Two initial spikes tried adding memory usage directly and produced unsatisfying implementations, but they exposed specific pain points and guided how to address them.
- A subsequent spike focused on a potential refactoring, letting the author experiment with different approaches; it was imperfect but useful for exploration and starting conversation.
- The author and Tobi met in person in Berlin to review the spike, discuss positives, concerns, and improvements, and this discussion surfaced previously unnamed concepts like Scenario and Scenario Context.
- They chose to model these concepts as a list of structs instead of combinations of keys and values in the nested map, with each struct holding all data needed for its domain concept.
- Iterating over the list of structs was at least as easy as iterating over the nested map, and adding fields to structs later would not require changing existing code, which was the main motivation for moving to structs.
- The first pull request introduced the basic Scenario concept without using it yet, intentionally splitting a large change into smaller, additive, non-breaking steps with minimal code changes and some new tests.
- The second pull request migrated storage of benchmark information to the new data structure, a larger task the author approached by updating one module at a time.
- For each module, they first updated unit tests to expect the new data structure, then refactored the module until those tests passed, with each commit representing one such step.
- They purposely did not update feature or integration tests during the module-by-module work, skipping any that broke, assuming they would pass again once all unit-level changes were complete.
- This assumption held for all but one feature test that checked the old nested map format, reflecting that the new struct-based model is a breaking change for Benchee’s public API and affects plugins.
- The author describes the overall experience as very pleasant and notes that the process stayed simple in the Rich Hickey sense, without moments of deep confusion common in their Ruby work.
- Because modules were highly decoupled, the author could break a large refactor into many small, clear steps and often proceed almost mechanically without heavy mental load.
- They prefer making many small, straightforward changes over a few large, complex changes and see that preference as aligned with maintainable software that still solves interesting problems in simple ways.
- During the refactor, changes in one module never broke tests in other modules; only feature and integration tests failed temporarily, and they passed again once each module was updated.
- The author emphasizes that low coupling was crucial, arguing that coupling makes software complicated, and that this codebase showed very little coupling between units.
- They reference Rich Hickey’s "Simplicity Matters" talk as a deeper exploration of the relationship between simplicity and coupling.
- While crediting Tobi’s thoughtful design, the author argues that Elixir itself promotes this style of decoupled, simple design, whereas some other languages make tight coupling easier.
- In Elixir, achieving tighter coupling usually requires using more advanced features like Protocols and Behaviours, suggesting that complexity requires deliberate effort.
- The author concludes that Elixir applications tend to be simple by default and must be pushed toward complexity, whereas applications in many other languages are complex by default and must be actively simplified.
- After completing the main refactor, the next work is to update Benchee plugins to use the new struct-based data structure.
