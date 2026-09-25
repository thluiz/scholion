---
url: "https://www.damirscorner.com/blog/posts/20250110-MemoizationForARecursiveFunctionInFSharp.html"
captured_at: "2026-09-25T21:54:01+01:00"
title: "Memoization for a recursive function in F#"
domain: "damirscorner-com"
---

This year I decided to solve the [Advent of Code](https://adventofcode.com/2024) puzzles using [F#, the functional programming language for .NET](https://dotnet.microsoft.com/en-us/languages/fsharp?WT.mc_id=DOP-MVP-4039670). Since I had very little previous experience with F#, this meant a lot of learning about the language as I was implementing my solutions. For [one of the puzzles](https://adventofcode.com/2024/day/11), [memoization](https://en.wikipedia.org/wiki/Memoization) seemed the best approach, which meant I had to find a way to implement it in F#.

The idea of memoization is to store the results of previous function calls so that the expensive calculation doesn't need to be repeated when the function is called again with the same parameters. For this to work, the function must be [pure](https://en.wikipedia.org/wiki/Pure_function), i.e., its result must always be the same for the same values of input parameters, and it mustn't have any side effects. This allows the function call to be skipped if the result is already known, without affecting the final outcome.

My first attempted solution for the puzzle was already written as a pair of pure functions. It was just too slow because the recursive function was recalculating the same results over and over:

```
let private transform (stone: int64) =  
    if stone = 0 then  
        [1L]  
    else  
        let stoneString = string stone  
        if stoneString.Length % 2 = 0 then  
            let halfLength = stoneString.Length / 2  
            [ int64 (stoneString.Substring(0, halfLength))  
              int64 (stoneString.Substring(halfLength)) ]  
        else  
            [stone * 2024L]  

let rec simpleStoneCountAfterBlinking blinks stone =  
    let newStones = transform stone  
    if blinks = 1 then  
        int64 newStones.Length  
    else  
        newStones  
        |> List.sumBy (simpleStoneCountAfterBlinking (blinks - 1))
```

This made it a perfect candidate for optimization using memoization. I quickly learned that there is no built-in support for memoization in F#, which meant that I'd have to implement it myself. [Don Syme](https://www.microsoft.com/en-us/research/people/dsyme/), the original author of F#, [blogged about memoization](https://dsyme.home.blog/2007/05/31/a-sample-of-the-memoization-pattern-in-f/) already in the early days of the language. As I tried to implement his approach, it became obvious that it wasn't suitable for recursive functions because the recursive calls still invoked the original function without memoization.

I couldn't think of a way to expand the concept to make it work with recursive functions myself, so I finally found [a newer blog post](https://riptutorial.com/fsharp/example/29649/memoization-in-a-recursive-function) by a different author which did exactly that. The important part was the extra parameter with the function to use for the recursive call, so that the wrapper function could pass a memoized version as the parameter:

```
let stoneCountAfterBlinkingForMemoization recursiveFunction (blinks, stone) =  
    let newStones = transform stone  
    if blinks = 1 then  
        int64 newStones.Length  
    else  
        newStones  
        |> List.sumBy (fun s -> recursiveFunction (blinks - 1, s))
```

You might have noticed that I also converted the original two parameters of my function into a tuple to make them look like a single parameter to the wrapper function:

```
let memoizeWithDictionary f =  
    let cache = Dictionary<_,_>()  
    let rec memoized param =  
        match cache.TryGetValue param with  
        | true, cachedValue -> cachedValue  
        | false, _ ->  
            let result = f memoized param  
            cache.Add (param, result)  
            result  
    memoized
```

The wrapper function is used to create a memoized version of a recursive function:

```
let memoized = memoizeWithDictionary(stoneCountAfterBlinkingForMemoization)
```

I used [a mutable dictionary from the .NET base class library](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?WT.mc_id=DOP-MVP-4039670) for the cache as suggested in the blog post I was basing my code on. Since Don Syme also included an example using [an immutable F# map](https://fsharp.github.io/fsharp-core-docs/reference/fsharp-collections-fsharpmap-2.html) stored in a mutable variable, I tried modifying that one for the recursive case as well:

```
let memoizeWithMap f =  
    let mutable cache = Map.empty  
    let rec memoized param =  
        match cache.TryFind param with  
        | Some cachedValue -> cachedValue  
        | None ->  
            let result = f memoized param  
            cache <- cache.Add(param, result)  
            result  
    memoized
```

The wrapper is still used the exact same way to create a memoized version of a recursive function:

```
let memoized = memoizeWithMap(stoneCountAfterBlinkingForMemoization)
```

As an alternative to the memoization approach which hides the fact that the results are cached from the caller, I also implemented a function which can be used with [the `mapFold` operation](https://fsharp.github.io/fsharp-core-docs/reference/fsharp-collections-listmodule.html#mapFold) and caches the results in a map that's passed in as the state:

```
let rec stoneCountAfterBlinkingWithCache cache (blinks, stone) =  
    let cacheKey = (blinks, stone)  
    match cache |> Map.tryFind cacheKey with  
    | Some cachedResult -> cachedResult, cache  
    | None ->  
        let newStones = transform stone  
        let result, updatedCache =  
            if blinks = 1 then  
                int64 newStones.Length, cache  
            else  
                let stoneCounts, cacheFromFold =  
                    newStones  
                    |> List.map (fun s -> blinks - 1, s)  
                    |> List.mapFold stoneCountAfterBlinkingWithCache cache  
                List.sum stoneCounts, cacheFromFold  
        result, updatedCache.Add (cacheKey, result)
```

This required even more changes to my recursive function:

*   As required by the `mapFold` operation, the cache is passed into the function as its first parameter and returned as part of the result.
*   [The `sumBy` operation](https://fsharp.github.io/fsharp-core-docs/reference/fsharp-collections-listmodule.html#sumBy) with the recursive function call is split into three parts:
    *   A preparation step in which I prepared the input parameters as a map of tuples instead of creating the tuple on-the-fly as part of the recursive function call.
    *   A recursive call inside map fold to map the stones to the length of their resulting sequence while passing along a cache with previous results.
    *   A final summation of the sequence lengths across all stones.
*   The final result is added to the cache before both are returned from the function.

Of course, I was interested in how all implemented approaches compare performance-wise. I used [BenchmarkDotNet](https://www.nuget.org/packages/BenchmarkDotNet) to measure it for three different number of blinks. I didn't want to further increase the number of blinks as it was already enough to see the pattern, and the simple implementation without caching took exceeding long for larger numbers.

Method

blinks

Mean

Error

StdDev

Ratio

RatioSD

Simple

25

2,775.7 us

19.84 us

18.56 us

1.00

0.01

Dictionary

25

101.8 us

0.58 us

0.49 us

0.04

0.00

MutableMap

25

1,382.1 us

10.63 us

9.43 us

0.50

0.00

MapState

25

1,410.2 us

6.89 us

6.45 us

0.51

0.00

Simple

30

22,840.2 us

208.15 us

173.81 us

1.000

0.01

Dictionary

30

140.9 us

2.07 us

1.83 us

0.006

0.00

MutableMap

30

1,892.1 us

8.45 us

7.49 us

0.083

0.00

MapState

30

2,043.9 us

12.31 us

10.91 us

0.089

0.00

Simple

35

181,954.4 us

2,287.77 us

2,028.04 us

1.000

0.02

Dictionary

35

184.1 us

1.51 us

1.34 us

0.001

0.00

MutableMap

35

2,445.8 us

9.90 us

8.27 us

0.013

0.00

MapState

35

2,499.5 us

11.08 us

9.82 us

0.014

0.00

To no surprise, the implementation without caching is the slowest of them all. The fastest caching implementation is the one using the mutable dictionary. The two using the immutable map are pretty close to each other.

You can find the full source code for all four implementations in [my GitHub repository](https://github.com/DamirsCorner/20250110-fs-memoization). You can use it to run the benchmarks yourself or as a basis for solving the said Advent of Code puzzle if you're still working on it.

F# is a functional-first language, but it's not a pure functional language so it also has support for mutable variables and mutable data structures. Both can come in handy in certain use case, such as implementing memoization.
