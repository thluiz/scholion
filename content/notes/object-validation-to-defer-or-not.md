---
title: "Object Validation: to Defer or Not?"
date: '2020-04-20T21:22:21+00:00'
category: webclip
summary: 'The article distinguishes constructor checks that protect object state from later checks that affect runtime behavior. Nil and wrong-type arguments belong in the constructor; file existence and file kind belong in the method.'
tags: ["object-validation", "constructors", "runtime-behavior", "rubys"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Object Validation: to Defer or Not?"
    url: "https://yegor256.com/2018/05/29/object-validation.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--object-validation-to-defer-or-not.md"
    kind: repo
---

The article separates two kinds of validation. A constructor should reject values that an object cannot represent as part of its state, such as nil or a non-String file name. Checks about whether the file exists or is actually a file belong later, when the object is used.

## Reading notes

- Constructors should stay focused on attribute initialization, but they may validate arguments that would make object state invalid.
- In the example, nil and non-String input are rejected in the constructor because the `Users` object cannot represent those values.
- Existence and file checks are done in `names`, because they affect runtime behavior rather than object state.
- The article describes two phases of interaction with an object: connecting and talking.
- During connecting, validation confirms that the object is suitable to work with later.
- During talking, validation may need to happen again because the situation can change over time.
- Strong typing can catch some of these errors earlier, and Kotlin null safety can remove the need for explicit nil checks.
- Ruby lacks those protections, so the checks must be done manually.
