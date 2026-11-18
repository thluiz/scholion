---
title: "Strategy Pattern"
date: '2020-04-20T21:22:42+00:00'
category: webclip
summary: 'Short overview of the Strategy (policy) pattern: choosing between interchangeable algorithms at runtime to change application behavior, with a JavaScript AI game example.'
tags: ["design-patterns", "strategy-pattern", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Strategy Pattern"
    url: "https://dev.to/francescoxx/strategy-pattern-5oh"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--strategy-pattern-francescoxx-dev-to.md"
    kind: repo
---

The page explains the Strategy, or policy, pattern as a behavioral design pattern that lets an application choose among different algorithms at runtime. This flexibility comes from encapsulating algorithms as separate strategy objects and switching them through a setStrategy method, illustrated with a JavaScript AI game that alternates between aggressive, defensive, and balanced behaviors.

## Reading notes

- Strategy pattern is also known as the policy pattern and focuses on selecting an algorithm at runtime.
- Deferring the choice of algorithm until runtime increases flexibility and reusability of the code.
- The pattern fits scenarios where an application’s behavior must change dynamically while it is running.
- Example behaviors mentioned are aggressive, defensive, and balanced modes.
- The intent is to define multiple algorithms and make them interchangeable through a setStrategy() method.
- It should be applied when classes differ only in behavior and when several variants of an algorithm are required.
- Using strategy families allows sharing common parts through inheritance.
- Applying the pattern helps avoid conditional statements that branch on behavior.
- Clients of the pattern can pick which behavior they need by choosing the appropriate strategy object.
- Downsides include an increased number of objects in the system.
- Another drawback is that strategies may be shared between objects instead of being tightly bound to a single instance.
- The pattern is highlighted as useful for encapsulating an algorithm.
- It is also described as suitable for changing the algorithm while the application is running.
- The JavaScript example defines concrete strategies AggressiveStrategy, BalancedStrategy, and DefensiveStrategy, each exposing a next method.
- AIGameStrategy acts as the strategy context, with a setStrategy method to assign the current game strategy and a next method delegating to the selected strategy.
- The main code initializes three strategy instances for aggressive, balanced, and defensive behaviors.
- An AIGameStrategy instance holds the current strategy and forwards calls to the chosen strategy object.
- The example demonstrates setting the strategy to defensive, then balanced, then aggressive, with console output reflecting the current behavior.
- A GitHub link is provided to a repository named Design-Patterns-Strategy-Javascript containing the implementation.
