---
title: "From Mockup to Angular Material"
date: '2026-11-16T07:55:33+00:00'
category: webclip
summary: 'The article shows how to turn a UI sketch for Doggo Quest into an Angular app, then use Angular Material, components, bindings, and directives to build the screen structure.'
tags: ["angular", "angular-material", "ui-components", "doggo-quest"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "From Mockup to Angular Material - Kill All Defects"
    url: "https://web.archive.org/web/20200808063421id_/https://killalldefects.com/2020/02/05/from-mockup-to-angular-material/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--from-mockup-to-angular-material-kill-all-defects.md"
    kind: repo
---

The article walks through building the main interface of a text-based adventure game called Doggo Quest from a mockup. It starts with Angular setup, project creation, and component generation, then adds Angular Material to shape the page and match the planned layout.

## Reading notes

- The goal is to convert a user interface sketch into the visual structure of a new Angular application.
- The project is the main user interface for a text-based adventure game called Doggo Quest.
- Angular is presented as a single page application framework for maintainable web applications.
- Angular Material is described as a component library for Google’s Material style UI.
- The setup includes installing npm and the Angular CLI, then creating a project with `ng new`.
- The article uses `doggo-quest` as the project name and chooses no routing and SCSS.
- `ng serve -o` is used to run the default app and see live changes in the browser.
- The default `index.html` content is replaced with placeholder text to simplify the screen.
- The mockup is split into components such as header, footer, story view, command entry, game over, player command, and story text.
- Components are generated with `ng g c` and Angular creates HTML, SCSS, TypeScript, and spec files.
- The app component is updated to include header, story view, and footer components.
- Angular Material is added with `ng add @angular/material`, choosing a custom theme and enabling HammerJS and animations.
- Material modules imported in `app.module.ts` include card, input, button, toolbar, and icon.
- The theme is customized in `styles.scss` by switching to cyan and green palette values and using a dark theme.
- The header uses `mat-toolbar` and binds a `Score` input property.
- The footer uses `*ngIf` to switch between command entry and game over components based on `GameOver`.
- The command entry uses `mat-form-field`, `matInput`, a button, and a send icon.
- The main app layout uses a card, a resize handler, a height binding, and a scroll container for the story area.
- Story text and player command components each bind a `Text` input property.
- The story view is populated with placeholder lines to complete the interface.
- The article ends by showing the finished layout and noting that the app will be expanded later with events, rendering, parsing, and state management.
