---
url: "https://how-to.dev/the-simplest-case-for-unit-tests-pure-functions"
captured_at: "2022-08-04T09:07:05-03:00"
title: "The Simplest Case for Unit Tests: Pure Functions"
domain: "how-to-dev"
---

# The Simplest Case for Unit Tests: Pure Functions

Development teams across the industry are using unit tests to maintain the quality of their code. However, it seems like many beginner-oriented materials are not really covering unit tests. That’s unfortunate—adding unit tests is a perfect onboarding task I like to give new colleagues on my teams. By getting used to unit tests, they can start to familiarize themselves with the codebase and make significant progress while facing no risk or stress related to building client facing changes.

## What are unit tests

Unit tests are small pieces of code that verify units of your code against explicit expectations. You write them to give yourself a way of checking your code automatically. Thus, it’s possible to quickly check that things work as expected as you continue working on the codebase.

In real-world JavaScript projects, people usually use one of these open-source frameworks for testing:

- Jasmine
- Jest
- Mocha

In this article, for simplicity, I’ll use pseudocode inspired by those frameworks.

## What are pure functions?

Pure functions are functions whose results depend only on the arguments that were provided. They don't keep internal state, and they don't read external values besides arguments. They are the same as functions in the mathematical sense—for example:

- `sin(x)`,
- `cos(x)`,
- `f(x) = 4 * x + 5`

## Data operation

Let’s define a greeting function:

```
function greet(name, surname) {
  return `Hello ${name} ${surname}!`;
}
```

It’s a pure function: every time when I run `greet(‘Marcin’, ‘Wosinek’)`, it will return ‘Hello Marcin Wosinek!’.

### Test it!

How can I test this function?

```
expect(greet(‘Lorem’, ‘Ipsum’)).toEqual(‘Hello Lorem Ipsum!’);
```

Testing frameworks turns the code above into something like:

```
if(greet(‘Lorem’, ‘Ipsum’) !== ‘Hello Lorem Ipsum!’) {
  throw new Error(“greet(‘Lorem’, ‘Ipsum’) doesn’t equal ‘Hello Lorem Ipsum!’”)
}
```

And shows you a report for the results for all the checks they run.

### Edge cases

Writing unit tests makes you think about edge cases. For example, what *should* happen if our function is called with only one parameter? Greeting the person by name sounds like the most reasonable thing, but the current implementation does a different thing:

```
greet(‘Marcin’); // returns “Hello Marcin undefined!”
```

If we want to do the support name-only calls, we can add the following test case:

```
expect(greet(‘Lorem’)).toEqual(‘Hello Lorem!’);
```

This will require improvements in our implementation:

```
function greet(name, surname) {
  if (surname) {
    return `Hello ${name} ${surname}!`;
  } else {
    return `Hello ${name}!`;
  }
}
```

Similarly, we could continue adding other edge cases. For example, what should happen:

- when we greet someone with surname only
- without a name or surname
- when the method is called with three parameters—with the middle name or second surname

By thinking about those cases and adding tests for them, we build more resilient code.

## Discount calculations

Let’s try some operations with money. Imagine we are building a shop system, and we want a method for applying discounts to the price. A quick and dirty solution would be:

```
function calculateDiscountedPrice(originalPrice, discount) {
  return originalPrice - originalPrice * discount;
};
```

### Test it!

Let’s consider a few cases we could test:

```
// case 1
expect(calculateDiscountedPrice(10, 1/4)).toBe(7.5);

// case 2
calculateDiscountedPrice(0.9, 2/3).toBe(0.3)

// case 3
expect(calculateDiscountedPrice(10, 1/3)).toBe(6.67);
expect(calculateDiscountedPrice(10, 2/3)).toBe(3.33);
```

Do those examples look similar—to the point of being a bit repetitive? Actually, they are very different, and only *case 1* will work as expected with our current implementation.

### Edge cases

What happens in our edge cases? In *case 2*, we are hitting a rounding error caused by how numbers are stored in JavaScript. JavaScript has only *floating-point* numbers, so every round decimal is represented in memory with an approximation that introduces a tiny rounding error. As you do operations on numbers, those errors can add up, and you will end up with a result that is slightly off from what you expected. In our case:

```
calculateDiscountedPrice(0.9, 2/3)
0.30000000000000004
```

It’s very close to `0.3`, but it’s not the same value. For applications in which we deal with money, it makes sense to implement a money operation in a way that cleans up those errors along the way.

The *case 3* test will fail because of the lack of rounding—the function returns `6.666666666666667` and `3.333333333333334` instead. In most systems, we care only about value down to the second decimal place—down to the cent.

Both issues can be resolved with the same implementation tweak:

```
function calculateDiscountedPrice(originalPrice, discount) {
  const newPrice = originalPrice - originalPrice * discount;
  return Math.round(newPrice * 100) / 100
};
```

Is it always working as expected? Not necessarily—you can check out this [stack overflow thread](https://stackoverflow.com/questions/11832914/how-to-round-to-at-most-2-decimal-places-if-necessary) to read about edge cases. If possible, you would probably like to use some third-party library to do the rounding for you.

## Math operations

Let’s consider some purely mathematical operations:

```
function power(base, exponent) {
  return base ** exponent;
};
```

Is there anything interesting we could test here?

### Test it!

```
// case 1
expect(power(2, 2)).toBe(4);
expect(power(2, 10)).toBe(1024);
expect(power(2, 0)).toBe(1);

// case 2
expect(power(0, 0)).toBe(NaN);
```

*Case 1* works as expected, whereas *case 2* fails: JS returns 1, which is different from what we learned in math.

### Edge cases

What else could we test here? We could expand our testing and cover cases with incorrect arguments, such as:

- `power()`,
- `power(‘lorem’, ‘ipsum’)`,
- `power({}, 0)`.

Why test those cases? Because they can happen in the application, and your program will do something with them. You will be better off if you spend some time thinking about what makes the most sense in the context of your application:

- returning `NaN`,
- throwing an error, or
- defaulting to some reasonable value, for example `1`

And whatever you decide, you can make it explicit in your unit tests.

## Want to know more?

I’ve written more about unit tests on my blog:

## Summary

Pure functions are the most straightforward to cover with unit tests. Even still, writing them puts you in the right mindset to find edge cases that otherwise wouldn’t be thought through correctly. It’s a valuable exercise and skill for beginner programmers: it teaches you to think in a very precise, machine-like way; and improving unit tests coverage is a welcome contribution in many projects.
