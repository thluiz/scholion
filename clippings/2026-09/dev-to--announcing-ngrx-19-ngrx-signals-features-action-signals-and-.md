---
url: "https://dev.to/ngrx/announcing-ngrx-19-ngrx-signals-features-action-signals-and-more-2b35?ref=dailydev"
captured_at: "2026-09-25T00:40:25+01:00"
title: "Announcing NgRx 19: NgRx Signals Features, Action Signals, and more!"
domain: "dev-to"
---

We are pleased to announce the latest major version of the NgRx framework with some exciting new features, bug fixes, and other updates.

* * *

## [](#updated-ngrx-signals-features)Updated NgRx Signals Features🚦

The NgRx Signals was released as stable in v18 as a new library built from the ground up with Angular Signals, opt-in RxJS interoperability, and entity management out of the box. the NgRx Signals library has continued to receive quality updates and improvements to enhance the developer experience.

### [](#new-props-signalstore-feature)New Props SignalStore Feature

One highly requested feature was the ability to define props for a SignalStore during its creation. To support this, the `withProps` base feature was added to allow static properties or observables to be defined as SignalStore members.  

```
export const BooksStore = signalStore(
  withEntities<Book>(),
  withRequestStatus(),
  withProps(({ isFulfilled }) => ({
    fulfilled$: toObservable(isFulfilled).pipe(filter(Boolean)),
  })),
);
```

Enter fullscreen mode Exit fullscreen mode

It can also be used for defining all dependencies in a single place:  

```
export const MyStore = signalStore(
  withProps(() => ({
    service1: inject(Service1),
    service2: inject(Service2),
  })),
  withMethods(({ service1, service2 }) => ({
    method1() {
      service1.foo();
    },
    method2() {
      service2.bar();
    },
  }))
);
```

Enter fullscreen mode Exit fullscreen mode

The new `withProps` feature integrates together with new Angular Signals features including `resource` and `linkedSignal`:  

```
const booksStore = signalStore(
  withProps(() => {
    const bookResource = resource({
      loader: () => Promise.resolve({ id: 1, title: "'Lord of the Rings' }),"
    });
    return {
      _bookResource: bookResource,
      bookResource: bookResource.asReadonly(),
    };
  }),
);
```

Enter fullscreen mode Exit fullscreen mode

The above exposes bookResource as readonly resource, and keeps the writable resource.

The next example exposes `prettyTitle` as `linkedSignal`, and keeps the writable state internally.  

```
signalStore(
  withState({ id: 1, title: "'Lord of the Rings' }),"
  withProps((store) => ({
    prettyTitle: linkedSignal(() => \`${store.id()}: ${state.store()}\`),
  })),
);
```

Enter fullscreen mode Exit fullscreen mode

The new `withProps` features allows you customize and extend the SignalStore even further with Angular Signals. Thanks to [Marko Stanimirović](https://twitter.com/MarkoStDev) for his continued work on improving NgRx Signals!

### [](#signal-method-utility-function)Signal Method Utility Function

The `rxMethod` utility function was introduced to provide a way to connect async work done with RxJS to Angular Signals. We've also introduced the `signalMethod` utility function that gives you the same benefits of `rxMethod` with the ability to use only use signals.

`signalMethod` is a factory function that processes side effects on signals or static values.  

```
import { Component } from '@angular/core';
import { signalMethod } from '@ngrx/signals';

@Component({ /* ... */ })
export class NumbersComponent {
  // 👇 This method will have an input argument
  // of type `number | Signal<number>`.
  readonly logDoubledNumber = signalMethod<number>((num) => {
    const double = num * 2;
    console.log(double);
  });
}
```

Enter fullscreen mode Exit fullscreen mode

At first sight, `signalMethod`, might look the same as an `effect`. However, signalMethod offers three distinctive advantages over effect:  

```
@Component({ /* ... */ })
export class NumbersComponent {
  readonly num = signal(2);
  readonly logDoubledNumberEffect = effect(() => {
    console.log(this.num() * 2);
  });
  readonly logDoubledNumber = signalMethod<number>((num) => {
    console.log(num * 2);
  });

  constructor() {
    this.logDoubledNumber(this.num);
  }
}
```

Enter fullscreen mode Exit fullscreen mode

**Flexible Input**: The input argument can be a static value, not just a signal. Additionally, the processor function can be called multiple times with different inputs.  
**No Injection Context Required**: Unlike an effect, that requires an injection context or an Injector, signalMethod's "processor function" can be called without an injection context.  
**Explicit Tracking**: Only the Signal of the parameter is tracked, while Signals within the "processor function" stay untracked.

Read the docs to learn more about [signalMethod](https://ngrx.io/guide/signals/signal-method).

### [](#development-mode-checks-for-state-mutations)Development Mode Checks for State Mutations

Ensuring that state updates are immutable is crucial for Signal to emit correctly and trigger necessary DOM updates, derived signals, or side effects. To mitigate this issue the `patchState` function applies a deep freeze on the state in development mode.

Before:  

```
const userState = signalState(initialState);
patchState(userState, (state) => {
  state.user.firstName = 'mutable change'; // mutable change which went through
  return state;
});
```

Enter fullscreen mode Exit fullscreen mode

After:  

```
const userState = signalState(initialState);
patchState(userState, (state) => {
  state.user.firstName = 'mutable change'; // throws in dev mode
  return state;
});
```

Enter fullscreen mode Exit fullscreen mode

This ensures that state changes remain immutable, providing a path to retaining performance and best practices.

## [](#ngrx-store-support-for-dispatching-actions-on-signal-changes)NgRx Store Support for Dispatching Actions on Signal changes

NgRx Store remains the defacto choice for global state management within Angular applications. NgRx Store previously introduced support for selecting state as a signal, and now introduces an ergonomic way to dispatch actions that read signals.  

```
class BookComponent {
  bookId = input.required<number>();

  constructor(store: Store) {
    store.dispatch(() => loadBook({ id: this.bookId() })));
  }
}
```

Enter fullscreen mode Exit fullscreen mode

The `dispatch` method executes initially and every time the `bookId` changes. If `dispatch` is called within an injection context, the signal is tracked until the context is destroyed. In the example above, that would be when `BookComponent` is destroyed.

When `dispatch` is called outside a component's injection context, the signal is tracked globally throughout the application's lifecycle. To ensure proper cleanup in such a case, provide the component's injector to the `dispatch` method:  

```
class BookComponent {  
  bookId = input.required<number>();
  injector = inject(Injector);
  store = inject(Store);

  ngOnInit() {
    // runs outside the injection context
    this.store.dispatch(
      () => loadBook({ id: this.bookId() }),
      { injector: this.injector }
    );
  }
}
```

Enter fullscreen mode Exit fullscreen mode

Thanks to [Rainer Hahnekamp](https://twitter.com/rainerhahnekamp) for adding these features!

## [](#ngrx-signals-the-new-default)NgRx Signals, the new Default 🤝

NgRx Signals is a ground-up approach to managing state reactively, and is opt-in for RxJS usage. It also has other utilities for working with Angular Signals in a structured way that helps developers scale up. NgRx Signals is now the **recommended** local state management library to integrate into your Angular applications. For new applications, start with NgRx SignalStore. For existing applications, consider migrating to the new `@ngrx/signals` package.

## [](#ngrx-workshops)NgRx Workshops 🎓

With NgRx usage continuing to grow with Angular, many developers and teams still need guidance on how to architect and build enterprise-grade Angular applications. We are excited to introduce upcoming workshops provided directly by the NgRx team!

Starting in Feburary, we will offer one to three full-day workshops that cover the basics of NgRx to the most advanced topics. Whether your teams are just starting with NgRx or have been using it for a while - they are guaranteed to learn new concepts during these workshops.

The workshop covers both global state with NgRx Store and libraries, along with managing local state with NgRx ComponentStore and NgRx Signals.

Visit our [workshops page](https://ngrx.io/workshops) to sign up from our list of upcoming workshops.

## [](#new-docs-site)New Docs site 💅

The new docs revamp is underway and is built up from scratch using [AnalogJS](https://analogjs.org/) and will have a brand-new design and revamped content. This will make sure to offer the best possible experience to our users and make it easier to find the information you need. It also ensures that the website will become easier to maintain and update. Because we're a community-driven project, we're keeping in mind that the website should be easy to contribute to.

Thanks to [Mike Ryan](https://twitter.com/MikeRyanDev) for his work on the new version of the NgRx website.

* * *

## [](#deprecations-and-breaking-changes)Deprecations and Breaking Changes 💥

This release contains bug fixes, deprecations, and breaking changes. For most of these deprecations or breaking changes, we've provided a migration that automatically runs when you upgrade your application to the latest version.

Take a look at the [version 19 migration guide](https://ngrx.io/guide/migration/v19) for complete information regarding migrating to the latest release. The complete [CHANGELOG](https://github.com/ngrx/platform/blob/main/CHANGELOG.md) can be found in our GitHub repository.

* * *

## [](#upgrading-to-ngrx-19)Upgrading to NgRx 19 🗓️

To start using NgRx 19, make sure to have the following minimum versions installed:

*   Angular version 19.x
*   Angular CLI version 19.x
*   TypeScript version 5.5.x
*   RxJS version ^6.5.x or ^7.5.x

NgRx supports using the Angular CLI `ng update` command to update your NgRx packages. To update your packages to the latest version, run the command:  

```
ng update @ngrx/store@19
```

Enter fullscreen mode Exit fullscreen mode

If your project uses `@ngrx/signals`, run the following command:  

```
ng update @ngrx/signals@19
```

Enter fullscreen mode Exit fullscreen mode

* * *

## [](#swag-store-and-discord-server)Swag Store and Discord Server 🦺

You can get official NgRx swag through our store! T-shirts with the NgRx logo are available in many different sizes, materials, and colors. We will look at adding new items to the store such as stickers, magnets, and more in the future. [Visit our store](https://ngrx.threadless.com/) to get your NgRx swag today!

Join our [Discord server](https://discord.com/invite/ngrx) for those who want to engage with other members of the NgRx community, old and new.

* * *

## [](#contributing-to-ngrx)Contributing to NgRx 🥰

We're always trying to improve the docs and keep them up-to-date for users of the NgRx framework. To help us, you can start contributing to NgRx. If you're unsure where to start, come take a look at our [contribution guide](https://ngrx.io/contributing) and watch the [introduction video](https://youtu.be/ug0c1tUegm4) [Jan-Niklas Wortmann](https://twitter.com/niklas_wortmann) and [Brandon Roberts](https://twitter.com/brandontroberts) have made to help you get started.

* * *

## [](#thanks-to-all-our-contributors-and-sponsors)Thanks to all our contributors and sponsors!

NgRx continues to be a community-driven project. Design, development, documentation, and testing all are done with the help of the community. Visit our [community contributors section](https://ngrx.io/about?group=Community) to see every person who has contributed to the framework.

If you are interested in contributing, visit our [GitHub](https://github.com/ngrx/platform) page and look through our open issues, some marked specifically for new contributors. We also have active GitHub discussions for new features and enhancements.

We want to give a big thanks to our Gold sponsor, [Nx](https://nx.app/company)! Nx has been a longtime promoter of NgRx as a tool for building Angular applications, and is committed to supporting open source projects that they rely on.

We also want to thank our Bronze sponsor, [House of Angular](https://houseofangular.io/)!

Follow us on [Bluesky](https://bsky.app/profile/ngrx.io), [LinkedIn](https://www.linkedin.com/company/ngrx), and [Twitter](https://twitter.com/ngrx_io) for the latest updates about the NgRx platform.
