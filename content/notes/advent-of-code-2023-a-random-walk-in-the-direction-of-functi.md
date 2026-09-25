---
title: "F# Advent of Code 2023: A random walk in the direction of functional enlightenment"
date: '2026-09-25T20:38:17+01:00'
category: webclip
summary: 'The post follows Scott’s refactoring of old Grace CLI code to make it more idiomatic F#, showing how smaller functions, less duplication, and monadic bind improve clarity while exposing older bugs.'
tags: ["f-sharp", "functional-programming", "refactoring", "grace"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "F# Advent of Code 2023: A random walk in the direction of functional enlightenment"
    url: "https://scottarbeit.com/blog/advent-of-code-2023-a-random-walk-in-the-direction-of-functional-enlightenment"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/scottarbeit-com--advent-of-code-2023-a-random-walk-in-the-direction-of-functi.md"
    kind: repo
---

Scott uses a refactor of old Grace CLI code to show how his F# practice has changed. He rewrites `grace switch` into smaller functions, reduces duplicated logic across output modes, and uses a custom bind for `Task<Result<...>>` to make the flow easier to follow.

He also uses the refactor to surface older bugs and to argue for shorter, more focused functions. The post treats the work as part of a larger learning process in F#, with examples from CLI handling, server validations, and JSON helpers.

## Reading notes

- The post starts from the author’s frustration with old Grace code and uses that as the subject of the article.
- `grace switch` is refactored first because it is the longest and most complex CLI command, even though that makes it the hardest case.
- The old version duplicated most of the logic for different output modes.
- The new version extracts the work into smaller functions and uses a custom `>>=!` operator for `Task<Result<...>>`.
- The refactor makes the code easier to understand, but it also reveals bugs that go back to the earlier implementation of `grace watch` and `grace switch`.
- The author describes `getNewGraceStatusAndDirectoryVersions` as too long and hard to maintain.
- He says code should not require telling a story to explain why it is shaped the way it is.
- He connects that rule to breaking large functions into smaller pieces.
- He says his F# practice is now better at judging function size and complexity.
- He says he is comfortable using functions as first-class values and using classes only when they make sense.
- He gives examples of validation arrays for server endpoints and small JSON serialize and deserialize helpers.
- He says he has more to learn, including SRTP, type providers, custom computation expressions, category theory, and Haskell.
- He closes by saying he is no longer at the start of the journey, but also not near the end, and that progress over time is worth being proud of.
