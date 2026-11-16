---
title: "Debugging Angular Ivy Applications from the Devtools Console"
date: '2020-02-22T12:12:01+00:00'
category: webclip
summary: 'The post shows how Ivy exposes new `ng` APIs in the browser console, letting you grab a selected component with `ng.getComponent($0)`, call its methods, and mark it dirty for change detection.'
tags: ["angular", "ivy", "devtools-console"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Debugging Angular Ivy Applications from the Devtools Console"
    url: "https://dev.to/angular/debugging-angular-ivy-applications-from-the-devtools-console-415j"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--debugging-angular-ivy-applications-from-the-devtools-console.md"
    kind: repo
---

The post explains that Ivy adds new APIs to the global `ng` object, making it easier to inspect and manipulate Angular component state from the browser devtools. It uses a selected DOM element in the Elements panel, retrieves the component instance with `ng.getComponent($0)`, and then calls the component API directly.

## Reading notes

- In AngularJS, developers could inspect component scope from the console with `angular.element($0).scope()`.
- Early Angular 2+ introduced `ng.probe` to interact with component state from the console.
- With Ivy, typing `ng` in the console shows new APIs on the global `ng` object.
- After selecting a component in the Elements panel, the selected node is available as `$0` in the console.
- `ng.getComponent($0)` returns the component instance for the selected DOM element.
- The example stores the component in a variable and calls `matDrawer.toggle()` to close the side menu.
- `ng.markDirty(matDrawer)` is used to trigger change detection on the component.
- The post says `ng.probe` most probably will not be supported by Ivy.
- Angular says it does not support NgProbe in Ivy because it has its own testing utilities and because NgProbe would prevent `DebugNode` and related code from tree-shaking properly.
- The conclusion says these APIs make it faster to test ideas without switching between editor and browser.
- The post also notes that new devtools extensions can be built on top of these APIs.
- It mentions that components have a `__ngContext__` with a `debug` object offering methods to query component and template properties.
- Some of these APIs are available only in development mode and are compiled away in production mode.
