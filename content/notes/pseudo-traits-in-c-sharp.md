---
title: "Pseudo Traits in C#"
date: '2019-09-05T17:00:58+00:00'
category: webclip
summary: 'The post shows how C# 8.0 default interface implementations inspired a trait-like pattern in C# 7.0 using marker interfaces and extension methods, letting empty classes gain behavior by implementing the right interfaces.'
tags: ["csharp", "traits", "interfaces", "extension-methods"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Pseudo Traits in C#"
    url: "https://dev.to/htissink/pseudo-traits-in-c-lnp"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--pseudo-traits-in-c-sharp.md"
    kind: repo
---

The post argues that C# 8.0 interfaces with default implementations resemble traits, but treats that idea as controversial. It then presents a C# 7.0 experiment that uses marker interfaces, an abstract `Trait` base class, and extension methods to attach behavior to classes without putting code in the classes themselves.

## Reading notes

- C# 8.0 interfaces with default implementations are presented as a bad fit for the idea of an interface.
- Traits are described as a construct that attaches default behavior to objects through the traits they exhibit.
- The examples use `Runner`, `Swimmer`, and `Flyer` as trait-like behaviors.
- Swift is mentioned as a language that fits this style well through protocol extensions.
- The C# experiment starts from shapes that can roll, bounce, or both.
- The pattern uses an abstract `Trait` class and `ITrait<T>` as a filter for trait types.
- `CanRoll` and `CanBounce` are defined as trait types.
- `ShapeTraits` adds `Roll` and `Bounce` extension methods for the matching trait interfaces.
- `Cylinder`, `Cube`, and `Ball` implement the relevant interfaces and get behavior from the extensions.
- The author calls the result “pseudo traits” and presents it as a thought experiment rather than recommended practice.
