---
title: "Devs: Don’t Just Read About Design Patterns, Implement Them"
date: '2026-09-25T21:23:55+01:00'
category: webclip
summary: 'The post argues that design patterns are more useful as examples you build than as theory you read. A contrived C# animal-mission setup shows how decoupling lets missions, heroes, and lairs vary independently.'
tags: ["design-patterns", "decoupling", "csharp", "object-oriented-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Devs: Don’t Just Read About Design Patterns, Implement Them"
    url: "https://thenewstack.io/devs-dont-just-read-about-design-patterns-implement-them/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/thenewstack-io--devs-dont-just-read-about-design-patterns-implement-them.md"
    kind: repo
---

The post says design patterns help document software, but they teach better through examples you can build. Its C# example uses hero animals, missions, and lairs to show extendable design as something that can change without breaking the system.

## Reading notes

- Design patterns are useful for confirming repeatable structures after you encounter them, but examples are better for learning how to solve new problems.
- The article uses a light-hearted C# setup with hero animals on a mission to explain the strategy or command pattern idea.
- Extendable design means knowing what can be altered or added without breaking the system.
- The mission is separate from the roster of heroes, so the system can use any animal heroes you define.
- The roster contains classes such as Penguin, Shark, Goat, and Gorilla.
- HeroAnimal is an abstract class that defines skills like canFly, canSwim, canClimb, canCrawl, and a home biome.
- Lair is an interface with a CanHeroBreakIn method.
- A Castle lair can be broken into by a flying hero or a climbing hero.
- Biomes are defined as Forest, Ice, Plains, Swamp, and Sea.
- Fish and Bird serve as base classes for hero animals, and Shark and Penguin are concrete examples.
- The system selects a team by list search and match, and the list could be mixed before each run.
- New animal heroes, lairs, missions, and even biomes can be added, though removing biomes might break existing heroes.
- The article closes by saying the Gang of Four should be respected after working on solutions yourself.
