---
url: "https://javascript.plainenglish.io/javascript-concepts-every-programmer-should-know-d04731fe7a7c"
captured_at: "2022-05-27T09:57:07-03:00"
title: "JavaScript Concepts Every Programmer Should Know | JavaScript in Plain English"
domain: "javascript-plainenglish-io"
---

# JavaScript Concepts Every Programmer Should Know

## Know these JavaScript concepts to make your life easier as a programmer.

JavaScript is the number one programming language for the web, but besides that, it also spread to many platforms because of many reasons.

One of those is the ease of development, and how easily it can be picked up and learned, but still — as in every programming language, there are always some less complex and some more complex concepts to grasp.

![1*InoFyDBUOEJiaoXEgTGR4A.png](javascript-plainenglish-io--javascript-concepts-every-programmer-should-know/8b2c928e1483eed76a1bd274619c5f77.png)

Image Credit — Workato

“JavaScript is the only programming language people feel like they don’t need to learn before they start using it.” — Douglas Crockford

It does feel intuitive but still, there are fundamentals and essentials to it, that you as either a novice or experienced programmer should know.

Let’s dig in!

# Arrow Functions

This one is rather easy — the Arrow Function was introduced in ES6, and you probably already know about it.

![1*VL71kTYK9FGUCZJmSWB5GQ.gif](javascript-plainenglish-io--javascript-concepts-every-programmer-should-know/5b30aa4c6d594c1aa96cc4fe31c9a08a.gif)

GIF Credit — [ahighmentality / deviantart.com](https://www.deviantart.com/ahighmentality)

Compared to traditional functions, we can write functions with the shorter *arrow syntax*.

```
# Traditional Function  
function sum(param1, param2) {  
    return param1 + param2;  
}let result = sum(1, 1);# Arrow Function  
let sum = (param1, param2) => param1 + param2;  
let result = sum(1, 1);
```

Few more things to keep in mind.

1. You can use [rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)

```
# Arrow Function With Rest Parameters  
let sum = (param1, param2, ...params) =>   
     params.reduce((total, next) => total + next, param1 + param2);let result = sum(1, 1, 2, 3, 4, 5);
```

2. You can define [default values for parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)

```
# Arrow Function With Default Parameters  
let sum = (param1, param2 = 2) => param1 + param2;let result = sum(1);
```

3. You can make use of [restructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)

```
# Arrow Function With Object Destructured Parameters  
let sum = ({ param1, param2 }) => param1 + param2;let object = {param1: 5, param2: 15};  
let result = sum(object);
```

The aforementioned concepts are worth looking into on their own, so make sure to read about:

# Array Reduce

The previous example brings me to — Array Reduce. The Reduce function is not a must-know, but understanding it might be well worth it. The `reduce()` function executes a provided *“reducer”* on a set of elements, executing an expression and providing the result to every next iteration.

The easiest way to remember how Reduce works is by imagining that it 1. it *reduces* a set of elements to a *single value* — and 2. similar to recursion, it iterates over each element, providing it with the *previous calculation ie. value*.

The result of the `reduce()`function is a single value.

```
# Reduce  
# def. reduce(callbackFn(previous, next);  
# def. reduce(callbackFn(previous, next), initialValue);const elements = [1, 2, 3, 4, 5];  
const sum = elements.reduce((previous, next) => previous + next, 0);
```

The reduce() function takes two arguments. The first one is a user-supplied function with two parameters, one being the **previous i.e. return value of the preceding element’s iteration**, and the other one being the **next element in the array** that's going to be computed.

It takes a second argument — initialValue, and as you can see this will be used as the **previous** for the first iteration, as there is no **return value of the preceding element’ iteration**.

Recursive functions like `reduce` are very powerful, but often hard to read and understand. The Array Reduce is something that may be useful to have in your skill-set, as it will make you much more comfortable when you actually need it or encounter this function, but when writing it, make sure you always weigh out the benefits versus the readability tradeoffs, as oftentimes the same can be achieved with much simpler code.

# Asynchronous Execution

There’s a lot of history to read about synchronous execution, how single-threaded computers ran tasks in cycles, allocating short time slots for each task, thus achieving what would look like “simultaneous” flows.

Now with multithreading in the picture in modern computer architectures, executing tasks at the same time is possible. However, how does async fit into the picture?

JavaScript is **synchronous** **by default and is single-threaded** — but to achieve asynchronous execution, we can make use of async / await. By definition, async tasks are tasks executed in the *“background”,* and generally are useful for long-running tasks, such as HTTP requests.

Async / await, and how it works in the background begs for a post on its own, but in simple terms — JS makes use of JS engines, such as Node or the Browser’s engine e.g. Google Chrome’s V8. The Engine itself will pick asynchronous tasks from JavaScript’s single thread and execute them in the background. This might still happen on the same thread, but there are some operations that the engine will actually execute on a different thread, for example, HTTP requests.

In any case, async tasks will be non-blocking for the rest of the JS code being run, which makes them perfect for long-running requests and generally, functions that take longer to complete.

## Async Script

First off — something to not be confused with `async / await`, is the async script tag. We can achieve asynchronous script loading by declaring the script included in the HTML, as `async`.

```
# Async script  
<script async src="..."></script>
```

Traditionally, browsers rendering the HTML would synchronously load and execute a script, unless we add the `async`keyword. This will let the browser know we want the script loaded *asynchronously, without blocking* the parsing of the HTML in question.

This is not to be confused with async / await — as this is a different concept, but yet useful for asynchronously loading JavaScript files.

## Async / Await

The asynchronous execution of JS blocks of code and functions itself always is referred to by `async / await`keywords.

To declare an asynchronous function in JS, we use the `async` keyword.

```
# Async function  
async function sum(param1, param2) {  
    return param1 + param2;  
}
```

Now, calculating just a sum would be a terrible example, as we already said — async is mainly useful with long-running tasks, but for the sake of the example, the above is how we declare an asynchronous function. This function can be used like any other — but, how is such a function executed and how is the return value used? We use `await` for exactly that.

```
# Await an asynchronous function  
let result = await sum(1, 2);
```

Now there’s a small gotcha here — await can be used only in async functions. It might be a bit unintuitive, but in order to get the returned value from an async function, we need to use Promises.

In short, if you inspect the returned value from `sum`, you’ll see it’s a Promise already. We can use the actual computed value within the `then` method.

```
# Promise - Then  
sum(1, 2).then(result => console.log(result));
```

Async / await in JavaScript is actually built on Promises, which brings us to the next.

# Promises

![1*h3awdHnwX2HYkXfxv2Dwlg.gif](javascript-plainenglish-io--javascript-concepts-every-programmer-should-know/4fcbe46b162c26ee97b275196fddb87d.gif)

If you need to give a promise to someone in sign language — Credit [How to sign PROMISE in ASL?](https://www.youtube.com/watch?v=HCFv9ZPJGu0)

The easiest way to understand Promises is to imagine that it’s a literal promise that some person gave you — eg. *I promise you I’ll clean up the house.*

The task itself will be asynchronous to you, it won’t be executed by you but by me — and I will notify you back with the result once done. One more thing to keep in mind is that I might fail during the task but still, I’ll get back to you with the result.

A big note, however — JavaScript first brought Promises and then async / await, so many will argue whether you should stick to them, but for the sake of concepts — here’s a quick example of how Promises work.

```
let promise = new Promise((resolve, reject) => {  
    // Long running task  
    let result = someGetFunction();  
    if (result.success) {  
        resolve(result.data);} else {  
        reject(result.error.message);  
    }  
});promise.then(result => {  
    console.log(result);  
}).catch(error => {  
    console.log(error);  
});console.log("Promise has finished, didn't it?");
```

The above block of code looks like it would first log the result or the error of the `promise` before the last line, but actually, as said — asynchronous tasks and in this case, Promises are meant for long-running executions.

Making an HTTP request to get data is a long-running task, and it will definitely take longer than our engine to parse the whole code block including the last log line.

The above code block also nicely illustrates how tasks are executed in the background, without blocking our parser to go through the rest of the code.

There are many JavaScript concepts that developers must know and learn other than the aforementioned.

Some are less important some are more important, but hopefully, this article highlights and focuses few of them and helps you better understand these.

If you are a developer reading this, I hope it helps you on your journey, regardless if you are just starting or you already have many years under your belt. Please feel free to comment and suggest more concepts that are likely to help others!

Thank you for reading!

—

If you enjoyed reading this article and thought it was interesting, check out [JavaScript Concepts Every Programmer Should Know v1.0.2](https://medium.com/p/cc87f541e05).

[## JavaScript Concepts Every Programmer Should Know v1.0.2

### Recently I wrote about JS in JavaScript Concepts Every Programmer Should Know, and the community feedback was great.

be-ja.medium.com](https://be-ja.medium.com/javascript-concepts-every-programmer-should-know-v1-0-2-cc87f541e05)

*More content at* [***PlainEnglish.io***](https://plainenglish.io/)*. Sign up for our* [***free weekly newsletter***](http://newsletter.plainenglish.io/)*. Follow us on* [***Twitter***](https://twitter.com/inPlainEngHQ) *and* [***LinkedIn***](https://www.linkedin.com/company/inplainenglish/)*. Check out our* [***Community Discord***](https://discord.gg/GtDtUAvyhW) *and join our* [***Talent Collective***](https://inplainenglish.pallet.com/talent/welcome)*.*
