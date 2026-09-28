---
title: "SOLID: The First 5 Principles of Object Oriented Design"
date: '2022-08-10T08:48:11-03:00'
category: webclip
summary: 'The article defines SOLID and explains each principle with PHP examples, showing how they improve extensibility, reduce coupling, and keep classes focused as software grows.'
tags: ["solid", "object-oriented-design", "php", "software-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "SOLID: The First 5 Principles of Object Oriented Design | DigitalOcean"
    url: "https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-08/digitalocean-com--solid-first-five-principles-object-oriented-design.md"
    kind: repo
---

The page introduces SOLID as the first five object-oriented design principles by Robert C. Martin and says they support software that is easier to maintain, extend, refactor, and adapt as it grows. It uses PHP examples to show how each principle changes the way classes and interfaces are organized.

## Reading notes

- SRP says a class should have one reason to change, so the article splits shape calculation from output formatting by moving JSON and HTML rendering into a separate outputter class.
- OCP says classes should be open for extension and closed for modification, so shape-specific area logic moves into each shape class instead of adding more conditional branches in `AreaCalculator`.
- To support OCP safely, the article introduces `ShapeInterface` and checks that each shape passed to the calculator implements `area()`.
- LSP is illustrated with `VolumeCalculator`, where a subtype must remain usable where the parent type is expected; returning an array from `sum()` breaks the outputter, so the subclass must return a compatible value.
- ISP says clients should not be forced to depend on methods they do not use, so the article separates flat-shape and three-dimensional shape contracts instead of making every shape implement `volume()`.
- The article also proposes a `ManageShapeInterface` with `calculate()` as a single API for handling both flat and 3D shapes.
- DIP says high-level modules should depend on abstractions, not concrete classes, so `PasswordReminder` depends on `DBConnectionInterface` rather than `MySQLConnection`.
- The conclusion says projects following SOLID are easier to share, extend, modify, test, and refactor with fewer complications.
