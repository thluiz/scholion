---
title: "VS Code shortcuts and tricks that I wish I knew sooner"
date: '2020-08-26T19:31:13+00:00'
category: webclip
summary: 'The article collects VS Code shortcuts, custom snippets, and extensions that help with HTML scaffolding, file paths, Git history, and automatic formatting, especially for collaborative work.'
tags: ["vs-code", "shortcuts", "extensions", "prettier"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "VS Code shortcuts and tricks that I wish I knew sooner"
    url: "https://dev.to/hannahgooding/vs-code-shortcuts-and-tricks-that-i-wish-i-knew-sooner-3mcj"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--vs-code-shortcuts-and-tricks-i-wish-i-knew-sooner.md"
    kind: repo
---

The article gathers VS Code shortcuts and tools the author learned after starting full-time development, with emphasis on small time savers that were easy to miss when working remotely. It focuses on HTML snippets, source control features, and extensions that help with code navigation, history, and formatting.

## Reading notes

- Emmet is built into VS Code and expands abbreviations for file types like HTML and CSS.
- Typing `!` in an HTML file inserts the default HTML skeleton.
- The author customized a `!!` shortcut in `html.json` to include a meta description, stylesheet and script links, and semantic tags like header, main, and footer.
- Emmet HTML abbreviations shown as useful include nested elements, repeated elements, text inside tags, multiple classes, and IDs.
- The Source Control tab lets you stage files and write commit messages in the VS Code interface instead of the terminal.
- The Source Control UI makes it easier to stage specific files, format commit messages, see the recommended character count, and view co-authoring credentials in Live Share.
- Bracket Pair Colorizer 2 colors matching brackets to make code scope easier to read.
- Relative File path helps copy the relative path of another file from the current file, which is useful in large nested codebases.
- GitLens is used here for Git blame, showing the latest commit history for each line, who changed it, and the commit message.
- Prettier automatically formats code in VS Code.
- The author recommends using `Format Document` or enabling format on save.
- A `.prettierrc` file in a group project can set shared formatting rules and override local settings.
- The example Prettier config sets print width, tab width, spaces instead of tabs, semicolons, and double quotes.
