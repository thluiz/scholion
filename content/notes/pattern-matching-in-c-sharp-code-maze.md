---
title: "Pattern Matching in C#"
date: '2022-06-16T09:27:02-03:00'
category: webclip
summary: 'The article explains pattern matching in C# as a way to replace nested conditionals with clearer checks on type, value, ranges, properties, tuples, and stored results.'
tags: ["csharp", "pattern-matching", "switch-expression"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Pattern Matching in C# - Code Maze"
    url: "https://code-maze.com/csharp-pattern-matching/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-06/code-maze-com--pattern-matching-in-c-sharp-code-maze.md"
    kind: repo
---

The article presents pattern matching in C# as a modern way to make decisions based on type, value, ranges, properties, or multiple inputs at once. It shows how `switch`, `is`, and switch expressions can replace longer nested `if` chains with simpler code.

## Reading notes

- Type patterns check whether an expression is non-null and whether it matches a specified type, with examples using `Animal`, `Cat`, and `Dog`.
- Constant patterns compare a value against fixed strings such as "Meow" and "Bark".
- Relational patterns use operators like `<`, `>`, `<=`, and `>=` to return different messages for numeric ranges.
- Logical patterns combine `and`, `or`, and `not` with other patterns, including null checks and age ranges.
- Property patterns match a non-null object by checking named properties such as `Name`, `Description`, and `Cloned`.
- Positional patterns compare multiple values together by turning method arguments into a tuple.
- Var patterns store a value temporarily from an expression and then test the stored result against other conditions.
