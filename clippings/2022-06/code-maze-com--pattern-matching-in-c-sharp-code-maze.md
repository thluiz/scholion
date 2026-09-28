---
url: "https://code-maze.com/csharp-pattern-matching/"
captured_at: "2022-06-16T09:27:02-03:00"
title: "Pattern Matching in C# - Code Maze"
domain: "code-maze-com"
---

# Pattern Matching in C#

Posted by [Code Maze](https://code-maze.com/author/codemazecontributor/ "Posts by Code Maze") | Jun 15, 2022 | [0](https://code-maze.com/csharp-pattern-matching/#comments)

In this article, we are going to talk about pattern matching in C#. We’ll see different patterns in action with simple examples.

To download the source code for this article, you can visit our [GitHub repository](https://github.com/CodeMazeBlog/CodeMazeGuides/tree/main/csharp-basic-topics/Patterns).

Let’s take a look at seven different types of pattern matching in C#!

## What is Pattern Matching?

Essentially with pattern matching, we can check if two things are equivalent.

But why is this useful?  One example includes allowing us to make decisions based on the type of something rather than the value of something.

Prior to pattern matching, we first would need to validate a condition to determine the object’s type.  After discovering the type, we would have to perform a cast so we could treat the object accordingly. However, utilizing pattern matching in C#, we can make a decision on whether to use the object based on the type alone!

Additionally, pattern matching is not limited to type matching, but can be applied in a variety of different contexts that C# has included since version 7.0 by mainly utilizing the [switch statement](https://code-maze.com/csharp-conditions-if-else-swtich-case/), [is operator](https://code-maze.com/csharp-as-is-operators/), or [switch expression](https://code-maze.com/csharp-switch-multiple-cases-return-same-result/).

In short, we can take lengthy nested `if` statements and turn them into a few clean readable lines of code.

## Type Patterns

Type patterns check to see if the given expression is not null. If not null, then the pattern checks to determine whether the expression is the same or can be cast to the same specified type.

For our pattern matching examples, we will be using a custom abstract object `Animal` that we will implement by various custom classes (i.e. `Cat`, `Dog`, etc.):

privatestaticstringMatchTypePattern(Animal animal) => animal switch

{

Cat =>"Meow",

Dog =>"Bark",

null =>"Please Provide A Non-Null Animal Object!",

\_ => $"Unknown Animal {nameof(animal)}!"

};

```
private static string MatchTypePattern(Animal animal) => animal switch
{
    Cat => "Meow",
    Dog => "Bark",
    null => "Please Provide A Non-Null Animal Object!",
    _ => $"Unknown Animal {nameof(animal)}!"
};
```

Based on the type of object, we return a string message. Notice how we can gracefully determine whether the object provided is null or is one of the `Animal` implementations.  Remember that we can use the “discard” symbol `_` to match anything else that we did not list – including null.

To use the method we can initialize a new `Cat` object and call `MatchTypePattern`:

var message = MatchTypePattern(newCat());

Note that we could use this same method to assign a result to a declared variable also known as a *Declaration Pattern.*

## Constant Pattern

We use a constant pattern to perform an equality check with a stored value against a set of values:

privatestaticstringMatchConstantPattern(string animalmessage) => animalmessage switch

{

"Meow" =>"Cat",

"Bark" =>"Dog",

null =>"Please Provide A Non-Null Message!",

\_ => $"Unknown Animal Message {animalmessage}!"

};

```
private static string MatchConstantPattern(string animalmessage) => animalmessage switch
{
    "Meow" => "Cat",
    "Bark" => "Dog",
    null => "Please Provide A Non-Null Message!",
    _ => $"Unknown Animal Message {animalmessage}!"
};
```

This pattern matches the value and not the type (as the *Type Pattern does*).  Again, we were able to gracefully handle an exact match for whatever string we passed to the method while also checking for null and handling unexpected inputs.

We can call `MatchConstantPattern` by supplying a string message as our parameter to be matched against the constants we listed:

var name = MatchConstantPattern("Bark");

## Relational Patterns

Relational patterns allow us to use comparison operators (such as `< > <= >=`) to determine if the current value matches the given comparison expression:

privatestaticstringMatchRelationalPattern(int? animalcount) => animalcount switch

{

<1000 =>"Less than one thousand animals",

>= 1000 =>"Greater than or equal to one thousand animals"

};

```
private static string MatchRelationalPattern(int? animalcount) => animalcount switch
{
    < 1000 => "Less than one thousand animals",
    >= 1000 => "Greater than or equal to one thousand animals"
};
```

If the number of animals is within the specified range, the expression returns the corresponding string message.

We can then call the method which returns the `"Less than two animals"` message:

MatchRelationalPattern(1);

## Logical Patterns

We can incorporate logical patterns in conjunction with the other patterns mentioned in this article. With logical patterns, we can use `and`, `or`, and `not` operators within the pattern expressions. The simplest example is performing a null check so we can call the `MatchRelationPattern` method safely:

if(numberOfAnimals is not null)MatchRelationalPattern(numberOfAnimals);

Furthermore, we can extend a relational pattern to better match whatever pattern we desire:

privatestaticstringMatchLogicalPattern(int animalage) => animalage switch

{

0or(>0 and <5) =>"Baby animal",

>= 5 and <= 13 =>"Child animal",

>13 and <20 =>"Teenage animal",

>= 20 and <60 =>"Adult animal",

>= 60 =>"Senior animal",

\_ =>"Unborn animal"

};

```
private static string MatchLogicalPattern(int animalage) => animalage switch
{
    0 or (> 0 and < 5) => "Baby animal",
    >= 5 and <= 13 => "Child animal",
    > 13 and < 20 => "Teenage animal",
    >= 20 and < 60 => "Adult animal",
    >= 60 => "Senior animal",
    _ => "Unborn animal"
};
```

We can now match against multiple specified ranges and not limit ourselves to matching a specific constant! Remember that the order of operations for resolving the logical operators within the same expression is `not`, `and`, `or` respectively. However, we can use parenthesis to change the order of any of the comparisons (as shown in the “Baby Animal” case).

We can use this method in a very similar manner as we did so far, which would return the `"Adult animal"` message:

MatchLogicalPattern(20);

## Property Pattern

We can use a property pattern to check a non-null object and its specific properties to match our specified criteria:

privatestaticboolMatchPropertyPattern(Animal animal) => animal is

{

Name: "Dog", Description: "furry animal with tail and paws", Cloned: false or true

};

```
private static bool MatchPropertyPattern(Animal animal) => animal is
{
    Name: "Dog", Description: "furry animal with tail and paws", Cloned: false or true
};
```

Notice how we can simply list as many comma-separated properties of the object that we want to check. Additionally, we can include the logical operators to expand the criteria for our pattern (as shown for the `Cloned` property). If any one of the checks fails, then the entire expression returns false.

By simply providing a new Dog instance the `MatchPropetyPattern` method returns true:

MatchPropertyPattern(newDog());

## Positional Pattern

We can utilize a positional pattern to take a result and match it positionally against multiple values:

privatestaticstringMatchPositionalPattern(int animalage, int animalweight) =>(animalage, animalweight)switch

{

(<= 20, <= 50) =>"Healthy young animal weight",

(<= 20, >50) =>"Unhealthy young animal weight",

(>= 21, <= 100) =>"Healthy adult animal weight",

(>= 21, >100) =>"Unhealthy adult animal weight"

};

```
private static string MatchPositionalPattern(int animalage, int animalweight) => (animalage, animalweight) switch
{
    ( <= 20, <= 50) => "Healthy young animal weight",
    ( <= 20, > 50) => "Unhealthy young animal weight",
    ( >= 21, <= 100) => "Healthy adult animal weight",
    ( >= 21, > 100) => "Unhealthy adult animal weight"
};
```

We can take the given parameters of the method and turn them into a tuple that we can compare at one time. See how we use this pattern to remove the need for additional code that we would need to check each value separately?

Calling the `MatchPositionalPattern` gives us the result of `"Unhealthy adult animal weight"`:

MatchPositionalPattern(50, 10000);

## Var Pattern

The var pattern temporarily holds and checks any values that we need within the expression:

publicstaticboolMatchVarPattern(Animal animal) =>

animal.CreateClone()isvar clone

&& clone.Clone

&& animal.Cloned

&& animal.GetType() == clone.GetType();

```
public static bool MatchVarPattern(Animal animal) => 
            animal.CreateClone() is var clone 
            && clone.Clone 
            && animal.Cloned
            && animal.GetType() == clone.GetType();
```

The type of var is determined at compile time and will be the result of the `Animal CreateClone` method.  We can then perform checks on the result of what we stored from the `CreateClone` method!

Calling this method will return a boolean as to whether the clone was successful:

var cloned = MatchVarPattern(newDog());

## Conclusion

We have now gone through seven different types of pattern matching in C#!  We hope that going forward, this knowledge will help you to write code that is more readable and maintainable thanks to this modern approach to dealing with patterns.
