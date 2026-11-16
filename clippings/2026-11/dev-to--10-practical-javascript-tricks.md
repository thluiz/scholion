---
url: "https://dev.to/zandershirley/10-practical-javascript-tricks-2b7h"
captured_at: "2026-11-16T01:17:51+00:00"
title: "10 Practical JavaScript Tricks"
domain: "dev-to"
---

I'm always on the lookout for new ways to be more efficient.

And JavaScript is always full of pleasant surprises.

### [](#1-transform-the-arguments-object-into-an-array)**1\. Transform the arguments object into an array.**

The **arguments** object is an Array-like object accessible inside functions that contains the values of the arguments passed to that function.

But it's not like other arrays, we can access the values and we can get the length, but no other array methods can be used on it.

Luckily, we can just convert it into a regular array:  

```
var argArray = Array.prototype.slice.call(arguments);
```

### [](#2-sum-all-the-values-from-an-array)**2\. Sum all the values from an array.**

My initial instinct was to use a loop, but that would have been wasteful.  

```
var numbers = [3, 5, 7, 2];
var sum = numbers.reduce((x, y) => x + y);
console.log(sum); // returns 17
```

### [](#3-short-circuit-conditionals)**3\. Short circuit conditionals.**

We have the following code:  

```
if (hungry) {
    goToFridge();
}
```

We can make it even shorter by using the variable with the function:  

```
hungry && goToFridge()
```

### [](#4-use-logical-or-for-conditions)**4\. Use logical OR for conditions.**

I used to declare my variables at the start of my function just to avoid getting _undefined_ if anything went unexpectedly wrong.  

```
function doSomething(arg1){ 
    arg1 = arg1 || 32; // if it's not already set, arg1 will have 32 as a default value
}
```

### [](#5-comma-operator)**5\. Comma operator.**

The comma operator (,) evaluates each of its operands (from left to right) and returns the value of the last operand.  

```
let x = 1;

x = (x++, x);

console.log(x);
// expected output: 2

x = (2, 3);

console.log(x);
// expected output: 3
```

### [](#6-using-length-to-resize-an-array)**6\. Using length to resize an array.**

You can either resize or empty an array.  

```
var array = [11, 12, 13, 14, 15];  
console.log(array.length); // 5  

array.length = 3;  
console.log(array.length); // 3  
console.log(array); // [11,12,13]

array.length = 0;  
console.log(array.length); // 0  
console.log(array); // []
```

### [](#7-swap-values-with-array-destructuring)**7\. Swap values with array destructuring.**

The destructuring assignment syntax is a JavaScript expression that makes it possible to unpack values from arrays, or properties from objects, into distinct variables.  

```
let a = 1, b = 2
[a, b] = [b, a]
console.log(a) // -> 2
console.log(b) // -> 1
```

### [](#8-shuffle-elements-from-array)**8\. Shuffle elements from array.**

_Every day I'm shufflin'_  
_Shufflin', shufflin'_  

```
var list = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(list.sort(function() {
    return Math.random() - 0.5
})); 
// [4, 8, 2, 9, 1, 3, 6, 5, 7]
```

### [](#9-property-names-can-be-dynamic)**9\. Property names can be dynamic.**

You can assign a dynamic property before declaring the object.  

```
const dynamic = 'color';
var item = {
    brand: 'Ford',
    [dynamic]: 'Blue'
}
console.log(item); 
// { brand: "Ford", color: "Blue" }
```

### [](#10-filtering-for-unique-values)**10\. Filtering for unique values.**

For all you ES6 fans out there, we can create a new array containing only the unique values by using the Set object with the Spread operator.  

```
const my_array = [1, 2, 2, 3, 3, 4, 5, 5]
const unique_array = [...new Set(my_array)];
console.log(unique_array); // [1, 2, 3, 4, 5]
```

### [](#closing-thoughts)**Closing thoughts.**

Being responsible is far more important than being efficient.

Your website NEEDS to work in all browsers.

You can use [Endtest](https://endtest.io/) or other similar tools to make sure it does.

What about you? Do you have any JavaScript tips or tricks to share?
