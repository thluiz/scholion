---
title: "Alan Kay's answer to What thought process would lead one to invent object-oriented programming?"
date: '2026-11-16T05:31:12+00:00'
category: webclip
summary: 'Alan Kay says OOP came from systems thinking: he saw objects as a scalable way to model intercommunicating processes, inspired by Sketchpad, Simula, systems, and simulation, not by data-structure programming.'
tags: ["object-oriented-programming", "alan-kay", "systems-thinking", "simulation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Alan Kay's answer to What thought process would lead one to invent object-oriented programming? - Quora"
    url: "https://quora.com/What-thought-process-would-lead-one-to-invent-object-oriented-programming/answer/Alan-Kay-11"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/quora-com--alans-kays-answer-to-what-thought-process-would-lead-one-to-.md"
    kind: repo
---

Alan Kay says he coined “object oriented programming” in 1966 for work that he understood as a rotation and generalization of ideas he had seen in biology, programming, operating systems, Sketchpad, Simula, and networked computers. What struck him was that enough intercommunicating computers could define anything done on a computer, and that this scaled better than procedures and data structures.

He presents OOP as a way to design and program simulations of complex systems made of processes. In this view, objects can replace arrays, stacks, queues, and other data structures with entities that manage their own state, version histories, atomic transactions, and consistency. He says the idea was later narrowed in C++ and Java toward abstract data structures, while the original intent was broader and more systems-oriented.

## Reading notes

- He coined “object oriented programming” for work he was doing in 1966.
- The idea grew from earlier forms he had seen in biology, the Air Force, the B5000, operating systems, Sketchpad, Simula, and ARPAnet.
- What he saw as decisive was that enough intercommunicating computers could define anything that can be done on a computer.
- He preferred this idea because it scaled better than procedures and data structures as building blocks.
- Sketchpad and the first Simula pushed him toward thinking in terms of designing and programming simulations.
- He describes the model as “semantic software computers intercommunicating via messaging.”
- In this model, arrays are not the only possible structure; sparse matrices, stacks, and queues can be handled by processes that decide what assignment means internally.
- Objects can manage state more safely by versioning histories, doing atomic transactions, and allowing views only when relationships are consistent.
- He says the data idea was always a bad one, and that this paradigm lets objects progress through time and learn while staying safer.
- He frames the core thought process as systems thinking aimed at defining systems of processes.
- He says many readers associate OOP with C++ and Java, but that this is a narrower view.
- He argues that C++ and Java often use objects like data structures, which he treats as a divergence from the original intent.
- The value of the idea depends on skilled systems design.
- An object can simulate a function, a procedure, or a data structure, and it can also simulate smarter agencies and agents.
- He says few people understood the implications of “universal scalable systems of processes,” and many stayed with older programming styles.
- At Parc, they got more done in fewer lines because they tried to use the new way to organize and program complex systems.
