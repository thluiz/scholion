---
title: "What's Wrong With Object-Oriented Programming?"
date: '2020-02-22T12:11:52+00:00'
category: webclip
summary: 'The page collects objections to object-oriented programming from several programmers and authors, who argue that OO code often becomes verbose, hard to read, hard to maintain, and prone to growing complexity.'
tags: ["object-oriented-programming", "software-design", "complexity"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What's Wrong With Object-Oriented Programming?"
    url: "https://yegor256.com/2016/08/15/what-is-wrong-object-oriented-programming.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--whats-wrong-with-object-oriented-programming.md"
    kind: repo
---

The page gathers criticisms of object-oriented programming from several well-known programmers and authors. Across the quotes, the recurring concerns are verbosity, poor readability, difficult maintenance, and the way large object graphs can make complexity harder to manage.

## Reading notes

- The author says that a better understanding of an object in OOP could help solve problems in existing pseudo-object-oriented languages.
- The quotes are presented in chronological order.
- Edsger W. Dijkstra says object-oriented programs are offered as alternatives to correct ones.
- Alan Kay says he did not have C++ in mind when he coined object-oriented, and calls Java distressing.
- Paul Graham says object-oriented programming offers a sustainable way to write spaghetti code.
- Richard Mansfield says OOP-inflected languages make software more verbose, less readable, less descriptive, and harder to modify and maintain.
- Eric Raymond says OO proved valuable in graphics systems, GUIs, and some simulations, but that significant benefits outside those areas have been hard to demonstrate.
- Jeff Atwood says OO seems to bring at least as many problems as it solves.
- Linus Torvalds says C++ leads to bad design choices and that limiting a project to C can help avoid them.
- Oscar Nierstrasz says OOP aims to tame complexity through modeling, but that this has not been mastered yet.
- Rich Hickey says large object-oriented programs struggle with increasing complexity as mutable objects accumulate.
- Eric Allman says object-oriented programs can turn into horrid messes once they are used in real programs.
- Joe Armstrong says binding functions and data structures together is a fundamental error.
- Rob Pike says data is sometimes just data and functions are just functions.
- John Barker says OOP introduces abstractions that attempt to improve code sharing and security, while still being essentially procedural code.
- Lawrence Krubner says OOP is an experiment that failed and should be abandoned.
- Asaf Shelly says object-oriented code can hide the big picture and make review of changed functions difficult.
