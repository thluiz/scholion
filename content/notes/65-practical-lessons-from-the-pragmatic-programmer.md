---
title: "65 practical lessons from \"The Pragmatic Programmer: From Journeyman to Master\""
date: '2020-02-22T12:08:19+00:00'
category: webclip
summary: 'The article compiles 65 paraphrased lessons from the first edition of The Pragmatic Programmer, covering responsibility, estimation, debugging, refactoring, requirements, teamwork, testing, and user focus.'
tags: ["software-development", "refactoring", "testing", "requirements"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "👨‍💻📚 65 practical lessons from \"The Pragmatic Programmer: From Journeyman to Master\""
    url: "https://dev.to/victorcordova/65-practical-lessons-from-the-pragmatic-programmer-from-journeyman-to-master-136a"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--65-practical-lessons-from-the-pragmatic-programmer.md"
    kind: repo
---

The article presents a practical compilation of lessons from the first edition of *The Pragmatic Programmer*. It frames the book as a career-shaping reference and treats the post as a teaser, with notes paraphrased from the text and some direct quotes.

It groups the lessons around pragmatic habits in software work, including accountability, proactive change, estimation, debugging, refactoring, testability, requirements discovery, teamwork, automation, and keeping the user in view.

## Reading notes

- It is a teaser for the book and a practical compilation of notes from the first edition.
- Pragmatic programmers are described as curious, critical, realistic, adaptable, and concerned with craft.
- They take responsibility, provide options, and avoid excuses.
- Software can rot, and technical debt should be addressed early or planned for.
- Positive change starts with being proactive and paying attention to the surrounding context.
- Users should be involved in trade-offs so real constraints can shape priorities.
- Perfect code is not possible, and working software today is often better than waiting for perfection.
- Knowledge and expertise are valuable but perishable professional assets.
- Reading and hearing should be approached critically so knowledge stays accurate.
- Communication should match the audience and arrive at the right time.
- Duplication should be avoided through clear design and ongoing communication with peers.
- Third-party libraries should be checked for unwanted restrictions.
- Prototypes can be used to evaluate risky decisions, architectures, components, and UI changes.
- Domain language should be learned and used in programs.
- Estimates depend on context, and asking someone with prior experience can help.
- Sometimes the timetable of a project becomes clear only through experience on that project.
- Saying “I’ll get back to you” can slow the process enough to improve an estimate.
- Plain text is presented as a simple, long-lasting, and easy format for knowledge.
- Debugging starts with the right mindset, calmness, and attention to root cause.
- If changing something breaks the system, that change is likely relevant to the bug.
- Suspected code should be tested with the data that triggers the problem.
- When a fix takes a long time, the lesson should be captured for the next time.
- When the program reaches an impossible state, it should crash rather than keep running corrupted.
- Exceptions belong to unexpected events, not normal control flow.
- Resource-allocating routines should also release resources.
- Requesting a service from an object should not create unnecessary coupling to returned dependencies.
- Runtime configuration is useful when business needs change often.
- Coding involves constant decisions and should be done with intent, not coincidence.
- Existing code should not dictate future code.
- Algorithm choice should be pragmatic, not driven only by speed.
- Software evolves, and refactoring should happen early and often.
- Refactoring should not be mixed with adding new functionality.
- Refactoring should be done in small steps and supported by good tests.
- Testability should be designed in from the beginning.
- Generated code should be fully understood before it is used.
- Requirements are hard to identify because they are buried under assumptions, misconceptions, and politics.
- The real reason behind user behavior matters more than the current procedure.
- Becoming a user is a way to understand requirements in context.
- Requirements are needs, not architecture, design, or interface.
- A project glossary helps keep communication consistent.
- Hard problems should be approached by identifying constraints and questioning assumptions.
- Possible solutions should be listed before dismissing any option.
- Difficult problems should be examined through questions about simplicity, relevance, necessity, and hidden difficulty.
- Specifications should not be overvalued, since coding can reveal options that were not visible before.
- More than one person on a project requires rules and delegation.
- Quality is a team responsibility.
- A team should present a clear identity and build a good reputation.
- Teams should be organized around functionality rather than job function.
- Repetitive work should be automated whenever possible.
- Code should be tested early, often, and automatically.
- Usability failures count as bugs.
- Test data matters, and coverage alone is not enough.
- When a bug escapes, a new test should be added to catch it next time.
- Comments should explain why something is done and record discarded alternatives.
- Project success is measured by how well user expectations are met.
- Users should be kept aligned with what will actually be delivered.
- The final goal is to surprise users and delight them.
