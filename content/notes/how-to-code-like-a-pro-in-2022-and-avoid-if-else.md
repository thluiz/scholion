---
title: "How to code like a pro in 2022 and avoid If-Else"
date: '2022-06-24T11:48:25-03:00'
category: webclip
summary: 'The post contrasts junior, mid-level, and senior approaches to branching, arguing that repeated If-Else chains should give way to switch statements, dictionaries, and reusable delegates with LINQ Any().'
tags: ["if-else", "switch", "delegates", "linq"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to code like a pro in 2022 and avoid If-Else"
    url: "https://thaitran.hashnode.dev/how-to-code-like-a-pro-in-2022-and-avoid-if-else?source=newsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-06/thaitran-hashnode-dev--how-to-code-like-a-pro-in-2022-and-avoid-if-else.md"
    kind: repo
---

The post argues that If-Else is useful early on, but senior developers should avoid it when possible. It contrasts simple branching with switch statements and then with a dictionary keyed by animal names, which the author presents as a more readable approach.

## Reading notes

- A junior developer is shown using repeated If-Else checks to map animal names to sounds.
- A mid-level developer replaces the If-Else chain with a switch statement for the same mapping.
- A senior developer stores animal names and sounds in a Dictionary<string, string> and uses TryGetValue.
- For a more complex case, the post uses input.Contains for keywords like Dog and Cat and filters breed arrays.
- The final version moves the action into a delegate, stores condition functions in an array, and calls them with LINQ Any().
- The author says this lets the evaluation stop on the first true condition and improves performance.
- The post ends by telling junior developers to learn these patterns and quotes advice about maintaining code.
