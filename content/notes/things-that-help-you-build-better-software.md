---
title: "Things that help you build better software"
date: '2023-11-12T06:26:21+00:00'
category: webclip
summary: 'Raul Junco suggests listing domain entities, documenting their roles, and using class and sequence diagrams with code links as an entry point that saves time and supports team alignment.'
tags: ["software-design", "documentation", "uml", "teamwork"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Thread by @RaulJuncoV: Things that help you build better software. Write a list of the main entities and concepts…"
    url: "https://x.com/RaulJuncoV/status/1721895688072835330"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2023-11/x-com--things-that-help-you-build-better-software.md"
    kind: repo
---

Raul Junco outlines practical practices to build better software: start by listing the main entities and concepts in the domain, including objects, processes, and roles, and write short paragraphs describing each one's purpose and role in the system. Then use class diagrams to capture entity structure, and sequence diagrams to illustrate workflows and object interactions in specific scenarios. He recommends adding links to relevant parts of the codebase so this documentation serves as an entry point that leads to implementation details.

He explains that he creates these artifacts by choice, not obligation, because they help him make decisions faster, keep the team aligned, and ease onboarding for newcomers beyond just developers. In replies, he emphasizes that flow and sequence diagrams are crucial for event-driven architectures, says that these practices save time for everyone, and notes that system design fundamentals exist for a reason. He also briefly discusses tooling, pointing to eraser.io and asking others about their favorite tools.

## Reading notes

- Start by writing a list of the main entities and concepts in the domain, covering objects, processes, and roles.
- For each main entity or concept, add a short paragraph explaining its purpose and role in the system.
- Use class diagrams to represent the structure of entities, including their attributes, methods, and relationships.
- Use sequence diagrams to describe workflows by showing how objects interact in particular scenarios.
- Add references or links from the diagrams and descriptions to relevant sections of the codebase for those who want detailed implementation information.
- Treat this documentation as an entry point that can redirect people into the code where implementation details live.
- The author creates these materials voluntarily because they save time when making decisions.
- He notes that these artifacts help keep the team aligned on how the system works.
- They also support onboarding of new people, including non-developers.
- In conversation, he states that flow and sequence diagrams are essential for event-driven architectures (EDA).
- He comments that these practices save time for everyone on the team.
- He remarks that fundamentals of system design exist for a reason, implying their continued relevance.
- He mentions eraser.io as a tool suggestion and asks others about their favorite tools.
- He clarifies that one of his examples is an abstract sequence diagram, not tied to a specific concrete implementation.
- He highlights the value of clear, visual representations of interactions and transitions within a system.
