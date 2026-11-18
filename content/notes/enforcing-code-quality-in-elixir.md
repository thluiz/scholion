---
title: "Enforcing code quality in Elixir"
date: '2019-07-04T11:04:40+00:00'
category: webclip
summary: 'The article sets up a Mix alias for Elixir projects that runs format, Credo, Sobelow, Dialyzer, and tests locally and in CI, with warnings treated as errors.'
tags: ["elixir", "code-quality", "dialyzer", "credo"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Enforcing code quality in Elixir"
    url: "https://dev.to/leandrocp/enforcing-code-quality-in-elixir-4on9"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--enforcing-code-quality-in-elixir.md"
    kind: repo
---

The article explains how to enforce code quality in an Elixir project with a Mix alias that can run locally and in CI/CD. It combines formatting, static analysis, security checks, warnings as errors, and tests, while noting that the level of enforcement should fit the project.

## Reading notes

- Credo checks whether the code follows common good practices from the community.
- Dialyzer is used through Dialyxir, which wraps Dialyzer and simplifies its use in Elixir.
- Sobelow is a static analysis tool focused on Phoenix security.
- mix format automatically formats code and helps avoid disputes about formatting rules.
- warnings_as_errors makes compilation fail when the project has warnings.
- The suggested setup adds Credo, Dialyxir, and Sobelow as dev and test dependencies.
- The project config also adds elixirc_options, aliases, and dialyzer settings for the PLT file and ignored warnings.
- The article recommends two aliases: quality for local development and quality.ci for CI/CD.
- The local alias runs format, credo --strict, sobelow --verbose, dialyzer, and test.
- The CI alias runs test, format --check-formatted, credo --strict, sobelow --exit, and dialyzer --halt-exit-status.
- A .dialyzer_ignore.exs file is created to ignore test-related warnings about ExUnit functions.
- Credo does not need extra setup, but its default rules can be adjusted with .credo.exs or inline comments.
- .gitignore should exclude Dialyzer PLT files and Sobelow output.
- The first dialyzer run may take time because it builds artifacts that are then cached.
- The CI/CD pipeline should run MIX_ENV=test mix quality.ci and fail when an issue is found.
