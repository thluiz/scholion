---
url: "https://thaitran.hashnode.dev/how-to-code-like-a-pro-in-2022-and-avoid-if-else?source=newsletter"
captured_at: "2022-06-24T11:48:25-03:00"
title: "How to code like a pro in 2022 and avoid If-Else"
domain: "thaitran-hashnode-dev"
---

# How to code like a pro in 2022 and avoid If-Else

Featured on Hashnode

Using If-Else is one of the programming fundamentals that we learned in college and it is helpful to get us into our first jobs. Interestingly, many senior developers are convinced that If-Else is **evil** and you should avoid using If-Else in your code whenever possible.

Let's take a look at these examples:

## How a junior developer writes code

```
var input = "Dog";
var output = "";
if (input == "Dog")
{
    output = "Bow Wow";
}
else if (input == "Cat")
{
    output = "Meow Meow";
}
else if (input == "Chicken")
{
    output = "Cluck Cluck";
}
else if (input == "Pig")
{
    output = "Oink Oink";
}
```

In this example, our developer needs to output the sound of different animals accordingly to the input. He can easily repeat the logic using If-Else statements.

Let's take a look at how this code will be written by a mid-level developer:

## How a mid-level developer writes code

```
var input = "Dog";
var output = "";
switch (input)
{
    case "Dog":
        output = "Bow Wow";
        break;
    case "Cat":
        output = "Meow Meow";
        break;
    case "Chicken":
        output = "Cluck Cluck";
        break;
    case "Pig":
        output = "Oink Oink";
        break;
}
```

By switching to a switch statement, our developer can avoid using If-Else in his code and get the same result but yet this is not the best solution.

Let's take a look at how a senior developer writes code

## How a senior developer writes code

```
var input = "Dog";
var map = new Dictionary<string, string>
{
    { "Dog", "Bow Wow" },
    { "Cat", "Meow Meow" },
    { "Chicken", "Cluck Cluck" },
    { "Pig", "Oink Oink" }
};

map.TryGetValue(input, out var output);
```

In this example, you can store the animal name and the animal sound as key-value pairs in a dictionary and call the `TryGetValue` method to get the output. This way, the code is more readable.

## But things could get more complicated

For example, we need to use a comparer other than an exact match and then, take an action accordingly. If the input contains the keyword `Dog`, then use it to filter the dog breeds. If the input contains the keyword `Cat`, then use it to filter the cat breeds.

A junior developer might solve this problem using If-Else statements:

```
var input = "Dachshund Dog";
var dogBreeds = new[] { "Dachshund" };
var catBreeds = new[] { "British Shorthair" };
var result = Enumerable.Empty<string>();
if (input.Contains("Dog"))
{
    result = dogBreeds.Where(b => input.Contains(b));
}
else if (input.Contains("Cat"))
{
    result = catBreeds.Where(b => input.Contains(b)); 
}
```

As he needs more conditions, he will keep adding If-Else to his code. The code will become nonreusable and harder to read. When this code is handed over to a senior developer, it will be rewritten as follows:

```
var input = "Dachshund Dog";
var dogBreeds = new[] { "Dachshund" };
var catBreeds = new[] { "British Shorthair" };
var result = Enumerable.Empty<string>();
var eval = delegate (string key, string[] array)
{
    if (!input.Contains(key))
        return false;
    result = array.Where(b => input.Contains(b));
    return true;
};
var conditions = new[] {
    () => eval("Dog", dogBreeds),
    () => eval("Cat", catBreeds)
};
conditions.Any(c=> c());
```

By moving your action to a delegate, you can reuse the same action for different conditions. Storing the delegates in an array and using `LINQ Any()` to invoke these functions will give you the same result. The best part is that the evaluation will exit as soon as a true condition is returned by one of these functions and this will save the performance.

If you're a junior developer, you should learn and use these pro tips. You will become a senior developer tomorrow. Remember:

> Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live

Thanks for reading ❤️
