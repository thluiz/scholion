---
url: "https://www.infoworld.com/article/3665748/8-new-javascript-features-to-start-using-today.html#tk.rss_all"
captured_at: "2022-07-07T17:15:37-03:00"
title: "8 new JavaScript features to start using today | InfoWorld"
domain: "infoworld-com"
---

# 8 new JavaScript features to start using today

### New features in ECMAScript 2022 include top-level await, RegExp match indices, new public and private class fields, and more. Let's get started!

By [Matthew Tyson](https://www.infoworld.com/author/Matthew-Tyson/)

Software Architect,
InfoWorld |
Jul 7, 2022 3:00 am PDT

![field-note_play-book_playbook_map_navigation_journey_by-hello-i-m-nik-via-unsplash-100813507-large.jpg](infoworld-com--8-new-javascript-features-to-start-using-today/ba4f4bcdd6038e43e02bf05df588582b.jpg)

[Hello I'm Nik](https://unsplash.com/photos/YiRQIglwYig)
[(CC0)](https://creativecommons.org/publicdomain/zero/1.0/)

ECMAScript 2022 (ES13) dropped on June 22, codifying the latest batch of new features for JavaScript. Every technology specification is a milestone in an ongoing dance with real-world usage. As developers use JavaScript, we continually discover opportunities and push the language into new territory. The ECMAScript specification responds by formalizing new features. These, in turn, establish a new baseline for JavaScript's continuing evolution.

The ES13 specification brings in [eight new features for JavaScript](https://github.com/tc39/proposals/blob/main/finished-proposals.md). Let's get started with these new features that you can use today.

## Class fields

[Class fields](https://github.com/tc39/proposal-class-fields) is an umbrella proposal that encompasses several improvements for handling members on JavaScript classes: [Class public and private instance fields](https://github.com/tc39/proposal-class-fields), [private instance methods and accessors](https://github.com/tc39/proposal-private-methods), and [static class features](https://github.com/tc39/proposal-static-class-features).

#### [ [Also on InfoWorld: 8 great JavaScript language features in ES12](https://www.infoworld.com/article/3658393/8-great-new-javascript-language-features-in-es12.html) ]

### Public and private instance fields

Previously, the standard approach when declaring a member field inside the `class` keyword was to introduce it in the constructor. The newest ECMAScript specification lets us define the member field inline as part of the class body. As shown in Listing 1, we can use a hashtag to denote a private field.

#### Listing 1. Inline public and private class fields

```
classSong{
    title ="";#artist = "";
    constructor(title, artist){this.title = title;this.#artist = artist;}}let song1 =newSong("Only a Song","Van Morrison");
console.log(song1.title);// outputs “Only a Song”
console.log(song1.artist);// outputs undefined
```

In Listing 1, we define a class, `Song`, using the `class` keyword. This class has two members, `title` and `artist`. The `artist` member is prefixed with a hash (#) symbol, so it is private. We allow for setting these fields in the constructor. Notice that the constructor must access `this.#artist` with the hash prefix again; otherwise, it would overwrite the field with a public member.

Next, we define an instance of the `Song` class, setting both fields via the constructor. We then output the fields to the console. The point is that `song1.artist` is not visible to the outside world, and outputs undefined.

Note, also, that even `song1.hasOwnProperty("artist")` will return false. Additionally, we cannot create private fields on the class later using assignment.

**[  [REGISTER NOW for CIO 100: Symposium & Awards Conference, August 15-17](https://bit.ly/3GcB9CY)  ]**

Overall, this is a nice addition, making for cleaner code. Most browsers have supported public and private instance fields for a while and it’s nice to see them officially incorporated.

### Private instance methods and accessors

The hash symbol also works as a prefix on methods and accessors. The effect on visibility is exactly the same as it is with private instance fields. So, you could add a private setter and a public getter to the `Song.artist` field, as shown in Listing 2.

#### Listing 2. Private instance methods and accessors

```
classSong{
  title ="";#artist = "";
  constructor(title, artist){this.title = title;this.#artist = artist;}get getArtist(){returnthis.#artist;}set#setArtist(artist) {this.#artist = artist;}}
```

### Static members

The class fields proposal also introduces static members. These look and work similarly to how they do in Java: if a member has the `static` keyword modifier, it exists on the class instead of object instances. You could add a static member to the `Song` class as shown in Listing 3.

#### Listing 3. Add a static member to a class

```
classSong{static label ="Exile";}
```

The field is then only accessible via the class name, `Song.label`. Unlike Java, the JavaScript instances do not hold a reference to the shared static variable. Note that it is possible to have a static private field with static `#label`; that is, a private static field.

## RegExp match indices

Regex `match` has [been upgraded](https://github.com/tc39/proposal-regexp-match-indices) to include more information about the matching groups. For performance reasons, this information is only included if the `/d` flag is added to the regular expression. (See the [RegExp Match Indices for ECMAScript](https://github.com/tc39/proposal-regexp-match-indices) proposal for a deep dive on the meaning of `/d` regex.)

Basically, using the `/d` flag causes the regex engine to include the start and end of all matching substrings. When the flag is present, the `indices` property on the `exec` results will contain a two-dimensional array, where the first dimension represents the match and the second dimension represents the start and end of the match.

In the case of named groups, the indices will have a member called `groups`, whose first dimension contains the name of the group. Consider Listing 4, which is taken [from the proposal](https://github.com/tc39/proposal-regexp-match-indices#examples).

#### Listing 4. Regex group indices

```
const re1 =/a+(?<Z>z)?/d;// block 1const s1 ="xaaaz";const m1 = re1.exec(s1);
m1.indices[0][0]===1;
m1.indices[0][1]===5;
s1.slice(...m1.indices[0])==="aaaz";// block 2
m1.indices[1][0]===4;
m1.indices[1][1]===5;
s1.slice(...m1.indices[1])==="z";// block 3
m1.indices.groups["Z"][0]===4;
m1.indices.groups["Z"][1]===5;
s1.slice(...m1.indices.groups["Z"])==="z";// block 4const m2 = re1.exec("xaaay");
m2.indices[1]===undefined;
m2.indices.groups["Z"]===undefined;
```

In Listing 4, we create a regular expression that matches the `a` char one or more times, followed by a named matching group (named `Z`) that matches the `z` char zero or more times.

Code block 1 demonstrates that `m1.indices[0][0]` and `m1.indices[0][1]` contain 1 and 5, respectively. That is because the first match for the regex is the string from the first `a` to the string ending in `z`. Block 2 shows the same thing for the `z` character.

Block 3 shows accessing the first dimension with the named group via `m1.indices.groups`. There is one matched group, the final `z` character, and it has a start of 4 and an end of 5.

Finally, block 4 demonstrates that unmatched indices and groups will return undefined.

The bottom line is that if you need access to the details of where groups are matched within a string, you can now use the regex match indices feature to get it.

## Top-level await

The ECMAScript specification now includes the ability to package asynchronous modules. When you import a module wrapped in `await`, the including module will not execute until all the `await`s are fulfilled. This avoids potential race conditions when dealing with interdependent asynchronous module calls. See the [top-level await proposal](https://github.com/tc39/proposal-top-level-await) for details.

Listing 5 includes an example borrowed from the [proposal](https://github.com/tc39/proposal-top-level-await#solution-top-level-await).

#### Listing 5. Top-level await

```
// awaiting.mjsimport{ process }from"./some-module.mjs";constdynamic=import(computedModuleSpecifier);const data = fetch(url);exportconst output = process((await dynamic).default, await data);// usage.mjsimport{ output }from"./awaiting.mjs";exportfunction outputPlusValue(value){return output + value }

console.log(outputPlusValue(100));
setTimeout(()=> console.log(outputPlusValue(100),1000);
```

Notice in `awaiting.mjs` the `await` keyword in front of its use of dependent modules `dynamic` and `data`. This means that when `usage.mjs` imports `awaiting.mjs`, `usage.mjs` will not be executed until `awaiting.mjs` dependencies have finished loading.

## Ergonomic brand checks for private fields

As developers, we want code that is comfortable—ergo [ergonomic private fields](https://github.com/tc39/proposal-private-fields-in-in). This new feature lets us check for the existence of a private field on a class without resorting to exception handling.

Listing 6 shows this new, ergonomic way to check for a private field from within a class, using the `in` keyword.

#### Listing 6. Check for the existence of a private field

```
classSong{#artist; 
  checkField(){return#artist in this;}}let foo =newSong();
foo.checkField();// true
```

Listing 6 is contrived, but the idea is clear. When you find yourself needing to check a class for a private field, you can use the format: `#fieldName in object`.

## Negative indexing with .at()

Gone are the days of `arr[arr.length -2]`. The [.at method](https://github.com/tc39/proposal-relative-indexing-method) on built-in indexables now supports negative indices, as shown in Listing 7.

#### Listing 7. Negative index with .at()

```
let foo =[1,2,3,4,5];
foo.at(3);// == 3
hasOwn
```

## hasOwn

[Object.hasOwn](https://github.com/tc39/proposal-accessible-object-hasownproperty) is an improved version of `Object.hasOwnProperty`. It works for some edge cases, like when an object is created with `Object.create(null)`. Note that `hasOwn` is a static method—it doesn’t exist on instances.

#### Listing 8. hasOwn() in action

```
let foo =Object.create(null);
foo.hasOwnProperty =function(){};Object.hasOwnProperty(foo,'hasOwnProperty');// Error: Cannot convert object to primitive valueObject.hasOwn(foo,'hasOwnProperty');// true
```

Listing 8 shows that you can use `Object.hasOwn` on the `foo` instance created with `Object.create(null)`.

## Class static block

Here’s a chance for Java developers to say, *Oh, we’ve had that since the '90s*. ES 2022 introduces [static initialization blocks](https://github.com/tc39/proposal-class-static-block) to JavaScript. Essentially, you can use the `static` keyword on a block of code that is run when the class is loaded, and it will have access to static members.

Listing 9 has a simple example of using a static block to initialize a static value.

#### Listing 9. Static block

```
classFoo{static bar;static{this.bar =“test”;}}
```

## Error cause

Last but not least, the `Error` class now [incorporates cause support](https://github.com/tc39/proposal-error-cause). This allows for Java-like stack traces in error chains. The error constructor now allows for an options object that includes a `cause` field, as shown in Listing 10.

#### Listing 10. Error cause

```
thrownewError('Error message',{ cause: errorCause });
```
