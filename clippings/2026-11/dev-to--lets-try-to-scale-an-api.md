---
url: "https://dev.to/ashokdey_/building-a-scalable-system-4l41"
captured_at: "2026-11-16T01:16:39+00:00"
title: "Let's try to scale an API"
domain: "dev-to"
---

[![cover](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F228847fx5bgi8lyp4zg4.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F228847fx5bgi8lyp4zg4.jpg)

#### [](#i-previously-wrote-about)I previously wrote about:

*   [Open Source JavaScript Data structures & Algorithms](https://dev.to/ashokdey_/my-first-open-source-project-to-cross-100-stars-232l)
*   [Highly Scalable Codebase Architecture](https://dev.to/ashokdey_/highly-scalable-codebase-architecture-4b)

In this article, we'll get to know the preliminary steps you can take as a **Software Engineer** for improving your code and scaling it.

_**Let's see how we can decrease loadtest time from 187s to 31s**_

**Note:** I'll be using **Node.js** but don't skip reading, try to absorb the concept, especially if you're a beginner.

### [](#here-is-the-task)Here is the task:

_**Build a server with only one `GET` request to return the highest Prime number between 0 - N**_

### [](#my-setup)My Setup

*   I've used pure Node.js (Not `express.js`) for the creation of my server and routes as well, you are free to use `express.js`
*   You can use this idea with any language, so don't skip reading but you can skip the code/code repo.

### [](#lets-start)Let's Start!

I used this as one of my assignments for hiring (experienced) devs. The session used to be a pair-programming setup where the **candidate was free to use the Internet** and tools of his/her choice. Considering the kind of my routine work, such assignments are really helpful.

### [](#when-you-wrote-a-bruteforce-approach)When you wrote a brute-force approach

Let's assume you created your server with the basic algorithm to find a Prime Number. Here is an brute force approach example:  

```
// just trying the first thought in mind
function isPrime(n) {
  for(let i = 2; i <= Math.sqrt(n); i += 1) {
    if (n % i === 0){
      return false;
    }
  }
  return true;
}

function calculateGreatestPrimeInRange(num) {
    const primes = [];
    for (let i = 2; i <= num; i += 1) {
      if (this.isPrime(i)) primes.push(i);
    }
    return primes.length ? primes.pop() : -1;
  }
```

Enter fullscreen mode Exit fullscreen mode

You'll try to use it in your `GET` route say like this `https:localhost:9090/prime?num=20`, it will work fine and you'll feel good. You tried it with some numbers like `?num=10, 55, 101, 1099` you will get instant response and life feels good :)

#### [](#hold-on)Hold On!

**As soon as you try a large number** say `num=10101091` you will feel the lag (I've tried it in the browser, you can use **Postman**)

Since we are not using **PM2** right now (which does a ton of things many of the beginners are not aware of), you'll notice that when you try to open a new tab and try for a smaller number, your tab will be waiting for the result of the previous tab.

### [](#what-can-you-do-now)What can you do now?

Let's bring in concurrency!

*   **Cluster mode at the rescue!**

Here is the block of code showing Cluster mode in action. If you are not aware of _Cluster Module_ please read about it.  

```
const http = require('http');
const cluster = require('cluster');
const os = require('os');
const routes = require('./routes');

const cpuCount = os.cpus().length;

// check if the process is the master process
if (cluster.isMaster) {
  // print the number of CPUs
  console.log(`Total CPUs are: ${cpuCount}`);

  for (let i = 0; i < cpuCount; i += 1) cluster.fork();

  // when a new worker is started
  cluster.on('online', worker => console.log(`Worker started with Worker Id: ${worker.id} having Process Id: ${worker.process.pid}`));

  // when the worker exits
  cluster.on('exit', worker => {
    // log
    console.log(`Worker with Worker Id: ${worker.id} having Process Id: ${worker.process.pid} went offline`);
    // let's fork another worker
    cluster.fork();
  });
} else {
  // when the process is not a master process, run the app status
  const server = http.createServer(routes.handleRequests).listen(9090, () => console.log('App running at http://localhost:9090'));
}
```

Enter fullscreen mode Exit fullscreen mode

### [](#voila)Voila!

After implementing the Cluster Module, you'll see a drastic change!

You can notice after this using threads, the browser tab with a smaller number will get the response quickly, meanwhile the other tab is busy doing the calculations (you can try it out in Postman as well)

For those who are not using Node.js, cluster mode refers to running your app in concurrent mode, utilizing the available threads on the CPU.

Now we have a bit of relaxation, but what else can we do to make it even more performant, because our single requests with large numbers are still lagging?

### [](#algorithms-at-your-rescue)Algorithms at your rescue!

I know this is a haunting word but it is an essential tool you cannot ignore and in the end, after implementing a new algorithm you'll get to realize the worth of Algorithms.

So for prime numbers, we have a **[Sieve of Eratosthenes  
](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)**We have to tweak it a bit so as to fit this in our use-case. You can find the complete code in the repo inside the class `Prime`.

Let's have a look at the **Loadtesting Results**

*   Brute force approach for `num=20234456`

Command passed to the **loadtest module**:  

```
loadtest -n 10 -c 10 --rps 200 "http://localhost:9090/prime?num=20234456"
```

Enter fullscreen mode Exit fullscreen mode

Result:  

```
INFO Total time:          187.492294273 s
INFO Requests per second: 0
INFO Mean latency:        97231.6 ms
INFO 
INFO Percentage of the requests served within a certain time
INFO   50%      108942 ms
INFO   90%      187258 ms
INFO   95%      187258 ms
INFO   99%      187258 ms
INFO  100%      187258 ms (longest request)
```

Enter fullscreen mode Exit fullscreen mode

*   Using SOE with modifications for `num=20234456`

Command passed to the **loadtest module**:  

```
loadtest -n 10 -c 10 --rps 200 "http://localhost:9090/prime?num=20234456"
```

Enter fullscreen mode Exit fullscreen mode

Result:  

```
INFO Total time:          32.284605092999996 s
INFO Requests per second: 0
INFO Mean latency:        19377.3 ms
INFO 
INFO Percentage of the requests served within a certain time
INFO   50%      22603 ms
INFO   90%      32035 ms
INFO   95%      32035 ms
INFO   99%      32035 ms
INFO  100%      32035 ms (longest request)
```

Enter fullscreen mode Exit fullscreen mode

You can compare both the results above and can see SOE is a clear winner here.

### [](#can-we-improve-it-further)Can we improve it further?

Yes, we can, we can add a **cache**, a plain Object in Javascript which can be used as a **HashMap**.

Using a cache will store the result for a given number N, if we get a request again for N, we can simply return it from the store instead of doing the calculations.

**REDIS will do a much better job here**

#### [](#lets-see-the-results)Let's see the results

*   Brute force approach with **cache** for `num=20234456`

```
INFO Target URL:          http://localhost:9090/prime?num=20234456
INFO Max requests:        10
INFO Concurrency level:   10
INFO Agent:               none
INFO Requests per second: 200
INFO 
INFO Completed requests:  10
INFO Total errors:        0
INFO Total time:          47.291413455000004 s
INFO Requests per second: 0
INFO Mean latency:        28059.6 ms
INFO 
INFO Percentage of the requests served within a certain time
INFO   50%      46656 ms
INFO   90%      46943 ms
INFO   95%      46943 ms
INFO   99%      46943 ms
INFO  100%      46943 ms (longest request)

```

Enter fullscreen mode Exit fullscreen mode

*   Using SOE with modifications & **cache** for `num=20234456`

```

INFO Target URL:          http://localhost:9090/prime-enhanced?num=20234456
INFO Max requests:        10
INFO Concurrency level:   10
INFO Agent:               none
INFO Requests per second: 200
INFO 
INFO Completed requests:  10
INFO Total errors:        0
INFO Total time:          31.047955697999996 s
INFO Requests per second: 0
INFO Mean latency:        19081.8 ms
INFO 
INFO Percentage of the requests served within a certain time
INFO   50%      23192 ms
INFO   90%      32657 ms
INFO   95%      32657 ms
INFO   99%      32657 ms
INFO  100%      32657 ms (longest request)

```

Enter fullscreen mode Exit fullscreen mode

### [](#time-analysis)Time Analysis

Conditions

Time

With basic algo

187.492294273 s

With Cache

47.291413455000004 s

With SOE

32.284605092999996 s

With SOE & Cache

31.047955697999996 s

### [](#finally)Finally

I hope you understood the benefits of the following:

*   Multithreading
*   Algorithms
*   Caching a.k.a Memoization

I hope you liked this short note, your suggestions are welcome. Hre is the code repo: [find-highest-prime](https://github.com/knaxus/highest-prime-number)

You can find me on [Github](https://github.com/ashokdey), [LinkedIn](https://linkedin.com/in/ashokdey), and, [Twitter](https://twitter.com/ashokdey_)
