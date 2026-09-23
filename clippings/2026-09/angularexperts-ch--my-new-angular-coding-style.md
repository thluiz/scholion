---
url: "https://angularexperts.ch/blog/new-angular-coding-style?ref=dailydev"
captured_at: "2026-09-23T17:47:59+01:00"
title: "My new Angular Coding Style - Angular Experts"
domain: "angularexperts.ch"
---

My new Angular Coding Style

Embracing the New Angular: A Fresh Perspective on how to write Angular code.

Modern Angular
emoji_objects
emoji_objects
emoji_objects

Kevin Kreuzer

@nivekcode

02.12.2024

7 min read

share
link

Hey there, Angular enthusiasts!

If you've been following along with the latest updates in Angular, you're probably just as pumped as I am about Signals! 🚀 I mean, seriously, the potential Angular Signals offer are mind-blowing.

If you're curious about Signals and how they can transform your Angular development, be sure to check out our brand-new eBook on Angular Signals. Packed with practical tips and insights, this guide will help you leverage Signals for more efficient and responsive applications.

Do you enjoy the content and want to master Angular's brand new Signal Forms?

Angular Signal Forms: Hands-On Masterclass

Master Angular's brand new Signal-Forms through 12 progressive chapters with theory and hands-on labs.

Learn form basics, validators, custom controls, subforms, migration strategies, and more!

Gerne mehr

I've recently had the chance to dive deep and rewrite a large codebase using Signals and Signal-based APIs. Let me tell you, it was quite the ride!🏄‍♂

Along the way, new coding styles and patterns began to emerge, leading us to gradually adapt our coding guidelines. So, I thought, why not share our new coding style?

Before we get started

Now, before we dive in, here's the scoop: this blog is a mix of best practices and personal preferences. As you read through, I encourage you to decide what resonates with you. Some of these suggestions are widely recommended; others are just how we like to roll. Ultimately, the choice is yours, and it's all about finding what works best for you and your team.

To make this easier, I've categorized each section into two groups:

best practices: stuff that's generally good to do and recomended.

personal preferences: My Personal Takes: Feel Free to Adapt, but Note It's Not a General Best Practice — Just My Own Preference.

Standalone is the future

Best Practice Alert! 🚨

Since standalone components were released we have been using them more and more. Standalone components already became the de facto standard in Angular development.

With the release of Angular 19, the framework takes another leap forward by making standalone components the default.

// Standalone component < Angular 19
@Component({
  standalone: true,
  selector: 'my-component',
  template: `Hello World!`
})

// Standalone component in Angular 19
@Component({
  // no standalone flag needed anymore
  selector: 'my-component',
  template: `Hello World!`
})


This evolution cements standalone components as the cornerstone of modern Angular development.

By now, most developers are familiar with the benefits of standalone components: an easier mental model, improved developer experience (DX), and better tree-shaking capabilities. But Angular 19 goes even further to ensure consistency and modernity in your projects.

Pro tip! Angular 19 introduced a compiler flag which will thro an error if it encounters a component, directive or pipe that is not standalone.

{
  "angularCompilerOptions": {
    "strictStandalone": true
  }
}

All-in on Signals

Best Practice Alert! 🚨

As highlighted in the introduction, Signals are the future of Angular. With the introduction of the new signal APIs, writing clean, reactive code has never been easier or more intuitive.

To fully unlock the potential of this new paradigm, we strongly encourage leveraging all the signal APIs:

Signals
Computed Signals
Signal Inputs
Signal Queries

By embracing the full suite of signal APIs, you're not just enhancing your application's reactivity and performance—you're also future-proofing your codebase.

Signals are set to become a cornerstone of Angular's transition to Zoneless apps and will be essential when Signal components arrive.

We won't dive into more details here because signals are such a vast topic—you could easily write an entire book on them.
Oh wait, that's exactly what we did! 😅

Zoneless

Best Practice Alert! 🚨

Zone.js has long been a pain point for Angular developers, but with Angular v19, we can finally bid it farewell. This marks a significant leap in performance, as it reduces unnecessary change detection cycles and allows changes to be detected at a much more granular level.

However, removing Zone.js doesn't come without risks—it could lead to regressions in your application. This is where signals become essential. To ensure your app is ready for a zoneless future, make sure to fully embrace signals and use OnPush change detection.

If your app is built with signals and OnPush in a Zone-based environment, you're already prepared for the transition. Such an app will seamlessly run without Zone.js, ensuring it's both performant and future-proof. So start adopting these practices now to make your app zoneless-ready!

A New Era Without Traditional Lifecycle Hooks

Best Practice Alert! 🚨
Let's talk lifecycle hooks — or rather, let's talk about ditching them! With Signals, computed properties, and effects, a lot of the old Angular lifecycle hooks become obsolete. Say goodbye to ngOnInit and ngAfterViewInit, and hello to a more streamlined approach!

Writing Angular without lifecycle hooks, how would that work? Well, let's take a look at the following graphic.

I went with a color-coding system here: green means the old API should no longer be necessary, orange indicates that there are scenarios where the life cycle hooks may make sense but there's usually a better alternative.

Now, don't get me wrong; afterRender and afterNextRender are still lifecycle hooks, but they're the new kids on the block. When we say "without traditional lifecycle hooks," we mean those that have been around yet.

If you're finding it hard to see why this is so exciting, let's explore a simple example. Imagine a straightforward component that takes a number as input and displays whether it's even or odd. Here's how it works!

@Component({
  standalone: true,
  selector: 'is-even',
  template: `<h1>Is Even: {{ isEven }}</h1>`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class IsEvenComponent implements OnChanges {
  isEven: boolean | undefined;
  @Input({ required: true }) counter!: number;

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['counter']) {
      this.isEven = changes['counter'].currentValue % 2 === 0;
    }
  }
}


In order to display updates when the counter changes we have to use the ngOnChanges life cycle hook. Now, let's leverage the power of Signals and rewrite this component with the "no lifecycle hooks" approach.

@Component({
  standalone: true,
  selector: 'is-even',
  template: `<h1>Is Even: {{ isEven() }}</h1>`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class IsEvenComponent {
  counter = input.required<number>();
  isEven = computed(() => this.counter() % 2 === 0);
}


Simple and elegant.

Inject Over Constructor Injection

Another Best Practice! 💡

Dependency injection in Angular is like the secret sauce that makes everything taste better. 🍔 And in modern Angular, there are two primary ways to inject a dependency: through constructor-based injection or using the inject function.

Constructor-based injection is the OG way, but let me tell you why I'm all about the inject function now.

The inject function retains the correct type when combined with injection tokens, allowing for type-safe dependency injection.
The inject function can be used within other functions, enabling the creation of composable functions that utilize services.
With inheritance, there's no need to pass injected services to the superclass by calling super in the constructor.

Constructor injection relies on TypeScript's useDefineForClassFields flag, which needs to be explicitly set to false. The inject function, on the other hand, is more robust and future-proof, making it a solid choice. Plus, who doesn't love a little less boilerplate?

Heads up, though — switching to inject might mess with some of your unit tests. Especially if you've been rolling with traditional vanilla unit tests without the magic of TestBedModule to mock dependencies (often the case for service tests). So, be prepared to update your testing strategy to keep things smooth.

Going Constructor-Free

The Highly Opinionated Territory! 💡

Here's where we get a bit controversial — we're stepping into the highly opinionated zone.

We recently rewrote a big codebase to use Signal APIs, and guess what? We almost never needed constructors. Yep, you heard that right. A constructor-free style might sound radical, but it's actually not!

Using the inject function instead of constructor injection makes constructors obsolete for dependency injection. But what about initialization logic? With the use of Signals, initialization typically happens directly at the field creation, because Signals always need an initial value. There are rare to no cases where you really need a constructor.

Okay, but how do we handle effects or the new lifecycle hooks like afterRender or afterNextRender? These are typically set up inside a constructor, right?

@Component({ /* ... */ })
export class MyComponent {
  constructor() {
    effect(() => { /* ... */
    });
    afterRender(() => { /* ... */
    });
    afterNextRender(() => { /* ... */
    });
  }
}


Well, you can actually assign these to class fields. Check it out:

@Component({ /* ... */ })
export class MyComponent {
  #logProductChanges = effect(() => { /* ... */
  });
  #afterNextRenderRef = afterRender(() => { /* ... */
  });
  #afterNextRender = afterNextRender(() => { /* ... */
  });
}


A word of caution: your IDE might flag these as unused variables because technically, they aren't called within the class.

This approach makes your code cleaner and more organized. It's like the debate between named functions vs. anonymous functions — there's no right or wrong answer; it's all about personal preference and project needs.

No More Async Pipes: A Modern Strategy

Best Practice Alert! 💡

If you're all in on Signals (and why wouldn't you be?), then it's time to wave goodbye to the async pipe. Instead, we're moving towards using Signals exclusively. Don't panic — we're not ditching RxJS entirely.

You'll still use RxJS for handling HTTP responses, but before binding data to the template, you'll convert it using toSignal from the interop package. This gives you a more consistent and reactive template experience, while still leveraging RxJS for those complex data streams. Neat, huh?

@Component({
  template: `{{ someValue() }}`
})
export class MyComponent {
  someValue = toSignal(someStream$);
}

Replacing Private with

Highly Opinionated Again! 💡

Okay, let's get into the weeds. When writing TypeScript, many of us declare variables as private. There are two ways to do this: using the private keyword or the # symbol.

Now, this might seem like just a style choice, but there's actually a technical difference:

private Keyword: A TypeScript-specific modifier that restricts access within the class. However, it's only enforced during compile time. Once the TypeScript is compiled to JavaScript, it's a free-for-all!

#: This is a JavaScript feature known as a private class field, and it's enforced at runtime. That means variables declared with # are truly private and cannot be accessed or modified outside the class, even after compiling to JavaScript. More robust, right?

I used the private keyword for years — who hasn't? But one day, during a lunch break while planning a big refactor, my colleague pitched the idea of switching to #. At first, I was skeptical (aren't we all about new things?), but after thinking about it — # offers runtime privacy, it's technically more robust, and hey, it's less to type.

Why not give it a shot?

After just one day, I was sold! Something clicked, and I haven't looked back since. Sometimes you just have to push your ego aside, try something new, and see if it fits.

@Component({
  // ...
})
export class MyComponent {
  #userService = inject(UserService);
}


So there you have it, folks! There are exciting ways to use Signals to shape your Angular codebase to be cleaner, more efficient, and dare I say — more fun to write. At the end of the day, it's all about finding what works best for you and your team.

So go ahead, experiment, and don't be afraid to break some eggs. After all, that's how you make a killer omelette! 🍳
