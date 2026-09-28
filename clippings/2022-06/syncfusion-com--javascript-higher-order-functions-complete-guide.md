---
url: "https://www.syncfusion.com/blogs/post/javascript-higher-order-functions-a-complete-guide.aspx"
captured_at: "2022-06-02T09:55:07-03:00"
title: "JavaScript Higher-Order Functions: A Complete Guide | Syncfusion Blogs"
domain: "syncfusion-com"
---

# JavaScript Higher-Order Functions: A Complete Guide

A function is a reusable piece of code designed to avoid repetitive code and improve code quality. As a functional programming language, JavaScript uses higher-order functions to implement this abstraction at an even higher level.

This article will guide you through the concept of higher-order functions in JavaScript along with their usage. However, to fully understand the underlying principles of higher-order functions, let’s first understand the concept of functional programming.

## Functional programming

JavaScript is a multiparadigm language. Functional programming is just one of the many programming paradigms it supports.

In a nutshell, functional programming helps us to handle pure mathematical functions. It also enables programmers to construct and structure code using functions.

Since functions are considered first-class citizens in functional programming, JavaScript is able to implement higher-order functions.

## Functions as first-class citizens

JavaScript treats functions as **first-class citizens**, enabling functions to operate similarly to any other data type such as strings, arrays, objects, and so on.

These are some of the operations that can be performed on functions when treated as first-class citizens:

- Assign them to a variable.
- Set them as object properties.
- Store them in arrays.
- Use them as an argument to a function or as a return from a function.

Here’s the exciting part:*The* *exact* *definition of* ***higher-order functions** has been mentioned above in the fourth operation**!*

As you can see, higher-order functions are only possible because functions are considered first-class citizens in functional programming.

Now that we have covered the underlying concepts of JavaScript that enable us to implement higher-order functions, let’s dive into the main topic of this article.

## Higher-order functions

As mentioned in the previous section, higher-order functions operate on other functions by taking them as arguments, returning them from a function, or both.

Let’s see some examples of each case to understand it better.

### Functions that take other functions as arguments

```
//Pass function as an argument to another function//array of names to be used in the functionconst names=['John','Tina','Kale','Max']//Function using function fn as a parameterfunction useFunction(arr,fn){for(let i=0; i<arr.length; i++){
    fn(arr[I]);}}//Function that is being used as a parameterfunction argFn (name){
  console.log("Hello "+ name );}//calling useFunction() with argFn() as a parameter
useFunction(names,argFn);/*Result printed:
   Hello John
   Hello Tina
   Hello Kale
   Hello Max
*/
```

In the above program, **useFunction()** is a higher-order function that takes the function **fn()** as an argument and manipulates the elements of an array according to **fn()**.

### Functions that return other functions

```
// Return function from function//array of names to be used in the functionconst names=['John','Tina','Kale','Max']//Function returning secondFunction()function returnFunction(arr){//returnFunction() returns the secondFunction() which needs the argument yreturnfunction secondFunction(y){ 
      console.log("First argument is an array: "+ arr);
      console.log("Argument passed to secondFunction is "+ y );};}//secondFunction() is assigned to myFuncconst myFunc = returnFunction(names);//"a string." is passed as the y variable to secondFunction()
myFunc("a string.");/*Result printed:
  First argument is an array: John,Tina,Kale,Max.
  Argument passed to secondFunction is a string.
*///You can also pass both variables as below.
returnFunction(names)("a string.");
```

The function **returnFunction()** in the above code snippet is a higher-order function because it returns the function **secondFunction()** which requires another parameter **y**.

### Functions that take other functions as arguments and return functions

Consider the small program below that modifies an array and prints the modified array along with an argument given to the inner function.

```
// Uses a function as a parameter and returns a function from a function//array of names to be used in the functionconst names=['John','Tina','Kale','Max']//Function using a function as a parameter and returns a functionfunction useReturnFunc(arr,fn){//modify the array using the parameter 
  fnfor(let i =0; i < arr.length; i++){
        arr[i]= fn(arr[i]);}//useReturnFunc() returns the secondFunction() which needs the argument 
  yreturn 
  function secondFunction(y){
     console.log("First argument is an array: "+ arr);
     console.log("Argument passed to secondFunction is "+ y );};}//Function that is being used as a parameterfunction argFn (name){return("Hello "+ name );}

useReturnFunc(names,argFn)("a string.");/*Result printed:
  Array modified by fn parameter: Hello John, Hello Tina, Hello Kale, Hello Max.
  Argument passed to secondFunction is a string.
*/
```

In the above program, **useReturnFunc()** is a higher-order function that uses a function **fn()** as a parameter and returns a function called **secondFunction()**.

## Higher-order functions to abstract over actions

Higher-order functions can also abstract over actions apart from implementing abstraction on values.

The following are some use cases where we can implement abstraction over actions.

### Functions to create new functions

```
//Use higher-order function to create a new function//Array of integers that needs to be filteredconst intArr =[3,10,25,1,7]//filterArr() returns a function greaterThan(m)//which filters the array elements that are greater than parameter mfunction filterArr(arr){const newArray =[];returnfunction greaterThan(m){for(let i=0; i<arr.length; i++){if(arr[i]> m){
          newArray.push(arr[i]);}}
     console.log("Elements that are greater than m = "+ m +" are: "+ newArray);}}

filterArr(intArr)(9);/*Result printed:
  Elements that are greater than m = 9 are: 10,25
*/
```

In the above example, the higher-order function **filterArr()** is used to create and return a second function **greaterThan()**, which filters array elements greater than the parameter **m**.

### Functions to change functions

```
//Use higher-order function to change a function//Array of integers that's used as an argumentconst intArr =[3,10,25,1,7]//changeFn() takes in Math.min function //and provides the arguments for the function laterfunction changeFn(f){returnfunction getArr(arr){let result = f(...arr);
    console.log("Called with", arr,", returned", result);return result;};}//change Math.min function using changeFn
changeFn(Math.min)(intArr);/* Resutl printed:
   Called with [ 3, 10, 25, 7 ] , returned 1
*/
```

The higher-order function **changeFn()** takes a function as a parameter and provides the necessary parameters to it separately using the return function **getArr()**.

### Functions to provide new control flows

```
//Use higher-order function to provide a new control flow//Array of integers that's used as an argumentconst intArr =[3,10,25,2,7]//Higher-order function 1: //  customForEach takes a function as an argumentfunction customForEach(arr,fn){for(let i=0; i<arr.length; i++){
     fn(arr[i]%2==0,()=>{
         console.log(arr[i],"is even");});}}/*Higher-order function 2: 
  unless() function takes the function then() as an argument 
  and performs a control flow operation
*/functionunless(test,then){if(test)then();}
  
customForEach(intArr,unless);/*
Result printed:
  10 is even
  2 is even

*/
```

The above example demonstrates how the higher-order function **unless()** is used to provide a new control flow depending on a test condition given by the user.

## Built-in higher-order functions in JavaScript

Many of the built-in JavaScript functions on arrays, strings, DOM methods, promise methods, etc. are higher-order functions that provide a significant level of abstraction.

Listed below are a few of the many built-in higher-order functions:

- **Array.prototype.map()**
- **Array.prototype.filter()**
- **Array.prototype.reduce()**
- **Array.prototype.forEach()**
- **EventTarget.addEventListener()**

## Benefits of higher-order functions

- They are an excellent way to abstract and separate actions in a program.
- They are easy to reuse.
- They provide simplicity to the code, allowing the programmer and any other party to understand the code at a high level easily.
- They make it less time-consuming to write fully functioning and clear code as it’s easier to debug when higher-order functions are used.
- Also, they help write compressed and composed code when programs get more complex.

## Conclusion

Higher-order functions are a beneficial feature of JavaScript. They enhance the functionalities of ordinary functions and let us communicate code through actions, increasing its reusability and abstraction.

Developers can either use the built-in higher-order functions provided in JavaScript libraries or create their own to write composed and complex functions according to their requirements.

Syncfusion [Essential JS 2](https://www.syncfusion.com/javascript-ui-controls "Essential JS 2 UI controls") is the only suite you will ever need to build an app. It contains over 65 high-performance, lightweight, modular, and responsive UI components in a single package. Download a [free trial](https://www.syncfusion.com/downloads/essential-js2 "Free evaluation of the Syncfusion Essential Studio") to evaluate the controls today.

If you have any questions or comments, you can also contact us through our [support forums](https://www.syncfusion.com/forums "Syncfusion support forum"), [support portal](https://support.syncfusion.com/ "Syncfusion support portal"), or [feedback portal](https://www.syncfusion.com/feedback/ "Syncfusion Feedback Portal"). We are always happy to assist you!

## Related blogs
