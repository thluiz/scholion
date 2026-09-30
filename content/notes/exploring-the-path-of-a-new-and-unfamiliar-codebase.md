---
title: "Exploring the path of a new and unfamiliar codebase"
date: '2021-02-13T08:39:27-03:00'
category: webclip
summary: 'The author outlines a practical way to get comfortable in a new codebase: explore the product, set up the environment, pick simple bugs, debug systematically, and ask for help when needed.'
tags: ["codebase", "debugging", "onboarding", "software-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Exploring the path of a new and unfamiliar codebase - DEV Community 👩‍💻👨‍💻"
    url: "https://dev.to/ridhwana/exploring-the-path-of-a-new-and-unfamiliar-codebase-49nh"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-02/dev-to--exploring-the-path-of-a-new-and-unfamiliar-codebase.md"
    kind: repo
---

The author describes a method for getting familiar with a new codebase by starting with the product, then moving into setup, code reading, bug fixing, and debugging. The approach is meant to replace feeling overwhelmed with steady progress and confidence.

## Reading notes

- Explore the production application first, including less-used parts of the interface, and get demos from team members when possible.
- Use the product exploration to understand what the local environment should look and behave like.
- Clone the code, read the setup documentation, and search for help when setup or other errors appear.
- Ask teammates for help when needed, then add any useful findings back into the documentation for the next person.
- Once set up, read code, navigate file structures, note packages and code styles, and look at tests.
- Start with bugs or simple tasks, because fixing existing problems gives a closer view of the system and avoids extra uncertainty from new feature work.
- Avoid first issues that are too complex, uncertain, or hard to reproduce, and look for smaller tasks that are easier to unblock.
- Break debugging into smaller parts, trace the code path across backend and frontend, and use logs to understand how the code works.
- Commenting out code can help check whether the investigation is happening in the right area, and debuggers can stop execution to inspect confusing parts.
- If debugging is still not enough, write down the problem, try rubber ducking, and ask for another pair of eyes.
- When asking for help, describe the problem, explain what has already been tried, ask direct questions, and share work in progress through draft PRs or pair programming.
- Make changes incrementally, test often, follow the code style, stay consistent with the codebase, and give teammates a heads-up when tools or technology may affect them.
- Be empathetic toward the person who wrote the code before you, and treat mistakes as something to learn from and move past.
