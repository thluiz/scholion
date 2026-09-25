---
title: "Symptoms of an Angular Disorder"
date: '2025-04-02T11:06:11-03:00'
category: webclip
summary: 'The article treats recurring Angular code smells as symptoms of deeper project problems, focusing on component over-flexibility, tight coupling, heavy templates, many subscriptions, manual change detection, and missing directives.'
tags: ["angular", "code-smells", "components", "directives"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Symptoms of an Angular Disorder"
    url: "https://www.angularspace.com/symptoms-of-an-angular-disorder/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-04/angularspace-com--symptoms-of-an-angular-disorder.md"
    kind: repo
---

The article frames several Angular code patterns as symptoms rather than standalone bad practices. Its point is that very flexible components, parent injection, large template loops, service injection in presentational components, manual change detection, many subscriptions, and few custom directives can signal deeper problems in a codebase.

## Reading notes

- Components with too many inputs can become hard to maintain, produce messy templates, and make required properties easy to forget.
- A better path can be splitting the component, using a configuration object, and providing default options through dependency injection.
- Injecting a parent component into a child creates tight coupling, makes testing harder, and can still cause change detection and data flow issues.
- Sharing data through services or InjectionTokens is presented as a cleaner alternative when inputs are not enough.
- Large `*ngFor` or `@for` blocks in templates can indicate that part of the UI should be moved into a child component.
- A very simple HTML fragment does not always need to be abstracted into another component.
- Injecting a service into a component that is meant to be presentational makes that component less reusable and harder to test.
- Manual change detection is described as something to avoid unless it is really needed, with `async` pipe, setters, signals, and pipes suggested as alternatives.
- Too many `subscribe` calls make code harder to maintain, can introduce race conditions, and may hide missing unsubscribe handling.
- The article suggests using `async` pipe, signals, template-driven forms with signals, or the Resource API when possible.
- A codebase with zero or very few custom directives may be failing to use Angular’s template power well.
- Repeated template patterns, like showing content only to authenticated users, can be candidates for custom directives.
