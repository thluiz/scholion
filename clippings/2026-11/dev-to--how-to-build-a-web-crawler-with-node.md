---
url: "https://dev.to/bnevilleoneill/how-to-build-a-web-crawler-with-node-3hn2"
captured_at: "2026-11-16T19:24:00+00:00"
title: "How to build a web crawler with Node"
domain: "dev-to"
---

**Written by [Jordan Irabor](https://blog.logrocket.com/author/jordanirabor/)**✏️

## [](#introduction)Introduction

A web crawler, often shortened to _crawler_ or sometimes called a _spider-bot_, is a bot that systematically browses the internet typically for the purpose of [web indexing](https://en.wikipedia.org/wiki/Web_indexing). These internet bots can be used by search engines to improve the quality of search results for users. In addition to indexing the world wide web, crawling can also be used to gather data (known as web scraping).

The process of web scraping can be quite tasking on the CPU depending on the site’s structure and the complexity of data being extracted. To optimize and speed up this process, we will make use of [Node workers](https://nodejs.org/api/worker_threads.html) (threads) which are useful for CPU-intensive operations.

In this article, we will learn how to build a web crawler that scrapes a website and stores the data in a database. This crawler bot will perform both operations using Node workers.

[![LogRocket Free Trial Banner](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5v4d38onzjhw8d6teqf6.png)](https://logrocket.com/signup/)

## [](#prerequisites)Prerequisites

1.  Basic knowledge of [Node.js](https://nodejs.org/en/docs/)
2.  [Yarn](https://yarnpkg.com/lang/en/) or [NPM](https://www.npmjs.com/) (we’ll be using Yarn)
3.  A system configured to run [Node](https://nodejs.org/en/) code (preferably version 10.5.0 or superior)

## [](#installation)Installation

Launch a terminal and create a new directory for this tutorial:  

```
$ mkdir worker-tutorial
$ cd worker-tutorial
```

Enter fullscreen mode Exit fullscreen mode

Initialize the directory by running the following command:  

```
$ yarn init -y
```

Enter fullscreen mode Exit fullscreen mode

We need the following packages to build the crawler:

*   [Axios](https://github.com/axios/axios) — a promised based HTTP client for the browser and Node.js
*   [Cheerio](https://cheerio.js.org/) — a lightweight implementation of jQuery which gives us access to the DOM on the server
*   [Firebase database](https://firebase.google.com/products/realtime-database) — a cloud-hosted NoSQL database. If you’re not familiar with setting up a firebase database, check out the [documentation](https://firebase.google.com/docs/web/setup) and follow steps 1-3 to get started

Let’s install the packages listed above with the following command:  

```
$ yarn add axios cheerio firebase-admin
```

Enter fullscreen mode Exit fullscreen mode

## [](#hello-workers)Hello workers

Before we start building the crawler using workers, let’s go over some basics. You can create a test file `hello.js` in the root of the project to run the following snippets.

## [](#registering-a-worker)Registering a worker

A worker can be initialized (registered) by importing the worker class from the `worker_threads` module like this:  

```
// hello.js

const { Worker } = require('worker_threads');

new Worker("./worker.js");
```

Enter fullscreen mode Exit fullscreen mode

## [](#hello-world)Hello world

Printing out `Hello World` with workers is as simple as running the snippet below:  

```
// hello.js

const { Worker, isMainThread }  = require('worker_threads');
if(isMainThread){
    new Worker(__filename);
} else{
    console.log("Worker says: Hello World"); // prints 'Worker says: Hello World'
}
```

Enter fullscreen mode Exit fullscreen mode

This snippet pulls in the worker class and the `isMainThread` object from the `worker_threads` module:

*   `isMainThread` helps us know when we are either running inside the main thread or a worker thread
*   `new Worker(__filename)` registers a new worker with the `__filename` variable which, in this case, is `hello.js`

## [](#communication-with-workers)Communication with workers

When a new worker (thread) is spawned, there is a messaging port that allows inter-thread communications. Below is a snippet which shows how to pass messages between workers (threads):  

```
// hello.js

const { Worker, isMainThread, parentPort }  = require('worker_threads');

if (isMainThread) {
    const worker =  new Worker(__filename);
    worker.once('message', (message) => {
        console.log(message); // prints 'Worker thread: Hello!'
    });
    worker.postMessage('Main Thread: Hi!');
} else {
    parentPort.once('message', (message) => {
        console.log(message) // prints 'Main Thread: Hi!'
        parentPort.postMessage("Worker thread: Hello!");
    });
}
```

Enter fullscreen mode Exit fullscreen mode

In the snippet above, we send a message to the parent thread using `parentPort.postMessage()` after initializing a worker thread. Then we listen for a message from the parent thread using `parentPort.once()`. We also send a message to the worker thread using `worker.postMessage()` and listen for a message from the worker thread using `worker.once()`.

Running the code produces the following output:  

```
Main Thread: Hi!
Worker thread: Hello!
```

Enter fullscreen mode Exit fullscreen mode

## [](#building-the-crawler)Building the crawler

Let’s build a basic web crawler that uses Node workers to crawl and write to a database. The crawler will complete its task in the following order:

1.  Fetch (request) HTML from the [website](https://www.iban.com/exchange-rates)
2.  Extract the HTML from the response
3.  Traverse the DOM and extract the table containing exchange rates
4.  Format table elements (`tbody`, `tr`, and `td`) and extract exchange rate values
5.  Stores exchange rate values in an object and send it to a worker thread using `worker.postMessage()`
6.  Accept message from parent thread in worker thread using `parentPort.on()`
7.  Store message in firestore (firebase database)

Let’s create two new files in our project directory:

1.  `main.js` – for the main thread
2.  `dbWorker.js` – for the worker thread

The source code for this tutorial is available here on [GitHub](https://github.com/Jordanirabor/workers-tutorial). Feel free to clone it, fork it or submit an issue.

## [](#main-thread-mainjs)Main thread (main.js)

In the main thread, we will scrape the [IBAN website](https://www.iban.com/exchange-rates) for the current exchange rates of popular currencies against the US dollar. We will import `axios` and use it to fetch the HTML from the site using a simple `GET` request.

We will also use `cheerio` to traverse the DOM and extract data from the table element. To know the exact elements to extract, we will open the [IBAN website](https://www.iban.com/exchange-rates) in our browser and load [dev tools](https://www.google.com/search?q=devtools&oq=devtools&aqs=chrome..69i57j0l4j69i60l2j69i61.2226j0j7&sourceid=chrome&ie=UTF-8):

[![devtools](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi1.wp.com%2Fblog.logrocket.com%2Fwp-content%2Fuploads%2F2019%2F12%2Fdevtools.png%3Fresize%3D730%252C456%26ssl%3D1)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi1.wp.com%2Fblog.logrocket.com%2Fwp-content%2Fuploads%2F2019%2F12%2Fdevtools.png%3Fresize%3D730%252C456%26ssl%3D1)

From the image above, we can see the `table` element with the classes — `table table-bordered table-hover downloads`. This will be a great starting point and we can feed that into our `cheerio` root element selector:  

```
// main.js

const axios = require('axios');
const cheerio = require('cheerio');
const url = "https://www.iban.com/exchange-rates";

fetchData(url).then( (res) => {
    const html = res.data;
    const $ = cheerio.load(html);
    const statsTable = $('.table.table-bordered.table-hover.downloads > tbody > tr');
    statsTable.each(function() {
        let title = $(this).find('td').text();
        console.log(title);
    });
})

async function fetchData(url){
    console.log("Crawling data...")
    // make http call to url
    let response = await axios(url).catch((err) => console.log(err));

    if(response.status !== 200){
        console.log("Error occurred while fetching data");
        return;
    }
    return response;
}
```

Enter fullscreen mode Exit fullscreen mode

Running the code above with Node will give the following output:

[![crawling data from example](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi0.wp.com%2Fblog.logrocket.com%2Fwp-content%2Fuploads%2F2019%2F12%2Fruncode.png%3Fresize%3D730%252C456%26ssl%3D1)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi0.wp.com%2Fblog.logrocket.com%2Fwp-content%2Fuploads%2F2019%2F12%2Fruncode.png%3Fresize%3D730%252C456%26ssl%3D1)

Going forward, we will update the `main.js` file so that we can properly format our output and send it to our worker thread.

## [](#updating-the-main-thread)Updating the main thread

To properly format our output, we need to get rid of white space and tabs since we will be storing the final output in `JSON`. Let’s update the `main.js` file accordingly:  

```
// main.js
[...]
let workDir = __dirname+"/dbWorker.js";

const mainFunc = async () => {
  const url = "https://www.iban.com/exchange-rates";
  // fetch html data from iban website
  let res = await fetchData(url);
  if(!res.data){
    console.log("Invalid data Obj");
    return;
  }
  const html = res.data;
  let dataObj = new Object();
  // mount html page to the root element
  const $ = cheerio.load(html);

  let dataObj = new Object();
  const statsTable = $('.table.table-bordered.table-hover.downloads > tbody > tr');
  //loop through all table rows and get table data
  statsTable.each(function() {
    let title = $(this).find('td').text(); // get the text in all the td elements
    let newStr = title.split("\t"); // convert text (string) into an array
    newStr.shift(); // strip off empty array element at index 0
    formatStr(newStr, dataObj); // format array string and store in an object
  });

  return dataObj;
}

mainFunc().then((res) => {
    // start worker
    const worker = new Worker(workDir); 
    console.log("Sending crawled data to dbWorker...");
    // send formatted data to worker thread 
    worker.postMessage(res);
    // listen to message from worker thread
    worker.on("message", (message) => {
        console.log(message)
    });
});

[...]

function formatStr(arr, dataObj){
    // regex to match all the words before the first digit
    let regExp = /[^A-Z]*(^\D+)/ 
    let newArr = arr[0].split(regExp); // split array element 0 using the regExp rule
    dataObj[newArr[1]] = newArr[2]; // store object 
}
```

Enter fullscreen mode Exit fullscreen mode

In the snippet above, we are doing more than data formatting; after the `mainFunc()` has been resolved, we pass the formatted data to the `worker` thread for storage.

## [](#worker-thread-dbworkerjs)Worker thread (dbWorker.js)

In this worker thread, we will initialize firebase and listen for the crawled data from the main thread. When the data arrives, we will store it in the database and send a message back to the main thread to confirm that data storage was successful.

The snippet that takes care of the aforementioned operations can be seen below:  

```
// dbWorker.js

const { parentPort } = require('worker_threads');
const admin = require("firebase-admin");

//firebase credentials
let firebaseConfig = {
    apiKey: "XXXXXXXXXXXX-XXX-XXX",
    authDomain: "XXXXXXXXXXXX-XXX-XXX",
    databaseURL: "XXXXXXXXXXXX-XXX-XXX",
    projectId: "XXXXXXXXXXXX-XXX-XXX",
    storageBucket: "XXXXXXXXXXXX-XXX-XXX",
    messagingSenderId: "XXXXXXXXXXXX-XXX-XXX",
    appId: "XXXXXXXXXXXX-XXX-XXX"
};

// Initialize Firebase
admin.initializeApp(firebaseConfig);
let db = admin.firestore();
// get current data in DD-MM-YYYY format
let date = new Date();
let currDate = `${date.getDate()}-${date.getMonth()}-${date.getFullYear()}`;
// recieve crawled data from main thread
parentPort.once("message", (message) => {
    console.log("Recieved data from mainWorker...");
    // store data gotten from main thread in database
    db.collection("Rates").doc(currDate).set({
        rates: JSON.stringify(message)
    }).then(() => {
        // send data back to main thread if operation was successful
        parentPort.postMessage("Data saved successfully");
    })
    .catch((err) => console.log(err))    
});
```

Enter fullscreen mode Exit fullscreen mode

> Note: To set up a database on firebase, please visit the [firebase documentation](https://firebase.google.com/docs/web/setup) and follow steps 1-3 to get started.

Running `main.js` (which encompasses `dbWorker.js`) with Node will give the following output:

[![node output](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi0.wp.com%2Fblog.logrocket.com%2Fwp-content%2Fuploads%2F2019%2F12%2Fnodeoutput.png%3Fresize%3D436%252C120%26ssl%3D1)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi0.wp.com%2Fblog.logrocket.com%2Fwp-content%2Fuploads%2F2019%2F12%2Fnodeoutput.png%3Fresize%3D436%252C120%26ssl%3D1)

You can now check your firebase database and will see the following crawled data:

[![firebase display of data](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi2.wp.com%2Fblog.logrocket.com%2Fwp-content%2Fuploads%2F2019%2F12%2Fcrawleddatainfirebase.png%3Fresize%3D1001%252C573%26ssl%3D1)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi2.wp.com%2Fblog.logrocket.com%2Fwp-content%2Fuploads%2F2019%2F12%2Fcrawleddatainfirebase.png%3Fresize%3D1001%252C573%26ssl%3D1)

## [](#final-notes)Final notes

Although web crawling can be fun, it can also be against the law if you use data to commit copyright infringement. It is generally advised that you read the terms and conditions of the site you intend to crawl, to know their data crawling policy beforehand. You can learn more in the Crawling Policy section of this [page](https://en.m.wikipedia.org/wiki/Web_crawler).

The use of worker threads does not guarantee your application will be faster but can present that mirage if used efficiently because it frees up the main thread by making CPU intensive tasks less cumbersome on the main thread.

## [](#conclusion)Conclusion

In this tutorial, we learned how to build a web crawler that scrapes currency exchange rates and saves it to a database. We also learned how to use worker threads to run these operations.

The source code for each of the following snippets is available on [GitHub](https://github.com/Jordanirabor/workers-tutorial). Feel free to clone it, fork it or submit an issue.

## [](#further-reading)Further reading

Interested in learning more about worker threads? You can check out the following links:

*   [Worker threads](https://nodejs.org/api/worker_threads.html)
*   [Node.js multithreading: What are Worker Threads and why do they matter?](https://blog.logrocket.com/node-js-multithreading-what-are-worker-threads-and-why-do-they-matter-48ab102f8b10/)
*   [Going Multithread with Node.js](https://medium.com/@Trott/using-worker-threads-in-node-js-80494136dbb6)
*   [Simple bidirectional messaging in Node.js Worker Threads](https://hackernoon.com/simple-bidirectional-messaging-in-node-js-worker-threads-7fe41de22e3c)

* * *

## [](#200s-only-monitor-failed-and-slow-network-requests-in-production)200's only: Monitor failed and slow network requests in production

Deploying a Node-based web app or website is the easy part. Making sure your Node instance continues to serve resources to your app is where things get tougher. If you’re interested in ensuring requests to the backend or third party services are successful, [try LogRocket.](https://logrocket.com/signup/)

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fd7vlcrb4oz72rxl65j48.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fd7vlcrb4oz72rxl65j48.png)

LogRocket instruments your app to record baseline performance timings such as page load time, time to first byte, slow network requests, and also logs Redux, NgRx, and Vuex actions/state. [Start monitoring for free.](https://logrocket.com/signup/)

* * *

The post [How to build a web crawler with Node](https://blog.logrocket.com/how-to-build-a-web-crawler-with-node/) appeared first on [LogRocket Blog](https://blog.logrocket.com/).
