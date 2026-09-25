---
url: "https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev"
captured_at: "2025-04-02T11:06:05-03:00"
title: "Starting a Modern Angular Application - DEV Community"
domain: "dev-to"
---

---
The initial architecture of a web application is fundamentally important — it will affect your app for multiple years, impacting not only development but also the user experience. Things like lazy loading, bundle size, icon reuse, and other small details will influence the user experience, not just CI time, code reuse, or the onboarding process.

In this article, I’ll review the tools and options we have when creating a new Angular app and which of them, in my opinion, should be chosen.

## [](https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev#workspace)Workspace

So the first thing we should create is a “workspace”. We should decide what structure our application will have — where all the components, services, and other things will be located.

Let’s discuss 3 ways of creating an initial structure:

1.  Using Angular CLI, without separation by sub-modules/packages/libraries;
2.  Using Angular CLI to create a monorepo, all the code is in libraries;
3.  Using Nx to create a monorepo.

There are other tools to create a monorepo, but that would take another article to describe them all :)

So let’s compare what pros and cons every option has:

### [](https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev#angular-cli-without-separation-by-submodulespackageslibraries)Angular CLI, without separation by sub-modules/packages/libraries

**Pros:**

-   Very easy to follow. Developers of any level can create a new component in the correct folder;
-   No additional dependencies.

**Cons:**

-   Very fragile because of tight coupling. Imports use relative paths: `import { NavbarComponent } from '../../../shared-components/navbar/navbar.component'`, and if something is moved or renamed, many dependent components/services might need an update. A smart IDE can help with this, but not with a 100% guarantee. Moving and renaming things become dangerous;
-   Easy to create circular dependencies and ruin lazy-loading. See the example below;
    
-   Lack of modularity. Moving some code to a separate library requires enormous effort in checking dependencies, and often this task remains forever in the backlog, with functionality just being copy-pasted to another app or project;
    
-   `test`, `lint`, and `build` will always handle all the code you have. The more code you have, the longer these commands take, even if only one line in one component was changed;
    
-   Upgrades of tools like linters are not handled by `ng update` - configs will remain the same, even if a linter or test runner library has a major version upgrade and requires modifications in configs.
    

Example of how the lazy-loading can be broken with this structure:

-   Component A imports Component B
-   Component B imports Service S and Component C
-   Component D imports Component A and Component B
-   When any component imports just a single Component D, every part listed above is imported as well. This happens very often in real apps. Ruining a lazy-loading is especially easy with this structure.

### [](https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev#angular-cli-to-create-a-monorepo-all-the-code-is-in-libraries)Angular CLI to create a monorepo, all the code is in libraries

**Pros:**

-   Modular. Every library can be reused by multiple apps or even moved to its own repo and published to a registry. Then, it can be added to dependencies with 0 changes required in the code of other apps/libraries (because all imports are already non-relative);
-   No additional dependencies.

**Cons:**

-   Every time you create a library you’ll need to manually modify the paths in tsconfig.json, because Angular CLI will generate paths to dist folder, so to get updates from any library, you need to build it first. And because all of the code is libraries, that would be a nightmare in ng serve mode, so you’ll change the path in tsconfig to the `public-api.ts` file of a library you created
-   No module boundaries tracking. Developers should create a document that explains the connections across modules to avoid circular dependencies. This document should be kept up to date and strictly followed every time a developer creates a library. There are tools such as _[madge](https://www.npmjs.com/package/madge)_ which help with this, but they still should be run manually.
-   `test`, `lint`, and `build` will always build every existing library and app. The more code you have, the longer these commands take, even if only one line in one library was changed.
-   `test`, `lint`, and `build` can only run consecutively, handling one library/app per run.
-   Upgrades of tools like linters are not handled by `ng update` - configs will remain the same, even if a linter or test runner library has a major version upgrade and requires modifications in configs.

### [](https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev#using-nx-to-create-a-monorepo)Using Nx to create a monorepo.

**Pros:**

-   Modular. Every library can be reused by multiple apps or even moved to its own repo and published to a registry. Then, it can be added to dependencies with 0 changes required in the code of other apps/libraries (because all imports are already non-relative).
-   Easy to configure e2e-testing with Playwright (comes out of the box with Nx).
-   `test`, `lint`, and `build` will:
-   handle libraries in parallel (the more cores your machine has, the sooner all the steps will be completed);
-   only run for modified code — if just one library is modified, just that library will be linted and tested;
-   use local cache — if code is not changed, results will be reused, even if commands are executed for all libraries (this behavior can be modified with `--skipNxCache`).
-   Nx automatically [controls](https://nx.dev/features/enforce-module-boundaries#project-apis) module boundaries.
-   `nx migrate` updates configs of linters and test runners when their version is updated.

**Cons:**

-   Nx as an additional dependency.

You can [read here](https://nx.dev/blog/virtuous-cycle-of-workspace-structure) how Nx recommends organizing your workspace.

There is also an excellent article, “[Managing TypeScript Packages in Monorepos](https://nx.dev/blog/managing-ts-packages-in-monorepos)”.

What you choose from these options is up to you. My recommendations:

-   Do not pick option 1, even if your app is small and you’re intimidated by the amount of boilerplate that other options bring — you’ll generate it once and forget about it;
-   If you decide that the maintenance cost of the Nx dependency is too high compared to the benefits it provides, use option 2, and you can add Nx later. If you go this route, [generate a multi-project workspace](https://angular.dev/reference/configs/file-structure#multiple-projects) — switching from a single-project to a multi-project workspace might take more time than expected, but doing it from the start will cost you nothing;
-   I recommend option 3, as it significantly improves maintenance (not only of your code but also of your tools) and reduces generated boilerplate.

## [](https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev#style)Style

First of all, use [Tailwind CSS](https://tailwindcss.com/docs/)!

It is an excellent tool. If your team is more familiar with Bootstrap, it might be difficult to make the switch, but consider this argument: at the time of writing, Tailwind CSS has more than twice the [weekly downloads](https://www.npmjs.com/package/tailwindcss) on npm [than Bootstrap](https://www.npmjs.com/package/bootstrap).

You’ll also need UI components (date picker, tabs, and so on). Here we have a lot of libraries, you can easily find them. Some of them:

-   [PrimeNG](https://primeng.org/): has a lot of components, can be styled using CSS variables, and has a plugin for Tailwind CSS support;
-   [Angular Material](https://material.angular.io/): has a lot of components and tools, can be styled using CSS variables (including the variables generated by Tailwind CSS), maintained by the Angular team, and they put a lot of effort into supporting accessibility features;
-   [spartan/ui](https://www.spartan.ng/documentation/installation): based on TailwindCSS, not so many components, in alpha stage;
-   [daysiUI](https://daisyui.com/): framework-agnostic, based on Tailwind CSS.

If you wonder why some libraries you know and love are not on this list, the answer is “for brevity” - enlisting them all would be pointless when we have so many search tools.

When picking a library, I recommend checking the following:

-   If it can be styled using CSS variables;
-   If it doesn’t require additional dependencies, that are maintained by someone else;
-   If Angular is the only JS part that it requires;
-   If it’s popular and actively maintained.

When the tool you picked asks you what format of CSS files you want, pick CSS — Tailwind works better with CSS, and in modern browsers, CSS can do things that were implemented only in SASS before, like nesting or variables.

## [](https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev#ssr)SSR

When the workspace generator asks you if you want SSR, answer “yes” even if you are 100% sure your app will never use Server Side Rendering.

The code you write should be compatible with SSR anyway. Because when you want to reuse some of the libraries you created for this app, you might be surprised how much effort and how many breaking changes are required to make the existing code compatible with SSR. And if you turn on SSR mode for the `serve` command, you’ll quickly learn what things to avoid to make code SSR compatible, and it will cost you nothing to write such code from the beginning.

If your app doesn’t need SSR, you can just set `"ssr": false` in the configuration file for the `build` command and forget about it. But your code will still be reusable in any app.

## [](https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev#standalone)Standalone

Modern Angular and Nx will generate standalone components, directives, pipes, and libraries by default, without `NgModule`. Do not try to change it — this is the direction the framework is moving towards, and creating NgModules at this point is pointless. There are still modules, of course, in the libraries and the framework itself, and you’ll use them, just don’t create new modules.

## [](https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev#reactivity)Reactivity

You are creating a new app, so it should use the latest features of Angular and be aligned with the trends in Angular evolution. Create a “zoneless” application. At the time of writing this article, it means that you’ll have to add `provideExperimentalZonelessChangeDetection()` to your list of providers in the application config.

Don’t be afraid of the “experimental” part — it works very well, even in the most complicated cases, and it might only require some workarounds if the libraries you use have usages of `NgZone.onMicrotaskEmpty`, `NgZone.onUnstable`, and `NgZone.onStable`. Because you are creating a new app, the chances of encountering such cases are low, as Angular is moving toward zoneless architecture, and libraries will support it. Right now, if a library supports the `OnPush` strategy and doesn’t use the methods of NgZone mentioned above, such a library is fully compatible with “zoneless” Angular apps.

If your app is zoneless, every component has a change detection strategy `OnPush` and you use _only signals_ in your template — Angular will benefit you with the best possible performance. And in the future, such apps will get even more performance optimizations in the framework core.

## [](https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev#state-management)State Management

I’ve built multiple apps using the approach explained in this article of mine: [Application State Management with Angular Signals](https://medium.com/@eugeniyoz/application-state-management-with-angular-signals-b9c8b3a3afd7).

If you feel that your app is going to be quite complicated and you don’t think `createEffect()` and signals will be enough — I would recommend giving a try to [SignalStore](https://ngrx.io/guide/signals/signal-store) — some professionals I know and respect use this library and love it.

That's it, you definitely will not need more complicated solutions.

And, of course, I recommend my libraries as helpers:

-   [Collection](https://github.com/e-oz/ngx-collection) for managing the state of lists/collections;
-   [Reactive Storage](https://github.com/e-oz/ngx-reactive-storage) for synchronizing data across tabs/windows using Signals, Observables, or Promises.

## [](https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev#testing)Testing

For e2e, I recommend [Playwright](https://playwright.dev/), and if your team really loves to test things — [Storybook](https://storybook.js.org/) (in addition).

For unit tests, I recommend [Vitest](https://vitest.dev/). If you prefer something else — pick a tool that runs tests in a real browser (headless). That makes a huge difference.

## [](https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev#strict-typescript-linters)Strict TypeScript + Linters

Here are options in tsconfig I use as basis and recommend for your project:  

```
<span>    </span><span>{</span><span>
      </span><span>"strict"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
      </span><span>//</span><span> </span><span>DO</span><span> </span><span>NOT</span><span> </span><span>remove</span><span> </span><span>'emitDecoratorMetadata'!</span><span> </span><span>'@typescript-eslint/consistent-type-imports'</span><span> </span><span>rule</span><span> </span><span>requires</span><span> </span><span>it</span><span>
      </span><span>"emitDecoratorMetadata"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
      </span><span>"importHelpers"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
      </span><span>"noFallthroughCasesInSwitch"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
      </span><span>"noImplicitAny"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
      </span><span>"noImplicitThis"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
      </span><span>"noImplicitReturns"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
      </span><span>"noImplicitOverride"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
      </span><span>"noUnusedLocals"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
      </span><span>"noUnusedParameters"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
      </span><span>"strictNullChecks"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
      </span><span>"strictPropertyInitialization"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
      </span><span>"useUnknownInCatchVariables"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
      </span><span>"noPropertyAccessFromIndexSignature"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
      </span><span>"angularCompilerOptions"</span><span>:</span><span> </span><span>{</span><span>
        </span><span>"strictInjectionParameters"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
        </span><span>"strictInputAccessModifiers"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
        </span><span>"strictTemplates"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
        </span><span>"strictStandalone"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
        </span><span>"fullTemplateTypeCheck"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
        </span><span>"enableI18nLegacyMessageIdFormat"</span><span>:</span><span> </span><span>false</span><span>,</span><span>
        </span><span>"disableTypeScriptVersionCheck"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
        </span><span>"extendedDiagnostics"</span><span>:</span><span> </span><span>{</span><span>
          </span><span>"checks"</span><span>:</span><span> </span><span>{</span><span>
            </span><span>"optionalChainNotNullable"</span><span>:</span><span> </span><span>"suppress"</span><span>,</span><span>
            </span><span>"nullishCoalescingNotNullable"</span><span>:</span><span> </span><span>"suppress"</span><span>,</span><span>
            </span><span>"suffixNotSupported"</span><span>:</span><span> </span><span>"warning"</span><span>,</span><span>
            </span><span>"textAttributeNotBinding"</span><span>:</span><span> </span><span>"warning"</span><span>,</span><span>
            </span><span>"invalidBananaInBox"</span><span>:</span><span> </span><span>"error"</span><span>,</span><span>
            </span><span>"missingControlFlowDirective"</span><span>:</span><span> </span><span>"error"</span><span>,</span><span>
            </span><span>"missingNgForOfLet"</span><span>:</span><span> </span><span>"error"</span><span>,</span><span>
            </span><span>"controlFlowPreventingContentProjection"</span><span>:</span><span> </span><span>"error"</span><span>,</span><span>
            </span><span>"unusedStandaloneImports"</span><span>:</span><span> </span><span>"warning"</span><span>
          </span><span>},</span><span>
          </span><span>"defaultCategory"</span><span>:</span><span> </span><span>"error"</span><span>
        </span><span>}</span><span>
      </span><span>}</span><span>
    </span><span>}</span><span>
</span>
```

That’s not the whole config, just options related to code check.

And ESLint rules:  

```
<span>    </span><span>{</span><span>
        </span><span>'no-extra-boolean-cast':</span><span> </span><span>'error'</span><span>,</span><span>
        </span><span>'no-case-declarations':</span><span> </span><span>'error'</span><span>,</span><span>
        </span><span>'@typescript-eslint/consistent-type-exports':</span><span> </span><span>'error'</span><span>,</span><span>
        </span><span>'@typescript-eslint/consistent-type-imports':</span><span> </span><span>'error'</span><span>,</span><span>
        </span><span>'@typescript-eslint/ban-ts-comment':</span><span> </span><span>[</span><span>'off'</span><span>],</span><span>
        </span><span>'@typescript-eslint/no-explicit-any':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'@typescript-eslint/no-non-</span><span>null</span><span>-assertion':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'@typescript-eslint/no-unused-vars':</span><span> </span><span>[</span><span>
          </span><span>'error'</span><span>,</span><span>
          </span><span>{</span><span>
            </span><span>argsIgnorePattern:</span><span> </span><span>'^_'</span><span>,</span><span>
            </span><span>varsIgnorePattern:</span><span> </span><span>'^_'</span><span>,</span><span>
            </span><span>caughtErrorsIgnorePattern:</span><span> </span><span>'^_'</span><span>,</span><span>
          </span><span>},</span><span>
        </span><span>],</span><span>
        </span><span>'rxjs-angular-x/prefer-takeuntil':</span><span> </span><span>[</span><span>
          </span><span>'error'</span><span>,</span><span>
          </span><span>{</span><span>
            </span><span>checkComplete:</span><span> </span><span>false</span><span>,</span><span>
            </span><span>checkDecorators:</span><span> </span><span>[</span><span>'Component'</span><span>,</span><span> </span><span>'Directive'</span><span>,</span><span> </span><span>'Injectable'</span><span>],</span><span>
            </span><span>alias:</span><span> </span><span>[</span><span>'takeUntilDestroyed'</span><span>],</span><span>
            </span><span>checkDestroy:</span><span> </span><span>false</span><span>,</span><span>
          </span><span>},</span><span>
        </span><span>],</span><span>
        </span><span>'rxjs/ban-observables':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/ban-operators':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-connectable':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-cyclic-action':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-compat':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-ignored-replay-buffer':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-unsafe-catch':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-unsafe-first':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-unsafe-switchmap':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-async-subscribe':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-create':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span> </span><span>//</span><span>
        </span><span>'rxjs/no-ignored-observable':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-exposed-subjects':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-nested-subscribe':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-ignored-notifier':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-redundant-notify':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-subject-unsubscribe':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-unbound-methods':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-unsafe-subject-next':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>'rxjs/no-unsafe-takeuntil':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
        </span><span>eqeqeq:</span><span> </span><span>[</span><span>'error'</span><span>,</span><span> </span><span>'smart'</span><span>],</span><span>
        </span><span>'prefer-const':</span><span> </span><span>'error'</span><span>,</span><span>
        </span><span>'no-unused-expressions':</span><span> </span><span>'error'</span><span>,</span><span>
        </span><span>'@angular-eslint/use-lifecycle-interface':</span><span> </span><span>'error'</span><span>,</span><span>
        </span><span>'@angular-eslint/no-input-rename':</span><span> </span><span>'off'</span><span>,</span><span>
        </span><span>'@angular-eslint/no-empty-lifecycle-method':</span><span> </span><span>[</span><span>'error'</span><span>],</span><span>
      </span><span>}</span><span>
</span>
```

Plugins for RxJS:

-   [@smarttools/eslint-plugin-rxjs](https://www.npmjs.com/package/@smarttools/eslint-plugin-rxjs)
-   [eslint-plugin-rxjs-angular-x](https://www.npmjs.com/package/eslint-plugin-rxjs-angular-x)

As always, linters’ rules are a very opinionated thing, but if you are looking for an initial setup — this will be helpful and will help you avoid a lot of errors.

## [](https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev#immutability)Immutability

Make your data structures immutable by default. Don’t expect that your view will be updated because you mutated some field of a large structure — that contradicts how Angular change detection works, so it’s the wrong approach.

Reactivity in Angular works best with Signals, and Signals compare their values by reference (you can change it, but deep checks are expensive and not always safe). This means that you need to create a new value for a signal every time you want to see any changes in your view.

In [this article](https://medium.com/@eugeniyoz/mastering-angular-essential-code-organization-principles-c09838dea6e2#19bc) of mine, you can read more about how to implement the simplest kind of immutability without any additional tools.

## [](https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev#nice-little-things)Nice Little Things

If you haven’t tried it yet, try `mat-icon` from Angular Material + [icons registry](https://material.angular.io/components/icon/overview#registering-icons). The SVG will be inlined, so you can affect currentColor and set CSS variables, which opens up a lot of possibilities. It is much better than icon fonts — you are not limited by a predefined set of images and can use literally any image you want, even with animations (for some very fancy cases). And they look sharper :)

Nice source of SVG icons: [Lucide](https://lucide.dev/icons/).

[type-fest](https://github.com/sindresorhus/type-fest) is a great tool that will add 0 bytes to your bundle.

Try [tailwindcss-safe-area](https://www.npmjs.com/package/tailwindcss-safe-area) if you care about how your app looks in landscape mode on mobile devices.

## [](https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev#things-to-avoid)Things to Avoid

Some Angular features might stay here for a while, but will not be actively developed. I recommend avoiding the following:

-   Angular Animations — use CSS animations instead. Yes, “leave” animations can’t be replaced, but that’s the only thing;
-   Old control flow directives: `ngIf`, `ngSwitch*`, and, especially `ngFor`;
-   If you use Angular Material, only style it using CSS variables, do not create CSS rules with their class names in selectors. It might cause very painful breaking changes.

___

_That’s what I use to create super-performant modern Angular apps. I hope this information will be useful for your awesome apps as well!_
