---
url: "https://dev.to/samanthaming/extract-functions-arguments-using-destructure-in-javascript-169k"
captured_at: "2020-09-07T16:47:30-03:00"
title: "Extract Functions Arguments using Destructure in JavaScript - DEV Community 👩‍💻👨‍💻"
domain: "dev-to"
---

# Extract Functions Arguments using Destructure in JavaScript

ES6 Destructuring is terrific at extracting value from your arguments. So the next time you see the array bracket notation, just swap them out and use the destructuring syntax instead

```
function omelette(...args) {
  // ❌ Old Way
  const egg = args[0];
  const cheese = args[1];

  // ✅ Better Way with Destructuring
  const [egg, cheese] = args;
}

omelette('', '');
```

## Breaking down the code

The first thing we’re doing is collecting all our arguments into an array.

```
// Step 1:
(...args)

args // [ '', '' ]
```

Next, we’re assigning them to our variables using array destructuring.

```
// Step 2:
const [egg, cheese] = args;

egg; // ''
cheese; // ''
```

## Understanding the `arguments` Object

There's been some confusion on the syntax. I think it's because of the arguments objects. So I'm going to try to explain it. In every function, there is a built-in `arguments` object. The `arguments` object is an Array-like object that corresponds to the arguments passed into a function.

```
function omelette() {
  console.log(arguments); // { 0: '', 1: '' }
}

omelette('', '');
```

☝️As you can see the `arguments` is not an array. It is an Array-like object. To convert this into a real array, I can use the `...` spread syntax.

```
function omelette() {
  var args = [...arguments];
  console.log(args); // [ '', ''  ]
}

omelette('', '');
```

Notice my function is NOT accepting any parameters, yet my `arguments` object exists. I know it's confusing cause I named it `args`. So let's make it crystal clear and check out a function that is passing in a parameter vs the `arguments` object.

```
function food(egg) {
  egg; // ''
  arguments; // { 0: '', 1: '' }
}

food('', '');
```

## The term Parameter vs Argument

I always thought these terms were interchangeable. Then I realize there is a language difference.

**Parameter**: is the variable in the function declaration. It is part of the function signature when you create it.

To use in a sentence, I'd say: "This function is accepting the `name` parameter"

```
function sayHi(name) {
  //  parameter
}
```

**Argument**: is the actual value of the variable being passed to the function when it is called.

To use in a sentence, I'd say: "I'm passing `samantha` in this function"

```
sayHi('samantha'); //  argument
```

Here's how I remember it. The "P" in Parameter stands for the **P**laceholder in the function declaration. The "A" in Argument stands for the the **A**ctual value of the function.

## Rest Parameters vs Arguments object

Let's start by explaining what are Rest Parameters:

> The rest parameter syntax allows us to represent an indefinite number of arguments as an array.

*[MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)*

Rest Parameters collects individual arguments that you pass into a function and returns an array

```
function cook(...ingredients) { //  Have to accept the parameters
  return ingredients;
  // [ '', '' ]  Returns an array
}

cook('', ''); //  Passing the arguments
```

However, this is different from the `arguments` object. Notice I didn't have to pass the arguments in the parameters. Every non-arrow function created in JavaScript has a local `arguments` object. It's also the reason, why you don't want to name using `arguments` because you will overwrite it.

```
function cook() { //  NOT accepting any parameters
  return arguments;
  // { '0': '', '1': '' }  Returns an "arguments" object
}

cook('', ''); //  Passing the arguments
```

The best practice is to avoid the `arguments` object, instead you should use the **rest parameters**. It's the reason why ES6 introduced the Rest Parameters to make it easier for JavaScript developers that need to access and make it easier to work with an indefinite number of arguments

## Arguments best practices

There are some best practices of using Function Arguments that was indicated from [AirBnb's JavaScript Style Guide](https://github.com/airbnb/javascript#functions--arguments-shadow):

> Never name a parameter arguments. This will take precedence over the arguments object that is given to every function scope.

```
// bad
function foo(name, options, arguments) {
  // ...
}

// good
function foo(name, options, args) {
  // ...
}
```

> Never use arguments, opt to use rest syntax ... instead

Why? `...` is explicit about which arguments you want pulled. Plus, rest arguments are a real Array, and not merely Array-like like arguments.

```
// bad
function foo() {
  const args = Array.prototype.slice.call(arguments);
}

// good
function foo(...args) {
}
```

## Community Input

**Setting Default Value**

*[@lukeshiru](https://twitter.com/lukeshiru/status/1241474994170769409?s=21):* You can even set default values in the header.

```
function omelette(...[egg = '', cheese = '']) {
  egg; // ''
  cheese; // ''
}

omelette(); //  NOT passing any value
```

**Destructuring Rest Parameters**

*[@lukeshiru](https://twitter.com/lukeshiru/status/1241474742680346624?s=20):* You can also do it like this.

```
function omelette(...[egg, cheese]) {
  egg; // ''
  cheese; // ''
}

omelette('', '');
```

☝️ Let me just break down what [@lukeshiru](https://dev.to/lukeshiru)
is doing here cause it might look at bit funky at first glance. This is the same as doing this:

```
// Step 1: using the rest parameter to collect the arguments
function omelette(...args) {
  args; // ['', '']

  // Step 2: extract the value using destructuring
  const [egg, cheese] = args;
}
```

I did the above in 2 steps, but I could also combine all the steps into one:

```
// "..." --> reflects the rest parameter
// "[egg, cheese]" --> reflects the destructuring
function omelette(...[egg, cheese]) {
  egg; // ''
  cheese; // ''
}
```

## Resources

---

**Thanks for reading ❤**  
Say Hello! [Instagram](https://www.instagram.com/samanthaming/) | [Twitter](https://twitter.com/samantha_ming) | [SamanthaMing.com](https://www.samanthaming.com/)
