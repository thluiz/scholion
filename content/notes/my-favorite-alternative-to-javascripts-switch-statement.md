---
title: "My favorite alternative to JavaScript’s switch statement"
date: '2013-05-24T10:21:28-03:00'
category: webclip
summary: 'The post argues that JavaScript switch statements become cumbersome, and shows how object literals and first-class functions can replace them with code that is more modular and easier to extend.'
tags: ["javascript", "switch-statement", "first-class-functions", "maintainability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "My favorite alternative to JavaScript's switch statement » Encosia"
    url: "http://encosia.com/first-class-functions-as-an-alternative-to-javascripts-switch-statement/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-05/encosia-com--my-favorite-alternative-to-javascripts-switch-statement.md"
    kind: repo
---

The post argues that JavaScript’s `switch` statement often becomes clumsy as code grows, and that object literals plus first-class functions offer a cleaner alternative. It uses invoice pricing as the example and shows how the pricing rules can be separated from the pricing logic.

## Reading notes

- `switch` is described as a common but cumbersome construct that tends to grow in size and complexity over time.
- JavaScript’s object literal syntax and first-class functions are presented as cleaner, more extensible alternatives.
- The pricing example starts with a `switch` that applies different discounts by customer type.
- The same logic is then rewritten with an object literal that stores discount values by customer type.
- A further rewrite uses functions as the values in that object so each customer type can contain its own pricing logic.
- The functional version allows arbitrary code inside each rule, including a condition for Preferred customers that only applies the discount to items up to $100.
- The method that calculates price only needs to choose the right function and does not need to know how pricing works internally.
- The pricing rules can live in separate files, which makes it easy to add a new pricing type by adding a new file and key/function pair.
- The author says this approach improves flexibility and modularity and helps avoid regression risk from centralized logic.
