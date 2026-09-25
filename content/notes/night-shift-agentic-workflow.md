---
title: "Night Shift Agentic Workflow"
date: '2026-09-25T16:59:39+01:00'
category: webclip
summary: 'Jamon Holmgren describes a day-shift/night-shift setup where he prepares specs during the day and lets AI agents work overnight with strict tests, docs, and review loops.'
tags: ["agentic-workflow", "ai-agents", "testing", "documentation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Night Shift Agentic Workflow - Jamon Holmgren"
    url: "https://jamon.dev/night-shift"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/jamon-dev--night-shift-agentic-workflow.md"
    kind: repo
---

Jamon Holmgren describes a workflow where he uses the day to gather requirements, write detailed specs, and organize docs, then lets AI agents work autonomously overnight. He says this keeps him in control, reduces babysitting, and lets him focus on one thing at a time.

He structures the agent night around specs, docs, tests, review agents, strict validation, changelog entries, and detailed commit messages. He says the feedback loop is the key: improve the workflow and validations so the next morning starts with better code and fewer basic mistakes.

## Reading notes

- Daytime work is for human thinking, requirement gathering, and writing specs for the agent to use later.
- Specs are organized mainly for the author’s own thinking, and unfinished specs can wait until the next day.
- A small router file tells the agent where to find workflow docs, skill docs, and system documentation.
- The night shift starts only after setup is complete and the computer is locked for the evening.
- The agent begins by cleaning the working tree and running the current test suite.
- It then chooses bugs first, or features that already have a spec.
- It loads the spec, relevant docs, and relevant code before planning the work.
- Testing is described as critical, and the agent is told to write extensive tests before implementation.
- Review agents act as critical reviewers using six personas: Designer, Architect, Domain Expert, Code Expert, Performance Expert, and Human Advocate.
- The agent loops through reviews until it gets green lights, then implements code and documentation changes.
- It runs type checking, linting, compiler checks, bundle-size reporting, and all relevant tests, repeating until everything passes.
- It runs the review agents again on the implementation diff and loops back if needed.
- Unrelated TODOs are added to a TODO doc for human review.
- The night shift ends with a changelog entry, a detailed commit message, and a concise report for human review.
- On the human side, review happens commit by commit, with stacked commits kept in the same branch.
- If the agent misbehaves, the workflow calls for fixing the docs, workflow, and validations first, then correcting the code.
- Jamon says the main result so far is less babysitting, more time thinking, and a calmer workflow with better output each day.
