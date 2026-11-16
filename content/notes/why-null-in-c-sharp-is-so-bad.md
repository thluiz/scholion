---
title: "Why null in C# is so bad"
date: '2026-11-16T01:42:28+00:00'
category: webclip
summary: 'The article argues that null breaks language assumptions, forces defensive branching, and causes bugs and NullReferenceException. It recommends nullable reference checks in C# 8.0 for new projects.'
tags: ["csharp", "null", "nullable-reference-types"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why null in C# is so bad"
    url: "https://dev.to/mbernard/why-null-in-c-is-so-bad-cid"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--why-null-in-c-sharp-is-so-bad.md"
    kind: repo
---

The article argues that null is a major source of bugs in C# because it breaks assumptions about types and behavior. It frames null as a special value that can stand in for any reference type, which forces code to branch and handle a separate null case.

It presents defensive null checks as verbose and easy to forget, making NullReferenceException likely in production. As the practical fix, it recommends enabling C# 8.0 nullable reference types with `<Nullable>enable</Nullable>`, especially in greenfield projects.

## Reading notes

- More than half of the author’s bugs were related to null values propagating where they should not have been.
- The null problem is described as the “billion-dollar mistake” because it breaks assumptions about the language.
- The article links this to the Liskov substitution principle, where subtypes should be usable in place of parent types without changing behavior.
- Null is presented as a special instruction that can substitute any type, so code must check whether a value is null before using it.
- Defensive programming with null checks makes code verbose and error-prone, and missing one check can lead to NullReferenceException in production.
- The Elvis operator `?.` is described as improving readability, but not solving the underlying issue.
- The only real solution presented is to avoid null altogether, though the author says this is hard to enforce across a team.
- C# 8.0 nullable reference types are presented as the main tool to let the compiler check null across code paths.
- The suggested project setting is `<Nullable>enable</Nullable>` in the `.csproj` file.
- The author recommends enabling it for greenfield projects, even if it may break an existing brownfield project at first.
