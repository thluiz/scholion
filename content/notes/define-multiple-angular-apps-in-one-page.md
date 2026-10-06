---
title: "Define multiple Angular apps in one page"
date: '2015-04-17T09:49:41-03:00'
category: webclip
summary: 'The page shows that only one AngularJS app can be auto-bootstrapped per document and presents three ways to run two apps on the same page: manual bootstrapping both, bootstrapping only the second, or injecting both into a root app.'
tags: ["angularjs", "bootstrapping", "dependency-injection"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Define multiple Angular apps in one page - CodeProject"
    url: "http://www.codeproject.com/Articles/862602/Define-multiple-Angular-apps-in-one-page"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/codeproject-com--define-multiple-angular-apps-in-one-page.md"
    kind: repo
---

The page explains that AngularJS auto-bootstrap via `ng-app` works only once per HTML document, so if a page has multiple `ng-app` attributes, only the first one is initialized. It then shows ways to place two Angular apps on the same page by bootstrapping them manually or by using a root app that includes both modules.

## Reading notes

- Only one AngularJS application can be auto-bootstrapped per HTML document.
- If a page has multiple `ng-app` attributes, only the first one is considered and the rest are ignored.
- One option is to remove `ng-app` and bootstrap both apps manually with `angular.bootstrap()`.
- Another option is to keep `ng-app` for the first app and manually bootstrap only the second app.
- A third option is to define a root app with `ng-app` and inject both apps as modules in that root app.
