---
url: "https://dev.to/marinvirdol/3-tips-that-will-simplify-your-application-state-management-21e9"
captured_at: "2026-11-16T01:37:01+00:00"
title: "3 Tips That Will Simplify Your Application State Management"
domain: "dev-to"
---

## [](#the-introduction)The Introduction

The goal of this blog post is to introduce you to some of the most common pitfalls that make state management unnecessarily difficult and to outline 3 simple strategies that will help you avoid them.

Managing the state of an application if extremely hard and I think is the main reason why applications tend to become so complex. For some reason, we try to manage the complexity by over-engineering our solution to the problem. There are so many ways of managing the state of your application ([redux](https://redux.js.org/), [flux](https://facebook.github.io/flux/), [finite state machines](https://en.wikipedia.org/wiki/Finite-state_machine)) and countless abstraction libraries on top of these.

But first, let's quickly define what I call the state of an application so we are on the same page.

## [](#the-definition-of-state)The Definition Of State

The state of an application is a representation of a system at a given time. The UI of a front-end application is a representation of the state. If a user changes the state by interacting with your application, the UI may look completely different afterward because it is represented by this new state.

The state is able to keep the data of different components in sync (or not) because each update will re-render all relevant components. Moreover, you can use the state to communicate between different components.

I would suggest that there are the following types of state:

*   **Persistent State** - this one lives on the server and it is accessible, for example, via a REST endpoint
*   **Navigation State** - where is the user in the application? Is he on the sign-in page, the sign-up page or the profile page?
*   **Local UI State** - what is the colour of the button? Is the panel expanded or not? Is the modal open
*   **Client State** - you can think of the filters selected by the user when dealing with a large list of items, the current page in the list of items

As you can see, there are many aspects to be taken into consideration when thinking about the state of our application. The **biggest problem** in state management arises when we try to **coordinate all these state sources** (server data, web workers, UI components, navigation etc) all of which **update the state concurrently.**

**How we decide to sync all this data is one of the most important decision when designing the state management of our application.**

## [](#the-3-simple-strategies-that-will-simplify-your-application-state-management)The 3 Simple Strategies That Will Simplify Your Application State Management

### [](#1-identify-the-type-of-state-you-are-dealing-with)1\. Identify the type of state you are dealing with

Make this your first step in your state management decision tree. Developers seriously underestimate the value of doing this (including myself) but it is extremely important in order to keep it simple.

To help you identify it, you should think if this particular state of the application should be saved for later use or if you want the user to share the exact same state of the application with another user. If this is the case you should consider to reflect the state of the application in the URL.

**Why is important?** Except for the persistent state, the rest of the state is not stored on the server which means that there is no way of saving it for later use or for sharing it with other users. Also, if the user refreshes the page he will land on the same state of the application.

**Example.** Think about when you want to share a Youtube video with a friend from a specific moment. The link you are going to share will have all the information needed to play the exact same video from that exact specific moment.

### [](#2-keep-your-state-data-as-close-as-possible)2\. Keep your state data as close as possible

The next step in simplifying the state of your application is to keep your state data as close as possible to where it is needed. This comes with the following two benefits: **maintainability** and **performance**.

**Performance**

Imagine you have a hierarchy of components and you keep your state in the root component. Each time the state changes the entire tree is re-rendered and that is perfectly fine if all the components in the tree depend on that state. But what if that change only affects a component somewhere at the bottom of the hierarchy? You want to keep that part of the state as close as possible to the component that needs it. This way the component tree will re-render a lot fewer components than a state change at the top of the tree.

**Maintainability**

From the maintainability point of view always start a new component by managing it’s internal state inside of that component and if a sibling or the parents need access to that state just lift that part of the state up to the parent. This goes both ways. If you have a piece of state in a parent component that only one child needs, then move that piece to the child level.

### [](#3-dont-keep-your-entire-state-globally)3\. Don't keep your entire state globally

I've notice this pattern especially in applications that use redux. There are developers that like to keep their entire state into redux. If you are using redux you should aim on keeping only global state into redux and the local state as close as possible to the components that need that data.

The problem with using redux for every piece of state is **increased complexity**. Redux adds a lot of complexity to your application because maintaining the state involves working with reducers, actions, dispatching calls which results in having your state management all over the place. It get really **hard to maintain.** Ben Lesh puts it really well in one of his tweets:

[https://twitter.com/BenLesh/status/1241525265228017670](https://twitter.com/BenLesh/status/1241525265228017670)

## [](#conclusions)Conclusions

As you can see, as soon as the application is starting to grow, so does the complexity of managing the state. This is why **the state management strategy is not something that you want to add late in your project, you should plan for it because it can be the decisive factor for the success or failure of your application.**

_“If you fail to plan, you are planning to fail!” - Benjamin Franklin_
