---
url: "https://dev.to/simonbrown/a-minimal-approach-to-software-architecture-documentation-4k6k"
captured_at: "2026-11-16T02:02:20+00:00"
title: "A minimal approach to software architecture documentation"
domain: "dev-to"
---

[![Simon Brown](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F45519%2F35de7496-eb6f-4108-bc5d-549f059f7e8c.jpeg)](https://dev.to/simonbrown)

The question of "how much documentation should we write?" is popping up a lot recently, probably driven by teams looking at their business continuity plans, and the increase in remote working. Many software developers will be quick to tell you that:

*   "we're agile"
*   "we value working software over comprehensive documentation"
*   "the value is in the conversation"
*   "the code is the documentation"
*   "the tests are the documentation"

## [](#the-code-is-the-truth-but-not-the-whole-truth)The code is the truth, but not the whole truth

As [Grady Booch](https://twitter.com/Grady_Booch/status/1278949993722724352) will tell you though, "the code is the truth, but not the whole truth". Although we should definitely strive for highly modular code, and naming that expresses intent rather than relying on comments, the code doesn't tell you things like:

*   What is the context of the thing we're building?
*   Who are the people using the project/product?
*   What interfaces does it have with other software systems, inside and outside of the organisation we work for?
*   Where is the software system deployed?
*   How do we support it?
*   What were the drivers that led the team to building the software system in the way they did?
*   What led to the early decisions being changed?
*   etc

## [](#describe-what-you-cant-get-from-the-code)Describe what you can't get from the code

With this in mind, and remembering that time is precious, here's my suggestion for a minimal set of software architecture documentation.

*   A [System Context diagram](https://c4model.com/#SystemContextDiagram)
*   A [Container diagram](https://c4model.com/#ContainerDiagram)
*   One or more [Deployment diagrams](https://c4model.com/#DeploymentDiagram)
*   Some lightweight Markdown/AsciiDoc documentation (e.g. [software guidebook](https://structurizr.com/share/14181/documentation), or [arc42](https://arc42.org/overview/))
*   [Architecture decision records (ADRs)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

Consider this a **starting point**, and it should ideally be stored alongside the source code. If you need a few code level diagrams to document parts of your codebase, feel free to add some UML Class or Sequence diagrams. If you need to document business processes, then add some UML Activity diagrams, or perhaps take a look at ArchiMate. Ditto wireframes, entity relationship models, domain models, state charts, API definitions, etc.

## [](#summary)Summary

Although statements such as "the code and tests are the documentation" is not necessarily incorrect, we should still strive to add something a little higher level, describing what we can't easily get from the code.
