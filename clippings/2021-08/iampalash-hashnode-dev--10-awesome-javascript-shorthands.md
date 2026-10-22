---
url: "https://iampalash.hashnode.dev/10-awesome-javascript-shorthands?source=newsletter"
captured_at: "2021-08-01T17:21:51-03:00"
title: "🔥 10 Awesome JavaScript Shorthands"
domain: "iampalash-hashnode-dev"
---

# 10 Awesome JavaScript Shorthands

Listen to this article

Hi everyone

Today I wanted to share with you 10 awesome **JavaScript** shorthands that will increase your speed by helping you to write less code and do more.

Let's start!

### 1. Merge Arrays

#### Longhand:

We usually merge two arrays using Array `concat()` method. The `concat()` method is used to merge two or more arrays. This method does not change the existing arrays but instead returns a new array. Here is a simple example:

```
let apples = ['', ''];
let fruits = ['', '', ''].concat(apples);

console.log( fruits );
//=> ["", "", "", "", ""]
```

#### Shorthand:

We can shorten this a bit by using ES6 Spread Operator (`...`) like this:

```
let apples = ['', ''];
let fruits = ['', '', '', ...apples];  // <-- here

console.log( fruits );
//=> ["", "", "", "", ""]
```

and we are still getting the same output as before.

---

### 2. Merge Arrays (*but at the start*)

#### Longhand:

Let's say we want to add all the items from the `apples` array at the start of `fruits` array, instead of at the end like we have seen in the last example. We can do this using [`Array.prototype.unshift()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift) like this:

```
let apples = ['', ''];
let fruits = ['', '', ''];

// Add all items from apples onto fruits at start
Array.prototype.unshift.apply(fruits, apples)

console.log( fruits );
//=> ["", "", "", "", ""]
```

Now the two red & green apples are at the start instead of the end after merging.

#### Shorthand:

We can shorten this long code again using ES6 Spread Operator (`...`) like this:

```
let apples = ['', ''];
let fruits = [...apples, '', '', ''];  // <-- here

console.log( fruits );
//=> ["", "", "", "", ""]
```

---

### 3. Clone Array

#### Longhand:

We can easily clone an array using the Array [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice) method like this:

```
let fruits = ['', '', '', ''];
let cloneFruits = fruits.slice();

console.log( cloneFruits );
//=> ["", "", "", ""]
```

#### Shorthand:

Using ES6 Spread Operator (`...`) we can clone an array like this:

```
let fruits = ['', '', '', ''];
let cloneFruits = [...fruits];  // <-- here

console.log( cloneFruits );
//=> ["", "", "", ""]
```

---

### 4. Destructuring Assignment

#### Longhand:

While working with arrays, we sometimes need to "unpack" arrays into a bunch of variables like this:

```
let apples = ['', ''];
let redApple = apples[0];
let greenApple = apples[1];

console.log( redApple );    //=> 
console.log( greenApple );  //=>
```

#### Shorthand:

We can achieve the same result in a single line using [Destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) like this:

```
let apples = ['', ''];
let [redApple, greenApple] = apples;  // <-- here

console.log( redApple );    //=> 
console.log( greenApple );  //=>
```

---

### 5. Template literals

#### Longhand:

Usually, when we have to add an expression to a string we do it like:

```
// Display name in between two strings
let name = 'Palash';
console.log('Hello, ' + name + '!');
//=> Hello, Palash!

// Add & Subtract two numbers
let num1 = 20;
let num2 = 10;
console.log('Sum = ' + (num1 + num2) + ' and Subtract = ' + (num1 - num2));
//=> Sum = 30 and Subtract = 10
```

#### Shorthand:

With [Template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) we can use backticks (`` ` `` ), which allow us to embed any expression into the string, by wrapping it in `${...}` like this:

```
// Display name in between two strings
let name = 'Palash';
console.log(`Hello, ${name}!`);  // <-- No need to use + var + anymore
//=> Hello, Palash!

// Add two numbers
let num1 = 20;
let num2 = 10;
console.log(`Sum = ${num1 + num2} and Subtract = ${num1 - num2}`);
//=> Sum = 30 and Subtract = 10
```

---

### 6. For Loop

#### Longhand:

Using the `for` loop we can loop through an array like this:

```
let fruits = ['', '', '', ''];

// Loop through each fruit
for (let index = 0; index < fruits.length; index++) { 
  console.log( fruits[index] );  // <-- get the fruit at current index
}

//=> 
//=> 
//=> 
//=>
```

#### Shorthand:

We can achieve the same result using the [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of) statement but with very little code like this:

```
let fruits = ['', '', '', ''];

// Using for...of statement 
for (let fruit of fruits) {
  console.log( fruit );
}

//=> 
//=> 
//=> 
//=>
```

---

### 7. Arrow Functions

#### Longhand:

To loop through an array we can also use Array [`forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach) method. But we have to write a bit more code, which is less than the most common `for` loop we have seen above, but still a bit more than the `for...of` statement :

```
let fruits = ['', '', '', ''];

// Using forEach method
fruits.forEach(function(fruit){
  console.log( fruit );
});

//=> 
//=> 
//=> 
//=>
```

#### Shorthand:

But with [Arrow function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) we can write the full loop code in a single line like this:

```
let fruits = ['', '', '', ''];
fruits.forEach(fruit => console.log( fruit ));  // <-- Magic ✨

//=> 
//=> 
//=> 
//=>
```

I mostly use `forEach` loop with arrow functions, but I wanted to show you both the shorthand for looping: `for...of` statement and `forEach` loop. So that you can use whichever code you like based on your preference.

---

### 8. Find an object in an array

#### Longhand:

To find an object in an array of objects by one of its properties, we usually use `for` loop like this:

```
let inventory = [
  {name: 'Bananas', quantity: 5},
  {name: 'Apples', quantity: 10},
  {name: 'Grapes', quantity: 2}
];

// Get the object with the name `Apples` inside the array
function getApples(arr, value) {
  for (let index = 0; index < arr.length; index++) {

    // Check the value of this object property `name` is same as 'Apples'
    if (arr[index].name === 'Apples') {  //=> 

      // A match was found, return this object
      return arr[index];
    }
  }
}

let result = getApples(inventory);
console.log( result )
//=> { name: "Apples", quantity: 10 }
```

#### Shorthand:

Wow! We have to write so much previously, to implement this logic. But with Array [`find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find#examples) method and arrow function `=>`, we can easily achieve this in one line like this:

```
// Get the object with the name `Apples` inside the array
function getApples(arr, value) {
  return arr.find(obj => obj.name === 'Apples');  // <-- here
}

let result = getApples(inventory);
console.log( result )
//=> { name: "Apples", quantity: 10 }
```

---

### 9. Convert String to Integer

#### Longhand:

The [`parseInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt) function is used to parse a string and return an integer:

```
let num = parseInt("10")

console.log( num )         //=> 10
console.log( typeof num )  //=> "number"
```

#### Shorthand:

We can achieve the same result by adding a `+` prefix before the string like this:

```
let num = +"10";

console.log( num )           //=> 10
console.log( typeof num )    //=> "number"
console.log( +"10" === 10 )  //=> true
```

---

### 10. Short-circuit Evaluation

#### Longhand:

Mostly `if-else` statement is used if we have to set a value based on another value is not a *falsy* value like this:

```
function getUserRole(role) {
  let userRole;

  // If role is not falsy value
  // set `userRole` as passed `role` value
  if (role) {
    userRole = role;
  } else {

    // else set the `userRole` as USER
    userRole = 'USER';
  }

  return userRole;
}

console.log( getUserRole() )         //=> "USER"
console.log( getUserRole('ADMIN') )  //=> "ADMIN"
```

#### Shorthand:

But using short-circuit evaluation (`||`), we can do this in one line like this:

```
function getUserRole(role) {
  return role || 'USER';  // <-- here
}

console.log( getUserRole() )         //=> "USER"
console.log( getUserRole('ADMIN') )  //=> "ADMIN"
```

Basically, `expression1 || expression2` is short-circuit evaluated to the truthy expression. So, it's like saying that if the first part is true don't bother evaluating the rest of the expression.

---

Finally, I would like to end this article by sharing one quote by [**Jeff Atwood**](https://blog.codinghorror.com/the-best-code-is-no-code-at-all/):

> Code is only our enemy because there are so many of us programmers writing so damn much of it. If you can’t get away with no code, the next best thing is to start with brevity.
>
> If you love writing code — really, truly love to write code — you’ll love it enough to write as little of it as possible.

If you liked this article, be sure to ❤ it.

## Happy Coding!
