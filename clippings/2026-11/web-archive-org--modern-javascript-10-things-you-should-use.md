---
url: "https://web.archive.org/web/20191210040946id_/https://dev.to/itnext/modern-javascript-10-things-you-should-be-using-starting-today-22dp"
captured_at: "2026-11-17T19:41:29+00:00"
title: "Modern JavaScript, 10 things you should be using, starting today"
domain: "web-archive-org"
---

Follow me on [Twitter](https://twitter.com/chris_noring), happy to take your suggestions on topics or improvements /Chris

> You may be completely new to JavaScript or you may have only used it sporadically over the years. One thing is clear though - a lot has changed and there are some features YOU should be using. This article describes the features I think you should be using on a daily basis, if you are serious about JavaScript

Here is the video version:

## [](#resources)Resources

These are my favorite resources for anything ES6+:

*   [ES6 Features](http://es6-features.org/)
*   [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)

## [](#1-spread-operator)\-1- Spread operator

This is denoted as a `...` before an object or an array and accomplishes just what the name is saying, it's turning something from being a structure into a comma-separated list. Let's demonstrate this:

**Spread array**  

```
let firstHalf = [ 'one', 'two'];
let secondHalf = ['three', 'four', ...firstHalf];
```

This is such a nice and compact way of writing it. Doing the same without this would mean doing something like this:

**NO Array spread**  

```
let firstHalf = [ 'one', 'two'];


let secondHalf = ['three', 'four'];
for(var i=0, i <firstHalf.length; i++ ) {
  secondHalf.push(firstHalf[i]);
}


```

This can also be used on objects as a way of _merging_ their properties:

**Spread object**  

```
const hero = {
  name: 'Xena - Warrior Princess',
  realName: 'Lucy Lawless'
}


const heroWithSword = {
 ...hero,
 weapon: 'sword'
}

```

Doing this the hard way would be us looping through all the properties on the object:

**NO Object spread**  

```
let keys = Object.keys(hero);
let obj = {};

for(var i=0; i< keys.length; i++) {
   obj[keys[i]] = keys[props[i]];
}
```

## [](#2-rest-parameter)\-2- Rest parameter

Rest parameters are about _collecting_ the remaining parameters into an array. JavaScript has the ability to be flexible on the number of input parameters you give it. Normally there is an `arguments` variable that collects these. Let's look at what we mean:  

```
function add(first, second, ...remaining) {
  return first + second;
}
```

Now, this above only summarize the parameters `first` and `second`. Which means invoking it with `add(1,2)` or `add(1,2,3, 4)` would yield the same results. To fix this we would type:  

```
function add(first, second, ...remaining) {
  return first + second + remaining.reduce((acc, curr) => acc + curr, 0);
}
```

The above means we are fixing the problem and use all input parameters.

As stated earlier using the rest parameter, i.e adding a preceding `...` as a way to collect the remaining parameters, is a way for us to name them and make it more explicit that we want to work with them. `arguments` have been around since at least ES5 but is less known I think.

## [](#3-string-interpolation)\-3- String interpolation

Have you ever seen a statement like this?  

```
class Product {
 constructor(name, description, price) {
   this.name = name;
   this.description = description;
   this.price = price;
 }

 getDescription() {
   return " Full description \n" + 
   " name: " + this.name + 
   " description: " + this.description

 }
}
```

I'm of course talking about the `getDescription()` method, a long, multiline, hard-to-read statement. This is a reality in most programming languages. There is also string interpolation available in some languages and JavaScript is no different, fortunately. We can turn our `getDescription()` method into the following:  

```
getDescription() {
   return `Full description \n: 
   name: ${this.name}
   description ${this.description}
   `;

 }
```

So double backticks `` ` `` is what we use to define a multi-line string. We also use `${}` to interpolate. There your world is hopefully a lot better now :)

## [](#4-shorthand-properties)\-4- Shorthand properties

You might be using this one without already knowing about it. In ES5 you had to write the following:  

```
function createCoord(x, y) {
  return {
    x: x,
    y: y
  }
}
```

In ES6 and onwards you can omit the what's to the right of `:` if it has the same name, like so:  

```
function createCoord(x, y) {
  return {
    x,
    y
  }
}
```

Looks less cluttered right?

## [](#5-method-properties)\-5- Method properties

This is how you define properties that point to methods in an object. Consider the following ES5 example:  

```
const math = {
  add: function(a,b) { return a + b; },
  sub: function(a,b) { return a - b; }, 
  multiply: function(a,b) { return a * b; }
}
```

You don't actually need to have the whole `add:` business from ES6 and forwards. You can just type it like so:  

```
const math = {
  add(a,b) { return a + b; },
  sub(a,b) { return a - b; },
  multiply(a,b) { return a * b; }
}
```

## [](#6-destructuring)\-6- Destructuring

Destructuring is about your own mental sanity as a developer.

**Object destructuring**

Consider the following code:  

```
function handle(req, res) {
 const name = req.body.name;
 const description = req.body.description;
 const url = req.url;

 log('url endpoint', url);

 // lots of logic happening
 dbService.createPerson( name, description )
}
```

The code above is not perfect, in any way, but it does represent a case where we want to dig out data from an object at different levels. What's the problem you ask? Well, what if I didn't have to declare all those variables and save a few keystrokes? You can do just that:  

```
function handle(req, res) {
 const { body: { name, description }, url }, = req;

 log('url endpoint', url);

 // lots of logic happening
 dbService.createPerson( name, description )
```

Above you see how three rows become one.

**Array destructuring**

This is not limited to objects. It can be done on arrays as well. Consider the following code:  

```
const array = [1,2,3,4,5,6];

const a = array[0];

const c = array[2];
```

This can be done in a much more elegant way, like so:  

```
const array = [1,2,3,4,5,6];
const [a, ,c, ...remaining] = arr;

// remaining = [4,5,6]
```

We can just break out the values from the array by the above pattern matching. If we want to skip something we type `, ,` and as a bonus, I threw in a REST statement to grab the remaining items.

**Parameter matching**

We can also do this on a function and its parameters. It has become the de-facto standard to collect all parameters in an object when you have more than 2-3 parameters in a function so you get a function looking like this:  

```
function doSomething(config) {
  if(config.a) { ... }
  if(config.b) { ... }
  if(config.c) { ... }
}
```

The better way to do this is:  

```
function doSomething({ a, b, c }) {
  if(a) { ... }
  if(b) { ... }
  if(c) { ... }
}
```

## [](#7-array-methods)\-7- Array methods

ES6 brought a whole slew of usable array methods like:

*   `find()`, finds an item in list else null
*   `findIndex()`, find the index of the item
*   `some()`, is the predicate true for at least one item in the list
*   `includes()`, is an item part of a list

Consider the following code to understand the usage:  

```
const array = [{ id: 1, checked: true }, { id: 2 }];
arr.find(item => item.id === 2) // { id: 2 }
arr.findIndex(item => item.id === 2) // 1
arr.some(item => item.checked) // true

const numberArray = [1,2,3,4];
numberArray.includes(2) // true
```

## [](#8-promises-asyncawait)\-8- Promises + Async/Await

If you have been around the block a while you might remember a time when callbacks were all we had, like this:  

```
function doSomething(cb) {
  setTimeout(() =>  {
    cb('done')
  }, 3000)
}

doSomething((arg) => {
 console.log('done here', arg);
})
```

We used this to handle the fact that some operations were asynchronous and simply took time to finish. Then we got promise libraries that people started using and eventually, we got native support in the language. So now we can do things like:  

```
function doSomething() {
  return new Promise((resolve, reject) => {
    setTimeout(() =>  {
      resolve('done')
    }, 3000)
  })
}

doSomething().then(arg => {
 console.log('done here', arg);
})
```

We can even chain the whole experience so we can do calls like this:  

```
getUser()
  .then(getOrderByUser)
  .then(getOrderItemsByOrder)
  .then(orderItems => {
    // do something with order items
  })

```

**Async/await**

Then we got async/await and life became even more glorious. Consider the above example with Promises now becoming this:  

```
async function getItems() {
  try {
    const user = await getUser();
    const order = await getOrderByUser(user);
    const items = await getOrderItemsByOrder(order);
    return items;
  } catch(err) {
    // handle error here, the suggestion to return something or rethrow
  }
}

getItems().then(items => {
  // do something with order items
})
```

We get a synchronous-looking asynchronous code. :)

## [](#%C2%A09-modules) -9- Modules

Pretty much any coding language supports the concept of modules. The ability to divide up your code in many different files, files that are also self-contained units, so-called modules. Consider the following code:  

```
// math.js

export function add(a,b) { return a + b; }
export function sub(a,b) { return a - b; }

export default (a,b) => a * b;

// main.js
import mult, { add, sub } from './math';

mult(2, 4) // 8
add(1,1)   // 2
sub(1,2)   // -1

```

Above we are using the `export` keyword to signal that these constructs `add` and `sub` is publically available for any module importing this module. The `export default` keyword is what we get if we just import it. In `main.js` we import the default as having name `mult` and we also specifically pick out methods `add()` and `sub()`

## [](#10-arrow-functions-lexical-raw-this-endraw-)\-10- Arrow functions + Lexical `this`

I've been using Arrow functions throughout this article and it's simply another function notation. In the past we could only write functions like this:  

```
function printArray(arr) {
 // do something
}
```

Now we can define that as:  

```
const printArray = (arr) => {
 // do something
}
```

**One line functions**

We can also define functions as one-liners:  

```
const add = (a,b) => a + b
```

This automatically means we do the operation and return the result. We can do the same and return an object, our syntax then becomes:  

```
const create = (a,b) = > ({ x: a, y: b })
```

**Lexical this**  
The problem we used to face was no knowing what `this` is. Consider the following problem:  

```
let array = [1,2,3];

function sum() {
  this.total = 0;

  arr.forEach(function(item) {
    this.total+= item;  // `this` is the inner functions `this`, BAD
  })
  return total;
} 
```

`this` in the above case points wrong inside of the `forEach`. The way we used to solve this was by doing:  

```
function sum() {
  this.total = 0;
  var self = this;

  arr.forEach(function(item) {
    self.total+= item;  // now we are using `self`, it solves it but feels hacky
  })
  return total;
} 
```

Arrow functions fix this, no more `self`, so now the code looks like this:  

```
function sum() {
  this.total = 0;

  arr.forEach((item) => {
    this.total+= item;  // all is well `this` points to outer function
  })
  return total;
} 
```

WINNING!

## [](#summary)Summary

There are more things I could mention about ES6 and forward but I just wanted to show you my favorites that I think you should adopt today :)
