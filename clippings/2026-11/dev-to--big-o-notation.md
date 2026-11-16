---
url: "https://dev.to/adafia/big-o-notation-3oi6"
captured_at: "2026-11-16T00:59:38+00:00"
title: "Big O Notation"
domain: "dev-to"
---

Almost all coding challenges have multiple approaches to solving them. Though all the different approaches get the job done, it is possible to rank them according to performance and efficiency. A standard system used by engineers to achieve this is the **Big O Notation**.

## [](#table-of-contents)Table Of Contents

*   [What is Big O Notation?](#obj-2)
*   [Time and space complexity](#obj-3)
    *   [Time Complexity](#obj-3-1)
    *   [Space Complexity](#obj-3-2)
*   [Brief introduction to Logarithms](#obj-4)
*   [Conclusion](#obj-5)

### [](#what-is-big-o-notation)What is Big O Notation?

Big O Notation is a way of classifying algorithms by assigning mathematical expressions based on the algorithm's runtime (time complexity) and memory/space requirement (space complexity).

###### [](#benefits)Benefits

Big O Notation is important because

*   It provides a precise vocabulary or terminology in talking about the performance of algorithms.
*   It is useful for discussing trade-offs between different approaches employed in algorithm design.
*   It helps in debugging code and figuring out reasons for slow performance, crashes, identifying parts of the code that are inefficient and identifying pain points.

### [](#time-and-space-complexity)Time and space complexity

In this section, I'll be attempting to explain the basic concepts of Big O Notation by analysing and classifying two valid solutions to a simple code challenge.

###### [](#question-1)Question 1

Write a function that calculates the sum of all numbers from 1 up to and including a given number n.

###### [](#solution-1)Solution 1

```
1. function addUpto(n) {
2.   return n * (n + 1) / 2;
3. }
```

Enter fullscreen mode Exit fullscreen mode

###### [](#solution-2)Solution 2

```
1. function addUpto(n) {
2.   let total = 0;
3.   for (let i = 1; i <= n; i++) {
4.     total += i;
5.   }
6.   return total;
7. }
```

Enter fullscreen mode Exit fullscreen mode

Which of the above solutions is better?

##### [](#discussion)Discussion

Before we answer the above question, we would have to define what _better_ means.

*   Does better mean faster?
*   Does better mean less memory-intensive (the data that is stored in memory each time the function is called)?

#### [](#time-complexity)Time Complexity

##### [](#lets-take-the-first-question-does-better-mean-faster)Let's take the first question _" Does better mean faster?"_

In thinking of the speed of algorithms, it may seem intuitive to record the time it takes for an algorithm to complete its task but doing that will lead to inconsistencies. This is because computers vary in hardware and computing power. A computer with a lot more resources will take a shorter period to complete a given algorithm than a computer with fewer resources.

So instead of counting seconds, which change based on computing power, consistent and standardized results can be achieved by counting **the number of simple operations the computer has to perform within an algorithm**. The time it takes for a computer to execute an algorithm is directly proportional to the number of operations it has to perform. Hence the greater the number of operations the longer it takes to execute.

Now that we have established the criteria for analysing an algorithm's runtime, let's count the number of simple operations in our solutions

###### [](#solution-1)Solution 1

```
1. function addUpto(n) {
2.   return n * (n + 1) / 2;
3. }
```

Enter fullscreen mode Exit fullscreen mode

Solution 1 has a total of three (3) simple operations.

*   one multiplication `n * ...`
*   one addition `n + 1` and
*   one division `... / 2` The number of operations in _solution 1_ does not change with increasing or decreasing the magnitude of the input(_n_). No matter how small or large _n_ is, the number of operations will always be 3.

###### [](#solution-2)Solution 2

```
1. function addUpto(n) {
2.   let total = 0;
3.   for (let i = 1; i <= n; i++) {
4.     total += i;
5.   }
6.   return total;
8. }
```

Enter fullscreen mode Exit fullscreen mode

In _solution 2_

*   line 2 shows 1 variable assignment `let total = 0;`
*   line 3 shows:
    *   1 variable assignment `let i = 1;`,
    *   _n_ comparisons `i <= n;`,
    *   _n_ additions and _n_ variable assignments `i++`.
*   line 4 shows _n_ additions and _n_ variable assignments.

It also makes use of a loop which runs _n_ times. Thus, if _n_ is 5, the loop will run five times. However, depending on what you count, the number of operations can be as low as `2n` or as high as `5n + 2`. Hence regardless of being precise, the number of operations grows roughly proportionally with _n_.

Consequently, unlike _solution 1_, counting the number of operations in _solution 2_ is a lot more complicated. Big O Notation doesn't necessarily care about precision only about general trends.

Based on the above, **_"time complexity with respect to big O notation is the measure of how the runtime of an algorithm grows as its input grows."_**

The various terminology available via Big O notation in classifying the _runtime / time complexity_ of algorithms includes the following.

##### [](#constant-o1)Constant O(1)

An algorithm with a _constant_ time complexity does not have its runtime significantly affected by an increase or decrease in the magnitude of its input(_n_). As the value of the input(n) grows the runtime of the algorithm fundamentally stays constant.

##### [](#linear-on)Linear O(n)

An algorithm is described as having a linear time complexity when its runtime scales proportionally with its input(_n_).

##### [](#quadratic-on2)Quadratic O(n^2)

An algorithm with a quadratic time complexity has its runtime scaling at a rate which is approximately the square of its input(_n_). Thus, as the value of _n_ increases the runtime of the algorithm increases by _n^2_.

###### [](#solution-1)Solution 1

```
1. function addUpto(n) {
2.   return n * (n + 1) / 2;
3. }
```

Enter fullscreen mode Exit fullscreen mode

> So the Big O of _solution 1_ is `O(1)` (_read as O of 1_). This means that the number of simple operations the computer has to do is constant as _n_ increases.

###### [](#solution-2)Solution 2

```
1. function addUpto(n) {
2.   let total = 0;
3.   for (let i = 1; i <= n; i++) {
4.     total += i;
5.   }
6.   return total;
8. }
```

Enter fullscreen mode Exit fullscreen mode

> _Solution 2_ has a big O of `O(n)` (_read as O of n_). This means that the number of operations is bound by a multiple of its input(_n_).

#### [](#space-complexity)Space Complexity

Space complexity is usually concerned with the amount of memory needed to run a given algorithm.

> Auxiliary space complexity: space/memory required by the algorithm without considering the space taken by the inputs.

For the scope of this blog post, space complexity refers to auxiliary space complexity.

### [](#helpful-tips-when-thinking-about-space-complexity)Helpful tips when thinking about space complexity

*   Most primitives (booleans, numbers, undefined, null) are constant space `O(1)`.
*   Strings require `O(n)` space (where _n_ is the length of the string).
*   Reference types are generally `O(n)`, where _n_ is the length of the array or the number of keys in the case of objects.

```
1. function sum(arr) {
2.   let total = 0;
3.   for (let i = 0; i < arr.length; i++) {
4.      total += arr[i];
5.   }
6.   return total;
7.  }
```

Enter fullscreen mode Exit fullscreen mode

The above function adds all numerical elements of a given array and returns the total.  
Since we are only concerned about the memory/space required by the function/algorithm alone, we are going to disregard the length of the array provided to the function. So the only space-consuming elements we are concerned about are on line 2 and 3.

*   On line 2 and 3, no matter the size/length of the array provided to the function/algorithm, it going consume the space of a single digit (0). line 2 => `let total = 0`. and line 3 => `let i = 0`

> So the big O of the _sum_ function with respect to auxiliary space complexity is `O(1)`.  

```
1. function double(arr) {
2.   let newArr = [];
3.   for (let i = 0; i < arr.length; i++) {
4.      newArr.push(2 * arr[i]);
5.   }
6.   return newArr;
7.  }
```

Enter fullscreen mode Exit fullscreen mode

The function _double_ takes in an array of numbers and returns a new array with each element of the input array doubled.

One thing to note is that an empty array is instantiated and based on the length of the input array, the memory required by the instantiated array increases proportionally on line 4. So the space complexity of the _double_ function is `O(n)`.

#### [](#brief-introduction-to-logarithms)Brief introduction to Logarithms

Although some of the common algorithms can be classified under constant `O(1)`, linear `O(n)` and quadratic `O(n^2)` space and time complexities, there are a lot of algorithms that are not adequately described by the above. These involve more complex mathematical expressions such as logarithms.

Logarithms are the inverse of exponentiation. Just as division and multiplication are a pair, exponentiation and logarithms are a pair.

Logarithmic space and time complexities are expressed with `O(log n)` and `O(nlog n)`

### [](#conclusion)Conclusion

To sum this all up, here are few things to remember about Big O Notation.

*   To analyze the performance of an algorithm, we use Big O Notation
*   Big O Notation can provide us with a high-level understanding of the time or space complexity of an algorithm.
*   Big O Notation doesn't necessarily care about precision only about general trends (linear, quadratic or constants)
*   The time or space complexity (as measured by Big O) depends only on the algorithm, and not the hardware used to run the algorithm.

Cover image by [Jeremy Perkins on Unsplash](https://unsplash.com/@jeremyperkins)
