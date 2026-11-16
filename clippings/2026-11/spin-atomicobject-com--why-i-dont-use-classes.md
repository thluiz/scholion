---
url: "https://spin.atomicobject.com/2020/03/12/why-i-dont-use-classes"
captured_at: "2026-11-16T03:02:42+00:00"
title: "Why I Don’t Use Classes"
domain: "spin-atomicobject-com"
---

Recently, one of my teammates noted that our project’s codebase doesn’t have a lot of classes. The observation wasn’t framed positively or negatively. It was just an observation about a particular code style of the team as a whole.

I didn’t think much about it at the time. But looking back, this observation has lead to some good self-reflection on what I value when writing software. I didn’t write this post to persuade others to follow patterns that I tend to follow. But I’m hoping this post is a catalyst for your own self-reflection.

For context, my projects lately have been in full-stack Typescript, and what I value in writing software is highly influenced by the experiences in the Typescript ecosystem. I’m guessing there are cross-cutting concerns here that are applicable in other ecosystems, but I’m not going to claim that’s the case.

I also should note that I don’t actively avoid writing classes. I just lean toward other solutions, typically functional solutions over object-orientated solutions. Since I spend the majority of my time in the Typescript ecosystem, I have the luxury of choosing either paradigm to solve the current problem at hand.

## Abstractions

I’m terrible at making good abstractions with classes. I’ll admit that the results have been mixed. But typically, using inheritance and polymorphism to model a problem space evolves into a mess. I think I know at least two sources of the mess.

### Terrible Method Names

First, classes end up having terrible method names if those methods are overriding base class methods. I’ve been fooled by too many method names that end up doing more than what they said they would. A base class will often set the name for a method based on what it should **do**. But as other classes extend and override those methods to address their version of the problem space, they usually end up having some other responsibilities in addition to the original task.

For example, I’ve implemented classes that manage database tables, so it implements an abstract class that needs an “update” method. Well, some tables when updating need to do more than just “update” a record, such as insert a log into a side table. While that might be innocent enough at first, I’ve seen quite a few methods continue to grow in their sets of responsibilities.

Maybe I just have organization problems. But I’ve found much more success creating groups of functions that don’t belong in a class. And I can give them any name I want and split responsibilities into new functions as I please.

### Classes Grow

Secondly, I’ve noticed that classes have a tendency to grow large. They will collect pieces of functionality that need to live in the context of the class, usually to access the internal state of that class. This dependency on the internal state makes it difficult to break the methods up into logical chunks.

This usually isn’t a huge pain point, but teams I’ve been on have preferred using groups of functions in modules that have state passed to them. It tends to be easier to break large modules into smaller ones if needed.

## State Management

I’m not great at managing state in classes. State contained and controlled by a class has been the cause of interesting and undesirably behaviors. While using class-managed state is likely well suited for a suite of problems, I’ve seen a pattern of buggy implementations coming out of class-based solutions that held their own state.

One concrete example of this pattern is class-based React components. Time and time again, whenever I would try to use a class-based component, that component would eventually be the source of a bug if it tried to manage some internal state.

I thought that maybe state management was just inherently complex, and maybe it wasn’t the classes to blame. However, now that I’ve been using React’s hooks to manage state for functional components, I haven’t come across this sort of bugs in my UI code. It seems like removing the class construct and replacing it with functions that can be passed around between components have simplified state management on my projects.

## Alternatives to Classes

As I’ve mentioned above, I like to use modules that expose groups of functions. These functions accept state and other dependencies. These modules tend to look like what my colleague Drew describes as [the functional module pattern](https://spin.atomicobject.com/typescript-functional-module-pattern/).

Maybe functions are more natural than classes in the Typescript ecosystem. There’s a chance that I would admire classes a bit more if I did more .NET development. Maybe I would benefit if I tried to use the object-orientated paradigm rather than the functional paradigm. I just haven’t found a compelling reason to do that on my project as of late.
