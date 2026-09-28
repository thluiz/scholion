---
url: "https://dasdocs.com/fsharp/1-succinct-fsharp.html"
captured_at: "2022-06-28T11:18:15-03:00"
title: "DasDocs"
domain: "dasdocs-com"
---

# Succinct FSharp

Page containing not just the syntax but walk you through FSharp concepts through examples and ample explanation.

# FSharp Interactive (fsi)

Probably the best way to learn F# is using FSharp Interactive (`fsi`). To use it, run `dotnet fsi`.

Things to note:

- To see all commands supported in `fsi`, run `#help;;`
- To quit the tool, run `#quit;;`
- To terminate your input (be it `fsi` command or your F# code), type `;;` at end before pressing Enter key.
- If you press enter after typing `#quit`, then `fsi` would wait for further input even after pressing Enter until you type `;;`.

## The `it` value

Run `3 + 2;;` in `fsi`. You'll see the following line:

```
val it: int = 5
```

Results of expressions like `3+2` will be evaluated and stored in a **value** called `it`.

In the above output, `it` has a type `int`.

You can reuse the `it` value:

```
> 3 + 2;;
val it: int = 5

> it + 10;;
val it: int = 15
```

You cannot try add `"10"` to `it` value above as `it`'s type is `int` and `"10"` is of `string` type.

The `+` operator accepts two values of the same type:

```
> it + "10";;

it + "10";;
  -----^^^^

stdin(4,6): error FS0001: The type 'string' does not match the type 'int'
```

- `it` value cannot be mutated:

```
> it <- 23 ;;

  it <- 23 ;;
  ^^^^^^^^

stdin(6,1): error FS0027: This value is not mutable. Consider using the mutable keyword, e.g. 'let mutable it = expression'.
```

# Bindings and `let` keyword

**Binding** is associating a name with a value or a function. You cannot change the value or function associated with the name.

- This would be similar to declaring and initializing a constant variable in languages such as C++ or Java.
- For example, to create a value storing sum of `2` and `3`, you can create the following binding using `let` keyword:

```
> let sum = 2 + 3;;
val sum: int = 2 + 3
```

Try assigning `10` to `sum` as you do in languages like C:

```
> sum = sum + 10;;
val it: bool = false
```

and you will see a surprising output saying boolean value `false` has been saved to `it` value. This is because in F# `=` is only used to compare values.

To overwrite value stored in `sum` value, use `<-` operator. However, this won't work because `let` bindings are **immutable** by default, meaning once value is bind to a name, we cannot change it:

```
> sum <- 10;;

sum <- 10;;
  ^^^^^^^^^

stdin(6,1): error FS0027: This value is not mutable. Consider using the mutable keyword, e.g. 'let mutable sum = expression'.
```

## Variables using `let mutable`

To create a mutable **variable**, we can use `let mutable`:

```
> let mutable sum = sum;;
val mutable sum: int = 5
```

Now, you can change the value of `sum` using `<-`:

```
> sum <- 10;;
val it: unit = ()

> sum;;
val it: int = 10
```

Notice how we can reuse the `sum` binding defined earlier. F# allows us to reuse a binding/variable name. This also allows us to assign different type of data to `sum`:

```
> sum;;
val it: int = 10

> let sum = "hello";;
val sum: string = "hello"
```

## `let..in` vs `let`

`let` is actually a lightweight syntax for `let..in`. For example, the following code with `let`:

```
> let a = 2 ;;
val a: int = 2

> a + 10 ;;
val it: int = 12
```

can be rewritten using `let in` as:

```
> let a = 2 in
- a + 10 ;;
val a: int = 2
val it: int = 12
```

The above code is equivalent to:

- defining a function with parameter `a` and returns value `a + 10`, and later
- invoking this function with argument 2:

```
> (fun a -> a + 10) 2 ;;
val it: int = 12
```

`fun a -> a + 10` above is called a lambda or anonymous function. Functions will be discussed in detail later.

## Double-tick identifiers

You can create binding names containing space and symbols like `-` using double-tick identifiers (``` `` ```):

```
> let ``answer to question of life, universe, and everything`` = 
    42;;
val ``answer to question of life, universe, and everything`` : int = 42
```

# Whitespace in F#

F# code is whitespace sensitive. It uses whitespace for a block of code unlike languages such as C which use curly braces `{..}`.

You could write your let binding as:

```
let p = "This is a very long string."
```

or in a separate block:

```
let p = 
    "This is a very long string."
```

The indentation is done using space. DO NOT use tabs or else F# compiler would throw error. However, if you want to use tabs, then configure IDE to replace tabs with fixed amount of space. F# recommends four spaces for indentation.

# Types

Data types in F# are called just **types**. Following are the categories of types in F#:

- Primitive type
- Collections
- Discriminated Unions
- Records
- Classes and Interfaces

Discriminated Unions, Records, Classes and Interfaces will be discussed later.

## Primitive Types

Primitive types are the most fundamental types in F#. They are the following:

- `bool` - Possible values are `true` or `false`

  ```
  > let boolVal = true;;
  val boolVal: bool = true
  ```
- `byte` - Values from `0uy` to `255uy`. Notice the suffix `uy` - its required to indicate that the number represents byte value.

  ```
  > let byteVal: byte = 12uy;;
  val byteVal: byte = 12uy
  ```
- `int` - Type to store Integer number. Accepts values from -2,147,483,648 to 2,147,483,647.

  ```
  > let intVal = 12;;
  val intVal: int = 12
  ```
- `float`, `double` - A 64-bit floating point type.

  ```
  > let floatVal = 1.0;;
  val floatVal: float = 1.0
  ```

  `double` is a type alias for `float` (meaning `double` is same as `float` but with different name) and can also be used to declare 64-bit floating point data type:

  ```
  > let doubleVal: double = 1.0;;
  val doubleVal: double = 1.0
  ```
- `float32`, `single` - A 32-bit floating point type.

  ```
  > let float32Val = 1.0f;;
  val float32Val: float32 = 1.0f
  ```

  `single` is a type alias for `float32` and can be used to declare 32-bit floating point type:

  ```
  > let singleVal: single = 1.0f;;
  val singleVal: single = 1.0f
  ```
- `char` - Unicode character values.

  ```
  > let charVal = 'c';;
  val charVal: char = "c"
  ```
- `string` - String Unicode text.

  ```
  > let helloStr = "hello";;
  val helloStr: string = "hello"
  ```
- `unit` - Indicates the absence of an actual value. The type has only one formal value, which is denoted `()`. The unit value, `()`, is often used as a placeholder where a value is needed but no real value is available or makes sense.

  ```
  > let unitVal = ();;
  val unitVal: unit = ()
  ```

There are others as well. For full list, look up [offical docs](https://docs.microsoft.com/en-us/dotnet/fsharp/language-reference/basic-types).

### String type

- To concatenate strings:

```
/// Create a string using string concatenation
let hello = "Hello" + " World"
```

- Adding `@` in front of a string makes it a **verbatim** string, meaining any escape sequences are ignored, except two quotation mark characters `""` are considered as one quotation mark character `"`:

```
> let p = @"hellot""world""" ;;
val p: string = "hellot"world""
```

- Write multi-line strings using triple quotes `"""`:

```
> let multiLineString = """
    <book title="Paradise Lost">
""";;
val multiLineString: string = "
    <book title="Paradise Lost">
"
```

Observe that the string stored in `multiLineString` preserve leading whitespace and requires no escaping for double quotes `"`.

- To create multi-line strings without leading whitespace, use backslash:

```
> let multiLineStr2 = 
    "This is a multi-line string 
    without leading 
    whitespace.";;
val multiLineStr2: string =
  "This is a multi-line string without leading whitespace."

> multiLineStr2;;   
val it: string = "This is a multi-line string without leading whitespace."
```

### Interpolated strings

Interpolated strings are strings that allow you to embed F# expressions into them. For example, you can create a string with F# bindings as follows:

```
> let name = "Sumeet";;
val name: string = "Sumeet"

> $"My name is {name}";;
val it: string = "My name is Sumeet"
```

Interpolated strings start with `$` followed by the string within double quotes (`"..."`) or triple quotes (`"""..."""`).

You can format values in an interpolated string using `%(format-specifier)`:

```
> $"%0.4f{System.Math.PI}";;
val it: string = "3.1416"
```

## Tuples

A tuple is a grouping of unnamed but ordered values, possibly of different types.

For example:

```
> let tupleVal = (12, 4.5, "Hello");;
val tupleVal: int * float * string = (12, 4.5, "Hello")
```

- Tuple's data type is represented as `type1 * type2 * ...`. For example, tuple `tupleVal` above has the type `int * float * string`.
- Tuple can hold multiple values of different data types. For instance, all values are different in `tupleVal`.
- In place of just values, tuples can also hold results of expressions:

```
> let name = "Hello ";;
val name: string = "Hello "

> let tuple2 = (name + "World", 12 + 30);;
val tuple2: string * int = ("Hello World", 42)
```

- You can **deconstruct** a tuple into separate values and store them in different bindings as follows:

```
> let (helloWorld, answer) = tuple2;;
val helloWorld: string = "Hello World"
val answer: int = 42
```

In case, you wanted to get just first value of `tuple2` and ignore the second, you could use `_` wildcard in place of those values you want to ignore:

```
> let (helloWorld, _) = tuple2;;
val helloWorld: string = "Hello World"
```

The first and second elements of a tuple can be obtained using `fst`, `snd` functions:

```
> tuple2 ;;
val it: string * int = ("Hello World", 42)

> fst tuple2 ;;
val it: string = "Hello World"

> snd tuple2 ;;
val it: int = 42
```

For third or further elements, use pattern matching (discussed later). Or, you could write a function like this:

```
> let third (_, _, c) = c ;;
val third: 'a * 'b * c: 'c -> 'c

> let tuple3 = (fst tuple2, snd tuple2, 5.6) ;;
val tuple3: string * int * float = ("Hello World", 42, 5.6)

> third tuple3 ;;
val it: float = 5.6
```

Quick note about `third`'s function signature - F# automatically converts types of parameters into a generic one like `a'`, `b'` if the type cannot be inferred.

## Collections

Collections are data structures which can store multiple values of one or more data types.

### Lists

A *list* is an immutable collection of elements of the same type.

- To write a list in a single line:

```
> let list1 = ["a"; "b"]
val list1: string list = ["a"; "b"]
```

- Write a list in multiple lines:

```
> let list2 = 
    [
        "a"
        "b"
    ];;
val list2: string list = ["a"; "b"]
```

- Prepending an item to a list using cons (`::`) operator:

```
> let list2 = "c" :: list1;;
val list3: string list = ["c"; "a"; "b"]
```

- Concatenate two lists using `@` operator:

```
> let list4 = list1 @ list2;;   
val list4: string list = ["a"; "b"; "a"; "b"]
```

- Generate a range of numbers in ascending order using range (`..`) operator:

```
> [1..5] ;;
val it: int list = [1; 2; 3; 4; 5]
```

- Ranges can have custom interval:

```
> [0..3..30] ;;
val it: int list = [0; 3; 6; 9; 12; 15; 18; 21; 24; 27; 30]

> [0..-3..-30] ;;
val it: int list = [0; -3; -6; -9; -12; -15; -18; -21; -24; -27; -30]
```

As observed above, ranges are end-inclusive and start-inclusive.

### Arrays

*Arrays* are fixed-size, zero-based, mutable collections of consecutive data elements.

- Write an array of elements:

```
> let array1 = [|"a"; "b"|];;
val array1: string[] = [|"a"; "b"|]
```

- Access elements using index number:

```
> array1[0];;  
val it: string = "a"
```

- Mutate array elements using `<-` operator:

```
> array1[0] <- "mutated";;
val it: unit = ()

> array1;;
val it: string[] = [|"mutated"; "b"|]
```

### Sequences

A *sequence* is a logical series of elements of the same type. Individual sequence elements are computed only as required, so a sequence can provide better performance than a list in situations in which not all the elements are used.

```
> let seq1 = 
    seq {
        yield 1
        yield 2

        yield! [5..10]
    }
;;
val seq1: seq<int>
```

- `yield` adds one element to the sequence.
- `yield!` adds a whole subsequence. For instance, `yield! [5..10]` adds element 5 till 9 to the sequence.

### Slices

A slice is a subset of any data type. Slices use range (`..`) operator.

For example, suppose you have a list called `tenNums` containing numbers from 1 till 10:

```
> let tenNums = [1 .. 10] ;;
val tenNums: int list = [1; 2; 3; 4; 5; 6; 7; 8; 9; 10]
```

You can get various subsets of `tenNums` using slices:

- Slice of elements for indices `1..5` (5 inclusive):

```
> let slice = tenNums[1 .. 5] ;;
val slice: int list = [2; 3; 4; 5; 6]
```

Note that in F#, index starts from 0.

- Slice of elements from beginning to index 5 (5 inclusive):

```
> let slice = tenNums[ .. 5] ;;
val slice: int list = [1; 2; 3; 4; 5; 6]
```

- Slice of elements from index 5 till end of the list:

```
> let slice = tenNums[5 .. ] ;;
val slice: int list = [6; 7; 8; 9; 10]
```

Slicing works on arrays too:

```
> let tenNumsArray = [| 1 .. 10 |];
val tenNumsArray: int[] = [|1; 2; 3; 4; 5; 6; 7; 8; 9; 10|]

> let arraySlice = tenNumsArray[1..5] ;;
val arraySlice: int[] = [|2; 3; 4; 5; 6|]
```

You can also slice 2-D arrays:

```
> let A = array2D [[1;2;3];[4;5;6];[7;8;9]] ;;
val A: int[,] = [[1; 2; 3]
                 [4; 5; 6]
                 [7; 8; 9]]

> // Take the first row
- let row0 = A[0,*] ;;
val row0: int[] = [|1; 2; 3|]

> // Take all rows but first two column
- let custom = A[*,0..1] ;;
val custom: int[,] = [[1; 2]
                      [4; 5]
                      [7; 8]]
```

# Comments

Block comments are placed between `(*` and `*)`.

```
(* 
    This is a 
    block comment 
*)
```

Line comments start from `//` and continue until the end of the line.

```
// This is a line comment
```

XML doc comments come after `///` allowing us to use XML tags to generate documentation.

```
/// The `let` keyword defines an (immutable) value
let result = 1 + 1 = 2
```

# Conditional code using `if..then..else`

In F#, `if..then..else` are expressions, meaning it evaluates to some value which can be assigned to a binding.

For example, if you want to compare two numbers, you can write a function that does this using `if..then..else:

```
> let compare x y = 
    if x < y then $"{x} is less than {y}"
    else if x > y then $"{x} is greater than {y}"
    else $"{x} and {y} are equal"
;;
val compare: x: 'a -> y: 'a -> string when 'a: comparison

> compare 3 6 ;;
val it: string = "3 is less than 6"

> compare 300 6 ;;
val it: string = "300 is greater than 6"

> compare 6 6 ;;
val it: string = "6 and 6 are equal"
```

# `for..in` expression

`for..in` can be used to loop over values in a list:

```
> let numbers = [1; 2; 3] ;;
val numbers: int list = [1; 2; 3]

> for num in numbers do
    printf $"{num}; "
printfn ""
;;
1; 2; 3; 
val it: unit = ()
```

You can use it to loop over a range of characters:

```
> for c in 'a' .. 'f' do
    printf $"char {c} - "
printfn ""
;;
char a - char b - char c - char d - char e - char f - 
val it: unit = ()
```

You can also loop over a range of numbers with custom interval:

```
> for num in 3..3..24 do
    printf $"{num} - "
printfn ""
;;
3 - 6 - 9 - 12 - 15 - 18 - 21 - 24 - 
val it: unit = ()
```

You can also generate a list of numbers:

```
> let multiplesOf3 = [ for num in 3..3..24 do num ] ;;
val multiplesOf3: int list = [3; 6; 9; 12; 15; 18; 21; 24]
```

Beginning and end of a range can also be functions:

```
> let add x y = x + y ;;
val add: x: int -> y: int -> int

> for num in (add 1 2) .. (add 0 3) .. (add 15 3) do
    printf $"{num} - "
printfn ""
;;  
3 - 6 - 9 - 12 - 15 - 18 - 
val it: unit = ()
```

You can also ignore loop element using wildcard `_`:

```
> let nums = [1; 2; 3] ;;
val nums: int list = [1; 2; 3]

> for _ in nums do printf "Hello! "
printfn ""
;;
Hello! Hello! Hello! 
val it: unit = ()
```

# `for..to` expression

`for..to` can be used to iterate over a range of value by incrementing counter by 1.

For example, you can loop over values from 1 till 10 as:

```
> for i = 1 to 10 do
    printf $"{i} "
printfn ""
;;
1 2 3 4 5 6 7 8 9 10 
val it: unit = ()
```

Notice that the start `1` and end `10` are included in the range.

You could also decrement counter value by 1 using `downto` instead of `to`:

```
> for i = 10 downto 1 do
    printf $"{i} "
printfn ""
;;
10 9 8 7 6 5 4 3 2 1 
val it: unit = ()
```

One cool application of this expression is that you can generate a list containing a range of numbers:

```
> let p = [ for i = 10 to 20 do i ] ;;
val p: int list = [10; 11; 12; 13; 14; 15; 16; 17; 18; 19; 20]
```

# `while..do` expression

Similar to `for..in` but gives you greater flexibility in incrementing/decrementing value of counter.

For example, you can print even numbers from 10 till 20 using `while..do` as:

```
> let mutable num = 10;;
val mutable num: int = 10

> while num <= 20 do
    printf $"{num} "
    num <- num + 2
printfn ""
;;
10 12 14 16 18 20 
val it: unit = ()
```

You can also use `while..do` to generate lists. For instance, you can generate a list containing even numbers from 10 till 20 as:

```
> let mutable num = 10;;

> let p = [ while num <= 20 do num <- num + 2; num - 2 ] ;;
val p: int list = [10; 12; 14; 16; 18; 20]
```

# Functions

The `let` keyword also defines named functions.

For example, we will define a function named `negate` which would accept a number and multiply it with `-1` and return the result:

```
> let negate x = x * -1 ;;
val negate: x: int -> int
```

Notice how we didn't provide any data type to the input parameter `x` yet F# figured out `int` data type from the function definition. This is yet another example of powerful **type inference** in F#.

Sometimes, F# cannot correctly infer types, or sometimes you just want to add types for clarity. In those cases, you can provide the types as:

```
> let negate (x: int): int = x * -1 ;;
val negate: x: int -> int
```

Here, `(x: int)` declares the data type of `x`, while as `: int` at the end declares the return type of `negate` function.

## Lambda (or Anonymous) functions

You can create anonymous/Lambda functions as follows:

```
> let negateLambda = fun x -> x * -1 ;;
val negateLambda: x: int -> int

> negateLambda 4 ;;
val it: int = -4
```

In F#, lamdbas capture the values of bindings/variables in the scope in which it is defined. Meaning, if `valX` is defined before defining lambda function, then we can use `valX` inside the lambda function definition:

```
> let valX = 3;;
val valX: int = 3

> let negateLambda = fun x -> x * -1 * valX ;;
val negateLambda: x: int -> int

> negateLambda 4 ;;
val it: int = -12
```

## Curried Functions

Let's write a function to add two numbers:

```
> let add x y: int = x + y ;;
val add: x: int -> y: int -> int
```

Notice the signature of `add` function: `add: x: int -> y: int -> int`. This can be made sense of by understanding *currying*.

**Currying** is a process that transforms a function that has more than one parameter into a series of embedded functions, each of which has a single parameter.

So, in the context of `add` function, how F# looks at it is as follows:

```
> let add = 
    fun x ->
        fun y -> 
            x + y ;;
val add: x: int -> y: int -> int
```

What this means is that F# converted `add` function into a function of one paramter (`fun x ->` ) which returns a function of one paramter (`fun y ->` ).

- Since type of `x` and `y` is `int`, you can now understand why `add` function signature is `x: int -> y: int -> int`, where `y: int -> int` indicates a function which accepts a parameter `y` of type `int` and returns value of type `int`.
- Similarly, `x: int -> y: int -> int` indicates a function which accepts a parameter `x` of type `int` and returns a function of type `y: int -> int`.

So now, you can create a function called `add2` which would always add `2` to an integer argument:

```
> let add2 = add 2 ;;
val add2: (int -> int)

> add2 10 ;;
val it: int = 12
```

## Pipe and composition operators

Pipe operator `|>` is used to chain functions and arguments together:

```
> let square x = x * x ;;
val square: x: int -> int

> let negate x = x * -1 ;;
val negate: x: int -> int

> let ``square and negate`` x = 
    x |> square |> negate ;;
val ``square and negate`` : x: int -> int
```

`x |> square |> negate` is equivalent to `negate (square x)`:

```
> ``square and negate`` 10 ;;
val it: int = -100

> negate (square 10) ;;
val it: int = -100
```

You could also write ``` ``square and negate`` ``` function using composition operator `>>`:

```
> let squareNegate = square >> negate ;;
squareNegate 10;;
```

`>>` operator is used to compose functions - `square >> negate` is equivalent to feeding `square` function's result to `negate` function, or `negate (square x)`.

## Recursive functions

The `rec` keyword is used together with the `let` keyword to define a recursive function:

```
let rec factorial x =
    if x < 1 then 1
    else x * factorial (x - 1)
```

Without `rec`, the compiler won't be able to find `factorial` function and hence will throw an error.

*Mutually recursive* functions (those functions which call each other) are indicated by `and` keyword:

```
let rec even x =
    if x = 0 then true 
    else odd (x - 1)

and odd x =
    if x = 0 then false
    else even (x - 1)
```

# Pattern Matching

Pattern matching is often facilitated through `match` keyword.

```
// a recursive function to calculate nth fibonacci number 
let rec fibonacci n =
    match n with
    // match 0 pattern
    | 0 -> 0
    | 1 -> 1
    // wildcard pattern _
    | _ -> fib (n - 1) + fib (n - 2)
```

- `| 0 -> 0` means when `n` equals `0`, then return `0`
  - `| 0` is called matching pattern `0` or matching arm `0`
  - Pattern and result expression are seperated by `->`
- In pattern matching, all patterns should be matched against, or else F# compiler would give a warning. To add a default pattern to match against any pattern not matched by existing patterns, use wildcard pattern `_`.
  - In the above recursive function, `| _ ->`  matches any value of `n` which is not 1 or 0.

## `when` keyword

In order to match sophisticated inputs, one can use `when` to create filters or guards on patterns:

```
let sign x = 
    match x with
    | 0 -> 0
    // this arm will be matched when x is less than 0
    | x when x < 0 -> -1
    | _ -> 1
```

## `function` keyword

`function` keyword is used to simply writing lambda functions containing `match` expression as function body. For instance, you have this lambda expression to compute distance from origin in 1-D, 2-D and 3-D coordinate system:

```
> let distanceFromOrigin = 
    fun coordinate -> 
        match coordinate with 
        | [ x ] -> x
        | [ x; y ] -> System.Math.Sqrt ( x * x + y * y )
        | [ x; y; z ] -> System.Math.Sqrt ( x * x + y * y + z * z )
        | _ -> printfn "Not supported!"; -1
;;
val distanceFromOrigin: coordinate: float list -> float

> distanceFromOrigin [ 3; 4 ] ;;
val it: float = 5.0
```

You could simplify `distanceFromOrigin` function definition using `function` keyword as follows:

```
> let distanceFromOrigin = 
    function
        | [ x ] -> x
        | [ x; y ] -> System.Math.Sqrt ( x * x + y * y )
        | [ x; y; z ] -> System.Math.Sqrt ( x * x + y * y + z * z )
        | _ -> printfn "Not supported!"; -1
;;
val distanceFromOrigin: _arg1: float list -> float

> distanceFromOrigin [ 3; 4 ] ;;
val it: float = 5.0
```

So, `function` keyword basically replaces `fun x -> match x with`.

## Cons (`::`) pattern with lists

We can write a recursive function `listSum` which computes sum of numbers in a list as:

```
> let rec sum list = 
    match list with
    | [] -> 0
    | head :: tail -> head + sum tail
;;
val sum: list: int list -> int

> sum [] ;;
val it: int = 0

> sum [1; 2; 3; 4] ;;
val it: int = 10
```

- `head :: tail` is called Cons pattern. Using this, we can extract head of the list `head` and rest of the list `tail`.

## Active Patterns

Active Pattern helps you to categorize an input data into some named partition, so that you can use these names as a pattern in match expressions.

For example, you can write an active pattern which would classify a number as even or odd as follows:

```
> let (|Even|Odd|) num = if num % 2 = 0 then Even else Odd ;;
val (|Even|Odd|) : num: int -> Choice<unit,unit>
```

- The `(|` and `|)`symbols are called **banana clips**.
- The function created above is called an **active recognizer**. It takes an input an returns an object of type `Choice`.

Now, you can match against a number as even or odd as follows:

```
> let testNum num = 
    match num with 
    | Odd -> printfn "Number is odd"
    | Even -> printfn "Number is even"
;;
val testNum: num: int -> unit

> testNum 6 ;;
Number is even
val it: unit = ()

> testNum 77 ;;
Number is odd
val it: unit = ()
```

### Parameterized active patterns

The above active patterns took just the input. You can provide more arguments to active patterns using **parameterized active patterns**.

For example, you can write an active pattern which would categorize an input `num` based on whether it is divisible by another number `by` as follows:

```
> let (|DivisibleBy|_|) by num = 
    if num % by = 0 then Some DivisibleBy else None
;;
val (|DivisibleBy|_|) : by: int -> num: int -> unit option
```

You can use this active pattern in `match` expressions to implement FizzBuzz solution where we check what to do based on whether input is divisible by 3 or 5:

```
> let fizzbuzz = 
    function 
        | DivisibleBy 5 & DivisibleBy 3 -> printfn "FizzBuzz"
        | DivisibleBy 5 -> printfn "Buzz"
        | DivisibleBy 3 -> printfn "Fizz"
        | x -> printfn "%d" x
;;
val fizzbuzz: _arg1: int -> unit

> fizzbuzz 15;;
FizzBuzz
val it: unit = ()

> fizzbuzz 11;;
11
val it: unit = ()
```

## Partial Active Patterns

Sometimes, you need to partition only part of the input space. In that case, you write a set of partial patterns each of which match some inputs but fail to match other inputs. Active patterns that do not always produce a value are called **partial active patterns**; they have a return value that is an `option` type.

To define a partial active pattern, you use a wildcard character (\_) at the end of the list of patterns inside the banana clips.

For example, suppose you want to parse a number from a string input, but would like to round float number to nearest integer.

# Records

*Records* represent simple aggregates of named values, optionally with members.

To declare a record type:

```
> type Person = { Name : string; Age : int } ;;
type Person =
  {
    Name: string
    Age: int
  }
```

To create a record via record expression:

```
> let paul = { Name = "Paul"; Age = 28 } ;;
val paul: Person = { Name = "Paul"
                     Age = 28 }
```

Expression to copy and update a record:

```
> let paulsTwin = { paul with Name = "Jim" } ;;
val paulsTwin: Person = { Name = "Jim"
                          Age = 28 }
```

Records can be augmented with properties and methods:

```
> type Person with
    member x.Info = (x.Name, x.Age)
;;
type Person with
  member Info: string * int

> paul.Info ;;
val it: string * int = ("Paul", 28)

> paulsTwin.Info ;;
val it: string * int = ("Jim", 28)
```

Properties of records, such as `Name` in `Person` record type, can't be modified by default. If you want a mutable record property, add `mutable` keyword to it:

```
> type Employee = 
    {
        Name: string
        mutable DepartmentId: int
    }
;;
type Employee =
  {
    Name: string
    mutable DepartmentId: int
  }

> let mutable empShyam = { Name = "Shyam"; DepartmentId = 15 } ;;
val mutable empShyam: Employee = { Name = "Shyam"
                           DepartmentId = 15 }

> // change the department ID for Shyam
- empShyam.DepartmentId <- 20 ;;

> empShyam ;;
val it: Employee = { Name = "Shyam"
                     DepartmentId = 20 }
```

- Note that in order to mutate a record, you also need to declare the record as mutable (e.g. `let mutable empShyam` in above code)

Records are essentially sealed classes with extra topping: default immutability, structural equality, and pattern matching support.

```
> let isPaul person =
    match person with
    | { Name = "Paul"; Age = _ } -> true
    | _ -> false
;;
val isPaul: person: Person -> bool

> isPaul paul ;;
val it: bool = true

> isPaul paulsTwin ;;
val it: bool = false
```

## Anonymous Records

Anonymous records are like records but don't need to be declared upfront. For example, here's a function returning an anonymouus record containing diameter, area, circumference of a circle for a given radius:

```
> let getCircleProps radius = 
    let dia = radius * 2.0
    // To compute square of radius, you can use ** operator
    let area = System.Math.PI * (radius ** 2.0)
    let peri = 2.0 * System.Math.PI * radius

    {| Diameter = dia; Area = area; Circumference = peri |}
;;
val getCircleProps:
  radius: float -> {| Area: float; Circumference: float; Diameter: float |}
```

You can accept an anonymous record as a parameter:

```
> let circleProps = getCircleProps 4.0 ;;
val circleProps: {| Area: float; Circumference: float; Diameter: float |} =
  { Area = 50.26548246
    Circumference = 25.13274123
    Diameter = 8.0 }

> let printCircleProps (circleProps: {| Area: float; Circumference: float; Diameter: float |}) = 
    printfn $"""
        Area: {circleProps.Area}
        Circumference: {circleProps.Circumference}
        Diameter: {circleProps.Diameter}
    """
;;

> printCircleProps circleProps ;;

        Area: 50.26548245743669
        Circumference: 25.132741228718345
        Diameter: 8

val it: unit = ()
```

You can also copy and extend an existing anonymous record:

```
> let circlePropsWithName = {| circleProps with Name = "Circle A" |} ;; 
val circlePropsWithName:
  {| Area: float; Circumference: float; Diameter: float; Name: string |} =
  { Area = 50.26548246
    Circumference = 25.13274123
    Diameter = 8.0
    Name = "Circle A" }
```

# Discriminated Unions (DU)

Discriminated Unions are helpful to model heterogenous data, or data which can be grouped under same category but can be modeled as different types like `int`, a class or a record.

For example, if you want to model a geometric shape which could be either a square, rectangle or a circle, you could do so using DU:

```
> type Shape = 
    | Circle of radius: int
    | Square of side: int
    | Rectange of length: int * width: int
;;
type Shape =
  | Circle of radius: int
  | Square of side: int
  | Rectangle of length: int * width: int
```

Now, you create an instance of `Circle`, `Square` or `Rectangle` type and save it to a binding/variable of type `Shape`:

```
> let shape: Shape = Circle 5 ;;
val shape: Shape = Circle 5

> shape <- Rectangle (5, 3);;
val it: unit = ()

> shape;;
val it: Shape = Rectange (5, 3)
```

## `option` type

`option` type is a discriminated union available in F# by default. Options can store a value of some type, or it does not have that value.

`option` is defined as:

```
type 'a option = 
    | Some of 'a
    | None
```

`'a` is a generic type parameter which could be any type. `option` type defines two types:

- `Some` type which stores a value of type `'a`
- `None` type which indicates that the `option` does not contain any value

For example, suppose you write a function which accepts a number as an argument and returns that number if it is a positive number or no value otherwise. Such a function could be written using `option` as return type:

```
> let getPositiveNumber num = 
    if num > 0 then Some num
    else None
;;
val getPositiveNumber: num: int -> int option

> getPositiveNumber 12;;
val it: int option = Some 12

> getPositiveNumber -12;;
val it: int option = None
```

- Note that the function signature of `getPositiveNumber` is `int -> int option`, meaning the function accepts an `int` value and returns an `option` of type `int`.

How do we extract a value from an `option` if the value exists? For example, suppose we write a function which accepts salary option as a parameter, and we return the salary value if it exists or default salary of `1000` if it does not. We can use pattern matching for this:

```
> let getSalary (salary: int option) = 
    match salary with 
    | Some salaryVal -> salaryVal
    | None -> 1000
;;
val getSalary: salary: int option -> int

> getSalary (Some 2000) ;;
val it: int = 2000

> getSalary (None) ;;
val it: int = 1000
```

We could also use `Option.defaultValue` function from `Option` module:

```
> let getSalary (salary: int option) = 
    salary |> Option.defaultValue 1000
;;

> getSalary (None) ;;
val it: int = 1000
```

There are lots of functions available in `Option` module which deal with `option` types. For full list, visit [this page](https://fsharp.github.io/fsharp-core-docs/reference/fsharp-core-optionmodule.html)

## `Result` type

`Result` type can be used to handle errors in a typesafe way. A binding of `Result` type can accept either `Ok` containing success data of any type, or `Error` containing error data of any type.

For example, you can write a function which divides two numbers using `Result` type as follows:

```
> let divide x y = 
    if y = 0 then Error "Trying to divide by 0"
    else Ok (x / y)  
;;
val divide: x: int -> y: int -> Result<int,string>

> divide 6 3 ;;
val it: Result<int,string> = Ok 2

> divide 6 0 ;;
val it: Result<int,string> = Error "Trying to divide by 0"
```

You can pattern match against the result value to perform action based on whether the operation was successful or failed due to an error:

```
> let res = divide 6 3 ;;

> match res with 
    | Ok result -> printfn $"The result of 6/3 is {result}"
    | Error message -> printfn $"An error occured"
;;
The result of 6/3 is 2
val it: unit = ()
```

# Generics and Automatic Generalization

Consider the following function definition:

```
> let makeList a b =
    [a; b]
;;
val makeList: a: 'a -> b: 'a -> 'a list
```

You see that F# infers `makeList` signature as `'a -> 'a -> 'a list`. Two takeaways from this:

- F# automatically generalized the function in the event no type could be inferred from the definition. This is called as **Automatic Generalization**.
- Since a list could have elements of the same type, both `a` and `b` have been assigned the same generic type `'a`.
- Generic types follow the convention: `'name`. For e.g., `'a`, `'hello`.

You can explicitly specify generics as:

```
> let makeList (a: 'a) (b: 'a) =
    [a; b]
;;
val makeList: a: 'a -> b: 'a -> 'a list
```

You can make it even more explicit using `<'generic>`:

```
> let makeList<'a> (a: 'a) (b: 'a) =
    [a; b]
;;
val makeList: a: 'a -> b: 'a -> 'a list
```

# Exceptions

## `failwith`

The `failwith` function throws an exception of type `Exception`.

```
> let divideFailwith x y =
    if y = 0 then 
        failwith "Divisor cannot be zero." 
    else x / y
;;
val divideFailwith: x: int -> y: int -> int

> divideFailwith 15 0;;
System.Exception: Divisor cannot be zero.
   at FSI_0060.divideFailwith(Int32 x, Int32 y)
   at <StartupCode$FSI_0061>.$FSI_0061.main@()
Stopped due to error
```

## `try/with`

Exception handling is done via `try/with` expressions.

```
> let divide x y =
    try
        Some (x / y)
    with :? System.DivideByZeroException -> 
        printfn "Division by zero!"
        None
;;

> divide 6 3;;
val it: int option = Some 2

> divide 5 0;;
Division by zero!
val it: int option = None
```

- Exception thrown is tried to be downcasted to `System.DivideByZeroException` using :?. If it is successful, then the `"Division by zero!"` message is printed and function returns `None`.

## Custom exceptions

You can throw custom exceptions by first defining them using `exception` keyword:

```
> exception CustomDivideByZero of string ;;
exception CustomDivideByZero of string
```

The above exception `CustomDivideByZero` accepts only string message as an argument.

You can then throw this custom exception via `raise` function:

```
> let divide x y =
    if y = 0 
    then 
        raise (CustomDivideByZero ("trying to divide a number by zero!"))
    else 
        (x |> float) / (y |> float)
;;
val divide: x: int -> y: int -> float

> divide 6 4;;
val it: float = 1.5

> divide 6 0;;
FSI_0065+CustomDivideByZero: Exception of type 'FSI_0065+CustomDivideByZero' was thrown.
   at FSI_0071.divide(Int32 x, Int32 y)
   at <StartupCode$FSI_0073>.$FSI_0073.main@()
Stopped due to error
```

## `try/finally`

The `try/finally` expression enables you to execute clean-up code even if a block of code throws an exception.

```
> exception InnerError of string ;;
exception InnerError of string

> exception OuterError of string ;;
exception OuterError of string

> let handleErrors x y =
    try 
        try 
            if x = y 
            then raise (InnerError("inner"))
            else raise (OuterError("outer"))
        with InnerError(str) -> 
            printfn "Error1 %s was caught" str
    finally
        printfn "Always print this."
 ;;
val handleErrors: x: 'a -> y: 'a -> unit when 'a: equality

> handleErrors 3 3 ;;
Error1 inner was caught
Always print this.
val it: unit = ()

> handleErrors 3 4 ;;
Always print this.
FSI_0075+OuterError: Exception of type 'FSI_0075+OuterError' was thrown.
   at FSI_0076.handleErrors[a](a x, a y)
   at <StartupCode$FSI_0078>.$FSI_0078.main@()
Stopped due to error
```

# Classes and Inheritance

In F#, you can create classes to model data.

For example, suppose you want to create a data structure to store a vector. You can start with create a class type:

```
type Vector() = class end
```

- `Vector()` provides class name and constructor to call in order to create a `Vector` object via `new Vector()`:

```
let vector = Vector()
```

- `class end` is required if your class doesn't require any properties or methods.

Next, we will add two class properties `X` and `Y` and will define a constructor for it:

```
type Vector (x: float, y: float) = 
    member this.X = x
    member _.Y = y
```

- Properties and methods are defined using `member` keyword.
- `this` can be replaced with wildcard `_` if it is not required. Also, you could use `self` or any other name in place of `this` because unlike Java, `this` is not a keyword in F#.

You can add getters and setters for `Y` property as follows:

```
let mutable yVal = y
member _.Y 
    with get() = yVal
    and set(newVal) = yVal <- newVal
```

- Important - `let mutable yVal` binding must come before any `member` declarations. So, if the first `member` declaration is `member this.X`, then `yVal` binding definition should come before it.

We can add methods to `Vector` clas definition like `Scale` to scale the vector:

```
member this.Scale scaleVal = 
    Vector(this.X * scaleVal, this.Y * scaleVal)
```

- In F#, properties and methods should start with a capital letter.

We can also implement operations such as adding two vectors by implementing `+` operator via static methods:

```
static member (+) (a : Vector, b : Vector) = 
    Vector(a.X + b.X, a.Y + b.Y)
```

You can also have `let` bindings inside class definition. Such bindings won't be available outside the class and can be used to compute members' values. For example, we can define a member `mag` which will store the computed magnitude of the vector:

```
type Vector (x: float, y: float) =
    let magnitude = sqrt(x * x, y * y)
    member _.mag = magnitude
```

Notice how value of `this.mag` depends on the constructor arguments `x` and `y`. Since we have a setter for `y`, let's modify `this.mag` to update value when `this.Y` changes:

```
let magnitude() = sqrt(x * x, yVal * yVal)
member _.mag 
    with get() = magnitude()
```

Now, everytime you fetch `mag` property, `magnitude` function would be executed.

Overall, our Vector class now looks like this:

```
> type Vector(x : float, y : float) =
    let mutable yVal = y
    let magnitude() = sqrt(x * x + yVal * yVal)

    member this.X = x 
    member _.Y 
        with get() = yVal
        and set(newVal) = yVal <- newVal
    member _.mag 
        with get() = magnitude()
    member this.Scale scaleVal = 
        Vector(this.X * scaleVal, this.Y * scaleVal)
    static member (+) (a : Vector, b : Vector) = 
        Vector(a.X + b.X, a.Y + b.Y)
;;
type Vector =
  new: x: float * y: float -> Vector
  member Scale: s: float -> Vector
  static member (+) : a: Vector * b: Vector -> Vector
  member Mag: float
  member X: float
  member Y: float
```

Now, you can use `Vector` class as follows:

```
> // Creating an instance of Vector class
- let v1 = Vector (3.0, 3.0);;
val v1: Vector

> v1.mag;;
val it: float = 4.242640687

> // Setting value of Y property
- v1.Y <- 4.0;;
val it: unit = ()

> v1.Y;;
val it: float = 4.0

> v1.mag;;
val it: float = 5.0

> v1.Scale 10;;
val it: Vector = FSI_0048+Vector {X = 30.0;
                                  Y = 40.0;
                                  mag = 50.0;}

> let v2 = Vector (12.0, 9.0);;
val v2: Vector

> v1 + v2;;
val it: Vector = FSI_0048+Vector {X = 15.0;
                                  Y = 13.0;
                                  mag = 19.84943324;}

> // Trying to access let binding `magnitude`
- v1.magnitude();;
v1.magnitude()
  ---^^^^^^^^^

stdin(304,4): error FS0039: The type 'Vector' does not define the field, constructor or member 'magnitude'.
```

## Inheritance

Call a base class from a derived one. For example, we have a base class `Animal` and a derived class `Dog` inheriting from `Animal` class. We can call `Animal` class methods from `Dog` using `base.MethodName(..)` syntax:

```
type Animal() =
    member __.Rest() = ()
            
type Dog() =
    inherit Animal()
    member __.Run() =
        base.Rest()
```

*Upcasting* is the process of converting a child class to a parent class. It can be done using `:>` operator.

```
let dog = Dog() 
let animal = dog :> Animal
```

*Dynamic downcasting* is convering a parent class to a child class. It can be done using (`:?>`) operator. This might throw an `InvalidCastException` if the cast doesn't succeed at runtime:

```
let shouldBeADog = animal :?> Dog
```

# Interfaces and Object Expressions

Declare `IVector` interface and implement it in `Vector'`.

```
type IVector =
    abstract Scale : float -> IVector

type Vector'(x, y) =
    interface IVector with
        member _.Scale(s) =
            Vector'(x * s, y * s) :> IVector
    member _.X = x
    member _.Y = y
```

Another way of implementing interfaces is to use *object expressions*.

```
type ICustomer =
    abstract Name : string
    abstract Age : int

let createCustomer name age =
    { new ICustomer with
        member __.Name = name
        member __.Age = age }
```

# Compiler Directives

Load another F# source file into FSI.

```
#load "../lib/StringParsing.fs"
```

Reference a .NET assembly (`/` symbol is recommended for Mono compatibility).

```
#r "../lib/FSharp.Markdown.dll"
```

Include a directory in assembly search paths.

```
#I "../lib"
#r "FSharp.Markdown.dll"
```

Other important directives are conditional execution in FSI (`INTERACTIVE`) and querying current directory (`__SOURCE_DIRECTORY__`).

```
#if INTERACTIVE
let path = __SOURCE_DIRECTORY__ + "../lib"
#else
let path = "../../../lib"
#endif
```

© 2022 Sumeet Das
