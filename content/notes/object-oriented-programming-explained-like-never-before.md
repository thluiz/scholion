---
title: "Object-Oriented Programming Explained Like Never Before"
date: '2022-05-17T09:42:45-03:00'
category: webclip
summary: 'The article defines OOP in JavaScript and walks through classes, objects, abstraction, encapsulation, inheritance, and polymorphism with car and student examples.'
tags: ["object-oriented-programming", "javascript", "classes", "inheritance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Object-Oriented Programming Explained Like Never Before"
    url: "https://kumartul.hashnode.dev/object-oriented-programming-explained-like-never-before"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-05/kumartul-hashnode-dev--object-oriented-programming-explained-like-never-before.md"
    kind: repo
---

The article explains object-oriented programming as a paradigm centered on objects rather than functions and logic, using JavaScript as the example language. It introduces classes and objects first, then shows the four pillars of OOP through code examples built around cars and students.

## Reading notes

- OOP is described as a programming paradigm used in languages such as Java and C++, and the article uses JavaScript to explain it.
- A class is presented as a blueprint or prototype from which objects are created.
- The `constructor` initializes object properties, and `this` refers to the current instance.
- A method is a function inside a class, such as `drive`, which changes state and logs output.
- An object is described as an instance of a class with state and behavior.
- Abstraction is explained as exposing only the essential parts of code and hiding internal complexity.
- The article uses `Math.abs` and a `Car.drive()` method as examples of abstraction.
- Encapsulation is presented as protecting data and controlling access so code is used as intended.
- Private fields are shown with `#isRunning`, and getters are used to read state without exposing the private field directly.
- The article says setters and getters are commonly used in encapsulation, but the setter example is commented out because it would allow unwanted modification.
- Inheritance is explained as a parent-child relationship where child classes reuse features from a parent class.
- The article compares separate `Sedan` and `Hatchback` classes with a shared `Car` base class to show code reuse.
- `extends` is used to create derived classes, and `super` calls the parent constructor.
- Three inheritance types are listed: single, hierarchical, and multilevel.
- Polymorphism is presented as changing inherited behavior through method overriding.
- The `introduce` method is overridden in `Boy` and `Girl` classes to add class-specific output.
- The article ends by saying the reader should now be confident enough to use OOP in a project.
