---
url: "https://ditdot.hr/en/causes-of-memory-leaks-in-javascript-and-how-to-avoid-them"
captured_at: "2026-11-16T03:53:13+00:00"
title: "Causes of Memory Leaks in JavaScript and How to Avoid Them"
domain: "ditdot-hr"
---

Insufficient care about memory management generally doesn't produce dramatic consequences when it comes to "old-fashioned" web pages. While the user navigates through links and loads new pages, page information is removed from memory with each load.

The rise of the SPA (Single Page Application) motivates us to pay more attention to memory-related JavaScript coding practices. If the application starts progressively using more and more memory, that can seriously affect the performance and even cause the browser's tab to crash.

In this article, we will explore programming patterns that cause memory leaks in JavaScript and explain how to improve memory management.

**Table of Contents:**

*   [What Is a Memory Leak?](#memory-leak-definition)
*   [Sources of Memory Leaks in JavaScript](#memory-leaks-sources)
    *   [Accidental Global Variables](#global-variables)
    *   [Closures](#closures)
    *   [Timers](#timers)
    *   [Event Listeners](#event-listeners)
    *   [Cache](#cache)
    *   [Detached DOM Elements](#detached-dom-elements)

## What Is a Memory Leak and How to Spot It?

The browser keeps objects in heap memory while they can be reached from the root through the reference chain. Garbage Collector is a background process in the JavaScript engine that identifies unreachable objects, removes them, and reclaims the underlying memory.

![Reference chain - garbage collector - objects](https://static.ditdot.hr/images/dev/010/reference-chain-garbage-collector.png)

An example of a reference chain from a Garbage Collector root to the objects

A memory leak occurs when an object in memory that is supposed to be cleaned in a garbage collection cycle stays reachable from the root through an unintentional reference by another object. Keeping redundant objects in memory results in excessive memory use inside the app and can lead to degraded and poor performance.

![Reference chain - memory leaks](https://static.ditdot.hr/images/dev/010/reference-chain-memory-leaks.png)

Object 4 is not reachable and will be removed from the memory. Object 3 is still reachable through the forgotten reference from Object 2 and will not be garbage collected.

How to figure out that our code is leaking memory? Well, memory leaks are sneaky and often difficult to notice and to localize. The leaking JavaScript code is not in any way considered invalid, and the browser will not throw any error while running it. If we notice that our page's performance is getting progressively worse, the browser's built-in tools can help us determine if a memory leak exists and what objects cause it.

The fastest way for a memory usage check is to take a look at the browser **Task Managers** (not to be confused with the operating system's Task Manager). They provide us with an overview of all tabs and processes currently running in the browser. Chrome's Task Manager can be accessed by pressing Shift+Esc on Linux and Windows, while the one built into Firefox by typing about:performance in the address bar. Among other things, they allow us to see the JavaScript memory footprint of each tab. If our site is just sitting there and doing nothing, but yet, the JavaScript memory usage is gradually increasing, there's a good chance we have a memory leak going on.

**Developer Tools** are providing more advanced memory management methods. By recording in Chrome's Performance tool, we can visually analyze the performance of a page as it's running. Some patterns are typical for memory leaks, like the pattern of increasing heap memory use shown below.

![Performance recording in Chrome](https://static.ditdot.hr/images/dev/010/performance-recording-in-chrome.png)

Performance recording in Chrome - the heap memory consumption is continuously growing (blue line)

Other than that, both Chrome and Firefox Developer Tools have excellent possibilities to further explore memory usage with the help of the Memory tool. Comparing consecutive heap snapshots shows us where and how much memory has been allocated between the two snapshots, along with additional details helping us to identify the troublesome objects in code.

## Common Sources of Memory Leaks in JavaScript Code

A search for the memory leaks causes is actually a search for programming patterns that can 'trick' us into keeping the references to the objects that would otherwise be qualified for the garbage collection. The following is a helpful list of places in code that are more susceptible to memory leaks and deserve special consideration when managing the memory.

### 1\. Accidental global variables

Global variables are always available from the root and will never get garbage collected. Some mistakes cause variables leak from the local scope into the global scope when in non-strict mode:

*   assigning value to the undeclared variable,
*   using 'this' that points to the global object.

```
function createGlobalVariables() {
  leaking1 = 'I leak into the global scope'; // assigning value to the undeclared variable
  this.leaking2 = 'I also leak into the global scope'; // 'this' points to the global object
};
createGlobalVariables();
window.leaking1; // 'I leak into the global scope'
window.leaking2; // 'I also leak into the global scope'
```

**How to prevent it:** Strict mode ("use strict") will help you prevent memory leaks and trigger console errors in the example above.

### 2\. Closures

Function-scoped variables will be cleaned up after the function has exited the call stack and if there aren't any references left outside of the function pointing at them. The closure will keep the variables referenced and alive although the function has finished executing and its execution context and variable environment are long gone.

```
function outer() {
  const potentiallyHugeArray = [];

  return function inner() {
    potentiallyHugeArray.push('Hello'); // function inner is closed over the potentiallyHugeArray variable
    console.log('Hello');
  };
};
const sayHello = outer(); // contains definition of the function inner

function repeat(fn, num) {
  for (let i = 0; i < num; i++){
    fn();
  }
}
repeat(sayHello, 10); // each sayHello call pushes another 'Hello' to the potentiallyHugeArray

// now imagine repeat(sayHello, 100000)
```

In this example, `potentiallyHugeArray` is never returned from any of the functions and cannot be reached, but its size can grow infinitely depending on how many times we call the `function inner()`.

**How to prevent it:** Closures are an unavoidable and an integral part of JavaScript, so it is important to:

*   understand when the closure has been created and what objects are retained by it,
*   understand closure's expected lifespan and usage (especially if used as a callback).

### 3\. Timers

Having a `setTimeout` or a `setInterval` referencing some object in the callback is the most common way of preventing the object from being garbage collected. If we set the recurring timer in our code (we can make `setTimeout` behave like `setInterval` i.e., by making it recursive), the reference to the object from the timer's callback will stay active for as long as the callback is invocable.

In the example below the `data` object can be garbage collected only after the timer is cleared. Since we have no reference to `setInterval`, it can never be cleared and `data.hugeString` is kept in memory until the app stops, although never used.

```
function setCallback() {
  const data = {
    counter: 0,
    hugeString: new Array(100000).join('x')
  };

  return function cb() {
    data.counter++; // data object is now part of the callback's scope
    console.log(data.counter);
  }
}

setInterval(setCallback(), 1000); // how do we stop it?
```

**How to prevent it:** Especially if the callback's lifespan is undefined or indefinite:

*   being aware of the objects referenced from the timer's callback,
*   using the handle returned from the timer to cancel it when necessary.

```
function setCallback() {
  // 'unpacking' the data object
  let counter = 0;
  const hugeString = new Array(100000).join('x'); // gets removed when the setCallback returns

  return function cb() {
    counter++; // only counter is part of the callback's scope
    console.log(counter);
  }
}

const timerId = setInterval(setCallback(), 1000); // saving the interval ID

// doing something ...

clearInterval(timerId); // stopping the timer i.e. if button pressed
```

### 4\. Event listeners

Active event listener will prevent all variables captured in its scope from being garbage collected. Once added, the event listener will remain in effect until:

*   explicitly removed with `removeEventListener()`
*   the associated DOM element is removed.

For some types of events, it is expected to be kept around until a user leaves the page - like buttons that are supposed to be clicked multiple times. However, sometimes we want an event listener to execute a definite number of times.

```
const hugeString = new Array(100000).join('x');

document.addEventListener('keyup', function() { // anonymous inline function - can't remove it
  doSomething(hugeString); // hugeString is now forever kept in the callback's scope
});
```

In the example above, an anonymous inline function is used as an event listener, which means it can’t be deleted with `removeEventListener()`. Likewise, the document can't be removed, thus we are stuck with the listener function and whatever it keeps in its scope, even if we only needed it to fire once.

**How to prevent it:** We should always unregister the event listener once no longer needed, by creating a reference pointing to it and passing it to `removeEventListener()`.

```
function listener() {
  doSomething(hugeString);
}

document.addEventListener('keyup', listener); // named function can be referenced here...
document.removeEventListener('keyup', listener); // ...and here
```

In case the event listener must only execute once, `addEventListener()` can take a third parameter, which is an object providing additional options. Given that `{once: true}` is passed as a third parameter to `addEventListener()`, the listener function will be automatically removed after handling the event once.

```
document.addEventListener('keyup', function listener() {
  doSomething(hugeString);
}, {once: true}); // listener will be removed after running once
```

### 5\. Cache

If we keep appending memory to the cache without getting rid of the unused objects and without some logic that limits the size, the cache can grow infinitely.

```
let user_1 = { name: "Peter", id: 12345 };
let user_2 = { name: "Mark", id: 54321 };
const mapCache = new Map();

function cache(obj){
  if (!mapCache.has(obj)){
    const value = `${obj.name} has an id of ${obj.id}`;
    mapCache.set(obj, value);

    return [value, 'computed'];
  }

  return [mapCache.get(obj), 'cached'];
}

cache(user_1); // ['Peter has an id of 12345', 'computed']
cache(user_1); // ['Peter has an id of 12345', 'cached']
cache(user_2); // ['Mark has an id of 54321', 'computed']

console.log(mapCache); // ((…) => "Peter has an id of 12345", (…) => "Mark has an id of 54321")
user_1 = null; // removing the inactive user

// Garbage Collector
console.log(mapCache); // ((…) => "Peter has an id of 12345", (…) => "Mark has an id of 54321") // first entry is still in cache
```

In the example above, the cache is still holding on to the `user_1` object. Therefore, we need to additionally clean the cache from the entries that will never be reused.

**Possible solution:** To work around this issue, we can use `WeakMap`. It is a data structure with weakly held key references which accepts only objects as keys. If we use an object as the key, and it is the only reference to that object – the associated entry will be removed from cache and garbage collected. In the following example, after nulling the `user_1` object, the associated entry gets automatically deleted from the WeakMap after the next garbage collection.

```
let user_1 = { name: "Peter", id: 12345 };
let user_2 = { name: "Mark", id: 54321 };
const weakMapCache = new WeakMap();

function cache(obj){
  // ...same as above, but with weakMapCache

  return [weakMapCache.get(obj), 'cached'];
}

cache(user_1); // ['Peter has an id of 12345', 'computed']
cache(user_2); // ['Mark has an id of 54321', 'computed']
console.log(weakMapCache); // ((…) => "Peter has an id of 12345", (…) => "Mark has an id of 54321"}
user_1 = null; // removing the inactive user

// Garbage Collector

console.log(weakMapCache); // ((…) => "Mark has an id of 54321") - first entry gets garbage collected
```

### 6\. Detached DOM elements

If a DOM node has direct references from JavaScript, it will prevent it from being garbage collected, even after the node is removed from the DOM tree.

In the following example, we created a `div` element and appended it to the `document.body`. The `removeChild()` doesn’t work as expected, and the Heap Snapshot will show detached HTMLDivElement since there is a variable still pointing to the `div`.

```
function createElement() {
  const div = document.createElement('div');
  div.id = 'detached';
  return div;
}

// this will keep referencing the DOM element even after deleteElement() is called
const detachedDiv = createElement();

document.body.appendChild(detachedDiv);

function deleteElement() {
  document.body.removeChild(document.getElementById('detached'));
}

deleteElement(); // Heap snapshot will show detached div#detached
```

**How to prevent it?** One possible solutions is to move DOM references into the local scope. In the example below, the variable pointing to the DOM element is removed after the function `appendElement()` is finished.

```
function createElement() {...} // same as above

// DOM references are inside the function scope

function appendElement() {
  const detachedDiv = createElement();
  document.body.appendChild(detachedDiv);
}

appendElement();

function deleteElement() {
  document.body.removeChild(document.getElementById('detached'));
}

deleteElement(); // no detached div#detached elements in the Heap Snapshot
```

## JS Memory Leaks Conclusion

When dealing with non-trivial apps, identifying and fixing JavaScript memory issues and leaks can turn into a highly challenging task. For that reason, the integral part of the memory management process is understanding the typical memory leak sources to prevent them from happening in the first place. In the end, when it comes to memory and performance, it is the user experience that is at stake, and that’s what matters the most.

Author: Ekaterina Vujasinović
