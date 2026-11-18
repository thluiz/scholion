---
url: "https://web.archive.org/web/20191119080207id_/https://dev.to/duomly/what-s-new-es2019-brings-48d7"
captured_at: "2026-11-18T12:05:52+00:00"
title: "ES2019 new features"
domain: "web-archive-org"
---

### [twitter logo](http://twitter.com/duomly) Nov 18 ・4 min read

Every year since 2015, new ECMAScript features are released. Creating a new ECMAScript standard has four stages, from stage 0 to stage 3 it is mostly planning, and drafts and stage 4 is final. It’s possible to use the newest features in Google Chrome version 72. Let’s take a look at what exactly ES2019 brings us:

*   Object.fromEntries(),
*   trimStart() and trimEnd(),
*   flat(),
*   flatMap(),
*   Symbol object description property,
*   catch optional binging,
*   well formatted JSON.stringify,

Let’s go one by one and check how we can use this brilliant new features.

#### 1\. Object.fromEntries();

Converting data in Javascript is very common, and almost every update of ECMAScript brings new, simple methods to do it. In ES2017 creators brought a new method Object.entries(), used to convert objects into arrays. But there was no way to do it in an opposite way, to convert key-value pair array into an object with one simple method.

And here it is, ES2019 brings us new feature, Object.fromEntries() which allows transforming an array of key-value pairs into an object.

Let’s check out how it’s possible to revert Object.entries method using ES2019 new feature Object.fromEntries():  

```
var car = {
make: 'Volvo',
seats: 4,
year: 2018,
}

console.log(Object.entries(car)); // [['make', 'Volvo], ['seats', 4], ['year', 2018]];

var carArr = [['make', 'Volvo'], ['seats', 4], ['year', 2018]];
console.log(Object.fromEntries(carArr)); // { make: 'Volvo', seats: 4, year: 2018 };
```

From the above code, we can see that now reversing Object.entries result is very easy.

#### 2\. trimStart() and trimEnd()

String manipulations are very common when working with Javascript on the front-end. Sometimes we need to adjust strings to needed format, and we need to trim part of the string. ES2019 brings us two useful features that may be used for this purpose: trimStart() and trimEnd(). trimStart() method removes whitespaces from the beginning of the string, and trimEnd() obviously trims whitespaces from the end of the string.

Let’s take a look at a code example:  

```
var string = '    string to trim     ';

console.log(string.trimStart()); // 'string to trim     '
console.log(string.trimEnd()); // '    string to trim'

```

This one looks pretty simple, right?

#### 3\. flat()

The new array .flat() method creates a new array with sub-arrays elements concentrated in a recursive way until specific depth. The depth is one by default, but it may be set as a parameter, or it may be set to Infinity to be sure that all the sub-arrays will be flattened.

Let’s see a code example:  

```
var array = [1, 2, [4, 4, [4, 7, [20, 1]]]];

console.log(array.flat()); // [1, 2, 4, 4, [4, 7, [20, 1]]]; 
console.log(array.flat(2)); // [1, 2, 4, 4, 4, 7, [20, 1]];
console.log(arra.flat(Infinity)); // [1, 2, 4, 4, 4, 7, 20, 1];
```

In the first usage of .flat() method, it concentrates only one level array as this is the default depth. In another console.log I defined two depth, and it concentrates two-level sub-arrays and the last console.log we set depth level to Infinity, and it concentrates all levels of our array.

#### 4\. flatMap()

If you work with an array a lot probably, you know how useful is .map() method, which allows iterate through the array and perform any function on every element. The .flatMap() method is a combination of .map() and .flat().

Let’s take a look at a code example:  

```
var array = [1, 23, [10, 43]];
console.log(array.flatMap(item => item + 2)); // [3, 25, 12, 45];
```

It seems like a very useful method.

#### 5\. Symbol object description property

The symbol was introduced as a new feature in ES6. Description in Symbols is added mainly for debugging purposes, but until now developers had to convert it to string to be able to access description with console.log. Now with the version from 2019 its possible to access description by Symbol.description.  

```
var symbolDesc = 'This is Symbol';
var symbolObj = Symbol(symbolDesc);

console.log(symbolObj.description); // 'This is Symbol';
```

#### 6\. Catch optional binding

Lots of developers use try…catch statement, and until now usage of binding in catch was required to avoid SyntaxError, but it wasn’t used in some cases. Let’s take a look at the code example before ES2019:  

```
try {
  ...
} catch (value) {
  ...
}
```

After ES2019:  

```
try {
  ...
} catch {
  ...
}
```

In the above example, we can see that value in the catch statement is not needed, and in this case, it’s a great possibility to skip it with the newest version of ECMAScript.

#### 7\. JSON.stringify superset

Usage of JSON.strignify is quite common when using Javascript. This change in ES2019 was introduced to prevent JSON.stringify() method from returning ill-formed Unicode strings. Now JSON.stringify() will present surrogate code points as strings and while we use JSON.parse() it will be transformed into the original representation.

Let’s take a look at some example:  

```
JSON.stringify('\uDF06\uD834'); // '"\\udf06\\ud834"'
JSON.stringify('\uDEAD'); // '"\\udead"'
```

#### Conclusion

ES2019 brings us lots of useful features which will make our development process much more pleasant. In this article, I’ve gone through the most important ones: Object.fromEntries(), trimStart() and trimEnd() string methods, flat() and flatMap() array methods, new description property for Symbol, catch optional binding and JSON.stringify() superset.

If you are not familiar with any of the updates from previous years, I encourage you to check out our [last article](https://www.blog.duomly.com/the-most-useful-features-in-the-latest-javascript-since-es6/) and start developing your code with the newest features.

Have a nice coding!

[![Duomly - programming online courses](https://res.cloudinary.com/practicaldev/image/fetch/s--9LQzXcAz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/i5p1tl4bym00d9shuyfp.png)](https://www.duomly.com/)

 [![twitter logo](https://practicaldev-herokuapp-com.freetls.fastly.net/assets/twitter-99c56e7c338b4d5c17d78f658882ddf18b0bbde5b3f42f84e7964689e7e8fb15.svg)](https://twitter.com/intent/tweet?text=%22ES2019%20new%20features%22%20by%20@duomly%20%23DEVcommunity%20https://dev.to/duomly/what-s-new-es2019-brings-48d7)[DISCUSS (1)](#comments)

![Copy to Clipboard](https://practicaldev-herokuapp-com.freetls.fastly.net/assets/content-copy-d564d822fccd292272dc5db1b788fe414691a408b10ccf1b34dfc366bd19eeeb.svg)

[![duomly profile](https://res.cloudinary.com/practicaldev/image/fetch/s--zubA6_yK--/c_fill,f_auto,fl_progressive,h_180,q_auto,w_180/https://thepracticaldev.s3.amazonaws.com/uploads/user/profile_image/191953/632861fe-ed9b-4849-8b2f-fa4c2cf4d492.png)](https://web.archive.org/duomly)

#### [Duomly](https://web.archive.org/duomly)

We believe everyone can learn how to code, so we are making learning fun and easy!
