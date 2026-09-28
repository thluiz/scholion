---
title: "What the heck is SOLID?"
date: '2022-07-06T11:46:36-03:00'
category: webclip
summary: 'The post explains SOLID as five design principles for cleaner, more maintainable object-oriented code, then walks through each principle with C# examples and refactorings.'
tags: ["solid", "object-oriented-programming", "c-sharp", "software-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What the heck is SOLID?"
    url: "https://lovelacecoding.hashnode.dev/what-the-heck-is-solid?mkt_tok=NDI2LVFWRC0xMTQAAAGFbee8hcp2lDLSYrNQYAyzS07xDLppHmKD_9n0yaQfq3wGKBX7mzjUZfFMfxbj57GR8Es3NChOwtCOHXQeZlXtMx0_cYc7GohNhBjIcFvgW130Gkxv"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/lovelacecoding-hashnode-dev--what-the-heck-is-solid.md"
    kind: repo
---

SOLID is presented as a set of five design principles for software development that help keep object-oriented code structured, readable, and maintainable. The post says these ideas make future changes easier, especially as a project grows or becomes harder to revisit.

It then explains each principle with examples: Single Responsibility says each method or function should have one goal; Open-Closed says code should be extendable without rewriting existing classes; Liskov Substitution says a base class should be replaceable by its subclass; Interface Segregation says interfaces should be split so classes only implement what they need; Dependency Inversion says high-level modules should depend on abstractions rather than concrete details.

## Reading notes

- SOLID is an acronym for five design principles in software development.
- The goal is to keep code structured, readable, and maintainable.
- The Single Responsibility Principle says each method or function should have only one goal or reason for change.
- The Open-Closed Principle says software entities should be open for extension but closed for modification.
- The Liskov Substitution Principle says a base class should be interchangeable with a subclass without breaking the program.
- The Interface Segregation Principle says interfaces should be separated so classes do not have to implement methods they do not need.
- The Dependency Inversion Principle says high-level modules should depend on abstractions, not on concrete low-level modules.
- The post uses C# examples to show how each principle changes class design.
