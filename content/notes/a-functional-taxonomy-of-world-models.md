---
title: "A Functional Taxonomy of World Models - Dr. Fei-Fei Li"
date: "2026-09-23T15:31:29+01:00"
category: webclip
summary: "Fei-Fei Li and the World Labs team split 'world model' into three functions: renderers output pixels, simulators output physically faithful state, planners output actions."
tags:
  - world-models
  - ai
  - robotics
  - simulation
has_commentary: false
sources:
  - title: "A Functional Taxonomy of World Models - Dr. Fei-Fei Li"
    url: "https://drfeifei.substack.com/p/a-functional-taxonomy-of-world-models?utm_source=tldrai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-06/drfeifei-substack-com--a-functional-taxonomy-of-world-models.md"
    kind: repo
---

Fei-Fei Li and the World Labs team propose a way to cut through the overloaded term "world model": break it into three functions built on the same agent-action-state-observation loop from reinforcement learning. A renderer outputs pixels for human eyes, a simulator outputs state as a faithful representation of geometry and physics, and a planner outputs actions given an observation and a goal.

The essay treats simulation as the central component, because it provides the physically grounded state that both rendering and planning depend on. Renderers are the most commercially mature but optimize for visual plausibility rather than physical accuracy. Planners are the most nascent, still confined mostly to constrained lab demos.

## Reading notes

- The three-function split traces back to the POMDP loop from reinforcement learning: an agent takes actions, actions affect world state, the agent only perceives partial observations of that state, and new observations drive new actions.
- The term "world model" itself predates AI: Kenneth Craik proposed in 1943 that minds reason by running small-scale models of reality, and the phrase entered neural networks in the late 1980s and early 1990s.
- Renderers (video models, Google's Genie 3, World Labs' RTFM) carry no explicit understanding of 3D structure. A drone shot can look flawless from above and fall apart the moment you try to drive through the city below.
- Simulators serve both human professionals (architects, filmmakers, game developers, who need accuracy beyond visual plausibility) and programs (RL agents, robot controllers, autonomous vehicles training at scale on scenarios too dangerous or expensive to run in reality).
- The hardest open problems concentrate in simulation: 3D data with explicit geometry and physical annotations is far scarcer than the internet video renderers train on, and the sim-to-real gap persists.
- World Labs' Marble already blurs the boundary between renderer and simulator, outputting both Gaussian splats for visual exploration and collision meshes a physics engine can operate on from a single model.
- The essay's bet: the same underlying knowledge of geometry, physics and dynamics sits beneath all three functions, so the field is converging toward one foundation model that renders, simulates and plans depending on what the task needs.
