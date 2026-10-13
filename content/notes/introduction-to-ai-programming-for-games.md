---
title: "Introduction to AI Programming for Games"
date: '2013-01-02T11:10:38-03:00'
category: webclip
summary: 'The tutorial shows how to add game AI with simple decision logic, steering behaviors like seek, arrive, and separate, and a finite state machine that changes strategy.'
tags: ["game-ai", "steering", "finite-state-machines", "cocos2d"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Introduction to AI Programming for Games"
    url: "http://www.raywenderlich.com/24824/introduction-to-ai-programming-for-games"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/raywenderlich-com--introduction-to-ai-programming-for-games.md"
    kind: repo
---

The post introduces game AI through a Monster Wars example. It starts with simple if/else decisions for attack, defense, and unit building, then fixes movement with steering behaviors, and finally refactors the enemy strategy into a finite state machine.

## Reading notes

- AI in games can be as simple as normal coding if the game only needs basic decisions.
- The first enemy logic compares army value to choose attack or defense, then picks units by countering the player’s unit mix.
- The tutorial uses Monster Wars, a Cocos2D iOS starter project, to keep the focus on AI.
- The original movement code moves monsters directly toward targets and causes jagged behavior, rounding issues, and sticking.
- Steering is presented as the AI side of movement, alongside pathfinding, with seek, flee, arrive, wander, separate, and path following as examples.
- Seek sets acceleration toward a target at max strength, but can overshoot.
- Arrive adds target radius, slow radius, and deceleration so units stop at the destination instead of flying past it.
- Separate adds acceleration away from nearby allies so units do not stack on top of each other.
- The state machine section defines four states: Massing, Countering, Defending, and Rushing.
- Defending reacts to enemies near the base and builds counters while under attack.
- Countering waits for an attack, then spends saved money to respond with overwhelming force.
- Rushing attacks when the army is strong enough and keeps building Quirks while ahead.
- The refactor moves state behavior into separate AIState subclasses with enter, execute, exit, and name methods.
- The tutorial ends by noting that game AI should serve fun and pointing to books and an example project for further study.
