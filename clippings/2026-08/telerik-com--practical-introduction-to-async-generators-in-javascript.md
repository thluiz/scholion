---
url: "https://www.telerik.com/blogs/practical-introduction-async-generators-javascript"
captured_at: "2026-08-03T17:42:35+01:00"
title: "Practical Introduction to Async Generators in JavaScript"
domain: "telerik-com"
---

---
Generators enable you to do [cooperative multitasking](https://en.wikipedia.org/wiki/Cooperative_multitasking) by allowing you to pause and resume functions at will. Put another way, they’re functions that produce an iterable sequence of values on demand, instead of generating them all at once. This kind of computation is **memory efficient** because it doesn’t require all values to be stored in memory at once.

Imagine you have to aggregate one billion rows from a text file. That function would:

1.  Load the file contents into memory
2.  Parse the contents
3.  Aggregate the rows
4.  Return the aggregated result

This would use a lot of memory and you have to wait for everything upfront. Another downside is that you might run out of memory and crash. Now, imagine if you could process each row as it comes in, without waiting for the entire file to load. Perhaps you could process it in smaller chunks and send progress updates to the user or calling function.

This is where **generator functions** come into play, and they can be synchronous or asynchronous.

## A Simple Example

Let’s start with a simple synchronous generator function that yields numbers from 1 to 3:

The `function*` syntax defines a generator function. When you call it, it doesn’t execute the function body immediately. Instead, it returns a generator object that conforms to both the [iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol) and [iterator protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol). This object is then used to control the process of collecting values.

The `yield` keyword is used to pause and hand back a value. It waits, remembering its exact spot until you ask for the next value. When you call `next()`, the generator resumes execution until it hits the next `yield` or completes.

The `next()` method returns an object with two properties: `value` (the yielded value) and `done` (a boolean indicating if the generator has completed). This makes it incredibly memory-efficient. You don’t need to hold all one billion numbers in memory. You just request for one row (or a limited number of rows), use it and then ask for the next.

The example manually calls `next()` to get each value. However, you can also use a `for...of` loop to automatically iterate over the values:

In this example, the `for...of` loop automatically calls `next()` on the generator until it is done. You won’t see an `undefined` value at the end because the loop stops when `done` is `true`.

## Async Generators

What if the next value isn’t ready yet? What if you have to wait for it to be downloaded or fetched from a database? This is where async generators come in. They are the perfect blend of:

-   **Synchronous generators**: They give you values one by one (`yield` or `yield*`).
-   **Async/Await**: They can await asynchronous tasks (like a network request) to finish before continuing.

Think of async generators like waiting for a new episode of a show to be released each week. You ask for the next episode, but you have to wait for it. While you’re waiting, your app isn’t frozen; it can do other things. This makes them ideal for working with files or other asynchronous data sources.

Due to the asynchronous nature of data streams, async generators are an elegant tool for transforming data streams (where both input and output are streams). They enable you to create modular, memory-efficient and highly readable stream-processing logic.

I’ll demonstrate this with a simple ETL (Extract, Transform, Load) pipeline that processes a stream of sales data from a CSV file.

Imagine you have a CSV file with sales data that looks like this:

```
orderID,product,quantity,unitPrice,country
1,Laptop,2,1200,USA
2,Mouse,5,15,USA
3,Keyboard,10,25,Canada
4,Webcam,20,5,UK
5,Monitor,1,300,Canada
6,USB-Cable,8,5,USA
```

Your task is to create a pipeline that can:

1.  **Extract:** Reads the CSV file row by row as a stream.
    
2.  **Transform:**
    
    -   Calculates a `totalPrice` for each sale (`quantity * unitPrice`)
    -   Enriches the data by adding a `region` based on the `country` (simulating an async API call)
    -   Filters out sales with a total price below $50
3.  **Load:** Logs the final, processed data to the console.
    

This entire process will happen one record at a time, without ever loading the full dataset into memory. You’ll create a separate generator function for each step in the pipeline. This makes it incredibly modular—easy to add, remove or reorder steps.

First, let’s create a generator function that reads a CSV file line by line and _yields_ each row as an object. We’ll use the `fs` module to read the file as a stream and the `readline` module to process it line by line.

The first line in the CSV file is treated as the header, which is used to create an object for each subsequent row. Each row is yielded as an object, allowing us to process it one at a time. The `rl` object supports the async iterable protocol, so we can use `for await...of` to read and process each line.

> The async iterator and iterable protocols are similar to the synchronous iterable and iterator protocols, except that each return value from the calls to the iterator methods is wrapped in a promise. Objects supporting these protocols have the methods `[Symbol.asyncIterator]()`, `next()`, `return()` and `throw()` that return promises for objects with the properties `value` and `done`. See the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_async_iterator_and_async_iterable_protocols) for more details.

### Transformers (Data Enrichment and Filtering)

Next, we’ll create three transformer functions. The first will calculate the `totalPrice`, the second will enrich the data with a `region` based on the `country`, and the third will filter out sales below a certain threshold.

### Assemble and Run the Pipeline

Finally, we can assemble the pipeline by chaining these async generator functions together. Here’s how you can run the entire ETL process:

This is where the magic happens! We chain the generator functions together in a clear, declarative way. The `for await...of` loop at the end pulls data through the entire pipeline on demand. When you run this code, you’ll see the processed high-value sales logged to the console, each enriched with a `totalPrice` and `region`. The entire process is efficient and modular, demonstrating the power of async generators in handling streaming data. The output will look something like this:

```
🚀 Starting ETL Pipeline...

--- Processed High-Value Sales ---
{
  orderID: '1',
  product: 'Laptop',
  quantity: 2,
  unitPrice: 1200,
  country: 'USA',
  totalPrice: 2400,
  region: 'North America'
}
{
  orderID: '2',
  product: 'Mouse',
  quantity: 5,
  unitPrice: 15,
  country: 'USA',
  totalPrice: 75,
  region: 'North America'
}
{
  orderID: '3',
  product: 'Keyboard',
  quantity: 10,
  unitPrice: 25,
  country: 'Canada',
  totalPrice: 250,
  region: 'North America'
}
{
  orderID: '4',
  product: 'Webcam',
  quantity: 20,
  unitPrice: 5,
  country: 'UK',
  totalPrice: 100,
  region: 'Europe'
}
{
  orderID: '5',
  product: 'Monitor',
  quantity: 1,
  unitPrice: 300,
  country: 'Canada',
  totalPrice: 300,
  region: 'North America'
}

✅ Pipeline finished.
```

You should notice the slight delay as the rows are streamed and processed, simulating real-world scenarios where data might come from a network or a slow file read.

The fun part? You can easily swap out the data source or add more transformation steps without changing the overall structure. This makes async generators a powerful tool for building flexible and efficient data processing pipelines in JavaScript.

## Wrapping Up

Async generators are a powerful way to process sequences of data **lazily** (one piece at a time) and **asynchronously** (waiting when necessary), leading to more efficient, composable and readable code.

Throughout this article, we’ve explored how they solve common challenges in modern web development:

-   **Memory efficiency:** By processing data on demand, you can handle massive datasets, even billions of rows—without crashing your application due to memory constraints.
-   **Readable asynchronous code:** Async generators allow you to write complex stream-processing logic that reads like simple, synchronous code, freeing you from callback hell.
-   **Modular and composable code:** The ETL example demonstrated how you can build clean, composable data processing pipelines by chaining generators. Each step is a self-contained unit, making your code easier to test, maintain and reason about.
-   **Lazy evaluation:** You only compute what you need, when you need it.

Whether you’re reading large files, consuming real-time data from an API, or building complex data transformation workflows, async generators offer a robust and elegant solution. They encourage you to think in terms of streams, which is a fundamental paradigm for building scalable and resilient applications.

So next time you’re faced with a data-intensive task, consider reaching for _generator functions_. You might be surprised at how much cleaner and more efficient your code becomes! No more wrangling with Buffers or backpressure—just smooth, flowing data processing.
