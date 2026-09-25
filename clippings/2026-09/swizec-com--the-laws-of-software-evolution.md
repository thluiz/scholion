---
url: "https://swizec.com/blog/the-laws-of-software-evolution/?ref=dailydev"
captured_at: "2026-09-25T21:17:14+01:00"
title: "The Laws of Software Evolution"
domain: "swizec-com"
---

![Swizec Teller](https://swizec.com/assets/swizec-byline-CCFrcNvL.jpg)

Large programs are never complete. They just continue to evolve forever because adding new functionality to existing systems feels easier than starting over.

One of the first to notice this was Manny Lehman who in 1980 published a prescient paper [Programs, Life Cycles, and Laws of Software Evolution](https://swizec.com/blog/pdfs/lehman.pdf). He classifies programs into 3 types, describes the ideal development life cycle (he's wrong), and sets down 5 laws of software evolution that ring true even today. He [later expanded these laws](https://en.wikipedia.org/wiki/Lehman%27s_laws_of_software_evolution).

And he was one of the first to say _"To achieve this requires insight, theory, models, methodologies, techniques, tools: a discipline. That is what software engineering is all about."_

> Favorite bit so far: Lehman describes, in 1980, the difference between programming and software engineering.
> 
> You'll remember this is a key point in that Software Engineering at Google book from 2020 [pic.twitter.com/SFrFBVszMk](https://t.co/SFrFBVszMk)
> 
> — Swizec Teller (@Swizec) [September 26, 2024](https://x.com/Swizec/status/1839339847703790068?ref_src=twsrc%5Etfw)

Thus the software engineer was born as distinct from programmer. A programmer can write code, an engineer can systematically develop software that evolves over time.

## [3 types of programs](#3-types-of-programs)

> Omg I figured it out!  
> How do you identify what should be a horizontal library/util/atom vs a vertical module?
> 
> It’s the S- vs E- programs from Lehman! 💡
> 
> Libs/utils do a thing exactly to a spec that doesn’t change and their input->output map can be fully specced.
> 
> Modules…
> 
> — Swizec Teller (@Swizec) [September 28, 2024](https://x.com/Swizec/status/1840043098321346891?ref_src=twsrc%5Etfw)

Lehman classifies programs into 3 types that continue to feel useful today. Reading it laid out like this clarified a lot of vibey thoughts for me.

**S-programs** map inputs to outputs according to a specification and can be exhaustively verified. S-programs are contained by the spec and don't care about the environment. Their behavior doesn't change. If you want to follow a different spec, you write a different program. These are your utils, atoms, etc.

**P-programs** are defined by the business rules they follow and aim to fulfill a real world need. You can describe their behavior, but you can't evaluate their correctness without comparing to external criteria. Does it get the job done? A bug-free p-program can still be wrong. These are your molecules, components, modules, etc.

**E-programs** combine any number of P- and S- programs into a cohesive whole that aims to encode and mechanize a human endeavor or system. These are your software. Constantly changing and adapting as the world changes, needs evolve, and the software itself creates new ideas and possibilities.

## [Development life-cycle](#development-life-cycle)

Lehman published this paper 21 years before agile. As such he is weirdly obsessed with waterfall and [big up-front design](https://swizec.com/blog/how-big-up-front-design-fails/).

He describes the ideal cycle as:

1.  Gather requirements
2.  Design top level specifications
3.  Recursively go into components
4.  Design specs for those
5.  Factor your whole system into nothing but S-programs
6.  Now programmers can "just implement" the specs
7.  Integrate
8.  Deploy
9.  Maintenance phase begins

This sounds great but as you and I know, steps 5 and 6 never quite happen. By the time you get that deep into writing specs, you may just do the work and write your specification as code.

You could argue that writing code in a high level programming language like JavaScript, Python, Haskell etc is like writing a specification detailed enough that your compiler can "just implement" the code. But they had high level languages in the 80's 🤷

Interestingly, Lehman notes several times that _"this is not how it works in practice and the phases are often interleaved and overlapped"_. We now know that's the only way.

## [5 laws of software evolution](#5-laws-of-software-evolution)

Lehman notes 5 laws of software evolution. They feel true to my experience. These might not solve any of your problems, but it's nice to know your experience is normal.

[![Lehman's Laws of Software Evolution](https://swizec.com/_vercel/image?url=%2Fassets%2FLehmans-Laws-of-Software-Evolution-cj156a-DU1gpkN3.jpeg&w=960&q=75)](https://swizec.com/assets/Lehmans-Laws-of-Software-Evolution-cj156a-DU1gpkN3.jpeg)

1.  **Continuing change** means software is never done. As long as you're using it, you're gonna have to make changes to adopt new requirements, changes in environment, or implement new ideas that come from feedback cycles with the software itself. S- programs don't change, P- programs change rarely (after they're "done"), and E-programs change always.
2.  **Increasing complexity** means your code keeps getting more complex unless you _do_ something about it. Lehman notes a typical cycle of new feature release followed by cleanup releases. You _have to_ [manage complexity](https://swizec.com/blog/why-taming-architectural-complexity-is-paramount/).
3.  **The fundamental law** means that even though we all make decisions based on local knowledge, the system as a whole behaves statistically and can be measured/understood.
4.  **Conservation of stability** means that the rate of output on a software project is constant. Due to growing complexity and maintenance, you have to keep adding people just to keep moving at the same pace.
5.  **Conservation of familiarity** means that as software evolves, it is increasingly constrained by past choices. The more users you have, the more disruptive large changes become.

Hope this concrete ways to talk about your gut feels and vibey thoughts. It did for me.

~Swizec

Filed under: [Papers](https://swizec.com/categories/papers)[Software Engineering](https://swizec.com/categories/software-engineering)[Scaling Fast Book](https://swizec.com/categories/scaling-fast-book)[Software Architecture](https://swizec.com/categories/software-architecture)

## Liked this article? You’ll love the book

### Related Articles

*   [What I learned from Software Engineering at Google](https://swizec.com/blog/what-i-learned-from-software-engineering-at-google/)
*   [25 lessons from 25 years of coding](https://swizec.com/blog/25-lessons-from-25-years-of-coding/)
*   [Empirical evidence for code modularity](https://swizec.com/blog/empirical-evidence-for-code-modularity/)
*   [Atoms, molecules, organisms](https://swizec.com/blog/atoms-molecules-organisms/)
*   [You can't stop the business, or why rewrites fail](https://swizec.com/blog/you-can-t-stop-the-business-or-why-rewrites-fail/)
