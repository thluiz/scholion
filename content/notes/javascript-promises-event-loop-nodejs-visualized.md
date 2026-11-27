---
title: "JavaScript Promises, Visualized: The Event Loop Behind Node.js"
date: '2026-11-26T14:43:05+00:00'
category: webclip
summary: 'Explains how promises, microtasks, Node.js event loop phases and APIs like nextTick, setImmediate, workers and perf_hooks interact, and how misuse can block probes and crash processes.'
tags: ["nodejs", "javascript", "event-loop", "promises"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "JavaScript Promises, Visualized: The Event Loop Behind Node.js"
    url: "https://devops-daily.com/posts/javascript-promises-event-loop-visualized?via=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devops-daily-com--javascript-promises-event-loop-nodejs-visualized.md"
    kind: repo
---

Node.js runs JavaScript on a single call stack, with promises and async/await built on a microtask queue that the event loop processes before timer and I/O tasks. The article walks through how executors, then/catch, async/await, and microtasks interact, then layers on Node-specific behavior: event loop phases, process.nextTick, setImmediate, and how these affect callback order. It shows how long synchronous work or microtask floods block health checks and other traffic, why unhandled promise rejections now crash the process, and how to detect blocking with event loop delay and utilization metrics.

## Reading notes

- Production symptoms like intermittent failing Kubernetes readiness probes with no errors often come from one long synchronous block that holds Node’s only JavaScript thread, leaving health checks stuck in sockets until they time out.
- JavaScript execution is built from five pieces: a single call stack that runs one function at a time, a host environment (Node.js or browser) that handles timers and I/O, a microtask queue for promise-related callbacks, a task queue for timers and I/O callbacks, and the event loop that coordinates them.
- Promise callbacks (then/catch and the rest of async functions after await) wait in the microtask queue, while timer and I/O callbacks wait in task queues (one per event loop phase in Node.js).
- The core event loop rule: once the call stack is empty, run all microtasks (including those queued during the drain), then run one task, then repeat. This explains why promise callbacks run before a 0 ms timer.
- A promise starts pending, then settles once as fulfilled or rejected. Callbacks for the corresponding outcome are queued as microtasks when it settles, instead of running immediately.
- The function passed to new Promise (the executor) runs synchronously inside the constructor call, but then callbacks always run later, even if resolve was called before then is attached.
- A promise settles only once; later calls to resolve or reject after the first settle have no effect, and resolving with another promise makes it follow that promise’s eventual state.
- A small example with console.log, setTimeout(…, 0), Promise.resolve().then, and queueMicrotask shows that synchronous logs run first, then microtasks (promise and explicit), and finally the timer callback, yielding output order A B C D E.
- Async functions always return a promise, and await pauses the function until the awaited value’s promise settles, returning a pending promise to the caller while the remainder of the function body resumes later as a microtask.
- Even when an awaited value is already available (such as a cached result), await still splits the function: code after await never runs in the same turn of the event loop as the code before it.
- Two async calls started together can interleave work at each await, allowing them to take turns on one thread without parallel execution, as long as each turn is short.
- Node.js extends the common model with process.nextTick, setImmediate, and multiple event loop phases. These APIs do not exist in Chromium in the same way, so scheduling details are Node-specific.
- Node’s event loop phases include timers (setTimeout/setInterval), poll (most I/O and waiting for new I/O), check (setImmediate), close callbacks, and a pending phase for a small set of system callbacks.
- Between every callback execution in any phase, Node drains process.nextTick callbacks first, then promise microtasks, repeating until both queues are empty before moving on to the next event loop callback.
- An example with two 0 ms timers, each queuing a nextTick and a resolved promise then, shows that inside each timer callback, the nextTick callback always runs before the promise microtask from that same callback.
- Putting setTimeout(…, 0), setImmediate, Promise.resolve().then, process.nextTick, and sync code together reveals that the relative order of promise microtasks and nextTick at top level changes between CommonJS and ES modules.
- In a CommonJS file, the observed order is: synchronous log, nextTick callback, promise then, timer callback, then setImmediate.
- In an ES module, the order flips between nextTick and promise: synchronous log, promise then, nextTick callback, timer callback, then setImmediate.
- The difference comes from how Node runs ES modules with async loading: top-level code runs while V8 is already draining the microtask queue, so microtasks created there can run before Node resumes draining nextTick callbacks.
- Inside any promise callback, process.nextTick callbacks queued there run only after the current microtask drain finishes, so promise microtasks created in that callback can run before those nextTicks.
- The article advises not to depend on relative ordering between process.nextTick and promise microtasks, because it varies by context and module system.
- Node’s docs state that the order between setTimeout(fn, 0) and setImmediate in the main module is not guaranteed, since it depends on how quickly the process reaches the event loop.
- Inside I/O callbacks, the ordering is stable: a setImmediate scheduled during a poll phase callback always runs before a 0 ms timer because the check phase comes immediately after poll and before timers.
- An example with fs.readFile shows that within a readFile callback, sync log runs first, then nextTick, then promise microtask, then setImmediate, and finally the timer callback, consistently across many runs.
- The recommended use is to prefer setImmediate when you intend to run code after the current I/O work, and reserve setTimeout(fn, 0) for true timer semantics.
- Other runtimes such as Bun have their own event loop implementations, so detailed scheduling assumptions tested on Node.js may not hold elsewhere and should be validated per runtime.
- A demo HTTP server shows two endpoints: /healthz responds immediately, and /report builds a large CSV synchronously by generating many objects, sorting them, and joining them into a string.
- In sync mode, /report performs the heavy work directly on the main thread; in worker mode, it delegates the report building to a worker thread using worker_threads and receives only the length of the result.
- A client script mimics a Kubernetes probe: it does a warm-up health check, then measures an idle /healthz, triggers /report with a long timeout, and sends another /healthz 100 ms later, each with a 1 second timeout.
- When /report runs synchronously on the main thread, the busy /healthz probe consistently fails after about 1 second, while /report completes in about 2.4 seconds.
- When /report runs in a worker thread with the same workload, /healthz during the report returns in roughly single-digit milliseconds, and the report finishes in about 2.2 seconds including worker overhead.
- The explanation is that /healthz is just another callback; it cannot execute until the call stack is free, and the long report blocks the stack for several seconds, preventing Node from accepting or reading the probe request before its timeout.
- Default Kubernetes probe settings (timeoutSeconds 1, periodSeconds 10, failureThreshold 3) mean repeated probe failures from slow answers mark the Pod as not ready or cause restarts, even if no errors appear in logs.
- Increasing timeoutSeconds only masks the problem while real user requests still wait behind stalled synchronous work; the article argues to fix the blocking cause instead of tuning probes first.
- To remove CPU-heavy work from the event loop, suggested options include worker_threads, a job queue with a dedicated worker process, or splitting such tasks into separate services.
- For worker-based designs in production, the article recommends a small, fixed worker pool with a bounded queue to avoid unbounded CPU and memory usage under bursts.
- Examples of CPU-heavy operations that often block the loop include sorting large collections, compression, hashing via synchronous APIs, and parsing very large JSON strings.
- Long loops can be made cooperative by breaking them into chunks and yielding back to the event loop between chunks so that timers and I/O callbacks can run.
- Health probes should stay lightweight and representative: a liveness probe should only verify that the process can respond, and the system should be load-tested with probes active.
- The article shows that async code can still block the loop when awaits resolve instantly, because each await adds microtasks and the event loop runs microtasks to completion before timers or I/O.
- A demo constructs 2,000,000 SKUs in an array and keeps a Map of prices. An async getPrice function simply returns from the Map, so every await getPrice resolves immediately.
- In priceAll without yielding, a 0 ms timer scheduled before the loop is delayed until the end of processing all 2,000,000 awaits, about 1.45 seconds later.
- When priceAll yields with await setImmediate() from node:timers/promises every 10,000 items, the 0 ms timer runs after only a few milliseconds, and total processing time remains similar.
- This works because setImmediate is not a microtask; awaiting it returns control to the event loop, which can run timers and I/O before returning to the async function in the check phase.
- Recursive process.nextTick usages can produce a similar blocking effect because Node drains the entire nextTick queue before moving on, so a long chain of ticks delays timers in the same way.
- Since Node.js 15, the default --unhandled-rejections mode is throw, so a rejected promise with no handler behaves like an uncaught exception, causing the process to exit with code 1 unless unhandledRejection is handled.
- An example with refreshToken throwing inside an async function, called without await or .catch, shows that the process logs an error and exits before even the next setInterval callback runs.
- A subtler bug occurs when a promise has a handler attached too late: if one fast-failing promise and one slow-resolving promise are awaited sequentially, the rejection may occur before any then/catch/await touches the fast promise.
- In the sequential await example, the invoices promise rejects at 50 ms while the function is still awaiting user for 300 ms, so the rejection has no handler at 50 ms and triggers a process exit.
- Refactoring the code to start both operations at once and await Promise.all on them attaches handlers to both promises immediately, allowing the catch block to see and handle the invoices failure.
- When all results should be collected even if some fail, the article suggests using Promise.allSettled instead of Promise.all.
- For unexpected rejections, the article recommends keeping the default throw behavior and adding a process-level unhandledRejection handler that logs context synchronously and exits the process.
- The logging example writes a JSON line to file descriptor 2 (stderr) using fs.writeSync, then calls process.exit(1), ensuring the log line is flushed even when stderr is a pipe.
- Running the earlier refreshToken example with this hook shows a single structured log line for the unhandled rejection and a clean exit code of 1.
- Switching Node’s unhandled-rejections mode to warn causes the unhandled rejection to only emit a warning while the process continues serving, leaving failed operations like token refresh in a broken state without recovery.
- The article argues that restarting the process from a clean state after unhandled rejections is usually safer than continuing with partial failure.
- To observe event loop blocking, Node’s perf_hooks module provides monitorEventLoopDelay and performance.eventLoopUtilization as built-in metrics.
- monitorEventLoopDelay uses an internal timer that should fire every resolution milliseconds, recording the distribution of observed delays as a histogram of nanoseconds; when the loop is blocked, observed delays increase.
- performance.eventLoopUtilization reports what fraction of time the event loop spent doing work (callbacks or synchronous code) versus being idle and waiting for I/O, and supports measuring deltas between calls.
- A demo script measures a 2-second idle period and a 2-second period with three 250 ms busy loops, using monitorEventLoopDelay with 10 ms resolution and ELU deltas between reports.
- In the idle period, the p50 delay is around the 10 ms sampling interval with near-zero utilization; in the busy period, p99 and max reflect the ~250 ms stalls, and utilization matches roughly 750 ms of busy time in a 2-second window.
- Because delay measurements include the sampling interval, the actual additional delay is the histogram value minus resolution, and outliers show up in p99 and max while the median may stay small.
- The article concludes that alerts should be based on high-percentile or max event loop delay, and that long stalls can be more visible in request latency metrics than in median event loop delay.
- For production monitoring, if prom-client is used, collectDefaultMetrics already exports event loop lag metrics like nodejs_eventloop_lag_p99_seconds using monitorEventLoopDelay.
- A practical alert is suggested: fire when event loop delay p99 stays above a threshold comfortably lower than probe timeouts, for example a few hundred milliseconds when Kubernetes timeoutSeconds is 1.
- When such alerts fire, the recommended response is to capture a CPU profile with node --cpu-prof during busy periods to pinpoint the synchronous code causing event loop blocking.
- The closing checklist emphasizes keeping synchronous work short or off the event loop, yielding in long loops with await setImmediate, avoiding reliance on fragile scheduling order details, starting related promises together with Promise.all or Promise.allSettled, preserving the default unhandled rejection behavior with a crash-logging hook, exporting event loop delay and utilization metrics, and load-testing with probes enabled.

## Related notes

- [How To Use Multithreading in Node.js](/notes/how-to-use-multithreading-in-node-js/)
- [Code Smell 155 — Multiple Promises](/notes/code-smell-155-multiple-promises/)
- [Node.js Best Practices — Error Handling and Logging](/notes/node-js-best-practices-error-handling-and-logging/)
- [Essential JavaScript Interview Questions](/notes/essential-javascript-interview-questions/)
- [Should Junior Developers Still Learn JavaScript the Hard Way?](/notes/should-junior-devs-still-learn-javascript-hard-way/)
