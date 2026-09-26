---
title: "Minimising cognitive load in F#"
date: '2024-12-25T19:53:39+00:00'
category: webclip
summary: 'The post lists F# habits that make code easier to read by reducing cognitive load: isolate implementation details, use modules and names well, simplify matches, and avoid overly terse styles.'
tags: ["f-sharp", "cognitive-load", "readability", "code-style"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Minimising cognitive load in F# - Michael Winch - Medium"
    url: "https://medium.com/@michaeljwinch/minimising-cognitive-load-in-f-2d4baa94b740"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2024-12/medium-com--minimising-cognitive-load-in-f-sharp.md"
    kind: repo
---

The post argues that code becomes easier to understand when it reduces how much readers need to hold in memory at once. It recommends separating implementation details into small functions, organizing domain functions in modules, and naming things clearly so intent is visible without tracing every expression.

It also suggests using custom operators sparingly, simplifying match statements with active patterns, being careful about when to create new types, and using computation expressions when they remove repeated plumbing. The same caution applies to point-free style and partial application when they make the code harder to inspect.

## Reading notes

- Split implementation details into their own functions, then compose them instead of embedding complex predicates or reducers inline.
- Put functions that work on a domain type into a module named after that type, so their purpose and input are easier to infer and they are easier to find.
- Use custom operators only when their meaning is local or widely understood, because otherwise they make code harder to read.
- Use active patterns to turn match cases into business meanings that are easier to read than raw implementation logic.
- Name functions, variables, types, and other values clearly, even if the names are long, and ask a colleague when naming is unclear.
- Balance type reuse against over-modelling; sometimes a value can stay a simple int instead of becoming a more specialized type.
- Use computation expressions when they remove repeated map and bind plumbing.
- Prefer point-fewer code when point-free style or partial application hides what a function is operating on.
