---
title: "A Simplified Version of Google's Spell Checker"
date: '2016-05-13T14:55:25-03:00'
category: webclip
summary: 'Peter Norvig explains a 20-line Python spell checker that uses word counts from a text file and edit distance to choose the most frequent correction. The post says the simple method solved more than 80% of test cases.'
tags: ["spell-checker", "python", "edit-distance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A Simplified Version of Google's Spell Checker"
    url: "http://googlesystem.blogspot.com/2007/04/simplified-version-of-googles-spell.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-05/googlesystem-blogspot-com--a-simplified-version-of-googles-spell-checker.md"
    kind: repo
---

Peter Norvig explains a spell checker in 20 lines of Python that works almost as well as Google's "did you mean" corrections for one-word errors. It reads a text file, counts word frequencies, generates possible corrections by edit distance, and picks the most frequent candidate.

## Reading notes

- It uses holmes.txt, a Project Gutenberg collection of Sherlock Holmes stories, as the training text.
- The words are converted to lowercase before counting, so "the" and "The" are treated the same.
- The error model gives edit distance 1 candidates much higher probability than edit distance 2 candidates, and both are less likely than an exact match.
- The post lists the four edit operations: deletion, transposition, alteration, and insertion.
- Norvig's tests gave correct answers in more than 80% of cases.
- The post notes that Google can improve on this because it has much more data, including web queries and refinements.
