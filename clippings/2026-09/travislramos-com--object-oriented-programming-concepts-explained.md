---
url: "https://travislramos.com/blog/object-oriented-programming-concepts-explained?ref=dailydev"
captured_at: "2026-09-25T21:40:06+01:00"
title: "Object Oriented Programming Concepts Explained"
domain: "travislramos-com"
---

April 8, 2020 (6y ago)

### [](#what-is-object-oriented-programming)What is Object Oriented Programming

Put simply, object oriented programming is the use of objects that contain both data and methods that interact with each other. For a language to be considered object oriented, it must have certain features like:

*   Encapsulation
*   Inheritance
*   Abstraction
*   Polymorphism

These features, along with a language having Objects and Classes, make up what we know as object oriented programming.

### [](#what-is-encapsulation)What is Encapsulation

Encapsulation is achieved when an object keeps its state private, so other objects don't have direct access to this state. Instead they must call a list of public methods to manipulate the state.

Take the photo below for example. The Cat has 3 different fields that are all private, plus a private meow() method. No other object that calls the Cat can change these values.

However, the Cat also has a list of public methods(Sleep, Play, and Feed). These public methods when called, will change the Cat's state as well as invoke the meow() method for Play and Feed.

![Encapsulation Description](https://images.ctfassets.net/4g6i57n5oteb/7pG5MS6BQ7OrfdDOFW1AT6/c21316f15877735252cdb46a5c56281b/encapsulation.png)

### [](#what-is-inheritance)What is Inheritance

Inheritance is the creation of a hierarchy within your classes. You start off with a parent class, and then extend onto child classes which will reuse all of the fields and methods from the parent class plus any unique methods it implements.

Like the example below, the Teacher and the Student are both Person's, but one has a subject while the other has a school. Person is the parent class and Teacher & Student are the child classes.

![Inheritance Description](https://images.ctfassets.net/4g6i57n5oteb/4V4U8gwQXfIi0bm8ImHdyq/06f3c9b3227f1b1b69ea5ecd1f158456/inheritance.png)

### [](#what-is-abstraction)What is Abstraction

Abstraction is the process in which an object only exposes itself at a high-level, and hides its internal implementation details. Other objects that are calling this don't care how things are being implemented, they just need the information to be processed.

Think of this as a small set of public methods that any other class can call wihout knowing how they are actually being implemented behind the scenes.

![abstraction description image](https://images.ctfassets.net/4g6i57n5oteb/4XCrVqynXh5fhE5gPLxCA5/0df1d7b2b5508611f4809354a2779abe/abstraction.png)

Take the cell phone from the picture above for example. We don't know how the buttons on the phone are doing what they are doing, we just know what they do.

### [](#what-is-polymorphism)What is Polymorphism

Polymorphism means somthing occuring in multiple different forms. It allows objects of different types to be accessed through the same interface with each type implementing its own independent version of this interface.

![Polymorphism Description](https://images.ctfassets.net/4g6i57n5oteb/3QG2Uu2eqv4TaBWD0Fv591/a85137f01e94fb5a131697a49aa4dc47/polymorphism.png)

The star, circle, and rectangle are all Figure's, they are just different types of figures. They all have a calculateSurface() and calculatePerimeter() method. The difference is how they are actually doing this calculation.

### [](#now-thats-all-folks)Now Thats All Folks

Thanks for taking the time to read this post! If you found it useful, or think others would enjoy it, share it!
