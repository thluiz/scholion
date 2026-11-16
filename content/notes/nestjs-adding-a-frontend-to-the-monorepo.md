---
title: "NestJS - Adding a frontend to the monorepo"
date: '2020-04-20T21:22:35+00:00'
category: webclip
summary: 'The post shows how to add a Vue frontend to a NestJS monorepo, setting up Webpack, TypeScript, Vue files, and npm scripts so the blog frontend can build and run.'
tags: ["nestjs", "vue", "webpack", "monorepo"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "NestJS - Adding a frontend to the monorepo"
    url: "https://dev.to/lampewebdev/nestjs-adding-a-frontend-to-the-monorepo-11g6"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--nestjs-adding-a-frontend-to-the-monorepo.md"
    kind: repo
---

The post explains how to add a Vue frontend inside an existing NestJS monorepo. It covers the dependency installs, the folder structure for a `frontend/blog` app, and the files needed to make Vue work with Webpack and TypeScript.

## Reading notes

- Installs Vue plus several development dependencies for Webpack to build and serve the frontend.
- Creates a `frontend/blog` folder and an `index.html` file with a `div` whose `id` is `app`.
- Uses a `webpack.config.js` that sets `context` to `__dirname`, outputs to `dist/frontend`, and handles Vue, CSS, SCSS, SVG, PNG, and TypeScript.
- Describes the `devServer` running on port `9000` and reading files from `public`.
- Adds a TypeScript config that includes `./blog/src/**/*` to avoid TypeScript errors.
- Creates `src/index.ts` to mount `App.vue` on `#app`.
- Creates `App.vue` as a simple component that renders the header `lampeweb dev blog`.
- Adds `vue-shim.d.ts` so TypeScript can import `.vue` files.
- Defines npm scripts for watching and building the blog frontend with Webpack.
