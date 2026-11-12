---
title: "The C Trilogy: How Dennis Ritchie, Bjarne Stroustrup, and Anders Hejlsberg Built the Modern World"
date: '2026-11-12T13:07:38+00:00'
category: webclip
summary: 'The article contrasts C, C++, and C# as three responses to the same problem: writing large programs without corrupting memory, and shows how each language still supports a different layer of modern software.'
tags: ["c", "c-plus-plus", "c-sharp", "programming-languages"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The C Trilogy: How Dennis Ritchie, Bjarne Stroustrup, and Anders Hejlsberg Built the Modern World 🏛️"
    url: "https://dev.to/devengers/the-c-trilogy-how-dennis-ritchie-bjarne-stroustrup-and-anders-hejlsberg-built-the-modern-world-1onp"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--the-c-trilogy-how-dennis-ritchie-bjarne-stroustrup-and-ander.md"
    kind: repo
---

The article presents C, C++, and C# as three solutions to the same problem of building large software without corrupting memory. C focuses on direct hardware control, C++ adds zero-cost abstractions and RAII, and C# shifts memory management to the runtime while keeping performance tools available.

## Reading notes

- C was created at Bell Labs to write operating systems in a language closer to hardware than assembly.
- Its rule is to trust the programmer, so memory must be managed manually with malloc and free.
- C became the base layer for systems such as Linux, Windows, macOS, Git, PostgreSQL, and Python's C runtime.
- C++ grew out of the need to handle larger software with abstractions while keeping C-level speed.
- Its design follows the idea of zero-cost abstractions and uses RAII so resources are cleaned up when objects leave scope.
- C++ is presented as a fit for game engines, browsers, financial trading, and aerospace software.
- C# was created at Microsoft after the Visual J++ dispute with Sun and was led by Anders Hejlsberg.
- It combines C-like syntax with the CLR and garbage collection, while still allowing unsafe code and Span<T> for low-level work.
- The article places C# in web backends, cloud software, and Unity development.
- The three languages are framed as occupying different layers of the stack rather than directly replacing one another.

## Related notes

- [C# is language of the year, Python of the decade](/notes/c-sharp-is-language-of-the-year-python-of-decade/)
- [Andrei Alexandrescu answer on C replacement languages](/notes/andrei-alexandrescu-answer-on-c-replacement-languages/)
- [The 8 most in-demand programming languages of 2016](/notes/the-8-most-in-demand-programming-languages-of-2016/)
