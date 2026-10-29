---
title: "Modernising legacy code with SOA and Agile"
date: '2016-02-10T17:03:59-03:00'
category: webclip
summary: 'The article describes how a legacy Delphi CRM was modernised without a full rewrite by translating some code, adding new services through SOA, and using Scrum to stabilise priorities and delivery.'
tags: ["legacy-code", "soa", "scrum", "agile"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "iTWire - Modernising legacy code with SOA and Agile"
    url: "http://www.itwire.com/opinion-and-analysis/the-wired-cio/71320-modernising-legacy-code-with-soa-and-agile"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/itwire-com--modernising-legacy-code-with-soa-and-agile.md"
    kind: repo
---

The article argues that a full rewrite of the legacy CRM would have been too risky and too slow for the business. Instead, it describes a path that kept the application running while gradually improving maintainability and delivery.

## Reading notes

- The team faced a long-maintained Delphi CRM, a separate C# delivery application, and pressure from business growth and changing priorities.
- The Delphi codebase was hard to extend, had no unit tests, sparse documentation, and was increasingly difficult to staff.
- A complete rewrite was presented as risky because it could fail, miss feature parity, lose historical data, or take years to complete.
- The article uses the Mozilla rewrite of Netscape as an example of a rewrite that took longer and cost more than expected.
- A cited alternative translated Delphi code into C# with a rules engine, allowing continued development on the existing product.
- The proposed approach for the company was to build new functionality as services in a service-oriented architecture and refactor existing code toward those services.
- Scrum was introduced to handle shifting business priorities, define user stories and acceptance criteria, and deliver a new build every fortnight.
- The article says the combination of SOA and Scrum improved developer focus, business confidence, transparency, and regular delivery.
