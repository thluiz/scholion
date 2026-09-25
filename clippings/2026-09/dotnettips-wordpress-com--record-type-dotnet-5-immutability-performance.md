---
url: "https://dotnettips.wordpress.com/2021/02/26/everything-you-want-to-know-about-the-record-type-in-net-5-but-were-afraid-to-ask/?utm_source=newsletter.csharpdigest.net&utm_medium=newsletter&utm_campaign=10-lessons-i-learned-from-using-aspire-in-production&_bhlid=02b275dc8f7af750ddde9a88efe8c83efdcd1cbe"
captured_at: "2026-09-25T08:24:53+01:00"
title: "Everything You Want to Know About the Record Type in .NET… But Were Afraid to Ask"
domain: "dotnettips-wordpress-com"
---

October 1, 2024

![RecordType Tweet](https://i0.wp.com/dotnettips.com/wp-content/uploads/2021/02/recordtype-tweet.png?resize=700%2C821&ssl=1)

In January 2021, I posed a question to viewers during one of my “**Rockin’ the Code World with dotNetDave**” shows: “**_What is the new class type for .NET 5?_**” The answer is the `**record**` class. I’ve been actively using this feature in my open-source project, Spargine, and I even conducted a Twitter poll to gauge interest among developers regarding the transition to .NET 5 for utilizing record types. In this article, I’ll explain why I’m _enthusiastic_ about this new feature, which has quickly become my favorite addition in .NET 5.

## Understanding Model Types

Many of the classes I create in my assemblies are what I refer to as “_model types_,” which include Data Transfer Objects (DTOs) or Plain Old CLR Objects (POCOs). These classes are primarily used to transport data to and from back-end API services, which I typically develop using ASP.NET Web API. You can think of them as code-first classes in Entity Framework. While it’s essential for these classes to adhere to good architecture and coding standards, their primary role is simply to represent data.

## The Introduction of Record Types

With the release of .NET 5 in 2020, the .NET team at Microsoft introduced the **record** class type, significantly reducing the “boilerplate” code developers need to write. Defining a record type is similar to defining a class, with the key distinction being the use of the record keyword instead of class. For instance, a type representing a person can be defined as follows:

1

`public` `sealed` `record Person : IDataRecord`

The `IDataRecord` interface is part of my Spargine OSS that implements an Id property for consistency across all DTOs and adds a method `AllPropertiesToString()` that converts all the properties and their values to a string representation.

## Setting Values

One significant difference with record types is how values are assigned. Instead of using `set`, we utilize **`init`**:

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

16

17

18

`public` `string` `Email`

`{`

    `get` `=>` `this``._email;`

    `init`

    `{`

        `if` `(``string``.Equals(``this``._email, value, StringComparison.Ordinal))`

        `{`

            `return``;`

        `}`

        `this``._email = value.HasValue(0, 75)` `is` `false`

            `?` `throw` `new` `ArgumentOutOfRangeException(`

            `nameof(``this``.Email),`

            `Resources.EmailLengthIsLimitedTo75Characters)`

            `: value;`

    `}`

`}`

The `init` accessor behaves like `set`, with two key rules:

1.  Init values can be set in the constructor, akin to read-only variables.
2.  Init values can be set during object initialization.

Once the object is created, the data cannot be modified, maintaining the immutability characteristic.

## Updating Values

Since the values of record classes cannot be updated after creation, how can you modify data, particularly on the client side, for backend updates? Instead of modifying existing objects, a new object must be created. Record types simplify this process using the `**with**` keyword:

1

2

3

4

5

6

7

8

`var` `email =` `"test@example.com"``;`

`var` `id =` `"12345"``;`

`var` `person =` `new` `PersonRecord(email, id)`

`{`

    `FirstName =` `"John"`

`};`

`person = person with { FirstName =` `"Jane"` `};`

## Equality and Comparisons

Whenever you create a class, especially model classes, it is important to implement `IComparable<T>`, `IEquatable<T>` and override the equality operators like this:

1

2

3

`public` `static` `bool` `operator` `>(Person left, Person right) =>`

    `left` `is` `not` `null` `&&`

    `left.CompareTo(right) > 0;`

This often leads to extensive boilerplate code, particularly for the `CompareTo()` method, and can discourage developers from implementing these methods. Fortunately, with record types, these methods are automatically generated.

## Hashing and ToString()

Another method frequently overlooked in types like these is `GetHashCode()`. Here’s how a developer might manually implement it:

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

`public` `override` `int` `GetHashCode()`

`{`

    `var` `hash =` `new` `HashCode();`

    `hash.Add(``this``.Addresses);`

    `hash.Add(``this``.BornOn);`

    `hash.Add(``this``.CellPhone);`

    `hash.Add(``this``.Email);`

    `hash.Add(``this``.FirstName);`

    `hash.Add(``this``.Phone);`

    `hash.Add(``this``.Id);`

    `hash.Add(``this``.LastName);`

    `return` `hash.ToHashCode();`

`}`

With record types, there’s no need to override the GetHashCode() method; it’s generated by the compiler. This alleviates maintenance concerns.

[![](https://i0.wp.com/dotnettips.com/wp-content/uploads/2021/02/personrecord-gethashcode-source.jpg?resize=700%2C373&ssl=1)](https://i0.wp.com/dotnettips.com/wp-content/uploads/2021/02/personrecord-gethashcode-source.jpg?ssl=1)

The default implementation of `ToString()` in most types typically returns the type name, which isn’t very informative. It’s generally recommended to override this method in classes and structures to provide a more meaningful representation of the data. However, with record types, overriding `ToString()` is unnecessary. For example, calling the `ToString()` method for a `Person` record might look like this:

1

``Person { Addresses = System.Collections.Generic.List`1[dotNetTips.Spargine.Tester.Models.Address], BornOn = 2/20/1974 1:06:36 PM -08:00, CellPhone = (858) 123-1234, Email = cokqfkkrfwmu@ysvwbustiojh.ly, FirstName = `OkRd_TQXfONhtH, HomePhone = 744-817-4861, Id = d6e1664bb11b421fb80fb8f1ef1804ab, LastName = gUbkABVdnrZ[crPCgTMfoGoe[ }``

The `Person` type contains a collection of `Address` objects. However, as demonstrated in the output above, the `ToString()` method does not accurately serialize these addresses. To address this issue, I developed a method called `PropertiesToString()` in the `IDataRecord` interface, which effectively serializes the addresses. Below is the implementation in the code:

1

`public` `override` `string` `ToString() =>` `this``.PropertiesToString();`

Here is the expected output from the `ToString()` method:

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

16

17

18

19

20

21

22

23

24

25

`Person.Addresses[0].Address1:13870 usuuffcrnjsdpgphhjp,`

`Person.Addresses[0].Address2:tnfuunfxrbrqkbigidw 43833,`

`Person.Addresses[0].City:,`

`Person.Addresses[0].Country:British Indian Ocean Territory,`

`Person.Addresses[0].CountyProvince:kyxbkbonverjxoetvcea,`

`Person.Addresses[0].Id:2d237cc1a73b47d7b5c1a8106a87fc98,`

`Person.Addresses[0].Phone:1647578148,`

`Person.Addresses[0].PostalCode:BB3D 1ZZ,`

`Person.Addresses[0].State:,`

`Person.Addresses[1].Address1:13728 xvvwxgjmrpdvjhxljgn,`

`Person.Addresses[1].Address2:ktstrsjmjqrfslpuxsm 55781,`

`Person.Addresses[1].City:,`

`Person.Addresses[1].Country:British Indian Ocean Territory,`

`Person.Addresses[1].CountyProvince:ubveipwvqkywdowqokhi,`

`Person.Addresses[1].Id:03aa7cde242545869832924fae8d2697,`

`Person.Addresses[1].Phone:2517715883,`

`Person.Addresses[1].PostalCode:XMWF5LG,`

`Person.Addresses[1].State:,`

`Person.BornOn:10/5/2004 2:01:09 PM -07:00,`

`Person.CellPhone:(858) 123-1234,`

`Person.Email:Ivy.Hebert@vmnjibch.ഭാരതം,`

`Person.FirstName:Ivy,`

`Person.Id:0f8db6fcbba1499d9857466b84a585b8,`

`Person.LastName:Hebert,`

`Person.Phone:4048740882`

This output provides a clear and accurate serialization of the `Address` collection, ensuring that all relevant information is represented properly. I have submitted an issue to the .NET team, but so far, they have not fixed it.

## Performance Considerations

Performance is _**critical**_ in my work; I even wrote a book on the subject. I conducted benchmarks to compare the performance of record types against value and reference types.

## Cloning

The benchmark below illustrates the performance differences in cloning between record types, value types, and reference types. This comparison highlights the varying speeds associated with each type of cloning operation, providing insights into their efficiency.

[![](https://i0.wp.com/dotnettips.com/wp-content/uploads/2021/02/cloning-types-chart.png?resize=700%2C269&ssl=1)](https://i0.wp.com/dotnettips.com/wp-content/uploads/2021/02/cloning-types-chart.png?ssl=1)

The benchmark results indicate that cloning a record is **1.12 times faster** than a value type and **1.23 times faster** than reference types.

## Computing Hash

The chart below displays the time required to hash reference types, value types, and record types.

[![](https://i0.wp.com/dotnettips.com/wp-content/uploads/2021/02/hashing-classes-records-structures.png?resize=700%2C294&ssl=1)](https://i0.wp.com/dotnettips.com/wp-content/uploads/2021/02/hashing-classes-records-structures.png?ssl=1)

When it comes to hashing, reference types are **1.02 times faster** than value types and **1.05 times faster** than record types.

## JSON Serialization

Serialization and deserialization of types to JSON is common, especially in API endpoints. Below are the results for this process.

[![](https://i0.wp.com/dotnettips.com/wp-content/uploads/2021/02/json-serialization.png?resize=700%2C293&ssl=1)](https://i0.wp.com/dotnettips.com/wp-content/uploads/2021/02/json-serialization.png?ssl=1)

[![](https://i0.wp.com/dotnettips.com/wp-content/uploads/2021/02/json-deserialization.png?resize=700%2C293&ssl=1)](https://i0.wp.com/dotnettips.com/wp-content/uploads/2021/02/json-deserialization.png?ssl=1)

## Looping and Sorting

Iterating over a list of records showed that it is less performant than reference types but faster than value types.

[![](https://i0.wp.com/dotnettips.com/wp-content/uploads/2021/02/list-foreach.png?resize=700%2C642&ssl=1)](https://i0.wp.com/dotnettips.com/wp-content/uploads/2021/02/list-foreach.png?ssl=1)

Sorting a list of record types is slightly faster than reference types and faster than value types.

[![](https://i0.wp.com/dotnettips.com/wp-content/uploads/2021/02/list-sort.jpg?resize=572%2C527&ssl=1)](https://i0.wp.com/dotnettips.com/wp-content/uploads/2021/02/list-sort.jpg?ssl=1)

These charts highlight some key performance differences between record types, reference types, and value types. If performance is a critical factor in your project, it’s essential to benchmark the performance of record types within your specific context.

## Summary

I hope this article enhances your understanding of record types and their performance benefits. If you’re interested, I encourage you to check out my coding standards book, where I detail the distinctions between record, reference, and value types. The key takeaway is that utilizing record types can significantly reduce coding effort and maintenance costs down the line.

Here are my main reasons for adopting record types, especially for DTOs:

1.  Simplifies the creation of immutable classes.
2.  Supports inheritance just like normal classes.
3.  Automatically generates equality operators, GetHashCode(), and a meaningful ToString() (with exceptions for collection properties).
4.  Can offer improved performance.

There are numerous advantages to migrating your projects to .NET 5 or above, and the introduction of record types is certainly one of them! If you have any comments or suggestions, please feel free to share below.

[![](https://i0.wp.com/dotnettips.com/wp-content/uploads/2024/05/cs-book-web-banner.png?resize=700%2C104&ssl=1)](https://dotnettips.com/2025/10/01/rock-your-code-coding-standards-for-microsoft-net-20th-anniversary-edition/)

![](https://i0.wp.com/dotnettips.com/wp-content/uploads/2026/01/rock-your-code-5th-web-banner.png?resize=700%2C104&ssl=1)

![](https://i0.wp.com/dotnettips.com/wp-content/uploads/2024/03/rock-your-code-5th-sponsor-web-banner.png?resize=700%2C104&ssl=1)

****Pick up any books by David McCarter by going to Amazon.com: [http://bit.ly/RockYourCodeBooks](http://bit.ly/RockYourCodeBooks)****

One-Time

Monthly

Yearly

#### Make a one-time donation

#### Make a monthly donation

#### Make a yearly donation

Choose an amount

$5.00

$15.00

$100.00

$5.00

$15.00

$100.00

$5.00

$15.00

$100.00

Or enter a custom amount

$

* * *

Your contribution is appreciated.

Your contribution is appreciated.

Your contribution is appreciated.

**If you liked this article, please** **buy David a cup of Coffee by going here:** [**https://www.buymeacoffee.com/dotnetdave**](https://www.buymeacoffee.com/dotnetdave)

**© The information in this article is copywritten and** _**cannot**_ **be reproduced in any way without express permission from David McCarter.**

Rate This

* * *

### Discover more from dotNetTips.com

Subscribe to get the latest posts sent to your email.
