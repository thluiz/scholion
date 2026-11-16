---
url: "https://web.archive.org/web/20200516032544id_/https://dontcodetired.com/blog/post/Variables-We-Dont-Need-No-Stinking-Variables-C-Discards"
captured_at: "2026-11-16T08:15:16+00:00"
title: "Don't Code Tired | Variables? We Don’t Need No Stinking Variables"
domain: "web-archive-org"
---

C# 7.0 introduced the concept of discards. Discards are intentionally unused, temporarily dummy variables that we don’t care about and don’t want to use.

For example, the following shows the result of an addition being discarded:

1

`_ = 1 + 1;`

Note the underscore **\_** this is the discard character.

Given the preceding example, you cannot access the result of this addition, for example:

1

`WriteLine(_);`

## Using C# Discards with Out Parameters

A more useful example is when you are working with a method that has one or more **out** parameters and you don’t care about using the **out**putted value.

As an example, consider one of the many **TryParse** methods in .NET such as **int.TryParse**. The following code show a method that writes to the console whether or not a string can be parsed as an int:

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

`static` `void` `ParseInt()`

`{`

    `WriteLine(``"Please enter an int to validate"``);`

    `string` `@``int` `= ReadLine();`

    `bool` `isValidInt =` `int``.TryParse(@``int``,` `out` `int` `parsedInt);`

    `if` `(isValidInt)`

    `{`

        `WriteLine($``"{@int} is a valid int"``);`

    `}`

    `else`

    `{`

        `WriteLine($``"{@int} is NOT a valid int"``);`

    `}`

`}`

The preceding method can be written using a discard because the **out int parsedInt** value is never used:

1

2

3

4

5

6

7

8

9

10

11

12

13

14

`static` `void` `ParseIntUsingDiscard()`

`{`

    `WriteLine(``"Please enter an int to validate"``);`

    `string` `@``int` `= ReadLine();`

    `if` `(``int``.TryParse(@``int``,` `out` `_))`

    `{`

        `WriteLine($``"{@int} is a valid int"``);`

    `}`

    `else`

    `{`

        `WriteLine($``"{@int} is NOT a valid int"``);`

    `}`

`}`

For example we could create an expression bodied method using a similar approach:

1

`static` `bool` `IsInt(``string` `@``int``) =>` `int``.TryParse(@``int``,` `out` `_);`

If you have a method that returns a lot of **out** values such as:

1

2

3

4

5

6

7

`private` `static` `void` `GenerateDefaultCity(``out` `string` `name,` `out` `string` `nickName,` `out` `long` `population,` `out` `DateTime founded)`

`{`

    `name =` `"London"``;`

    `nickName =` `"The Big Smoke"``;`

    `population = 8_000_000;`

    `founded =` `new` `DateTime(50, 1, 1);`

`}`

In this case you might only care about the returned population value so you could discard all the other **out** values:

1

2

`GenerateDefaultCity(``out` `_,``out` `_,` `out` `var` `population,` `out` `_);`

`WriteLine($``"Population is: {population}"``);`

## Using C# Discards with Tuples

Another use for discards is where you don’t care about all the fields of a tuple. For example the following method returns a tuple containing a name and age:

1

2

3

4

`static` `(``string` `name,` `int` `age) GenerateDefaultPerson()`

`{`

    `return` `(``"Amrit"``, 42);`

`}`

If you only cared about the age you could write:

1

2

`var` `(_, age) = GenerateDefaultPerson();`

`WriteLine($``"Default person age is {age}"``);`

## Simplifying Null Checking Code with Discards

Take the following null checking code:

1

2

3

4

5

6

7

8

`private` `static` `void` `Display(``string` `message)`

`{`

    `if` `(message` `is` `null``)`

    `{`

        `throw` `new` `ArgumentNullException(nameof(message));`

    `}`

    `WriteLine(message);`

`}`

You could refactor this to make use of throw expressions:

1

2

3

4

5

6

`private` `static` `void` `DisplayV2(``string` `message)`

`{`

    `string` `checkedMessage = message ??` `throw` `new` `ArgumentNullException(nameof(message));`

    `WriteLine(checkedMessage);`

`}`

In the preceding version however, the **checkedMessage** variable is somewhat redundant, this could be refactored to use a discard:

1

2

3

4

5

6

`private` `static` `void` `DisplayWithDiscardNullCheck(``string` `message)`

`{`

    `_ = message ??` `throw` `new` `ArgumentNullException(nameof(message));`

    `WriteLine(message);`

`}`

## Using C# Discards with Tasks

Take the following code:

1

2

`Task.Run(() => SayHello());`

Where the SayHello method is defined as:

1

2

3

4

5

`private` `static` `string` `SayHello()`

`{`

    `string` `greeting =` `"Hello there!"``;`

    `return` `greeting;`

`}`

If we don’t care about the return value and want to discard the result and get rid of the compiler warning::

1

2

`_ = Task.Run(() => SayHello());`

If there are any exceptions however, they will be supressed:

1

2

`await Task.Run(() =>` `throw` `new` `Exception());`

`_ = Task.Run(() =>` `throw` `new` `Exception());`

## Pattern Matching with Switch Statements and Discards

You can also use discards in switch statements:

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

`private` `static` `void` `SwitchExample(``object` `o)`

`{`

    `switch` `(o)`

    `{`

        `case` `null``:`

            `WriteLine(``"o is null"``);`

            `break``;`

        `case` `string` `s:`

            `WriteLine($``"{s} in uppercase is {s.ToUpperInvariant()}"``);`

            `break``;`

        `case` `var` `_:`

            `WriteLine($``"{o.GetType()} type not supported."``);`

            `break``;`

    `}`

`}`

If you want to learn a load more C# tips check out my [C# Tips and Traps course](https://pluralsight.pxf.io/csharptipsandtraps) today. You can even currently start watching with a [Pluralsight Free Trial with Unlimited Access](https://pluralsight.pxf.io/c/1392775/503634/7490) .

[![](https://a.impactradius-go.com/display-ad/7490-431403)](https://pluralsight.pxf.io/c/1392775/431403/7490)

SHARE:[](https://twitter.com/share?url=http%3a%2f%2fdontcodetired.com%2fblog%2fpost%2fTesting-EventGridTrigger-Azure-Functions-Locally-\(Without-Using-ngrok\)&text=Testing+EventGridTrigger+Azure+Functions+Locally+\(Without+Using+ngrok\)&via=robertsjason "Share post on Twitter")[](https://www.linkedin.com/shareArticle?mini=true&url=http%3a%2f%2fdontcodetired.com%2fblog%2fpost%2fTesting-EventGridTrigger-Azure-Functions-Locally-\(Without-Using-ngrok\)&title=Testing+EventGridTrigger+Azure+Functions+Locally+\(Without+Using+ngrok\)&source=dontcodetired.com "Share post on LinkedIn")[](mailto:?subject=Testing%20EventGridTrigger%20Azure%20Functions%20Locally%20\(Without%20Using%20ngrok\)&body=Thought%20you%20might%20like%20this:%20http://dontcodetired.com/blog/post/Testing-EventGridTrigger-Azure-Functions-Locally-\(Without-Using-ngrok\) "Email a link to this post")
