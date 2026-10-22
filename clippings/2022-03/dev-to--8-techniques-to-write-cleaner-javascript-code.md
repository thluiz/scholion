---
url: "https://dev.to/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e"
captured_at: "2022-03-17T11:21:59-03:00"
title: "8 techniques to write cleaner JavaScript code - DEV Community 👩‍💻👨‍💻"
domain: "dev-to"
---

![2cab86auqek9wqzpv79e.png](dev-to--8-techniques-to-write-cleaner-javascript-code/ddfe48d5a22018179092e12c4b450d8e.png)

[![fd44bf4a-29f7-4769-85be-82205ec5ed06.jpeg](dev-to--8-techniques-to-write-cleaner-javascript-code/db382be8082e473c0f4b2da2f525e0c4.jpeg)](https://dev.to/codewithahsan)

[Muhammad Ahsan Ayaz](https://dev.to/codewithahsan)

Posted on Jan 2

# 8 techniques to write cleaner JavaScript code

[#javascript](https://dev.to/t/javascript)
[#webdev](https://dev.to/t/webdev)
[#node](https://dev.to/t/node)
[#beginners](https://dev.to/t/beginners)

I believe being a Software Engineer is just like being a Super Hero! And with great power, comes great responsibility. While writing code is an integral part of being a Software Engineer, just like estimations, brainstorming, writing unit tests are important aspects, writing clean code is really important as well.   
In this article, we're going to look at 8 different techniques to help you write cleaner JavaScript code.

> If you'd prefer watching a video instead, check this out:  
> [Video Tutorial](https://youtu.be/LTGcEIC2Tp8)

Now let's discuss each technique, one at a time.

## Pure Functions

A pure function is a function that always returns the same output, given the same input(s). It doesn't depend on any external variable apart from the inputs provided, nor it affects/changes any outside variable.  
Having pure functions makes it a lot easier for testing as they make testing super easy as you can always stub/mock the inputs and test your expected values. Let's see the following example

```
let name = "Peter Parker";
const splitName = () => {
  name = name.split(' ');
}
name = splitName();
console.log(name); // outputs [ 'Peter', 'Parker' ]
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='713'%3e%3ctitle data-evernote-id='714' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='715' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='716'%3e%3ctitle data-evernote-id='717' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='718' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

While the above code seems appropriate. It is not (lol). And that's because the `splitName` function depends on an outside variable named `name` and if someone else starts changing this variable, the function `splitName` starts providing a different output. Making it a non-pure function as we'd still be calling `splitName()` but the output is going to be different.

Let's change this to a pure function and let's see how that would look like:

```
let name = "Peter Parker";
const splitName = (nameString) => {
  return nameString.split(' ');
}
name = splitName(name);
console.log(name); // outputs [ 'Peter', 'Parker' ]
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='769'%3e%3ctitle data-evernote-id='770' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='771' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='772'%3e%3ctitle data-evernote-id='773' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='774' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

With the above change, the `splitName` is now a Pure Function because:

- It only relies on the input(s) (the `nameString` input).
- It doesn't change/re-assign any external variable

## Fewer or Named Parameters

When using functions, we often use positional parameters which have to be provided as they're declared with the function declaration. For example, in the call `arithmaticOp(num1, num2, operator)`, we can't provide the `operator` argument without providing `num1` and `num2`. And while this works for this example, for many functions, that'd become a problem.  
Consider the following example:

```
const createButton = (title, color, disabled, padding, margin, border, shadow)  => {
  console.log(title, color, disabled, padding, margin, border, shadow)
}
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='834'%3e%3ctitle data-evernote-id='835' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='836' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='837'%3e%3ctitle data-evernote-id='838' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='839' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

Looking at the above code, you can already see that in if we wanted to make any of the arguments optional (to use default values) while calling the `createButton` +, that'd be a disaster and might look something like this:

```
createButton('John Wick', undefined /* optional color */, true ,'2px....', undefined  /* optional margin*/);
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='866'%3e%3ctitle data-evernote-id='867' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='868' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='869'%3e%3ctitle data-evernote-id='870' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='871' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

You can see that the above statement doesn't look **Clean** at all. Also, it is hard to see from the function-calling statement which parameter corresponds to which argument of the function. So this is a practice we could follow:

- If we have 2 or fewer arguments, we can keep them as positional arguments
- Else, we provide an object with key-value pairs

Let's use this technique with the above example and see how it looks like:

```
const createButton = ({title, color, disabled, padding, margin, border, shadow})  => {
  console.log(title, color, disabled, padding, margin, border, shadow)
}

createButton({
  title: 'John Wick',
  disabled: true,
  shadow: '2px....'
});
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='941'%3e%3ctitle data-evernote-id='942' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='943' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='944'%3e%3ctitle data-evernote-id='945' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='946' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

Notice that the statement to call the `createButton` function is much cleaner now. And we can easily see which value in the key-value pair corresponds to the arguments for the functions. Yayy!

## Object / Array Destructuring

Consider the following javascript example in which we're taking some properties from an object and assigning to their individual variables:

```
const user = {
  name: 'Muhammad Ahsan',
  email: 'hi@codewithahsan.dev',
  designation: 'Software Architect',
  loves: 'The Code With Ahsan Community'
}

const name = user.name;
const email = user.email;
const loves = user.loves;
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='1007'%3e%3ctitle data-evernote-id='1008' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='1009' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='1010'%3e%3ctitle data-evernote-id='1011' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='1012' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

In the above example, it is much cringe to use the `user.*` notation so many times. This is where Object Destructuring comes in. We can change the above example as follows with Object Destructuring:

```
const user = {
  name: 'Muhammad Ahsan',
  email: 'hi@codewithahsan.dev',
  designation: 'Software Architect',
  loves: 'The Code With Ahsan Community'
}

const {name, email, loves} = user;
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='1060'%3e%3ctitle data-evernote-id='1061' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='1062' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='1063'%3e%3ctitle data-evernote-id='1064' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='1065' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

See! Much better. Right? Let's consider another example:

```
const getDetails = () => {
  return ['Muhammad Ahsan', 'hi@codewithahsan.dev', 'Some Street', 'Some City', 'Some Zip', 'Some Country'];
}

const details = getDetails();
const uName = details[0];
const uEmail = details[1];
const uAddress = `${details[2]}, ${details[3]}, ${details[4]}, ${details[5]}`;
const uFirstName = uName.split(' ')[0];
const uLastName = uName.split(' ')[1];
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='1180'%3e%3ctitle data-evernote-id='1181' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='1182' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='1183'%3e%3ctitle data-evernote-id='1184' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='1185' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

Ugh. I even hated the code writing the above example . Had to do it though. You can see that the code looks super weird and is hard to read. We can use Array Destructuring to write it a bit cleaner as follows:

```
const getDetails = () => {
  return ['Muhammad Ahsan', 'hi@codewithahsan.dev', 'Some Street', 'Some City', 'Some Zip', 'Some Country'];
}

const [uName, uEmail, ...uAddressArr] = getDetails();
const uAddress = uAddressArr.join(', ');
const [uFirstName, uLastName] = uName.split('');
console.log({
  uFirstName,
  uLastName,
  uEmail,
  uAddress
});
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='1274'%3e%3ctitle data-evernote-id='1275' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='1276' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='1277'%3e%3ctitle data-evernote-id='1278' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='1279' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

You can see how cleaner this is

## Avoid Hard-coded values

This is an issue that I often request changes for the Pull Requests I review. And is a no-go. Let's see an example:

```
/**
 * Some huge code
 * 
 * 
 * 
 * 
 * 
 */

setInterval(() => {
  // do something
}, 86400000);
// WHAT IS THIS 86400000 ???
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='1300'%3e%3ctitle data-evernote-id='1301' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='1302' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='1303'%3e%3ctitle data-evernote-id='1304' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='1305' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

Someone looking at the code would have no idea what this number stands for, how it was calculated and what's the business logic behind this. Instead of hardcoding this value, we could've created a constant as follows:

```
const DAY_IN_MILLISECONDS = 3600 * 24 * 1000; // 86400000

setInterval(() => {
  // do something
}, DAY_IN_MILLISECONDS);
// now this makes sense
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='1332'%3e%3ctitle data-evernote-id='1333' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='1334' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='1335'%3e%3ctitle data-evernote-id='1336' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='1337' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

Let's consider another example:

```
const createUser = (name, designation, type) => {
  console.log({name, designation, type});
}

createUser('Muhammad Ahsan', 'Software Architect', '1');
// WHAT IS this '1'?
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='1383'%3e%3ctitle data-evernote-id='1384' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='1385' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='1386'%3e%3ctitle data-evernote-id='1387' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='1388' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

Looking at the call for `createUser` method. It is really hard for someone reading the code to understand what this `'1'` stands for. I.e. what `type` of user this is. So instead of hard-coding the value `'1'` here, we could've created an Object mapping of the type of users we have as follows:

```
const USER_TYPES = {
  REGULAR_EMPLOYEE: '1'
}

const createUser = (name, designation, type) => {
  console.log({name, designation, type});
}

createUser('Muhammad Ahsan', 'Software Architect', USER_TYPES.REGULAR_EMPLOYEE);
// smoooooooth
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='1448'%3e%3ctitle data-evernote-id='1449' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='1450' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='1451'%3e%3ctitle data-evernote-id='1452' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='1453' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

## Avoid Short-hand variable names

Short-hand variables make sense where they're needed. Like if you've positional coordinates like `x` and `y`, that works. But if we create variables like `p`, `t`, `c` without having a context, it is really hard to read, trace and maintain such code. See this example for instance:

```
const t = 25;

let users = ['Muhammad Ahsan', 'Darainn Mukarram'];

users = users.map((user) => {
  /**
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   * 
   */

  return {
    ...user,
    tax: user.salary * t / 100 // WHAT IS `t` again? 
  }
})
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='1513'%3e%3ctitle data-evernote-id='1514' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='1515' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='1516'%3e%3ctitle data-evernote-id='1517' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='1518' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

The above examples shows that now the developer/reader has to scroll all the way up or go to the definition to try to understand what this variable is. Ergo NOT CLEAN CODE . This is also called mind-mapping the variables in which only the author knows what they mean. So instead of the short hand variable name, we could've given this a proper name as follows:

```
const taxFactor = 25;

let users = ['Muhammad Ahsan', 'Darainn Mukarram'];

users = users.map((user) => {
  // some code
  return {
    ...user,
    tax: user.salary * taxFactor / 100
  }
})
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='1570'%3e%3ctitle data-evernote-id='1571' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='1572' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='1573'%3e%3ctitle data-evernote-id='1574' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='1575' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

And now this makes much more sense.

## Set default Object values using Object.assign()

There might be cases where you'd want to create a new object from another object, providing some default value if the source object doesn't have them. Consider the following example:

```
const createButton = ({title, color, disabled, padding})  => {
  const button = {};
  button.color = color || '#333';
  button.disabled = disabled || false;
  button.title = title || '';
  button.padding = padding || 0;
  return button;
}

const buttonConfig = {
  title: 'Click me!',
  disabled: true
}

const newButton = createButton(buttonConfig);
console.log('newButton', newButton)
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='1673'%3e%3ctitle data-evernote-id='1674' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='1675' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='1676'%3e%3ctitle data-evernote-id='1677' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='1678' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

Instead of doing all that, we can use `Object.assign()` to override the default properties if provided by the source object as follows:

```
const createButton = (config)  => {
  return {
    ...{
      color: '#dcdcdc',
      disabled: false,
      title: '',
      padding: 0
    },
    ...config 
  };
}

const buttonConfig = {
  title: 'Click me!',
  disabled: true
}

const newButton = createButton(buttonConfig);
console.log('newButton', newButton)
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='1751'%3e%3ctitle data-evernote-id='1752' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='1753' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='1754'%3e%3ctitle data-evernote-id='1755' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='1756' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

## Use method chaining (especially for classes)

Method chaining is a technique that can be useful if we know the user of the class/object is going to use multiple functions together. You might have seen this with libraries like moment.js. Let's see an example:

```
class Player {
  constructor (name, score, position) {
    this.position = position;
    this.score = score;
    this.name = name;
  }
  setName(name) {
    this.name = name;
  }
  setPosition(position) {
    this.position = position;
  }
  setScore(score) {
    this.score = score;
  }
}

const player = new Player();
player.setScore(0);
player.setName('Ahsan');
player..setPosition([2, 0]);
console.log(player)
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='1868'%3e%3ctitle data-evernote-id='1869' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='1870' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='1871'%3e%3ctitle data-evernote-id='1872' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='1873' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

In the above code, you can see that we needed to call a bunch of functions together for the player. If this is the case for your object/class, use method chaining. And all you need to do is to return the object's instance from the functions you want to chain. The above example can be modified as follows to achieve this:

```
class Player {
  constructor (name, score, position) {
    this.position = position;
    this.score = score;
    this.name = name;
  }
  setName(name) {
    this.name = name;
    return this; // <-- THIS
  }
  setPosition(position) {
    this.position = position;
    return this; // <-- THIS
  }
  setScore(score) {
    this.score = score;
    return this; // <-- THIS
  }
}

const player = new Player();
player.setScore(0).setName('Ahsan').setPosition([2, 0]);
// SUPER COOL 
console.log(player)
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='1992'%3e%3ctitle data-evernote-id='1993' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='1994' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='1995'%3e%3ctitle data-evernote-id='1996' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='1997' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

## Use Promises over Callbacks

Promises have made our lives easier. We had something called callback hell a couple of years ago that made the code so hard to read. It looks something like this:

[![ssr9izx4571fazh655ej.png](dev-to--8-techniques-to-write-cleaner-javascript-code/b19f5eb0deeb2b1ece71b48700b4cdd4.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--D9C34L9R--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ssr9izx4571fazh655ej.png)

Even if I'm working with a library that has callbacks, I try to add a wrapper there that promisifies that (yeah, that's a term now). Let's consider the following example:

```
 const getSocials = (callback) => {
  setTimeout(() => {
      callback({socials: {youtube: 'youtube.com/CodeWithAhsan', twitter: '@codewith_ahsan'}});
    }, 1500);
}

const getBooks = (callback) => {
  setTimeout(() => {
    callback({books: ['Angular Cookbook']});
  }, 1500);
}

const getDesignation = (callback) => {
  setTimeout(() => {
    callback({designation: 'Software Architect'});
  }, 1500);
}

const getUser = (callback) => {
  setTimeout(() => {
    callback({user: 'Ahsan'});
  }, 1500);
}

 getUser(({user}) => {
    console.log('user retrieved', user)
    getDesignation(({designation}) => {
      console.log('designation retrieved', designation)
      getBooks(({books}) => {
        console.log('books retrieved', books)
        getSocials(({socials}) => {
          console.log('socials retrieved', socials)
        })
      })
    })
  })
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='2185'%3e%3ctitle data-evernote-id='2186' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='2187' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='2188'%3e%3ctitle data-evernote-id='2189' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='2190' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

All of the functions in the above code are asynchronous and they send back the data after 1.5 seconds. Now if there were 15 different functions involved, imagine what it would look like. Probably like the image I shared above . Instead of having this callback hell, we can promisify our functions and use promises as follows for better readability:

```
const getSocials = () => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve({socials: {youtube: 'youtube.com/CodeWithAhsan', twitter: '@codewith_ahsan'}});
    }, 1500);
  })

}

const getBooks = () => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve({books: ['Angular Cookbook']});
    }, 1500);
  })
}

const getDesignation = () => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve({designation: 'Software Architect'});
    }, 1500);
  })
}

const getUser = () => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve({user: 'Ahsan'});
    }, 1500);
  })
}

  getUser()
    .then(({user}) => {
      console.log('user retrieved', user);
      return getDesignation();
    })
    .then(({designation}) => {
      console.log('designation retrieved', designation)
      return getBooks();
    })
    .then(({books}) => {
      console.log('books retrieved', books);
      return getSocials();
    })
    .then(({socials}) => {
      console.log('socials retrieved', socials)
    })
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='2411'%3e%3ctitle data-evernote-id='2412' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='2413' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='2414'%3e%3ctitle data-evernote-id='2415' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='2416' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

You can see that the code already is much readable now as all the `.then()` statements are indented and show what data is retrieved in each `.then()` step. We can easily see the steps using this syntax as every `.then()` call returns the next function call along with its promise.

Now we can take it up a notch and make our code even more readable. How? By using `async await`. We'll modify our code as follows to achieve that:

```
const getSocials = () => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve({socials: {youtube: 'youtube.com/CodeWithAhsan', twitter: '@codewith_ahsan'}});
    }, 1500);
  })

}

const getBooks = () => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve({books: ['Angular Cookbook']});
    }, 1500);
  })
}

const getDesignation = () => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve({designation: 'Software Architect'});
    }, 1500);
  })
}

const getUser = () => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve({user: 'Ahsan'});
    }, 1500);
  })
}

const performTasks = async () => {
  const {user} = await getUser();
  console.log('user retrieved', user);

  const {designation} = await getDesignation();
  console.log('designation retrieved', designation);

  const {books} = await getBooks();
  console.log('books retrieved', books);

  const {socials} = await getSocials();
  console.log('socials retrieved', socials);
}
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='2429'%3e%3ctitle data-evernote-id='2430' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='2431' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='2432'%3e%3ctitle data-evernote-id='2433' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='2434' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

Notice that we wrapped our code inside the `performTasks()` function which is an `async` function as you can see the usage of the `async` keyword. And inside, we're making each function call using the `await` keyword which essentially would wait for the promise from the function to be resolved before executing the next line of code. And with this syntax, our code look as if it was all synchronous, however being asynchronous. And our code is a lot more cleaner

# Conclusion

I hope you enjoyed reading the article. If you did, make sure to hit like and bookmark. And check my [YouTube Channel](https://youtube.com/CodeWithAhsan) for more amazing content. And if you feel adventurous and are interested in taking your #Angular skills to the next level, check out my [Angular Cookbook](https://ahsanayaz.com/ng-book)

## Discussion (16)

![cc5f4526-0872-4ee6-b0b3-6dfaad5eccea.jpeg](dev-to--8-techniques-to-write-cleaner-javascript-code/2fe4e69336215c91df3a3dadf710cb6c.jpeg)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='a4rrq2t8gmtlmliu39uouu7h8gd4aknl' class='crayons-icon expanded js-evernote-checked' data-evernote-id='377'%3e%3ctitle id='a4rrq2t8gmtlmliu39uouu7h8gd4aknl' data-evernote-id='2482' class='js-evernote-checked'%3eCollapse%3c/title%3e %3cpath d='M12 10.677L8 6.935 9 6l3 2.807L15 6l1 .935-4 3.742zm0 4.517L9 18l-1-.935 4-3.742 4 3.742-1 .934-3-2.805z' data-evernote-id='2483' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='agehee10q61uxzwzojozvx6rq6saamym' class='crayons-icon collapsed js-evernote-checked' data-evernote-id='389'%3e%3ctitle id='agehee10q61uxzwzojozvx6rq6saamym' data-evernote-id='2484' class='js-evernote-checked'%3eExpand%3c/title%3e %3cpath d='M12 18l-4-3.771 1-.943 3 2.829 3-2.829 1 .943L12 18zm0-10.115l-3 2.829-1-.943L12 6l4 3.771-1 .942-3-2.828z' data-evernote-id='2485' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![7f4f85f0-8b26-45d9-a756-d169f0bf59cf.gif](dev-to--8-techniques-to-write-cleaner-javascript-code/dc2dc434c7a44bcdcc6a4c087d812047.gif)](https://dev.to/lukeshiru)

•
[Jan 3](https://dev.to/lukeshiru/comment/1l0e1)

Nice article, a few things to add:

- You can make this one even better:

```
const splitName = nameString => {
    return nameString.split(" ");
};
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='2548'%3e%3ctitle data-evernote-id='2549' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='2550' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='2551'%3e%3ctitle data-evernote-id='2552' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='2553' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

We just need to get rid of the block we are not using, and we can also make it curried so is more reusable. And instead of calling it `splitName`, we just call it what it is: `spaceSplit`:

```
const split = separator => string => string.split(separator);
const spaceSplit = split(" ");

spaceSplit("Peter Parker"); // ["Peter", "Parker"]
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='2592'%3e%3ctitle data-evernote-id='2593' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='2594' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='2595'%3e%3ctitle data-evernote-id='2596' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='2597' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

- You can use `Object.assign` when you want to actually update a newly created object that's more complex than a plain one, take this example:

```
const createElement = tagName => props =>
    Object.assign(document.createElement(tagName), props);
const createButton = createElement("button");

createButton({
    className: "btn",
    textContent: "Hello there!",
}); // <button class="btn">Hello there!</button>
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='2650'%3e%3ctitle data-evernote-id='2651' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='2652' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='2653'%3e%3ctitle data-evernote-id='2654' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='2655' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

- Instead of using chained methods, you could just pipe functions:

```
const set = property => value => object => ({
    ...object,
    [property]: value,
});

const setName = set("name");
const setPosition = set("position");
const setScore = set("score");

const pipe = functions => value =>
    functions.reduce((output, pipedFunction) => pipedFunction(output), value);

const player = pipe([setScore(0), setName("Ahsan"), setPosition([2, 0])])({});
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='2752'%3e%3ctitle data-evernote-id='2753' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='2754' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='2755'%3e%3ctitle data-evernote-id='2756' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='2757' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

With some luck we'll get the [pipe operator soon](https://github.com/tc39/proposal-pipeline-operator), and this will be even cleaner:

```
const player = setScore(0)({}) |> setName("Ahsan")(%) |> setPosition([2, 0])(%);
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='2791'%3e%3ctitle data-evernote-id='2792' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='2793' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='2794'%3e%3ctitle data-evernote-id='2795' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='2796' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

- Finally, the `async`/`await` solution can be also simplified without the need for `async`/`await`:

```
const delayed = timeout => value => () =>
    new Promise(resolve => setTimeout(() => resolve(value), timeout));

const delayed1500 = delayed(1500);

const getSocials = delayed1500({
    socials: {
        youtube: "youtube.com/CodeWithAhsan",
        twitter: "@codewith_ahsan",
    },
});
const getBooks = delayed1500({ books: ["Angular Cookbook"] });
const getDesignation = delayed1500({ designation: "Software Architect" });
const getUser = delayed1500({ user: "Ahsan" });

const log = prepend => log => console.log(prepend, log);

getUser()
    .then(log("user retrieved"))
    .then(getDesignation)
    .then(log("designation retrieved"))
    .then(getBooks)
    .then(log("books retrieved"))
    .then(getSocials)
    .then(log("socials retrieved"));
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='2963'%3e%3ctitle data-evernote-id='2964' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='2965' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='2966'%3e%3ctitle data-evernote-id='2967' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='2968' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

Cheers!

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' role='img' aria-labelledby='agb3y6hezv8vftvy89pm45mviozlruts' class='crayons-icon reaction-icon not-reacted js-evernote-checked' data-evernote-id='133'%3e%3ctitle id='agb3y6hezv8vftvy89pm45mviozlruts' data-evernote-id='2974' class='js-evernote-checked'%3eComment button%3c/title%3e%3cpath d='M10.5 5h3a6 6 0 110 12v2.625c-3.75-1.5-9-3.75-9-8.625a6 6 0 016-6zM12 15.5h1.5a4.501 4.501 0 001.722-8.657A4.5 4.5 0 0013.5 6.5h-3A4.5 4.5 0 006 11c0 2.707 1.846 4.475 6 6.36V15.5z' data-evernote-id='2975' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)
Reply](https://dev.to/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e#/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e/comments/new/1l0e1)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='a2dwss9tng4ihwcllzcobvvpi00yfmr1' class='crayons-icon expanded js-evernote-checked' data-evernote-id='378'%3e%3ctitle id='a2dwss9tng4ihwcllzcobvvpi00yfmr1' data-evernote-id='2977' class='js-evernote-checked'%3eCollapse%3c/title%3e %3cpath d='M12 10.677L8 6.935 9 6l3 2.807L15 6l1 .935-4 3.742zm0 4.517L9 18l-1-.935 4-3.742 4 3.742-1 .934-3-2.805z' data-evernote-id='2978' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='ad5e5hohux7mqwmi1vos31nd73b4vofh' class='crayons-icon collapsed js-evernote-checked' data-evernote-id='390'%3e%3ctitle id='ad5e5hohux7mqwmi1vos31nd73b4vofh' data-evernote-id='2979' class='js-evernote-checked'%3eExpand%3c/title%3e %3cpath d='M12 18l-4-3.771 1-.943 3 2.829 3-2.829 1 .943L12 18zm0-10.115l-3 2.829-1-.943L12 6l4 3.771-1 .942-3-2.828z' data-evernote-id='2980' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![c5134c54-cde5-4f4c-944c-d7d77124e2ab.jpeg](dev-to--8-techniques-to-write-cleaner-javascript-code/597d9b31b80d0ce80ef9042f66732c30.jpeg)](https://dev.to/romeerez)

•
[Jan 9](https://dev.to/romeerez/comment/1l576)

The article was about general advises, and you are suggesting a functional programming approach which is worth a separate article :)

The approach is tricky, leads to unclean code (what createElement does? creates a function!) so I wouldn't recommend it as a general advise

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' role='img' aria-labelledby='aqo5oiwwgre62a23d42ckbf6o9s4gs71' class='crayons-icon reaction-icon not-reacted js-evernote-checked' data-evernote-id='140'%3e%3ctitle id='aqo5oiwwgre62a23d42ckbf6o9s4gs71' data-evernote-id='3022' class='js-evernote-checked'%3eComment button%3c/title%3e%3cpath d='M10.5 5h3a6 6 0 110 12v2.625c-3.75-1.5-9-3.75-9-8.625a6 6 0 016-6zM12 15.5h1.5a4.501 4.501 0 001.722-8.657A4.5 4.5 0 0013.5 6.5h-3A4.5 4.5 0 006 11c0 2.707 1.846 4.475 6 6.36V15.5z' data-evernote-id='3023' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)
Reply](https://dev.to/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e#/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e/comments/new/1l576)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='a6jhpwtiedi8y0hk8v2by11567vj9a8y' class='crayons-icon expanded js-evernote-checked' data-evernote-id='379'%3e%3ctitle id='a6jhpwtiedi8y0hk8v2by11567vj9a8y' data-evernote-id='3025' class='js-evernote-checked'%3eCollapse%3c/title%3e %3cpath d='M12 10.677L8 6.935 9 6l3 2.807L15 6l1 .935-4 3.742zm0 4.517L9 18l-1-.935 4-3.742 4 3.742-1 .934-3-2.805z' data-evernote-id='3026' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='ajchx0knceq6b804dt2arvr6tbvt48pd' class='crayons-icon collapsed js-evernote-checked' data-evernote-id='391'%3e%3ctitle id='ajchx0knceq6b804dt2arvr6tbvt48pd' data-evernote-id='3027' class='js-evernote-checked'%3eExpand%3c/title%3e %3cpath d='M12 18l-4-3.771 1-.943 3 2.829 3-2.829 1 .943L12 18zm0-10.115l-3 2.829-1-.943L12 6l4 3.771-1 .942-3-2.828z' data-evernote-id='3028' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![7f4f85f0-8b26-45d9-a756-d169f0bf59cf.gif](dev-to--8-techniques-to-write-cleaner-javascript-code/dc2dc434c7a44bcdcc6a4c087d812047.gif)](https://dev.to/lukeshiru)

•
[Jan 9](https://dev.to/lukeshiru/comment/1l579)

You and me seem to have pretty different definitions of "unclean" .... you might want to take a look at [currying](https://wikipedia.org/wiki/Currying) ... and "unclean" libraries such as [ramda](https://ramdajs.com/)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='a84h61dagt7aalzfjhoole8j4wtekpwc' class='crayons-icon js-evernote-checked' data-evernote-id='3075'%3e%3ctitle id='a84h61dagt7aalzfjhoole8j4wtekpwc' data-evernote-id='3076' class='js-evernote-checked'%3eThread%3c/title%3e %3cpath d='M17 13l-5 6-5-6h3.125c0-3.314 2.798-6 6.25-6 .17 0 .34.006.506.02-1.787.904-3.006 2.705-3.006 4.78V13H17z' data-evernote-id='3077' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
Thread

[![c5134c54-cde5-4f4c-944c-d7d77124e2ab.jpeg](dev-to--8-techniques-to-write-cleaner-javascript-code/597d9b31b80d0ce80ef9042f66732c30.jpeg)](https://dev.to/romeerez)

•
[Jan 9
• Edited on Jan 9](https://dev.to/romeerez/comment/1l57g)

Guess what `isQueenOfSpades` contains in ramda docs? Guessing not works in here, in such way need to read source to know. While in normal JS where naming matters it is a boolean.

Is it clean? In common programming sense, name is given to describe what function or variable does, so in this way no, it's not clean. Functional programming has roots in math where naming doesn't matter, they are cool with formulas like [this one](https://stackoverflow.com/questions/12532552/what-part-of-hindley-milner-do-you-not-understand), but it's not right to expect your teammates will be happy of guessing how your `log` works.

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='a2ictwawyr6w4wjv3o8g2ratbj1rl72g' class='crayons-icon js-evernote-checked' data-evernote-id='3124'%3e%3ctitle id='a2ictwawyr6w4wjv3o8g2ratbj1rl72g' data-evernote-id='3125' class='js-evernote-checked'%3eThread%3c/title%3e %3cpath d='M17 13l-5 6-5-6h3.125c0-3.314 2.798-6 6.25-6 .17 0 .34.006.506.02-1.787.904-3.006 2.705-3.006 4.78V13H17z' data-evernote-id='3126' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
Thread

[![7f4f85f0-8b26-45d9-a756-d169f0bf59cf.gif](dev-to--8-techniques-to-write-cleaner-javascript-code/dc2dc434c7a44bcdcc6a4c087d812047.gif)](https://dev.to/lukeshiru)

•
[Jan 9
• Edited on Jan 9](https://dev.to/lukeshiru/comment/1l57l)

Let's go one thing at a time:

1. You don't need to read the source to understand a function, nowadays we have inline docs and typing systems.
2. Is it really hard for you to figure out what `isQueenOfSpades` does? Do you prefer the name to be `isAnObjectWhichContainsARankQAndASuitOfSpades` instead?
3. A name should hint what a function does, but you don't need to explain the entire implementation in the name.
4. If you're working with currying, you already know every function is an unary that returns a new function until you have all the arguments.
5. Programming has roots in binary and asm, and that doesn't have anything to do with the way we do things nowadays. I would never advocate for naming practices like the ones used in languages like Haskell, with single letters. Using Haskell to debate FP practices is like using ASM to justify that programming is hard to understand.
6. Nobody needs to "guess" how something works if it has good docs, types and a clear enough name.

Do you use libraries without knowing what the utils they provide will return, and relying only on the name? I imagine back in the day you had a really hard time with jQuery's `$.get` if that's the case. My teammates are perfectly fine with a `log` function, because when they use it they get autocompletion in their editors telling them the arguments that function takes, the thing it returns, and if they use it wrong they get a red squiggly underline to let them know, not to mention that if they hover over the function or the arguments, they get examples from the JSDocs

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='arh92a1ivf1b40t6uds7wuq119i5o3qo' class='crayons-icon js-evernote-checked' data-evernote-id='3184'%3e%3ctitle id='arh92a1ivf1b40t6uds7wuq119i5o3qo' data-evernote-id='3185' class='js-evernote-checked'%3eThread%3c/title%3e %3cpath d='M17 13l-5 6-5-6h3.125c0-3.314 2.798-6 6.25-6 .17 0 .34.006.506.02-1.787.904-3.006 2.705-3.006 4.78V13H17z' data-evernote-id='3186' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
Thread

[![c5134c54-cde5-4f4c-944c-d7d77124e2ab.jpeg](dev-to--8-techniques-to-write-cleaner-javascript-code/597d9b31b80d0ce80ef9042f66732c30.jpeg)](https://dev.to/romeerez)

•
[Jan 9
• Edited on Jan 9](https://dev.to/romeerez/comment/1l583)

Agree, makes sense now, I get used to rely on naming and I'm not hovering things at all, while in this practice programmer has to rely on hovering hint. I've tested and it works nicely, even in plain JS I got hint

```
log = (prepend: any) => (log: any) => void
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='3230'%3e%3ctitle data-evernote-id='3231' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='3232' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='3233'%3e%3ctitle data-evernote-id='3234' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='3235' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

Libraries is a different thing and only way is it read docs and memoize frequently used stuff.

$.get - jQuery was intended to do what document.querySelector does before it appeared, so I expect it to get element by selector. I honestly didn't check docs. But if it was ramda I would expect: get(key, object) and get(key)(object), but wrong, it's a 'prop' in ramda.

1 nowadays we have inline docs and typing systems.

So in general thanks for response, in editors it's not hard to get hints.

But not everywhere, while reviewing code in github it can give you hints as well, but far less intelligent and it won't work so nicely.

2 and 3 `isAnObjectWhichContainsARankQAndASuitOfSpades`

I would have a type Card = { rank: string, suite: string }

And a function `getIsCardAQueenOfSpaces`.

And now I can assign it to local variable `isQueenOfSpaces` and use it in imperative way

4 Makes sense, but it means whole project need to follow FP and currying to stay predictable, everyone in team must be good with FP and be on same page

> Do you use libraries without knowing what the utils they provide will return, and relying only on the name?

Yes, sure, other teammates may introduce libs which I never used and I'm reviewing the code, and usually it's understandable just by looking on name and usage

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' role='img' aria-labelledby='aajonqg53tbbjgzbivsyafsct3uxqvec' class='crayons-icon reaction-icon not-reacted js-evernote-checked' data-evernote-id='162'%3e%3ctitle id='aajonqg53tbbjgzbivsyafsct3uxqvec' data-evernote-id='3256' class='js-evernote-checked'%3eComment button%3c/title%3e%3cpath d='M10.5 5h3a6 6 0 110 12v2.625c-3.75-1.5-9-3.75-9-8.625a6 6 0 016-6zM12 15.5h1.5a4.501 4.501 0 001.722-8.657A4.5 4.5 0 0013.5 6.5h-3A4.5 4.5 0 006 11c0 2.707 1.846 4.475 6 6.36V15.5z' data-evernote-id='3257' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)
Reply](https://dev.to/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e#/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e/comments/new/1l583)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='abfcwgi0vebm23wyrrgtfuwwzklu5v14' class='crayons-icon expanded js-evernote-checked' data-evernote-id='380'%3e%3ctitle id='abfcwgi0vebm23wyrrgtfuwwzklu5v14' data-evernote-id='3259' class='js-evernote-checked'%3eCollapse%3c/title%3e %3cpath d='M12 10.677L8 6.935 9 6l3 2.807L15 6l1 .935-4 3.742zm0 4.517L9 18l-1-.935 4-3.742 4 3.742-1 .934-3-2.805z' data-evernote-id='3260' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='arj0p0h2mt0o82grmixvh20fctrhvla3' class='crayons-icon collapsed js-evernote-checked' data-evernote-id='392'%3e%3ctitle id='arj0p0h2mt0o82grmixvh20fctrhvla3' data-evernote-id='3261' class='js-evernote-checked'%3eExpand%3c/title%3e %3cpath d='M12 18l-4-3.771 1-.943 3 2.829 3-2.829 1 .943L12 18zm0-10.115l-3 2.829-1-.943L12 6l4 3.771-1 .942-3-2.828z' data-evernote-id='3262' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![fd44bf4a-29f7-4769-85be-82205ec5ed06.jpeg](dev-to--8-techniques-to-write-cleaner-javascript-code/db382be8082e473c0f4b2da2f525e0c4.jpeg)](https://dev.to/codewithahsan)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='a18f50fng0polg62646joatesp4hpa00' class='crayons-icon js-evernote-checked' data-evernote-id='3291'%3e%3ctitle id='a18f50fng0polg62646joatesp4hpa00' data-evernote-id='3292' class='js-evernote-checked'%3eAuthor%3c/title%3e %3cpath d='M12 8.25a6 6 0 110 12 6 6 0 010-12zm0 2.625l-.992 2.01-2.218.322 1.605 1.564-.379 2.21L12 15.937l1.984 1.043-.379-2.209 1.605-1.564-2.218-.323L12 10.875zm.75-6.376l3.75.001v2.25l-1.022.854a7.45 7.45 0 00-2.728-.817V4.5zm-1.5 0v2.288a7.451 7.451 0 00-2.727.816L7.5 6.75V4.5h3.75z' data-evernote-id='3293' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
Author

•
[Jan 4](https://dev.to/codewithahsan/comment/1l242)

[@lukeshiru](https://dev.to/lukeshiru) You're right. Thanks for the tips. I tried to keep things in this article (and the video). But yeah, once we get the pipe operator, things are going to be much more fun.

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' role='img' aria-labelledby='amw8rnoggfcft3zyyunzseq41wpz7tqv' class='crayons-icon reaction-icon not-reacted js-evernote-checked' data-evernote-id='169'%3e%3ctitle id='amw8rnoggfcft3zyyunzseq41wpz7tqv' data-evernote-id='3316' class='js-evernote-checked'%3eComment button%3c/title%3e%3cpath d='M10.5 5h3a6 6 0 110 12v2.625c-3.75-1.5-9-3.75-9-8.625a6 6 0 016-6zM12 15.5h1.5a4.501 4.501 0 001.722-8.657A4.5 4.5 0 0013.5 6.5h-3A4.5 4.5 0 006 11c0 2.707 1.846 4.475 6 6.36V15.5z' data-evernote-id='3317' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)
Reply](https://dev.to/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e#/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e/comments/new/1l242)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='ahn63w59uzd2msg70mtyco4goclnrblu' class='crayons-icon expanded js-evernote-checked' data-evernote-id='381'%3e%3ctitle id='ahn63w59uzd2msg70mtyco4goclnrblu' data-evernote-id='3319' class='js-evernote-checked'%3eCollapse%3c/title%3e %3cpath d='M12 10.677L8 6.935 9 6l3 2.807L15 6l1 .935-4 3.742zm0 4.517L9 18l-1-.935 4-3.742 4 3.742-1 .934-3-2.805z' data-evernote-id='3320' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='agdcexy35hfqt1lxgz9jsizu9heb2fr3' class='crayons-icon collapsed js-evernote-checked' data-evernote-id='393'%3e%3ctitle id='agdcexy35hfqt1lxgz9jsizu9heb2fr3' data-evernote-id='3321' class='js-evernote-checked'%3eExpand%3c/title%3e %3cpath d='M12 18l-4-3.771 1-.943 3 2.829 3-2.829 1 .943L12 18zm0-10.115l-3 2.829-1-.943L12 6l4 3.771-1 .942-3-2.828z' data-evernote-id='3322' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![c697abaf-3944-4838-a1ba-b9d8ced89a68.jpeg](dev-to--8-techniques-to-write-cleaner-javascript-code/e9d941d70c5171220c9db1d9ef7d9d97.jpeg)](https://dev.to/samantrags)

•
[Jan 3](https://dev.to/samantrags/comment/1l0mb)

Great writeup Muhammud .

Q: const DAY\_IN\_MILLISECONDS = 3600 \* 24 \* 1000; // 86400000  
isnt it better to put the breakup in comments to avoid the calculations being done every time ? Performance over ease of understanding

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' role='img' aria-labelledby='aqvyf2qdgqes2ocxj1l3kmocryr10cmq' class='crayons-icon reaction-icon not-reacted js-evernote-checked' data-evernote-id='176'%3e%3ctitle id='aqvyf2qdgqes2ocxj1l3kmocryr10cmq' data-evernote-id='3367' class='js-evernote-checked'%3eComment button%3c/title%3e%3cpath d='M10.5 5h3a6 6 0 110 12v2.625c-3.75-1.5-9-3.75-9-8.625a6 6 0 016-6zM12 15.5h1.5a4.501 4.501 0 001.722-8.657A4.5 4.5 0 0013.5 6.5h-3A4.5 4.5 0 006 11c0 2.707 1.846 4.475 6 6.36V15.5z' data-evernote-id='3368' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)
Reply](https://dev.to/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e#/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e/comments/new/1l0mb)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='ay8wgb15ffyifwzzly39hlrxdkvoar2' class='crayons-icon expanded js-evernote-checked' data-evernote-id='382'%3e%3ctitle id='ay8wgb15ffyifwzzly39hlrxdkvoar2' data-evernote-id='3370' class='js-evernote-checked'%3eCollapse%3c/title%3e %3cpath d='M12 10.677L8 6.935 9 6l3 2.807L15 6l1 .935-4 3.742zm0 4.517L9 18l-1-.935 4-3.742 4 3.742-1 .934-3-2.805z' data-evernote-id='3371' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='at5qtdmfhwq1ne83k6m5d7v3wggj9pm2' class='crayons-icon collapsed js-evernote-checked' data-evernote-id='394'%3e%3ctitle id='at5qtdmfhwq1ne83k6m5d7v3wggj9pm2' data-evernote-id='3372' class='js-evernote-checked'%3eExpand%3c/title%3e %3cpath d='M12 18l-4-3.771 1-.943 3 2.829 3-2.829 1 .943L12 18zm0-10.115l-3 2.829-1-.943L12 6l4 3.771-1 .942-3-2.828z' data-evernote-id='3373' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![fd44bf4a-29f7-4769-85be-82205ec5ed06.jpeg](dev-to--8-techniques-to-write-cleaner-javascript-code/db382be8082e473c0f4b2da2f525e0c4.jpeg)](https://dev.to/codewithahsan)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='aa8hg5f8wmkn0vn5cd7t0hguu1d24rwf' class='crayons-icon js-evernote-checked' data-evernote-id='3402'%3e%3ctitle id='aa8hg5f8wmkn0vn5cd7t0hguu1d24rwf' data-evernote-id='3403' class='js-evernote-checked'%3eAuthor%3c/title%3e %3cpath d='M12 8.25a6 6 0 110 12 6 6 0 010-12zm0 2.625l-.992 2.01-2.218.322 1.605 1.564-.379 2.21L12 15.937l1.984 1.043-.379-2.209 1.605-1.564-2.218-.323L12 10.875zm.75-6.376l3.75.001v2.25l-1.022.854a7.45 7.45 0 00-2.728-.817V4.5zm-1.5 0v2.288a7.451 7.451 0 00-2.727.816L7.5 6.75V4.5h3.75z' data-evernote-id='3404' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
Author

•
[Jan 4](https://dev.to/codewithahsan/comment/1l243)

Thanks Raghav,  
I didn't understand the question. With `const DAY_IN_MILLISECONDS = 3600 * 24 * 1000;` we're performing the calculations one time and that constant can be used multiple times now. And we can definitely have a better comment around it.

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' role='img' aria-labelledby='aoy4knpn9fwie9pe2vhdlonk9y17gnsu' class='crayons-icon reaction-icon not-reacted js-evernote-checked' data-evernote-id='183'%3e%3ctitle id='aoy4knpn9fwie9pe2vhdlonk9y17gnsu' data-evernote-id='3428' class='js-evernote-checked'%3eComment button%3c/title%3e%3cpath d='M10.5 5h3a6 6 0 110 12v2.625c-3.75-1.5-9-3.75-9-8.625a6 6 0 016-6zM12 15.5h1.5a4.501 4.501 0 001.722-8.657A4.5 4.5 0 0013.5 6.5h-3A4.5 4.5 0 006 11c0 2.707 1.846 4.475 6 6.36V15.5z' data-evernote-id='3429' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)
Reply](https://dev.to/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e#/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e/comments/new/1l243)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='ar6g5c9oc1o6ys2fmsd3i75y8x1dne14' class='crayons-icon expanded js-evernote-checked' data-evernote-id='383'%3e%3ctitle id='ar6g5c9oc1o6ys2fmsd3i75y8x1dne14' data-evernote-id='3431' class='js-evernote-checked'%3eCollapse%3c/title%3e %3cpath d='M12 10.677L8 6.935 9 6l3 2.807L15 6l1 .935-4 3.742zm0 4.517L9 18l-1-.935 4-3.742 4 3.742-1 .934-3-2.805z' data-evernote-id='3432' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='a3lohgsf61191bir8hfe3wkmq8navk27' class='crayons-icon collapsed js-evernote-checked' data-evernote-id='395'%3e%3ctitle id='a3lohgsf61191bir8hfe3wkmq8navk27' data-evernote-id='3433' class='js-evernote-checked'%3eExpand%3c/title%3e %3cpath d='M12 18l-4-3.771 1-.943 3 2.829 3-2.829 1 .943L12 18zm0-10.115l-3 2.829-1-.943L12 6l4 3.771-1 .942-3-2.828z' data-evernote-id='3434' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![74d89777-dca6-4e47-9b4c-fa1a457ba723.png](dev-to--8-techniques-to-write-cleaner-javascript-code/631b11ab55e86327e7671843215ce774.png)](https://dev.to/luishrodg)

•
[Jan 5](https://dev.to/luishrodg/comment/1l2f2)

I believe that what Raghav meant was, if you put this variable in an kind of component that calculation will be done every time that i use the component.

use this:

```
const DAY_IN_MILLISECONDS = 86400000 // 3600 * 24 * 1000
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='3485'%3e%3ctitle data-evernote-id='3486' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='3487' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='3488'%3e%3ctitle data-evernote-id='3489' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='3490' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='amzo6z4yvghep8ypvzzt9qvrt8xlstft' class='crayons-icon js-evernote-checked' data-evernote-id='3496'%3e%3ctitle id='amzo6z4yvghep8ypvzzt9qvrt8xlstft' data-evernote-id='3497' class='js-evernote-checked'%3eThread%3c/title%3e %3cpath d='M17 13l-5 6-5-6h3.125c0-3.314 2.798-6 6.25-6 .17 0 .34.006.506.02-1.787.904-3.006 2.705-3.006 4.78V13H17z' data-evernote-id='3498' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
Thread

[![fd44bf4a-29f7-4769-85be-82205ec5ed06.jpeg](dev-to--8-techniques-to-write-cleaner-javascript-code/db382be8082e473c0f4b2da2f525e0c4.jpeg)](https://dev.to/codewithahsan)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='arl52ug61qlrwqr4fwyr5s74y1wi0y7n' class='crayons-icon js-evernote-checked' data-evernote-id='3526'%3e%3ctitle id='arl52ug61qlrwqr4fwyr5s74y1wi0y7n' data-evernote-id='3527' class='js-evernote-checked'%3eAuthor%3c/title%3e %3cpath d='M12 8.25a6 6 0 110 12 6 6 0 010-12zm0 2.625l-.992 2.01-2.218.322 1.605 1.564-.379 2.21L12 15.937l1.984 1.043-.379-2.209 1.605-1.564-2.218-.323L12 10.875zm.75-6.376l3.75.001v2.25l-1.022.854a7.45 7.45 0 00-2.728-.817V4.5zm-1.5 0v2.288a7.451 7.451 0 00-2.727.816L7.5 6.75V4.5h3.75z' data-evernote-id='3528' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
Author

•
[Jan 8](https://dev.to/codewithahsan/comment/1l4h2)

Oh. Yeah, definitely. This should most likely be in a constants file or something. You're right.

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' role='img' aria-labelledby='a7wq0mdz5zizd26sdvbzjqklidq7xeq7' class='crayons-icon reaction-icon not-reacted js-evernote-checked' data-evernote-id='195'%3e%3ctitle id='a7wq0mdz5zizd26sdvbzjqklidq7xeq7' data-evernote-id='3550' class='js-evernote-checked'%3eComment button%3c/title%3e%3cpath d='M10.5 5h3a6 6 0 110 12v2.625c-3.75-1.5-9-3.75-9-8.625a6 6 0 016-6zM12 15.5h1.5a4.501 4.501 0 001.722-8.657A4.5 4.5 0 0013.5 6.5h-3A4.5 4.5 0 006 11c0 2.707 1.846 4.475 6 6.36V15.5z' data-evernote-id='3551' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)
Reply](https://dev.to/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e#/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e/comments/new/1l4h2)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='a2hky61rcx73woe0twish6xa9k16k53q' class='crayons-icon expanded js-evernote-checked' data-evernote-id='384'%3e%3ctitle id='a2hky61rcx73woe0twish6xa9k16k53q' data-evernote-id='3553' class='js-evernote-checked'%3eCollapse%3c/title%3e %3cpath d='M12 10.677L8 6.935 9 6l3 2.807L15 6l1 .935-4 3.742zm0 4.517L9 18l-1-.935 4-3.742 4 3.742-1 .934-3-2.805z' data-evernote-id='3554' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='annsvead8duiz6vgj8x5k16ic49i67g5' class='crayons-icon collapsed js-evernote-checked' data-evernote-id='396'%3e%3ctitle id='annsvead8duiz6vgj8x5k16ic49i67g5' data-evernote-id='3555' class='js-evernote-checked'%3eExpand%3c/title%3e %3cpath d='M12 18l-4-3.771 1-.943 3 2.829 3-2.829 1 .943L12 18zm0-10.115l-3 2.829-1-.943L12 6l4 3.771-1 .942-3-2.828z' data-evernote-id='3556' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![02a9a324-8ed4-46b0-9c54-b029a0a4095f.jpeg](dev-to--8-techniques-to-write-cleaner-javascript-code/aa350dab3d1556668b9ec6bc4cdfa86e.jpeg)](https://dev.to/zalithka)

•
[Jan 18](https://dev.to/zalithka/comment/1lc3a)

I'm normally somewhat sceptical of posts in this category, simply because so many of these points end up being very closely tied to the wonderful concept of "personal preference".. that said, this has some real gems, with some good clear examples. nicely done!

with regards to the idea of avoiding short-hand variable names, I agree wholeheartedly with what you're saying, but *(..and there it is)* I have one small exception to this "rule": and that is dinky, tiny, one-liner helper functions..

using your first `splitName` function as an example, simply because of how small it actually is, instead of writing it like this:

```
const splitName = (nameString) => {
  return nameString.split(' ');
}
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='3624'%3e%3ctitle data-evernote-id='3625' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='3626' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='3627'%3e%3ctitle data-evernote-id='3628' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='3629' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

*I personally* would have written is like this:

```
const splitName = (n) => n.split(' ');
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='3653'%3e%3ctitle data-evernote-id='3654' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='3655' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='3656'%3e%3ctitle data-evernote-id='3657' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='3658' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

with that said, as soon as the function arguments start growing, or the function body requires more than a single line, then **both** the implicit return and short-hand variable names go straight out the window.. tied to a rock.. shot by a cannon.. sometimes without even opening the window first.. (:

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' role='img' aria-labelledby='alxbnginye8iunsaelfvroh2cyait1be' class='crayons-icon reaction-icon not-reacted js-evernote-checked' data-evernote-id='202'%3e%3ctitle id='alxbnginye8iunsaelfvroh2cyait1be' data-evernote-id='3665' class='js-evernote-checked'%3eComment button%3c/title%3e%3cpath d='M10.5 5h3a6 6 0 110 12v2.625c-3.75-1.5-9-3.75-9-8.625a6 6 0 016-6zM12 15.5h1.5a4.501 4.501 0 001.722-8.657A4.5 4.5 0 0013.5 6.5h-3A4.5 4.5 0 006 11c0 2.707 1.846 4.475 6 6.36V15.5z' data-evernote-id='3666' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)
Reply](https://dev.to/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e#/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e/comments/new/1lc3a)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='ae2cc1i33nymtfhf8lc7ka8m39oakgc' class='crayons-icon expanded js-evernote-checked' data-evernote-id='385'%3e%3ctitle id='ae2cc1i33nymtfhf8lc7ka8m39oakgc' data-evernote-id='3668' class='js-evernote-checked'%3eCollapse%3c/title%3e %3cpath d='M12 10.677L8 6.935 9 6l3 2.807L15 6l1 .935-4 3.742zm0 4.517L9 18l-1-.935 4-3.742 4 3.742-1 .934-3-2.805z' data-evernote-id='3669' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='ak0gaagq9mxc6fjp80o7lxy2vndsq9dn' class='crayons-icon collapsed js-evernote-checked' data-evernote-id='397'%3e%3ctitle id='ak0gaagq9mxc6fjp80o7lxy2vndsq9dn' data-evernote-id='3670' class='js-evernote-checked'%3eExpand%3c/title%3e %3cpath d='M12 18l-4-3.771 1-.943 3 2.829 3-2.829 1 .943L12 18zm0-10.115l-3 2.829-1-.943L12 6l4 3.771-1 .942-3-2.828z' data-evernote-id='3671' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![0dd54cdb-8f76-425e-b406-b4e126f69d7b.png](dev-to--8-techniques-to-write-cleaner-javascript-code/9692b922eee0d99e6b77435d0d62fb57.png)](https://dev.to/robertrynard)

•
[Jan 11](https://dev.to/robertrynard/comment/1l75n)

For default object values is there a reason you are spreading out the two objects. Is there an advantage over doing

```
const createButton = (config) => {
    return {
      color: "#dcdcdc",
      disabled: false,
      title: "",
      padding: 0,
      ...config
    };
}
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='3746'%3e%3ctitle data-evernote-id='3747' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='3748' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='3749'%3e%3ctitle data-evernote-id='3750' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='3751' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

or using the default values in the arguments?

```
const createButton = ({ title = "", color = "#333", disabled = false, padding = 0 }) => {
  return {
      title,
      color,
      disabled,
      padding
  };
};
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='3794'%3e%3ctitle data-evernote-id='3795' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='3796' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='3797'%3e%3ctitle data-evernote-id='3798' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='3799' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' role='img' aria-labelledby='a32nkiz9qlqr96tg6v7otqcbm7c6iwws' class='crayons-icon reaction-icon not-reacted js-evernote-checked' data-evernote-id='209'%3e%3ctitle id='a32nkiz9qlqr96tg6v7otqcbm7c6iwws' data-evernote-id='3804' class='js-evernote-checked'%3eComment button%3c/title%3e%3cpath d='M10.5 5h3a6 6 0 110 12v2.625c-3.75-1.5-9-3.75-9-8.625a6 6 0 016-6zM12 15.5h1.5a4.501 4.501 0 001.722-8.657A4.5 4.5 0 0013.5 6.5h-3A4.5 4.5 0 006 11c0 2.707 1.846 4.475 6 6.36V15.5z' data-evernote-id='3805' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)
Reply](https://dev.to/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e#/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e/comments/new/1l75n)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='alfn3zcrbbs9hi1ki4ha8zecfxw5pfl6' class='crayons-icon expanded js-evernote-checked' data-evernote-id='386'%3e%3ctitle id='alfn3zcrbbs9hi1ki4ha8zecfxw5pfl6' data-evernote-id='3807' class='js-evernote-checked'%3eCollapse%3c/title%3e %3cpath d='M12 10.677L8 6.935 9 6l3 2.807L15 6l1 .935-4 3.742zm0 4.517L9 18l-1-.935 4-3.742 4 3.742-1 .934-3-2.805z' data-evernote-id='3808' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='a40160x95diyiqra7wuxo85xlntyrwn4' class='crayons-icon collapsed js-evernote-checked' data-evernote-id='398'%3e%3ctitle id='a40160x95diyiqra7wuxo85xlntyrwn4' data-evernote-id='3809' class='js-evernote-checked'%3eExpand%3c/title%3e %3cpath d='M12 18l-4-3.771 1-.943 3 2.829 3-2.829 1 .943L12 18zm0-10.115l-3 2.829-1-.943L12 6l4 3.771-1 .942-3-2.828z' data-evernote-id='3810' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![d24610dd-87ed-4b1a-b8b2-ce55a38a7113.png](dev-to--8-techniques-to-write-cleaner-javascript-code/69d7b4c6d48b36654ac61708d7b50d84.png)](https://dev.to/rafiqm)

•
[Jan 18](https://dev.to/rafiqm/comment/1lc53)

Awesome Article, Thanks for the great techniques, you provided in this great article

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' role='img' aria-labelledby='a29ji0jvdxnvd0q0robokslrko1j0sd0' class='crayons-icon reaction-icon not-reacted js-evernote-checked' data-evernote-id='216'%3e%3ctitle id='a29ji0jvdxnvd0q0robokslrko1j0sd0' data-evernote-id='3853' class='js-evernote-checked'%3eComment button%3c/title%3e%3cpath d='M10.5 5h3a6 6 0 110 12v2.625c-3.75-1.5-9-3.75-9-8.625a6 6 0 016-6zM12 15.5h1.5a4.501 4.501 0 001.722-8.657A4.5 4.5 0 0013.5 6.5h-3A4.5 4.5 0 006 11c0 2.707 1.846 4.475 6 6.36V15.5z' data-evernote-id='3854' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)
Reply](https://dev.to/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e#/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e/comments/new/1lc53)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='agmbth2us0fwtziec651llv5s31ke6bq' class='crayons-icon expanded js-evernote-checked' data-evernote-id='387'%3e%3ctitle id='agmbth2us0fwtziec651llv5s31ke6bq' data-evernote-id='3856' class='js-evernote-checked'%3eCollapse%3c/title%3e %3cpath d='M12 10.677L8 6.935 9 6l3 2.807L15 6l1 .935-4 3.742zm0 4.517L9 18l-1-.935 4-3.742 4 3.742-1 .934-3-2.805z' data-evernote-id='3857' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='agv6ucysah54wpsp6fh3f7fparb9o8wi' class='crayons-icon collapsed js-evernote-checked' data-evernote-id='399'%3e%3ctitle id='agv6ucysah54wpsp6fh3f7fparb9o8wi' data-evernote-id='3858' class='js-evernote-checked'%3eExpand%3c/title%3e %3cpath d='M12 18l-4-3.771 1-.943 3 2.829 3-2.829 1 .943L12 18zm0-10.115l-3 2.829-1-.943L12 6l4 3.771-1 .942-3-2.828z' data-evernote-id='3859' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![fd44bf4a-29f7-4769-85be-82205ec5ed06.jpeg](dev-to--8-techniques-to-write-cleaner-javascript-code/db382be8082e473c0f4b2da2f525e0c4.jpeg)](https://dev.to/codewithahsan)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='a6uhaq5rn3gcuju0yq7epru7v94o1ujx' class='crayons-icon js-evernote-checked' data-evernote-id='3888'%3e%3ctitle id='a6uhaq5rn3gcuju0yq7epru7v94o1ujx' data-evernote-id='3889' class='js-evernote-checked'%3eAuthor%3c/title%3e %3cpath d='M12 8.25a6 6 0 110 12 6 6 0 010-12zm0 2.625l-.992 2.01-2.218.322 1.605 1.564-.379 2.21L12 15.937l1.984 1.043-.379-2.209 1.605-1.564-2.218-.323L12 10.875zm.75-6.376l3.75.001v2.25l-1.022.854a7.45 7.45 0 00-2.728-.817V4.5zm-1.5 0v2.288a7.451 7.451 0 00-2.727.816L7.5 6.75V4.5h3.75z' data-evernote-id='3890' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
Author

•
[Jan 19](https://dev.to/codewithahsan/comment/1lcpo)

Anytime!! Thanks.

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' role='img' aria-labelledby='amjgc16dtgy7vh9yx53j7d6sjyhnu072' class='crayons-icon reaction-icon not-reacted js-evernote-checked' data-evernote-id='223'%3e%3ctitle id='amjgc16dtgy7vh9yx53j7d6sjyhnu072' data-evernote-id='3912' class='js-evernote-checked'%3eComment button%3c/title%3e%3cpath d='M10.5 5h3a6 6 0 110 12v2.625c-3.75-1.5-9-3.75-9-8.625a6 6 0 016-6zM12 15.5h1.5a4.501 4.501 0 001.722-8.657A4.5 4.5 0 0013.5 6.5h-3A4.5 4.5 0 006 11c0 2.707 1.846 4.475 6 6.36V15.5z' data-evernote-id='3913' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)
Reply](https://dev.to/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e#/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e/comments/new/1lcpo)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='a8nsdc74avwj4nsfmem7ip24hycbk90' class='crayons-icon expanded js-evernote-checked' data-evernote-id='388'%3e%3ctitle id='a8nsdc74avwj4nsfmem7ip24hycbk90' data-evernote-id='3915' class='js-evernote-checked'%3eCollapse%3c/title%3e %3cpath d='M12 10.677L8 6.935 9 6l3 2.807L15 6l1 .935-4 3.742zm0 4.517L9 18l-1-.935 4-3.742 4 3.742-1 .934-3-2.805z' data-evernote-id='3916' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='apxm6pxsqd9ryzb7u32u2gqq27y5fhq1' class='crayons-icon collapsed js-evernote-checked' data-evernote-id='400'%3e%3ctitle id='apxm6pxsqd9ryzb7u32u2gqq27y5fhq1' data-evernote-id='3917' class='js-evernote-checked'%3eExpand%3c/title%3e %3cpath d='M12 18l-4-3.771 1-.943 3 2.829 3-2.829 1 .943L12 18zm0-10.115l-3 2.829-1-.943L12 6l4 3.771-1 .942-3-2.828z' data-evernote-id='3918' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![8ee2d2ae-9287-4d90-82af-9222de89e589.jpeg](dev-to--8-techniques-to-write-cleaner-javascript-code/e9fb84ba986fd34e83717d96446cd6bc.jpeg)](https://dev.to/gabrielizalo)

•
[Jan 31](https://dev.to/gabrielizalo/comment/1lkoe)

Hey.. Remember update your Twitter in your Dev Profile: [dev.to/codewithahsan](https://dev.to/codewithahsan)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' role='img' aria-labelledby='aripc1u2bzxsgj9ekntlv7bsdv5u0ltu' class='crayons-icon reaction-icon not-reacted js-evernote-checked' data-evernote-id='230'%3e%3ctitle id='aripc1u2bzxsgj9ekntlv7bsdv5u0ltu' data-evernote-id='3963' class='js-evernote-checked'%3eComment button%3c/title%3e%3cpath d='M10.5 5h3a6 6 0 110 12v2.625c-3.75-1.5-9-3.75-9-8.625a6 6 0 016-6zM12 15.5h1.5a4.501 4.501 0 001.722-8.657A4.5 4.5 0 0013.5 6.5h-3A4.5 4.5 0 006 11c0 2.707 1.846 4.475 6 6.36V15.5z' data-evernote-id='3964' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)
Reply](https://dev.to/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e#/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e/comments/new/1lkoe)

[Code of Conduct](https://dev.to/code-of-conduct)
•
[Report abuse](https://dev.to/report-abuse)
