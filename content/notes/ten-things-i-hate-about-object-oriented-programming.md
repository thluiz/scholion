---
title: "Ten Things I Hate About Object-Oriented Programming"
date: '2020-02-22T12:11:52+00:00'
category: webclip
summary: 'The essay argues that OOP lacks a stable core paradigm, blurs code and running objects, and still leaves major gaps around change, tools, types, and modeling.'
tags: ["object-oriented-programming", "software-design", "programming-languages", "modeling"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Ten Things I Hate About Object-Oriented Programming — The JOT Blog"
    url: "https://blog.jot.fm/2010/08/26/ten-things-i-hate-about-object-oriented-programming"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-jot-fm--ten-things-i-hate-about-object-oriented-programming.md"
    kind: repo
---

The essay treats object-oriented programming as a moving target rather than a settled paradigm. It says OOP is framed in conflicting ways, from objects and classes to encapsulation and reuse, and argues that its real point is programming as modeling. It also says OOP tools and languages often expose classes in the source while hiding the runtime objects and their interactions.

## Reading notes

- OOP is presented as hard to define because different accounts emphasize different features, and none of them fully captures it.
- The text rejects the idea that reuse, design flow, or a simple formula of objects and messages explains the paradigm.
- It argues that OOP is really about letting each problem shape its own way of modeling.
- The essay contrasts the way people praise and attack different OOP languages, especially C++, Java, and Smalltalk.
- Classes are criticized because they are mental constructs, while programs run with objects.
- The author says source code and runtime behavior are disconnected in OOP, and current IDEs reinforce that gap.
- Methods are described as too fragmented for reading code efficiently, since developers spend time jumping among many small pieces.
- The text calls for tools that let developers move between a running application and its code.
- Types are said to create false confidence, to assume consistency the world does not have, and to struggle with multiple useful type systems.
- Change is treated as the central problem, and context is proposed as a first-class concept that languages and IDEs should support.
- Design patterns are described as adding complexity, with Visitor used as an example.
- Methodologies are mocked as fear-driven, and UML is criticized because diagrams do not fail at runtime.
- The conclusion says OOP has lasted longer than expected and that its deeper value may lie in helping manage complexity and change.
