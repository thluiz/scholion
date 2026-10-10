---
url: "http://arqex.com/939/learning-much-javascript-one-line-code?utm_source=javascriptweekly&utm_medium=email"
captured_at: "2014-10-12T11:34:20-03:00"
title: "Learning much javascript from one line of code - arqex"
domain: "arqex-com"
---

# Learning much javascript from one line of code

Since javascript is everywhere nowadays, it is really easy to learn new stuff everyday. Once you know the basics of the language, you can take bits of code from here and there that have a lot of knowledge in them. **Bookmarklets** are perfect examples of a bunch of packed functionality, whenever I discover a useful one, I enjoy studying their source, discovering how it can do so much. Also snippets to use external services, like the google analytics code, or facebook likebox, can teach us more than some books.

Today I want to break in pieces a [one-liner code](https://gist.github.com/addyosmani/fd3999ea7fce242756b1) that [**Addy Osmani**](http://addyosmani.com/blog/) shared a few days ago that can be used to debug your CSS layers. Here it is, in 3 lines to fit in the post:

|  |  |
| --- | --- |
|  | forEachfunction  styleoutline"1px solid #"random<<toString |

Try to type it in your browser console, and the different layers of HTML that there are in the web page will be highlighted in different colors. Isn’t it awesome? Basically, **it gets all the elements of the page, and applies a 1 px outline to them with a random color**. The idea is simple, but to create a code line like this you must master a lot of aspects of web development. Let’s study them.

## Selecting all the elements of a page

What it is needed the first is to get all the elements, and Addy uses the  function `$$` that is only available in the console of browsers. Try it by yourself, open your browser’s javascript console and type `$$('a')` and you will get a list with all the anchor elements of the current page.

`$$` function is part of the command line API of modern browsers, and it is equivalent to use the method `document.querySelectorAll`, you can pass a CSS selector as argument to get the matched elements in the current page. So if you would like to use the one-liner out the browser’s console you could replace `$$('*')` by `document.querySelectorAll('*')`. More about the function `$$` can be found in [this stackoverflow answer](http://stackoverflow.com/questions/8981211/what-is-the-source-of-the-double-dollar-sign-selector-query-function-in-chrome-f#answer-10308917).

It is great! For me, it was worthy to study the code just by meeting the function `$$`. But there are more about selecting everything in a page, if you have a look at the comments of the gist, there are people discussing this part of the code. One of them is [**Mathias Bynens**](https://mathiasbynens.be/), ( a lot of clever people there! ) who suggests that we can also use `document.all` to select all the elements of a page, it is not standard, but it works ok in every browser ~~but firefox~~ (in FF too).

## Iterating over the elements

So we have all the elements now as a [`NodeList`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList) and we want to go through all of them applying the colorful outline. But wait, what the heck is used in our code?

|  |  |
| --- | --- |
|  | forEachfunctionelement/\* And the modification code here \*/ |

[`NodeLists`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList) seems like `Arrays`, you can access to their nodes using brackets, and you can check how many elements it contains using the property length, but they doesn’t implement all the methods of the `Array` interface, so using `$$('*').forEach` will fail. In Javascript there are several objects that look like arrays but they are not, like the arguments variable inside functions, and we have here a very useful pattern to handle with them: Calling array methods on no-array objects as `NodeLists` is possible using the Function’s methods call and apply. [I wrote about those functions some months ago](http://arqex.com/853/javascript-function-bind-vs-call-apply "Javascript function context: bind vs call & apply"), they execute a function using the first parameter as the object this inside of the function

|  |  |
| --- | --- |
|  | function  console  'hola''Mike'// Prints out 'hola Mike' in the console  // Also you can use it on the arguments object  functionexample  returnArrayprototypeslicearguments// Returns [arg2, arg3] |

The one-liner is using `[].forEach.call` instead of `Array.prototype.forEach.call` to save some bytes ( another nice trick yeah? ) calling the method in the `Array` object `[]`. This would be equivalent to `$$('*').forEach` if `$$('*')` value was an `Array`.

If you have a look at the comments again, there are some people who use `for(i=0;A=$$('*');)` instead to make the code shorter. It works, but it is leaking global variables, so if you want to use the code out of the console, you better get a clean enviroment using

|  |  |
| --- | --- |
|  | documentquerySelectorAll/\* your code here \*/ |

If you use it in the browser’s console it doesn’t really matter, the variables `i` and `A` will be available there since you are declaring them there.

## Assigning colors to the elements

To make the elements have that nice border, the code is using the CSS property [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/outline). In case you don’t know, the rendered outline is out of the CSS box model so **it doesn’t affect the size of the element or its position in the layout**, so it is perfect for this purpose. It’s syntax is like the one used for the `border` property, so it shouldn’t be difficult to understand this part:

|  |  |
| --- | --- |
|  | styleoutline"1px solid #"color |

What  is interesting is how the color is defined:

|  |  |
| --- | --- |
|  | random<<toString |

Scary uh? Sure. I am not a bit-wise operations expert, so this is the part I liked the most, because it let me learn a lot of new stuff.

What we want to achieve is a hexadecimal color like white `FFFFFF` or blue `0000FF` or… who knows… `37f9ac`. Non super-human people, like me, is used to work with decimal numbers, but our beloved code knows a lot about hexadecimal ones.

First thing it can teach us is how to convert a decimal number to hex using the method `toString` for integers. The method accepts a parameter to convert a number to a string using a base number of characters. If the parameter is not used, 10 characters are used (0…9, hence, decimal numbers), but you can use whatever other base:

|  |  |
| --- | --- |
|  | toString// "30"  toString// "30"  toString// "1e" Hexadecimal  toString// "11110" Binary  toString// "u" 36 is the maximum base allowed |

The other way around, you can convert hexadecimal string to decimal numbers using the second parameter of the `parseInt` method:

|  |  |
| --- | --- |
|  | parseInt// "30"  parseInt// "30"  parseInt// "30"  parseInt"11110"// "30"  parseInt// "30" |

So we need a random number between `0` and `ffffff` in hexadecimal, that is `parseInt("ffffff", 16) == 16777215` and 16777215 is exactly `2^24 - 1`.

Do you like binary maths? If not, you will be ok knowing that `1<<24 == 16777216` (try it in the console).

If you like them, you need to know that every time that you add a 0 to the right of a 1 you are doing performing the `2^n` operation, being `n` the number of 0s you add.

|  |  |
| --- | --- |
|  | // 1 == 2^0  // 4 == 2^2  10000// 16 == 2^4  1000000000000000000000000// 16777216 == 2^24 |

The left shift operation `x << n` adds `n` `0`s to the binary representation of the number `x`, so `1<<24` is a short way of saying `16777216`, and doing `Math.random()*/(1<<24)` we get a number between `0` and `16777216`.

We are not ready yet, because `Math.random` return a float number, and we need only the whole part. Our code use the **tilde operator** to get so. Tilde operator is used to negate a variable bit by bit. If you don’t know about what I am talking about, here it is a good explanation: [Javascript’s tilde operator](http://www.javascriptturnsmeon.com/the-tilde-operator-in-javascript/).

But the code doesn’t care about bitwise negation, it uses the tilde because the bitwise operations discard the decimal part of a float number, so bitwise-negation applied twice is a short way of writing `parseInt`:

|  |  |
| --- | --- |
|  | 12.34// ~~a = 12  1231.8754// ~~b = -1231  3213.000001// ~~c = 3213  parseInt// true  parseInt// true  parseInt// true |

Again, if you go to the [gist](https://gist.github.com/addyosmani/fd3999ea7fce242756b1) and have a look at the comments you will realize that people there is using a shorter version to get the parseInt result. Using the bitwise **OR operator** you can get rid of the decimal part of our random number

|  |  |
| --- | --- |
|  | ~~a == 0|a == parseInt(a, 10)  ~~b == 0|b == parseInt(b, 10)  ~~c == 0|c == parseInt(c, 10) |

Or operator is the last to be used in a operation so the parenthesis are not needed anymore. Here it is the [precedence of javascript operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)s in case you are interested in having a look.

Finally we have our random number `0` and `16777216`, our random color. We just need to turn it to a hexadecimal string using `toString(16)` to make it work.

## Last thoughts

Being a programmer is not easy. We are used to code like crazy and sometimes we don’t realize about how much knowledge is needed to do what we do. It takes a long long time to learn and internalize all the concepts that we use in our job.

I wanted to highlight the complexity of our job because I know that programmers are usually underestimated, ( especially in my country, Spain ) and it is nice to say ocassionally that we are really worthy and a key part of most of companies nowadays.

If you understood the one-liner code at first sight you can feel proud of yourself.

If not, but you have reach this point of the article, don’t worry man, you will be able to write lines like that soon, you are a learner!

If you thought *tl;dr* at the second line of the article but you are reading this, you are really weird, but your thoughts are also welcome in the comments section below : )
