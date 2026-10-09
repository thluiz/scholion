---
url: "http://www.toptal.com/c-sharp/top-10-mistakes-that-c-sharp-programmers-make"
captured_at: "2014-04-28T21:50:28-03:00"
title: "10 Most Common C# Mistakes | Toptal"
domain: "toptal-com"
---

# Top 10 Mistakes that C# Programmers Make

[View all articles](http://www.toptal.com/blog)

## About C#

[C#](http://en.wikipedia.org/wiki/C_Sharp_(programming_language)) is one of several languages that target the Microsoft [Common Language Runtime](http://msdn.microsoft.com/en-us/library/8bs2ecf4(v=vs.110).aspx) (CLR). Languages that target the CLR benefit from features such as
cross-language integration and exception handling, enhanced security, a
simplified model for component interaction, and debugging and profiling
services.  Of today’s CLR languages, C# is the most widely used for
complex, professional development projects that target the Windows
desktop, mobile, or server environments.

C# is an object oriented, strongly-typed language. The strict type
checking in C#, both at compile and run times, results in the majority
of typical programming errors being reported as early as possible, and
their locations pinpointed quite accurately. This can save the
programmer a lot of time, compared to tracking down the cause of
puzzling errors which can occur long after the offending operation takes
place in languages which are more liberal with their enforcement of type
safety.  However, a lot of programmers unwittingly (or carelessly) throw
away the benefits of this detection, which leads to some of the issues
discussed in this article.

## About this article

**This article describes 10 of the most common programming mistakes made, or pitfalls to be avoided, by C# programmers.**

While most of the mistakes discussed in this article are C# specific, some are also relevant to other languages that target the CLR or make use of the [Framework Class Library](http://msdn.microsoft.com/en-us/library/gg145045(v=vs.110).aspx) (FCL).

![5f8bd3ea65d785d8cafbc58d864453d4.gif](toptal-com--top-10-mistakes-csharp-programmers-make/5f8bd3ea65d785d8cafbc58d864453d4.gif)

## Common Mistake #1: Using a reference like a value or vice versa

Programmers of C++, and many other languages, are accustomed to being in
control of whether the values they assign to variables are simply values
or are references to existing objects. In C#, however, that decision is
made by the programmer who wrote the object, not by the programmer who
instantiates the object and assigns it to a variable.  This is a common
“gotcha” for newbie C# programmers.

If you don’t know whether the object you’re using is a value type or
reference type, you could run into some surprises. For example:

```
  Point point1 = new Point(20, 30);
  Point point2 = point1;
  point2.X = 50;
  Console.WriteLine(point1.X);       // 20 (does this surprise you?)
  Console.WriteLine(point2.X);       // 50
  
  Pen pen1 = new Pen(Color.Black);
  Pen pen2 = pen1;
  pen2.Color = Color.Blue;
  Console.WriteLine(pen1.Color);     // Blue (or does this surprise you?)
  Console.WriteLine(pen2.Color);     // Blue
```

As you can see, both the `Point` and `Pen` objects were created the exact same way, but the value of `point1` remained unchanged when a new `X` coordinate value was assigned to `point2`, whereas the value of `pen1` *was* modified when a new color was assigned to `pen2`. We can therefore *deduce* that `point1` and `point2` each contain their own copy of a `Point` object, whereas `pen1` and `pen2` contain references to the same `Pen` object. *But how can we know that without doing this experiment?*

The answer is to look at the definitions of the object types (which you
can easily do in Visual Studio by placing your cursor over the name of
the object type and pressing F12):

```
  public struct Point { … }     // defines a “value” type
  public class Pen { … }        // defines a “reference” type
```

As shown above, in C#, the `struct` keyword is used to define a value
type, while the `class` keyword is used to define a reference type. *For
those with a C++ background, who were lulled into a false sense of
security by the many similarities between C++ and C# keywords, this
behavior likely comes as a surprise.*

If you’re going to depend on some behavior which differs between value
and reference types – such as the ability to pass an object as a method
parameter and have that method change the state of the object – make
sure that you’re dealing with the correct type of object.

## Common Mistake #2: Misunderstanding default values for uninitialized variables

In C#, value types can’t be null. By definition, value types have a
value, and even uninitialized variables of value types must have a
value. This is called the default value for that type.  This leads to
the following, usually unexpected result when checking if a variable is
uninitialized:

```
  class Program {
      static Point point1;
      static Pen pen1;
      static void Main(string[] args) {
          Console.WriteLine(pen1 == null);      // True
          Console.WriteLine(point1 == null);    // False (huh?)
      }
  }
```

Why isn’t `point1` null? The answer is that `Point` is a value type, and the
default value for a `Point` is (0,0), not null. Failure to recognize this
is a very easy (and common) mistake to make in C#.

Many (but not all) value types have an `IsEmpty` property which you can
check to see if it is equal to its default value:

```
  Console.WriteLine(point1.IsEmpty);        // True
```

When you’re checking to see if a variable has been initialized or not,
make sure you know what value an uninitialized variable of that type
will have by default and don’t rely on it being null..

## Common Mistake #3: Using improper or unspecified string comparison methods

There are many different ways to compare strings in C#.

Although many programmers use the `==` operator for string comparison, it
is actually one of the *least* desirable methods to employ, primarily
because it doesn’t specify explicitly in the code which type of
comparison is wanted.

Rather, the preferred way to test for string equality in C# is with the `Equals` method:

```
  public bool Equals(string value);
  public bool Equals(string value, StringComparison comparisonType);
```

The first method signature (i.e., without the `comparisonType` parameter),
is actually the same as using the `==` operator, but has the benefit of
being explicitly applied to strings. It performs an ordinal comparison
of the strings, which is basically a byte-by-byte comparison. In many
cases this is exactly the type of comparison you want, especially when
comparing strings whose values are set programmatically, such as file
names, environment variables, attributes, etc. In these cases, as long
as an ordinal comparison is indeed the correct type of comparison for
that situation, the only downside to using the `Equals` method without a
`comparisonType` is that somebody reading the code may not know what type
of comparison you’re making.

Using the `Equals` method signature that includes a `comparisonType` every
time you compare strings, though, will not only make your code clearer,
it will make you explicitly think about which type of comparison you
need to make. This is a worthwhile thing to do, because even if English
may not provide a whole lot of differences between ordinal and
culture-sensitive comparisons, other languages provide plenty, and
ignoring the possibility of other languages is opening yourself up to a
lot of potential for errors down the road.  For example:

```
  string s = "strasse";
  
  // outputs False:
  Console.WriteLine(s == "straße");
  Console.WriteLine(s.Equals("straße"));
  Console.WriteLine(s.Equals("straße", StringComparison.Ordinal));
  Console.WriteLine(s.Equals("Straße", StringComparison.CurrentCulture));        
  Console.WriteLine(s.Equals("straße", StringComparison.OrdinalIgnoreCase));
  
  // outputs True:
  Console.WriteLine(s.Equals("straße", StringComparison.CurrentCulture));
  Console.WriteLine(s.Equals("Straße", StringComparison.CurrentCultureIgnoreCase));
```

The safest practice is to always provide a `comparisonType` parameter to
the `Equals` method. Here are some basic guidelines:

- When comparing strings that were input by the user, or are to be displayed to the user, use a culture-sensitive comparison (`CurrentCulture` or `CurrentCultureIgnoreCase`).
- When comparing programmatic strings, use ordinal comparison (`Ordinal` or `OrdinalIgnoreCase`).
- `InvariantCulture` and `InvariantCultureIgnoreCase` are generally not to be used except in very limited circumstances, because ordinal comparisons are more efficient.  If a culture-aware comparison is necessary, it should usually be performed against the current culture or another specific culture.

In addition to the `Equals` method, strings also provide the
`Compare` method, which gives you information about the relative order of
strings instead of just a test for equality. This method is preferable
to the `<`, `<=`, `>` and `>=` operators, for the same reasons as discussed
above.

## Common Mistake #4: Using iterative (instead of declarative) statements to manipulate collections

In C# 3.0, the addition of [Language-Integrated Query](http://msdn.microsoft.com/en-us/library/bb308959.aspx) (LINQ) to the language changed forever the way collections are queried and
manipulated.  Since then, if you’re using iterative statements to
manipulate collections, you didn’t use LINQ when you probably should
have.

Some C# programmers don’t even know of LINQ’s existence, but
fortunately that number is becoming increasingly small. Many still
think, though, that because of the similarity between LINQ keywords and
SQL statements, its only use is in code that queries databases.

While database querying is a very prevalent use of LINQ statements, they
actually work over any enumerable collection (i.e., any object that
implements the IEnumerable interface).  So for example, if you had an
array of Accounts, instead of writing:

```
  decimal total = 0;
  foreach (Account account in myAccounts) {
    if (account.Status == "active") {
      total += account.Balance;
    }
  }
```

you could just write:

```
  decimal total = (from account in myAccounts
                   where account.Status == "active"
                   select account.Balance).Sum();
```

While this is a pretty simple example, there are cases where a single
LINQ statement can easily replace dozens of statements in an iterative
loop (or nested loops) in your code.  And less code general means less
opportunities for bugs to be introduced. Keep in mind, however, there
may be a trade-off in terms of performance. In performance-critical
scenarios, especially where your iterative code is able to make
assumptions about your collection that LINQ cannot, be sure to do a
performance comparison between the two methods.

Editor's note: want posts just like this delivered straight to your inbox? Subscribe below to receive our latest engineering articles.

We will never share your email with any 3rd party or spam you

## Common Mistake #5: Failing to consider the underlying objects in a LINQ statement

LINQ is great for abstracting the task of manipulating collections,
whether they are in-memory objects, database tables, or XML documents.
 In a perfect world, you wouldn’t need to know what the underlying
objects are. But the error here is assuming we live in a perfect world.
 In fact, identical LINQ statements can return different results when
executed on the exact same data, if that data happens to be in a
different format.

For instance, consider the following statement:

```
  decimal total = (from account in myAccounts
                   where account.Status == "active"
                   select account.Balance).Sum();
```

What happens if one of the object’s `account.Status` equals “Active” (note
the capital A)?  Well, if `myAccounts` was a `DbSet` object (that was set up with the
default case-insensitive configuration), the `where` expression would
still match that element.  However, if `myAccounts` was in an in-memory
array, it would not match, and would therefore yield a different result for total.

But wait a minute.  When we talked about string comparison earlier, we
saw that the `==` operator performed an ordinal comparison of strings. So
why in this case is the `==` operator performing a case-insensitive
comparison?

*The answer is that when the underlying objects in a LINQ statement are
references to SQL table data (as is the case with the Entity Framework
DbSet object in this example), the statement is converted into a T-SQL
statement. Operators then follow T-SQL rules, not C# rules, so the
comparison in the above case ends up being case insensitive.*

In general, even though LINQ is a helpful and consistent way to query
collections of objects, in reality you still need to know whether or not
your statement will be translated to something other than C# under the
hood to ensure that the behavior of your code will be as expected at
runtime.

## Common Mistake #6: Getting confused or faked out by extension methods

As mentioned earlier, LINQ statements work on any object that implements
IEnumerable. For example, the following simple function will add up the
balances on any collection of accounts:

```
  public decimal SumAccounts(IEnumerable<Account> myAccounts) {
      return myAccounts.Sum(a => a.Balance);
  }
```

In the above code, the type of the myAccounts parameter is declared as
`IEnumerable<Account>`.  Since `myAccounts` references a `Sum` method (C#
uses the familiar “dot notation” to reference a method on a class or
interface), we’d expect to see a method called `Sum()` on the definition
of the `IEnumerable<T>` interface.  However, the definition of
`IEnumerable<T>`, makes no reference to any `Sum` method and simply looks
like this:

```
  public interface IEnumerable<out T> : IEnumerable {
      IEnumerator<T> GetEnumerator();
  }
```

So where is the `Sum()` method defined? C# is strongly typed, so if the
reference to the `Sum` method was invalid, the C# compiler would
certainly flag it as an error.  We therefore know that it must exist,
but where?  Moreover, where are the definitions of all the other methods
that LINQ provides for querying or aggregating these collections?

The answer is that `Sum()` is not a method defined on the
`IEnumerable` interface. Rather, it is a static method (called an
“extension method”) that is defined on the `System.Linq.Enumerable` class:

```
  namespace System.Linq {
    public static class Enumerable {
      ...
      // the reference here to “this IEnumerable<TSource> source” is
      // the magic sauce that provides access to the extension method Sum
      public static decimal Sum<TSource>(this IEnumerable<TSource> source,
                                         Func<TSource, decimal> selector);
      ...
    }
  }
```

So what makes an extension method different from any other static method
and what enables us to access it in other classes?

The distinguishing characteristic of an extension method is the
`this` modifier on its first parameter. This is the “magic” that
identifies it to the compiler as an extension method. The type of the
parameter it modifies (in this case `IEnumerable<TSource>`) denotes the
class or interface which will then appear to implement this method.

(As a side point, there’s nothing magical about the similarity between
the name of the `IEnumerable` interface and the name of the
`Enumerable` class on which the extension method is defined. This
similarity is just an arbitrary stylistic choice.)

With this understanding, we can also see that the `sumAccounts` function
we introduced above could instead have been implemented as follows:

```
  public decimal SumAccounts(IEnumerable<Account> myAccounts) {
      return Enumerable.Sum(myAccounts, a => a.Balance);
  }
```

The fact that we could have implemented it this way instead raises the
question of why have extension methods at all?  [Extension methods](http://msdn.microsoft.com/en-us/library/bb383977.aspx) are essentially a convenience of the C# language that enables you to “add” methods to existing types without creating a new derived type, recompiling, or otherwise modifying the original type.

Extension methods are brought into scope by including a `using [namespace];` statement at the top of the file. You need to know which
namespace includes the extension methods you’re looking for, but that’s
pretty easy to determine once you know what it is you’re searching for.

When the C# compiler encounters a method call on an instance of an
object, and doesn’t find that method defined on the referenced object
class, it then looks at all extension methods that are within scope to
try to find one which matches the required method signature and
class. If it finds one, it will pass the instance reference as the first
argument to that extension method, then the rest of the  arguments, if
any, will be passed as subsequent arguments to the extension method.
 (If the C# compiler doesn’t find any corresponding extension method
within scope, it will throw an error.)

Extension methods are an example of “syntactic sugar” on the part of the
C# compiler, which allows us to write code that is (usually) clearer
and more maintainable.  Clearer, that is, if you’re aware of their
usage. Otherwise, it can be a bit confusing, especially at first.

While there certainly are advantages to using extension methods, they
can cause headaches and wasted time for those developers who aren’t
aware of them or don’t properly understand them. This is especially true
when looking at code samples online, or at any other pre-written code.
When such code  produces compiler errors (because it invokes methods
that clearly aren’t defined on the classes they’re invoked on), the
tendency is to think the code applies to a different version of the
library, or to a different library altogether. A lot of time can be
spent searching for a new version, or phantom “missing library”, that
doesn’t exist.

Even developers who are familiar with extension methods still get caught
occasionally, when there is a method with the same name on the object,
but its method signature differs in a subtle way from that of the
extension method. A lot of time can be wasted looking for a typo or
error that just isn’t there.

Use of extension methods in C# libraries is becoming increasingly
prevalent.  In addition to LINQ, the [Unity Application Block](http://msdn.microsoft.com/en-us/library/ff648512.aspx) and the [Web API framework](http://msdn.microsoft.com/en-us/library/hh833994%28v=vs.108%29.aspx) are
examples of two heavily-used modern libraries by Microsoft which make
use of extension methods as well, and there are many others. The more
modern the framework, the more likely it is that it will incorporate
extension methods.

Of course, you can write your own extension methods as well. Realize,
however, that while extension methods appear to get invoked just like
regular instance methods, this is really just an illusion.  In
particular, your extension methods can’t reference private or protected
members of the class they’re extending and therefore cannot serve as
a complete replacement for more traditional class inheritance.

## Common Mistake #7: Using the wrong type of collection for the task at hand

C# provides a large variety of collection objects, with the following
being only a partial list:  
`Array`, `ArrayList`, `BitArray`, `BitVector32`, `Dictionary<K,V>`, `HashTable`, `HybridDictionary`, `List<T>`, `NameValueCollection`, `OrderedDictionary`, `Queue, Queue<T>`, `SortedList`, `Stack, Stack<T>`, `StringCollection`, `StringDictionary`.

While there can be cases where too many choices is as bad as not enough
choices, that isn’t the case with collection objects. The number of
options available can definitely work to your advantage.  Take a little
extra time upfront to research and choose the optimal collection type
for your purpose.  It will likely result in better performance and less
room for error.

If there’s a collection type specifically targeted at the type of
element you have (such as string or bit) lean toward using that one
first. The implementation is much more efficient when it’s targeted to a
specific type of element.

To take advantage of the type safety of C#, you should usually prefer a
generic interface over a non-generic one. The elements of a generic
interface are of the type you specify when you declare your object,
whereas the elements of non-generic interfaces are of type object. When
using a non-generic interface, the C# compiler can’t type-check your
code. Also, when dealing with collections of primitive value types,
using a non-generic collection will result in repeated
[boxing/unboxing](http://msdn.microsoft.com/en-us/library/yz2be5wk.aspx) of
those types, which can result in a significant negative performance
impact when compared to a generic collection of the appropriate type.

Another common pitfall is to write your own collection object. That
isn’t to say it’s never appropriate, but with as comprehensive a
selection as the one .NET offers, you can probably save a lot of time by
using or extending one that already exists, rather than reinventing the
wheel.  In particular, the [C5 Generic Collection Library](https://www.itu.dk/research/c5/) for C# and CLI offers a wide array of additional collections “out of the box”, such as persistent tree data structures, heap based priority
queues, hash indexed array lists, linked lists, and much more.

## Common Mistake #8: Neglecting to free resources

The CLR environment employs a garbage collector, so you don’t need to
explicitly free the memory created for any object. In fact, you can’t.
There’s no equivalent of the C++ `delete` operator or the `free()` function
in C . But that doesn’t mean that you can just forget about all objects
after you’re done using them. Many types of objects encapsulate some
other type of system resource (e.g., a disk file, database connection,
network socket, etc.).  Leaving these resources open can quickly deplete
the total number of system resources, degrading performance and
ultimately leading to program faults.

While a destructor method can be defined on any C# class, the problem
with destructors (also called finalizers in C#) is that you can’t know
for sure when they will be called. They are called by the garbage
collector (on a separate thread, which can cause additional
complications) at an indeterminate time in the future. Trying to get
around these limitations by forcing garbage collection with
`GC.Collect()` is not a good practice, as that will block the thread for
an unknown amount of time while it collects all objects eligible for
collection.

This is not to say there are no good uses for finalizers, but freeing
resources in a deterministic way isn’t one of them. Rather, when you’re
operating on a file, network or database connection, you want to
explicitly free the underlying resource as soon as you are done with it.

Resource leaks are a concern in almost any environment. However, C#
provides a mechanism that is robust and simple to use which, if
utilized, can make leaks a much rarer occurrence. The .NET framework
defines the `IDisposable` interface, which consists solely of the
`Dispose()` method. Any object which implements `IDisposable` expects to
have that method called whenever the consumer of the object is finished
manipulating it. This results in explicit, deterministic freeing of
resources.

If you are creating and disposing of an object within the context of a
single code block, it is basically inexcusable to forget to call
`Dispose()`, because C# provides a `using` statement that will ensure
`Dispose()` gets called no matter how the code block is exited (whether it
be an exception, a return statement, or simply the closing of the
block). And yes, that’s the same `using` statement mentioned previously that is used to include namespaces at the top of your file. It
has a second, completely unrelated purpose, which many C# developers
are unaware of; namely, to ensure that `Dispose()` gets called on an
object when the code block is exited:

```
  using (FileStream myFile = File.OpenRead("foo.txt")) {
    myFile.Read(buffer, 0, 100);
  }
```

By creating a `using`block in the above example, you know for sure that
`myFile.Dispose()` will be called as soon as you’re done with the file,
whether or not `Read()` throws an exception.

## Common Mistake #9: Shying away from exceptions

C# continues its enforcement of type safety into runtime. This allows
you to pinpoint errors much more quickly than in languages such as C++,
where faulty type conversions can result in arbitrary values being
assigned to an object’s fields. However, once again, programmers can
squander this great feature of C#. They fall into this trap because C#
provides two different ways of doing things, one which can throw an
exception, and one which won’t. Some will shy away from the exception
route, figuring that not having to write a try/catch block saves them
some coding.

For example, here are two different ways to perform an explicit type cast in C#:

```
  // METHOD 1:
  // Throws an exception if account can't be cast to SavingsAccount
  SavingsAccount savingsAccount = (SavingsAccount)account;
  
  // METHOD 2:
  // Does NOT throw an exception if account can't be cast to
  // SavingsAccount; will just set savingsAccount to null instead
  SavingsAccount savingsAccount = account as SavingsAccount;
```

The most obvious error that could occur with the use of Method 2 would
be a failure to check the return value. That would likely result in an
eventual NullReferenceException, which could possibly surface at a much
later time, making it much harder to track down the source of the
problem.  In contrast, Method 1 would have immediately thrown an
`InvalidCastException` making the source of the problem much more
immediately obvious.

Moreover, even if you remember to check the return value in Method 2,
what are you going to do if you find it to  be null? Is the method
you’re writing an appropriate place to report an error? Is there
something else you can try if that cast fails? If not, then throwing an
exception is the correct thing to do, so you might as well let it happen
as close to the source of the problem as possible.

Here are a couple of examples of other common pairs of methods where one
throws an exception and the other does not:

```
  int.Parse();     // throws exception if argument can’t be parsed
  int.TryParse();  // returns a bool to denote whether parse succeeded
  
  IEnumerable.First();           // throws exception if sequence is empty
  IEnumerable.FirstOrDefault();  // returns null/default value if sequence is empty
```

Some programmers are so “exception adverse” that they automatically
assume the method that doesn’t throw an exception is superior.  While
there are certain select cases where this may be true, it is not at all
correct as a generalization.

As a specific example, in a case where you have an alternative
legitimate (e.g., default) action to take if an exception would have
been generated, then that the non-exception approach could be a
legitimate choice.  In such a case, it may indeed be better to write
something like this:

```
  if (int.TryParse(myString, out myInt)) {
    // use myInt
  } else {
    // use default value
  }
```

instead of:

```
  try {
    myInt = int.Parse(myString);
    // use myInt
  } catch (FormatException) {
    // use default value
  }
```

However, it is incorrect to assume that `TryParse` is therefore
necessarily the “better” method.  Sometimes that’s the case, sometimes
it’s not. That’s why there are two ways of doing it. Use the correct one
for the context you are in, remembering that exceptions can certainly be
your friend as a developer.

## Common Mistake #10: Allowing compiler warnings to accumulate

While this one is definitely not C# specific, it is particularly
egregious in C# since it abandons the benefits of the strict type
checking offered by the C# compiler.

Warnings are generated for a reason.  While all C# compiler errors
signify a defect in your code, many warnings do as well. What
differentiates the two is that, in the case of a warning, the compiler
has no problem emitting the instructions your code represents. Even so,
it finds your code a little bit fishy, and there is a reasonable
likelihood that your code doesn’t accurately reflect your intent.

A common simple example is when you modify your algorithm to eliminate
the use of a variable you were using, but you forget to remove the
variable declaration. The program will run perfectly, but the compiler
will flag the useless variable declaration. The fact that the program
runs perfectly causes programmers to neglect to fix the cause of the
warning. Furthermore, programmers take advantage of a Visual Studio
feature which makes it easy for them to hide the warnings in the “Error
List” window so they can focus only on the errors. It doesn’t take long
until there are dozens of warnings, all of them blissfully ignored (or
even worse, hidden).

But if you ignore this type of warning, sooner or later, something like
this may very well find its way into your code:

```
  class Account {
  
      int myId;
      int Id;   // compiler warned you about this, but you didn’t listen!
  
      // Constructor
      Account(int id) {
          this.myId = Id;     // OOPS!
      }
  
  }
```

And at the speed Intellisense allows us to write code, this error isn’t
as improbable as it looks.

You now have a serious error in your program (although the compiler has
only flagged it as a warning, for the reasons already explained), and
depending on how complex your program is, you could waste a lot of time
tracking this one down. Had you paid attention to this warning in the
first place, you would have avoided this problem with a simple
five-second fix.

**Remember, the C# compiler gives you a lot of useful information about
the robustness of your code… if you’re listening. Don’t ignore
warnings.** They usually only take a few seconds to fix, and fixing new
ones when they happen can save you hours. Train yourself to expect the
Visual Studio “Error List” window to display “0 Errors, 0 Warnings”, so
that any warnings at all make you uncomfortable enough to address them
immediately.

Of course, there are exceptions to every rule.  Accordingly, there may
be times when your code will look a bit fishy to the compiler, even
though it is exactly how you intended it to be. In those very rare
cases, use `#pragma warning disable [warning id]` around only the code
that triggers the warning, and only for the warning ID that it triggers.
This will suppress that warning, and that warning only, so that you can
still stay alert for new ones.

## Wrap-up

C# is a powerful and flexible language with many mechanisms and
paradigms that can greatly improve productivity.  As with any software
tool or language, though, having a limited understanding or appreciation
of its capabilities can sometimes be more of an impediment than a
benefit, leaving one in the proverbial state of “knowing enough to be
dangerous”.

Familiarizing oneself with the key nuances of C#, such as (but by no means limited to) the issues raised in this article, will help optimize use of the language while avoiding some of its more common pitfalls.

[Looking to hire top engineers? Check out Toptal's C# developers!](http://www.toptal.com/c-sharp)
