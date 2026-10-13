---
url: "http://www.toptal.com/dot-net/interview-questions"
captured_at: "2016-02-21T18:06:10-03:00"
title: "Essential .NET Interview Questions"
domain: "toptal-com"
---

# 12 Essential .NET Interview Questions\*

Explain the difference between a class and an object.

Hide answer

In short, a class is the definition of an object, and an object is instance of a class.

We can look at the class as a template of the object: it describes all the properties, methods, states and behaviors that the implementing object will have. As mentioned, an object is an instance of a class, and a class does not become an object until it is instantiated. There can be more instances of objects based on the one class, each with different properties.

[Comment](http://www.toptal.com/dot-net/interview-questions#)

Explain the difference between managed and unmanaged code.

Hide answer

Managed code is a code created by the .NET compiler. It does not depend on the architecture of the target machine because it is executed by the CLR (Common Language Runtime), and not by the operating system itself. CLR and managed code offers developers few benefits, like garbage collection, type checking and exceptions handling.

On the other hand, unmanaged code is directly compiled to native machine code and depends on the architecture of the target machine. It is executed directly by the operating system. In the unmanaged code, the developer has to make sure he is dealing with memory usage and allocation (especially because of memory leaks), type safety and exceptions manually.

In .NET, Visual Basic and C# compiler creates managed code. To get unmanaged code, the application has to be written in C or C++.

[Comment](http://www.toptal.com/dot-net/interview-questions#)

Explain the difference between the `while` and `for` loop. Provide a .NET syntax for both loops.

Hide answer

Both loops are used when a unit of code needs to execute repeatedly. The difference is that the `for` loop is used when you know how many times you need to iterate through the code. On the other hand, the `while` loop is used when you need to repeat something until a given statement is true.

The syntax of the `while` loop in C# is:

```
while (condition [is true])
{
  // statements
}
```

The syntax of the `while` loop in VB.NET is:

```
While condition [is True]
  ' statements
End While
```

The syntax of the `for` loop in C# is:

```
for (initializer; condition; iterator)
{
  // statements
}
```

The syntax of the `for` loop in VB.NET is:

```
For counter [ As datatype ] = start To end [ Step step ]
  ' statements
Next [ counter ]
```

[Comment](http://www.toptal.com/dot-net/interview-questions#)

Explain the difference between boxing and unboxing. Provide an example.

Hide answer

Boxing is the process of converting a value type to the type object, and unboxing is extracting the value type from the object. While the boxing is implicit, unboxing is explicit.

Example (written in C#):

```
int i = 13;
object myObject = i;    // boxing 
i = (int)myObject;      // unboxing
```

[Comment](http://www.toptal.com/dot-net/interview-questions#)

Discuss the difference between constants and read-only variables.

View the answer →

Explain what LINQ is.

View the an     swer →

Discuss what garbage collection is and how it works. Provide a code example of how you can enforce garbage collection in .NET.

View the answer →

What do the following acronyms in .NET stand for: IL, CIL, MSIL, CLI and JIT?

View the answer →

Explain the difference between the Stack and the Heap.

View the answer →

Explain what inheritance is, and why it’s important.

View the answer →

Explain the differences between an Interface and an Abstract Class in .NET.

View the answer →

Explain deferred execution vs. immediate execution in LINQ. Provide examples.

View the answer →

\* There is more to interviewing than tricky technical questions, so these are intended merely as a guide. Not every “A” candidate worth hiring will be able to answer them all, nor does answering them all guarantee an “A” candidate. At the end of the day, [hiring remains an art, a science — and a lot of work](http://www.toptal.com/freelance/in-search-of-the-elite-few-finding-and-hiring-the-best-developers-in-the-industry).
