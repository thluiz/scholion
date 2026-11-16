---
url: "https://dev.to/puf17640/spreading-destructuring-and-rest-parameters-in-javascript-1haf"
captured_at: "2026-11-16T01:27:38+00:00"
title: "Spreading, Destructuring and Rest Parameters in Javascript"
domain: "dev-to"
---

## [](#intro)Intro

Since the 2015 version of the ECMAScript specification Javascript developers got access to a lot of new functionality regarding working with arrays and objects. In this article, I am going to explain 'spreading', 'destructuring' and the 'rest parameters' by showing you examples of how they can be used to reduce your code length or make it more easily understandable.

These concepts are not common in other programming languages so they can be something completely new for many developers, even ones that have been in the game for a long time.

## [](#spreading)Spreading

The spread syntax (`...`) is a very helpful technique when working with arrays or objects since it allows you to unpack and expand objects or arrays and make shallow copies of them.

## [](#spreading-objects)Spreading objects

Spreading can be used to copy an object, like `Object.assign()`, or update it.

### [](#copy)Copy

```
// without spreading
const originalObject = { 
    enabled: true, 
    darkMode: false 
}
const secondObject = Object.assign({}, originalObject)
```

Enter fullscreen mode Exit fullscreen mode

```
// with spreading
const originalObject = { 
    enabled: true, 
    darkMode: false 
}
const secondObject = { ...originalObject }
console.log(secondObject)

// Output:
{enabled: true, darkMode: false}
```

Enter fullscreen mode Exit fullscreen mode

Keep in mind this only creates a shallow copy of the object and nested objects will still be passed by reference.

### [](#update)Update

Updating objects is effortless using spreading, so let's add another property, `stayLoggedIn` to our `originalObject`.  

```
const originalObject = { 
    enabled: true, 
    darkMode: false 
}
const updatedObject = { 
    ...originalObject, 
    stayLoggedIn: true 
}
console.log(updatedObject)

// Output:
{enabled: true, darkMode: false, stayLoggedIn: true}
```

Enter fullscreen mode Exit fullscreen mode

One thing that has to be noted when updating nested objects is that they have to be spread as well, because they will be overwritten if you do not.  

```
const originalObject = { 
    enabled: true, 
    settings: { 
        darkMode: false 
    } 
}
const updatedObject = { 
    ...originalObject, 
    settings: { 
        stayLoggedIn: true 
    } 
}
console.log(updatedObject)

// Output:
{enabled: true, settings: {stayLoggedIn: true}}
```

Enter fullscreen mode Exit fullscreen mode

As said above, the `settings` object will be overwritten. To solve this, you need to spread the nested objects like this:  

```
const originalObject = { 
    enabled: true, 
    settings: { 
        darkMode: false 
    } 
}
const updatedObject = { 
    ...originalObject, 
    settings: { 
        ...originalObject.settings, 
        stayLoggedIn: true 
    } 
}
console.log(updatedObject)

// Output:
{enabled: true, settings: {darkMode: false, stayLoggedIn: true}}
```

Enter fullscreen mode Exit fullscreen mode

## [](#spreading-arrays)Spreading arrays

Using the spread syntax, you can simplify quite a lot of common tasks, like duplicating arrays.

### [](#duplicate)Duplicate

```
const originalArray = ['A', 'B', 'C']
const copyArray = [...originalArray]
originalArray.pop()
console.log(copyArray)

// Output:
['A', 'B', 'C']
```

Enter fullscreen mode Exit fullscreen mode

Cool, right? This creates a shallow copy of the array, this means that all top level properties will be cloned but nested properties will be passed by reference still. But that's not the end, you can also concatenate arrays way easier now.

### [](#-concat). Concat

```
const first = ['A', 'B', 'C']
const second = ['D', 'E', 'F']
const union = [...first, ...second]
console.log(union)

// Output:
['A', 'B', 'C', 'D', 'E', 'F']
```

Enter fullscreen mode Exit fullscreen mode

You can also split up a string into an array using spreading like this:  

```
const string = 'awesome'
const charArray = [...string]
console.log(charArray)

// Output:
['a', 'w', 'e', 's', 'o', 'm', 'e']
```

Enter fullscreen mode Exit fullscreen mode

## [](#destructuring)Destructuring

Destructuring is very helpful because it lets you assign array values or object properties to multiple variables at once.

## [](#destructuring-objects)Destructuring objects

Before destructuring came, if we wanted to have specific properties of an object mapped to normal variables, we had to assign every property separately.  

```
const obj = { 
    enabled: true, 
    darkMode: false, 
    stayLoggedIn: true 
}
const enabled = obj.enabled
const darkMode = obj.darkMode
const stayLoggedIn = obj.stayLoggedIn
```

Enter fullscreen mode Exit fullscreen mode

Now with object destructuring, this can be shortened down to just one line instead of three, check it out!  

```
const obj = { 
    enabled: true, 
    darkMode: false, 
    stayLoggedIn: true 
}
const { enabled, darkMode, stayLoggedIn } = obj
console.log(enabled, darkMode, stayLoggedIn)

// Output: 
true
false
true
```

Enter fullscreen mode Exit fullscreen mode

As you can see, all properties got mapped to variables with the same name. If you don't want to have your variables named exactly like the properties, you can use a colon (`:`) to map the right value to another variable name.  

```
const obj = { 
    enabled: true, 
    darkMode: false, 
    stayLoggedIn: true 
}
const { enabled: activated, darkMode, stayLoggedIn } = obj
console.log(enabled, activated)

// Output:
undefined
true
```

Enter fullscreen mode Exit fullscreen mode

As you can see, the `obj.enabled` property got mapped to the variable `activated` instead of `enabled`. You can easily decide the names for your variables while keeping it's simplicity.

You can also destructure nested properties, it works just like you would expect it to.  

```
const obj = { 
    enabled: true, 
    settings: { 
        darkMode: false,
        stayLoggedIn: true
    } 
}
const { settings: { darkMode, stayLoggedIn } } = obj
console.log(darkMode, stayLoggedIn)

// Output:
false
true
```

Enter fullscreen mode Exit fullscreen mode

In this example, we mapped the nested properties to variables and didn't bother with any other values, they do not get deleted or anything by this, they just don't get mapped.

Destructuring can also be used to access properties of primitive types, like `String.length`.  

```
const string = 'awesome'
const { length } = string
console.log(length)

// Output:
7
```

Enter fullscreen mode Exit fullscreen mode

## [](#destructuring-arrays)Destructuring arrays

Arrays can also be destructured, they are guaranteed to preserve their order which means you can destructure it just like an object.  

```
const date = ['09', '04', '2001']
const day = date[0]
const month = date[1]
const year = date[2]
```

Enter fullscreen mode Exit fullscreen mode

As you can see, this is nearly the same as it was with the objects, before destructuring, we had to assign them separately after another which can take up a lot of lines in your code.  

```
const date = ['09', '04', '2001']
const [day, month, year] = date
console.log(day, month, year)

// Output:
09
04
2001
```

Enter fullscreen mode Exit fullscreen mode

You can also skip values by not specifying a variable name.  

```
const date = ['09', '04', '2001']
const [day, , year] = date
console.log(day, year)

// Output:
09
2001
```

Enter fullscreen mode Exit fullscreen mode

Nested arrays can also be destructured, just like nested objects.  

```
const nested = ['A', 'B', ['C', 'D'], 'E']
const [a, b, [c, d], e] = nested
console.log(a, b, c, d, e)

// Output:
'A'
'B'
'C'
'D'
'E'
```

Enter fullscreen mode Exit fullscreen mode

Object destructuring and array destructuring can be combined into one assignment and you can even use default parameters when destructuring, let me show you!  

```
const obj = { 
    enabled: true, 
    darkMode: false, 
    roles: ['user', 'admin', 'moderator']
}
const { 
    enabled, 
    date = new Date(), 
    darkMode, 
    roles: [userRole, , moderatorRole] 
} = obj
console.log(date)

// Output:
Wed Jun 17 2020 09:52:20 GMT+0200 (Central European Summer Time)
```

Enter fullscreen mode Exit fullscreen mode

## [](#rest-parameters)Rest parameters

Instead of allowing you to unpack or update objects and arrays, rest parameters makes it easy for you to create arrays with an indefinite amount of arguments.  
The syntax is the same as it is for spreading (`...`).  

```
const foo = (...args) => console.log(args)
foo('A', 'B', 'C', 'D')

// Output:
['A', 'B', 'C', 'D']
```

Enter fullscreen mode Exit fullscreen mode

As you can see, all arguments passed to `foo` were aggregated into the array `args`.

Rest parameter syntax can only be used in two ways, as the last parameter, catching all arguments that are not declared, or as the only parameter of a function, catching all arguments as shown above.  

```
const foo = (first, second, ...args) => console.log(first, second, args)
foo('A', 'B', 'C', 'D')

// Output:
A
B
['C', 'D']
```

Enter fullscreen mode Exit fullscreen mode

That's not everything, though!  

```
const { enabled, ...originalObject } = { 
    enabled: true, 
    darkMode: false,
    stayLoggedIn: true
}
console.log(enabled, originalObject)

// Output:
true
{darkMode: false, stayLoggedIn: true}
```

Enter fullscreen mode Exit fullscreen mode

As you can see, objects can also be destructured using rest parameter syntax, but it is also possible with arrays, let me show you!  

```
const [first, second, ...rest] = ['A', 'B', 'C', 'D']
console.log(first, second, rest)

// Output:
A
B
['C', 'D']
```

Enter fullscreen mode Exit fullscreen mode

## [](#tldr)TLDR:

*   [Spreading](#Spreading) can be used to unpack arrays and objects
*   [Destructuring](#Destructuring) can be used to create multiple variables from arrays or objects
*   [Rest parameters](#Rest-parameters) can be use to create arrays with indefinite size

You should definitely be using them in your next project! Have fun experimenting with these three techniques.
