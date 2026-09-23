---
url: "https://angularexperts.ch/blog/top-10-angular-architecture-mistakes?ref=dailydev"
captured_at: "2026-09-23T17:39:41+01:00"
title: "Top 10 Angular Architecture Mistakes You Really Want To Avoid - Angular Experts"
domain: "angularexperts.ch"
---

Top 10 Angular Architecture Mistakes You Really Want To Avoid

In 2024, Angular keeps changing for better with ever increasing pace, but the big picture remains the same which makes architecture know-how timeless and well worth your time!

Angular
Modern Angular
emoji_objects
emoji_objects
emoji_objects

Tomas Trajan

@tomastrajan

10.09.2024

15 min read

share
link

Learn how to prevent such scenario in your project (even though it looks kind of cool 😉)
Image by GPT4 | design by Tomas Trajan

Hey there folks! The Angular renaissance continues, and it's going even stronger in 2024 with Angular team delivering amazing things like Signal based input / outputs / viewChild(ren) / contentChild(ren), new control flow, @defer for seamless component lazy loading all the way to the zone-less change detection which was released in preview in Angular 18 in May!

These new APIs, syntaxes and approaches are amazing and have demonstrably positive impact on the developer experience, performance and the quality of the codebases!

BUT

At the same time, they don't really have much impact on the way we structure our applications and workspaces. And that's a great thing because…

Angular architecture focused know-how is basically timeless and well worth spending time on!

The way we structure and architect our Angular application stayed virtually the same from the times of ancient Angular 4 which brought us stable Router implementation with support for lazy loaded routes which is one of the most important building blocks of clean architecture (not just performance) until today!

Of course, there have been some API adjustments over time, but they mostly had effect on the more low (syntax) level instead of completely changing the way we're doing things!

The best example to illustrate this point is the advent of the standalone components and APIs which made NgModules optional. The impact of this change is that instead of lazy loading of feature modules, we're now lazy loading feature route configs (or root feature components).

Is it a difference? Sure!

Does it change how things are organized and structured on the higher architectural level ? NOT AT ALL!

I hope this introduction sets the tone and spiked your curiosity to learn more about Angular architecture as such know-how was, is and will stay relevant and useful! It will allow you to ensure success of your projects and provide value for you, your team and the organization you work for!

So what are the most common mistakes in the context of Angular application architecture?
Not having an architecture (or a plan) at all!

We often hear about moving fast and breaking things, and it IS a good desirable thing because it allows us (in theory) to swiftly react to the ever changing demands and help our app or product to stay relevant!

What is unfortunately often forgotten is that if we want to be able to keep moving fast also one year after we started our project, then we also need to make sure that our project doesn't become an overconnected ball of mud or to use more technical term, we don't end up with a tangled dependency graph with lot's of circular dependencies…

Yes, this is a dependency graph from a real project, all the lines are dependencies (imports between files)

Working without a clear idea about architecture tends to end up in situations as depicted above. This changes our original statement…

"move fast and break things "

into something more akin to

"try to change this one thing, break everything"

kind of situation 😅

One of the best ways to know if this is your case is the constant feeling of being stuck in a spider web when trying to fix one thing leads you to a journey of changing half of the codebase, adding condition after condition just to make it work just this one more time.

To summarize, yes, we do need to think about architecture so that we can "keep moving fast, and breaking little isolated things (without impact on the whole)" over the course of the project lifetime.

Not thinking about the difference between eager and lazy parts of the app

In Angular (and frontend in general) we try to minimize amount of Javascript that we need to load initially because it has huge positive impact on the startup performance for the end users.

By the way, nowadays, the problem is NOT the speed of network connection, but the lack of power of CPU in weaker devices which need to parse and execute all that downloaded Javascript…

So naturally, most of the existing Angular apps will have some concepts like core (eager) and feature / page / view (lazy) to account for this base underlying reality of web development in general.

But having concepts and corresponding folders is not enough, we also have to make sure that we accidentally don't break this separation over the project lifetime.

Typical example is when we have some feature specific service which manages some kind of feature specific state, and then we realize that it would be really useful to be able to get access to that state also in some service in the eager core.

In that case, it's very easy to just import and inject the feature service in the core service and overlook this eager / lazy boundary violation (or just miss it during the PR review). The outcome will be that the service (and everything else it imports) will suddenly become part of the eager Javascript bundle!

This is bad for performance and for architecture as well as we're introducing dependencies between parts which should have been isolated or only depend on each other in one direction, eg feature can consume core, but not the other way around!

Over time, this often leads to a situation depicted in the description of the first mistake of this article with excessively tangled dependency graph!
Get notified about new blog posts

Sign up for Angular Experts Content Updates & News and you'll get notified whenever I release a new article about Angular, Ngrx, RxJs or other interesting Frontend topics!

We will never share your email with anyone else and you can unsubscribe at any time!

Email*
Sign up
Emails may include additional promotional content, for more details see our Privacy policy.
Not lazy loading ALL the features

Another common offender that tends to happen also in reasonably architected projects is that even though they mostly embraced the eager / lazy split and have most of the logic implemented as the lazy loaded features, for some reason, some of the features are "forgotten"…

The most common offenders I have seen in the wild are:

login / sing up
generic error page / 404 page
first implemented feature (eg home or dashboard)

The last example is the most common and the most unfortunate at the same time, especially because is easy to empathize why would something like this happen in the practice.

Imagine a situation when we're working on a new application, and we are working on the first set of business requirements where we need to display some kind of data.

We don't have any navigation yet, so we just start creating components and using them recursively in the template all the way up to the root AppComponent.

Then of course, new requirements come in, and we need to add navigation and the new feature will be implemented properly as a lazy loaded feature. Unfortunately, there usually won't be time (budget, or will) to refactor original feature to be lazy loaded as well.

Now we are in a situation, when there are at least 2 ways of doing things (eager feature and lazy features), plus our isolation and performance suffer as well!

The best way to remedy this is to always implement everything including the first (original feature) as a lazy loaded feature! Or in other words...

Even a one-pager (single feature) application without navigation, this first page / feature should be implemented as the first lazy loaded feature!

The cost of this is very minimal and will thank ourselves that we did that soon enough!

export const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: 'dashboard'
  },
  // application with a single feature 
  // implemented as a first lazy loaded feature
  {
    path: 'dashboard',
    loadChildren: () => import('./features/dashboard/dahsboard.routes.ts')
      .then(m => m.routes)
  }
]


Do you enjoy the content and would like to learn more about how to ensure long term maintainability of your Angular application?

Angular Enterprise Architecture eBook

Learn how to architect a new or existing enterprise grade Angular application with a bulletproof tooling based automated architecture validation.

This will ensure that Your project stays maintainable, extendable and therefore with high delivery velocity over the whole project lifetime!

Gerne mehr
Using more than one way to achieve the same

Building on top of the previous point, we should always strive to minimize the amount of ways we're doing things in our workspace.

Let's take routing as an example, currently there are at least 4 ways to do it

eager route to a component with component

lazy route to a component with loadComponent

lazy route to a module with loadChildren

lazy route to routes based feature (feature-x.routes.ts) with loadChildren

In this case, we most likely want to pick one and stick with it.

I would personally recommend to always define lazy route with the routes based feature with loadChildren which is the most modern and flexible way of doing things. Then, in case our lazy feature contains sub navigation, we can lazy load additional components with loadComponent.

We should do this also (and especially) in the case if our lazy feature has only one component to start with because the chances are high the requirements will be extended or adjusted in the future.

Proposed approach allows us to seamlessly grow to any amount of complexity while maintain single unified way of doing this across the whole project which removes cognitive load because everything looks and is done the same way!

// app.routes.ts
export const routes: Routes = [
  {
    path: 'dashboard',
    loadChildren: () => import('./features/dashboard/dahsboard.routes.ts')
      .then(m => m.routes)
  }
]

// dahsboard.routes.ts (routes based lazy feature)
export const routes: Routes = [
  {
    path: '',
    loadComponent: () => import('./dahsboard.component.ts')
      .then(m => m.DashboardComponent)
  },
  
  // which is easy to extend with in the future, eg
  {
    path: 'editor',
    loadComponent: () => import('./dahsboard-editor.component.ts')
      .then(m => m.DashboardEditorComponent)
  },
  
  // or a larger sub-feature
  {
    path: 'forecast', // forecast sub lazy feature added later
    loadChildren: () => import('./forecast/forecast.routes.ts')
      .then(m => m.routes)
  }
]

Focusing on DRY instead of ISOLATION

Isolation reduces coupling and often stands in opposition to another well known approach in software engineering, the DRY, which stands for "Don't repeat yourself".

The DRY is a principle aimed at reducing the code repetition in the codebase, replacing duplicate code with abstractions. The idea is that each piece of knowledge or logic should be represented in a single place in a system.

If the same information or logic is repeated in multiple places, any new requirement which necessitates a change in how it should work will require us to change the logic consistently in all these places which can lead to errors and inconsistencies.

As it turns out, in frontend applications, it's 3 - 10x more valuable to have more isolation than to focus on removing every instance of repetition at the cost of increased coupling and introduction of additional abstractions!

The argument we're trying to make is that in frontend codebases it's better to have some amount of duplicated code (e.g. in multiple lazy features) because that will allow them to evolve independently as the requirements change, and they do change!

In frontend, it's also much more common to encounter requirements that are very ad-hoc, e.g. to custom rule as part of a specific flow for a very small subset of users.

In frontend, it's much more common to encounter requirements that are very specific. Because of this, the isolation and the flexibility it provides, is much more valuable than abstracting away every single instance of repetition!
Analyzing architecture manually instead of with the help of tooling

Angular CLI workspace doesn't really provide any great tools for workspace architecture analysis out of the box.

This is probably main reason why this topic is pretty much unexplored and outside the general discourse of the Angular developers in the online communities worldwide.

On the other hand, NX based workspaces come with a great way to analyze architecture and dependency graph with nx graph command 👏

An example of manual architecture validation, something like verifying isolation between lazy loaded feature is a very tedious error-prone process...

We would have to…

use our editor search functionality
select a specific feature folder, eg feature-a
then search for ../feature-b (and ALL other features...)
to detect if feature A contains a relative import to any of the sibling features which means there is a violation of the rule that sibling lazy features should be isolated from one another

Such approach, while technically possible, is something that is at best frustrating and no one in their right mind would want to keep doing that on regular basis!

So what are the available alternatives?
Madge

Madge is a developer tool for generating a visual graph of your module dependencies, finding circular dependencies, and giving you other useful info

— madge npm docs

One of my favorite and honestly one of the best tools when determining the health of the Angular codebase is called madge which allows us to visualize dependency graph of the project with a single command!

npx madge src/main.ts --ts-config tsconfig.json --image ./deps.webp

and that's it!*

(* make sure to adjust paths based on your exact workspace structure)

It will crawl through all files .ts files (and the files they import, …) and produce an easy to understand chart with which are very easy to read

✅ does it look organized, left to right
🔥 does it look like it was made by a bunch of drunk spiders

and we can use them to

determine codebase health
find areas to improve
communicate with non-technical colleagues

The last point can come extremely handy when justifying often much needed refactoring / technical dept clearing efforts which can benefit the organization by increasing overall shipping velocity, but are often hard to justify and communicate properly!

Eslint plugin boundaries

Using eslint-plugin-boundaries is one of the easiest and best way to guarantee that the Angular application architecture stays clean over the whole project lifetime!

It allows us to define types and rules which encode our desired architecture with a couple of lines of configuration.

This plugin works just with folder structure which means there is no additional overhead and no changes in the actual implementation of the application itself!

Architecture as described above could be then expressed with the following architectural type config…

{
  "overrides": [
    {
      "files": ["*.ts"],
      "plugins": ["boundaries"],
      "settings": {
        "boundaries/elements": [
          {
            "type": "core",
            "pattern": "core"
          },
          {
            "type": "feature",
            "pattern": "feature/*",
            "capture": ["feature"]
          }
        ]
      }
    }
  ]
}


With the types in place we can then define rules which govern allowed relationships within such dependency graph…

{
  "overrides": [
    {
      "files": ["*.ts"],
      // rest omitted for brevity
      "rules": {
         "boundaries/element-types": [
            "error",
            {
              "default": "disallow",
              "rules": [
                {
                  "from": "core",
                  "allow": ["core"]
                },
                {
                  "from": "feature",
                  "allow": ["core"]
                },
              ]
            }
          ]
      }
    }
  ]
}


Such rule set prevents imports between features (would break isolation) as well as imports from feature into core (would break eager / lazy boundary)

This is pretty amazing because it's a fully automated way to validate architecture on every single pull request (or build) which provides us with a bulletproof guarantee that it stays clean for the whole project lifetime!

Would you like to save time and skip right to the proven scalable automated Angular architecture validation setup?

Then check out my eBook which comes with an extensive preset of architecture types, rules that govern their relationships as well as in-depth explanation of what to implement as each individual type.

Besides that, it also comes with and ready to use example repository which can be used as a basis for your next Angular project or serve as an example of how to implement such architecture in your existing projects!

Learn more about Angular Enterprise Architecture eBook now!

Not thinking about the dependency graph

As we have seen across multiple previous points, clean architecture and architecture in general is very strongly related to the underlying dependency graph of our codebase.

Event though it's not readily visible when working on code in individual files, we should always keep in mind what is going on behind the scenes and what is the impact of our changes on the big picture!

In general, we want to make sure that the following 3 points are always considered and preserved as much as possible

we want to preserve one-way nature of the dependency graph this is synonymous with preserving clean eager / lazy boundary in our codebase and can be extended further a one way direction when lazy sub-features are allowed to import from parent lazy features but not the other way around

we want to preserve isolation between independent branches of the dependency graph this maps one to one on the concept of full isolation between sibling lazy features (on the same level of navigation)

on a more micro scale, we want to prevent any cycles within dependency graph these often lead to situation which breask previous two points as well as just making it harder to take things apart once we want to re-use and therefore extract a piece of feature specific logic



Not having a clear concept for sharing of components & logic

Another common issue in many codebases can be illustrated with the following scenario…

We have already implemented 2 isolated lazy features (great) and now we need to add a third one.

As it turns out, one of the components from feature A could help us solve a similar use case in the new feature C.

In such case, what unfortunately tends to happen very often, is that we just import that standalone component from the feature A in the feature C and call it a day.

The application works, the lazy bundling still mostly works, BUT we have introduced invisible coupling between the features and therefore lost desired isolation between these features with most of its benefits!

A single component is not end of the world, but such cases tend to increase over time. This again leads to tangled dep graph and inability to change feature A without affecting feature C, which reduces our velocity and often introduces regression!

So what could we do instead?!

In this case, if we had a well-defined concept like ui for generic reusable components, the right thing to do would be to extract the desired component from the feature A into the ui.

This in practice also means that we would need to:

clean up any feature specific logic to make that component fully generic which is often possible (and desirable)
move component to the ui/ folder
import and integrate it in both feature A and feature C

After that we can use newly extracted generic component in both features without any issue or worry.

The one way dependency graph, isolation and therefore clean architecture is fully preserved!
Not being familiar with the two main systems in Angular and the rules by which they behave

When working with Angular everything is governed by two main underlying systems :

template context what can we use in the template of component A?

injector hierarchy which instance of an injectable are we going to inject in component A (or service A)?

Similar to underlying base reality of lazy loading and Javascript bundles these two systems represent same base reality from the Angular perspective and have therefore impact on everything in our codebase and especially on the architecture.

The impact on the architecture is then all about where do we want to implement our components or services so that they can be used in templates (or injected) in the features in a way that preserves clean architecture.

Great example of this is scoping of feature specific services to that specific feature, by removing the providedIn: 'root' option from the @Injectable() decorator and providing it in the lazy feature routes config instead.

export const routes: Routes = [
  {
    path: '',
    providers: [ProductService], // scoping service to a lazy feature
    children: [
      {
        path: '',
        loadComponent: () =>
          import('./product-list/product-list.component').then(
            (m) => m.ProductListComponent)
      },
    ],
  },
];


Do you enjoy the theme of the code preview? Explore our brand new theme plugin

Skol - the ultimate IDE theme

Northern lights feeling straight to your IDE. A simple but powerful dark theme that looks great and relaxes your eyes.

Gerne mehr

That way we can prevent the accidental consumption of a service which should only ever be consumed in feature A from the feature B!

And if such requirement is valid, we are forced to do it in a clean way, for example by extracting the service one level up parent lazy feature or even all the way up to the core!

Not using standalone components

Angular brought support for standalone components since version 14, so it has now been more than two years since the NgModules became optional!

Standalone components, bring the most value and are hands down the best solution especially when implementing reusable / generic UI components ( components which communicate only using inputs and outputs and not bound to any specific business logic or data source).

Using standalone components instead of NgModules means that our dependency graph becomes more granular and this higher resolution allows us to gain better insight of how each parts of app relate to each other and discover more issues!

Besides that, it allows lazy features to cherry-pick only those UI components which is actually needs instead of depending on all of them, as was often the case when applications grouped and exposed them in commonly used SharedModule!

Angular architecture can be awesome!

I hope that you enjoyed learning about the 10 most common Angular architectural mistakes and found at least a couple of actionable items which you will be able to put in practice in your existing and especially when starting new projects!

Also, don't hesitate to ping me if you have any questions using the article responses or using X(Twitter) DMs @tomastrajan...

And never forget, future is bright

Obviously the bright Future (📸 by Tomas Trajan in Madeira )

Build smarter UIs with Angular + AI

Angular + AI Video Course

A hands-on course showing how to integrate AI into Angular apps using Hash Brown to build intelligent, reactive UIs.

Learn streaming chat, tool calling, generative UI, structured outputs, and more — step by step.

Gerne mehr

Do you enjoy the content and want to master Angular's brand new Signal Forms?

Angular Signal Forms: Hands-On Masterclass

Master Angular's brand new Signal-Forms through 12 progressive chapters with theory and hands-on labs.

Learn form basics, validators, custom controls, subforms, migration strategies, and more!

Gerne mehr
Responses & comments

Do not hesitate to ask questions and share your own experience and perspective with the topic

Tomas Trajan

GDE for Angular & Web Technologies

public
"

I help developer teams deliver successful Angular applications through training and consulting with focus on NgRx, RxJs and Nx!

Ein Google-Developer expert für Angular und Webtechnologien, der als Berater und Angular-Trainer arbeitet. Derzeit unterstützt er weltweit Teams in Unternehmen bei der Implementierung von Kernfunktionalitäten, Architekturen, der Einführung von Best Practices, und der Optimierung von Arbeitsabläufen.

Tomas ist ständig bestrebt, seinen Kunden und der breiteren Entwicklergemeinschaft einen maximalen Nutzen zu bieten. Seine Arbeit wird durch eine umfangreiche Erfolgsbilanz unterstrichen, in der er populäre Fachartikel veröffentlicht, Vorträge auf internationalen Konferenzen und Meetups hält und zu Open-Source-Projekten beiträgt.

52

Blog posts

4.7M

Blog views

3.5K

Github stars

612

Trained developers

39

Given talks

8

Capacity to eat another cake

You might also like

Check out following blog posts from Angular Experts to learn even more about related topics like Angular or Modern Angular !

Angular Signal Forms: Custom Controls Without ControlValueAccessor

Build reusable Angular custom controls with FormValueControl, model(), touch events, and schema-driven validation—without writing a ControlValueAccessor.

Modern Angular
Signals
emoji_objects
emoji_objects
emoji_objects

Kevin Kreuzer

@nivekcode

12.08.2026

7 min read

Angular Signal Forms: The Missing Create/Edit Pattern

Learn a practical Angular Signal Forms pattern for create and edit flows, with route-based mode, edit data loading, linkedSignal prefilling, submit branching, and validation context.

Modern Angular
Signals
emoji_objects
emoji_objects
emoji_objects

Kevin Kreuzer

@nivekcode

01.08.2026

6 min read

Angular Signal Forms Essentials

Understand the core concepts behind modern Angular Forms. Learn how to create Signal Forms, wire them up in templates, use built-in and custom validators, handle cross-field validation, submit forms, and more.

Modern Angular
emoji_objects
emoji_objects
emoji_objects

Kevin Kreuzer

@nivekcode

14.02.2026

12 min read

Stärken Sie Ihr Team mit unserer umfassenden Erfahrung

Unsere Angular Experten haben viele Jahre damit verbracht, Unternehmen und Startups zu beraten, Workshops und Tutorials zu leiten und umfangreiche Open-Source-Ressourcen zu pflegen. Wir sind sehr stolz auf unsere Erfahrung im Bereich des modernen Frontends und würden uns freuen auch Ihrem Unternehmen zum Aufschwung zu verhelfen.

Vorname*
Nachname*
Email*
Firma
Dienstleistung
Ad-hoc consulting
NX monorepo setup
App & library architecture review
App & library starter templates
Component library & showcase templates
Custom reusable icon library setup
Pipeline review & optimization
Bundle size analysis & optimization
State management with NgRx
Server-side rendering
Product support
Project development outsourcing
One-on-one pair programming sessions
Frontend Heroes Workshop
Angular Mastery Workshop
Getting Reactive with RxJs Workshop
Angular State Management Workshop with NgRx
Other Angular related request...
Wo haben Sie von uns gehört?
Nachricht

This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply.

Nehmen Sie Kontakt auf
or
video_call
Get in touch call
FREE
