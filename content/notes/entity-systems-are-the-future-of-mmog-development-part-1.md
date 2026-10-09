---
title: "Entity Systems are the future of MMOG development – Part 1"
date: '2014-05-05T08:43:57-03:00'
category: webclip
summary: 'The post argues that entity systems help MMOG teams change game logic faster, support post-launch rewrites, and fit the needs of large, networked projects, while also warning about performance costs and team complexity.'
tags: ["entity-systems", "mmog-development", "game-architecture", "network-programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Entity Systems are the future of MMOG development – Part 1 | T-machine.org"
    url: "http://t-machine.org/index.php/2007/09/03/entity-systems-are-the-future-of-mmog-development-part-1/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-05/t-machine-org--entity-systems-are-the-future-of-mmog-development-part-1.md"
    kind: repo
---

The post presents entity systems as a strong fit for MMOG development because they let designers change game logic without a programmer, make cross-cutting game ideas easier to implement, and support fast compile-test-debug cycles. It also says they helped with post-launch rewriting of game features and were especially useful when a team had to keep evolving a live game.

It also notes the limits of the approach. The author says entity systems can hurt runtime performance because of indirection and checks, and that they can be hard to use well. In the OFP2 project, the system was attractive for memory management and stream-oriented coding, and it helped the network programmer add latency hiding and prediction without forcing large redesigns across the team.

## Reading notes

- Entity systems were first used here to address MMOG development problems, especially the need to keep changing game logic after launch.
- The post links MMOG success to the ability of the team to improve the game month after month.
- It says entity systems can become a performance problem at runtime because of indirection and checks.
- On Operation Flashpoint 2, the system was seen as useful for memory management and stream-oriented coding.
- The author argues that an entity system as the shared interconnect between subsystems makes network features easier to implement without disrupting other code.
- The post suggests that next-generation MMOGs may be difficult to build without a core entity system.
