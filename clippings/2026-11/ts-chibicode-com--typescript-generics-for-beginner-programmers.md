---
url: "https://ts.chibicode.com/generics"
captured_at: "2026-11-16T02:49:01+00:00"
title: "TypeScript Generics for People Who Gave Up on Understanding Generics"
domain: "ts-chibicode-com"
---

**Hello!** I write tutorials to help _beginner programmers_ learn TypeScript. My tutorials might NOT be as useful for experienced programmers learning TypeScript.

**Why target beginner programmers?** As TypeScript is becoming popular, more beginner programmers will be learning it. However, I noticed that many existing tutorials are not so friendly for beginner programmers. This is my attempt to offer a friendlier alternative.

Slide 1 / 14

### TypeScript Generics Too Hard?

function makePair<

  F extends number | string,

  S extends boolean | F

\>()

If you’re (1) new to TypeScript, (2) new to **generics**, and (3) _struggling_ to understand generics, then you’re exactly like me when I was learning Java 13 years ago.

Like TypeScript, the Java programming language supports generics. When I was studying Java in college, I was a beginner programmer, and _generics felt very difficult_ to me. So I gave up on understanding generics at the time and used them without knowing what I was doing. I didn’t understand generics until I got a full time job after college.

I gave up on understanding generics when I was learning Java 13 years ago

Maybe you’re like me from 13 years ago and have felt that TypeScript generics are too difficult. If so, this tutorial is for you! I’ll try to help you actually understand generics.

#### Side Note

If you already understand generics, you won’t find anything new in this tutorial. However, you might know someone (maybe one of your Twitter followers) who’s struggling with generics. I’d appreciate it if you could share this article with them. You can [click here to tweet this article.](https://twitter.com/intent/tweet?url=https%3A%2F%2Fts.chibicode.com%2Fgenerics&via=chibicode&text=TypeScript%20Generics%20for%20People%20Who%20Gave%20Up%20on%20Understanding%20Generics)

The source code for this site is on [GitHub](https://github.com/chibicode/TypeScript-for-Beginner-Programmers):

Slide 2 / 14

### Let’s talk about `makeState()`

First, I created a function called `makeState()` below. We’ll use this function to talk about generics.

function makeState() {

  let state: number

  function getState() {

    return state

  }

  function setState(x: number) {

    state \= x

  }

  return { getState, setState }

}

When you run `makeState()`, it returns two functions: `getState()` and `setState()`. You can use these functions to set and get the variable called `state`.

Let’s try it out! What gets printed out to the console when you run the following code? Try to guess first, and then press the Run button.

const { getState, setState } \= makeState()

setState(1)

console.log(getState())

setState(2)

console.log(getState())

↑ Press this button!

It printed `1`, then `2`. Pretty simple, right?

#### Side Note

If you’ve used React, you might have realized that `makeState()` is similar to the `useState()` hook.

**Confused?** Some people might be wondering: “Why do we have functions inside another function?” or “What’s the `{ getState, setState }` syntax?” If so, click here for more explanation.

Slide 3 / 14

### What if we use a string?

Now, instead of numbers like `1` or `2`, what happens if we use a _string_ like `'foo'`? Try to guess first, and then press the Compile button.

const { getState, setState } \= makeState()

setState('foo')

console.log(getState())

It failed to compile because `setState()` expects a number:

function makeState() {

  let state: number

  function getState() {

    return state

  }

  function setState(x: number) {

    state \= x

  }

  return { getState, setState }

}

To fix this, we can change the type of `state` and `x` from `number` to `string`:

function makeState() {

  let state: string

  function getState() {

    return state

  }

  function setState(x: string) {

    state \= x

  }

  return { getState, setState }

}

It’ll now work! Press Run .

const { getState, setState } \= makeState()

setState('foo')

console.log(getState())

Slide 4 / 14

### Challenge: Two different states

Now that we got the basics down, here’s a challenge for you:

**Question:** Can we modify `makeState()` such that, it can create _two different states_: one that only allows numbers, and the other that only allows strings?

Here’s what I mean:

const numState \= makeState()

numState.setState(1)

console.log(numState.getState()) 

const strState \= makeState()

strState.setState('foo')

console.log(strState.getState()) 

Earlier, our first `makeState()` created number-only states, and our second `makeState()` created string-only states. However, it couldn’t create both number-only states and string-only states.

How can we modify `makeState()` to achieve our goal?

Slide 5 / 14

### Attempt 1: Does this work?

Here’s the first attempt. Does this work?

function makeState() {

  let state: number | string

  function getState() {

    return state

  }

  function setState(x: number | string) {

    state \= x

  }

  return { getState, setState }

}

**This does NOT work.** You’ll end up creating a state that allows both numbers and strings, which is not what we want. Instead, we want `makeState()` to support creating two different states: one that allows only numbers, and the other that allows only strings.

const numAndStrState \= makeState()

numAndStrState.setState(1)

console.log(numAndStrState.getState())

numAndStrState.setState('foo')

console.log(numAndStrState.getState())

Slide 6 / 14

### Attempt 2: Use generics

This is where **generics** come in. Take a look below:

function makeState<S\>() {

  let state: S

  function getState() {

    return state

  }

  function setState(x: S) {

    state \= x

  }

  return { getState, setState }

}

`makeState()` is now defined as `makeState<S>()`. You can think of `<S>` as another thing that you have to pass in when you call the function. But instead of passing a value, you pass a **type** to it.

For example, you can pass the type `number` as `S` when you call `makeState()`:

makeState<number\>()

Then, inside the function definition of `makeState()`, `S` will become `number`:

let state: S 

function setState(x: S ) {

  state \= x

}

Because `state` will be `number` and `setState` will only take `number`, it creates a number-only state.

const numState \= makeState<number\>()

numState.setState(1)

console.log(numState.getState())

On the other hand, to create a string-only state, you can pass `string` as `S` when you call `makeState()`:

const strState \= makeState<string\>()

strState.setState('foo')

console.log(strState.getState())

**Note:** We call `makeState<S>()` a **“generic function”** because it’s literally generic—you have a choice to make it number-only or string-only. And you know it’s a generic function if it takes a type parameter.

`makeState<S>()` is a generic function

function makeState<S\>() {

  let state: S

  function getState() {

    return state

  }

  function setState(x: S) {

    state \= x

  }

  return { getState, setState }

}

#### Side Note

**You might be wondering:** Why did we name the type parameter as “`S`”?

**Answer:** It could actually be any name, but usually people use the first letter of a word that describes what the type is representing. In this case, I chose “`S`” because it’s describing the type of a **“S”**tate. The following names are also common:

*   `T` (for **“T”**ype)
*   `E` (for **“E”**lement)
*   `K` (for **“K”**ey)
*   `V` (for **“V”**alue)

Slide 7 / 14

### Problem: You can create a boolean state!

**But wait a minute:** If you pass `boolean` to `S`, you can create a boolean-only state.

const boolState \= makeState<boolean\>()

boolState.setState(true)

console.log(boolState.getState())

**Maybe we might NOT want this to be allowed.** Suppose that don’t want `makeState()` to be able to create non-number or non-string states (like `boolean`). How can we ensure this?

How can we prevent `makeState()` from  
creating non-number or non-string states?

**The solution:** When you declare `makeState()`, you change the type parameter `<S>` to `<S extends number | string>`. That’s the only change you need to make.

function makeState<S extends number | string\>()

By doing this, when you call `makeState()`, you’d only be able to pass `number`, `string`, or any other type that extends either `number` or `string` as `S`.

Let’s see what happens now when you try to pass `boolean` as `S`. Press Compile below.

function makeState<

  S extends number | string

\>() {

  let state: S

  function getState() {

    return state

  }

  function setState(x: S) {

    state \= x

  }

  return { getState, setState }

}

const boolState \= makeState<boolean\>()

It resulted in an error, which is what we want! We have successfully prevented `makeState()` from creating non-number or non-string states.

As you just saw, you can specify what’s allowed for the type parameter(s) of a generic function.

Slide 8 / 14

### Default type

It can be annoying to specify types like `<number>` or `<string>` every time you call `makeState()`.

**So here’s an idea:** Can we make it so that `<number>` is the_default type parameter_ of `makeState()`? We want to make it so that, if `S` is unspecified, it’s set as `number` by default.

const numState1 \= makeState()

const numState2 \= makeState<number\>()

To make this happen, we can specify the default type of `S` by adding `= number` at the end. It’s kind of like setting default values for regular function parameters, right?

function makeState<

  S extends number | string \= number

\>()

By doing this, you can create a number-only state without specifying the type:

const numState \= makeState()

numState.setState(1)

console.log(numState.getState())

Slide 9 / 14

### Quick recap: Just like regular function parameters

We are about _two-thirds_ of the way through this article. Before we continue, let’s do a quick recap.

What you should remember is that _generics are just like regular function parameters._ The difference is that regular function parameters deal with values, but generics deal with type parameters.

* * *

**Example 1:** For example, here’s a regular function that takes any value:

function regularFunc(x: any) {

}

regularFunc(1)

Similarly, you can declare a generic function with a type parameter:

function genericFunc<T\>() {

}

genericFunc<number\>()

* * *

**Example 2:** In regular functions, you can specify the type of a parameter like this:

function regularFunc(x: number)

regularFunc(1)

regularFunc('foo')

Similarly, you can specify what’s allowed for the type parameter of a generic function:

function genericFunc<T extends number\>()

genericFunc<number\>()

genericFunc<string\>()

* * *

**Example 3:** In regular functions, you can specify the default value of a parameter like this:

function regularFunc(x \= 2)

regularFunc()

Similarly, you can specify the default type for a generic function:

function genericFunc<T \= number\>()

genericFunc()

* * *

Generics are not scary. They’re like regular function parameters, but instead of values, it deals with types. If you understood this much, you’re good to go!

Slide 10 / 14

### Let’s talk about `makePair`

Let’s take a look at the new function called `makePair()`. It’s similar to `makeState()`, but instead of storing a single value, this one stores a pair of values as `{ first: ?, second: ? }`. Right now, it only supports numbers.

function makePair() {

  let pair: { first: number; second: number }

  function getPair() {

    return pair

  }

  function setPair(x: number, y: number) {

    pair \= {

      first: x,

      second: y

    }

  }

  return { getPair, setPair }

}

Let’s try it out! What gets printed out to the console when you run the following code? Try to guess first, and then press the Run button.

const { getPair, setPair } \= makePair()

setPair(1, 2)

console.log(getPair())

setPair(3, 4)

console.log(getPair())

Now, just as we did for `makeState()`, let’s turn `makePair()` into a generic function.

Slide 11 / 14

### Generic `makePair`

Here’s a generic version of `makePair`.

*   It takes _two_ type parameters `F` and `S` (for “F”irst and “S”econd).
*   The type of `first` will be `F`.
*   The type of `second` will be `S`.

function makePair<F, S\>() {

  let pair: { first: F; second: S }

  function getPair() {

    return pair

  }

  function setPair(x: F, y: S) {

    pair \= {

      first: x,

      second: y

    }

  }

  return { getPair, setPair }

}

Here’s an example usage. By calling `makePair` with `<number, string>`, it forces `first` to be `number` and `second` to be `string`.

const { getPair, setPair } \= makePair<

  number,

  string

\>()

setPair(1, 'hello')

* * *

To summarize, you can create a generic function that takes **multiple type parameters**.

function makeState<S\>()

function makePair<F, S\>()

Of course, you can also use the `extends` keyword or default types like before:

function makePair<

  F extends number | string \= number,

  S extends number | string \= number

\>()

You can even make the second type (`S`) to be related to the first type (`F`). Here’s an example:

function makePair<

  F extends number | string,

  S extends boolean | F

\>()

makePair<number, boolean\>()

makePair<number, number\>()

makePair<string, boolean\>()

makePair<string, string\>()

makePair<number, string\>()

Slide 12 / 14

### Generic interfaces and type aliases

Let’s go back to our previous implementation of `makePair()`. Now, take a look at the type of `pair`:

function makePair<F, S\>() {

  let pair: { first: F; second: S }

}

This works as is, but if we want to, we can refactor `{ first: F, second: S }` into an **interface** or a **type alias** so it can be reused.

Let’s first extract the type of `pair` into a **generic interface**. I’ll use `A` and `B` as type parameter names to distinguish them from the type parameters of `makePair()`.

interface Pair<A, B\> {

  first: A

  second: B

}

We can then use this interface to declare the type for `pair`.

function makePair<F, S\>() {

  let pair: Pair<F, S\>

}

By extracting into a generic interface (an interface that takes type parameters), we can reuse it in other places if necessary.

* * *

Alternatively, we can extract it into a **generic type alias**. For object types, type aliases are basically identical to interfaces, so you can use whichever one you prefer.

type Pair<A, B\> \= {

  first: A

  second: B

}

To summarize, you can create generic interfaces and type aliases, just as you can create generic functions.

Slide 13 / 14

### Generic classes

The last thing we’ll cover is **generic classes**. First, let’s revisit the code for `makeState()`. This is the generic version that doesn’t use `extends` or default type parameters.

Let’s revisit `makeState()`

function makeState<S\>() {

  let state: S

  function getState() {

    return state

  }

  function setState(x: S) {

    state \= x

  }

  return { getState, setState }

}

We can turn `makeState()` into a generic class called `State` like below. It looks similar to `makeState()`, right?

class State<S\> {

  state: S

  getState() {

    return this.state

  }

  setState(x: S) {

    this.state \= x

  }

}

To use this, you just need to pass a type parameter on initialization.

const numState \= new State<number\>()

numState.setState(1)

console.log(numState.getState())

To summarize, generic classes are just like generic functions. Generic functions take a type parameter when we call them, but generic classes take a type parameter when we instantiate them.

#### Side Note

You need to set `"strictPropertyInitialization": false` on TypeScript config (`tsconfig.json`) to get the above code to compile.

Slide 14 / 14

### That’s all you need to know!

Thanks for reading! That’s all you need to know about generics in TypeScript. Hope I made generics less scary to you.

If you’d like me to write about some other topics on TypeScript, or if you have feedback, please let me know on [Twitter at @chibicode](https://twitter.com/chibicode).

The source code for this site is on [GitHub](https://github.com/chibicode/TypeScript-for-Beginner-Programmers):

#### More Articles

*   [Your Coding Tutorial Might Need Some Refactoring](https://ts.chibicode.com/refactor/)
    
    Jan 1, 2020
    
*   [TypeScript Tutorial for JS Programmers Who Know How to Build a Todo App](https://ts.chibicode.com/todo/)
    
    Dec 18, 2019
