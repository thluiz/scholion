---
title: "Solid Principles Simplified (C#, .Net 5)"
date: '2022-07-04T10:47:17-03:00'
category: webclip
summary: 'The article explains SOLID as a set of design principles that improve readability, changeability, extensibility, scalability, maintainability, and loose coupling in C# and .NET 5 code.'
tags: ["solid-principles", "object-oriented-programming", "csharp", "dotnet-5"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Solid Principles Simplified (C#, .Net 5)"
    url: "https://www.c-sharpcorner.com/article/solid-principles-simplified-c-sharp-net-52/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/c-sharpcorner-com--solid-principles-simplified-c-sharp-dot-net-5.md"
    kind: repo
---

The article introduces SOLID as a group of design principles meant to make code easier to understand, adapt, extend, scale, and maintain. It connects these principles to loose coupling and to easier refactoring, especially as applications grow and changes begin to affect related parts of the code.

It then walks through each principle with examples in C# and .NET 5. The examples show how Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion reduce coupling, separate responsibilities, and make classes or modules easier to change without modifying unrelated code.

## Reading notes

- SOLID is presented as a set of basic design principles for object-oriented programming in C# and .NET 5.
- The article says these principles help code become easier to understand, adapt, extend, scale, and maintain.
- One of the main benefits highlighted is loose coupling, which makes change and feature growth easier to manage.
- The article says SOLID was introduced by Robert C. Martin.
- Single Responsibility Principle is described as giving each function, class, or module one responsibility.
- The article shows an order class that creates an order, stores it in a database, and sends email as an example of violating SRP.
- The SRP example is split into separate order, database, and email classes.
- Open-Closed Principle is stated as keeping entities open for extension but closed for modification.
- The article uses vehicle carbon footprint calculation to show how adding new vehicle types can force changes when OCP is violated.
- The OCP version uses an IVehicle interface so each vehicle calculates its own carbon footprint.
- Liskov Substitution Principle is described as allowing derived classes to replace base classes without changing behavior.
- The article uses employee classes to show how contractual employees can break a design that assumes all employees receive benefits.
- The LSP example separates permanent and contractual employees so each can use the base salary update behavior without modifying the base class.
- Interface Segregation Principle says clients should not be forced to implement methods they do not use.
- The article first shows one large employee interface with many methods, then replaces it with smaller interfaces for permanent, contractual, and part-time employees.
- Dependency Inversion Principle is presented as making higher-level and lower-level modules depend on abstractions.
- The article shows a user service and user repository that are tightly coupled, then refactors them to use IUserService and IUserRepository interfaces.
- The summary states that each SOLID principle is explained with examples for clear understanding.
