---
url: "https://dev.to/leirasanchez/like-console-log-but-better-nhm"
captured_at: "2026-11-16T00:30:36+00:00"
title: "Like `console.log` But Better"
domain: "dev-to"
---

[![Leira Sánchez](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F320897%2Fc2861085-61ec-4e67-9f29-1bc604632177.jpeg)](https://dev.to/leirasanchez)

Who hasn't peppered their code with console.logs in an attempt to find that pesky bug? The logs can get daunting and confusing. These will help you enhance your debugging experience with the console.

Did you know the console has more properties than log? Try it yourself! Write this into your console and be amazed.  

```
console.log(console);
```

Enter fullscreen mode Exit fullscreen mode

I will go through the ones I find the most useful.

## [](#consoletable)console.table();

This method displays your arrays and objects in a neat table. It takes in two parameters, the data, and the names (in an array) of the columns you wish to display (optional). Every element, or property, will correspond to a row in the table.

Example:  

```
const array = [1, 2, 3, 4, 5];
const object = {
  name: "Leira",
  lastName: "Sánchez",
  twitter: "MechEngSanchez",
};

console.log('array: ', array); 
// array:  [ 1, 2, 3, 4, 5 ]

console.log('object: ', object); 
// object:  { name: 'Leira', lastName: 'Sánchez', twitter: 'MechEngSanchez' }
```

Enter fullscreen mode Exit fullscreen mode

What is displayed when using table, is much more organized and easy to understand.  

```
console.table(array);
```

Enter fullscreen mode Exit fullscreen mode

[![console.table(array)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Ft8jnieosxl0l36f9e6hk.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Ft8jnieosxl0l36f9e6hk.png)  

```
console.table(object);
```

Enter fullscreen mode Exit fullscreen mode

[![console.table(object)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fr25ft9l30ra4fx32q8jy.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fr25ft9l30ra4fx32q8jy.png)

## [](#consolecount)console.count()

This method keeps a count of how many times it has been called. I mostly use it to check that my functions are being called when I expect them to. You can provide it with a string as a parameter. It will serve as the label. If left blank, the default label is "default".  

```
let dev = '';
const followMe = (dev) => {
    console.count('followers');
    return `${dev} is following you`;
}

followMe('John'); // followers: 1
followMe('Karen'); // followers: 2
followMe('Camila'); // followers: 3
```

Enter fullscreen mode Exit fullscreen mode

## [](#consoleassert)console.assert()

This method only writes to the console if the assertion is false. You will not see it if it's true. The first parameter is what it will make the check on. The second one is the error message you wish to display.  

```
const sum = (n1, n2) => {
    console.assert(n1 + n2 === 10, 'Not 10');
};

sum(3,2); // Assertion failed: Not 10
sum(5,5); //
sum(10,0); //
```

Enter fullscreen mode Exit fullscreen mode

## [](#style-the-raw-consolelog-endraw-)Style the `console.log`

### [](#labels)Labels

A quick, easy way to organize and keep track of your console.logs is to add labels. Simply, add a string as the first parameter and whatever you want to log as the second. I also like to add a colon and a space for readability.  

```
const firstName = 'Leira';
console.log('First Name: ', firstName); // First Name: Leira
```

Enter fullscreen mode Exit fullscreen mode

You can add a string as every other parameter to add multiple labels to multiple values but I find that can get messy fast.  

```
const lastName = 'Sánchez';

console.log('First Name: ', firstName, 'Last Name: ', lastName);
// First Name: Leira Last Name: Sánchez
```

Enter fullscreen mode Exit fullscreen mode

Messy, right?

### [](#add-flair-with-css)Add Flair with CSS!

Make your logs colorful and pretty. Just add '%c' to the front of a string as the first parameter. The second parameter will be the CSS styles as a string.  

```
console.log("%cCLICKED!", "font-family:arial;color:green;font-weight:bold;font-size:3rem");
```

Enter fullscreen mode Exit fullscreen mode

[![clicked](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fq7k07brwy3k7rol32jfe.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fq7k07brwy3k7rol32jfe.png)

Let me know in the comments how else you use these or what other methods you find useful!
