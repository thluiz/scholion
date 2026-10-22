---
title: "Package by component and architecturally-aligned testing"
date: '2020-09-07T14:37:02-03:00'
category: webclip
summary: 'Simon Brown proposes package by component as a hybrid between layer and feature, with public component interfaces, package-protected internals, and tests aligned to architectural boundaries.'
tags: ["software-architecture", "testing", "modularity", "java"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Package by component and architecturally-aligned testing - Coding the Architecture"
    url: "http://www.codingthearchitecture.com/2015/03/08/package_by_component_and_architecturally_aligned_testing.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/codingthearchitecture-com--package-by-component-and-architecturally-aligned-testing.md"
    kind: repo
---

Simon Brown presents package by component as a hybrid packaging style that aims for stronger modularity and clearer architecture in code. It keeps a presentation layer on top, but groups business and data access logic into coarse-grained components with public interfaces and package-protected implementation details.

## Reading notes

- Package by layer groups code by type, which can make data access easier to swap and layers easy to test, but it often leads to a big ball of mud.
- Package by feature groups code by vertical slice, keeps feature-specific classes together, and can hide some implementation details, but cross-feature access can push classes toward public visibility again.
- Package by component combines business and data access logic for a specific domain concept or bounded context, with a public interface and package-protected internals.
- New features that need data from other components must go through those components’ public interfaces, and direct access to data access code is not allowed.
- This approach depends on using Java access modifiers properly and not making classes public by default.
- For testing, the article suggests not forcing everything into “unit tests” and instead testing some classes in isolation and some components through their public interface.
- Domain classes, utility classes, and web controllers with mocked components are examples of classes that can be tested in isolation.
- Components that store data in MySQL should be tested end to end from the public interface back to the database.
- The article treats integration-style testing as component-level black-box testing, especially when the component controls what it touches.
- External services and asynchronous messaging may require dependency injection points such as ports and adapters to make testing practical.
- The same testing strategy applies to microservices, with class tests, service tests through public interfaces, and system tests end to end.
- Brown says this strategy produces a simpler codebase with understandable dependencies, less test-induced design damage, and code that better reflects the architecture drawn in design discussions.
