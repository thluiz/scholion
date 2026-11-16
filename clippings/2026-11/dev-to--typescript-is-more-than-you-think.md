---
url: "https://dev.to/macsikora/typescript-is-more-than-you-think-2nbf"
captured_at: "2026-11-16T01:53:05+00:00"
title: "TypeScript is more than you think"
domain: "dev-to"
---

TypeScript - commonly known as JS and additional type annotations, it's correct way of describing it, but hides the potential which lies in the language. What if I would describe TypeScript as far more than that, as two languages in one shell?

TypeScript like every statically typed language has two levels - value and type level. Value level can be simply considered as just JavaScript, the whole grammar and syntax works at this level exactly like JS specification says should work. The second level - type level is the syntax and grammar which was created specially for TypeScript. TS has even more, we can distinguish three levels of the language - Type System Language, Type Annotations and the last but not least JavaScript.

[![TypeScript levels](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fuu5votoyq4kutnlkxcnk.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fuu5votoyq4kutnlkxcnk.png)

> **Note** type annotations level is a place where type system meets JS, so these are all annotations like `a: T` and assertions `a as T`.

The article will introduce to you, **TypeScript type system (TSts)** as a fully flavored language by itself, so be prepared 💪.

## [](#typescript-type-system-languagetsts)TypeScript type system language(TSts)🟦

When we think about any language, we consider values, variables, expressions, operators, functions. We have tools for performing data flow, we can branch the flow by conditions, we can iterate the flow by iterations or recursions. Lets investigate how much of these things can be seen in TypeScript type system?

## [](#values-and-variables)Values and variables

What stands for value in TS type system? It's a type, value at this level is represented as a type. We can assign the value to the variable by typical assign operator.  

```
// TSts🟦
type X = string;
type Y = number;
type Z = boolean;
```

Enter fullscreen mode Exit fullscreen mode

At the left we have alias, name which we set for the value, on the right side we have the value. Variable `X` has value `string`.

> **Note** I say variable because variable is a term we all programmers know, in TS there are only single assignment variables, so we cannot re-declare the value, naturally then its like JS `const`
> 
> **Note** Type in TSts is not only like const, but also like immutable const, as it cannot be mutated. We can compose types but never change the original one.  

```
type X = 1;   /* is TSts🟦 equivalent for JS🟨 : */ const X = 1;
```

Enter fullscreen mode Exit fullscreen mode

## [](#types-of-types)Types of types

In the next part of the article I will use such terms:

*   `type` is the same thing as `value`
*   `value` is the same thing as `type`
*   `kind` is a type of the type

**Kind** can be something new here, in TypeScript type system, kind is something which defines another type shape, in the same way at JS level type annotation defines a JS value shape.  

```
X extends string /*is TSts🟦 equivalent for annotated JS🟨 */ const X: string
```

Enter fullscreen mode Exit fullscreen mode

## [](#operators)Operators

Not surprisingly type level TypeScript has its own operators, below some of them

*   `A = B` assign
*   `A & B` intersection
*   `A | B` union
*   `keyof A`
*   `A extends B ? C : D` condition
*   `K in T` iteration

```
// TSts🟦
type Z = X | Y // Z is either X or Y
type D = A & B | C // D is combined A and B or C
type Keys = keyof {a: string, b: boolean} // get property keys in form of union
```

Enter fullscreen mode Exit fullscreen mode

## [](#conditions-and-equality)Conditions and equality

As I wrote we have possibility to do conditions by condition operator(conditional type as TS docs say), how about checking if something is equal to another thing? In order to achieve such we need to understand that when we ask `A extends B` it means if `A` then `B` and `A` can be used as `B`, what conveys equality in the one direction (operation is not commutative), if `A extends B` it doesn't implies that `B extends A`. To check equality we need to perform the check in both directions.  

```
// TSts🟦
type A = string
type B = "1"
type AisB = A extends B ? true : false // false
type BisA = B extends A ? true : false // true
```

Enter fullscreen mode Exit fullscreen mode

As you can see `B` can be used as `A` but not in other way round.  

```
// TSts🟦
type A = 1
type B = 1
type AisBandBisA = A extends B ? B extends A ? true : false : false // true
```

Enter fullscreen mode Exit fullscreen mode

Above is full equality check, we check in two directions, and then types are considered equal.

> **Note** the equality implemented like that has some gotchas and doesn't properly work in some cases. Example of such case you can find in [the playground](https://www.typescriptlang.org/play/#code/C4TwDgpgBAGlC8UDeUCGAuKBnYAnAlgHYDmANFAEYD8mFA9nQDYSqFQC+AUKJFAJoJkaTDgIlyAYxqUGzVl27hoASSwBRAI4BXVIwA8AQXIAhAHydBBqBAAewCIQAmWKMagWqr63YfOoVjyg8LWgLTAAzXSxQqCgIqIhORV4AJUFVTR19GHI+UygAegKg3BCLIA). Special thanks for [Titian Cernicova Dragomir](https://twitter.com/TitianCernicova) for this remark.
> 
> **Note** This naive implementation works also incorrectly for union types
> 
> **Note** Very important to mention is the fact that such conditions and equality work in a logical way for sound types, but TS has also unsound ones like `any, unknown, never`, these types can give us quite surprising results and equality doesn't work correctly for these types.

## [](#functions)Functions

Functions are something fundamental for basic abstraction. Fortunately in TS type system there are functions, functions working with types which are commonly named - generic types. Lets create a function which will check any two values to be equal:  

```
// TSts🟦
type IsEqual<A, B> = A extends B ? B extends A ? true : false : false
// use it
type Result1 = IsEqual<string, number> // false
type Result2 = IsEqual<1, 2> // false
type Result3 = IsEqual<"a","a"> // true 
```

Enter fullscreen mode Exit fullscreen mode

Function `IsEqual` has two arguments `A, B` which can be every type. So function works with any kind of type (single arity kind `*`). But we can create functions with more precised arguments requirements.  

```
// TSts🟦
type GetLength<A extends Array<any>> = A['length']
type Length = GetLength<['a', 'b', 'c']> // evaluates to 3 
```

Enter fullscreen mode Exit fullscreen mode

Function `GetLength` is a function which works only with types being an `Array<any>` kind. Take a look again at these two functions, if I put them right before JS functions what would you see?  

```
// TSts🟦
type IsEqual<A, B>
 = A extends B 
 ? B extends A 
 ? true 
 : false 
 : false
// JS🟨
const isEqual = (a:any, b: any) => a == b ? b == a ? true : false : false

// TSts🟦
type GetLength<A extends Array<any>> = A['length']
// JS🟨
const getLength = (a: Array<any>) => a['length']
```

Enter fullscreen mode Exit fullscreen mode

Almost the same thing, don't you think? I hope now you are quite convinced that popular generic types are just functions evaluated at the compile time 💪

## [](#composing-functions)Composing functions

If we have functions, then it is natural to think there is possibility to call one function in another. As an example lets reuse written before `IsEqual` function and use it inside body of another function `IfElse`.  

```
// TSts🟦
type IfElse<A, B, IfTrue, IfFalse> =
    IsEqual<A, B> extends true ? IfTrue : IfFalse

type Result1 = IfElse<0, 1, 'Equal', 'Not Equal'> // Not Equal
type Result2 = IfElse<1, 1, 'Equal', 'Not Equal'> // Equal
```

Enter fullscreen mode Exit fullscreen mode

## [](#local-variables)Local variables

We have functions, we have also variables, but can we have function local scope variables? Again yes, at least we can have some illusion of them which is quite handy.  

```
// TSts🟦
type MergePropertyValue<
    A,
    B,
    Prop extends (keyof A & keyof B),
    _APropValue = A[Prop], // local variable
    _BPropValue = B[Prop]> // local variable
= _APropValue | _BPropValue // sum type

// JS🟨 take a look at similar JS function but working at assumed number fields
function mergePropertyValue(a, b, prop) {
 const _aPropValue = a[prop];
 const _bPropValue = b[prop];
 return _aPropValue  + _bPropValue; // sum
}
```

Enter fullscreen mode Exit fullscreen mode

In the list of arguments, at the end we can put local variables and assign value to them, it is a great tool for aliasing evaluated constructs. In above example we didn't gain a lot, but such local aliases can be handy if the type is more complicated, and we can also use other function there! Let's try to make equality check for three arguments.  

```
// TSts🟦
type AreEqual<
    A,
    B,
    C,
    _AisB = IsEqual<A, B>,
    _BisC = IsEqual<B, C>,
    > = _AisB extends true ? IsEqual<_AisB, _BisC> : false

type Result = AreEqual<1,1,1> // true
type Result2 = AreEqual<1, 2, 1> // false
type Result3 = AreEqual<'A', 'A', 'A'> // true
type Result4 = AreEqual<'A', 'A', 'B'> // false
```

Enter fullscreen mode Exit fullscreen mode

In above definition `_AisB` and `_BisC` can be considered as local variables of `AreEqual` function.

> **Note** issue with saying that these are local variables is in a fact that we can ruin our type behavior from outside by setting those arguments like `AreEqual<1, 1, 1, false, false>`.
> 
> **Note** underscore which I have used above for local variables is only convention. The purpose is to give a hint that these arguments should not be touched.

## [](#loops)Loops

Every language has a way to iterate over a data structure, **TSts** isn't here an exception.  

```
// TSts🟦
type X = {a: 1, b: 2, c: 3}
type Y = {
  [Key in keyof X]: X[Key] | null
} // {a: 1 | null, b: 1 | null, c: 1 | null}
```

Enter fullscreen mode Exit fullscreen mode

Type `Y` is evaluated by iterating in `for in` loop style over type `X`, to every field of `X` we append additional value `null`. **TSts** can do more, we can even just do iteration, lets say from 0 to 5.  

```
// TSts🟦
type I = 0 | 1 | 2 | 3 | 4 | 5

type X = {
  [Key in I]: Key
}
// X is [0, 1, 2, 3, 4, 5]

// JS🟨 look at JS similar code
const x = []
for (let i = 0; i<= 6; i++) {
  x.push(i);
}
```

Enter fullscreen mode Exit fullscreen mode

We just have generated type which represents 6-elements array with values from 0 to 5. Its amazing, on the type level we have iterated from `i=0` to `i=5` and pushed `i` to array. Looks like `for loop` doesn't it?

> **Caution** Hey reader 👋, remember all the time we talk about types, every time I say value its the same as type. 0,1... above are types which have only single exactly the same JS runtime representation, but still we work with types only.

## [](#recursion)Recursion

Recursion is a situation when function inside the definition call itself. Can we call the same function inside its body? Yes we can!  

```
// TSts🟦
type HasValuesOfType<T extends object, F> = ({
    [K in keyof T]: T[K] extends F ? true : T[K] extends object ? HasValuesOfType<T[K], F> : false
}[keyof T]) extends false ? false : true
```

Enter fullscreen mode Exit fullscreen mode

Above function `HasValuesOfType` is traversing argument being an kind of object (type of types). Function is checking if the value of the property has given type, if yes, its saying `true`, if not, it does the recursive call to itself if the property is also an object. In the result function will tell us if at any level of the type there exists the wanted type.

## [](#mapping-filtering-and-reducing)Mapping, filtering and reducing

The language is capable of conditions, looping recursion, lets try to use those tools in order to transform types.

### [](#mapping)Mapping

```
// TSts🟦
type User = {
    name: string,
    lastname: string
}
type MapUsers<T extends Array<User>> = {
    [K in keyof T]: T[K] extends User ? { name: T[K]['name'] } : never 
}
type X = [{
    name: 'John',
    lastname: 'Doe'
}, {
    name: 'Tom',
    lastname: 'Hanks'
}]

type Result = MapUsers<X> // [{name: 'John'}, {name: 'Tom'}]
```

Enter fullscreen mode Exit fullscreen mode

Function `MapUsers` works with array of users kind, and maps every user by removing `lastname`. Take a look how we map - `{ name: T[K]['name']}`, in every iteration over the type `T`, we get value at this point `T[K]` and take `name` property which we put to the new value.

### [](#filtering)Filtering

**TSts** gives us tools for simple filtering object types. We can make function `FilterField` which will perform removing field from an object kind of value.  

```
// TSts🟦
type FilterField<T extends object, Field extends keyof T> = {
    [K in Exclude<keyof T, Field>]: T[K]
}
// book
type Book = {
    id: number,
    name: string,
    price: number
}
type BookWithoutPrice = FilterField<Book, 'price'> // {id: number, name: string}
```

Enter fullscreen mode Exit fullscreen mode

> **Note** filtering tuple types is not so simple, language doesn't support it without very sophisticated tricks which are outside the scope of this article.

`FilterField` is doing iteration over `T`, but by using `Exclude` it is excluding `Field` from list of keys, in result we get object type without this field.

> **Note** there is utility type `Pick` and `Omit` which can be used instead of `FilterField`

### [](#reducing)Reducing

Reducing or folding is a transforming data from a shape `A` 🍌 into some other shape `B` 🌭. Can we do that and transform data from kind `A` to kind `B`? Sure we can 😎, even we did that already in previous examples. Lets for example sum how many properties has our object given as argument. Caution this one can be hard to grasp, but what I want to show here is a power of the language:  

```
// TSts🟦
type Prepend<T, Arr extends Array<any>> = ((a: T, ...prev: Arr) => any) extends ((...merged: infer Merged) => any) ? Merged : never

type KeysArray<T extends object, ACC extends Array<any> = []> = ({
    [K in keyof T]: {} extends Omit<T, K> ? Prepend<T[K], ACC> : KeysArray<Omit<T, K>, Prepend<T[K], ACC>>
}[keyof T]);

type CountProps<T extends object, _Arr = KeysArray<T>> = _Arr extends Array<any> ? _Arr['length'] : never;

type Y = CountProps<{ a: 1, b: 2, c: 3, d: 1 }> // Evaluates to 4
```

Enter fullscreen mode Exit fullscreen mode

Yes a lot of code, yes quite complicated, we needed to use some additional helper type `Prepend` and `KeysArray`, but finally we were able to count the number of properties in the object, so we've reduced the object from `{ a: 1, b: 2, c: 3, d: 4 }` to `4` 🎉.

### [](#tuple-transformations)Tuple transformations

TypeScript 4.0 introduced [variadic tuple types](https://github.com/microsoft/TypeScript/pull/39094) which gives more tools to our TSts language level. We now very easily can remove, add elements or merge tuples.  

```
// merging two lists
// TSts🟦
type A = [1,2,3];
type B = [4,5,6];
type AB = [...A, ...B]; // computes into [1,2,3,4,5,6]

// JS🟨 - the same looking code at value level
const a = [1,2,3];
const b = [1,2,3];
const ab = [...a,...b];

// push element to the lists
// TSts🟦
type C = [...A, 4]; // computes into [1,2,3,4]
// JS🟨 - the same looking code at value level
const c = [...a, 4];

// unshift element to the list
// TSts🟦
type D = [0, ...C]; // computes into [0,1,2,3,4]
// JS🟨 - the same looking code at value level
const d = [0, ...c];

```

Enter fullscreen mode Exit fullscreen mode

As we can see thanks to variadic tuple types, operations on tuples at TSts look very similar to operations on Arrays in JS with using spread syntax.

> **Note** Tuple type at our type level can be considered just as a list.

### [](#string-concatenation)String concatenation

Concatenation of strings for TS > 4.1 is also not a problem anymore. We can glue strings at the type level in almost the same way we do that in value level.  

```
// concatenate two strings
// TSts🟦
type Name = "John";
type LastName = "Doe";
type FullName = `${Name} ${LastName}`; // "John Doe"

// JS🟨 - the same looking code at value level 🤯
const name = "John";
const lastName = "Doe";
const fullName = `${name} ${lastName}`;
```

Enter fullscreen mode Exit fullscreen mode

What about concatenation of strings in the list?  

```
// TSts🟦
type IntoString<Arr extends string[], Separator extends string, Result extends string = ""> = 
    Arr extends [infer El,...infer Rest] ? 
            Rest extends string[] ?
            El extends string ?
            Result extends "" ?
            IntoString<Rest, Separator,`${El}`> :
            IntoString<Rest, Separator,`${Result}${Separator}${El}`> :
            `${Result}` :
            `${Result}` :
            `${Result}`


type Names = ["Adam", "Jack", "Lisa", "Doroty"]
type NamesComma = IntoString<Names, ","> // "Adam,Jack,Lisa,Doroty"
type NamesSpace = IntoString<Names, " "> // "Adam Jack Lisa Doroty"
type NamesStars = IntoString<Names, "⭐️"> // "Adam⭐️Jack⭐️Lisa⭐️Doroty"
```

Enter fullscreen mode Exit fullscreen mode

Above example maybe looks little bit more complicated, but proves that we can have generic type level function which will concatenate strings with given separator.

## [](#higher-order-functions)Higher order functions?

Is **TSts** functional language, is there possibility to pass functions and return functions? Below some naive try example  

```
// TSts🟦
type ExampleFunction<X> = X // identity function
type HigherOrder<G> = G<1> // 🛑 higher order function doesn't compile
type Result = HigherOrder<ExampleFunction> // 🛑 passing function as argument doesn't compile
```

Enter fullscreen mode Exit fullscreen mode

Unfortunately (or fortunately) there is no such option, at type level that sort of thing has a name - **Higher Kinded Types**, such constructs are available in for example Haskell programming language.

It also means we cannot create polymorphic functions like map, filter and reduce, as those functional constructs demand kind `* -> *`(function) as argument.

## [](#standard-library)Standard library

Every language has some standard library, no difference with TypeScript type level language. It has standard library, called in official documentation ["utility types"](https://www.typescriptlang.org/docs/handbook/utility-types.html). Despite the name, utility types are type level functions included in TypeScript. These functions can help with advanced type transformations without the need of writing everything from scratch.

## [](#in-summary)In summary

TypeScript type system **TSts** is something which should be considered as fully flavored language, it has all the things any language should have, we have variables, functions, conditions, iterations, recursion, we can compose, we can write sophisticated transformations. Type system is expression based and operates only on immutable values(types). It has no higher order functions, but it doesn't mean will not have them 😉.

Additional links:

*   [TypeScript is Turing complete](https://github.com/Microsoft/TypeScript/issues/14833)
*   [Binary Arithmetic in TypeScript's Type System](https://www.youtube.com/watch?v=7lyb22x9tcM)
*   [TS toolbelt - library with functions for type level TS](https://pirix-gh.github.io/ts-toolbelt/4.2.1/)
*   [Advanced TypeScript Exercises series](https://dev.to/macsikora/advanced-typescript-exercises-question-1-45k4)

If you want to know about TypeScript and interesting things around it please follow me on [dev.to](https://dev.to/macsikora) and [twitter](https://twitter.com/macsikora).
