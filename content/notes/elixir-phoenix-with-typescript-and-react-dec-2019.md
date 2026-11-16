---
title: "Elixir Phoenix with Typescript and React – December 2019 Edition"
date: '2026-11-16T01:41:40+00:00'
category: webclip
summary: 'The guide sets up a Phoenix umbrella app with Postgres, Docker Compose, TypeScript, and React, then wires a small React component into the Phoenix page.'
tags: ["elixir", "phoenix", "typescript", "react"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir Phoenix with Typescript and React – December 2019 Edition"
    url: "https://dev.to/aisrael/elixir-phoenix-with-typescript-and-react-december-2019-edition-39l4"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--elixir-phoenix-with-typescript-and-react-dec-2019.md"
    kind: repo
---

The article walks through creating a Phoenix umbrella app, using Postgres by default, and running it locally with Docker Compose. It then adds TypeScript support in the frontend by adjusting tsconfig and webpack, and finishes by mounting a React component on the Phoenix home page.

## Reading notes

- It assumes Elixir 1.9.4 or newer, npm, and optionally Docker for PostgreSQL.
- It installs Phoenix with Hex and phx_new, then creates an umbrella app with `mix phx.new hello_react --umbrella`.
- The guide explains that the umbrella structure keeps apps organized as the project grows.
- It shows alternative app generation flags for MySQL and for skipping Ecto entirely.
- It uses Docker Compose to start PostgreSQL with defaults that match the generated Phoenix app.
- It installs the frontend dependencies in `apps/hello_react_web/assets` with `npm install`.
- It verifies the Phoenix app by running `mix phx.server` and visiting `localhost:4000`.
- It adds TypeScript packages and generates a default `tsconfig.json` before changing compiler options.
- It updates `webpack.config.js` to handle `.ts` files and to resolve `.ts` and `.js` extensions.
- It replaces the CSS import in `app.js` with `require` so Webpack keeps processing `app.css`.
- It adds a small TypeScript module that returns the greeting string used on the page.
- It installs React and ReactDOM, plus their type definitions, and reconfigures Webpack for `.jsx` and `.tsx` files.
- It creates a `Greeter` React component, replaces the Phoenix template section with a `greeting` container, and renders the component into that element.
