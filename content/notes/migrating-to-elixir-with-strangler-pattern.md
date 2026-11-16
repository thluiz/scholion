---
title: "Migrating to Elixir with the Strangler Pattern"
date: '2026-11-16T20:08:27+00:00'
category: webclip
summary: 'Article explains how to migrate an existing app to Elixir using the Strangler Fig pattern, routing traffic gradually and testing new endpoints against the old system.'
tags: ["elixir", "strangler-pattern", "system-migration"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Migrating to Elixir with the Strangler Pattern"
    url: "https://devonestes.com/migrating-to-elixir-with-the-strangler-pattern"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--migrating-to-elixir-with-strangler-pattern.md"
    kind: repo
---

The text describes how teams can migrate existing applications to Elixir by using Martin Fowler's Strangler Fig Application pattern. It focuses on wrapping the old app with a new Elixir router, gradually moving routes, and running live comparisons between old and new implementations to avoid regressions. The author also warns against leaving the migration half-finished or depending on the old system as a long-term backend.

## Reading notes

- Many Elixir production users arrived there by migrating from another language rather than starting fresh.
- Rewriting an application is presented as risky and intimidating, so the goal is to make the process simpler and reduce regressions.
- The starting point is Martin Fowler’s Strangler Fig Application pattern, where a new application wraps the old one and incrementally replaces parts of it.
- This pattern lets teams keep the old application running while gradually moving behavior to the new system and verifying that the new behavior matches the old.
- A simple initial Elixir router is set up that forwards all requests to the old application through a redirect controller.
- Because Phoenix routers match routes top to bottom, new routes can be added above the catch-all forward, allowing one route at a time to be migrated.
- After adding a concrete route like `GET /users` to the new router, that specific request is handled by the new Elixir app instead of the legacy system.
- Before switching over in production, the author suggests gaining confidence by testing that the new implementation matches the old implementation.
- The example `UserController` intercepts the request, spawns a process to call both new and old implementations, compares the results, and then still forwards the original request to the old system.
- This approach enables testing in production: each incoming request triggers a comparison between old and new behavior without affecting the user-facing response.
- Differences between the new and old responses should be logged with extensive context to help track down bugs in the new code.
- If the comparison runs in production for days or weeks without mismatches, it becomes reasonably safe to switch traffic fully to the new implementation and remove the old one.
- The author notes that this strategy is easier to apply for `GET` endpoints than for `POST`, `PUT`/`PATCH`, and `DELETE`, though with planning it can still be used for those.
- Property-based tests can be used before production testing, hitting both systems with generated requests and checking that responses match.
- Setting up good property-based tests can be time-consuming for complex APIs, but they provide ongoing protection against regressions even after migration.
- The overall migration steps are: put a router in front that forwards everything, implement a replacement for one route, route that traffic to the new app while still forwarding for comparison, switch fully when confident, then repeat.
- Although the article uses Elixir for the example, the author states that this pattern applies to migrating any web app between any two systems.
- There is a caution against keeping the old system as a permanent API for the new system, only migrating parts that change.
- That idea assumes the legacy system will stay mostly stable, which the author argues is rarely true for long in software.
- Migrating concerns like HTML rendering can require a lot of work upfront, especially when CSS is involved, which tempts teams to leave them in the old system.
- The author argues that migrations of this kind work best when treated as an all-or-nothing effort rather than an indefinite hybrid setup.
- Such migrations deliberately introduce temporary complexity with the expectation of simplifying the system once the work is complete.
- This pattern is likened to common refactorings where extra complexity is accepted temporarily as a way to reach a cleaner end state.
- If the migration never finishes, the system is left with the additional, supposedly temporary complexity permanently.
- The target end state should be a simple system, and stopping halfway only leaves an already complex system even more complex.
