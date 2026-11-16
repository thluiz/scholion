---
url: "https://dev.to/andywer/seamless-web-workers-worker-threads-threads-js-2g36"
captured_at: "2026-11-16T19:23:00+00:00"
title: "Seamless web workers & worker threads - threads.js"
domain: "dev-to"
---

A quick leap into running cross-platform Javascript / TypeScript code in workers. Using a transparent API – minus the hassle.

After half a year in beta, [threads.js](https://threads.js.org/) v1.0 has finally been released. It allows you to use web workers and worker threads in an intuitive way, provides features like thread pools, works in web clients as well as node.js and is less than 10kB in size!

The benefits of using workers have already been covered in plenty of other articles, so here is the gist:

*   Leverage all the available CPU power to run heavy CPU-bound tasks
*   Move all non-rendering code off the main thread to ensure smooth animations and a responsive user interface (web workers)
*   Isolate software modules, restrict them to communicate via message passing

Now even though the web worker and worker threads APIs are similar, unfortunately they are not fully compatible. Furthermore, they are rather low-level building blocks: Create a worker, subscribe to message, post a message, etc.

What happens if you post some messages to a worker and one causes the worker to throw? Chances are the calling code will never know there was an error - it will just not receive a response message. And then there is all the glue code…

## [](#powers-of-a-transparent-api)Powers of a transparent API

Enter the stage… threads.js! Let's write a simple worker that hashes passwords for us.  

```
// workers/auth.js
import sha256 from "js-sha256"
import { expose } from "threads/worker"

expose({
  hashPassword(password, salt) {
    return sha256(password + salt)
  }
})
```

Now let's write the main thread's code – spawn a new worker and hash a password.  

```
// master.js
import { spawn, Thread, Worker } from "threads"

async function main() {
  const auth = await spawn(new Worker("./workers/auth"))
  const hashed = await auth.hashPassword("Super secret password", "1234")

  console.log("Hashed password:", hashed)

  await Thread.terminate(auth)
}

main().catch(console.error)
```

It's simple. Expose a function in the worker, call it from the other thread – done!

Note that `auth.hashPassword()` will always return a promise, whether `hashPassword` originally returns a promise or not – the return value will be promisified, due to the async nature of worker communication.

So what about error handling? It's simple as we are now working with a promise-based API.  

```
// master.js
import { spawn, Thread, Worker } from "threads"

async function main() {
  let auth, hashed

  try {
    auth = await spawn(new Worker("./workers/auth"))
  } catch (error) {
    // Cannot spawn the worker or crashed immediately before doing anything
  }

  try {
    hashed = await auth.hashPassword("Super secret password", "1234")
  } catch (error) {
    // Hashing this password failed
  }

  console.log("Hashed password:", hashed)

  await Thread.terminate(auth)
}

main().catch(console.error)
```

By the way, did you notice `Thread.terminate()`? We use it to terminate a worker once we are done using it.

## [](#run-in-nodejs)Run in node.js

Let's take our previous sample code and change the ES module `import` statements into `require()` calls for now. You can clone the code from [this GitHub Gist](https://gist.github.com/andywer/925395687f42f6da04d111adf7d428ac).  

```
$ git clone git@gist.github.com:925395687f42f6da04d111adf7d428ac.git ./threads-gist
$ cd threads-gist
$ npm install
```

Running it is trivial.  

```
$ node ./master
```

This code will run in any node.js version that comes with worker threads support, so node 12+ or node 10+ with a feature flag set.

You can even run it on node 8.12+. Install the `tiny-worker` npm package – threads.js will automatically pick it up as a polyfill if worker threads are not available.

## [](#build-using-webpack)Build using webpack

A vast number of people use webpack to bundle their code for front-end deployment. So how do we now make that code build with webpack?

We use our code as is, take our webpack config and add the [`threads-plugin`](https://www.npmjs.com/package/threads-plugin) – that's it!  

```
  // webpack.config.js
  const path = require("path")
+ const ThreadsPlugin = require("threads-plugin")

  module.exports = {
    entry: {
      app: "./src/index.js"
    },
    mode: "development",
    module: {
      rules: [
        {
          test: /\.css$/,
          use: ["style-loader", "css-loader"]
        },
        {
          test: /\.jsx?$/,
          use: ["babel-loader"]
        }
      ]
    },
    output: {
      path: path.join(__dirname, "dist")
    },
    plugins: [
      new HtmlPlugin(),
+     new ThreadsPlugin()
    ]
  }
```

The plugin is based on Google's [`worker-plugin`](https://github.com/GoogleChromeLabs/worker-plugin) – it will recognize `new Worker()` expressions, make sure the referenced worker file is bundled independently from the main entrypoint and rewrite the path in the `new Worker()` expression to the worker bundle path.

## [](#first-class-typescript-support)First class TypeScript support

Threads.js is written in TypeScript and thus fully statically typed, so your IDE's IntelliSense will show you all available exports, functions and parameters with documentation as you write. That's not all – even running TypeScript workers becomes easier.

When running your TypeScript code in node.js you will frequently find yourself using `ts-node` in development and running the transpiled JavaScript code in production.

When resolving a worker, threads.js will try to load the transpiled JavaScript worker. If that fails and `ts-node` is installed it will automatically fail-over to run the untranspiled TypeScript worker file using `ts-node`. You don't have to lift a finger 🙌

## [](#thread-pools-observables-amp-more)Thread pools, observables & more

There is more to explore!

*   Thread pools to spawn multiple workers and dispatch jobs to them
*   Returning observables to expose events to subscribe to
*   Support for transferable objects to efficiently pass binary data
*   and more… 🚀

You can find the detailed documentation on [threads.js.org](https://threads.js.org/).

There are also more features to come. Check out the [GitHub repository](https://github.com/andywer/threads.js) and its issues to see what's in discussion right now or watch the repository's releases to stay up to date.

* * *

That's it for today – I hope you enjoyed the blog post. If you like the project, give the repository a 🌟 on GitHub, contribute to the development or [become a sponsor](https://github.com/sponsors/andywer).

Feel invited to comment and leave feedback of any kind below.

Happy holidays and happy hacking!

Andy

[_Teaser image by Adi Goldstein on Unsplash_](https://unsplash.com/photos/EUsVwEOsblE).
