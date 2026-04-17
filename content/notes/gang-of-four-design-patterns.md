---
title: Gang of Four Design Patterns
date: '2026-04-04T08:30:50+01:00'
summary: 'The 23 design patterns catalogued by Gamma, Helm, Johnson and Vlissides in Design Patterns: Elements of Reusable Object-Oriented Software (1994).'
tags: ["software-engineering", "design-patterns", "gang-of-four"]
has_commentary: true
sources:
- title: 'Design Patterns: Elements of Reusable Object-Oriented Software — Wikipedia'
  url: https://en.wikipedia.org/wiki/Design_Patterns
  kind: wiki
---

The 23 design patterns catalogued by Gamma, Helm, Johnson and Vlissides in *Design Patterns: Elements of Reusable Object-Oriented Software* (1994).

## Creational

1. **Abstract Factory** — provide an interface for creating families of related objects without specifying their concrete classes.
2. **Builder** — separate the construction of a complex object from its representation, so the same process can create different representations.
3. **Factory Method** — define an interface for creating an object, but let subclasses decide which class to instantiate.
4. **[Prototype](/notes/prototype-pattern)** — create new objects by cloning an existing instance.
5. **Singleton** — ensure a class has only one instance and provide a global point of access to it.

## Structural

6. **[Adapter](/notes/adapter-pattern)** — convert the interface of a class into another interface clients expect.
7. **Bridge** — decouple an abstraction from its implementation so the two can vary independently.
8. **Composite** — compose objects into tree structures to represent part-whole hierarchies, letting clients treat individual objects and compositions uniformly.
9. **[Decorator](/notes/decorator-pattern)** — attach additional responsibilities to an object dynamically, as an alternative to subclassing.
10. **[Facade](/notes/facade-pattern)** — provide a simplified interface to a complex subsystem.
11. **Flyweight** — use sharing to support large numbers of fine-grained objects efficiently.
12. **[Proxy](/notes/proxy-pattern)** — provide a surrogate or placeholder for another object to control access to it.

## Behavioral

13. **[Chain of Responsibility](/notes/chain-of-responsibility-pattern)** — pass a request along a chain of handlers until one processes it.
14. **Command** — encapsulate a request as an object, allowing parameterization, queuing, and undo.
15. **Interpreter** — define a grammar and an interpreter that uses the grammar to interpret sentences.
16. **[Iterator](/notes/iterator-pattern)** — access elements of a collection sequentially without exposing its underlying representation.
17. **[Memento](/notes/memento-pattern)** — capture an object's internal state so it can be restored later without violating encapsulation.
18. **[Mediator](/notes/mediator-pattern)** — define an object that encapsulates how a set of objects interact, promoting loose coupling.
19. **Observer** — define a one-to-many dependency so that when one object changes state, all dependents are notified.
20. **[Strategy](/notes/strategy-pattern)** — define a family of algorithms, encapsulate each one, and make them interchangeable at runtime.
21. **State** — allow an object to alter its behavior when its internal state changes, appearing to change its class.
22. **Template Method** — define the skeleton of an algorithm in a base class, letting subclasses override specific steps.
23. **[Visitor](/notes/visitor-pattern)** — represent an operation to be performed on elements of an object structure without changing the classes.
