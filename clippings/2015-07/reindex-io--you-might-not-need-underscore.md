---
url: "https://www.reindex.io/blog/you-might-not-need-underscore/"
captured_at: "2015-07-13T15:28:37-03:00"
title: "You Might Not Need Underscore | Reindex"
domain: "reindex-io"
---

# You Might Not Need Underscore

###### By [ville](https://www.reindex.io/blog/author/ville/ "Posts by ville") / In [JavaScript](https://www.reindex.io/blog/category/javascript/)

![22f25db4d7dad0dbe6f35bcb16283de0.png](reindex-io--you-might-not-need-underscore/22f25db4d7dad0dbe6f35bcb16283de0.png)

During past years utility libraries like [Underscore](http://underscorejs.org/) and [lodash](https://lodash.com/) have found their way into the toolchain of many JavaScript programmers.

While those utility libraries might make the code easier for you to *write*, they don’t necessarily make the code *simpler* or easier to *understand*. People reading and maintaining the code are obliged to, in addition to knowing the language and its standard library, also know the utility library it’s using. Libraries come and go, and everyone has their own favorite. What’s the order of arguments for this `map()` function? Which library was it from again? Underscore (the perennial favorite), lodash (its speedy and versatile younger brother), [Ramda](http://ramdajs.com/) (the more functional cousin that [got the argument order right](https://www.youtube.com/watch?v=m3svKOdZijA)), or whichever cool abstraction you found today? If you’re a team, whose favorite library should you choose? How about choosing the *standard library*?

When you write simple code that uses the standard library functions, you are making it easier for the future user and maintainer (who might as well be you) to understand. Yes, it might be more characters to type, but since when is writing speed the bottleneck in writing good, maintainable software?

> It’s much easier to recover from no abstraction than the wrong abstraction. —[Sebastian Markbåge](http://2014.jsconf.eu/speakers/sebastian-markbage-minimal-api-surface-area-learning-patterns-instead-of-frameworks.html)

It’s a lot easier to refactor verbose code with few abstractions than concise code with the wrong abstractions. When you start seeing patterns in your code repeated over and over, it’s time to abstract, but now you can tell what is the right abstraction and it’s more likely you end up with something that is worth the additional overhead *every* abstraction adds.

JavaScript is evolving and new ES2015 and ES2016 editions (previously known as ES6 and ES7, respectively) pack a bunch of new features and [Babel](https://babeljs.io/) makes it very easy to use of them today. These features make some previously essential functions from utility libraries obsolete.

Good resources for learning those new features include the [Learn ES2015](https://babeljs.io/docs/learn-es2015/) page on Babel website and [Understanding ECMAScript 6](https://leanpub.com/understandinges6/read) book by Nicholas C. Zakas. Learning to fully utilize the language of the Web gives you a transferable skill. JavaScript is likely to stick around much longer than the utility library of the day.

This is not to say there is no a place for any utility library or *function* installed from [npm](https://www.npmjs.com/) anymore. It’s just that many utility functions that were almost essential in order to be productive when we were writing ES3 are not needed anymore and today you might be better off just using plain JavaScript to do those tasks.

You might not need Underscore.

---

## Examples

These examples illustrate some things ES5.1, ES2015 and ES2016 have made so easy that you might not need an utility library anymore.

##### What do I need to use them?

**ES5** is now natively supported by all current browsers and Node.js. **ES2015** and **ES2016** examples can be [compiled to ES5 with Babel.](http://babeljs.io/docs/setup/) Babel is easy to add to almost any common JavaScript build tool in existence or to use with the require hook on Node.js. If you need to support legacy browsers (IE8, released 6 years ago) you can still get most of ES5 with a polyfill like [es-shim](https://github.com/es-shims/es5-shim).

### Arrays

#### Iterate

- Underscore

  ```
  _array iteratee
  ```
- ES5.1

  ```
  arrayforEachiteratee
  ```

- Underscore

  ```
  _array iteratee
  ```
- ES5.1

  ```
  arrayiteratee
  ```

- Underscore

  ```
  _array predicate
  ```
- ES2015

  ```
  arraypredicate
  ```

#### Get a property from each element in an array

- Underscore

  ```
  _pluckarray propertyName
  ```
- ES2015

  ```
  arrayvalue  valuepropertyName
  ```

#### Check if array includes an element

- Underscore

  ```
  _containsarray element
  ```
- ES2016

  ```
  arrayincludeselement
  ```

#### Convert an array-like object to array

- Underscore

  ```
  _toArrayarguments
  ```
- ES2015

  ```
  Arrayarguments
  ```

#### Create a copy of an array with all falsy values removed.

- Underscore

  ```
  _compactarray
  ```
- ES2015

  ```
  arrayfilterx  x
  ```

#### Create a copy of an array with duplicates removed

- Underscore

  ```
  _array
  ```
- ES2015

  ```
   array
  ```

#### Find the index of a value in an array

- Underscore

  ```
  _indexOfarray value
  ```
- ES5.1

  ```
  arrayindexOfvalue
  ```

#### Create an array with n numbers, starting from x

- Underscore

  ```
  _rangex x  n
  ```
- ES2015

  ```
  Array length n  v k  k  x
  ```

### Objects

#### Names of own enumerable properties

- Underscore

  ```
  _object
  ```
- ES5.1

  ```
  Objectobject
  ```

#### Names of all enumerable properties

- Underscore

  ```
  _allKeysobject
  ```
- ES2015

  ```
  Reflectenumerateobject  // Returns an Iterator
  ```

#### Values

- Underscore

  ```
  _valuesobject
  ```
- ES5.1

  ```
  Objectobjectkey  objectkey
  ```

#### Create a new object with the given prototype

- Underscore

  ```
  _createproto propertiesObject
  ```
- ES5.1

  ```
  Objectcreateproto propertiesObject
  ```

#### Create a new object from merged properties

- Underscore

  ```
  _extend source  a false
  ```
- ES2016

  ```
   source a false
  ```

#### Create a shallow clone of an object

- Underscore

  ```
  _cloneobject
  ```
- ES2016

  ```
   object
  ```

#### Check if an object is an array

- Underscore

  ```
  _isArrayobject
  ```
- ES5.1

  ```
  ArrayisArrayobject
  ```

#### Check if an object is a finite Number

- Underscore

  ```
  _isFiniteobject
  ```
- ES2015

  ```
  NumberisFiniteobject
  ```

### Functions

#### Bind a function to an object

- Underscore

  ```
  function  
    

  _objectfun object
  ```
- ES2015

  ```
  objectfunobject
  ```
- ES2016

  ```
  objectfun
  ```

### Utility

#### Identity function

- Underscore

  ```
  _identity
  ```
- ES2015

  ```
  value  value
  ```

#### A function that returns a value

- Underscore

  ```
  const fun  _constantvalue
  ```
- ES2015

  ```
  const fun    value
  ```

#### The empty function

- Underscore

  ```
  _
  ```
- ES2015

Did you find a bug? Do you have more examples of things that previously might have required an utility library, but not anymore? [Send us a pull request on GitHub!](https://github.com/reindexio/youmightnotneedunderscore)

[Discuss this post on Hacker News.](https://news.ycombinator.com/item?id=9794773)

Share this post:
