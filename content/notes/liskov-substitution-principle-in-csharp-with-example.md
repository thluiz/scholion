---
title: "Liskov Substitution Principle in C# with Example"
date: '2026-09-25T21:54:43+01:00'
category: webclip
summary: 'The page explains LSP with a Bird/Ostrich example, shows how overriding Fly in Ostrich breaks substitution, and refactors the design around IBird and Move so each bird type behaves correctly.'
tags: ["liskov-substitution-principle", "solid", "object-oriented-design", "csharp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Liskov Substitution Principle in C# with Example"
    url: "https://www.c-sharpcorner.com/blogs/liskov-substitution-principle-in-c-sharp-with-example?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/c-sharpcorner-com--liskov-substitution-principle-in-csharp-with-example.md"
    kind: repo
---

The page explains the Liskov Substitution Principle as a rule of object-oriented design in which objects should be replaceable with subtype instances without breaking program correctness. It uses a Bird and Ostrich example to show how an overridden Fly method that throws an exception breaks substitution.

## Reading notes

- LSP is presented as one of the five SOLID principles.
- A subtype should be usable wherever the base type is expected without changing the program’s correctness.
- In the first example, Bird defines Fly and Ostrich overrides Fly to throw NotSupportedException.
- Assigning an Ostrich to a Bird reference and calling Fly causes an exception.
- The text treats that exception as a violation of LSP because the derived class changes the expected behavior.
- To follow LSP, the page suggests a better hierarchy or interfaces for different behaviors.
- It introduces IBird with a Move method as the shared contract.
- FlyingBird implements IBird and calls Fly from Move.
- Ostrich implements IBird and calls Run from Move.
- In the refactored code, both FlyingBird and Ostrich can be used through IBird without breaking the program.
- The page concludes that this design makes the code more robust, maintainable, and scalable.
