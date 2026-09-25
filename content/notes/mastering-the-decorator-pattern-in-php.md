---
title: "Mastering the Decorator Pattern in PHP"
date: '2025-08-14T20:52:30+01:00'
category: webclip
summary: 'The page shows how the Decorator Pattern avoids class explosion in PHP by wrapping a base object with small decorators that add features at runtime. It contrasts this with inheritance-heavy combinations and a large factory switch.'
tags: ["php", "decorator-pattern", "design-patterns", "object-oriented-programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Mastering the Decorator Pattern in PHP: From Code Explosion to Elegant Solutions | by Murilo Livorato | Jul, 2025 | Medium"
    url: "https://medium.com/@murilolivorato/mastering-the-decorator-pattern-in-php-from-code-explosion-to-elegant-solutions-75fb47c8f458"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/medium-com--mastering-the-decorator-pattern-in-php.md"
    kind: repo
---

The page argues that building a separate class for every feature combination leads to class explosion, duplicated logic, and a maintenance burden. Using the Decorator Pattern keeps the base object simple and lets behavior be added by wrapping it with focused decorators.

## Reading notes

- A coffee-shop example shows how combinations of milk, sugar, whipped cream, vanilla, and other add-ons can quickly grow into many classes.
- The article says this approach creates exponential growth, with up to 2^n classes for n ingredients.
- A factory based on ingredient combinations becomes hard to manage and throws exceptions for unsupported combinations.
- The Decorator Pattern is presented as a structural pattern that adds behavior by placing an object inside wrapper objects.
- The pattern is broken into four parts: component interface, concrete component, decorator, and concrete decorators.
- In the coffee example, SimpleCoffee implements the interface and CoffeeDecorator stores another Coffee object.
- MilkDecorator, SugarDecorator, and WhippedCreamDecorator each extend CoffeeDecorator and add to cost and description.
- The page shows that decorators can be chained to build combinations such as coffee with milk, sugar, and whipped cream.
- A VanillaDecorator example shows that adding a new feature requires only one new decorator class.
- An image upload example uses decorators to add resize, watermark, and compression steps around a base uploader.
- The uploader decorators call the wrapped uploader first and then run their own behavior.
- The article says the pattern is useful when responsibilities must be added dynamically, class explosion must be avoided, and each piece should keep a single responsibility.
- It lists UI components, file operations, text processing, HTTP requests, and database operations as common use cases.
- Best practices include keeping interfaces simple, making each decorator do one job, paying attention to order, documenting behavior, and favoring composition over inheritance.
- The disadvantages mentioned are many small classes, more complexity, harder debugging, and decorator stacks that can be difficult to understand.
