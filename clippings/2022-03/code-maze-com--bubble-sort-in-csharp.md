---
url: "https://code-maze.com/csharp-bubble-sort/"
captured_at: "2022-03-27T18:58:03-03:00"
title: "Bubble Sort In C# - Code Maze"
domain: "code-maze-com"
---

# Bubble Sort In C#

Posted by [Code Maze](https://code-maze.com/author/codemazecontributor/ "Posts by Code Maze") | Updated Date Mar 5, 2022 | [0](https://code-maze.com/csharp-bubble-sort/#comments)

Sorting arrays is quite a common problem in programming. The bubble sort algorithm is simple to implement as it involves comparing adjacent elements and swapping them when they are in the wrong order. We are going to learn how Bubble Sort in C# works.

To download the source code for this article, you can visit our [GitHub repository](https://github.com/CodeMazeBlog/CodeMazeGuides/tree/main/csharp-algorithms/BubbleSort).

Let’s dive in.

## What is Bubble Sort Algorithm?

So, how does bubble sort in C# work?

Let’s say we want to sort an array that has seven elements:

int[] array = {73, 57, 49, 99, 133, 20, 1};

Using the bubble sort algorithm, let’s start by comparing 73 and 57. 57 is less than 73, so we swap their positions and the array becomes:

`57, 73, 49, 99, 133, 20, 1`

49 is less than 73, which triggers the algorithm to swap their positions:

`57, 49, 73, 99, 133, 20, 1`

73 is less than 99 while 99 is less than 133, so the algorithm skips these positions. Next, we compare 133 with 20 and swap their positions as 20 is less than 133:

`57, 49, 73, 99, 20, 133, 1`

Since 1 is less than 33, the algorithm swaps their positions:

`57, 49, 73, 99, 20, 1, 133`

The bubble sort algorithm repeats this process until all the elements are in the correct order with the final result being:

`1, 20, 49, 57, 73, 99, 133`

## How to Implement Bubble Sort in C#?

We are going to define an integer array property `NumArray`, that we are going to use to implement the bubble sort algorithm:

publicint[]? NumArray {get; set; }

Let’s create a method that implements the bubble sort algorithm in C# that sorts the values in the `NumArray` property:

publicint[]SortArray()

{

var n = NumArray.Length;

for(int i = 0; i < n - 1; i++)

for(int j = 0; j < n - i - 1; j++)

if(NumArray[j]> NumArray[j + 1])

{

var tempVar = NumArray[j];

NumArray[j] = NumArray[j + 1];

NumArray[j + 1] = tempVar;

}

return NumArray;

}

```
public int[] SortArray() 
{
    var n = NumArray.Length;

    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (NumArray[j] > NumArray[j + 1])
            {
                var tempVar = NumArray[j];
                NumArray[j] = NumArray[j + 1];
                NumArray[j + 1] = tempVar;
            }

    return NumArray;
}
```

The variable `n` holds the size of the array while the `tempVar` variable holds values temporarily during the swap process. Let’s use our array example to understand how the code works:

The outer loop iterates through the array while the inner loop compares adjacent elements. Since 57 is less than 73, they swap their positions and the inner loop continues comparing adjacent values until it gets to the last element of that array. For each iteration of the outer loop, the inner loop iterates while performing comparisons.

Let’s check if our loop performed correctly:

var array = newint[]{73, 57, 49, 99, 133, 20, 1};

var expected = newint[]{1, 20, 49, 57, 73, 99, 133};

var sortFunction = newBubble();

sortFunction.NumArray = array;

var sortedArray = sortFunction.SortArray();

Assert.IsNotNull(sortedArray);

CollectionAssert.AreEqual(sortedArray, expected);

```
var array = new int[] { 73, 57, 49, 99, 133, 20, 1 };
var expected = new int[] { 1, 20, 49, 57, 73, 99, 133 };
var sortFunction = new Bubble();
sortFunction.NumArray = array;

var sortedArray = sortFunction.SortArray();

Assert.IsNotNull(sortedArray);
CollectionAssert.AreEqual(sortedArray, expected);
```

## Time and Space Complexity

The space complexity of the bubble sort algorithm is O(1) because it requires a single additional space that holds the temporary value we are using to swap the elements.

Nested loops have detrimental effects on how algorithms perform as the size of the array grows. The bubble sort algorithm has a time complexity of O(N²) as it has two nested loops. Let’s analyze how the algorithm performs in different levels of complexity.

**Best Case Complexity:** this case occurs when we want to sort an array that is already in required order. The algorithm traverses the array without swapping values, which means, its complexity is O(N).

**Average Case Complexity:** this case occurs when an array has some elements that are in the correct order. The bubble sort algorithm performs comparisons while swapping some values, which means, it has a complexity of O(N²).

**Worst Case Complexity:** this scenario occurs when assuming we have a list of numbers that are in descending order and we need to sort them in ascending order, the algorithm would encounter a worst-case complexity as the length of that array grows to N. Therefore, the algorithm compares all elements while swapping them, which means, it has a complexity of O(N²).

## Advantages and Disadvantages

The bubble sort algorithm is easy to learn and implement. On top of that, it has little memory overhead as the sorting is done in place, which is similar to [selection sort](https://code-maze.com/csharp-selection-sort/). This attribute comes in handy in memory-intensive applications. This algorithm **performs well in cases where an array is almost in order as it is an example of the** [best case complexity](https://code-maze.com/csharp-bubble-sort/#algorithm-complexity) **scenario**.

On the other hand, the bubble sort algorithm **has high levels of time complexity O(N²), which is inefficient when compared to other algorithms** such as merge sort.

## How to Optimize the Bubble Sort Algorithm in C#?

We can see that the bubble sort algorithm still iterates even in cases where an array is already in order. We can optimize the swapping process by checking whether we need to swap elements or not. Let’s optimize our previous implementation and see what’s different about it:

publicint[]SortOptimizedArray()

{

var n = NumArray.Length;

bool swapRequired;

for(int i = 0; i < n - 1; i++)

{

swapRequired = false;

for(int j = 0; j < n - i - 1; j++)

if(NumArray[j]> NumArray[j + 1])

{

var tempVar = NumArray[j];

NumArray[j] = NumArray[j + 1];

NumArray[j + 1] = tempVar;

swapRequired = true;

}

if(swapRequired == false)

break;

}

return NumArray;

}

```
public int[] SortOptimizedArray()
{
    var n = NumArray.Length;
    bool swapRequired;

    for (int i = 0; i < n - 1; i++) 
    {
        swapRequired = false;

        for (int j = 0; j < n - i - 1; j++)
            if (NumArray[j] > NumArray[j + 1])
            {
                var tempVar = NumArray[j];
                NumArray[j] = NumArray[j + 1];
                NumArray[j + 1] = tempVar;
                swapRequired = true;
            }
        if (swapRequired == false)
            break;
    }

    return NumArray;
}
```

We introduce a boolean value `swapRequired` to track whether we need to swap the elements or not. The `swapRequired` variable becomes true when we swap elements, otherwise, it’s set to false. In iterations where swapping is not required, the `swapRequired` will be false, which means, the array elements are in order and we break the loop before it finishes to the end.  This way we save a lot of time.

Let’s check if our optimal bubble sort algorithm performs correctly:

var array = newint[]{73, 57, 49, 99, 133, 20, 1};

var expected = newint[]{1, 20, 49, 57, 73, 99, 133};

var sortFunction = newBubble();

sortFunction.NumArray = array;

var sortedArray = sortFunction.SortOptimizedArray();

Assert.IsNotNull(sortedArray);

CollectionAssert.AreEqual(sortedArray, expected);

```
var array = new int[] { 73, 57, 49, 99, 133, 20, 1 };
var expected = new int[] { 1, 20, 49, 57, 73, 99, 133 };
var sortFunction = new Bubble();

sortFunction.NumArray = array;
var sortedArray = sortFunction.SortOptimizedArray();

Assert.IsNotNull(sortedArray);
CollectionAssert.AreEqual(sortedArray, expected);
```

## Bubble Sort Performance

Let’s verify the bubble sort algorithm has a time complexity of O(N²) by measuring the time it takes for the algorithm to sort an array.

First, let’s write a method to generate a set of random numbers that are going to be added into the array:

publicstaticint[]GenerateRandomNumber(int size)

{

var array = newint[size];

var rand = newRandom();

var maxNum = 10000;

for(int i = 0; i < size; i++)

array[i] = rand.Next(maxNum + 1);

return array;

}

```
public static int[] GenerateRandomNumber(int size)
{
    var array = new int[size];
    var rand = new Random();
    var maxNum = 10000;

    for (int i = 0; i < size; i++)
        array[i] = rand.Next(maxNum + 1);

    return array;
}
```

The `GenerateRandomNumber` method takes an integer as its sole input. Using the inbuilt `Random` class, we generate integer values (less than 10000) that we’re going to put into the array.

To simulate a scenario where we have a sorted array, we are going to define a method that generates a sequence of elements:

publicstaticint[]GenerateSortedNumber(int size)

{

var array = newint[size];

for(int i = 0; i < size; i++)

array[i] = i;

return array;

}

```
public static int[] GenerateSortedNumber(int size)
{
    var array = new int[size];

    for (int i = 0; i < size; i++)
        array[i] = i;

    return array;
}
```

Next, we are going to implement a performance benchmark to assess how the normal bubble sort algorithm performs versus the optimized bubble sort algorithm when sorting randomly generated numbers:

int[] smallArray = GenerateRandomNumber(200);

int[] mediumArray = GenerateRandomNumber(2000);

int[] largeArray = GenerateRandomNumber(200000);

```
int[] smallArray = GenerateRandomNumber(200);
int[] mediumArray = GenerateRandomNumber(2000);
int[] largeArray = GenerateRandomNumber(200000);
```

The array objects have different sizes (to simulate time complexity scenarios) and hold [random numbers](https://code-maze.com/csharp-generate-random-numbers-range/) that are added by the `GenerateRandomNumber` method. Let’s assess the sample best, average, and worst-case complexity performance results of the algorithm:

| Method | NumArray | Mean | Error | StdDev |

|------------------- |-------------- |--------------------:|------------------:|--------------------:|

| SortArray | Int32[200000] | 34,217,602,373.3 ns | 680,856,233.76 ns | 1,852,319,597.83 ns |

| SortOptimizedArray | Int32[200000] | 404,684.5 ns | 22,163.41 ns | 64,300.07 ns |

| SortArray | Int32[2000] | 3,188,246.8 ns | 32,947.14 ns | 30,818.77 ns |

| SortOptimizedArray | Int32[2000] | 3,191.4 ns | 23.51 ns | 21.99 ns |

| SortArray | Int32[200] | 32,333.2 ns | 512.23 ns | 766.68 ns |

| SortOptimizedArray | Int32[200] | 323.9 ns | 6.34 ns | 6.51 ns |

```
|             Method |      NumArray |                Mean |             Error |              StdDev |
|------------------- |-------------- |--------------------:|------------------:|--------------------:|
|          SortArray | Int32[200000] | 34,217,602,373.3 ns | 680,856,233.76 ns | 1,852,319,597.83 ns |
| SortOptimizedArray | Int32[200000] |        404,684.5 ns |      22,163.41 ns |        64,300.07 ns | 
|          SortArray |   Int32[2000] |      3,188,246.8 ns |      32,947.14 ns |        30,818.77 ns |
| SortOptimizedArray |   Int32[2000] |          3,191.4 ns |          23.51 ns |            21.99 ns | 
|          SortArray |    Int32[200] |         32,333.2 ns |         512.23 ns |           766.68 ns |
| SortOptimizedArray |    Int32[200] |            323.9 ns |           6.34 ns |             6.51 ns |
```

The worst-case execution demonstrates this concept as the `SortArray` method takes approximately 34,217,602,373.3 ns (~34.21 seconds) to run while the `SortOptimizedArray` method takes 404,684.5 ns (~0.000404 seconds) which is a huge difference.

Next, are going to re-run the same benchmark but with the arrays holding values that have already been sorted invoking the `GenerateSortedNumber` method. These are the array objects we are going to use for the next benchmark run:

int[] sortedSmallArray = GenerateSortedNumber(200);

int[] sortedMediumArray = GenerateSortedNumber(2000);

int[] sortedLargeArray = GenerateSortedNumber(200000);

```
int[] sortedSmallArray = GenerateSortedNumber(200);
int[] sortedMediumArray = GenerateSortedNumber(2000);
int[] sortedLargeArray = GenerateSortedNumber(200000);
```

And let’s assess the results of this benchmark:

| Method | NumArray | Mean | Error | StdDev |

|------------------- |-------------- |--------------------:|------------------:|--------------------:|

| SortArray | Int32[200000] | 33,916,006,053.2 ns | 654,826,121.87 ns | 1,277,188,059.76 ns |

| SortOptimizedArray | Int32[200000] | 320,074.5 ns | 6,279.92 ns | 10,663.78 ns |

| SortArray | Int32[2000] | 3,122,602.4 ns | 16,882.03 ns | 15,791.46 ns |

| SortOptimizedArray | Int32[2000] | 3,112.0 ns | 18.00 ns | 15.95 ns |

| SortArray | Int32[200] | 34,262.8 ns | 1,023.35 ns | 2,919.67 ns |

| SortOptimizedArray | Int32[200] | 315.0 ns | 3.85 ns | 3.22 ns |

```
|             Method |      NumArray |                Mean |             Error |              StdDev |
|------------------- |-------------- |--------------------:|------------------:|--------------------:|
|          SortArray | Int32[200000] | 33,916,006,053.2 ns | 654,826,121.87 ns | 1,277,188,059.76 ns |
| SortOptimizedArray | Int32[200000] |        320,074.5 ns |       6,279.92 ns |        10,663.78 ns |
|          SortArray |   Int32[2000] |      3,122,602.4 ns |      16,882.03 ns |        15,791.46 ns |
| SortOptimizedArray |   Int32[2000] |          3,112.0 ns |          18.00 ns |            15.95 ns |
|          SortArray |    Int32[200] |         34,262.8 ns |       1,023.35 ns |         2,919.67 ns |
| SortOptimizedArray |    Int32[200] |            315.0 ns |           3.85 ns |             3.22 ns |
```

The optimized bubble sort algorithm implementation is faster than the normal version of the bubble sort algorithm in all case scenarios. We can also see that the time complexity of this algorithm worsens exponentially as the number of elements increases.

We can also see that the algorithm takes less time for an array that is already in order from the second benchmark which means that the complexity is lower. This would be even more emphasized with the larger arrays.

## Conclusion

In this article, we’ve learned how the bubble sort in C# works and how to implement it. It is simple to implement but not that efficient when compared to other algorithms. In case you want to learn how to implement another sorting algorithm, check out this [selection sort](https://code-maze.com/csharp-selection-sort/) article.

[![ultimate-aspnet-core-banner-v2-690-min.webp](code-maze-com--bubble-sort-in-csharp/0397bd8791f4321ba0b87cd78ca7c4fe.webp)](https://code-maze.com/ultimate-aspnetcore-webapi-second-edition?source=bbanner&p=csharp-bubble-sort)

Want to build **great APIs?** Or become **even better** at it? Check our program **[Ultimate ASP.NET Core Web API](https://code-maze.com/ultimate-aspnetcore-webapi-second-edition?source=bbanner&p=csharp-bubble-sort)** and learn how to create a full production-ready ASP.NET Core API using only the **latest .NET technologies**. Bonus materials included!
