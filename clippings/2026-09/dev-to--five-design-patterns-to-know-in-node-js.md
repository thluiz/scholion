---
url: "https://dev.to/jacobandrewsky/five-design-patterns-to-know-in-nodejs-265h?context=digest"
captured_at: "2026-09-25T00:13:14+01:00"
title: "Five Design Patterns to know in Node.js"
domain: "dev-to"
---

Hey there!

I recently went through multiple knowledge resources to learn more about popular design and architectural patterns in Node.js. My aim was mainly at the server (backend) side but as I was going through them, I was seeing a lot of similarities to the browser (frontend) frameworks. Some of them are even directly used in the frameworks for which I am even more happy because I was using them already without knowing it 😉

There are many (really many) design patterns that you could use, so in this article, I decided to choose 5 of them and explain them in more detail.

Enjoy!

## [](#what-is-a-design-pattern)🟢 What is a Design Pattern?

Design patterns are proven and battle-tested solutions to solve problems that we as developers encounter every day. These patterns help promote best practices and implement a structured approach to solving everyday issues while designing and developing software architecture. Software engineers can develop maintainable, secure, and stable systems by using these patterns.

Node.js due to its flexibility does not force you to stick to certain patterns but instead gives you the freedom of choosing just the ones needed for your task. That is why in my opinion it is so widely used today (and by the way thanks to JavaScript :D).

## [](#five-popular-design-patterns-in-nodejs)✅ Five Popular Design Patterns in Node.js

Below, you will see a list of 5 selected design patterns that I like.

### [](#singleton)Singleton

This pattern is all about classes that can have only one instance and provide global access to it. Modules can be cached and shared across the application in Node.js which will help improve the efficiency of resources. A common example of such a singleton pattern is a module for connecting with certain third-party services like databases, cache services, email providers, etc that is used extensively in the Nest.js framework. Let's take a look at the following example:  

```
class Redis {
  constructor() {
    this.connection = null;
  }

  static getInstance() {
    if (!Redis.instance) {
      Redis.instance = new Redis(options);
    }

    return Redis.instance;
  }

  connect() {
    this.connection = 'Redis connected'
  }
}
```

Enter fullscreen mode Exit fullscreen mode

And then we can use it like the following:  

```
const redisOne = Redis.getInstance();
const redisTwo = Redis.getInstance();

console.log(redisOne === redisTwo); // it will result to `true`

redisOne.connect();

console.log(redisOne.connection) // 'Redis connected'
console.log(redisTwo.connection) // 'Redis connected'
```

Enter fullscreen mode Exit fullscreen mode

This approach ensures that there is only one connection to Redis and prevents duplicating connections.

### [](#factory)Factory

With this pattern, you can create new objects without specifying the class of object that will be created. Thanks to it we are abstracting object creation which can help improve code readability and reusability:  

```
class Character {
  constructor(type, health) {
    this.type = type;
    this.health = health;
  }
}

class CharacterFactory {
  createCharacter(name) {
    switch(name) {
      case 'mage': 
        return new Character('Powerful Mage', 8);
      case 'warrior':
        return new Character('Courageous Warrior', 10);
      case 'rogue':
        return new Character('Sneaky Rogue', 9)
      default:
        return new Error('Unknown character');
    }
  }
}
```

Enter fullscreen mode Exit fullscreen mode

And then we can use it like the following:  

```
const characterFactory = new CharacterFactory();

const mage = characterFactory.createCharacter('mage');
const warrior = characterFactory.createCharacter('warrior');

console.log(mage.type) // Powerful Mage
console.log(warrior.type) // Courageous Warrior
```

Enter fullscreen mode Exit fullscreen mode

This approach allows consumers of this factory to use the factory code instead of using the Character class constructor directly.

### [](#observer)Observer

This pattern works in a way that you will have an entity that manages the list of depending elements called observers and notifies them if the state changes. This pattern is used widely in the Vue.js framework and be implemented like this:  

```
class Topic {
  constructor() {
    this.observers = []; 
  }

  subscribe(observer) {
    this.observers.push(observer);
  }

  unsubscribe(observer) {
    this.observers = this.observers.filter(o => o !== observer);
  }

  notify(data) {
    this.observers.forEach(o => o.update(data));
  }
}

class Observer {
  constructor(name) {
    this.name = name;
  }

  update(data) {
    console.log(`${this.name} received ${data}`);
  }
}
```

Enter fullscreen mode Exit fullscreen mode

And you can use it like the following:  

```
const topic = new Topic();

const observer1 = new Observer('Observer 1');
const observer2 = new Observer('Observer 2');

topic.subscribe(observer1);
topic.subscribe(observer2);

topic.notify('Hello World');
// Observer 1 received Hello World 
// Observer 2 received Hello World

topic.unsubscribe(observer2);

topic.notify('Hello Again');
// Observer 1 received Hello Again
```

Enter fullscreen mode Exit fullscreen mode

It is a really useful pattern for event handling and asynchronous workflows that allows to update of multiple objects without coupling the publisher to the subscribers.

### [](#decorator)Decorator

This pattern is quite useful for extending the existing functionality with a new one without affecting the initial/original instances. It is used widely in the Nest.js framework thanks to the full support of TypeScript but in regular Node.js it can be used in following:  

```
class Character {
  constructor() {
    this.endurance = 10;
  }

  getEndurance() {
    return this.endurance;
  }
}

class CharacterActions {
  constructor(character) {
    this.character = character;
  }

  attack() {
    this.character.endurance -= 2;
  }

  rest() {
    this.character.endurance += 1; 
  }
}
```

Enter fullscreen mode Exit fullscreen mode

And then it can be used like the following:  

```
const character = new Character();

console.log(character.getEndurance()); // 10

const characterWithActions = new CharacterActions(character);

characterWithActions.attack(); // - 2
characterWithActions.rest(); // + 1

console.log(characterWithActions.character.getEndurance()); // 9
```

Enter fullscreen mode Exit fullscreen mode

By using this pattern we can easily extend already existing classes without affecting their core functionality.

### [](#dependency-injection)Dependency Injection

In this pattern, classes or modules receive dependencies from external sources rather than registering them internally. This approach allows extracting certain reusable elements from your system for easier testing and maintenance. It is used quite extensively in the Nest.js framework. It can be implemented like following:  

```
class UserService {
  constructor(databaseService, loggerService) {
    this.db = databaseService;
    this.logger = loggerService;
  }

  async getUser(userId) {
    const user = await this.db.findUserById(userId);
    this.logger.log(`Fetched user ${user.name}`);
    return user;
  }
}
```

Enter fullscreen mode Exit fullscreen mode

And then, you can use it like following:  

```
const databaseService = new Database();
const loggerService = new Logger();

const userService = new UserService(databaseService, loggerService);

userService.getUser(1);
```

Enter fullscreen mode Exit fullscreen mode

This approach allows you to extract elements of your system into intependent entities that can be injected when needed.

## [](#learn-more)📖 Learn more

If you would like to learn more about Vue, Nuxt, JavaScript or other useful technologies, check VueSchool by clicking this [link](https://vueschool.io/courses?friend=baroshem) or by clicking the image below:

[![Vue School Link](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fj7hlfz848ut2d9ly8i8q.png)](https://vueschool.io/courses?friend=baroshem)

It covers the most important concepts while building modern Vue or Nuxt applications that can help you in your daily work or side projects 😉

## [](#summary)✅ Summary

Well done! You have just learned how certain design patterns work in Node.js and how to implement them.

Take care and see you next time!

And happy coding as always 🖥️
