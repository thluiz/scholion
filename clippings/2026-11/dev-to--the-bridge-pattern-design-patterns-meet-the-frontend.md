---
url: "https://dev.to/coly010/the-bridge-pattern-design-patterns-meet-the-frontend-46fc"
captured_at: "2026-11-16T00:53:28+00:00"
title: "The Bridge Pattern - Design Patterns meet the Frontend"
domain: "dev-to"
---

The Bridge Design pattern is one of the design patterns I've had most difficulty wrapping my head around. 🤯 _Note: This article assumes some basic knowledge of Interfaces in Object Oriented Programming_

In this article, I'll explain what this pattern is, how it can be used and an example of where it is currently used in the Frontend space (psst Angular 🚀).

We'll go over a few things:

*   What is it? 🤔
*   Let's break it down 😱
*   But why? 😐
*   Where can I find it in action? 🚀
*   Where else could I use it? 🎉

## [](#what-is-it)What is it? 🤔

The Bridge Pattern can be thought of as part if the Composition over Inheritance Argument. It essentially "bridges a gap" between the Abstraction and the Implementation. These terms might cause a little confusion so lets clear them up.

*   Implementation - This is an interface that will describe a set of specific behaviour that can be used by any Object in our codebase. It can have multiple concrete impletations that adhere to the contract defined in the interface.
*   Abstraction - This is the object that will provide an API that will make use of an underlying Implementation. It acts as a layer over the top of the Implementation that can be further refined through inheritance if required.

Ok, mind blown. 🤯 I know, that can be a bit hairy to read.

So let's take a quick look at a UML Diagram (I know, sigh, but it really does help):

[![Bridge Design Pattern UML](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fr365newb6l1yqecctdcu.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fr365newb6l1yqecctdcu.png)

As we can see from the diagram, the pattern allows us to separate two interfaces that can define the specifics of an object, in this case the type of Shape the object is and the Color that Shape is.

We can create multiple colors, or multiple shapes, without worrying about one impacting the other, therefore increasing loose coupling in our codebase! 🔥

## [](#lets-break-it-down)Let's break it down 😱

Keeping our example above in mind, the Abstraction would be our Shape class, whilst our Implementation is the Color class.

The Abstraction contains a reference to the Implementation via a property on the class (hence the composition over inheritance), in our case, Shape has a Color property. Any class that implements the Color contract can then be used by any Shape property.

The consumer of the Abstraction doesn't need to worry about the underlying implementation whilst the pattern itself also increases loose coupling between the Abstraction and the Implementation.

If you're like me, looking at code can help clear things up. So let's do just that!

We'll be using TypeScript for these examples

```


// Define an interface for the Implementation
interface Color {
    log(): string;
}

// Define an abstract class for the Abstraction
abstract class Shape {
    color: Color;

    constructor(color: Color) {
        this.color = color;
    }

    logMe() {
        console.log(`I am a ${this.color.log()} shape.`);
    }
}

// Create a Concrete Implementation
class Red implements Color {
    log() {
        return 'red';
    }
}

class Blue implements Color {
    log() {
        return 'blue';
    }
}

// Create a refined Abstraction that behaves slightly differently
class Circle extends Shape {
    constructor(color: Color) {
        super(color);
    }

    logMe() {
        console.log(`I am a ${this.color.log()} circle.`);
    }
}

class Triangle extends Shape {
    constructor(color: Color) {
        super(color);
    }
}

// Instantiate the circle with a concrete implementation
const circle = new Circle(new Red());
const triangle = new Triangle(new Blue());

circle.logMe();
// Output: I am a red circle.

triangle.logMe();
// Output: I am a blue shape.


```

Enter fullscreen mode Exit fullscreen mode

Awesome! We can create as many `Colors` as we like, or as many `Shapes` as we like, without affecting one or the other! 🚀🚀🚀

Keeping things simple and separated increases the maintainability and testability of our code, which leads to better code! We can extend and new shapes and colors in the future very easily now too!

## [](#but-why)But why? 😐

Let's take a look at some reasons why we would use this pattern:

*   The Bridge Pattern decouples the Abstraction and the Implementation, therefore allowing the two to differ independently.
*   It keeps the Abstraction and the Implementation in it's their own inheritance hierarchy, allowing them to grow without affecting the other.
*   The Abstraction does not need to know about the Concrete Implementation and therefore it can be set or swapped at run-time without breaking the Abstraction.

Awesome, but where can I use it? 🤔

## [](#where-can-i-find-it-in-action)Where can I find it in action? 🚀

Ok, the Bridge Pattern is awesome. It can increase our loose coupling, but, where can we _actually_ use it? Where is it being used in the wild?

The `ControlValueAccessor` is an interface with methods that must be implemented for any class that implements it. Angular provides it's own concreate implementations of the `ControlValueAccessor` Implementation, but any developer can implement the interface and any `NgControl` will be able to use it!

In other words, an implementation outside of the Angular Framework is perfectly acceptable by an Abstraction within the Framework! 🔥🔥

Likewise, a developer can create their own `NgControl` and any of the concrete implementations provided by Angular will be able to work with it! 💥💥

Hopefully that can help you understand the power behind The Bridge Pattern, but if you still need your own use case, keep reading!

## [](#where-else-could-i-use-it)Where else could I use it? 🚀

Well, I've found that a perfect example of this in the Frontend world would be in a Data Access Layer.

You can have the following:

*   An Abstraction defining an Entity Service that will handle logic related to the entities within your system.
*   An Implementation defining an API Interface that allows you to interact with _any_ potential backend system or API.

Let's take a quick look at this in action:

We'll start with our Implementation (API Interface):

```


export interface IApiService {
    get<T>(): T;
    getAll<T>(): T[];
    add<T>(entity: T): void;
    update<T>(entity: T): void;
    delete<T>(entity: T): void;
}


```

Enter fullscreen mode Exit fullscreen mode

and next we will define our Abstraction (Entity Service):

```


export abstract class EntityService {
    apiService: IApiService;

    constructor(apiService: IApiService) {
        this.apiService = apiService;
    }
}


```

Enter fullscreen mode Exit fullscreen mode

Ok, so we've set up our Abstraction and our Implementation. Let's put them to use!

First let's create a UserService that refines our Abstraction.

```


export interface User {
    id: string;
    name: string;
    email: string;
}

export class UserService extends EntityService {
    activeUser: User;

    constructor(apiService: IApiService) {
        super(apiService);
    }

    addNewUser(user: User) {
        this.apiService.add(user);
    }

    // Here we perform some logic custom to the UserService
    // But use the underlying bridge between the concrete
    // implementation and the abstraction to update the
    // active user after some custom logic
    setActiveUserEmail(email: string) {
        this.activeUser.email = email;
        this.apiService.update(this.activeUser);
    }
}


```

Enter fullscreen mode Exit fullscreen mode

Now that we have a Refined Abstraction, let's go ahead and create a Concrete Implementation

```


export class CustomApiService implements IApiService {
    get<T>(): T {
        // fetch the user from the api
    }

    getAll<T>(): T[] {
        // etc
    }

    add<T>(entity: T): void {
        // etc
    }

    update<T>(entity: T): void {
        // etc
    }

    delete<T>(entity: T): void {
        // etc
    }
}


```

Enter fullscreen mode Exit fullscreen mode

Ok, now let's use our Concrete Implementation along with our Refined Abstraction:

```


const apiService = new CustomApiService();
const userService = new UserService(apiService);

userService.addNewUser({...} as User);


```

Enter fullscreen mode Exit fullscreen mode

Awesome! Our `UserService` does not need to know the nitty gritties of the `IApiService` Implementation for it to still perform as expected.

What happens if down the road requirments change and suddenly we can't use the `CustomApiService` any more! 😱

Have no fear, the Bridge Pattern is here! 😍

Simply create a new Concrete Implementation, and supply that to the `UserService` instead:

```


// Create new implementation
export class MongoDBService implements IApiService {
   // etc
}

// Swap out the api service
const apiService = new MongoDbService();

// No need to change the rest!
const userService = new UserService(apiService);

userService.addNewUser({...} as User);


```

Enter fullscreen mode Exit fullscreen mode

Isn't that awesome! 🚀🚀🚀

* * *

Hopefully you learned a bit (_more?_) about the Bridge Pattern from this article, a potential use-case for it and how it is used in Angular.

If you have any questions, feel free to ask below or reach out to me on Twitter: [@FerryColum](https://twitter.com/FerryColum).
