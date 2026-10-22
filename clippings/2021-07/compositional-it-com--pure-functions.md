---
url: "https://www.compositional-it.com/news-blog/pure-functions/"
captured_at: "2021-07-20T16:53:31-03:00"
title: "Pure functions | Compositional IT"
domain: "compositional-it-com"
---

# Pure functions

A pure function is a function with both of the following properties:

1. If the function is called multiple times with the same arguments, the output value is the same each time.
2. The function has no side effects.

Let's examine each of these properties in more detail.

## Determinism

A function with the first of the above properties is said to be deterministic. A good way to understand determinism is to see some of the ways in a which a function might be non-deterministic.

### Non-determinism: dependence on a non-local mutable variable

Consider the `addVariable` function below:

```
let mutable variable = 1
let addVariable x = x + variable
```

It's not deterministic - its return value can be different even when given the same argument:

```
addVariable 3 // 4

variable <- 2
addVariable 3 // 5
```

Note that the function would be deterministic if it relied on a constant value instead of a mutable variable.

```
let constVal = 3
let addConst x = x + constVal
```

### Non-determinism: dependence on a mutable parameter

```
let countRa (ra: ResizeArray<'a>) = ra.Count
```

The `countRa` function above is not deterministic:

```
let ra = ResizeArray<string> [ "a"; "b" ]
countRa ra // 2

ra.Add "c"
countRa ra // 3
```

But it would be if it relied on an immutable parameter.

```
let countList l = List.length l
```

### Non-determinism: dependence on an input stream

```
let addFiveToUserInput () =
    System.Console.WriteLine "Enter an int:"
    let s = System.Console.ReadLine ()
    let x = System.Int32.Parse s
    x + 5
```

`addFiveToUserInput` is not deterministic:

```
addFiveToUserInput () // Enter 1 when prompted, get 6.
addFiveToUserInput () // Enter 2 when prompted, get 7.
```

### Determinism: an alternative interpretation

You may have noticed a common theme in the examples: a function is non-deterministic if it depends on something that might change between function invocations. This is true generally of non-deterministic functions, and thinking of non-determinism in this way can be useful.

To say the same thing another way: a deterministic function is a function that is isolated from the effects of other parts of the program.

## No side effects

A side effect of a function is a change that the function makes in addition to returning a value in the usual way. We'll look at some functions that have side effects to get a better understanding of when a function has no side effects.

### Side effect: mutation of a non-local variable

```
let mutable counter = 0
let add x y =
    counter <- counter + 1
    x + y
```

The `add` function above mutates a non-local variable, `counter`, which is a side effect.

```
counter // 0

add 1 2
counter // 1 - add has had a side effect.
```

### Side effect: argument mutation

```
let count (ra: ResizeArray<'a>) =
    let c = ra.Count
    ra.Reverse()
    c
```

The `count` function above has the side effect of changing (reversing) its argument.

```
let x = ResizeArray<string> [ "a"; "b" ]
x // ResizeArray<string> = seq ["a"; "b"]

count x
x // ResizeArray<string> = seq ["b"; "a"] - count has had a side effect.
```

### Side effect: emitting data via an output stream

```
let multiply x y =
    let result = x * y
    printfn $"{x} times {y} is {result}"
    result
```

`multiply` has a side-effect: writing to stdout. Other examples of emitting data via an output stream might be saving to a database or sending an email.

```
multiply 5 7 // Prints "5 times 7 is 35" to stdout.
```

### No side effects: an alternative interpretation

As seen above, a function has side effects if it changes something external to the function when it's evaluated.

To say the same thing another way: a function with no side effects is a function that doesn't change anything external to itself.

## Pure functions: putting it together

As I've already alluded to, a pure function is isolated from other parts of the program: it is unaffected by other functions' side effects and doesn't have any side effects that might impact other functions. As a result, a pure function only has *direct* input (arguments) and output (return value) rather than *indirect* input (non-local variables or an input stream) and output (side effects).

Note that isolation is stronger than lack of indirect input/output: a function with only direct input and output must also ensure that its arguments are immutable in order to be isolated from the rest of the program.

## Summary

A pure function is deterministic and has no side effects. As a result, it has no indirect input or output, making it inherently simple, and is isolated from the rest of the program. This brings a host of benefits, which I'll discuss in a future blog post.

## References

- Wikipedia's [pure function](https://en.wikipedia.org/wiki/Pure_function) article.
- The terminology (in)direct input/output is borrowed from Mark Seemann's [dependency rejection](https://blog.ploeh.dk/2017/02/02/dependency-rejection/) blog post.
