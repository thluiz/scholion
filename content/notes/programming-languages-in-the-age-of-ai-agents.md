---
title: "Programming Languages in the Age of AI Agents"
date: "2026-09-23T17:31:46+01:00"
category: webclip
has_commentary: false
summary: "If AI agents write the code, does language choice still matter? Alexandru Nedelcu argues static typing sharpens the agent's feedback loop, but comprehension debt stays a human problem."
tags:
  - ai-agents
  - programming-languages
  - type-systems
  - comprehension-debt
sources:
  - title: "Programming Languages in the Age of AI Agents - Alexandru Nedelcu"
    url: "https://alexn.org/blog/2025/11/16/programming-languages-in-the-age-of-ai-agents/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/alexn-org--programming-languages-in-the-age-of-ai-agents.md"
    kind: repo
---

Alexandru Nedelcu asks whether programming language choice still matters once AI agents are the ones writing the code, or whether everything converges on whatever the training corpus favors. Python's popularity is already a feedback loop this way: because there's more Python to train on, agents generate working Python more reliably, which makes Python more popular still. His answer for language enthusiasts is that there's reason for both worry and hope.

The hope rests on two things: a fast feedback loop for the agent, and reviewability for the human. A compiler with an expressive static type system, as in Scala, Haskell, or Rust, lets an agent iterate against real errors instead of guessing, which is why agents can produce working code even in something as fresh as Scala 3's macro system. But someone still has to read what was generated. Nedelcu names a specific risk he calls comprehension debt: agents have no persistent memory of the reasoning behind a change, so if no one on the team understands the system anymore, the project is in trouble regardless of how clean the code looks.

## Reading notes

- A language's popularity in AI training data is self-reinforcing: more Python in the corpus produces more working Python from agents, which produces more Python.
- Static, expressive type systems (Scala, Haskell, Rust) give agents a faster feedback loop than unit tests alone, letting them converge on compiling code through iteration against compiler errors.
- Running the program and checking the output is a superficial test; someone still needs to read the generated code and its tests to know whether edge cases were covered.
- Comprehension debt: agents don't retain the dialogue that produced a piece of code, and even saved chat logs make poor, easily misread documentation.
- Quotes Peter Naur's "Programming as Theory Building": software degrades when people who don't understand the original design concept modify it, because they invalidate rules they never held.
- Naur, via Nedelcu: sustaining a large program over time depends on a group of programmers who stay closely and continuously connected to it, not on the text of the program alone.
- Higher-level source code that expresses intent and design constraints matters for AI agents too, since assembly-level output can't losslessly carry that specification.
- Functional programming's equational reasoning stays valuable in this context because deductive reasoning is how humans verify code, and that's still needed when the code was written by "an inconsistent idiot that can't learn."
