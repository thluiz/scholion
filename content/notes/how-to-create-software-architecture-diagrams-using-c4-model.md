---
title: "How to Create Software Architecture Diagrams Using the C4 Model"
date: '2026-09-25T22:06:21+01:00'
category: webclip
summary: 'The page explains the C4 model as four zoom levels for describing software architecture and shows how Structurizr DSL and GitHub Actions can automate diagram creation and publishing.'
tags: ["c4-model", "software-architecture", "structurizr", "diagrams-as-code"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Create Software Architecture Diagrams Using the C4 Model"
    url: "https://www.freecodecamp.org/news/how-to-create-software-architecture-diagrams-using-the-c4-model?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/freecodecamp-org--how-to-create-software-architecture-diagrams-using-c4-model.md"
    kind: repo
---

The page presents the C4 model as a way to describe and communicate software architecture through four levels: context, containers, components, and code. It uses a task management system to show how each level adds detail, from actors and external systems to internal structure and code-level views. It also mentions supplementary diagrams for deployment and dynamic flows.

It then explains diagrams as code, emphasizing version control, collaboration through pull requests, and automated rendering in build pipelines. The article uses Structurizr DSL as the main tool example and shows how a GitHub Action can generate and publish the diagrams as a static site.

## Reading notes

- The C4 model is presented as a way for software teams to describe and communicate architecture through four levels.
- Level 1, context, shows the system in its wider environment, focusing on actors and external systems.
- Level 2, containers, shows applications, databases, APIs, and other functional units and how they interact.
- Level 3, components, shows the main building blocks inside a container, such as authentication and CRUD logic.
- Level 4, code, is described as the deepest view and as less commonly used, though useful in regulated or legacy systems.
- The page also mentions supplementary deployment and dynamic diagrams for processes like login flows.
- Diagrams as code is framed as storing diagrams in version control, reviewing them with pull requests, and rendering them automatically in CI.
- Structurizr and its DSL are presented as the main practical tool for modeling the C4 structure.
- A GitHub Actions workflow is shown to generate HTML from the DSL file and publish it to GitHub Pages.
