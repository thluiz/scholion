---
url: "https://web.archive.org/web/20191224110410id_/https://dev.to/aminnairi/automate-your-getters-and-setters-with-proxies-5bgp"
captured_at: "2026-11-16T07:48:30+00:00"
title: "Automate your getters and setters with Proxies"
domain: "web-archive-org"
---

_Cover image credits go to nearsay.com._

Let's say you have a class that represents a motorcycle. It has one property. A brand. But you don't want to write by hand the getters for that class. You could use a [Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) to do the job.  

```
"use strict";

class Motorcycle {
    constructor(constructionYear) {
        this.constructionYear = constructionYear;
    }
}

const withGetters = {
    get(object, property) {
        // "getConstructionYear"
        if (property.startsWith("get")) {
            // "ConstructionYear"
            const getter = property.slice(3);

            // "c"
            const firstLetter = getter[0].toLowerCase();

            // "onstructionYear"
            const rest = getter.slice(1);

            // "constructionYear"
            const fullProperty = firstLetter + rest;

            // motorcycle.getConstructionYear()
            return () => object[fullProperty];
        }

        // motorcycle.constructionYear
        return object[property];
    }
};

const motorcycle = new Proxy(new Motorcycle(2020), withGetters);

console.log(motorcycle.constructionYear);       // 2020
console.log(motorcycle.getConstructionYear());  // 2020
```

## [](#we-want-to-access-a-property)We want to access a property

Let's explain the code step by step.

First we have our class. We defined a constructor method in which we choose to receive one property. We then attach the property. Plain and simple.

Next, we have our [Proxy handler](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler). It will receive all properties and methods accessed, just like a Web Proxy receiving the request before processing it (like [Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)). If we try to access a method that starts with `get`, it means we want to access a property using its getter. But we do not have one. So we try to convert this method name into its property name. Once we know what property the user is trying to access, we can fake the method call by returning a function that will just return the property from that object.

And if the property does not start with a `get`, it means that our job is done and we just return the accessed property.

Now we just have to instanciate our class by wrapping it up with a proxy. Next time we try to access a property, we can use both the getter and the property syntax. This also means that it will be automated for all properties that we decide to attach to our instance.  

```
"use strict";

class Motorcycle {
    constructor(brand, model, constructionYear) {
        this.brand = brand;
        this.model = model;
        this.constructionYear = constructionYear;
    }
}

const withGetters = {
    get(object, property) {
        // "getConstructionYear"
        if (property.startsWith("get")) {
            // "ConstructionYear"
            const getter = property.slice(3);

            // "c"
            const firstLetter = getter[0].toLowerCase();

            // "onstructionYear"
            const rest = getter.slice(1);

            // "constructionYear"
            const fullProperty = firstLetter + rest;

            // motorcycle.getConstructionYear()
            return () => object[fullProperty];
        }

        // motorcycle.constructionYear
        return object[property];
    }
};

const motorcycle = new Proxy(new Motorcycle("Triumph", "Street Triple", 2020), withGetters);

console.log(motorcycle.brand);              // "Triumph"
console.log(motorcycle.model);              // "Street Triple"
console.log(motorcycle.constructionYear);   // 2020

console.log(motorcycle.getBrand());              // "Triumph"
console.log(motorcycle.getModel());              // "Street Triple"
console.log(motorcycle.getConstructionYear());   // 2020
```

## [](#getters-amp-setters)Getters & setters

Of course we could do the same for setters as well.  

```
"use strict";

class Motorcycle {
    constructor(brand, model, constructionYear) {
        this.brand = brand;
        this.model = model;
        this.constructionYear = constructionYear;
    }
}

function getPropertyFromGetterSetter(property) {
    const sliced = property.slice(3);
    const firstLetter = sliced[0].toLowerCase();
    const rest = sliced.slice(1);

    return firstLetter + rest;
}

const withGettersSetters = {
    get(object, property) {
        // "getConstructionYear"
        if (property.startsWith("get")) {
            // motorcycle.getConstructionYear()
            return () => object[getPropertyFromGetterSetter(property)];
        }

        if (property.startsWith("set")) {
            // motorcycle.setConstructionYear(2021)
            return (newValue) => {
                object[getPropertyFromGetterSetter(property)] = newValue;
            };
        }

        // motorcycle.constructionYear
        return object[property];
    }
};

const motorcycle = new Proxy(
    new Motorcycle("Triumph", "Street Triple", 2020),
    withGettersSetters
);

console.log(motorcycle.getConstructionYear()); // 2020

motorcycle.setConstructionYear(2021);

console.log(motorcycle.getConstructionYear()); // 2021
```

You could even use the proxyfication inside your class in the constructor to ease the syntax.  

```
"use strict";

function getPropertyFromGetterSetter(property) {
    const sliced = property.slice(3);
    const firstLetter = sliced[0].toLowerCase();
    const rest = sliced.slice(1);

    return firstLetter + rest;
}

const withGettersSetters = {
    get(object, property) {
        // "getConstructionYear"
        if (property.startsWith("get")) {
            // motorcycle.getConstructionYear()
            return () => object[getPropertyFromGetterSetter(property)];
        }

        if (property.startsWith("set")) {
            // motorcycle.setConstructionYear(2021)
            return (newValue) => {
                object[getPropertyFromGetterSetter(property)] = newValue;
            };
        }

        // motorcycle.constructionYear
        return object[property];
    }
};

class Motorcycle {
    constructor(brand, model, constructionYear) {
        this.brand = brand;
        this.model = model;
        this.constructionYear = constructionYear;

        return new Proxy(this, withGettersSetters);
    }
}

const motorcycle = new Motorcycle("Triumph", "Street Triple", 2020);

console.log(motorcycle.getConstructionYear()); // 2020

motorcycle.setConstructionYear(2021);

console.log(motorcycle.getConstructionYear()); // 2021
```

And you could even go further (if you do not extend from any other classes) by creating a class for an easier integration with child classes.  

```
"use strict";

function getPropertyFromGetterSetter(property) {
    const sliced = property.slice(3);
    const firstLetter = sliced[0].toLowerCase();
    const rest = sliced.slice(1);

    return firstLetter + rest;
}

const withGettersSetters = {
    get(object, property) {
        // "getConstructionYear"
        if (property.startsWith("get")) {
            // motorcycle.getConstructionYear()
            return () => object[getPropertyFromGetterSetter(property)];
        }

        if (property.startsWith("set")) {
            // motorcycle.setConstructionYear(2021)
            return (newValue) => {
                object[getPropertyFromGetterSetter(property)] = newValue;
            };
        }

        // motorcycle.constructionYear
        return object[property];
    }
};

class GettersSetters {
    constructor() {
        return new Proxy(this, withGettersSetters);
    }
}

class Motorcycle extends GettersSetters {
    constructor(brand, model, constructionYear) {
        super();

        this.brand = brand;
        this.model = model;
        this.constructionYear = constructionYear;
    }
}

const motorcycle = new Motorcycle("Triumph", "Street Triple", 2020);

console.log(motorcycle.getConstructionYear()); // 2020

motorcycle.setConstructionYear(2021);

console.log(motorcycle.getConstructionYear()); // 2021
```

## [](#advantages)Advantages

A huge advantage to using Proxy to automate your getters & setters is that it is now easier to write trivial classes that do not have much logic in the setters & getters.

Also, people that have no [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment)s like me (I code using [VIM](https://en.wikipedia.org/wiki/Vim_\(text_editor\)) on my terminal) and that do not have access to getters/setters generator can now enjoy writing classes with getters and setters as quickly as you would in an IDE.

And another great advantage is that you don't have to think about removing you getters/setters for unused properties that you will want to remove since it is computed by the proxy at runtime.

There are also drawbacks from using this technique but I'll let you experiment and go as far as you can to see it in action and make yourself an idea of what Proxies can bring to your project.

## [](#to-sum-up)To sum up

There are, in my opinion, unlimited possibilities for using Proxies in your project. This getter/setter example was just a pretext to show you how awesome Proxies are in JavaScript. But you could go so much further and do something similar to what Symfony does with their annotations by creating a Proxy that will be responsible to turn a class into an entity connected to your API. This is left as an exercise for the reader and you could begin by creating a Proxy that will communicate with an API like [JSONPlaceholder](http://jsonplaceholder.typicode.com/), maybe a class called `Fetchable` to make it sounds and look cool!

So that's it for today. I hope you see now that Proxies are really powerful. Let me know if you have some other useful usage for Proxies and let's discuss about that in the comment section below. Thanks for reading me!
