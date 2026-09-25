---
title: "How to: Design for exception safety"
date: '2025-08-20T20:55:57+01:00'
category: webclip
summary: 'Explains how exception safety depends on RAII, simple resource classes, and the three guarantees: no-fail, strong, and basic. It also lists class-design rules for constructors, destructors, and ownership.'
tags: ["exception-safety", "raii", "smart-pointers", "c++"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to: Design for exception safety | Microsoft Learn"
    url: "https://learn.microsoft.com/en-us/cpp/cpp/how-to-design-for-exception-safety?view=msvc-170"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/learn-microsoft-com--design-for-exception-safety.md"
    kind: repo
---

The page says exception-safe code must let exceptions propagate or be handled without leaving partial objects, leaked memory, or unusable data structures behind. It recommends designing exception policy early, catching only when recovery is complete, and letting exceptions bubble up when lower layers lack context.

## Reading notes

- Keep resource wrapper classes simple and limited to a single resource.
- Prefer smart pointers when managing resources manually.
- Use RAII so allocated memory and released handles are tied to automatic object lifetimes.
- Treat `vector`, `string`, `make_shared`, and `fstream` as examples of types that manage acquisition for you.
- Distinguish the three guarantees: no-fail prevents propagation, strong leaves state unchanged on failure, and basic keeps the object usable with no leaks.
- Assume destructors do not throw when reasoning about the strong and basic guarantees.
- In user-defined types, use smart pointers or other RAII wrappers for resources.
- Use a function try block when a derived constructor needs to translate an exception from a base class constructor.
- Do not let exceptions escape from destructors; catch and swallow them if a destructor must run risky code.
