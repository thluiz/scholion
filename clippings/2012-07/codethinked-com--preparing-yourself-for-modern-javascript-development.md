---
url: "http://www.codethinked.com/preparing-yourself-for-modern-javascript-development"
captured_at: "2012-07-09T11:11:30-03:00"
title: "Preparing Yourself for Modern JavaScript Development | CodeThinked"
domain: "codethinked-com"
---

## Preparing Yourself for Modern JavaScript Development

There is a lot going on in the JavaScript world these days, both in and out of the browser. Talk about script loaders, client side MVC frameworks, minifiers, AMD, Common.js, Coffeescript, can quickly get your head spinning. And for those people who are completely immersed in that world, it can be easy to forget that the vast majority of JavaScript developers today haven’t heard of any of these tools, and in fact, they likely aren’t even equipped to **try** these tools.

This post is going to be an attempt to simply address some of the low hanging fruit out there, and try to bring together a few different concepts that a developer should understand before they go out and try to tackle something like Backbone.js or Ember.js. Once you understand most of the concepts in this post, then you can go out and approach more advanced JavaScript topics with a bit of confidence. This post does assume that you have developed with JavaScript before, so if you haven’t, then you might be better off starting with something a bit more basic. With that out of the way, here we go!

## Modules

How many of you are working with an application that has JavaScript that looks like this just sitting in a file (notice I didn’t say embedded in your html files, there is no good excuse for that):

[?](http://www.codethinked.com/preparing-yourself-for-modern-javascript-development#)

|  |  |
| --- | --- |
| 1  2  3 | `var` `someSharedValue = 10;`  `var` `myFunction =` `function``(){` `//do something }`  `var` `anotherImportantFunction =` `function``() {` `//do more stuff }` |

If you’ve made it to this point in the post, then most likely you are dealing with (or creating) code that looks like this. I’m not judging you, I wrote code like that for a really long time. The problems here are many, but the one that we are going to focus on is the pollution of the global namespace. When writing code like this, you are just shoving all of these methods and variables into the global namespace. We need some way to keep this kind of data out of the global namespace, and the technique we are going to use here is the module pattern. There are different forms that modules can take, but I’m going to start off with the easiest method that you can start using today, an IIFE (Immediately Invoked Function Expression).

It is a big name, but the implementation is very simple:

[?](http://www.codethinked.com/preparing-yourself-for-modern-javascript-development#)

|  |  |
| --- | --- |
| 1  2  3 | `(``function``(){`  `//do some work`  `})();` |

If you haven’t used an IIFE before this might look at bit weird at first. There are a lot of parentheses going on around here! Basically we have an anonymous function with a set of parentheses following it which cause the function to be immediately invoked. So we are creating the function, then immediately calling it. Hence the “immediately invoked function” part of the name. The “expression” part of IIFE comes from the fact that we need to turn this into an expression and not a statement, since a function statement must have a name. We do this by adding the extra set of parentheses around the outside. This also gives us an easy way to spot IIFE’s when looking through our code.

Now that we know how to implement it, let’s talk about why we do this. In JavaScript all we have to work with for scoping is functions, and so if we want to create scope, we use a function. By executing code inside of the IIFE we are scoping all variables and functions inside of the IIFE and so we aren’t polluting the global namespace. The only problem is that all variables we create are now scoped inside of the function, so if we want to access them outside of the global scope, we need to get them into the global namespace, or at least into something that is in the global namespace.

One thing we can do is to use the window object and assign any functions or values to this object, which allows us to call these methods externally. In order to guarantee that nothing messes with the window variable, we can pass the window object as a parameter to our IIFE. We can do the same thing with references to libraries or even the value ‘undefined’. Our IIFE ends up looking like this:

[?](http://www.codethinked.com/preparing-yourself-for-modern-javascript-development#)

|  |  |
| --- | --- |
| 1  2  3 | `(``function``(window, $, undefined){`  `//do some work`  `})(window, jQuery);` |

As you can see, we are passing in the window and jQuery variables (the jQuery $ variable is just an alias for the ‘jQuery’ variable, and we use it here in case another library has redefined the $ variable), but then we have three parameters going into the method. The idea is that since we aren’t passing a third parameter, it ends up being undefined, so we get a variable called ‘undefined’ local to the method that is guaranteed to actually have the value ‘undefined’, in case another piece of JavaScript modified it. Notice that we could call any of these values within the function without passing them in, this works because functions in JavaScript form closures where they “close over” the outer scope that they reside in. This topic can be an entire post, and I have [written one which explains closures in terms of C#](http://www.codethinked.com/c-closures-explained), but the concepts are very similar.

Now we have a a method which is executed immediately, has a much safer execution context containing valid window, $, and undefined variables (it is still possible that something could have reassigned one of these variables before we hit this script, but it is much less likely). We are in a pretty good place, having saved our code from becoming a bunch of clutter in the global namespaces and reducing the potential for collisions with other JavaScript running in our application.

At this point anything we want to export from the module we are just assigning direction to the window object. But often I don’t want to just assign everything in my module directly to the window object, I want to have some way of grouping functionality. In most languages we call these containers namespaces, and we can emulate them in JavaScript using objects.

## Namespaces

If we wanted to declare a namespace, and assign a function to it, we could do something like this:

[?](http://www.codethinked.com/preparing-yourself-for-modern-javascript-development#)

|  |  |
| --- | --- |
| 1  2  3  4 | `window.myApp = window.myApp || {};`  `window.myApp.someFunction =` `function``(){`  `//so some work`  `};` |

We are merely creating an object in the global namespace by checking to see if the object already exists, and if so we use it, otherwise we create a new object using the object literal notation: {}. At this point we could just start building up the namespace by assigning functions like we are doing above, but we don’t want our code just hanging out there, we want to combine our namespaces with our modules, like this:

[?](http://www.codethinked.com/preparing-yourself-for-modern-javascript-development#)

|  |  |
| --- | --- |
| 1  2  3 | `(``function``(myApp, $, undefined){`  `//do some work`  `}(window.myApp = window.myApp || {}, jQuery));` |

This could also be written like this:

[?](http://www.codethinked.com/preparing-yourself-for-modern-javascript-development#)

|  |  |
| --- | --- |
| 1  2  3  4 | `window.myApp = (``function``(myApp, $, undefined){`  `//do some work`  `return` `myApp;`  `})(window.myApp || {}, jQuery);` |

Now, instead of passing in window to our module, we are passing in a namespace object that is hanging off the window object. The reason we assign it using || is so that if we use this namespace in multiple places we will end up using the same object over and over instead of creating a new object each time which would clear out our namespace. Many libraries include namespace functions which will create namespaces for you, or you can use something like [namespace.js](https://github.com/maximebf/Namespace.js "Namespace.js on Github") which allows you to easily create nested namespaces. I generally try not to create deeply nested namespaces, since in JavaScript you have to specify the namespace on every item that is in the namespace. So if you created a “doSomething” method in the MyApp.MyModule.MySubModule namespace, you would either have to reference it like:

[?](http://www.codethinked.com/preparing-yourself-for-modern-javascript-development#)

|  |  |
| --- | --- |
| 1 | `MyApp.MyModule.MySubModule.doSomething();` |

every time you called it, or you would have to alias the namespace inside of your module by doing:

[?](http://www.codethinked.com/preparing-yourself-for-modern-javascript-development#)

|  |  |
| --- | --- |
| 1 | `var` `MySubModule = MyApp.MyModule.MySubModule;` |

This way you would only need to say “MySubModule.doSomething()”. It just makes things more complicated, and unless you have a ton of code, it can be unnecessary.

## Revealing Module Pattern

There is another pattern that you’ll often see being used to create modules, and it is called the revealing module pattern. This pattern is just a different approach to creating a module, letting you define everything privately inside of the module, then expose what you want to expose by returning an object which has references to everything you want to expose publicly. Let’s take a look at how you would define this:

[?](http://www.codethinked.com/preparing-yourself-for-modern-javascript-development#)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | `var` `myModule = (``function``($, undefined){`  `var` `myVar1 =` `''``,`  `myVar2 =` `''``;`    `var` `someFunction =` `function``(){`  `return` `myVar1 +` `" "` `+ myVar2;`  `};`    `return` `{`  `myVar1: myVar1,` `//myVar1 made public`  `someFunction: someFunction` `//some function made public`  `}`  `})(jQuery);` |

As you can see, we are creating a module in one pass which makes it more simple, and then we are returning an object which exposes the pieces of our module that we are interested in making public, while allowing us to keep our private variables hidden. The variable “myModule” is going to contain the two publicly exposed items, but as you can see, “someFunction” uses “myVar2″, but it is not externally accessible.

## Creating Constructors (Classes)

In JavaScript we don’t have classes, but we can create objects, and we do this by creating a constructor function. Let’s say that we wanted to create a bunch of Person objects, and we wanted to pass in a first name, last name, and age. We could define our constructor like this (we would most likely put this inside of a module):

[?](http://www.codethinked.com/preparing-yourself-for-modern-javascript-development#)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | `var` `Person =` `function``(firstName, lastName, age){`  `this``.firstName = firstName;`  `this``.lastName = lastName;`  `this``.age = age;`  `}`    `Person.prototype.fullName =` `function``(){`  `return` `this``.firstName +` `" "` `+` `this``.lastName;`  `};` |

Looking at just the first function for now, you’ll see that we are creating a Person constructor. This is what we will use to build new person objects. It takes three parameters and it assigns them all to the execution context from the current invocation of the constructor. This is how we get public instance variables. We could create private variables here too, by assigning the constructor parameters to local variables inside of the constructor, but the problem becomes that public methods can’t access those variables, and so you’re probably better off making them all public. You can create methods inside of the constructor which are publicly accessible, and can access the private variables, but they create a whole different set of problems.

Next you’ll see that we accessing the “prototype” of the Person constructor. The prototype of a function is an object that all instances of a function will go to when trying to resolve fields or functions called on the instance. So what we are doing here is creating a single instance of a “fullName” method that all instances of “Person” can access without having a ton of instances of “fullName” hanging around. We could have defined “fullName” inside of the constructor as “this.fullName = function() { …” but then every person would have another copy of the fullName method, which is not what we want.

If we wanted to start creating people, we could do so like this:

[?](http://www.codethinked.com/preparing-yourself-for-modern-javascript-development#)

|  |  |
| --- | --- |
| 1  2 | `var` `person =` `new` `Person(``"Justin"``,` `"Etheredge"``);`  `alert(person.fullName());` |

If we wanted to, we could also create another constructor that inherits from the Person constructor. Let’s say we wanted to create a Spy constructor, that would build an instance of Spy, but would only declare a single method:

[?](http://www.codethinked.com/preparing-yourself-for-modern-javascript-development#)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | `var` `Spy =` `function``(firstName, lastName, age){`  `this``.firstName = firstName;`  `this``.lastName = lastName;`  `this``.age = age;`  `};`  `Spy.prototype =` `new` `Person();`    `Spy.prototype.spy =` `function``(){`  `alert(``this``.fullName() +` `" is spying."``);`  `}`    `var` `mySpy =` `new` `Spy(``"Mr."``,` `"Spy"``, 50);`  `mySpy.spy();` |

As you can see, we are creating a constructor that looks just like the person, but then we are settings its prototype to an instance of the Person constructor. Now we can add methods, and when we create an instance of Spy, it can access methods in the Person constructor, and the methods can access variables which were assigned in the Spy instance! It is a bit convoluted, but once you get past the details, it is pretty elegant.

## Wrapping It Up

At this point, if you have learned something, then awesome! But unfortunately we really haven’t touched on any “modern” JavaScript development. All of the topics that we have gone over in this blog post are relatively old, and have been in fairly wide use for at least the last few years. But now hopefully you are at least heading down the right road. Now that you are splitting up your code into modules and using lots of different files (you should be!), the next step for you should be to start researching JavaScript combination and minification. If you are a Rails developer, and are using Rails 3, then you get all of this for free in the asset pipeline. If you’re using .NET then you can look at the framework that I started, [SquishIt](https://github.com/jetheredge/SquishIt "SquishIt Github"). If you’re using ASP.NET MVC 4, then it also has some built in combination and minification support.

Hope this helped, and I hope to see you back here next time when I will start to explore a few topics in modern JavaScript development!
