---
url: "https://blog.logrocket.com/design-patterns-in-node-js/"
captured_at: "2026-11-16T19:03:21+00:00"
title: "A guide to Node.js design patterns - LogRocket Blog"
domain: "blog-logrocket-com"
---

_**Editor’s note**: This article was last updated on 20 March 2023 to include a section on the builder, prototype, and dependency injection design patterns. Learn more about the latter in [this article.](https://blog.logrocket.com/dependency-injection-node-js-typedi/)_

![](https://blog.logrocket.com/wp-content/uploads/2019/06/design_patterns_node_js_web.png)

Design patterns are part of the day to day of any software developer. In this article, we will look at how to identify these patterns out in the wild and look at how you can start using them in your own projects.

_Jump ahead_:

*   [What are design patterns?](#what-are-design-patterns)
*   [Immediately Invoked Function Expressions](#immediately-invoked-function-expressions-iife)
*   [The factory method pattern](#factory-method-pattern)
*   [The singleton pattern](#singleton-pattern)
*   [The builder pattern](#builder-pattern)
*   [The prototype pattern](#prototype-pattern)
*   [The observer pattern](#observer-pattern)
*   [Dependency injection](#dependency-injection)
*   [The chain of responsibility pattern](#chain-of-responsibility-pattern)
*   [Streams](#streams)

## What are design patterns?

Design patterns are a way for you to structure your solution’s code in a way that allows you to gain some kind of benefit, such as faster development speed, code reusability, etc.

All patterns lend themselves quite easily to the OOP (object-oriented programming) paradigm. Although, given JavaScript’s flexibility, you can implement these concepts in non-OOP projects as well.

When it comes to design patterns, there are too many of them to cover in just one article. In fact, books have been written exclusively about this topic and every year new patterns are created, leaving their lists incomplete.

A very common classification for the pattern is the one used in the [GoF book](https://en.wikipedia.org/wiki/Design_Patterns) (The Gang of Four Book) but because I’m going to review just a handful of design patterns, I will ignore the classification and simply present you with a list of patterns you can see and start using in your code right now.

The first pattern we’ll explore is one that allows you to define and call a function at the same time. Due to the way JavaScript scopes works, using IIFEs can be great to simulate things like private properties in classes. In fact, this particular pattern is sometimes used as part of the requirements of other, more complex ones. We’ll see how in a bit.

### What does an IIFE look like?

Before we delve into the use cases and the mechanics behind IIFE, let me quickly show you what it looks like:

(function() {
   var x \= 20;
   var y \= 20;
   var answer \= x + y;
   console.log(answer);
})();

By pasting the above code into a Node.js REPL or even your browser’s console, you’d immediately get the result because, as the name suggests, you’re executing the function as soon as you define it.

The template for an IIFE consists of an anonymous function declaration, inside a set of parenthesis (whichs turn the definition into a function expression, or an an assignment) and then a set of calling parenthesis at the end tail of it:

(function(/\*received parameters\*/) {
//your code here
})(/\*parameters\*/)

### Use cases

There are a few use cases where using an IIFE can be a good thing. These include:

### Simulating static variables

Remember [static variables](https://en.wikipedia.org/wiki/Static_variable)? Think other languages such as C or C#. If you’re not familiar with them, a static variable gets initialized the first time you use it and then it takes the value that you last set it to. The benefit is that if you define a static variable inside a function, that variable will be common to all instances of the function, no matter how many times you call it. It greatly simplifies cases like this:

function autoIncrement() {
    static let number \= 0
    number++
    return number
}

The above function would return a new number every time we call it (assuming, of course, the static keyword is available for us in JS). We could do this with generators in JS, that’s true, but pretend we don’t have access to them, you could simulate a static variable like this:

let autoIncrement \= (function() {
    let number \= 0

    return function () {
            number++
            return number
    }
})()

What you’re seeing above is the magic of closures all wrapped up inside an IIFE. Pure magic. You’re basically returning a new function that will be assigned to the `autoIncrement` variable (thanks to the actual execution of the IIFE). With the scoping mechanics of JS, your function will always have access to the number variable (as if it were a global variable).

### Simulating private variables

As you may know, ES6 classes treat every member as public, meaning there are no private properties or methods. That’s out of the question, but thanks to IIFEs you could potentially simulate that:

const autoIncrementer \= (function() {
  let value \= 0;

  return {
        incr() {
                  value++
        },

        get value() {
                  return value
        }
  };
})();
\> autoIncrementer.incr()
undefined
\> autoIncrementer.incr()
undefined
\> autoIncrementer.value
2
\> autoIncrementer.value \= 3
3
\> autoIncrementer.value
2

The code above shows you a way to do it. Although you’re not specifically defining a class which you can instantiate afterward, you are defining a structure, a set of properties, and methods that make use of variables that are common to the object you’re creating but that are not accessible (as shown through the failed assignment) from outside.

## The factory method pattern

The factory method pattern is one of my favorite pattern because it acts as a tool you can implement to clean your code up.

The factory method allows you to centralize the logic of creating objects (which object to create and why) in a single place. This allows you to focus on simply requesting the object you need and then using it.

This might seem like a small benefit but it’ll make sense, trust me.

### What does the factory method pattern look like?

This particular pattern would be easier to understand if you first look at its usage, and then at its implementation.

Here is an example:

( \_ \=> {

    let factory \= new MyEmployeeFactory()

    let types \= \["fulltime", "parttime", "contractor"\]
    let employees \= \[\];
    for(let i \= 0; i < 100; i++) {
            employees.push(factory.createEmployee({type: types\[Math.floor( (Math.random(2) \* 2) )\]})    )}

    //....
    employees.forEach( e \=> {
            console.log(e.speak())
    })

})()

The key takeaway from the code above is the fact that you’re adding objects to the same array, all of which share the same interface (in the sense they have the same set of methods) but you don’t really need to care about which object to create and when to do it.

You can now look at the actual implementation. As you can see, there is a lot to look at but it’s straightforward:

class Employee {

    speak() {
            return "Hi, I'm a " + this.type + " employee"
    }

}

class FullTimeEmployee extends Employee{
    constructor(data) {
            super()
            this.type \= "full time"
            //....
    }
}

class PartTimeEmployee extends Employee{
    constructor(data) {
            super()
            this.type \= "part time"
            //....
    }
}

class ContractorEmployee extends Employee{
    constructor(data) {
            super()
            this.type \= "contractor"
            //....
    }
}

class MyEmployeeFactory {

    createEmployee(data) {
            if(data.type \== 'fulltime') return new FullTimeEmployee(data)
            if(data.type \== 'parttime') return new PartTimeEmployee(data)
            if(data.type \== 'contractor') return new ContractorEmployee(data)
    }
}

### Use case

The previous code already shows a generic use case but if we wanted to be more specific, one particular use case I like to use this pattern for is handling error object creation.

Imagine having an Express application with 10 endpoints, where every endpoint you need to return has between two to three errors based on the user input. We’re talking about 30 sentences like the following:

if(err) {
  res.json({error: true, message: “Error message here”})
}

That wouldn’t be a problem until the next time you had to suddenly add a new attribute to the error object. Now you have to go over your entire project, modifying all 30 places. And that would be solved by moving the definition of the error object into a class. That would be great unless you had more than one error object, and again, you’ll have to decide which object to instantiate based on some logic only you know. See what I’m trying to get to?

If you were to centralize the logic for creating the error object, then all you’d have to do throughout your code would be something like:

if(err) {
  res.json(ErrorFactory.getError(err))
}

That’s it; you’re done, and you never have to change that line again.

## The singleton pattern

The singleton pattern is another oldie but goodie. It’s a simple pattern but it helps you keep track of how many instances of a class you’re instantiating. The pattern helps you keep that number to just one, all of the time.

* * *

### More great articles from LogRocket:

*   [Learn how LogRocket's Galileo AI](https://logrocket.com/products/galileo-ai) watches user sessions for you, proactively surfaces the most impactful issues, and gives you the context to fix them
*   [See how Meilisearch](https://blog.logrocket.com/meilisearch-logrocket-mcp/) improved free trial experience and feature adoption with LogRocket's MCP
*   Keep up with which AI frontend dev tech reigns supreme with our [AI dev tool power rankings & comparison](https://blog.logrocket.com/ai-dev-tool-power-rankings/)
*   [Check out the CSS features](https://blog.logrocket.com/switching-between-node-versions-during-development/) currently shaping frontend development
*   These [10 React Native UI libraries](https://blog.logrocket.com/creating-custom-mouse-cursor-css/) could speed up development and polish your design
*   Which AI CLI tool should you use? [This comparison could help you decide](https://blog.logrocket.com/tested-5-ai-cli-tools/)

* * *

The singleton pattern allows you to instantiate an object once, and then use that one every time you need it, instead of creating a new one without having to keep track of a reference to it, either globally or just passing it as a dependency everywhere.

### What does the singleton pattern look like?

Normally, other languages implement this pattern using a single static property where they store the instance once it exists. The problem here is that, as I mentioned before, we don’t have access to static variables in JS. So we could implement this in two ways, one would be by using IIFEs instead of classes.

The other would be by using ES6 modules and having our singleton class using a locally global variable, in which to store our instance. By doing this, the class itself gets exported out of the module, but the global variable remains local to the module.

It sounds a lot more complicated than it looks:

let instance \= null

class SingletonClass {

    constructor() {
            this.value \= Math.random(100)
    }

    printValue() {
            console.log(this.value)
    }

    static getInstance() {
            if(!instance) {
                    instance \= new SingletonClass()
            }

            return instance
    }
}

module.exports \= SingletonClass

And you could use it like this:

`const Singleton = require("./singleton")`

const obj \= Singleton.getInstance()
const obj2 \= Singleton.getInstance()

obj.printValue()
obj2.printValue()

console.log("Equals:: ", obj \=== obj2)

The output would look like this:

0.5035326348000628
0.5035326348000628
Equals::  true

### Use cases

When trying to decide if you need a singleton-like implementation or not, you need to consider how many instances of your classes you will need. If the answer is two or more, then this is not the pattern for you.

Once you’ve connected to your database, it would be a good idea to keep that connection alive and accessible throughout your code. This can be solved in many different ways and this pattern is one of them.

Using the above example, we can extrapolate it into something like this:

const driver \= require("...")

let instance \= null

class DBClass {

    constructor(props) {
            this.properties \= props
            this.\_conn \= null
    }

    connect() {
            this.\_conn \= driver.connect(this.props)
    }

    get conn() {
            return this.\_conn
    }

    static getInstance() {
            if(!instance) {
                    instance \= new DBClass()
            }

            return instance
    }
}

module.exports \= DBClass

Now you’re sure that no matter where you are, if you’re using the `getInstance` method, you’ll be returning the only active connection (if any).

## The builder pattern

In this design pattern, the focus is to separate the construction of complex objects from their representation. In Node.js builder, the pattern is a way to create complex objects in a step-by-step manner.

When there are multiple ways to create an object or many properties inside the object, seasoned developers usually opt for builder design patterns. The essence of the builder design pattern is to break down complex code into smaller and more manageable steps, so this design pattern makes it easier to modify the complex code easily over time.

One of the core features of the builder pattern is that it allows the developer to create a blueprint for the object. Then, while instantiating the object, the developer can create various instances of the object with different configurations.

### What does the builder pattern look like?

Most of the time while developing a solution one has to handle too many properties. One approach is to pass all the properties in the constructor.

If developed properly, the code will run but passing so many arguments inside the constructor will look ugly and if it’s a large-scale application, it might become unreadable over time.

To avoid this, developers use builder design patterns. Let’s understand this by looking at an example:

class House {
  constructor(builder) {
    this.bedrooms \= builder.bedrooms;
    this.bathrooms \= builder.bathrooms;
    this.kitchens \= builder.kitchens;
    this.garages \= builder.garages;
  }
}
class HouseBuilder {
  constructor() {
    this.bedrooms \= 0;
    this.bathrooms \= 0;
    this.kitchens \= 0;
    this.garages \= 0;
  }
  setBedrooms(bedrooms) {
    this.bedrooms \= bedrooms;
    return this;
  }
  setBathrooms(bathrooms) {
    this.bathrooms \= bathrooms;
    return this;
  }
  setKitchens(kitchens) {
    this.kitchens \= kitchens;
    return this;
  }
  setGarages(garages) {
    this.garages \= garages;
    return this;
  }
  build() {
    return new House(this);
  }
}
const house1 \= new HouseBuilder()
  .setBedrooms(3)
  .setBathrooms(2)
  .setKitchens(1)
  .setGarages(2)
  .build();
console.log(house1); // Output: House { bedrooms: 3, bathrooms: 2, kitchens: 1, garages: 2 }

In the example above, the `H``ouse` class is the class that represents the complex object we want to create while the `HouseBuilder` class is the class that is providing a step-by-step way to create instances of the `House` class with different configurations.

In `HouseBuilderClass`, there are several methods to set the values for the various properties of the `House` object and there is also a build method inside it that, when called, returns a new `House` object with the specified configurations.

The step-by-step way to create the `House` object is that first we will create a new instance of the HouseBuilder class and then use the respective methods of the `HouseBuilder` class to set the desired values of the `House` object’s properties.

After setting the values, we will call the `build` method to create a new instance of the `House` class with the desired specific configurations.

### Use cases

When deciding whether to opt for a builder design pattern or not, the deciding factors are complexity in object creation, flexibility in object creation, and other available options. These are also the main use cases for this design pattern.

If object creation is a complex process and the developer wants to be flexible and create different variations of the object and also has multiple options that can be taken to create the object, then the best design pattern to opt for is the builder pattern.

Let’s take a use case where we want to instantiate various objects of the `Person` class that can have different combinations of properties.

Here, the developer wants flexibility in the creation of objects. Instantiating a person’s object is a complex process as it can have multiple properties that need to be catered to. In this case, opting for a builder design pattern is a good idea:

 class Person {
  constructor(name, age, email, phoneNumber) {
    this.name \= name;
    this.age \= age;
    this.email \= email;
    this.phoneNumber \= phoneNumber;
  }
}
class PersonBuilder {
  constructor() {
    this.name \= "";
    this.age \= 0;
    this.email \= "";
    this.phoneNumber \= "";
  }
  withName(name) {
    this.name \= name;
    return this;
  }
  withAge(age) {
    this.age \= age;
    return this;
  }
  withEmail(email) {
    this.email \= email;
    return this;
  }
  withPhoneNumber(phoneNumber) {
    this.phoneNumber \= phoneNumber;
    return this;
  }
  build() {
    return new Person(this.name, this.age, this.email, this.phoneNumber);
  }
}
// Example usage
const person1 \= new PersonBuilder()
  .withName("Alice")
  .withAge(30)
  .withEmail("alice@example.com")
  .build();
const person2 \= new PersonBuilder()
  .withName("Bob")
  .withPhoneNumber("555-1234")
  .build();

The `Person` class is representing the complex object we want to create and to do this, `PersonBuilder` class is providing the step-by-step way. To achieve our goal we instantiate the `PersonBuilder` and use its methods to set the desired value for `Person Object`. Finally, we call the build method to create a new instance of `Person` class.

After going through this process, we can see that we get specific desired configurations of the `Person` object by using the different methods of `PersonBuilder`, i.e., `person1` has the properties of name, age, and email while `person2` has the specific properties of name and number only.

## The prototype pattern

In the context of the Node, a prototype design pattern is classified as a creational design pattern and allows us to create new objects based on a pre-existing object. The gist of this design pattern is to create an object as a prototype and then instantiate a new object by cloning the prototype.

This pattern is extremely useful when we have to create multiple objects with similar properties and methods. In a Node-based ecosystem, the prototype design pattern is mostly used to create objects and implement inheritance. One of the major benefits of using prototype design patterns is that we can avoid redundant code and improve the performance of our application.

### What does the prototype pattern look like?

The prototype design pattern usually consists of the following three parts:

*   Prototype interface: This is usually an interface or an abstract class that declares the methods for cloning itself. Usually the clone method is used for cloning the prototype
*   Concrete prototype: This is the concrete implementation of the prototype interface
*   Client: This is the class that uses the prototype to create a new object

The set process that is being followed in the prototype design pattern is that, firstly, the client retrieves the prototype object. Then the client calls the prototype object’s clone method to create the new object. The clone method creates a new object and initializes its state by copying the state of prototype object. Then, the new object is returned to the client.

Let’s understand this with an example:

// Define a prototype object
const prototype \= {
  greeting: 'Hello',
  sayHello: function() {
    console.log(this.greeting + ' World!');
  },
  clone: function() {
    return Object.create(this);
  }
};
// Create a new object by cloning the prototype
const newObj \= prototype.clone();
// Modify the new object's properties
newObj.greeting \= 'Hola';
// Call the sayHello method of the new object
newObj.sayHello(); // Output: Hola World!

In this example, there is a prototype object that has a greeting property and a `sayHello` method. We have also implemented the clone method to create a new object by using `Object.create` to copy the prototype object.

Then, we are creating a new object by cloning the prototype and modifying its greeting property to “Hola”. In the end, we are calling the `sayHello` method of the new object, which outputs `Hola World!` to the console.

Although it is a simple example, it illustrates the basic concepts of prototype design pattern.

### Use cases

There are multiple use cases in which prototype design pattern can be used:

*   **Creating new objects with similar properties**: If developers need to create new objects that share similar properties, opting for prototype design pattern is the best decision
*   **Optimizing object creation**: If creating new object in the application is a costly decision, opting for prototype pattern to reduce the overhead is the best decision.
*   **Caching**: If the developer needs to cache data in the application, he can opt for the Prototype pattern to create a cache of objects that are initialized with default values. When a new object is needed, developers can clone one of the objects in the cache and modify its properties as needed

To better understand this, here is an example of how the prototype design pattern can be used to cache data in a Node.js application:

// Define a prototype object for caching data
const cachePrototype \= {
  data: {},
  getData: function(key) {
    return this.data\[key\];
  },
  setData: function(key, value) {
    this.data\[key\] \= value;
  },
  clone: function() {
    const cache \= Object.create(this);
    cache.data \= Object.create(this.data);
    return cache;
  }
};
// Create a cache object by cloning the prototype
const cache \= cachePrototype.clone();
// Populate the cache with some data
cache.setData('key1', 'value1');
cache.setData('key2', 'value2');
cache.setData('key3', 'value3');
// Clone the cache to create a new cache with the same data
const newCache \= cache.clone();
// Retrieve data from the new cache
console.log(newCache.getData('key1')); // Output: value1
// Modify data in the new cache
newCache.setData('key2', 'new value');
// Retrieve modified data from the new cache
console.log(newCache.getData('key2')); // Output: new value
// Retrieve original data from the original cache
console.log(cache.getData('key2')); // Output: value2

In the example above, we have defined a prototype object for caching data with two methods: `getData` and `setData`. We have also defined a clone method to create a new object by copying the prototype and its data.

We are creating a cache object by cloning the prototype and then populating it with some data by using the `setData` method. After that, we are cloning the cache to create a new cache object with the same data.

Then we are retrieving the data from the new cache using the `getData` method and modifying its data using the `setData` method. We are then retrieving the modified data from the new cache and the original data from the original cache to verify that they are different.

## The observer pattern

The observer pattern allows you to respond to a certain input by being reactive to it instead of proactively checking if the input is provided. In other words, with this pattern, you can specify what kind of input you’re waiting for and passively wait until that input is provided in order to execute your code. It’s a set and forget kind of deal.

Here, the observers are your objects and they know the type of input they want to receive and the action to respond with. These are meant to observe another object and wait for it to communicate with them.

The observable, on the other hand, will let the observers know when a new input is available, so they can react to it, if applicable. If this sounds familiar, it’s because it is — anything that deals with events in Node is implementing this pattern.

### What does the observer pattern look like?

Have you ever written your own HTTP server? Something like this:

const http \= require('http');

const server \= http.createServer((req, res) \=> {
  res.statusCode \= 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Your own server here');
});

server.on('error', err \=> {
    console.log(“Error:: “, err)
})

server.listen(3000, '127.0.0.1', () \=> {
  console.log('Server up and running');
});

There, hidden in the code above, you’re looking at the observer pattern in the wild. An implementation of it, at least.

Your server object would act as the observable, while your callback function is the actual observer. The event-like interface here (see the bolded code), with the `on` method, and the event name there might obfuscate the view a bit, but consider the following implementation:

class Observable {

    constructor() {
            this.observers \= {}
    }

    on(input, observer) {
            if(!this.observers\[input\]) this.observers\[input\] \= \[\]
            this.observers\[input\].push(observer)
    }

    triggerInput(input, params) {
            this.observers\[input\].forEach( o \=> {
                    o.apply(null, params)    
            })
    }
}

class Server extends Observable {

    constructor() {
            super()
    }

    triggerError() {
            let errorObj \= {
                    errorCode: 500,
                    message: 'Port already in use'
            }
            this.triggerInput('error', \[errorObj\])
    }
}

You can now, again, set the same observer, in exactly the same way:

server.on('error', err \=> {
    console.log(“Error:: “, err)
})

And if you were to call the `triggerError` method (which is there to show you how you would let your observers know that there is new input for them), you’d get the exact same output:

Error:: { errorCode: 500, message: 'Port already in use' }

> If you were to be considering using this pattern in Node.js, please look at the [EventEmitter](https://nodejs.org/api/events.html) object first, as it is Node.js’ own implementation of this pattern, and might save you some time.

### Use cases

This pattern is, as you might have already guessed, great for dealing with asynchronous calls, as getting the response from an external request can be considered a new input.

And what do we have in Node.js, if not a constant influx of asynchronous code into our projects? So next time you’re having to deal with an async scenario, consider looking into the observer pattern.

Another widely spread use case for this pattern, as you’ve seen, is that of triggering particular events. This pattern can be found on any module that is prone to having events triggered asynchronously (such as errors or status updates). Some examples are the [HTTP module](https://nodejs.org/api/http.html), any database driver, and even [Socket.IO,](https://socket.io/) which allows you to set observers on particular events triggered from outside your own code.

## Dependency injection

In the context of Node.js, dependency injection is a design pattern that is used to decouple application components and make them more testable and maintainable.

The basic idea behind dependency injection is to remove the responsibility of creation and management of an object’s dependencies (i.e., the other objects it depends on to function) from the object itself and delegate this responsibility to an external component. Rather than creating dependencies inside an object, the object receives them from an external source at runtime.

By using dependency injection, we can:

*   Avoid hardcoding dependencies inside an object, which makes it difficult to modify or replace them
*   Simplify the testing process by injecting mock dependencies during the testing phase
*   Promote code reusability and modularity by separating concerns

In Node.js, there are various techniques to implement dependency injection, such as constructor injection, setter injection, or interface injection, among others.

### What does the dependency injection look like?

To get an idea of what dependency looks like let’s take an example:

class UserService {
  constructor(userRepository) {
    this.userRepository \= userRepository;
  }
  async getUsers() {
    const users \= await this.userRepository.getUsers();
    return users;
  }
  async addUser(user) {
    await this.userRepository.addUser(user);
  }
}
class UserRepository {
  async getUsers() {
    // get users from database
  }
  async addUser(user) {
    // add user to database
  }
}
// Creating instances of the classes
const userRepository \= new UserRepository();
const userService \= new UserService(userRepository);
// Using the userService object to get and add users
userService.getUsers();
userService.addUser({ name: 'John', age: 25 });

In this example, we have two classes: `UserService` and `UserRepository`. The `UserService` class depends on the `UserRepository` class to perform operations. Instead of creating an instance of `UserRepository` inside `UserService`, we are injecting it via the constructor.

We can easily switch out the implementation of `UserRepository` with a different one (e.g., a mock repository for testing), without having to modify the `UserService` class itself.

The example above is showing how DI can be used to separate the creation and management of an object’s dependencies.

### Use cases

Dependency injection has many different uses:

*   **Testing**: One of the main benefits of DI is that it makes it easier to test code. By injecting dependencies into classes, it becomes easier to replace them with mock during testing, which allows us to isolate the code under test
*   **Modularization**: DI can also help to make code more modular by minimizing the coupling between different components of code
*   **Scalability**: DI can also help to make applications more scalable. It does this by making it easier to manage dependencies between different components

Let’s take an example of how DI can be more beneficial during testing.

Suppose we have a class called `Calculator` that performs mathematical calculations. `Calculator` has a dependency on a `Logger` class that is used to log information about the calculations. Here is what `Calculator` might look like:

Let’s say we have an `EmailSender` class that sends emails to users, and it depends on an `EmailService` class to actually send the email. We want to test `EmailSender` without actually sending emails to real users, so we can create a mock `EmailService` class that logs the email content instead of sending the email:

// emailSender.js
class EmailSender {
  constructor(emailService) {
    this.emailService \= emailService;
  }

  async sendEmail(userEmail, emailContent) {
    const success \= await this.emailService.sendEmail(userEmail, emailContent);
    return success;
  }
}

// emailService.js
class EmailService {
  async sendEmail(userEmail, emailContent) {
    // actually send the email to the user
    // return true if successful, false if failed
  }
}

// emailSender.test.js
const assert \= require('assert');
const EmailSender \= require('./emailSender');
const EmailService \= require('./emailService');

describe('EmailSender', () \=> {
  it('should send email to user', async () \=> {
    // Create a mock EmailService that logs email content instead of sending the email
    const mockEmailService \= {
      sendEmail: (userEmail, emailContent) \=> {
        console.log(\`Email to ${userEmail}: ${emailContent}\`);
        return true;
      }
    };

    const emailSender \= new EmailSender(mockEmailService);

    const userEmail \= 'example@example.com';
    const emailContent \= 'Hello, this is a test email!';
    const success \= await emailSender.sendEmail(userEmail, emailContent);

    assert.strictEqual(success, true);
  });
});

In this example, we created a mock `EmailService` object that logs the email content instead of actually sending the email. We then passed this mock object into the `EmailSender` class constructor during testing. This allows us to test the `EmailSender` class logic without actually sending emails to real users.

## The chain of responsibility pattern

The chain of responsibility pattern is one that many Node.js developers have used without even realizing it.

It consists of structuring your code in a way that allows you to decouple the sender of a request with the object that can fulfill it. In other words, if object A sends request R, you might have three different receiving objects R1, R2, and R3. How can A know which one it should send R to? Should A care about that?

The answer to the last question is: no, it shouldn’t. Instead, if A shouldn’t care about who’s going to take care of the request, why don’t we let R1, R2, and R3 decide by themselves?

Here is where the chain of responsibility comes into play; we’re creating a chain of receiving objects, which will try to fulfill the request and if they can’t, they’ll just pass it along. Does it sound familiar yet?

### What does the chain of responsibility look like?

Here is a very basic implementation of this pattern. As you can see at the bottom, we have four possible values (or requests) that we need to process, but we don’t care who gets to process them — we just need at least one function to use them. So, we just send it to the chain and let each one decide whether they should use it or ignore it:

function processRequest(r, chain) {

    let lastResult \= null
    let i \= 0
    do {
            lastResult \= chain\\\[i\\\](r)
            i++
    } while(lastResult != null && i < chain.length)
    if(lastResult != null) {
            console.log("Error: request could not be fulfilled")
    }
}

let chain \= \[
    function (r) {
            if(typeof r \== 'number') {
                    console.log("It's a number: ", r)
                    return null
            }
            return r
    },
    function (r) {
            if(typeof r \== 'string') {
                    console.log("It's a string: ", r)
                    return null
            }
            return r
    },
    function (r) {
            if(Array.isArray(r)) {
                    console.log("It's an array of length: ", r.length)
                    return null
            }
            return r
    }
\]

processRequest(1, chain)
processRequest(\[1,2,3\], chain)
processRequest('\[1,2,3\]', chain)
processRequest({}, chain)

The output will be:

It's a number:  1
It's an array of length:  3
It's a string:  \[1,2,3\]
Error: request could not be fulfilled

### Use cases

The most obvious case of this pattern in our ecosystem is the [middlewares for ExpressJS](http://expressjs.com/en/guide/using-middleware.html). With that pattern, you’re essentially setting up a chain of functions (middlewares) that evaluate the request object and decide whether to act on it or ignore it. You can think of the pattern as the asynchronous version of the exampleabove. Let’s see this in more detail.

### Middleware

In Node.js, middleware is the design pattern that allows a developer to add functionalities in the request/response processing pipelines of the application. In its essence, it is a layer that sits between the browser (client) and Node.js-based application(server). It intercepts incoming requests and outgoing responses.

The middleware functions take in three arguments: request, response, and next. The request is the HTTP request object, the response is the HTTP response object, and the next is the function used to call the next middleware function; by doing so, it helps in the implementation of the chain of responsibility).

Middleware design patterns can be used for the implementation of a variety of functions such as authentication, logging, and error handling. It is a powerful tool for building modular, scalable, and maintainable Node.js applications.

One of the simple examples to understand middleware functions is:

// Middleware function to log incoming requests
app.use((req, res, next) \=> {
  console.log(\`Incoming request: ${req.method} ${req.url}\`);
  next();
});
// Route handler for the home page
app.get('/', (req, res) \=> {
  res.send('Hello World!');
});
// Start the server
app.listen(3000, () \=> {
  console.log('Server listening on port 3000');
});

Here we are using the middleware function to log the HTTP method and URL of each incoming request to the control before calling the next middleware function in the chain. And you can see, `next()` is being used here to pass the control to the next middleware function in line.

From the example above, it becomes obvious that middlewares are a particular implementation of a chain of responsibility pattern because instead of only one member of the chain fulfilling the request, one could argue that all of them could do it. Nevertheless, the rationale behind it is the same.

Managing large chunks of data in an efficient manner is necessary. There are multiple ways to achieve it. One of the ways in which we can achieve this is by implementing a pipeline of processing stages. Each stage can perform specific operation on the data and then pass it on the next stage. Although this will be done by using streams, this method of setting up data processing stages can be seen as a form of chain of responsibility.

## Streams

Streams in Node.js are a way to efficiently handle large amounts of data by breaking the data down into smaller chunks and processing it one chunk at a time. Streams aren’t inherently designed to process the data by building pipelines of streams so that all the data can be handled by using a stage-by-stage approach but sometimes developers have to do this and when they implement it in this way, they are using the chain of responsibility approach.

In this pipeline model, each stream in the pipeline is responsible for performing a specific operation on data and then pass data to the next stream.

Let’s understand it in this way. Suppose we have a chunk of data in a file and we have to read the data, modify it and the write it in a new file. All of these operations can be achieved by setting stages of processing where at the “read stream”, we read data from the file, at the “transform stream”, we modify the data and at the “write stream”, we write the data to a new file.

Let’s see an example to understand this concept in a better way:

 const { Readable, Transform, Writable } \= require('stream');

// Define a Readable stream that emits an array of numbers
class NumberGenerator extends Readable {
  constructor(options) {
    super(options);
    this.numbers \= \[1, 2, 3, 4, 5\];
  }

  \_read(size) {
    const number \= this.numbers.shift();
    if (!number) return this.push(null);
    this.push(number.toString());
  }
}

// Define a Transform stream that doubles the input number
class Doubler extends Transform {
  \_transform(chunk, encoding, callback) {
    const number \= parseInt(chunk, 10);
    const doubledNumber \= number \* 2;
    this.push(doubledNumber.toString());
    callback();
  }
}

// Define a Writable stream that logs the output
class Logger extends Writable {
  \_write(chunk, encoding, callback) {
    console.log(\`Output: ${chunk}\`);
    callback();
  }
}

// Create instances of the streams
const numberGenerator \= new NumberGenerator();
const doubler \= new Doubler();
const logger \= new Logger();

// Chain the streams together
numberGenerator.pipe(doubler).pipe(logger);

In the code segment above, we are creating three streams (`Readable`, `Transform`, and `Writable`) and then chaining them together by using the `.pipe()` method. Code is behaving in a way where the `Read` stream is emitting an array of numbers, which are then doubled by the `Transform` stream and then the `Writable` stream is logging it to the console. This code is showing how a developer can implement chain of responsibility using streams.

Although streams in Node.js don’t directly implement chain of responsibility, they do provide a similar mechanism for chaining together processing stages.

## Conclusion

The main purpose of implementing a design pattern is to improve the quality of the code and provide a proven reusable solution to a commonly occurring problem in software engineering design. Design patterns are standard a way to document and discuss the solutions to design level problems.

If used correctly, design patterns are a proven way to improve software quality and maintainability by promoting modular and extensible software design. They also provide a common structure and vocabulary for developers to follow and thus reducing the likelihood of errors and inconsistencies.

Design patterns are also a great tool to save time as they improve the efficiency of software development process by providing a well-defined solution that can be adapted and used in different contexts and thus eliminating the need to reinvent the wheel every time.

Sometimes, for an early career engineer, understanding the way in which design patterns can efficiently solve a problem or using the design patterns in their solutions can be overwhelming. This is particularly true when working with Node.js, where the ecosystem is vast and many things are happening on a daily basis.

We have a full article for the Node.js based ecosystem that tackles this issue and provides a detailed understanding of every major design pattern so that engineers can implement them in their solutions. [Che](https://blog.logrocket.com/understanding-design-patterns-typescript-node-js/)[c](https://blog.logrocket.com/understanding-design-patterns-typescript-node-js/)[k it out her](https://blog.logrocket.com/understanding-design-patterns-typescript-node-js/)[e](https://blog.logrocket.com/understanding-design-patterns-typescript-node-js/).
