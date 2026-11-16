---
title: "Write Angular code 10x faster"
date: '2026-11-16T00:29:20+00:00'
category: webclip
summary: 'The post argues that reusable Angular components and VS Code snippets speed up development by inserting shared HTML blocks for common UI parts like blades and grids.'
tags: ["angular", "vscode", "snippets", "shared-components"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Write Angular code 10x faster"
    url: "https://dev.to/get_hariharan/write-angular-code-10x-faster-gbi"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--write-angular-code-10x-faster.md"
    kind: repo
---

The post says Angular development can move faster when common UI pieces are built once and reused across the application. It points to shared components such as blades, modals, filters, charts, and grids, then shows how VS Code snippets can insert full HTML blocks instead of typing them repeatedly.

## Reading notes

- The post frames speed as a necessity and presents VS Code snippets as the way to write Angular code faster.
- It recommends focusing first on common components and reusing them across the application.
- It says VS Code can automatically insert full component HTML when a snippet is triggered.
- It describes creating a user snippet in Visual Studio Code through F1 and User Snippets.
- It says Angular snippets can be created in the HTML snippet file.
- It gives a snippet structure with a prefix and a body array.
- It notes that each line in the body array must be enclosed in quotes.
- It shows a blade snippet using app-blade with header, content, and footer sections.
- It shows a Kendo Grid snippet with data, filterable, pageSize, skip, selected keys, resizable, and sortable settings.
- It says the author uses a larger set of snippets in an enterprise application and finds them useful for workflow and coding speed.
