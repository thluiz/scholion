---
url: "https://quantamagazine.org/barbara-liskov-is-the-architect-of-modern-algorithms-20191120"
captured_at: "2026-11-16T02:53:35+00:00"
title: "The Architect of Modern Algorithms"
domain: "quantamagazine-org"
---

Good code has both substance and style. It provides all necessary information, without extraneous details. It bypasses inefficiencies and bugs. It is accurate, succinct and eloquent enough to be read and understood by humans.

But by the late 1960s, advances in computing power had outpaced the abilities of programmers. Many computer scientists created programs without thought for design. They wrote long, incoherent algorithms riddled with “goto” statements — instructions for the machine to leap to a new part of the program if a certain condition is satisfied. Early coders relied on these statements to fix unforeseen consequences of their code, but they made programs hard to read, unpredictable and even dangerous. Bad software eventually claimed lives, as when the [Therac-25 (opens a new tab)](https://www.computer.org/csdl/magazine/co/2017/11/mco2017110008/13rRUxAStVR) computer-controlled radiation machine delivered massive overdoses of radiation to cancer patients.

By the time [Barbara Liskov (opens a new tab)](https://www.csail.mit.edu/person/barbara-liskov) earned her doctorate in computer science from Stanford University in 1968, she envied electrical engineers because they worked with hardware connected by wires. That architecture naturally allowed them to break up problems and divide them into modules, an approach that gave them more control since it permitted them to reason independently about discrete components.

As a computer scientist thinking about code, Liskov had no physical objects to work with. Like a novelist or a poet, she was staring at a blank page.

Liskov, who had studied mathematics as an undergraduate at the University of California, Berkeley, wanted to approach programming not as a technical problem, but as a mathematical problem — something that could be informed and guided by logical principles and aesthetic beauty. She wanted to organize software so that she could exercise control over it, while also making sense of its complexity.

When she was still a young professor at the Massachusetts Institute of Technology, she led the team that created the first programming language that did not rely on goto statements. The language, CLU (short for “cluster”), relied on an approach she invented — data abstraction — that organized code into modules. Every important programming language used today, including Java, C++ and C#, is a descendant of CLU.

“One advantage to being in the field so early was that great problems were sitting there. All you had to do was jump on them,” said Liskov. In 2008, [Liskov won the Turing Award (opens a new tab)](http://amturing.acm.org/award_winners/liskov_1108679.cfm) — often called the Nobel Prize of computing — for “contributions to practical and theoretical foundations of programming language and system design, especially related to data abstraction, fault tolerance, and distributed computing.”

_Quanta Magazine_ caught up with Liskov at her home following the Heidelberg Laureate Forum — an intimate, invitation-only gathering of computer scientists and mathematicians who have earned the most prestigious awards in their fields. Liskov had been invited to Heidelberg but needed to cancel a few weeks before the forum for personal reasons. The interview has been condensed and edited for clarity.

### You came of age professionally during the development of artificial intelligence. How has thinking about AI and machine learning changed during your career?

I did my Ph.D. with [John McCarthy (opens a new tab)](http://amturing.acm.org/award_winners/mccarthy_1118322.cfm) in AI. I wrote a program to play chess endgames. John suggested this topic because I didn’t play chess. I read the \[chess\] textbooks and translated those algorithms into computer science. In those days, the perceived wisdom was to get the program to act the way a person would. That’s not how it is now.

Today, machine learning programs do a pretty good job most of the time, but they don’t always work. People don’t understand why they work or don’t work. If I’m working on a problem and need to understand exactly why an algorithm works, I’m not going to apply machine learning. On the other hand, one of my colleagues is analyzing mammograms with machine learning and finding evidence that cancer can be detected much earlier.

AI is an application rather than a core discipline. It’s always been used to do something.

### Were you more interested in it as a core discipline?

Honestly, AI couldn’t do much in those days. I was interested in the underlying work. “How do you organize software?” was a really interesting problem. In a design process, you’re faced with figuring out how to implement an application. You need to organize the code by breaking it into pieces. Data abstraction helps with this. It’s a lot like proving a theorem. You can’t prove a theorem in one fell swoop. Instead, you invent some lemmas and you decompose the problem.

In my version of computational thinking, I imagine an abstract machine with just the data types and operations that I want. If this machine existed, then I could write the program I want. But it doesn’t. Instead I have introduced a bunch of subproblems — the data types and operations — and I need to figure out how to implement them. I do this over and over until I’m working with a real machine or a real programming language. That’s the art of design.
