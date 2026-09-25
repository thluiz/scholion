---
title: "EP 66: Clean Code Tips for .NET Developers - Part I"
date: '2026-09-25T18:00:06+01:00'
category: webclip
summary: 'The post argues that clean code in .NET comes from meaningful names, avoiding null returns, keeping classes focused, limiting method size, reusing existing tools, and enforcing shared rules with EditorConfig and project settings.'
tags: ["clean-code", "dotnet", "csharp", "code-style"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "EP 66 : Clean Code Tips for .NET Developers - Part I"
    url: "https://mwaseemzakir.substack.com/p/ep-66-clean-code-tips-for-net-developers?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/mwaseemzakir-substack-com--ep-66-clean-code-tips-for-net-developers-part-i.md"
    kind: repo
---

The post collects several clean code habits for .NET work. It favors names that make code self-explanatory, recommends throwing exceptions instead of returning null in some cases, and encourages smaller classes with one reason to change. It also points to using existing logging tools, better IDE support, and project-wide configuration.

## Reading notes

- Meaningful names make code easier to understand and reduce the need for extra comments.
- Returning null can lead to NullReferenceException errors and makes callers check for null before using the value.
- A method or class should stay focused, with separate classes for validation, payment, inventory, email, and order processing when concerns are different.
- There is no hard rule for method length, but 20 to 40 lines is described as enough for a method.
- Reinventing the wheel wastes time and effort when logging is already available through ILogger and configured tools.
- Using the right IDE features helps with syntax highlighting, code completion, and early error checking.
- EditorConfig and project settings can apply common code rules across .NET projects.
