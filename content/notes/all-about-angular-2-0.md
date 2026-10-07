---
title: "All About Angular 2.0"
date: '2014-11-07T15:03:41-03:00'
category: webclip
summary: 'The article explains why Angular 2.0 was being designed, focusing on performance, the changing web, mobile, and easier use. It then outlines AtScript, dependency injection, templating, directives, databinding, and the router.'
tags: ["angular-2-0", "web-components", "dependency-injection", "router"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "All About Angular 2.0"
    url: "http://eisenbergeffect.bluespire.com/all-about-angular-2-0/?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-11/eisenbergeffect-bluespire-com--all-about-angular-2-0.md"
    kind: repo
---

The article lays out the main motivations behind Angular 2.0. It says AngularJS 1.3 is the current version to use, while Angular 2.0 responds to performance limits, mobile needs, Web Components, ES6, and the desire for a simpler framework design. It also says the team still needed to clarify support for 1.x and a migration path.

## Reading notes

- AngularJS 1.3 is presented as the best current version, with bug fixes, feature improvements, and performance gains.
- Angular 2.0 is framed as a redesign for the modern web, not a small update.
- The reasons for the change include performance limits in the current binding and templating system, the rise of mobile, and the changing browser platform.
- The article says Web Components and ES6 features such as modules and classes require new framework strategies.
- AtScript is described as an ES6 superset with type syntax and metadata annotations used to author Angular 2.0.
- Runtime type assertions and metadata are used to support frameworks and dependency injection.
- Dependency injection gains metadata-based construction, instance scope control, child injectors, and other features such as lazy and promise-based injection.
- The article says Angular 2.0 removes $scope but keeps and relocates some of its useful behavior.
- Templates are compiled into ProtoViews and then Views, with caching and async loading built into the process.
- Directives are split into Component, Decorator, and Template directives.
- Controllers are folded into the Component model, which pairs a View and a Controller.
- The proposed binding syntax is shaped by Web Components, attribute encoding, and the need to keep expressions out of the DOM seen by components.
- The article argues that the team had not settled the question of two-way databinding and that the issue remained open.
- The router is described as supporting child routers, route lifecycle hooks, navigation pipelines, and back-porting to Angular 1.3.
