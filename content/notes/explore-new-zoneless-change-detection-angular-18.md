---
title: "Explore the New Zoneless Change Detection in Angular 18"
date: '2026-09-25T23:05:02+01:00'
category: webclip
summary: 'Angular 18 introduces an experimental zoneless change detection mechanism that calls tick() without Zone.js. The article explains dirty marking, shows how to enable it, and lists cases that still need manual triggering.'
tags: ["angular", "zoneless-change-detection", "zone-js", "onpush"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Explore the New Zoneless Change Detection in Angular 18"
    url: "https://www.telerik.com/blogs/explore-new-zoneless-change-detection-angular-18?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/telerik-com--explore-new-zoneless-change-detection-angular-18.md"
    kind: repo
---

The article explains how Angular change detection works, with components marked dirty and the application tree traversed from the root through tick(). It then describes the new experimental zoneless mechanism in Angular 18, which schedules change detection without relying on Zone.js.

## Reading notes

- Angular components combine view and data logic, and change detection keeps both in sync as users interact with the app.
- In the older model, Zone.js acted as the main notification system that told Angular when to schedule change detection.
- When a component’s data changes, Angular marks that component and its ancestors as dirty so the root traversal can reach it.
- Zone.js monkey patches browser async APIs, including events, timeouts, and promises, so Angular can schedule change detection after async work finishes.
- Zoneless change detection triggers tick() on the Angular application without using Zone.js.
- The article says the switch to zoneless can reduce bundle size, improve performance, work better with async/await, and make debugging simpler.
- To enable zoneless in a new app, the guide adds provideExperimentalZonelessChangeDetection() in app.config.ts and removes zone.js from angular.json polyfills.
- The implementation uses ChangeDetectionSchedulerImpl to call tick(), and NoopNgZone as a placeholder for NgZone.
- The article says change detection runs automatically in zoneless mode when an event handler updates an instance variable, signal, or observable.
- Signal updates always trigger change detection, including updates made from setInterval.
- Observables update the view automatically when they are used with the async pipe, which marks the component dirty.
- If a change comes from a lifecycle hook or another non-event path, the article says the developer may need to inject ChangeDetectorRef and call markForCheck().
- Components that use signals are described as highly compatible with zoneless change detection.
- For better performance in larger trees, the article recommends the OnPush strategy so fewer component nodes are refreshed during a cycle.
