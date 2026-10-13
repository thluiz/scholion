---
title: "Some practices to write better C#/.NET code"
date: '2013-09-27T15:47:50-03:00'
category: webclip
summary: 'The article argues that readable C#/.NET code depends on conventions, clear naming, small classes and methods, fewer parameters, simpler expressions, and disciplined review and tooling.'
tags: ["csharp", "dotnet", "coding-conventions", "readability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Some practices to write better C#/.NET code"
    url: "http://www.codeproject.com/Articles/539179/Some-practices-to-write-better-Csharp-NET-code"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-09/codeproject-com--some-practices-to-write-better-csharp-dotnet-code.md"
    kind: repo
---

The article argues that code should be written for people first and computers second. It uses FizzBuzz examples to show how naming and structure affect readability, then recommends conventions, smaller classes and methods, fewer parameters, clearer expressions, and treating warnings seriously.

## Reading notes

- Coding standards matter because they create consistency across a project.
- Naming is one of the hardest parts of software work, and names add meaning to code.
- Readable code helps during reviews, fixes, changes, and reuse in other projects.
- To improve readability, read other people’s code, compare good and bad patterns, and practice.
- Tools mentioned for enforcing style and analysis include FxCop, StyleCop, and ReSharper.
- Coding conventions cover indentation, comments, declarations, whitespace, naming, and programming practices.
- PascalCase is recommended for class and method names.
- camelCase is recommended for method arguments and local variables.
- Abbreviations and underscores in identifiers are discouraged.
- Interfaces should start with I.
- Member variables should be declared at the top of a class, with static variables first.
- Enum names should be singular, and should not end with Enum.
- Conventions help transfer knowledge across projects, speed up learning on new projects, and show relationships among related items.
- Large classes often violate the Single Responsibility Principle and should be split.
- Obsolete comments should be removed or updated, and method names are often better than comments.
- Regions can hide code that should instead be moved into separate classes.
- Long methods should be refactored, often with Extract Method.
- Too many parameters can be replaced by a class that groups related data.
- Complex expressions should be hidden behind clearer properties or abstractions.
- Warnings should be treated as errors.
- Multiple returns should be minimized when they make routines harder to follow.
- Variable declarations should be placed near first use.
- Assertions are for checking assumptions during development.
- Loop endpoints should be tested carefully, including first, middle, and last cases.
