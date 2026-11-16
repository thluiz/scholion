---
title: "Rules of thumb for a 1x developer"
date: '2020-07-05T14:11:24+00:00'
category: webclip
summary: 'The author describes himself as a 1x developer and uses that perspective to set practical rules on learning, language choice, testing, DevOps, security, design, and project management.'
tags: ["software-engineering", "productivity", "testing", "project-management"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Rules of thumb for a 1x developer"
    url: "https://muldoon.cloud/programming/2020/04/17/programming-rules-thumb.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/muldoon-cloud--rules-of-thumb-for-a-1x-developer.md"
    kind: repo
---

The post frames software work from the perspective of a 1x developer who has limited time, values conventional wisdom, and wants to improve by choosing rules that reduce waste and compound over time. It argues that many skills are context-specific, so learning should favor general-purpose ideas, durable tools, and habits that create a virtuous cycle.

## Reading notes

- Rules of thumb provide guardrails, structure, and a more explicit way to decide when goals require rationality rather than simple pattern-following.
- Most learning is highly contextual, so much of what is learned in one job does not transfer well to the next.
- Learning time should go toward things that compound, such as typing faster, building relationships, and reflecting on what is consumed.
- Java is presented as a good fit for large enterprise systems, while C# is the Microsoft equivalent.
- Python and Ruby are described as scripting languages used when speed matters more than legibility or debugging, with Python also used for ML and AI.
- For harder languages, the post favors Go or Rust for fresh services with latency or performance needs, and Kotlin over Clojure or Scala for JVM work.
- JavaScript advice is to use TypeScript, keep logic on the server when possible, use Vue or React for interactivity, and keep unit tests.
- C is treated as something that is chosen by the problem space, while C++ is tied to performance-sensitive domains such as robotics, games, and high-frequency trading.
- Serverless functions are recommended for small, simple code that runs only occasionally.
- SQL is recommended for ad hoc queries and ACID transactions; noSQL is the fallback when those needs are absent.
- Unit tests should be written when defect cost is non-trivial, integration tests when external code is not trusted, and end-to-end tests for user-session coverage, regression, or hard-to-predict results.
- A dedicated SRE should be advocated when after-hours pages are a real risk, especially for inherited systems.
- Security should not be delegated entirely to InfoSec, because that tends to produce overly restrictive rules.
- Design sessions should be for input and questions, not for approval or signoff.
- Estimates are described as creating pressure more than enabling planning.
- The post distinguishes hard deadlines, soft deadlines, internal deadlines, and expected completion dates, and warns against conflating them.
- When a team says Agile, the author prefers Kanban over Scrum because Scrum can turn estimation into pressure to work extra hours.
