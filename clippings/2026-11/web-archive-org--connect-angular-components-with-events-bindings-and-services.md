---
url: "https://web.archive.org/web/20200810163737id_/https://killalldefects.com/2020/02/08/connect-angular-components-with-events-services-and-binding/"
captured_at: "2026-11-16T07:55:16+00:00"
title: "Connect Angular Components with Events, Bindings, and Services - Kill All Defects"
domain: "web-archive-org"
---

In this article we’ll explore how to use Angular two-way binding, events, and services to wire up a user interface and allow different components to interact with each other without being strongly tied to one another. We’ll do this by using `ngModel` to collect commands from a user, send them to a service, and have another component subscribe to events from the service whenever a command is entered.

## The Project

In this article we’ll start with a text-based game called [“Doggo Quest”](https://killalldefects.com/2020/02/01/game-design-with-event-modeling/) that I’m currently developing. The game has an [already created user interface](https://killalldefects.com/2020/02/05/from-mockup-to-angular-material/) with a story view and a player input area. However, the game does nothing at the moment as these areas don’t talk to each other at all.

![](https://i2.wp.com/killalldefects.com/wp-content/uploads/2020/02/image-31.png?w=770&ssl=1)

In this article, we’ll change that by using Angular two-way binding, events, event emitters, services, and subscriptions to link together the user interface. The user will be able to type in a command and see it appear in the game’s story view, along with a generic response.

![](https://i0.wp.com/killalldefects.com/wp-content/uploads/2020/02/AngularWIringHIgh.gif?w=770&ssl=1)

_Note: Later on in this series we may explore [NgRx](https://ngrx.io/), [RxJs](https://www.learnrxjs.io/) and more complex ways of handling events and state management, but for now I want to start with the simplest way to manage state and events in basic Angular._

If you want to follow along from the beginning, check out [this tag of the Doggo Quest repository](https://github.com/IntegerMan/DoggoQuest/tree/SelectiveComponentRendering). The finished code from the end of this article [is also available](https://github.com/IntegerMan/DoggoQuest/tree/AngularEventEmitters).

## Create the Service

Right now our user interface is just an input box and a button that do nothing. In order to connect the command entry component to the main story display, we’ll add a service.

Services are classes designed to provide some functionality to other areas of the application. They’re very close to being ordinary objects except for one distinction: Angular can inject services into other component’s constructors automatically (more on this later).

To create a component, we’ll launch our command line and navigate into the project directory, then type `ng g s <name-of-service>` to **g**enerate a new **s**ervice. Keep in mind that you don’t type in `service` in the name of your service as Angular will automatically end your service in `.service` for you.

In my case, I run `ng g s story` to generate the `story.service`.

![](https://i0.wp.com/killalldefects.com/wp-content/uploads/2020/02/image-29.png?w=770&ssl=1)

## Build the Service Method and EventEmitter

Next, we’ll flesh out the service by adding an `EventEmitter` and a `handlePlayerInput` method as shown below:

Let’s stop for a moment and talk about event emitters. An `EventEmitter` is an object that can emit events (as the name suggests) that other code can subscribe to and get notifications of the events when they occur.

![](https://i1.wp.com/killalldefects.com/wp-content/uploads/2020/02/crop-0-0-645-603-0-image-32.png?resize=323%2C302&ssl=1)

Events can be emitted simply by calling `.emit` on the `EventEmitter` and providing an instance of the emitter’s generic type as shown on line 24 above.

Subscribers will receive an event with that object as a parameter. We’ll see what this looks like for a subscriber later in this article. You should keep in mind that any `EventEmitter` can have no subscribers or many different subscribers. This flexible architecture keeps services decoupled from the individual components that rely on them.

Right now all this will do is log the message to the console, but later on in this article we’ll set up an event emitter so other components can subscribe to command events.

## Send Commands to the Service

Okay, now that we have a service, we can take advantage of Angular’s built-in dependency injection capabilities to provide the `story.service` to our `command-entry.component`. We do this simply by adding it to the constructor as an argument as seen below on line 12:

You don’t need to worry about how the service gets to the component. Angular automatically provides the service for you from your application module.

Now let’s talk about the `submitCommand` method. This is the method our component’s template will call (we’ll see more about this next section) that will then pull the value out of the `Command` field and pass it on to the service.

Note here that we’re clearing the `Command` field after sending the command on to the service. We’ll talk more about this next section.

Let’s take a look at the user interface of the `command-entry.component`:

Much of this is standard markup, though it uses [Angular Material](https://killalldefects.com/2020/02/05/from-mockup-to-angular-material/) for some additional polish.

Let’s focus on some of the binding and event-based syntax in this class, and we’ll start from the bottom-up due to order of complexity.

The `(click)` handler on line 6 tells Angular to watch for the click event on the button and to invoke the `submitCommand` method in the component’s class definition when the event is raised. This is how our user interface knows to invoke that method.

Similarly, on line 4 we see a handler on `keyup.enter`. This is fancy Angular syntax that only listens to keyup events related to the enter key. In this case, we want to invoke the `submitCommand` method when the user hits enter for usability purposes.

## Two-way Binding

Incidentally, in Angular, parentheses in templates `()` mean _events_ while brackets `[]` mean _binding_. Think of `()` as indicating that something goes _into_ the component’s class definition and the `[]` as indicating that something comes _out of_ the class definition.

Now let’s look at the syntax on line 3 of the snippet above: `[(ngModel)]="Command"`

This syntax is one of the things that takes the most adjusting to with Angular. It’s often referred to as a “banana in a box”, alluding to the parentheses nested inside of the brackets.

Think about this `[()]` syntax as simply a _combination_ of our property binding `[]` syntax and our event binding `()` syntax. In other words, when we use `[()]` we want a two-way binding where the component’s user interface receives updates from the class’s fields, and updates that might impact the source field (like the user typing into the textbox) also get pushed back to the class.

Confused? Think back to the code-behind for this component. We have a `Command` field that gets updated via the binding when the user types in something in the input box.

Additionally, after we call `submitCommand` we clear out the `Command` field to an empty string. The two-way binding kicks in and Angular’s [change detection](https://blog.angular-university.io/how-does-angular-2-change-detection-really-work/) tells the user interface to set the input box’s value to that empty string.

## Subscribe to EventEmitters

Now that we’ve covered the service and the `command-entry.component`, let’s finish up by focusing on the `story-view.component` that displays the story to the user.

Similar to the `command-entry.component` we’ll use Angular’s dependency injection to provide the `story.service` to the component. Only instead of calling methods on that service, we’ll subscribe to any event emitted by the `EntryAdded` `EventEmitter` as shown below:

Let’s look first at line 12. This component implements the `OnInit` and `OnDestroy` interfaces. This forces us to add `ngOnInit` and `ngOnDestroy` methods to the component. Angular looks for these methods on components and will invoke them when the component is loaded and unloaded respectfully.

We can use these methods to subscribe and unsubscribe from events we care about in other services. As we see on lines 24 and 29, we subscribe and unsubscribe from an `EventEmitter` and store the subscription in a field so we can unsubscribe later.

The unsubscribe aspect of this is important as it ensures that the component is properly disposed of and does not lead to code running on future events that is related to “dead” components. Failure to unsubscribe can lead to errors and poor performance.

* * *

Finally, let’s take a look at line 24. With this one line we subscribe to the `EntryAdded` event emitter on our service and add the new entry to the end of our story array. Angular’s binding and change detection mechanisms will automatically add a component to the user interface for this based on how we [previously set up our user interface](https://killalldefects.com/2020/02/05/from-mockup-to-angular-material/).

## Conclusion

With only a few steps, we took a user interface that existed in style and structure only and we wired it together using binding, events, a service, and an `EventEmitter`.

What’s more, we did this in a very flexible way so we could replace entire components without needing to make extensive changes in other areas.

Now when the user enters text, it immediately appears in the story view along with a default response as shown below:

![](https://i0.wp.com/killalldefects.com/wp-content/uploads/2020/02/AngularWIringHIgh.gif?w=770&ssl=1)

It’s not too hard to see how the rest of this project will be about parsing the user’s input and coming up with an intelligent response, but we still need to talk about important concepts such as accessibility and user interface testing.

Stay tuned.
