---
title: "Refactoring Catalog"
date: '2026-09-25T21:37:01+01:00'
category: webclip
summary: 'The post lists refactorings the author plans to cover in Tidy Together, argues that refactorings are reversible in both directions, and groups them by whether they change access and invocation or the arrangement of state and logic.'
tags: ["refactoring", "code-structure", "software-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Refactoring Catalog"
    url: "https://tidyfirst.substack.com/p/refactoring-catalog?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/tidyfirst-substack-com--refactoring-catalog.md"
    kind: repo
---

The post says the author is building a long catalog of refactorings for Tidy Together and keeps finding more to add as the list grows. It also says the work has not converged yet.

It presents two main ideas. First, refactorings work in both directions, so structure changes are generally reversible, even if one direction is used more often. Second, the refactorings cluster around two kinds of change: how state is accessed and logic is invoked, or how state and logic are arranged in the interface or implementation.

## Reading notes

- The author is assembling a long list of refactorings for Tidy Together and keeps discovering more while writing.
- Refactorings are described as bi-directional, with structural changes generally reversible.
- Mastery is tied to being able to use each transformation in either direction with equal ease.
- The refactorings are grouped by whether they change access and invocation patterns or the arrangement of state and logic.
- Several refactorings are marked as drafted and sent to paying subscribers for review.
- The list includes pairs such as global and local state, constructor and builder, constructor and factory, boolean parameter and two methods, and extract and inline parameter cluster.
- Other listed pairs include index access and named access, collection mutation and mutation methods, literal and constant, flag field and subclasses, flag field and delegate, static and instance, extract and inline function or method, and extract and inline fields.
