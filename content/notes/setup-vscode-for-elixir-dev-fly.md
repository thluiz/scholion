---
title: "Setup VSCode for Elixir Dev"
date: '2022-07-28T09:33:07-03:00'
category: webclip
summary: 'The page recommends a VS Code setup for Elixir and Phoenix development: ElixirLS and Phoenix Framework as must-have extensions, Elixir Test as a helpful add-on, and Tailwind CSS IntelliSense for Tailwind users.'
tags: ["vscode", "elixir", "phoenix", "tailwind-css"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Setup VSCode for Elixir Dev · Fly"
    url: "https://fly.io/phoenix-files/setup-vscode-for-elixir-development/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/fly-io--setup-vscode-for-elixir-dev-fly.md"
    kind: repo
---

The page lays out a VS Code setup for productive Elixir and Phoenix development. It recommends starting with the main extensions, then adding a few optional ones depending on the project.

## Reading notes

- ElixirLS is the first must-have extension. It provides Elixir support, debugger, autocomplete, and code formatting, but it runs an initial project analysis that can take time.
- The `.elixir_ls` directory created by ElixirLS should be added to `.gitignore`.
- Phoenix Framework adds syntax highlighting for Phoenix templates, including `.heex` and `~H` embedded templates.
- The extension author recommends adding `"emmet.includeLanguages":{"phoenix-heex":"html"}` to `settings.json`.
- If the changes do not appear, the page suggests reloading the window or restarting VS Code.
- Elixir Test is presented as a nice-to-have extension with commands that help with Elixir tests and keyboard shortcuts for each platform.
- Tailwind CSS IntelliSense is optional for projects that use Tailwind CSS.
- To make Tailwind CSS IntelliSense work well with Phoenix templates and embedded `~H` components, the page recommends adding `"tailwindCSS.includeLanguages":{"elixir":"html","phoenix-heex":"html"}` to `settings.json`.
- The page says that after the setup, developers are ready to work productively on Elixir code.
- It also points new VS Code users to the official learning resources.
