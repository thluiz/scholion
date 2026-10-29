---
url: "https://medium.com/@MikeRyan52/angular-2-first-app-post-mortem-b2b2b3618828#.j00nfhe78"
captured_at: "2016-02-07T22:50:27-03:00"
title: "Angular 2 First App Post-Mortem — Medium"
domain: "medium-com"
---

# Angular 2 First App Post-Mortem

I recently got the opportunity to help build a web app using Angular 2. I think the framework suffers from complexity, though Angular 2 is undeniably powerful. This post-mortem delves into my experiences building with the framework, good and bad.

#### Angular 2 + Reactive Programming = ❤

I was already using RxJS pretty heavily in my Angular 1 apps with subjects in particular making for great messaging busses between our services. With Angular 2 promising first-class support for observables I was excited to fully embrace reactive programming throughout the app.

I leveraged the [Flux architecture](https://facebook.github.io/flux/docs/overview.html) powered by the i[mmensely popular Redux library](https://github.com/rackt/redux). For a cleaner integration with Angular 2’s injector and TypeScript’s type system, I wrote a class-based wrapper around Redux that exposes state changes using RxJS observables. Consumers can subscribe to these observables and use the Store class to dispatch state-changing actions. André Staltz has [an excellent guide](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754) on reactive programming, and if you want to learn more about how to use Redux with Angular 2 or RxJS I recommend these resources:

Complimenting the reactive programming style is a powerful new Http service that functions as an observable-based wrapper around XmlHttpRequest. In addition, the new Router exposes route changes as an observable which I leveraged to keep route state synchronized with my Redux store. With everything wired up, I was able to get a thin Angular 2 wrapper around the Redux dev tools working letting me tap into the power of their [time traveling debugger](https://www.youtube.com/watch?v=xsSnOQynTHs), a privilege that React developers have had for some time.

One disappointing part of reactive programming with Angular 2 is that the framework uses traditional callbacks to handle events and listen for input changes. Setting up event listeners in templates and using the callbacks to push to subjects isn’t too hard to setup yourself, and even hooking into Angular 2’s OnChanges lifecycle hook to do something similar for input changes is reasonable. Still, if Angular 2 [supported these patterns](https://github.com/angular/angular/issues/5689) it would make reactive programming with the framework more natural.

#### The Async Pipe is Amazing

Perhaps the best part of selecting RxJS+Redux was how easy it was to connect state changes to Angular 2’s change detection cycle, thanks mostly to the async pipe. Angular 2 pipes are most commonly seen in template expressions to handle data transformation. They are analogous to filters from Angular 1 or traditional Unix pipes. The async pipe can subscribe to observables or promises passed to it and emit their values directly in templates.

[**AsyncPipe**](https://angular.io/docs/ts/latest/api/common/AsyncPipe-class.html "https://angular.io/docs/ts/latest/api/common/AsyncPipe-class.html")The async pipe subscribes to an Observable or Promise and returns the latest value it has emitted. When a new value is emitted, the async pipe marks the component to be checked for changes.

Taking the classic todo app example, here is a code sample using ngrx/store and the async pipe:

Calling the pipe async is a bit deceiving here because ngrx/store exposes state with a [BehaviorSubject](https://github.com/Reactive-Extensions/RxJS/blob/master/doc/api/subjects/behaviorsubject.md). This means that the async pipe receives the most recent value immediately and is then notified asynchronously of any future changes made to the todo list. While awesome, this still isn’t optimal because Angular 2 will continue to perform wasted change detection on our component.

Lifting from React best practices, I separated components into two categories: wrapper components that were responsible for connecting to the Redux store, and pure components that received state through input properties and emitted output through events. This coupled with Angular 2’s capability to alter the change detection strategy for components resulted in change detection that occurred when my Redux Store dispatched changes. Here’s the above example refactored to demonstrate:

By setting TodoList’s [change detection strategy](https://angular.io/docs/ts/latest/api/core/ChangeDetectionStrategy-enum.html) to OnPush I am telling Angular 2 to perform change detection if the inputs of TodoList change, and because the inputs are bound to my Redux Store using an async pipe TodoList will only update if my Redux Store updates.

This alone is a big win for me. With little code I can build clean, performant, and reactive UIs using Angular 2.

#### Dependency Injection is Vastly Improved

One of Angular 1’s shortcomings is its string-based [dependency injection](https://docs.angularjs.org/guide/di). It requires strict conventions to prevent naming collisions and special build tools to keep code minification safe. Thankfully in Angular 2 dependency injection has been vastly improved to overcome these flaws.

The first big change Angular 1 developers will notice is that DI now uses tokens instead of strings. You can still use strings for your provider tokens, however binding to types is the preferred way to go:

With emitDecoratorMetadata turned on in the TypeScript compiler, the typings on class constructors is emitted in the class’s metadata. Angular 2 uses this type information to wire up dependency injection automatically, a capability typically reserved for languages with real reflection APIs.

The new injector is also hierarchical. Angular 2 creates a new child injector for each component it compiles, resulting in an injection hierarchy that matches the component hierarchy. This helps prevent global collisions and allows developers to write well-encapsulated components that declare their required providers as part of the component configuration.

One major downside of the injector isn’t so much in the injector itself but in how little type information is emitted by TypeScript during compilation. TypeScript interfaces and generic types lack a JavaScript counterpart resulting in the loss of runtime type information available to the Angular 2 injector.

Take a look at this TypeScript code:

Using TypeScript’s experimental Reflect API, I expected the parameter type metadata emitted for MyService to look like:

```
[[ ILights ], [ Camera<string> ], [ Action[] ]
```

but instead I got:

```
[[ Object ], [ Camera ], [ Array ]]
```

The TypeScript compiler translated my ILights interface into the generic Object type, lost the precision of the generic type for my Camera class, and reduced my Action[] array signature down to just Array. This loss in type fidelity limits what kind of types I was able to actually use with Angular 2 providers.

Another major shortcoming of the type system is that sometimes the community type definitions for a library mistakenly declare types when they really mean to declare interfaces. For instance, when building my RxJS wrapper around Redux I wanted to provide Redux’s Store class using a factory:

While that would appear to be valid, Reducer is actually just an interface and lacks a JavaScript equivalent. Thankfully TypeScript is smart enough to catch this and throw a warning when interface is used this way:

![1*okrU8aViZPYiCfrBB1A0Hg.png](medium-com--angular-2-first-app-post-mortem/da145eb1850c22566cd5c94688a17651.png)

![]()

I refactored the code to provide Reducer using a string token:

The above code compiles without issue but does not work. This is because the community typings for Redux declare Store as an exported class though Redux has no such export. This results in Store being undefined at runtime. I had to refactor the code again to provide both Reducer and Store using string tokens instead of types.

Compounding my frustration was how difficult it was to debug this issue. TypeScript has no way of knowing that the type definition files don’t match the actual library. When I tried to register a provider for the Store class Angular 2 threw a comically cryptic error “Token must be defined!” and “TypeError: injector is undefined.” I eventually isolated the issue by comparing the named exports in Redux to the type definition file.

This was not a great experience and I can foresee this causing other developers some trouble when they try wiring up their favorite libraries into the injector using community written type definition files. It also seems unlikely that TypeScript will provide [higher fidelity runtime types](https://github.com/Microsoft/TypeScript/issues/3015) in the future, potentially leaving Angular 2’s DI slightly crippled for some time to come.

#### The New Router is Promising

Angular 2 ships with a new router called the Component Router. It resembles something of a cross between react-router and Ember’s router. I generally found the Component Router to be “good enough,” though the routing requirements for my project were light.

For bigger projects the new router is missing some critical features that I will need like handling routing errors, easily redirecting missing routes to 404 pages, and resolving data before entering a route. I was able handle 404s by adding asterisk routes in all route configs, pointing these asterisk routes a 404 component. I was also able to temporarily solve data resolution by abusing the router’s @CanActivate decorator to execute async requests before entering routes.

One solution to these problems that I’ve seen other developers have some success with is to sub-class the router’s RouterOutlet component and manually enhance the router lifecycle hooks with new features. While this may end up being the preferred solution, for a framework that claims to prefer composition over inheritance, having to resort to sub-classing framework components does not feel like a particularly well thought out strategy.

I am hoping to see more routing alternatives as the framework nears release. Excitingly, there are already early proof-of-concepts of [ui-router](http://plnkr.co/edit/PF69BVa1WnUYZKkURgMm?p=info) for Angular 2.

#### ES5, ES2015, or TypeScript?

I found the ES5 syntax for Angular 2 to be painful to use and the docs for vanilla ES2015 are nonexistent. Save yourself some effort and just use TypeScript (or Dart, if you fancy). One major reason for this is that Angular 2 makes heavy use of decorators including parameter decorators which are currently absent from the ES2017 decorator proposal:

While I was able to wire up the metadata myself, the lack of both docs and brevity made it an exercise in pain:

I found it to be even more chaotic when writing it in ES5:

The Angular 2 team is [prioritizing documentation for ES5, TypeScript, and Dart](https://github.com/angular/angular/issues/5449), asking developers who want to use ES2015/ES2016 to learn how to de-sugar TypeScript’s syntax themselves. While I can certainly understand this decision (most frameworks hardly get one language’s documentation right), this effectively disqualified writing Angular 2 apps in anything but TypeScript.

#### Angular 2 is Heavy

When I say Angular 2 is heavy I mean it in two different ways: Angular 2 is heavy in terms of complexity, and the Angular 2 payload is large.

A common complaint about Angular 1 was the steep learning curve and wide breadth of new terminology. I honestly do not think Angular 2 does much to address these concerns and in many cases I found Angular 2 to be more complex. The upside here is that unlike Angular 1 a lot of best practices are baked right into the framework making it much safer to work with than its predecessor.

A good example of more complex but safer is Angular 2’s controversial new templating language. While I’m not going to make assertions about its quality, I will say that while the new language is more complex in comparison to Angular 1, the new templating language results in more predictable code. Not being able to place an \*ngIf and an \*ngFor on the same element, for example, negates the need to handle directive priority that existed with Angular 1. It also forces the developer to be a lot more explicit about expected results.

![1*N12EOpzaU_iMwQdqiTuodw.png](medium-com--angular-2-first-app-post-mortem/819e165798e68486a8a612e57d2d5925.png)

![]()

Ugly but explicit, I prefer this to Angular 1’s templating language

With the new templating language I was actually able to read a component’s template and tell the difference between various attribute bindings. This was a particular sore point with Angular 1 templates and their magic attribute bindings. While it took some getting used to, I am more productive with this templating language than I was with Angular 1's.

In terms of actual size my small Angular 2 app with code splitting is significantly heavier on initial page load than a 30K+ LOC Angular 1 app I previous worked on. With whispers of an audacious plan to get simple Angular 2 apps down to 10KB by the end of the year, I’m anxious to see how much this improves in the coming months. In the short term the Angular 2 team will be providing tools to compile templates and resolve injector providers as part of the build step rather than performing these tasks at run time. This should reduce how much code is needed to send down to end users and make the app run faster.
