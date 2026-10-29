---
title: "Opinionated AngularJS styleguide for teams"
date: '2014-07-30T11:40:26-03:00'
category: webclip
summary: 'Todd Motto argues for a stricter AngularJS styleguide built from team experience, favoring getter syntax, controllerAs, directives for DOM work, resolves in routing, and consistent naming.'
tags: ["angularjs", "styleguide", "javascript", "team-practices"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Opinionated AngularJS styleguide for teams"
    url: "http://toddmotto.com/opinionated-angular-js-styleguide-for-teams/?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-07/toddmotto-com--opinionated-angularjs-styleguide-for-teams.md"
    kind: repo
---

Todd Motto presents an opinionated AngularJS styleguide for team projects, based on his own experience and in response to what he saw as gaps in Google’s guidelines. The page argues for consistent syntax, clearer structure, and moving work into the right Angular layer, especially as applications grow.

## Reading notes

- Use `angular.module('app')` getter syntax after defining a module once with the setter.
- Pass named function references into module methods so stack traces stay readable.
- Wrap compiled or concatenated code in an IIFE to avoid polluting the global namespace.
- Use `controllerAs` instead of binding controllers directly to the DOM with `ng-controller`.
- Prefer `this` in controllers when using `controllerAs`, and avoid `$scope` where possible.
- Keep logic out of controllers and delegate it to factories or services.
- Write services as class-like functions that use `this`.
- Treat factories as singleton services and return an object from the factory function.
- Put DOM manipulation and reusable behavior into directives.
- Do not prefix custom directives with `ng-`.
- Avoid comment and class directive syntax when possible; use elements and attributes instead.
- Use `resolve` in routes so data is ready before the controller is instantiated.
- Use route change events to show and hide loading or ajax spinners.
- Avoid `$scope.$watch` when `ng-change` or another event can do the job.
- Keep one role per file and split controllers, services, and directives into separate files.
- Use consistent file names, and consider a feature-based folder structure for larger apps.
- Avoid `$` and `$$` prefixes in your own service, directive, provider, and factory names.
- Order injected dependencies with Angular providers first and custom ones after.
- Use `ng-annotate` and `@ngInject` for automated dependency injection annotation.
