---
url: "https://dev.to/mayruiz27/design-patterns-for-frontend-developers-2ii3"
captured_at: "2020-11-12T08:59:08-03:00"
title: "Design Patterns for Web Development - DEV Community 👩‍💻👨‍💻"
domain: "dev-to"
---

# Design Patterns for Web Development

Nov 3
・3 min read

There are times where building a design structure for your project might seem daunting when you don't know how to start. Knowing design patterns can help us as developers to find out how to better build our software depending on how scalable we will want it or the kind of functionality we need.

Design patterns are typical solutions to common problems in software design. Rather than being a code solution, they are general concepts you can implement in your software to expect certain behavior from it. The book "Design Patterns: Elements of Reusable Object-Oriented Software", which has become a classic in software development, introduced 23 patterns to solve object-oriented design. Here I'm going to cover 3 design patterns which are some of the most used in front-end development.

But first, why learning design patterns is so important?

1.Recognize patterns in libraries and languages   
Some libraries like Angular use design patterns in the way they are structured and the way they create solutions to problems. This gives us an idea of how we can use this current behavior to build our own solutions.

2.Avoid reinventing the wheel

It's easier to create solutions others have previously faced and succeeded in implementing them, than coming up with a solution from scratch.

3.Shared vocabulary

Within development teams, it's easier to talk about how to design your solutions if everyone in the team is familiarized with design patterns. It is easier to explain an abstract idea just by using its name rather than explaining the whole concept.

### Types of Patterns

There are 3 types of design patterns depending on their behavior.

- Creational patterns: Provide a structure to create objects easily, provide certain flexibility on its creation, and reuse existent code.
- Structural patterns: Provide a structure that helps assemble objects and classes into larger structures.
- Behavioral patterns: Assign responsibilities between objects and take care of communication.

### Singleton

Singleton is a creational design pattern that restricts class to have only one instance, while also creating a global access point to this instance. It is used when control access to a shared resource is needed.

- Use this pattern when you need to ensure control access to a resource that might return inconsistencies if it is changed by two different objects at the same time. (Ex. Databases, state of an object)

```
class Singleton {
    private static instance: Singleton;

    private constructor() { }

    public static getInstance(): Singleton {
        if (!Singleton.instance) {
            Singleton.instance = new Singleton();
        }

        return Singleton.instance;
    }
}
```

### Observer

Observer is a behavioral design pattern in which objects get information about any events happening to the object they are observing. The observer pattern defines a subscriber method, which will update every object that is subscribed to itself, making sure every subscriber gets the latest update.

An example of an observer in our daily life would be subscribing to a newsletter. The moment you join the mailing list you are notified when there is a new publication.

- Use this pattern when changes on one object may require updating other objects, and the actual set of objects is unknown or changes dynamically.

```
class Observable {

    // List of observers
    private observers: Observer[] = [];

    public attach(observer: Observer): void {
        const exists = this.observers.includes(observer);
        if (!exists) {
            this.observers.push(observer);
        }
    }

    public detach(observer: Observer): void {
        const observerIndex = this.observers.indexOf(observer);
        if (observerIndex !== -1) {
            this.observers.splice(observerIndex, 1);
        }
    }

    public notify(): void {
        for (const observer of this.observers) {
            observer.update(this);
        }
    }
}

class Observer {
    public update(observable: Observable): void {
        // Update observer according to Observable state
    }
}
```

### Decorator

Decorator is a structural pattern that lets you add new characteristics to objects by adding a wrapper that contains the behaviors.

We can find examples of this pattern in food delivery apps where you can choose any toppings or extras to your food, then the application adds the corresponding cost to your order.

- Use this pattern when it's necessary to add these extra behaviors on run time, or when inheritance is not possible.

```
interface Coffee {
    getCost(): int;
}

class SimpleCoffee implements Coffee {
    public getCost(): int {
        return 2;
    }
}

class CoffeeDecorator implements Coffee {
    protected decoratedCoffee: SimpleCoffee;

    constructor(decoratedCoffee: SimpleCoffee) {
        this.decoratedCoffee = decoratedComponent;
    }

    public getCost(): int {
        return this.component.getCost();
    }
}

class WithMilk extends CoffeeDecorator {
    public getCost(): int {
        return super.getCost + 0.5;
    }
}
```

Even though knowing these design patterns is useful to build better solutions, it is not always necessary to use them in every project we come across. We need to take some time to think about the pros and cons of implementing them on our own code. Remember to avoid overcomplicating your code if you will not get any benefit from using them in that particular case.

Have you used any other design patterns in your web development projects? Let me know which are the ones you use the most.

To learn more about design patterns check out:  
[Refractoring Guru - Design Patterns](https://refactoring.guru/design-patterns)
