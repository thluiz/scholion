---
title: "Data evolution with set-theoretic types"
date: '2026-09-24T23:31:16+01:00'
category: webclip
summary: 'The text proposes using set-theoretic types and revisions in structs to maintain compatibility as data evolves, preserving type safety between old and new versions.'
tags: ["elixir","types","structs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Data evolution with set-theoretic types"
    url: "https://dashbit.co/blog/data-evolution-with-set-theoretic-types"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dashbit-co--data-evolution-with-set-theoretic-types.md"
    kind: repo
---

The article argues that libraries need a way to evolve public data definitions without forcing breaking changes on every consumer. It uses an Elixir struct example to show how set-theoretic types, structural subtyping, and explicit revisions could let old and new versions of a struct coexist while preserving type safety.

It proposes that the compiler rewrite a generic `Schema.t()` signature into version-aware signatures that preserve the revision of the input. The same idea is extended to multiple fields, transitive dependencies, downcasting, and higher-order functions, with the compiler enforcing that each new revision is a supertype of the previous one.

## Reading notes

- The text starts from a case in Rust and C in which a field that should accept `null` ended up causing incompatibility between libraries.
- The most correct change would be to make the `name` field optional, but that would break existing users of the library.
- Converting `null` into an empty string preserves compatibility, but keeps the type divergent from the specification.
- The article wants to show how set-theoretic types can help libraries evolve public data definitions without losing type safety.
- The discussion takes Elixir as a testbed to explore structs, structural subtypes, and revisions.
- In nominal types, changing the definition of a struct changes the type associated with all values instantiated with it.
- With structural subtyping, the type depends on the effective fields of the value, so broadening the definition of the struct does not change already instantiated data.
- The problem appears in functions: a function that received a struct with `name` as a string starts to fail type checking when the field starts to accept `nil`.
- The text argues that a new version of the struct can coexist with the old one without invalidating old code, because the presence of `nil` does not yet exist in the old values.
- For this, the article proposes explicit revisions in structs, with revision 1 corresponding to the original fields and revision 2 broadening types.
- `Schema.t()` comes to represent the most recent revision, but the type can be explicitly refined by field.
- The central property proposed is that a function preserve the revision it receives: if it receives an old revision, it returns the same revision; if it receives a new revision, it returns the new revision.
- The text says this can be expressed with intersection types, generating different signatures for each compatible revision.
- When there are multiple revised fields, the number of cases to check grows with the number of changed fields.
- The author suggests that users explicitly choose which revisions they accept, being more useful for library authors than for common applications.
- The revision configuration also applies to transitive dependencies, allowing valid combinations as long as revisions are not removed when going down the dependency tree.
- The text shows that it is possible to downcast a new revision to an old one, either by filling the field with an empty string or by failing at runtime when the value is not compatible.
- In the formalization, the compiler generates one clause per revision, with the domain restricted by the previous types and the codomain accumulating the previous and current revisions.
- The text also discusses higher-order functions and shows that the resulting semantics preserve the safest possible reading for inputs and outputs.
- The changes allowed in a revision are making a field broader, adding a field with a default value, and marking a field as obsolete.
- Removing fields, narrowing types, or using disjoint types is treated as a breaking change.
- The conclusion is that revisions could make data evolution progressive and safe for libraries, especially in the Elixir ecosystem.
