---
url: "https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript"
captured_at: "2026-11-16T19:58:45+00:00"
title: "GitHub - amejiarosario/dsa.js-data-structures-algorithms-javascript: 🥞Data Structures and Algorithms explained and implemented in JavaScript + eBook"
domain: "github-com"
---

[![image](https://user-images.githubusercontent.com/418605/59557258-10742880-8fa3-11e9-84fb-4d66a9d89faa.png)](https://user-images.githubusercontent.com/418605/59557258-10742880-8fa3-11e9-84fb-4d66a9d89faa.png)

[![CircleCI](https://camo.githubusercontent.com/34f786afd211f3c694ad0dd71e31d534beae5f0602524825111200005b15ce4c/68747470733a2f2f636972636c6563692e636f6d2f67682f616d656a6961726f736172696f2f6473612e6a732d646174612d737472756374757265732d616c676f726974686d732d6a6176617363726970742e7376673f7374796c653d736869656c64)](https://app.circleci.com/pipelines/github/amejiarosario/dsa.js-data-structures-algorithms-javascript) [![NPM version](https://camo.githubusercontent.com/41bf02204ef000f839659d94ad677ad46116404a9002fa7c31521a49c4cb9fd1/68747470733a2f2f62616467652e667572792e696f2f6a732f6473612e6a732e737667)](https://badge.fury.io/js/dsa.js) [![chat](https://camo.githubusercontent.com/a4791d097673b482d5fc9d074ccdd459acbb09e20de58fa74fdd0f4afdc64c04/68747470733a2f2f6473616a732d736c61636b696e2e6865726f6b756170702e636f6d2f62616467652e737667)](https://dsajs-slackin.herokuapp.com/)

> This is the coding implementations of the [DSA.js book](https://books.adrianmejia.com/dsajs-data-structures-algorithms-javascript/) and the repo for the NPM package.

> In this repository, you can find the implementation of algorithms and data structures in JavaScript. This material can be used as a reference manual for developers, or you can refresh specific topics before an interview. Also, you can find ideas to solve problems more efficiently.

[![Interactive Data Structures](https://user-images.githubusercontent.com/418605/46118890-ba721180-c1d6-11e8-82bc-6a671428b422.png)](https://user-images.githubusercontent.com/418605/46118890-ba721180-c1d6-11e8-82bc-6a671428b422.png)

## Table of Contents

[](#table-of-contents)

*   [Installation](#installation)
*   [Features](#features)
*   [What's Inside](#whats-inside)
    *   [📈 Algorithms Analysis](#-algorithms-analysis)
    *   [🥞 Linear Data Structures](#-linear-data-structures)
    *   [🌲 Non-Linear Data Structures](#-non-linear-data-structures)
    *   [⚒ Algorithms Techniques](#%E2%9A%92-algorithms-techniques)
*   [Book](#book)
*   [FAQ](#faq)
*   [Support](#support)
*   [License](#license)

## Installation

[](#installation)

You can clone the repo or install the code from NPM:

npm install dsa.js

and then you can import it into your programs or CLI

const { LinkedList, Queue, Stack } \= require('dsa.js');

For a list of all available data structures and algorithms, [see index.js](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/index.js).

## Features

[](#features)

Algorithms are an essential toolbox for every programmer.

You will need to mind algorithms runtime when you have to sort data, search for a value in a big dataset, transform data, scale your code to many users, to name a few. Algorithms are just the step you follow to solve a problem, while data structures are where you store the data for later manipulation. Both combined create programs.

> Algorithms + Data Structures = Programs.

Most programming languages and libraries indeed provide implementations for basic data structures and algorithms. However, to make use of data structures properly, you have to know the tradeoffs to choose the best tool for the job.

This material is going to teach you to:

*   🛠 Apply strategies to tackle algorithm questions. Never to get stuck again. Ace those interviews!
*   ✂️ Construct efficient algorithms. Learn how to break down problems into manageable pieces.
*   🧠 Improve your problem-solving skills and become a well-rounded developer by understanding fundamental computer science concepts.
*   🤓 Cover essential topics, such as big O time, data structures, and must-know algorithms. Implement 10+ data structures from scratch.

## What's Inside

[](#whats-inside)

All the code and explanations are available on this repo. You can dig through the links and code examples from the ([src folder](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src)). However, the inline code examples are not expanded (because of Github's asciidoc limitations), but you can follow the path and see the implementation.

_Note: If you prefer to consume the information more linearly, then the [book format](https://books.adrianmejia.com/dsajs-data-structures-algorithms-javascript/) would be more appropriate for you._

The topics are divided into four main categories, as you can see below:

### 📈 [Algorithms Analysis](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/part01-algorithms-analysis.asc)

[](#-algorithms-analysis)

> Computer Science nuggets without all the mumbo-jumbo. _(Click to expand)_
> 
> * * *
> 
> ### [Computer Science nuggets without all the mumbo-jumbo](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part01/algorithms-analysis.asc)
> 
> [](#computer-science-nuggets-without-all-the-mumbo-jumbo)
> 
> #### Learn to calculate run time from code examples
> 
> [](#learn-to-calculate-run-time-from-code-examples)
> 
> [![Translating lines of code to an approximate number of operations](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/raw/master/book/images/image4.png)](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/images/image4.png)
> 
> * * *
> 
> Learn how to compare algorithms using Big O notation. _(Click to expand)_
> 
> * * *
> 
> ### [Learn how to compare algorithms using Big O notation.](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part01/big-o-examples.asc#finding-if-an-array-is-empty)
> 
> [](#learn-how-to-compare-algorithms-using-big-o-notation)
> 
> #### Comparing algorithms using Big O notation
> 
> [](#comparing-algorithms-using-big-o-notation)
> 
> Let's say you want to find the duplicates on an array. Using Big O notation, we can compare different solutions that solve the same problem but has a massive difference in how long it takes to do it.
> 
> *   [Optimal solution using a map](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part01/big-o-examples.asc#linear-example)
> *   [Finding duplicates in an array (naïve approach)](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part01/big-o-examples.asc#quadratic-example)
> 
> * * *
> 
> 8 examples to explain with code how to calculate time complexity. _(Click to expand)_
> 
> * * *
> 
> [8 examples to explain with code how to calculate time complexity](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part01/big-o-examples.asc#summary)
> 
> #### Most common time complexities
> 
> [](#most-common-time-complexities)
> 
> [![image](https://user-images.githubusercontent.com/418605/59617342-2a715080-90f4-11e9-9de9-9315fb0133f9.png)](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part01/big-o-examples.asc#summary)
> 
> #### Time complexity graph
> 
> [](#time-complexity-graph)
> 
> [![Most common time complexities](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/raw/master/book/images/image5.png)](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/images/image5.png)
> 
> * * *

### 🥞 [Linear Data Structures](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/part02-linear-data-structures.asc)

[](#-linear-data-structures)

> Understand the ins and outs of the most common data structures. _(Click to expand)_
> 
> * * *
> 
> #### [Understand the ins and outs of the most common data structures](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/part02-linear-data-structures.asc)
> 
> [](#understand-the-ins-and-outs-of-the-most-common-data-structures)
> 
> *   [Arrays](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part02/array.asc): Built-in in most languages so not implemented here. [Array Time complexity](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part02/array.asc#array-complexity)
>     
> *   [Linked List](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part02/linked-list.asc): each data node has a link to the next (and previous). [Code](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/data-structures/linked-lists/linked-list.js) | [Linked List Time Complexity](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part02/linked-list.asc#linked-list-complexity-vs-array-complexity)
>     
> *   [Queue](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part02/queue.asc): data flows in a "first-in, first-out" (FIFO) manner. [Code](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/data-structures/queues/queue.js) | [Queue Time Complexity](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part02/queue.asc#queue-complexity)
>     
> *   [Stack](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part02/stack.asc): data flows in a "last-in, first-out" (LIFO) manner. [Code](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/data-structures/stacks/stack.js) | [Stack Time Complexity](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part02/stack.asc#stack-complexity)
>     
> 
> * * *
> 
> When to use an Array or Linked List. Know the tradeoffs. _(Click to expand)_
> 
> * * *
> 
> #### [When to use an Array or Linked List. Know the tradeoffs](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part02/array-vs-list-vs-queue-vs-stack.asc)
> 
> [](#when-to-use-an-array-or-linked-list-know-the-tradeoffs)
> 
> Use Arrays when…
> 
> *   You need to access data in random order fast (using an index).
> *   Your data is multi-dimensional (e.g., matrix, tensor).
> 
> Use Linked Lists when:
> 
> *   You will access your data sequentially.
> *   You want to save memory and only allocate memory as you need it.
> *   You want constant time to remove/add from extremes of the list.
> *   when size requirement is unknown - dynamic size advantage
> 
> * * *
> 
> Build a List, Stack, and a Queue. _(Click to expand)_
> 
> * * *
> 
> #### [Build a List, Stack and a Queue from scratch](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/part02-linear-data-structures.asc)
> 
> [](#build-a-list-stack-and-a-queue-from-scratch)
> 
> Build any of these data structures from scratch:
> 
> *   [Linked List](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/data-structures/linked-lists/linked-list.js)
> *   [Stack](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/data-structures/stacks/stack.js)
> *   [Queue](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/data-structures/queues/queue.js)
> 
> * * *

### 🌲 [Non-Linear Data Structures](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/part03-graph-data-structures.asc)

[](#-non-linear-data-structures)

> Understand one of the most versatile data structure of all: Hash Maps. _(Click to expand)_
> 
> * * *
> 
> #### [HashMaps](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part03/map.asc)
> 
> [](#hashmaps)
> 
> Learn how to implement different types of Maps such as:
> 
> *   [HashMap](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part02/hash-map.asc)
> *   [TreeMap](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part03/tree-map.asc)
> 
> Also, [learn the difference between the different Maps implementations](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part03/time-complexity-graph-data-structures.asc):
> 
> *   `HashMap` is more time-efficient. A `TreeMap` is more space-efficient.
> *   `TreeMap` search complexity is _O(log n)_, while an optimized `HashMap` is _O(1)_ on average.
> *   `HashMap`’s keys are in insertion order (or random depending on the implementation). `TreeMap`’s keys are always sorted.
> *   `TreeMap` offers some statistical data for free such as: get minimum, get maximum, median, find ranges of keys. `HashMap` doesn’t.
> *   `TreeMap` has a guarantee always an _O(log n)_, while `HashMap`s has an amortized time of _O(1)_ but in the rare case of a rehash, it would take an _O(n)_.
> 
> * * *
> 
> Know the properties of Graphs and Trees. _(Click to expand)_
> 
> * * *
> 
> #### [Know the properties of Graphs and Trees](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/part03-graph-data-structures.asc)
> 
> [](#know-the-properties-of-graphs-and-trees)
> 
> ##### [Graphs](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part03/graph.asc)
> 
> [](#graphs)
> 
> Know all the graphs properties with many images and illustrations.
> 
> [![graph example with USA airports](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/raw/master/book/images/image46.png)](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/images/image46.png)
> 
> **Graphs**: data **nodes** that can have a connection or **edge** to zero or more adjacent nodes. Unlike trees, nodes can have multiple parents, loops. [Code](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/data-structures/graphs/graph.js) | [Graph Time Complexity](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part03/graph.asc#graph-complexity)
> 
> #### [Trees](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part03/tree-intro.asc)
> 
> [](#trees)
> 
> Learn all the different kinds of trees and their properties.
> 
> [![tree data structure properties](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/raw/master/book/images/image31.jpg)](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/images/image31.jpg)
> 
> *   **Trees**: data nodes has zero or more adjacent nodes a.k.a. children. Each node can only have one parent node otherwise is a graph, not a tree. [Code](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/data-structures/trees) | [Docs](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part03/tree-intro.asc)
>     
>     *   **Binary Trees**: same as a tree but only can have two children at most. [Code](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/data-structures/trees) | [Docs](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part03/tree-intro.asc#binary-tree)
>         
>     *   **Binary Search Trees** (BST): same as a binary tree, but the nodes value keep this order `left < parent < right`. [Code](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/data-structures/trees/binary-search-tree.js) | [BST Time complexity](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part03/binary-search-tree.asc#tree-complexity)
>         
>     *   **AVL Trees**: Self-balanced BST to maximize lookup time. [Code](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/data-structures/trees/avl-tree.js) | [AVL Tree docs](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/C-AVL-tree.asc) | [Self-balancing & tree rotations docs](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/B-self-balancing-binary-search-trees.asc)
>         
>     *   **Red-Black Trees**: Self-balanced BST looser than AVL to maximize insertion speed. [Code](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/data-structures/trees/red-black-tree.js)
>         
> 
> * * *
> 
> Implement a binary search tree for fast lookups.
> 
> * * *
> 
> #### [Implement a binary search tree for fast lookups](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part03/binary-search-tree.asc)
> 
> [](#implement-a-binary-search-tree-for-fast-lookups)
> 
> *   Learn how to add/remove/update values in a tree: [![inserting node in a tree](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/raw/master/book/images/image36.png)](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/images/image36.png)
>     
> *   [How to make a tree balanced?](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/B-self-balancing-binary-search-trees.asc)
>     
> 
> From unbalanced BST to balanced BST
> 
> ```
> 1                           2
>   \                       /   \
>    2        =>           1     3
>     \
>      3
> ```
> 
> * * *

### ⚒ [Algorithmic Toolbox](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/part04-algorithmic-toolbox.asc)

[](#-algorithmic-toolbox)

> Never get stuck solving a problem with 7 simple steps. _(Click to expand)_
> 
> * * *
> 
> #### [Never get stuck solving a problem with 8 simple steps](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/part04-algorithmic-toolbox.asc)
> 
> [](#never-get-stuck-solving-a-problem-with-8-simple-steps)
> 
> 1.  Understand the problem
> 2.  Build a simple example (no edge cases yet)
> 3.  Brainstorm solutions (greedy algorithm, Divide and Conquer, Backtracking, brute force)
> 4.  Test your answer on the simple example (mentally)
> 5.  Optimize the solution
> 6.  Write code. Yes, now you can code.
> 7.  Test your written code
> 8.  Analyse the complexity, both space and time, and make sure to optimize further.
> 
> Full details [here](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/part04-algorithmic-toolbox.asc)
> 
> * * *
> 
> Master the most popular sorting algorithms (merge sort, quicksort, etc.) _(Click to expand)_
> 
> * * *
> 
> #### [Master the most popular sorting algorithms](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part04/sorting-algorithms.asc)
> 
> [](#master-the-most-popular-sorting-algorithms)
> 
> We are going to explore three essential sorting algorithms O(n^2), which have low overhead:
> 
> *   Bubble Sort. [Code](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/algorithms/sorting/bubble-sort.js) | [Docs](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part04/bubble-sort.asc)
>     
> *   Insertion Sort. [Code](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/algorithms/sorting/insertion-sort.js) | [Docs](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part04/insertion-sort.asc)
>     
> *   Selection Sort. [Code](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/algorithms/sorting/selection-sort.js) | [Docs](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part04/selection-sort.asc)
>     
> 
> and then discuss efficient sorting algorithms O(n log n) such as:
> 
> *   Merge Sort. [Code](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/algorithms/sorting/merge-sort.js) | [Docs](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part04/merge-sort.asc)
>     
> *   Quicksort. [Code](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/src/algorithms/sorting/quick-sort.js) | [Docs](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part04/quick-sort.asc)
>     
> 
> * * *
> 
> Learn different approaches to solve problems such as divide and conquer, dynamic programming, greedy algorithms, and backtracking. _(Click to expand)_
> 
> * * *
> 
> #### [Learn different approaches to solve algorithmic problems](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/part04-algorithmic-toolbox.asc)
> 
> [](#learn-different-approaches-to-solve-algorithmic-problems)
> 
> We are going to discuss the following techniques for solving algorithms problems:
> 
> *   [Greedy Algorithms](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part04/greedy-algorithms.asc): makes greedy choices using heuristics to find the best solution without looking back.
> *   [Dynamic Programming](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part04/dynamic-programming.asc): a technique for speeding up recursive algorithms when there are many _overlapping subproblems_. It uses _memoization_ to avoid duplicating work.
> *   [Divide and Conquer](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part04/divide-and-conquer.asc): _divide_ problems into smaller pieces, _conquer_ each subproblem, and then _join_ the results.
> *   [Backtracking](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part04/backtracking.asc): search _all (or some)_ possible paths. However, it stops, and _go back_ as soon as notice the current solution is not working.
> *   _Brute Force_: generate all possible solutions and tries all of them. (Use it as a last resort or as the starting point).
> 
> * * *

## FAQ

[](#faq)

How would I apply these to my day-to-day work? _(Click to expand)_

As a programmer, we have to solve problems every day. If you want to solve problems well, it's good to know about a broad range of solutions. Often, it's more efficient to learn existing resources than stumble upon the answer yourself. The more tools and practice you have, the better. This book helps you understand the tradeoffs among data structures and reason about algorithms performance.

Why you created this repo/book?

There are not many books about Algorithms in JavaScript. This material fills the gap. Also, it's good practice :)

Is there anyone I can contact if I have questions about something in particular?

Yes, open an issue or ask questions on the \[slack channel\]([https://dsajs-slackin.herokuapp.com](https://dsajs-slackin.herokuapp.com/)).

## Book

[](#book)

This project is also available in a [book](https://books.adrianmejia.com/dsajs-data-structures-algorithms-javascript/). You will get a nicely formatted PDF with 180+ pages + ePub and Mobi version.

[![dsa.js book](https://camo.githubusercontent.com/e070e1730bdd264341ddf28cf684f14c9590558b0f9e3bf126b063288fb2b3bb/68747470733a2f2f626f6f6b732e61647269616e6d656a69612e636f6d2f6473616a732d646174612d737472756374757265732d616c676f726974686d732d6a6176617363726970742f696d616765732f6473616a732d636f7665722d33323068322e706e67)](https://books.adrianmejia.com/dsajs-data-structures-algorithms-javascript/)

## Support

[](#support)

Reach out to me at one of the following places!

*   Twitter at [`@iAmAdrianMejia`](http://twitter.com/iAmAdrianMejia)
*   Chat on [`dsajs.slack.com`](https://dsajs-slackin.herokuapp.com/)

## License

[](#license)

[![License](https://camo.githubusercontent.com/ec32b28ddc386bf40a7cf595a938c46301f1e1afaa2c8fe05bc89cd7b1e4c5c5/68747470733a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)](https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/LICENSE)
