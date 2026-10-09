---
url: "http://www.joezimjs.com/javascript/patterns-asynchronous-programming-promises/?utm_source=javascriptweekly&utm_medium=email"
captured_at: "2014-04-25T18:02:19-03:00"
title: "Patterns for Asynchronous Programming with Promises | Joe Zim's JavaScript Blog"
domain: "joezimjs-com"
---

# Patterns for Asynchronous Programming with Promises

![8cc7fd929370da22e165a936229fd887.jpg](joezimjs-com--patterns-for-asynchronous-programming-with-promises/8cc7fd929370da22e165a936229fd887.jpg)Promises are currently the best tool we have for asynchronous programming and they appear to be our best hope for the forseeable future, even if they'll be hiding behind [generators or async functions](http://www.joezimjs.com/javascript/synchronizing-asynchronous-javascript-es7/). For now, we'll need to use promises directly, so we should learn some good techniques for using them right now, especially when dealing with multiple asynchronous operations, whether they happen in parallel or sequentially.

## Before We Start

Before I get into details on the patterns, I'm going to have to fill you in on some points. First off, I'm using [Q](http://documentup.com/kriskowal/q/) for my promises implementation. I'm also using [Underscore](http://underscorejs.org/) or [Lodash](http://lodash.com/) (pick your favorite; personally I like Lodash) for things like `map`, `each`, and `reduce`. In the code, `asyncOperation` just represents a function that takes a single number parameter, performs an asynchronous operation according to that number, and returns a promise, while `// ...` represents whatever code is specific to your application that operates on the values returned from `asyncOperation`.

## Parallel Asynchronous Operations

First we'll take a look at parallel operations. This refers to getting multiple asynchronous operations queued up and running at the same time. By running them in parallel, you can significantly increase your performance. Sadly, this isn't always possible. You may be required to run the operations in sequential order, which what we'll be talking about in the next section.

Anyway, we'll first look at running the asynchronous operations in parallel, but then performing synchronous operations on them in a specific order after all of the asynchronous operations have finished. This gives you a performance boost from the parallel operations, but then brings everything back together to do things in the right order when you need to.

|  |  |
| --- | --- |
|  | `function` `parallelAsyncSequentialSync (){`  `var` `values = [1,2,3,4];`  `` // Use `map` to create an array of promises by performing ``  `` // `asyncOperation` on each element in the original array. ``  `// They should happen in parallel.`  `var` `operations = _.map(values, asyncOperation);`  `// Return a promise so outside code can wait for this code.`  `return` `Q.all(operations).then(``function``(newValues) {`  `// Once all of the operations are finished, we can loop`  `// through the results and do something with them`  `_.each(newValues,` `function``(value) {`  `// ...`  `});`  `// Make sure we return the values we want outside to see`  `return` `newValues;`  `});`  `}` |

We use `map` to get all of our asynchronous operations fired off right away, but then use `Q.all` to wait for them all to finish, and then we just run a loop over the new values and do whatever operations we need to do in the original order.

Sometimes, the order that our synchronous operations run in don't matter. In this case, we can run each of our synchronous operations immediately after their respective asynchronous operations have finished.

|  |  |
| --- | --- |
|  | `function` `parallelAsyncUnorderedSync (){`  `var` `values = [1,2,3,4];`  `` // Use `map` to create an array of promises ``  `var` `operations = _.map(values,` `function``(value) {`  `` // return the promise so `operations` is an array of promises. ``  `return` `asyncOperation(value).then(``function``(newValue) {`  `// ...`  `// we want the new values to pass to the outside`  `return` `newValue;`  `});`  `});`  `// return a promise so the outside can wait for all operations to finish.`  `return` `Q.all(operations);`  `}` |

For this, we use `map` again, but instead of waiting for all of the operations to finish, we provide our own callback to `map` and do more inside of it. Inside we invoke our asynchronous function and then call `then` on it immediately to set up our synchronous operation to run immediately after the asynchronous one has finished.

## Sequential Asynchronous Operations

Let's take a look at some patterns for sequential asynchronous operations. In this case, the first asynchronous operation should finish before moving on to the next asynchronous operation. I have two solutions for doing this, one uses `each` and one uses `reduce`. They are quite similar, but the version with `each` needs to store a reference to the promise chain, whereas the version with `reduce` passes it through as the memo. Essentially, the version with `each` is just more explicit and verbose, but they both accomplish the same thing.

|  |  |
| --- | --- |
|  | `function` `sequentialAsyncWithEach (){`  `var` `values = [1,2,3,4];`  `var` `newValues = [];`  `var` `dfd = Q.defer();`  `var` `promise;`  `dfd.resolve();`  `promise = dfd.promise;`  `_.each(values,` `function``(value) {`  `promise = promise.then(``function``() {`  `return` `asyncOperation(value);`  `}).then(``function``(newValue) {`  `// ...`  `newValues.push(newValue);`  `});`  `});`  `return` `promise.then(``function``() {`  `return` `newValues;`  `});`  `}` |

|  |  |
| --- | --- |
|  | `function` `sequentialAsyncWithReduce (){`  `var` `values = [1,2,3,4];`  `var` `newValues = [];`  `var` `dfd = Q.defer();`  `dfd.resolve();`  `return` `_.reduce(values,` `function``(memo, value) {`  `return` `memo.then(``function``() {`  `return` `asyncOperation(value);`  `}).then(``function``(newValue) {`  `// ...`  `newValues.push(newValue);`  `});`  `}, dfd.promise).then(``function``() {`  `return` `newValues;`  `});`  `}` |

In each version we just chain each asynchronous operation off of the previous one. It's annoying that we need to create a "blank" promise that is simply used to start the chain, but it's a necessary evil. Also, we need to explicitly assign values to the `newValues` array (assuming you want to return those), which is another necessary evil, though maybe not quite as evil. I personally think the version with `each` is slightly easier to read thanks to its explicit nature, but it's a stylistic choice and `reduce` works perfectly for this situation.

## Conclusion

I used to think promises were very straight-forward and even had a hard time finding a reason to use them over standard callbacks, but the more I need them, the more useful I find them to be, but I also find them to be more complicated with numerous ways they can be used, as shown above. Understanding your options and keeping a list of patterns you can follow great helps when the time comes to use them. If you don't already have these patterns embedded in your brain, you may want to save them somewhere so you have them handy when you need them.

Well, that's all for today. God bless! Happy Coding!

## About the Author

[![5aa6b9879604fd6f0d1e2405d416d5fa.jpg](joezimjs-com--patterns-for-asynchronous-programming-with-promises/5aa6b9879604fd6f0d1e2405d416d5fa.jpg)](http://www.joezimjs.com/authors/joe-zimmerman/)

### [Joe Zim](http://www.joezimjs.com/authors/joe-zimmerman/)

Joe Zimmerman has been doing web development ever since he found an HTML book on his dad's shelf when he was 12. Since then, JavaScript has grown in popularity and he has become passionate about it. He also loves to teach others though his blog and [other](http://coding.smashingmagazine.com/author/joseph-zimmerman/?rel=author) [popular](http://www.adobe.com/devnet/author_bios/joseph-zimmerman.html) [blogs](http://net.tutsplus.com/author/joe-zimmerman/). When he's not writing code, he's spending time with his wife and children and leading them in God's Word.
