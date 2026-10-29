---
title: "The Mythical Man-Month"
date: '2015-09-21T16:01:56-03:00'
category: webclip
summary: 'Brooks argues that software schedules fail because communication overhead and complexity grow with team size. He also presents practices for preserving conceptual integrity, managing change, and limiting redesign.'
tags: ["software-engineering", "brookss-law", "project-management"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Mythical Man-Month - Wikipedia, the free encyclopedia"
    url: "https://en.wikipedia.org/wiki/The_Mythical_Man-Month#The_second-system_effect"
    kind: wiki
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-09/en-wikipedia-org--the-mythical-man-month.md"
    kind: repo
---

Brooks presents software projects as work that cannot be split cleanly into independent parts. Adding people to a late project increases communication costs and can delay delivery further. He also argues that no single technique can deliver a tenfold improvement in productivity, reliability, or simplicity.

## Reading notes

- Brooks's law says adding manpower to a late software project makes it later.
- Complex programming projects cannot be divided into discrete tasks without communication and interdependence.
- As the number of people who must communicate grows, the work slows because coordination takes more time.
- Brooks rejects the idea of a single silver bullet that would transform software productivity or reliability.
- The second-system effect warns that a second design is especially vulnerable to over-engineering.
- In complex systems, some errors seem irreducible, and fixing one can introduce others.
- Small delays across many tasks can accumulate into a large overall schedule slip.
- Conceptual integrity comes from separating architecture from implementation and keeping a single architectural vision.
- A chief architect may choose to leave out features so the system stays usable.
- The chief architect should produce specifications for what the user sees, and those documents should be updated as feedback arrives.
- A pilot system can expose lessons that lead to a better second system, which is the one that should be delivered.
- Formal project documents help define goals, responsibilities, timing, and cost, and can expose inconsistencies.
- Estimation should account for administrative work and meetings, not only technical work.
- Teams should stay in close communication and ask for clarification before making assumptions.
- Brooks compares software work to surgery, with one strong programmer handling the most critical parts.
- Good programmers are described as five to ten times more productive than mediocre ones.
- Once enough of a system exists for users to react, requirements may change, but changes must eventually stop so the system can be finished.
- Teams should have specialized tools, and common tools should be built by a dedicated tools group.
- Brooks suggests hiring implementers after architecture is done, or buying software instead of building it when possible.
