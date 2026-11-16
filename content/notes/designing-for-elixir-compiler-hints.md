---
title: "Designing For Elixir Compiler Hints"
date: '2026-11-16T20:08:27+00:00'
category: webclip
summary: 'Author examines Elixir 1.11 struct-field compile-time checks, arguing they give limited benefit, complicate polymorphic design, and shouldn’t drive application architecture.'
tags: ["elixir", "compiler", "structs", "dialyzer"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Designing For Elixir Compiler Hints"
    url: "https://devonestes.com/designing-for-elixir-compiler-hints"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--designing-for-elixir-compiler-hints.md"
    kind: repo
---

The text discusses new compile-time checks in Elixir 1.11 for non-existent struct fields and how they work only when the compiler knows a variable’s struct type locally. It notes that similar safety has long been achievable via pattern matching and tools like Dialyzer, and argues that the new checks offer modest value compared to their impact on design, especially with polymorphic functions. The author warns against reshaping domain models and adding layers of structs just to satisfy compiler hints, recommending simpler designs that use pattern matching and static analysis tools instead of bending architectures around current compiler capabilities.

## Reading notes

- Elixir 1.11 introduces compile-time checks for accessing fields that don’t exist on structs, which previously only failed at runtime.
- To trigger these warnings, code must explicitly bind a variable to a specific struct type (e.g. `%DateTime{} = DateTime.utc_now()`); otherwise the compiler cannot validate field access.
- The struct-type knowledge is scoped to a single function definition, so passing a struct to another function without a typed pattern in the callee prevents the warning.
- A changelog note suggests that in future versions the compiler may track struct types across functions and possibly modules for broader checks.
- The author points out that compile-time detection of wrong struct fields has been possible by pattern matching on the struct and binding fields, which already fails at compile time.
- Dialyzer would also detect these erroneous field accesses in all showcased versions of the code, though its error messages are described as not very clear.
- For polymorphic code that works with multiple date-like structs, insisting on compiler hints forces a choice between multiple function heads per struct type or normalizing all inputs to a single struct type.
- Duplicating function heads for each struct type is seen as simple to implement but high in duplication cost relative to the benefit of catching typos.
- Converting all variants to a single struct type (e.g. turning `DateTime` into `NaiveDateTime`) may be manageable in small examples but can complicate larger applications.
- The author questions whether domain models should introduce new structs for each abstraction level purely to gain extra typo protection on field names.
- They argue that Dialyzer already offers similar protection with far less structural overhead, making the added complexity of reshaping code for compiler hints hard to justify.
- One anticipated misuse is defining dedicated parameter structs for HTTP endpoints (e.g. `CreateParams` in a controller) purely to validate field names, even though inputs are still subject to separate validation logic.
- Another concern is creating generic abstraction structs (like `Creatable`) to work around polymorphism in domain logic, leading to extra transformations and indirection.
- The author fears a trend where developers contort application designs "in the name of safety" to align with the current form of compiler checks.
- They suggest that if future compiler features can fully replace Dialyzer with clearer messages, that would be positive, but evaluate the present feature as not yet at that point.
- As a practical guideline, they recommend favoring pattern matching to gain some compile-time guarantees instead of rearchitecting for the new struct-field warnings.
- The closing advice is to design applications as simply as possible and then apply available tools for added safety, rather than shaping designs around present tool limitations that will continue to evolve.
- The author concedes that if struct field typos are a significant recurring issue for a team, heavy use of this feature might be justified, but they personally doubt that benefit typically outweighs the duplication and complexity costs.
