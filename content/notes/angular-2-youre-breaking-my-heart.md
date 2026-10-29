---
title: "Angular 2 You're Breaking My Heart"
date: '2016-04-25T16:59:06-03:00'
category: webclip
summary: 'The article argues that Angular 2 still feels hard to enter in beta because its docs assume TypeScript knowledge, its APIs split between syntaxes, migration from Angular 1 looks heavy, and the framework needs clearer guidance for existing users.'
tags: ["angular-2", "typescript", "frontend-frameworks", "migration"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Angular 2 You're Breaking My Heart"
    url: "http://www.thatguyjackguy.com/tech/angular-breaking-my-heart/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/thatguyjackguy-com--angular-2-youre-breaking-my-heart.md"
    kind: repo
---

Angular 2 is presented as a beta framework that fixes some Angular 1 problems but also introduces new friction. The author says the documentation pushes users into setup and TypeScript without enough explanation, the code paths are split across JavaScript and TypeScript, and migration from Angular 1 looks much harder than promised.

## Reading notes

- The quickstart guide asks users to copy setup files without explaining what the dependencies do.
- The TypeScript guide assumes prior knowledge and leaves key topics like decorators and module imports underexplained.
- Angular 2 code in TypeScript and JavaScript does not map cleanly enough to feel like one framework with two equal options.
- The framework keeps `ngModel` two-way binding even though it was meant to move away from that pattern.
- The Angular 1 upgrade path looks technical and hard to use in real projects.
- The article argues that Angular 2 should have a different name, a single preferred language, and a guide aimed at Angular 1 developers.
