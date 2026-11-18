---
title: "The Dream of C# 9.0"
date: '2019-12-30T08:16:43+00:00'
category: webclip
summary: 'The article highlights C# 9 proposals that would make the language more concise and more open to functional programming, especially simplified null checks, primary constructors, records, and discriminated unions.'
tags: ["csharp", "functional-programming", "language-design", "dotnet"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Dream of C# 9.0"
    url: "https://dev.to/integerman/the-dream-of-c-9-0-5fc7"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--the-dream-of-csharp-90.md"
    kind: repo
---

The article looks at several C# 9 proposals and focuses on how they could make the language more concise while supporting more functional programming techniques. It treats the features as proposals, not final decisions, and reads them as a sign of where C# may be headed.

## Reading notes

- Simplified null validation could make argument checks shorter and more visible to callers through IntelliSense.
- The author prefers C# 8 null validation, but sees value in the new syntax and in combining both approaches for readability and documentation.
- Primary constructors would reduce boilerplate and make class constructors closer to the concise style used in TypeScript and F#.
- Record classes are presented as a compact way to model data objects with no methods.
- The author sees records as related to primary constructors and as a step toward more advanced features.
- Discriminated unions are described as the most desired feature, because they would let code match on one of several possible types directly.
- The proposed enum class approach could support switch-based matching on different cases.
- The author says this proposal is still volatile and may change or disappear.
- The closing argument is that C# keeps moving toward functional programming support while remaining adaptable over time.
