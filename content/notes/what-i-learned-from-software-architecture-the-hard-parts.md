---
title: "What I learned from Software Architecture: The Hard Parts"
date: '2024-01-02T08:07:48+00:00'
category: webclip
summary: 'The post highlights the book’s focus on tradeoff analysis, modularity drivers, and two ways to break a monolith into microservices, while noting the lack of implementation detail and the abstract, fictional structure.'
tags: ["software-architecture", "microservices", "monolith-decomposition", "tradeoffs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dr Milan Milanović (@milan_milanovic) on X"
    url: "https://x.com/milan_milanovic/status/1742095333499310164?s=20"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2024-01/x-com--what-i-learned-from-software-architecture-the-hard-parts.md"
    kind: repo
---

The post says the book centers on breaking monoliths into microservices and on making architectural decisions by weighing tradeoffs. It also points to modularity drivers such as speed-to-market, scalability, and fault tolerance, and contrasts component-based decomposition with tactical forking.

## Reading notes

- The book is mainly about splitting monolith applications into microservices and pairs well with "Monolith to Microservices" by Sam Newman.
- Its core architectural skill is making decisions and balancing tradeoffs.
- A modern tradeoff analysis should identify entangled parts, examine coupling, and assess the impact of change across interdependent systems.
- The main modularity drivers are speed-to-market, scalability, and fault tolerance.
- The book presents two ways to break down a monolith: component-based decomposition for a modular monolith, and tactical forking for a big ball of mud.
- For component sizing, it suggests counting statements and aiming for 1 to 2 standard deviations from the average component size.
- The post says the book stays abstract and does not go into implementation details, technologies, or architectural patterns.
- It also says the fictional Sysops SAGA story feels artificial and that a real-life example would have been more useful.
- The post notes that the book makes many assumptions and does not provide real project data such as pricing.
- It says the structure felt uneven, moving from modularity and decomposition to components, data, service granularity, reuse patterns, data ownership, and access patterns.
