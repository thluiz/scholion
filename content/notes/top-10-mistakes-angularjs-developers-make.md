---
title: "The Top 10 Mistakes AngularJS Developers Make"
date: '2014-10-12T11:12:53-03:00'
category: webclip
summary: 'The article lists common AngularJS pitfalls around app structure, dependency injection, controllers, watchers, scope, testing, and jQuery, with practical guidance for scaling apps.'
tags: ["angularjs", "javascript", "testing", "application-architecture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "10 Top Mistakes Angular.js Developers Make"
    url: "http://www.airpair.com/angularjs/posts/top-10-mistakes-angularjs-developers-make?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-10/airpair-com--top-10-mistakes-angularjs-developers-make.md"
    kind: repo
---

The article groups ten common AngularJS mistakes into structural, architectural, performance, scope, and testing issues. It argues that feature-based organization, proper dependency injection, smaller controllers, and fewer watchers make larger apps easier to maintain and debug.

## Reading notes

- Group files by feature instead of file type so related templates, controllers, directives, and services stay together.
- Avoid hanging everything off a single module; feature-based modules scale better and are easier to reuse across apps.
- Use dependency injection explicitly so code stays clear and can be minified without breaking AngularJS.
- Wrap global libraries in AngularJS modules when they need to be injected, especially under strict mode.
- Keep controllers thin; DOM work belongs in directives, business logic in services, and shared data in services when possible.
- Start with services when choosing between service and factory; factories can be useful when you need more flexibility or private helpers.
- Use Batarang to inspect models, dependency graphs, performance, and the watch tree while debugging AngularJS apps.
- Watcher counts matter; once an app has too many watchers, digest cycles can slow down noticeably.
- Use object properties on scope when parent and child scopes need to share updates through the prototype chain.
- Test AngularJS apps with Protractor for end-to-end behavior and Karma for fast test runs across browsers.
- Avoid using jQuery by default; AngularJS directives and built-in features should handle DOM work first.
