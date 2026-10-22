---
title: "Automatically Format your code on Git Commit using Husky, ESLint, Prettier in 9 minutes"
date: '2022-03-17T12:11:37-03:00'
category: webclip
summary: 'The article shows how to automate code formatting on commit with Husky, ESLint, Prettier, and lint-staged so a project keeps a consistent style when developers commit code.'
tags: ["javascript", "git", "eslint", "prettier"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Automatically Format your code on Git Commit using Husky, ESLint, Prettier in 9 minutes - DEV Community 👩‍💻👨‍💻"
    url: "https://dev.to/ruppysuppy/automatically-format-your-code-on-git-commit-using-husky-eslint-prettier-in-9-minutes-45eg"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-03/dev-to--automatically-format-code-on-git-commit-husky-eslint-prettie.md"
    kind: repo
---

The page explains how to automate formatting on Git commit so a project keeps a consistent code style. It uses Husky, ESLint, Prettier, and lint-staged, with setup split into package installation, ESLint and Prettier config, lint-staged rules, and a Husky pre-commit hook.

## Reading notes

- Install Husky, ESLint, Prettier, and lint-staged as dev dependencies.
- Initialize ESLint with `npx eslint --init` and use or copy the generated `.eslintrc.json`.
- Add a `.prettierrc.json` file in the project root with formatting options such as `singleQuote`, `semi`, `trailingComma`, `printWidth`, and `tabWidth`.
- Add a `.prettierignore` file to skip files and folders such as `package-lock.json`, `yarn.lock`, and `node_modules`.
- Add `lint-staged` settings in `package.json` so staged `.js`, `.jsx`, and `.json` files run `eslint . --fix` and `prettier --write .`.
- Add Husky scripts and a `pre-commit` hook in `package.json`, then run the `configure-husky` script.
- After committing changes, the setup formats code automatically and keeps the style consistent.
