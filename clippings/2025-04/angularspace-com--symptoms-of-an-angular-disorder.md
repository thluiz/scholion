---
url: "https://www.angularspace.com/symptoms-of-an-angular-disorder/?ref=dailydev"
captured_at: "2025-04-02T11:06:11-03:00"
title: "Symptoms of an Angular Disorder"
domain: "angularspace-com"
---

Bad practices often involve phrases like "avoid too complex components" or "separate logic," which sound quite abstract. This often means that we might answer interview questions about these bad practices but will have a hard time recognizing them in the codebase.

---
![Symptoms of an Angular Disorder](https://www.angularspace.com/content/images/size/w1075h650/2025/02/angularspacethumb-erick-2-2--20-.jpg)

There are millions of Angular projects out there, and we have undoubtedly encountered lots of poorly written code. Also, there are many "Angular Bad Practices" articles—I wrote several of them—but trust me, this is not one of them.

Bad practices often involve phrases like "avoid too complex components" or "separate logic," which sound quite abstract. This often means that we might answer interview questions about these bad practices but will have a hard time recognizing them in the codebase.

So, in this article, we are going to tackle some of the symptoms that might not themselves be considered bad practices but can be indicative of a larger chronic illness that a given Angular project might be suffering from.

> Note: it is important to understand that everything mentioned in this article is only an indication that something might be off, and we do not seek to refactor everything just to avoid some instances of these "symptoms".

Let's get started!

## Too many inputs on a components

Sometimes, we might see a component that tries to be _incredibly_ customizable. This is not necessarily a bad thing itself, however, it often results in a very cumbersome component. Take a look at this component that is displaying a dropdown:

Now, I have purposefully not provided the code for the component itself, but you can imagine what mess is going on there: a lot of `if` statements to handle the dropdown being multiselect or not, a lot of mess in the template, long code just to define inputs.

### What is the problem?

1.  Huge component that is hard to maintain
2.  Ugly template whenever we use this component
3.  Easy to forget a property unless marked as required

### What can be done?

1.  Break the component into two: dropdown and multiselect
2.  Use a configuration object instead of multiple inputs
3.  Injectable provider of default options so they can be customized

This can result in a much better template:

And, alternatively, we can use a default configuration:

Then, we won't even need to provide the `config` input unless we want to override the defaults. Also, the component can implement a `mergeConfig` functionality so that only configs provided via the input override the default configuration.

Also, if the default configuration needs to be different for a certain part of the application, it is easy to provide a different configuration for only that parts using providers in routing:

As we can see, components being flexible is not bad, however, trying to be over-the-top generic can result in lots of trouble, and it might be best for all parties involved to break the components into different ones depending on their purpose and use configurations objects + Dependency Injection (DI) to simplify everything.

### When can this be permissible?

In the case of large, highly customizable UI component libraries, having a lot of inputs can make sense. However, both pieces of advice mentioned above still apply - it might be a good idea to use them. Now, onto the next one!

## Injecting a parent component

Sometimes, when we work with complex UIs that we already broke down into smaller components, we might encounter situations where normal ways of communicating between those aren't enough.

For instance, almost everyone was tempted at some point to pass a `formControl` or `formGroup` to a child component as an input. While this can work in a simple scenario, it will introduce more complexity and even bugs when an `OnPush` change detection strategy is applied to the child component (parent sets the value of a control but that is not readily apparent in the child component if it uses `OnPush`).

So, in such scenarios, developers sometimes (thought thankfully not very often) come up with a the idea of just injecting the parent component and using its reference to access anything it has. Here is the simples showcase:

### What is the problem?

1.  Incredibly tight coupling between the two components - Child components simply cannot function without being nested in the parent component's template (this can be circumvented by using the `optional` DI lookup modifier, but will introduce even more complexity)
2.  Hard to test - now we need to mock the parent component in the child component's tests
3.  Can still results in change detection issues
4.  Bugs related to data flow will become very hard to find and fix

### What can be done?

1.  Avoid doing this at all costs
2.  Use injectables (services, `InjectionToken`\-s) to share data that cannot be shared via inputs

Here is an example of moving the `formGroup` to an injectable:

As we can see, both components now have access to the same `formGroup`, but are not tightly coupled. Additionally, if we are talking about a small form, using [`ControlValueAccessor`](https://angular.dev/api/forms/ControlValueAccessor?ref=angularspace.com) might also be a good idea.

### When can this be permissible?

When we are building components that are actually meant to only be used together, this can make sense. For example, a `TabsComponent` might have projected `TabComponent`\-s inside its template:

In this case, the `TabComponent` does not make sense on its own, and it will be perfectly okay to inject the `TabsComponent` into it. Now, let's talk about an elusive case.

## Large _for_ loops in template

We often talk about how we need to break components down into smaller ones, but it is often not very obvious when this "threshold" has been crossed and we need to create a new child component and move some logic over there.

However, one big indication for this is having a `*ngFor` or `@for` loop in the template with a large template inside. Consider the following snippet:

### What is the problem?

1.  Large piece of UI that can easily be abstracted away
2.  A separate cognitive unit that "breaks" the logical flow of the UI: we can think of "one comment" and a "list of comments" with the understanding that it might have the functionality from above.
3.  Less code in a given template

### What can be done?

Now this one is very obvious, just move the piece of this template to a child component:

### When can this be permissible?

When we are dealing with a very simple piece of HTML code, abstracting away might just complicate things:

No need to move this simple piece of code to a separate component. But now, let's move to the child component itself and discuss some red flags there

## Service injected in a supposedly presentational component

There is a lots of talk about the container-presenter pattern, and how we should separate logic from the UI in all of front-end framework communities. In short, the idea is that we should have components that are responsible for the UI only, which would receive the data they need via inputs (and optionally emit events via outputs), and components that are responsible for the logic only, like getting the necessary data, setting up forms, etc.

For instance, the very `<app-comment>` component we discussed above is an example of such a presentational component: it receives the comment data and emits events when a user interacts with it for the parent component to handle.

Such a component is good when it is only used to _display_ the data; and why is that? Well, imagine we have a lot of different section in our apps that have comments: a product description that allows user reviews, a blog post that allows comments, maybe videos, and so on. Eash time the comment looks exactly the same, however underneath, it might perform differently: a comment in a video section wants to update a completely different entity with a completely different URL (like "videos//comments/") than, say, a comment in the blog post section ("posts//comments/").

With such a situation, it makes sense that we might want to make the `CommentComponent` as simple and reusable as possible, and delegate the logic of updating the comment to the parent component.

Now, imagine we did something like this inside the `CommentComponent`:

### What is the problem?

1.  The component is no longer independent and less reusable - we can only use it in contexts where the `CommentService` is available
2.  The component does way more than one might expect from a component that is supposed to just display some UI
3.  Harder to test - now we need to mock the service in the component's tests

### What can be done?

There are no easy solutions to this since when the service is injected into a component, it most probably is being used somewhere, creating tight couplings. The way to deal with this is to delegate the functionality to the parent component.

### When can this be permissible?

When we are building a component that is actually meant to be used in a very specific context, this can make sense. For instance, a `UserComponent` that is supposed to display the user's data and allow them to change their password might have a `UserService` injected into it. However, in most cases, this is a red flag that the component is doing too much and should be refactored.

## Using manual change detection

Now, this one is tricky, and happens rarely, but you might run into some code like this:

Now, it is not necessary that the code would contain an Observable, but it is often the case. So, what does it even mean? Well, Angular has a very powerful change detection mechanism that is able to detect changes in the component's template bindings and update the UI accordingly. As we all know, this process is fully automatic and very, very rarely needs manual enhancement.

### What is the problem?

1.  A bit confusing for another developer who reads this code - why is the change detection being called manually?
2.  Might actually be unnecessary - change detection is a complex topic and sometimes developers, having not understood it properly, encounter a complex scenario and put a manual call to change detection "just in case"
3.  Increases the amount of CD cycles, which might potentially result in performance issues

### What can be done?

1.  Do not use manual change detection unless you are absolutely sure you need it
2.  `async` pipe in template, in case when you deal with observables
3.  Setter in @Input (if you work with versions prior 16) or a combination of input + computed from a signal
4.  Update your state from sync functions executed from template (event)
5.  Using pipes to transform data
6.  If you feel you need it, examine the code as a whole and try to figure out why it works the way it works. Switching to Observables/signals might help improve the situation
7.  If absolutely necessary, at least provide a detailed comment explaining why the manual change detection is being used in a given situation

### When can this be permissible?

It is hard to predict when this might be necessary. One scenario can be if we're developing a complex component that also works with a third-party library that does not play well with Angular's change detection. Maybe it registers a lot of listeners and results in lots of unnecessary CD cycles. In such cases, we might opt-in into running the component outside of Angular's zone (using `ngZone.runOutsideAngular()`), and then manually call change detection when necessary.

## Lots of `subscribe` calls

Now, this is a popular one: we have all seen a dreaded component like this:

As we can see, this component does a lot in terms of subscribing to things. And we didn't even include logic to unsubscribe from these Observables!

### What is the problem?

1.  Hard to maintain - we need to keep track of all subscriptions and unsubscribe from them when the component is destroyed
2.  Potential race conditions - sometimes some data from Observable A is needed in the subscription to Observable B, but arrives later than B, causing bugs and requiring even more complexity
3.  Looks bad - this one is not even subjective, the code it really hard to read and visually "scary"
4.  Has the potential to grow even worse

### What can be done?

1.  Every time an Observable is used to extract data to a local property, (`someObservable$.subscribe(data => this.data = data)` scenario), ditch that subscription and use the `async` pipe in the template, or, alternatively, convert the Observable to a signal
2.  When subscribing a lot to some Reactive Forms controls, consider switching the form to a template-driven form with signals and utilize tools like `computed`, `linkedSignal`, and `effect`. Read more about this in my [blog post](https://armenvardanyan.dev/blog/why-i-switched-to-template-driven-forms?ref=angularspace.com).
3.  If subscriptions are necessary to handle side-effects of HTTP calls (loading, error), consider using the [Resource API](https://www.angularspace.com/everything-you-need-to-know-abour-resource-for-now/).

### When can this be permissible?

When dealing with a third-party API that works in an imperative way (like the reactive forms themselves), there might be no other option than to subscribe. Try your best to minimize the amount of subscriptions and only resort to them when absolutely confident there is no other way.

## Zero or very few custom directives

Finally, this one is more of a general advice, but if a codebase lacks any custom directives (or has very few of them), it might be a sign that the developers are not utilizing the full power of Angular.

### What is the problem?

1.  A fairly large application will definitely have some complex template logic that might be better off being in a directive, but probably gets copy-pasted around
2.  Sometimes components are used to handle some UI logic that can be done via a directive instead, complicating the template code
3.  This might also signal that developers are not very familiar with all the powers of Angular

### What can be done?

There is no general solution to this, but the very first step would be learning about the powers of Angular directives. I would suggest reading my mega-article about [Angular Directives](https://www.angularspace.com/mega-article-superpowers-with-directives-and-dependency-injection/), which covers _everything_ you need to know about them.

Next, you might start noticing patterns in your template that repeat a lot, and think about how they can be turned into a directive. For instance, if you have a lot of elements that need to be shown only to authenticated users, you might create an `*appAuthenticated` directive that would handle this logic. Here is an example of such a directive:

And then, you can simple use it in your template whenever you want to hide elements based on user's auth status:

Finally, you might notice components that don't actually modify the UI a lot and rather act as "add-ons" to some existing elements, and consider if you can actually use a directive in their stead, simplifying your template

### When can this be permissible?

When you are working on a very small project that does not have a lot of complex UI logic, it might be okay to not have any custom directives. However, as the project grows, pay attention tou your templates and components, and some patterns will probably emerge

## In Conclusion

Angular is a huge framework with lots of interconnected parts, and there are a bunch of good and bad practices, of which we all are aware to some degree. As sometimes it is hard to recognize a bad pattern, I am hopeful this article will shed some light on how we can start thinking about our Angular codebases to reveal underlying issues and quickly fix them.

![Gg2RPJKWwAAHSId.png](https://www.angularspace.com/content/images/2025/01/Gg2RPJKWwAAHSId.png)  
My book, Modern Angular, is now in print! I spent a lot of time writing about every single new Angular feature from v12-v18, including enhanced dependency injection, RxJS interop, Signals, SSR, Zoneless, and way more.

If you work with a legacy project, I believe my book will be useful to you in catching up with everything new and exciting that our favorite framework has to offer. Check it out here: [https://www.manning.com/books/modern-angular](https://www.manning.com/books/modern-angular?ref=angularspace.com)

___

![](https://www.angularspace.com/content/images/2025/02/Screenshot-2024-11-13-at-15.52.00--1---3---1---1-.jpg)

**Last Update:** February 19, 2025
