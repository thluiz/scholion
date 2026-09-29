---
url: "https://livecodestream.dev/post/2020-06-03-stranger-things-javascript-edition/"
captured_at: "2020-06-04T19:45:25-03:00"
title: "Stranger Things, JavaScript Edition"
domain: "livecodestream-dev"
---

# Stranger Things, JavaScript Edition

## Find the explanation to some of the weirdest JavaScript moments here

Jun 3, 2020

![Hero.jpg](livecodestream-dev--stranger-things-javascript-edition/06c87cf02bf33812014122cd8281ce88.jpg)

Today we are going to make a special post dedicated to those weird JavaScript moments, where things behave a little bit strange.

> “Nobody normal ever accomplished anything meaningful in this world.” — Jonathan, Stranger Things

We will look at some code snippets with surprising results, and we will do an explanation of what is going on, so that we can better understand our beloved programming language. Though it’s a weirdo, we love it!

---

## Scenario #1: [‘1’, ‘7’, ‘11’].map(parseInt)

Let’s take a look at the code for our first scenario

```
['1', '7', '11'].map(parseInt);
```

For what you would expect the output to be:

```
[1, 7, 11]
```

However, things get a bit off here, and the actual result is:

```
[1,NaN,3]
```

At first, this may look up very weird, but it actually has an elegant explanation. To understand what is going on, we need to understand the 2 involved functions, `map` and `parseInt`.

### map()

`map()` calls a provided `callback` function **once for each element** in an array, in order, and constructs a new array from the results. `callback` is invoked only for indexes of the array which have assigned values (including [undefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)).

Now the `callback` function referenced above will receive some particular parameters, let’s take an example with it’s output:

```
[1, 2, 3].map(console.log)
1 1 0 > (3) [1, 2, 3]
1 2 1 > (3) [1, 2, 3]
1 3 2 > (3) [1, 2, 3]
```

As can be seen, the map function not only did pass the value of the item but also the index and a copy of the full array on each iteration. This is important and is in part what’s affecting our previous result.

### parseInt()

The `parseInt()` function parses a string argument and returns an integer of the specified radix (the base in mathematical numeral systems).

So now, by definition, `parseInt(string [, radix])` expects two parameters, the string we want to parse, and the radix.

### Resolving the mistery

Now we know enough about the two functions, let’s try to understand what is happening in our case, we will start with our original script, and we will explain it step by step:

```
['1', '7', '11'].map(parseInt);
```

As we know the `callback` for the `map` function will receive 3 arguments, so let’s do that:

```
['1', '7', '11'].map((currentValue, index, array) => parseInt(currentValue, index, array));
```

Starting to get an idea of what happened? When we add the arguments, it comes clear that the `parseInt` function is receiving additional parameters and not only the actual value of the item in the array, so now we can take test what the function would do for each of these value combinations, but we can also ignore the array parameter as it will be discarded by the `parseInt` function:

```
parseInt('1', 0)
1
```

```
parseInt('7', 1)
NaN
```

```
parseInt('11', 2)
3
```

So that now explains the values we saw initially, the `parseInt` function result is being altered by the `redix` parameter which determines the base for the conversion.

### Is there a way to get the originally expected result?

Now know how it works, we can easily fix our script and get the desired result:

```
['1', '7', '11'].map((currentValue) => parseInt(currentValue));
> (3) [1, 7, 11]
```

---

## Scenario #2: (‘b'+'a'+ + ‘a’ + ‘a’).toLowerCase() === ‘banana’

You may be thinking that the expression above is false, after all, there are is no letter ‘n’ in the string we are building on the left side of the expression, or isn’t it? Let’s find out:

```
('b'+'a'+ + 'a' + 'a').toLowerCase() === 'banana'
true
```

Ok, you probably realized already what is going on, but if not let me quickly explain it here. Let’s focus on the left side of the expression, there’s nothing weird on the right side, believe me.

```
('b'+'a'+ + 'a' + 'a').toLowerCase()
"banana"
```

Interestingly enough we are forming the word ‘banana’, so the issue seems in here, let’s remove the lower case conversion and see what happens:

```
('b'+'a'+ + 'a' + 'a')
"baNaNa"
```

Bingo! We found some ‘N’ now, and looks like we actually found a `NaN` inside the string, perhaps it’s coming from the `+ +` expression, let’s pretend that and see what we would get:

```
b + a + NaN + a + a
```

Not quite good, we have an extra `a`, so let’s try something else:

```
+ + 'a'
NaN
```

Ahh there we go… the `+ +` operation by itself is not evaluating, but when we add the character ‘a’ at the end, it all goes into `NaN`, and now fits into our code. The `NaN` expression is then concatenated as a string with the rest of the text, and we finally get `banana`. Pretty weird!

---

## Scenario #3: Can’t even name it

```
(![] + [])[+[]] +
  (![] + [])[+!+[]] +
  ([![]] + [][[]])[+!+[] + [+[]]] +
  (![] + [])[!+[] + !+[]] === 'fail'
```

What in the world? How does a bunch of brackets form the word fail? And believe me, JS is not failing, we are actually getting the string `fail` as the output.

Let’s try to explain it, there are a few things in that bunch that form a pattern:

```
(![] + [])
```

That pattern evaluates to the string `false`, which is strange, but its a property of the language, turns out that `false + [] === 'false'`, this transformation has to do with how JS internally map the internal calls, we won’t get into the detail as to why this exactly happens.

Once you form the string `false` the rest is easy, just look for the positions of the letters that you need, except for one case, the letter `i` which is not part of the word `false`.

For that the original expression changed a bit, let’s look at it `([![]] + [][[]])` which evaluates to the string `falseundefined`. So basically we force an undefined value and concatenate it to the `false` string we know how to get, and the rest is history.

Loving it so far? Let’s do some more.

---

## Scenario #4: To be truthy or to be true, that is the question.

> To be truthy or to be true, that is the question.
> To be falsy or to be false, that is the question.

### What is truthy and falsy? and why are they different from true or false?

Every value in JavaScript as its own boolean value (truthy/falsy), these values are used in operations where a boolean is expected but not given. Very likely you at least once did something like this:

```
const array = [];
if (array) {
  console.log('Truthy!');
}
```

In the code above, `array` is not a boolean even though the value is “truthy” and the expression will result in executing the `console.log` below.

### How do I know what is truthy and what is falsy?

Everything that is not falsy is truthy. Terrible explanation? fair enough, let’s examine it further.

Falsy are values with an inherit boolean `false`, values like:

- 0
- -0
- 0n
- '’ or "”
- null
- undefined
- NaN

Everything else would be truthy.

---

## Scenario #5: Array equality

Some things in JS are simply weird, it’s the way the language is design, and we accept it the way it is. Let’s see some weird array equalities:

```
[] == ''   // -> true
[] == 0    // -> true
[''] == '' // -> true
[0] == 0   // -> true
[0] == ''  // -> false
[''] == 0  // -> true

[null] == ''      // true
[null] == 0       // true
[undefined] == '' // true
[undefined] == 0  // true

[[]] == 0  // true
[[]] == '' // true

[[[[[[]]]]]] == '' // true
[[[[[[]]]]]] == 0  // true

[[[[[[ null ]]]]]] == 0  // true
[[[[[[ null ]]]]]] == '' // true

[[[[[[ undefined ]]]]]] == 0  // true
[[[[[[ undefined ]]]]]] == '' // true
```

If you are interested in why? you can read it in section [7.2.13 Abstract Equality Comparison](https://www.ecma-international.org/ecma-262/#sec-abstract-equality-comparison) of the specification. Though I have to warn you, it’s not for normal human beings :p.

---

## Scenario #6: Math is Math, unless….

In our real-world we know that math is math, and we know how it works, we were taught since kids how to add numbers, and that always if you sum the same numbers you will get the result, right? Well… for JavaScript this is not always true… or kind of… let’s see it:

```
3  - 1  // -> 2
 3  + 1  // -> 4
'3' - 1  // -> 2
'3' + 1  // -> '31'

'' + '' // -> ''
[] + [] // -> ''
{} + [] // -> 0
[] + {} // -> '[object Object]'
{} + {} // -> '[object Object][object Object]'

'222' - -'111' // -> 333

[4] * [4]       // -> 16
[] * []         // -> 0
[4, 4] * [4, 4] // NaN
```

Initially, all started good, until we got to:

```
'3' - 1  // -> 2
'3' + 1  // -> '31'
```

When we subtracted, the string and the number interacted as numbers, but during the addition, both acted as a string, why? Well… it’s designed that way, but there’s a simple table that will help you understand what JavaScript would do in each case:

```
Number  + Number  -> addition
Boolean + Number  -> addition
Boolean + Boolean -> addition
Number  + String  -> concatenation
String  + Boolean -> concatenation
String  + String  -> concatenation
```

What about the other examples? A `ToPrimitive`  and `ToString`  methods are being implicitly called for `[]`  and `{}`  before addition. Read more about evaluation process in the specification:

Notably, `{} + []` here is the exception. The reason why it differs from `[] + {}` is that, without parenthesis, it is interpreted as a code block and then a unary +, converting `[]` into a number. It sees the following:

```
{
  // a code block here
}
+[]; // -> 0
```

To get the same output as `[] + {}` we can wrap it in parenthesis.

```
({} + []); // -> [object Object]
```

---

## Conclusion

I hope you enjoy this post as much as I enjoyed writing it. JavaScript is an amazing language, full of tricks and weirdness, and I hope this article brings you some clarity into some of these interesting topics and that next time you encounter something like this, you know what exactly what is happening.

There are more situations under which JS can be very weird, and I can probably do more posts like these in the future if you all like it.

Thanks so much for reading!
