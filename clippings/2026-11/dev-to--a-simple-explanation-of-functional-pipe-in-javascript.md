---
url: "https://dev.to/benlesh/a-simple-explanation-of-functional-pipe-in-javascript-2hbj"
captured_at: "2026-11-16T18:58:26+00:00"
title: "A simple explanation of functional pipe in JavaScript"
domain: "dev-to"
---

Sometimes I'm asked why we don't have "dot-chaining" in RxJS anymore, or why RxJS made the switch to use `pipe`. There are a lot of reasons, but this is really something that needs to be looked at from a higher level than just RxJS.

The need for piping functions comes from two problems butting heads: The desire to have a broad set of available development APIs for simple types (like Array, Observable, Promise, etc), and the desire to ship smaller apps.

## [](#the-size-problem)The size problem

JavaScript is a very unique language with a problem that most other programming languages do not have: Usually, JavaScript is shipped over a network, parsed, and executed at the exact moment the user wants to use the app the JavaScript is powering. The more JavaScript shipped, the longer it will take to download and parse, thus slowing down your app's responsiveness. Something that can have a HUGE impact on the user experience.

This means that trying to keep JavaScript apps small is critically important. Fortunately, we have a lot of great tools to do this nowadays. We have a lot of "build time" bundlers and optimizers that can do things like tree-shaking in order to get rid of unused code prior at build time, so we can ship the least amount of JavaScript possible to the users.

Unfortunately, tree-shaking doesn't remove code if it can't statically be sure that the code isn't being used somewhere.

## [](#providing-broad-apis)Providing broad APIs

For types to be as useful as possible, it is nice to have a well-groomed set of known functionality attached to the type. Especially in such a way that it can be "chained" by making calls left-to-right on that type.

The "built-in" way for JavaScript to provide broad APIs for a given type is prototype augmentation. This means that you would add methods to any given type's `prototype` object. So if we wanted to add a custom `odds` filter to array, we could do it like this:  

```
Array.prototype.odds = function() {
  return this.filter(x => x % 2 === 1)
}

Array.prototype.double = function () {
  return this.map(x => x + x);
}

Array.prototype.log = function () {
  this.forEach(x => console.log(x));
  return this;
}
```

Enter fullscreen mode Exit fullscreen mode

### [](#prototype-augmentation-is-problematic)Prototype augmentation is problematic

**Mutating global variables**. You're now manipulating something that everyone else can touch. This means other code could start depending on this `odds` method being on `Array`, without knowing that it actually came from a third party. It also means that another bit of code could come through and trample `odds` with it's own definition of `odds`. There are solutions to this, like using `Symbol`, but it's still not ideal.

**Prototype methods cannot be tree-shaken**. Bundlers will not currently attempt to remove unused methods that have been patched onto the prototype. For reasoning, see above. The bundler has no way of knowing whether or not a third party is depending on using that prototype method.

## [](#functional-programming-ftw)Functional programming FTW!

Once you realize that the `this` context is really just a fancy way to pass another argument to a function, you realize you can rewrite the methods above like so:  

```
function odds(array) {
  return array.filter(x => x % 2 === 0);
}

function double(array) {
  return array.map(x => x + x);
}

function log(array) {
  array.forEach(x => console.log(x));
  return array;
}
```

Enter fullscreen mode Exit fullscreen mode

The problem now is that you have to read what's happening to your array from right-to-left, rather than from left-to-right:  

```
// Yuck!
log(double(odds([1, 2, 3, 4, 5])))
```

Enter fullscreen mode Exit fullscreen mode

The advantage, though, is that if we don't use `double`, let's say, a bundler will be able to tree-shake and remove the `double` function from the end result that is shipped to users, making your app smaller and faster.

## [](#piping-for-lefttoright-readability)Piping for Left-to-right readability

In order to get better left-to-right readability, we can use a `pipe` function. This is a common functional pattern that can be done with a simple function:  

```
function pipe(...fns) {
  return (arg) => fns.reduce((prev, fn) => fn(prev), arg);
}
```

Enter fullscreen mode Exit fullscreen mode

What this does is return a new higher-order function that takes a single argument. The function that _that_ returns will pass the argument to the first function in the list of functions, `fns`, then take the result of that, and pass it to the next function in the list, and so on.

This means that we can now compose this stuff from left-to-right, which is a little more readable:  

```
pipe(odds, double, log)([1, 2, 3, 4, 5])
```

Enter fullscreen mode Exit fullscreen mode

You could also make a helper that allowed you to provide the argument as the first argument to make it even more readable (if a bit less reusable) like so:  

```
function pipeWith(arg, ...fns) {
  return pipe(...fns)(arg);
}

pipeWith([1, 2, 3, 4, 5], odds, double, log);
```

Enter fullscreen mode Exit fullscreen mode

In the case of `pipeWith`, now it's going to take the first argument, and pass it to the function that came right after it in the arguments list, then it will take the result of that and pass it to the next function in the arguments list, and so on.

### [](#pipeable-functions-with-arguments)"Pipeable" functions with arguments

To create a function that can be piped, but has arguments, look no further than a higher order function. For example, if we wanted to make a `multiplyBy` function instead of `double`:  

```
pipeWith([1, 2, 3, 4, 5], odds, multiplyBy(2), log);

function multiplyBy(x) {
  return (array) => array.map(n => n * x);
}
```

Enter fullscreen mode Exit fullscreen mode

### [](#composition)Composition

Because it's all just functions, you can simplify code and make it more readable by using `pipe` to create other reusable, and pipeable, functions!  

```
const tripleTheOdds = pipe(odds, multiplyBy(3));


pipeWith([1, 2, 3, 4, 5], tripleTheOdds, log)
```

Enter fullscreen mode Exit fullscreen mode

## [](#the-larger-js-ecosystem-and-the-pipeline-operator)The larger JS ecosystem and the Pipeline Operator

This is roughly the same pattern that is used by [RxJS operators](https://rxjs.dev/guide/operators) via Observable `pipe` method. This was done to get around all of the issues listed with prototype above. But this will clearly work with any type.

While `prototype` augmentation may be the "blessed" way to add methods to types in JavaScript, in my opinion, it is a bit of an antipattern. JavaScript needs to start embracing this pattern more, and ideally we can get a simple version of the [pipeline operator proposal](https://github.com/tc39/proposal-pipeline-operator) to land in JavaScript.

With the pipeline operator, the above code could look like this, but be functionally the same, and there wouldn't be a need to declare the `pipe` helper.  

```
pipeWith([1, 2, 3, 4, 5], odds, double, log);

// becomes

[1, 2, 3, 4, 5] |> odds |> double |> log
```

Enter fullscreen mode Exit fullscreen mode
