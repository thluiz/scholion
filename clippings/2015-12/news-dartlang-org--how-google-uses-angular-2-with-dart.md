---
url: "http://news.dartlang.org/2015/11/how-google-uses-angular-2-with-dart.html"
captured_at: "2015-12-11T18:22:51-03:00"
title: "Dart News & Updates: How Google Uses Angular 2 with Dart"
domain: "news-dartlang-org"
---

# How Google Uses Angular 2 with Dart

*[Cross-post from the Angular blog.](http://angularjs.blogspot.com/2015/11/how-google-uses-angular-2-with-dart.html)*

Google is always busy building new web apps, and recently a lot of that development is using [Angular 2 for Dart](https://angular.io/docs/dart/latest/quickstart.html). Just last week, the [Google Fiber](https://fiber.google.com/) team launched Google’s first production Angular 2 app, written in Dart. Take a look at their just-launched Angular 2 for Dart app:  
  
[![jy3f0aJD6YHVt1SJrSyP81L7fCXmtkucpvz3URDUmSXpOPgZZD_lDcsJI0LT3aLAS2wgdCQqzNDirYlO7Mllfuq9PpU2a2URo3HTvVTQF_WtHhFOY64Alm4bOjP9PYqIFNQ_fo3z.png](news-dartlang-org--how-google-uses-angular-2-with-dart/26454871da9a35b4859c0265ac4eb12d.png)](https://fiber.google.com/cities/kansascity/fiberhoods/)  
  
The Fiber team has lots of company within Google—Angular 2 for Dart is being quickly adopted by many other Google teams.

[Dart](https://www.dartlang.org/) is an open-source development platform from Google that makes web and [mobile development](https://flutter.io/) more productive. The Dart language is a concise yet expressive language that’s familiar to developers coming from Java, C#, ActionScript, and JavaScript. The Dart platform gives you an instant edit-debug cycle, great core libraries, a canonical package manager, a powerful semantic analyzer, and IDE support via IntelliJ IDEA and WebStorm. You can run Dart code compiled to JavaScript on all modern browsers.

We’ve worked closely with the Angular team as they’ve developed Angular and Angular 2, and we’ll be working together going forward. The Angular team’s initial experiences with Dart shaped many different aspects of Angular 2—for instance, [Angular 2’s new change detection system](http://victorsavkin.com/post/110170125256/change-detection-in-angular-2) and [template compilation](https://github.com/angular/angular/issues/3605). Both of these features dramatically sped up Angular 2 for both JS and Dart with [3x faster startup and 2.5x faster rendering than Angular 1](https://docs.google.com/presentation/d/1r1ffV-shRXHXct9DbJRVesNs6oLLk8PFGQvlE1zLpRE/edit#slide=id.ge4d624f6e_1_202). This sort of speedup makes a big difference for our users, especially on the mobile web.

We started our collaboration with the Angular team by working on Google’s internal CRM application, Greentea. The Angular team built the initial version of [Angular 1 for Dart](https://angulardart.org/) as Greentea was built, providing lots of feedback to the Dart team. By working with the Greentea team and the Angular team, we were able to make large improvements in Dart compilation to JavaScript, Dart-JavaScript interop, and IDE support for Dart.

Once Greentea was up and running, the Angular team started working on Angular 2. We’re thrilled to have Dart as a first-class language for Angular 2. Beyond Google Fiber, teams that have publicly announced that they’re currently moving to Angular 2 for Dart include:

- Greentea, Google’s internal CRM system.
- [Google AdWords](https://www.google.com/adwords/), the largest advertising system at Google.

The Google Fiber team told us that they chose Angular 2 for Dart because “Our engineers were highly productive as their projects scaled to many engineers. Dart’s support for strong typing, its object-oriented nature, and its excellent IDE integration really worked for us.”

We're continuing to improve the tools for writing and deploying apps that use Angular 2 for Dart. For instance, we’re adding Dart Analyzer support for Angular 2 templates, which will allow navigation and refactoring across Angular 2 templates and Dart code. We’re also dramatically cutting the JS that’s output by the Dart2JS compiler—“Hello, World” is down to 82KB gzipped, and we’re continuing work to slice that further.

We hope that sharing our experience will convince you to give Angular 2 for Dart a try. Angular 2 for Dart is available for you to try as a Developer Preview now—take a spin through the [Angular 2 Getting Started tour now](https://angular.io/docs/dart/latest/quickstart.html)!

*Dan Grove and Kevin Moore for the Dart team*
