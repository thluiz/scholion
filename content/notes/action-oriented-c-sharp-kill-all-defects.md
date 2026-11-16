---
title: "Action-Oriented C# - Kill All Defects"
date: '2020-02-22T12:11:45+00:00'
category: webclip
summary: 'The post argues that passing Action and Func delegates adds configurable behavior, reduces duplicated patterns, and makes code easier to maintain even if the syntax is a bit harder to read.'
tags: ["c-sharp", "functional-programming", "delegates", "maintainability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Action-Oriented C# - Kill All Defects"
    url: "https://web.archive.org/web/20191206183600id_/https://killalldefects.com/2019/09/15/action-oriented-c/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--action-oriented-c-sharp-kill-all-defects.md"
    kind: repo
---

The post describes a point where code quality and flexibility stopped improving, even though the code already followed SOLID principles. The author then uses Action and Func to replace repeated patterns, especially where a condition controls whether custom logic runs and where the same change would otherwise need to be made in several places.

The main idea is that passing delegates makes methods more configurable. Action is presented as a method signature with no return value, while Func returns a value. Using a lambda expression in a Func call can shorten the calling code, and the author says this can improve maintainability and reduce defects from duplication, even if the syntax is a little harder to read.

## Reading notes

- The author reached a plateau where code quality and flexibility stopped improving.
- The code was already pretty SOLID, but it still had many similar patterns that made maintenance harder.
- A repeated routine checked a property, ran custom logic only when the property was true, and stored the result on the object.
- The pattern resisted method extraction because some calculation methods could not run unless the related degree was present.
- A bug or code change in that pattern could require updating the same logic in three places.
- Copy / paste driven development is described as an anti-pattern and a source of bugs when changes are not applied everywhere.
- Passing Action and Func types gives methods configurable behavior.
- Action is described as a generic signature for invoking a method without a return type.
- Func is described as similar to Action, except that it returns a value, with the last generic type argument as the return type.
- A Func can be used to extract a method with configurable behavior.
- Lambda expressions are used in the example and are compared to those used in LINQ queries.
- The syntax is harder to read, but the maintainability benefits are presented as real.
- The post frames this as a useful idea from functional programming that can also help in object-oriented programming.
