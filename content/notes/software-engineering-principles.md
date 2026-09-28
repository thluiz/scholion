---
title: "Software Engineering Principles"
date: '2022-05-02T19:26:07-03:00'
category: webclip
summary: 'The post introduces core software engineering and OOP ideas, then ties them to SOLID, composition, DRY, KISS, YAGNI, and UML-based modeling for cleaner, more maintainable code.'
tags: ["software-engineering", "oop", "solid", "design-patterns"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Software Engineering Principles"
    url: "https://bognov.tech/software-engineering-oop-principles-and-good-practices-to-avoid-spaghetti-code"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-05/bognov-tech--software-engineering-principles.md"
    kind: repo
---

The post presents software engineering as a set of basic concepts and good practices that help avoid spaghetti code, while stressing that there is no universal answer and that decisions depend on the case. It walks through OOP building blocks, core design principles, and simple modeling tools.

## Reading notes

- OOP is introduced through classes that define an object’s state and behavior, using attributes and methods.
- Encapsulation keeps data and behavior inside one unit, with public or private methods.
- Abstraction hides internal implementation and lets users focus on how to use an object.
- Inheritance is presented through interfaces, classes, abstract classes, superclasses, and subclasses.
- Polymorphism is described as many forms, with interfaces having multiple implementations.
- Method overriding changes a superclass method in a subclass.
- Method overloading uses the same method name with different parameters, and the program chooses at compile time.
- Duck typing is linked to behavior over type, especially in Python.
- IS-A and HAS-A are listed as two key OOP relationships.
- SOLID is described as five principles for understandable, flexible, and maintainable code.
- SRP says a class, function, or module should have one responsibility.
- OCP says software entities should be open for extension and closed for modification.
- LSP says a subclass should be substitutable for its superclass.
- ISP says clients should not depend on interfaces they do not use.
- DIP says high-level and low-level modules should depend on abstractions.
- Composition and aggregation are both described as forms of association between objects.
- Composition over inheritance is presented as a way to improve encapsulation, testing, and refactoring.
- Polymorphism can replace long chains of conditionals.
- The engineering principles section highlights Measure twice and cut once, DRY, KISS, YAGNI, avoiding premature optimization, POLA, and the Law of Demeter.
- The Law of Demeter is tied to reducing coupling and keeping related classes cohesive.
- UML is introduced as a way to model classes, abstract classes, and interfaces before implementation.
- Design patterns are described as solutions to common architecture problems, grouped as creational, structural, and behavioral.
