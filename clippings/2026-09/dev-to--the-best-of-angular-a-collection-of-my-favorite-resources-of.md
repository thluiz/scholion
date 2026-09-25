---
url: "https://dev.to/this-is-angular/the-best-of-angular-a-collection-of-my-favorite-resources-of-2024-2ei4?ref=dailydev"
captured_at: "2026-09-25T01:15:06+01:00"
title: "The best of Angular: a collection of my favorite resources of 2024"
domain: "dev-to"
---

I collected the best Angular articles of 2024, so if you are looking to develop your Angular skills or get up to speed with some of the newest solutions, check out these insightful pieces.

## [](#new-angular-versions-released-in-2024)📢New Angular versions released in 2024

*   [Master Angular 17 Study guide](https://www.angularaddicts.com/p/master-angular-17)
*   [Master Angular 17.1 and 17.2 Study guide](https://www.angularaddicts.com/p/master-angular-17-1-and-17-2)
*   [What's new in Angular 17.3](https://www.angularaddicts.com/p/whats-new-in-angular-17-3)
*   [What's new in Angular 18](https://www.angularaddicts.com/p/whats-new-in-angular-18), [Official release announcement](https://blog.angular.dev/angular-v18-is-now-available-e79d5ac0affe) by [Minko Gechev](https://twitter.com/mgechev)
*   [What's new in Angular 18.1?](https://blog.ninja-squad.com/2024/07/10/what-is-new-angular-18.1/) by [Cédric Exbrayat](https://x.com/cedric_exbrayat)
*   [What's new in Angular 18.2?](https://blog.ninja-squad.com/2024/08/14/what-is-new-angular-18.2/) by [Cédric Exbrayat](https://x.com/cedric_exbrayat)
*   [Angular v19 is now available!](https://blog.angular.dev/meet-angular-v19-7b29dfd05b84) by [Minko Gechev](https://twitter.com/mgechev)

## [](#new-angular-features)💎New Angular features

### [](#manfred-steyers-signals-article-series)📰[Manfred Steyer](https://x.com/ManfredSteyer)'s Signals article series

[Manfred Steyer](https://x.com/ManfredSteyer) wrote a 6-piece article series about Angular Signals:

*   [Signals in Angular: The Future of Change Detection](https://www.angulararchitects.io/en/blog/angular-signals/)
*   [Component Communication with Signals: Inputs, Two-Way Bindings, and Content/ View Queries](https://www.angulararchitects.io/en/blog/component-communication-with-signals-inputs-two-way-bindings-and-content-view-queries/)
*   [Successful with Signals in Angular – 3 Effective Rules for Your Architecture](https://www.angulararchitects.io/en/blog/successful-with-signals-in-angular-3-effective-rules-for-your-architecture/)
*   [Skillfully Using Signals in Angular – Selected Hints for Professional Use](https://www.angulararchitects.io/en/blog/skillfully-using-signals-in-angular-selected-hints-for-professional-use/)
*   [When (Not) to use Effects in Angular — and what to do instead](https://www.angulararchitects.io/en/blog/when-not-to-use-effects-in-angular-and-what-to-do-instead/)
*   [Asynchronous Data Flow with Angular’s new Resource API](https://www.angulararchitects.io/en/blog/asynchronous-resources-with-angulars-new-resource-api/)

### [](#replace-your-input-setters-with-input-signals)📰[Replace your @Input setters with input() signals](https://riegler.fr/blog/2024-05-01-input-setters-caveats)

In his blog post, [Matthieu Riegler](https://x.com/Jean__Meche) discusses the pitfalls of using `@Input` setters in Angular applications, and then highlights how using `input()` signals, along with `effect()`, can provide a more reliable, glitch-free approach.

### [](#everything-you-need-to-know-about-the-resource-api)📰 [Everything you need to know about the resource API](https://push-based.io/article/everything-you-need-to-know-about-the-resource-api)

[Enea Jahollari](https://x.com/Enea_Jahollari) 's tutorial shows, how to:

*   Use the resource API to update data locally
*   Load and refresh data
*   Create reusable resources
*   Use Observables and the `rxResource` function for data loading

### [](#exploring-angulars-new-let-syntax-enhancing-template-variable-declarations)📰[Exploring Angular’s New @let Syntax: Enhancing Template Variable Declarations](https://netbasal.com/exploring-angulars-new-let-syntax-enhancing-template-variable-declarations-40487b022b44)

The Angular team recently merged a [PR](https://github.com/angular/angular/pull/55848) with the new `@let` syntax, allowing Angular developers to declare local variables in templates. In his blogpost, [Netanel Basal](https://x.com/NetanelBasal) explains when and how to use this new feature.

### [](#angular-forms-new-unified-control-state-change-events)📰[Angular Forms new unified control state change events](https://medium.com/@davidepassafaro/angular-forms-new-unified-control-state-change-events-9e8e361c4777)

[Angular 18](https://www.angularaddicts.com/p/whats-new-in-angular-18) introduced a new feature in its Reactive Forms library called unified control state change events. The `AbstractControl` class (the base class for `FormControl`, `FormGroup`, and `FormArray`) now has a new `events: Observable<ControlEvent<TValue>>` property. This property is an observable, that emits for value, status, pristine or touched changes. [Davide Passafaro](https://x.com/DavidePassafaro)' s article starts with the basics of Reactive Forms, binding them with the template, understanding validation and the disabled state. Then, he explains how to use the new `events` observable to track the form's state.

### [](#angular-19-linkedsignal)📰 [Angular 19: linkedSignal](https://dev.to/kristiyan_velkov/angular-19-linkedsignal-303g)

Angular 19's new `linkedSignal` function is similar to `signal`, but with one key distinction: instead of providing a default value, you supply a computation function, much like `computed`. Whenever the result of this computation changes, the value of the `linkedSignal` updates accordingly. [Kristiyan Velkov](https://dev.to/kristiyan_velkov) explains when and how to use this new function.

## [](#angular-gems-of-2024)💎Angular Gems of 2024

### [](#my-new-angular-coding-style)📰 [My new Angular Coding Style](https://angularexperts.ch/blog/new-angular-coding-style)

[Kevin Kreuzer](https://x.com/nivekcode) has rewritten a large codebase using Signals and the new Angular APIs recently. In this article, he explains the new coding styles and patterns that emerged during the refactoring. Key points include the adoption of standalone components as a standard, the transition to using Signals for reactivity, and moving away from traditional lifecycle hooks.

### [](#magic-with-interceptors)📰 [Magic with Interceptors](https://www.angularspace.com/magic-with-interceptors/)

[Armen Vardanyan](https://x.com/Armandotrue) covers Angular Interceptors, including URL modifications, request contexts, app state injection, and error handling.

### [](#bringing-the-power-of-signals-to-angular-forms-with-signal-forms)📰[Bringing the power of Signals to Angular Forms with Signal Forms](https://timdeschryver.dev/blog/bringing-the-power-of-signals-to-angular-forms-with-signal-forms)

[Tim Deschryver](https://twitter.com/tim_deschryver) began creating signal based forms. These are built on top of `ngModel` and have an API similar to reactive forms but use signals instead of RxJS. The implementation is still a work in progress. In this blog post, Tim explains his ideas behind signal forms, provides examples, and asks for feedback from the community.

### [](#angulars-effect-use-cases-amp-enforced-asynchrony)📰 [Angular's effect(): Use Cases & Enforced Asynchrony](https://www.angularspace.com/angulars-effect-use-cases-enforced-asynchrony/)

[Rainer Hahnekamp](https://x.com/rainerhahnekamp) 's article explores the differences between `computed` Signals and `effect`s. He explains when to use `effect`s and how to handle enforced asynchrony to prevent timing bugs.

### [](#this-is-your-signal-to-try-tanstack-query-amp-angular)📰[This is your sign(al) to try TanStack Query & Angular](https://dev.to/this-is-angular/this-is-your-signal-to-try-tanstack-query-angular-35m9)

[Robin Goetz](https://twitter.com/goetzrobin) explains to us the origins of the [TanStack Query](https://tanstack.com/query/latest) data-fetching library and what is a server state. Then he summarizes, what the biggest challenges are, when we manage the server state, and how TanStack Query addresses these issues. He also shows us examples for data queries and mutations, client-side invalidation, and explains how he uses TanStack Query with modern Angular.

### [](#building-a-realtime-chat-application-with-angular-and-firebase)📰[Building a Real-Time Chat Application with Angular and Firebase](https://medium.com/@md.mollaie/building-a-real-time-chat-application-with-angular-and-firebase-89f70ebdd5a1)

[Moe Mollaie](https://x.com/MoeMollaei) explains, when real-time connections are needed and compares different solutions. He then walks through building a real-time chat application using Angular and a Firebase.

### [](#improving-code-reusability-in-angular-projects)📰[Improving Code Reusability in Angular Projects](https://medium.com/@eugeniyoz/improving-code-reusability-in-angular-projects-b169d4a1c786)

In his article, [Evgeniy Tuboltsev (OZ)](https://twitter.com/eugeniyoz) shares some recommendations on how to make our Angular applications reusable, maintainable, and scalable. He covers the following topics:

*   Pure functions
*   Component state management
*   Composition vs. inheritance
*   `::ng-deep`
*   Nested subscriptions

### [](#implicit-libraries-with-nx-lightweight-angular-architectures-by-convention)📰[Implicit Libraries with Nx: Lightweight Angular Architectures by Convention](https://www.angulararchitects.io/en/blog/implicit-libraries-with-nx-lightweight-angular-architectures-by-convention/)

[Manfred Steyer](https://x.com/ManfredSteyer) shows us an architecture where library configurations are derived by an Nx plugin using conventions. With implicit libraries, we can create a new library by creating a folder with an `index.ts` file.

The idea of implicit libraries comes from [Younes Jaaidi](https://x.com/yjaaidi)'s [blog post](https://medium.com/marmicode/nx-implicit-libraries-the-hidden-gem-d965d5118ecd). He also wrote a [step by step guide](https://cookbook.marmicode.io/nx/implicit-libraries/) on this topic.

### [](#using-isolatedmodules-in-angular-182)📰[Using isolatedModules in Angular 18.2](https://blog.angular.dev/using-isolatedmodules-in-angular-18-2-68a7d3a6c03d)

Angular 18.2 supports TypeScript `isolatedModules`. This feature may boost production build times. [Mark Thompson](https://x.com/marktechson) and Charles Lyding explain how this feature works and how to set it up in an Angular project.

### [](#angular-rxjs-vs-signals-what-to-use)📰[Angular: RxJS vs Signals, what to use?](https://medium.com/@IgorPak-dev/angular-rxjs-vs-signals-what-to-use-17f2655b7e9c)

[Igor Pak](https://www.linkedin.com/in/igor-pak-693584241/) provi-des two use cases to illustrate when to use Signals and when to use RxJS. His article shows that while Signals are good for state management and simple data updates, they might miss intermediate values in complex scenarios.

### [](#top-10-angular-architecture-mistakes-you-really-want-to-avoid)📰 [Top 10 Angular Architecture Mistakes You Really Want To Avoid](https://angularexperts.ch/blog/top-10-angular-architecture-mistakes)

In his latest blog post, [Tomas Trajan](https://x.com/tomastrajan) collected common mistakes developers make in Angular, like:

*   Not thinking about the difference between eager and lazy parts of the app
*   Using more than one way to achieve the same
*   Focusing on DRY instead of ISOLATION
*   Analyzing architecture manually instead of with the help of tooling
*   Not being familiar with the two main systems in Angular and the rules by which they behave

## [](#about-the-author)👨‍💻About the author

My name is [Gergely Szerovay](https://www.linkedin.com/in/gergelyszerovay/), I worked as a data scientist and full-stack developer for many years, and I have been working as frontend tech lead, focusing on Angular based frontend development. As part of my role, I'm constantly following how Angular and the frontend development scene in general is evolving. To share my knowledge, I started the [Angular Addicts](https://angularaddicts.com/) monthly newsletter and publication in 2022, so that I can send you the best resources I come across each month. Whether you are a seasoned Angular Addict or a beginner, I got you covered. Let me know if you would like to be included as a writer. Let’s learn Angular together! [Subscribe here](https://www.angularaddicts.com/) 🔥

Angular has evolved very rapidly over the past few years, and in the past year, with the rise of generative AI, our software development workflows have also evolved rapidly. In order to closely follow the evolution of AI-assisted software development, I decided to start building AI tools in public, and publish my progress on [AIBoosted.dev](https://aiboosted.dev/). Join my on this learning journey: [Subscribe here](https://aiboosted.dev/) 🚀

Follow me on [Substack (Angular Addicts)](https://www.angularaddicts.com/), [Substack (AIBoosted.dev)](https://aiboosted.dev/), [Medium](https://medium.com/@GergelySzerovay), [Dev.to](https://dev.to/gergelyszerovay), [Twitter](https://twitter.com/GergelySzerovay) or [LinkedIn](https://www.linkedin.com/in/gergelyszerovay/) to learn more about Angular, and how to build AI apps with AI, Typescript, React and Angular!
