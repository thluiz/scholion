---
title: "Providence: Failure Is Always an Option"
date: '2015-02-19T06:26:12-03:00'
category: webclip
summary: 'Jason Punyon revisits Providence’s year-long build and argues that the project failed slowly because it was too large, relied on speculative technology choices, and spent too long on incidental work instead of validating the models in production.'
tags: ["providence", "engineering", "technology-choices", "failure"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Providence: Failure Is Always an Option - Jason Punyon"
    url: "http://jasonpunyon.com/blog/2015/02/12/providence-failure-is-always-an-option"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/jasonpunyon-com--providence-failure-is-always-an-option.md"
    kind: repo
---

Jason Punyon says Providence took about a year to build, but the long timeline hid a series of avoidable mistakes. The project started with oversized assumptions, like keeping a year of person data, and then moved through speculative choices about datastores, architecture, and update frequency.

The post argues that the team kept solving the wrong problems for too long. Cassandra and then Elasticsearch brought operational pain, and the real breakthrough came only after the team simplified the system, reduced the data window, and tested the models in the real world. That experience led to more caution in engineering decisions, including RFCs and a preference for small projects.

## Reading notes

- Providence took about a year to ship, but much of that time was spent on bad assumptions and avoidable complexity.
- The original data retention plan was for 365 days, which the later traffic pattern made look far too large.
- SQL Server was rejected on speculation, and Cassandra was chosen after limited experience and little comparison with other options.
- The team also adopted a Windows Service architecture and async/await with only partial experience.
- The Developer Kinds model was finished offline in June, but it sat untested for four months.
- A datacenter power cut exposed Cassandra problems that could not be diagnosed quickly, which pushed the team away from it.
- Elasticsearch became the next choice, but it also caused operational trouble and performance loss after HTTP pipelining was turned off.
- Progress improved only when the team simplified the system, cut back to six weeks of data, and updated daily instead of every 15 minutes.
- Real-world model tests began within two weeks after that change and the results were mostly positive.
- The team later adopted RFCs and a preference for small, Friday-sized work to avoid repeating the same failure mode.
