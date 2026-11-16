---
url: "https://dev.to/codingdive/introducing-state-machine-advent-24-bite-sized-blog-posts-about-state-machines-and-statecharts-2ce0"
captured_at: "2026-11-16T00:52:01+00:00"
title: "Introducing state machine advent: 24 bite-sized blog posts about state machines and statecharts"
domain: "dev-to"
---

TL;DR: I'm creating one piece of content each day until Christmas to explain the theory and application of state machines and statecharts.

## [](#my-backstory-of-how-and-why-i-got-to-use-xstate)My backstory of how and why I got to use XState

A couple of months ago, I went down the rabbit hole of looking for the best state management library. When I glanced at the number of issues in my backlog and knowing the complexity of some of the tasks, I knew that the library would need to scale extremely well and provide a great developer experience.

I stumbled upon state machines/statecharts and was immediately reminded of my limited - but horrific - experience with them in college. My professor probably gave the worst introduction to the world of finite automata I could've hoped for, but despite knowing about his incompetence, there was no way that I would ever want to think about _Greek letters_ when writing code.

When turning to Redux, I turned a blind eye on the concept of a global store and the need for additional packages like Redux thunks to properly handle asynchronicity. Nonetheless, there was one particular event that made me pause and rethink my decision. After days of going through countless blog posts, tutorials and resources on how to write beautiful Redux apps, my attempt of creating the _hello world app of state management libraries_ was halted when my todo mvc app looked like this: [https://imgur.com/a/KdXN4JB](https://imgur.com/a/KdXN4JB).

At some point, my example app got into an invalid state where it somehow finished loading the todos while also indicating that todos are still being loaded at the same time (wut?). I simply forgot to set the `loading` boolean flag back to false once the todos were resolved but this should not have happened. I knew that the two states can never be present at the same time and yet my program was completely clueless about this exclusive relationship between the states. I quickly came to realize that Redux was not the "best state management library" I was hoping to find because I couldn't model the transition from one state to another with ease. This would undoubtedly introduce more bugs in the future so I had to go back to the drawing board.

Having learned from my experience with Redux, I needed a programming paradigm that would allow me to strictly model all the possible states (and their transitions) of my application. Naturally, I went back to finite state machines and found some great JavaScript implementations. After devouring their documentation and videos, I fell in love with [XState](https://github.com/davidkpiano/xstate).  
I started using it and contrary to my instinctive belief, state machines and statecharts can be defined in plain JavaScript objects without any Greek letters. 😄 To this day, I'm still learning new things about its extensive API and have never looked back at any other state management library.

This is my very first blog post. Any feedback is greatly appreciated. 😊

## [](#about-this-series)About this series

I'll publish one piece of content each day to teach you about the ins and outs of state machines and statecharts. As you'll learn in this series, they'll make your app more resilient, eliminate bugs and allow you to reason about your code more easily.

* * *

Day 1:  
[https://dev.to/codingdive/state-machine-advent-the-simplest-state-machine-that-will-improve-your-code-today-1-24-5bfi](https://dev.to/codingdive/state-machine-advent-the-simplest-state-machine-that-will-improve-your-code-today-1-24-5bfi)

Day 2:  
[https://dev.to/codingdive/state-machine-advent-anatomy-of-a-state-machine-2-24-4gfo](https://dev.to/codingdive/state-machine-advent-anatomy-of-a-state-machine-2-24-4gfo)

Day 3:  
[https://dev.to/codingdive/state-machine-advent-baby-s-first-state-machine-with-xstate-3-24-3b62](https://dev.to/codingdive/state-machine-advent-baby-s-first-state-machine-with-xstate-3-24-3b62)

Day 4:  
[https://dev.to/codingdive/state-machine-advent-visualize-your-state-machines-with-diagrams-as-you-code-4-24-1m7b](https://dev.to/codingdive/state-machine-advent-visualize-your-state-machines-with-diagrams-as-you-code-4-24-1m7b)

Day 5:  
[https://dev.to/codingdive/state-machine-advent-invoking-a-state-machine-in-react-1nm7](https://dev.to/codingdive/state-machine-advent-invoking-a-state-machine-in-react-1nm7)

Day 6:  
[https://dev.to/codingdive/state-machine-advent-from-implicit-to-explicit-state-machine-6-24-2nge](https://dev.to/codingdive/state-machine-advent-from-implicit-to-explicit-state-machine-6-24-2nge)

Day 7:  
[https://dev.to/codingdive/state-machine-advent-statically-type-state-machines-with-typescript-7-24-445m](https://dev.to/codingdive/state-machine-advent-statically-type-state-machines-with-typescript-7-24-445m)

Day 8:  
[https://dev.to/codingdive/state-machine-advent-why-state-machines-don-t-scale-8-24-eoi](https://dev.to/codingdive/state-machine-advent-why-state-machines-don-t-scale-8-24-eoi)

Day 9:  
[https://dev.to/codingdive/state-machine-advent-introduction-to-nested-and-parallel-states-using-statecharts-7ed](https://dev.to/codingdive/state-machine-advent-introduction-to-nested-and-parallel-states-using-statecharts-7ed)

Day 10:  
[https://dev.to/codingdive/state-machine-advent-how-to-match-against-nested-states-in-xstate-10-24-4hhf](https://dev.to/codingdive/state-machine-advent-how-to-match-against-nested-states-in-xstate-10-24-4hhf)

Day 11:  
[https://dev.to/codingdive/state-machine-advent-a-safer-way-to-type-events-and-state-11-24-4o0e](https://dev.to/codingdive/state-machine-advent-a-safer-way-to-type-events-and-state-11-24-4o0e)

Day 12:  
[https://dev.to/codingdive/state-machine-advent-you-are-saying-i-can-put-infinite-state-into-my-finite-automata-2647](https://dev.to/codingdive/state-machine-advent-you-are-saying-i-can-put-infinite-state-into-my-finite-automata-2647)

Day 13:  
[https://dev.to/codingdive/state-machine-advent-update-xstate-context-with-actions-1e9d](https://dev.to/codingdive/state-machine-advent-update-xstate-context-with-actions-1e9d)

Day 14:  
[https://dev.to/codingdive/state-machine-advent-guard-state-transitions-guard-actions-14-24-oc3](https://dev.to/codingdive/state-machine-advent-guard-state-transitions-guard-actions-14-24-oc3)

Day 15:  
[https://dev.to/codingdive/state-machine-advent-one-event-two-possible-state-transitions-15-24-588k](https://dev.to/codingdive/state-machine-advent-one-event-two-possible-state-transitions-15-24-588k)

Day 16:  
[https://dev.to/codingdive/state-machine-advent-a-better-way-to-type-guards-and-actions-g3g](https://dev.to/codingdive/state-machine-advent-a-better-way-to-type-guards-and-actions-g3g)

Day 17:  
[https://dev.to/codingdive/state-machine-advent-reusable-conditional-logic-with-custom-guards-4nec](https://dev.to/codingdive/state-machine-advent-reusable-conditional-logic-with-custom-guards-4nec)

Day 18:  
[https://dev.to/codingdive/state-machine-advent-let-the-machine-handle-accessibility-for-you-2n21](https://dev.to/codingdive/state-machine-advent-let-the-machine-handle-accessibility-for-you-2n21)

Day 19:  
[https://dev.to/codingdive/state-machine-advent-asynchronous-code-in-xstate-102p](https://dev.to/codingdive/state-machine-advent-asynchronous-code-in-xstate-102p)

Day 20:  
[https://dev.to/codingdive/state-machine-advent-the-power-of-null-events-3kn8](https://dev.to/codingdive/state-machine-advent-the-power-of-null-events-3kn8)

Day 21:  
[https://dev.to/codingdive/state-machine-advent-invoking-a-reusable-state-machine-1gln](https://dev.to/codingdive/state-machine-advent-invoking-a-reusable-state-machine-1gln)

Day 22:  
[https://dev.to/codingdive/state-machine-advent-building-hierarchy-using-the-actor-model-and-cross-machine-communication-2ln1](https://dev.to/codingdive/state-machine-advent-building-hierarchy-using-the-actor-model-and-cross-machine-communication-2ln1)

Day 23:  
[https://dev.to/codingdive/state-machine-advent-accessing-private-actor-state-in-components-3o44](https://dev.to/codingdive/state-machine-advent-accessing-private-actor-state-in-components-3o44)

Day 24:  
[https://dev.to/codingdive/state-machine-advent-everything-you-need-to-master-statecharts-1fe](https://dev.to/codingdive/state-machine-advent-everything-you-need-to-master-statecharts-1fe)
