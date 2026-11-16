---
url: "https://blog.logrocket.com/using-typescript-to-stop-unexpected-data-from-breaking-your-app"
captured_at: "2026-11-16T02:48:48+00:00"
title: "Take control of unexpected data at runtime with TypeScript - LogRocket Blog"
domain: "blog-logrocket-com"
---

In this article, we’ll explore how to use TypeScript type definitions to get better guarantees for runtime safety. We’ll show how [runtypes](https://github.com/pelotom/runtypes) and [io-ts](https://gcanti.github.io/io-ts/) libraries are used and explain why they exist in the first place.

![Using TypeScript to stop unexpected data from breaking your app](https://blog.logrocket.com/wp-content/uploads/2019/12/using-typescript-stop-unexpected-data-breaking-your-app.png)

The TypeScript compiler is a powerful friend. It will help you understand what kind of data you are dealing with — function parameters, return types, constants, library definitions, and so on. You can avoid surprising values and find common mistakes with minimal configuration. The compiler will save you from having to validate everything with tests, or manually in a UI, which saves time. Libraries tend to have decent type definitions these days, and many are written in TypeScript. With additional flags, you can turn the (type) quality of the code up:

*   `strict` (recommended – includes `noImplicitThis`, `noImplicitAny`, enforces types)
*   `noEmitOnError` (all emitted code should be checked)
*   `noImplicitReturns`
*   `noFallthroughCasesInSwitch`

With a strict config and extensive typing, can your app compile and still break? Yes it can!

## Runtime safety

TypeScript provides compile time safety. If you refer to a familiar value in a wrong way in the code, you’ll get compile errors. Typo in an attribute name? A compile error. What about runtime safety? Runtime exceptions are a feature of JavaScript, and therefore of Typescript. For example, `JSON.parse` throws an exception if it encounters non-JSON data. `foo.bar()` throws a `ReferenceError` if `foo` doesn’t exist. These can be caught with `try {…} catch (e) {…}`, or handled as Promise rejections. That is all well and good, but we can do even better.

Usually, when an unexpected exception is thrown, the culprit is the data that flows in and out of the application. Given that you can near-perfectly define how a TypeScript app deals with data that conforms to known `interface`s, how can it happen? Declaring an interface is like stating that “this is what my data looks like; enforce it please.” Well, you can lie — or just be wrong.

I’ll show how to deal with unexpected data during runtime with three distinct examples.

## Exploring the unknown

I’ve concluded that no existing static site generator will do, so I decided to build my own. After a lot of hard work, I came up with this:

import fs from 'fs'

interface Config {
  siteName: string
  siteUrl: string
  contentPath: string
}

try {
  const configFile \= fs.readFileSync('./config.json', 'utf-8')
  const config: Config \= JSON.parse(configFile)

  console.info(\`![🚧](https://s.w.org/images/core/emoji/17.0.2/svg/1f6a7.svg) Generating "${config.siteName}"\`)

  const pages \= fs.readdirSync(config.contentPath)
  // do something with the pages ...

  console.info('![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Done')
} catch (e) {
  console.error('Something went wrong!', e)
}

Being a seasoned developer, I am wary of exceptions thrown by `fs` and `JSON.parse` . My app compiles. But when I run it, I see this:

$ node site\_generator.js

![🚧](https://s.w.org/images/core/emoji/17.0.2/svg/1f6a7.svg) Generating "undefined"
...

Looks like I have a typo in my config file. It spells “sitename” instead of “siteName.” This is a simple example of how essentially all data that comes into your app is technically unknown. Luckily, there’s a way to deal with unknown data at runtime. I introduced the [`runtypes`](https://github.com/pelotom/runtypes) library to my app.

import fs from 'fs'
import { String, Record, Static } from 'runtypes'

const Config \= Record({
  siteName: String,
  siteUrl: String,
  contentPath: String
})

// this is equivalent to the "Config" interface from before
type Config \= Static<typeof Config\>

try {
  const configFile \= fs.readFileSync('./config.json', 'utf-8')
  const config: Config \= JSON.parse(configFile)

  // The important bit
  Config.check(config)

  console.info(\`![🚧](https://s.w.org/images/core/emoji/17.0.2/svg/1f6a7.svg) Generating "${config.siteName}"\`)

  const pages \= fs.readdirSync(config.contentPath)
  // do something with the pages ...

  console.info('![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Done')
} catch (e) {
  console.error('Something went wrong!', e)
}

The app looks almost the same. The difference is that I’ve declared `Config` using the types provided by `runtypes`. The term [record](https://en.wikipedia.org/wiki/Record_\(computer_science\)) and the related term field are similar to what people refer to as objects and attributes, but since objects in JavaScript can be just about anything, (`window`, `Array`, etc.), the distinction is useful. Think of records as rows in a spreadsheet — they’re “just” data. The runtime object that `runtypes` builds from the record has methods such as `check` and `guard` that validate that some data is compatible with the actual type definition that I declared (line 11).

You might have used some form validation library before to do something similar. In a form, we validate the values. Here, we validate the structure (“fields” and their values). You can add [extra validation constraints](https://github.com/pelotom/runtypes#constraint-checking) that narrow down the valid values too. This is great for validating incoming payloads in API handlers.

This might seem like a lot to take in. Let’s run the new version with the same faulty config file before I explain the implications of all of this (you can try it in [CodeSandbox](https://codesandbox.io/s/ts-runtime-safety-node-70dx2)).

$ node site\_generator\_safe.js

Something went wrong! ValidationError: Expected string, but was undefined
    at new ValidationError (./node\_modules/runtypes/lib/errors.js:19:28)
    at Object.check (./node\_modules/runtypes/lib/runtype.js:23:15)
    < some stack frames omitted \>
    at Function.Module.runMain (internal/modules/cjs/loader.js:1047:10)
    at internal/main/run\_main\_module.js:17:11 {
  key: 'siteName',
  name: 'ValidationError'
}

The undefined value was recognized. The application stopped before it had a chance to use the bad config. As you might imagine, a somewhat more advanced app would benefit from giving up early on, rather than halfway through a long process. Slightly incorrect config could wreak havoc in a script that, for example, bills customers monthly.

In the result above, my app threw an exception with `ValidationError` when it checked bad config. That’s how the `check` method works: it brings unexpected data into the realm of things you can manage by catching it. There is a way to deal with bad data without using exceptions — we’ll get to that shortly. First, let’s talk about the reliability of web APIs.

## What if an API lies?

Few web or mobile applications are useful without external data. In 2019, most apps get their data from cloud-based [REST or GraphQL](https://blog.logrocket.com/graphql-vs-rest-what-you-didnt-know/) APIs. These APIs are often versioned and hopefully come with some kind of documentation that states what kind of data you can expect to receive (or should send). The documentation can be interactive — [Swagger](https://swagger.io/) is a nice tool for that.

Errors from questionable design, like returning HTML-formatted error responses with OK (200) status from JSON APIs, can be caught in the JSON parsing phase. If you’re lucky enough to have solid TypeScript code on both the backend and the frontend, you can share type definitions and, at best, guarantee that both sides truly understand each other. The reality is that you often end up hoping that developers on the other side know what they are doing. Thoughtful devs use integration tests, versioning, and frozen schemas to provide guarantees for their API. You might still make errors on your side when writing type definitions.

Changes in the APIs you rely on and any weird behavior can be caught with `runtypes` during testing and QA. You can build integration tests on your side that only validate that the API responses are up to date with your assumptions (or the other way around) using runtime type checking. An app that is running in production might not have a reasonable way to recover from type errors. You can still get a descriptive error message or crash report. An infinite (restart) loop can also be avoided.

I’ll show you how this works in practice.

## Fetch me a type-safe record, will you?

The static site generator proved to be too big an undertaking, so I’m going to build a to-do app instead. Let’s start by retrieving data from the API using [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API). We’ll see that having `runtypes` validate incoming data brings other benefits too.

import { String, Number, Boolean, Record, Static } from 'runtypes'

const Todo \= Record({
  userId: Number,
  id: Number,
  title: String,
  completed: Boolean
})

type Todo \= Static<typeof Todo\>

function getTodo(id: number) {
  fetch(\`https://jsonplaceholder.typicode.com/todos/${id}\`)
    .then(response \=> response.json())
    .then(todo \=> Todo.check(todo))
    // todo is now verified to be a Todo and you can safely access the attributes
    .then(todo \=> console.log(\`Todo: #${todo.id}: ${todo.title}\`))
    .catch(e \=> console.error(e))
}

The `getTodo` function fetches some data, parses the JSON response, and then type checks the result in separate steps. Any errors in type checking will be caught, along with connection and JSON parsing-related errors, in the `.catch` handler. After the type is checked, you can work with the contents of a `Todo` without an explicit type annotation. This will clean up the code in cases where TypeScript can’t infer the type of essentially unknown data.

If I add a new field called “priority” with type `Number` to the Todo record (not present in the API), a call to `getTodo` results in `ValidationError: Expected number, but was undefined`. I can specify less fields than the API provides if I don’t need all of them in the app.

Fields that can be `null` in the API response are supported. They look like this: `priority: Number.Or(Null)`. Note the capital N in Null. It’s defined by `runtypes`.

The to-do app is using a Promise-based flow. Had I used `async / await`, `getTodo` would look like this:

async function getTodo(id: number) {
  try {
    const response \= await fetch(\`https://jsonplaceholder.typicode.com/todos/${id}\`)
    const data \= await response.json()
    const todo \= Todo.check(data)

    console.log(\`Todo: #${todo.id}: ${todo.title}\`)
  } catch (e) {
    console.error(e)
  }
}

It’s up to you to decide which format works better for your use case. `runtimes` doesn’t limit the options for the application design. In fact, now is a good time to discuss how we can avoid type checking-related exceptions altogether.

## Errors as data

I’m personally not a fan of the idea of runtime exceptions. I much prefer to use a language or library that gives me a chance to work with failures as data instead of a [GOTO-like control flow](https://softwareengineering.stackexchange.com/questions/189222/are-exceptions-as-control-flow-considered-a-serious-antipattern-if-so-why). What does failure as data look like? Many are familiar with the NodeJS convention for callback parameters `(err, data)` , which are sometimes used as function return values.

const \[err, data\] \= myFunction("foo", "bar")

This format can prevent exceptions, but it is still cumbersome. You have to check for the presence of `err` or `data` (the idea is that one of them is always `null`, not guaranteed). This design can be thought to have boolean logic — an action results in err or data. A more sophisticated approach is to use a union type.

type Success<T\> \= {
  success: true
  value: T
}

type Failure \= {
  success: false
  message: string
  key?: string
}

type Result<T\> \= Success<T\> | Failure

The snippet above is from `runtypes` source code (I’ve removed export statements and comments). A successful operation is presented as a record with an associated `value`. A failure (error) describes the error with a `message`. This idea is not unique to `runtypes`; it’s found in many programming languages, such as Rust, Elm, Haskell and Swift. It’s also similar to Option/Maybe in its duality. Let’s see how using this idea changes the `getTodo` function.

function getTodo(id: number): Promise<Result<Todo\>> {
  return fetch(\`https://jsonplaceholder.typicode.com/todos/${id}\`)
    .then(response \=> response.json())
    .then(Todo.validate)
}

getTodo(1)
  .then(result \=> {
    if (result.success) {
      console.log(\`Todo: #${result.value.id}: ${result.value.title}\`)
    } else {
      // result is Failure
      console.error(result.message)
    }
  })
  // the request or JSON parsing can still fail
  .catch(e \=> console.error(e))

For those familiar with generics in TypeScript, the function return type makes sense. If it looks weird for others, don’t be alarmed! It’s just a specific kind of data inside a different kind of data. You can work with the `result` in the function’s promise chain if you want to, but I have chosen to move the logic out of the function. This way, `Todo`s can be fetched and validated, and you can do whatever you want with the results.

Regarding the `.catch` handler above, if `fetch` worked with `Result`s out of the box, it would be possible to chain it with our validation logic. You can build a wrapper that catches exceptions and returns a `Result`. That’s outside the scope of this article. Some languages have a Result-like type baked into their standard library, and it’s used by everything that can fail, making things much safer and convenient than in the TS/JS ecosystem by default.

If you’ve made it this far, awesome! Now you have a new tool at your disposal that can greatly improve the quality of an app. You can play around with this version in [CodeSandbox](https://codesandbox.io/s/merhk?fontsize=14&hidenavigation=1&theme=dark). If I can still have your attention, I have something to show.

## No alarms and no surprises, please

Think about the proposition that if your app compiles, it works. If you can rely on that, you’ll only have to fix any compile errors and you’ll have an app that is completely predictable. Then you only have to make sure your algorithms are valid and that you haven’t forgotten to render some results. This enables you to work without the usual anxiety and doubt.

The [Elm programming language](https://elm-lang.org/) is known for promising zero runtime exceptions. It’s a big promise to make. Consider third-party libraries: how in the world can you be sure that code authored by someone else is completely safe, so to speak? That’s only possible if the programming language authors carefully choose a limited set of operations that everybody adheres to. Curious about how Elm makes this possible? All libraries are pure Elm, retrieved from a central package registry that enforces the following:

*   Semantic versioning — a library will not compile if the semantic version is wrong.
*   Safety — libraries are written in Elm, so everybody’s code equally safe from exceptions.
*   Any ultimate `Result`s in a library function will be handled by you — a lib can’t cause mayhem. You can also disregard any errors in the library, if it pleases you

Elm has a runtime of its own that requires you to encode/decode (validate) all data that flows in an out of the application. Being a pure functional language, all functions in an app and libs deal only with values provided as their parameters and can only return descriptions of [side-effects](https://jrsinclair.com/articles/2018/how-to-deal-with-dirty-side-effects-in-your-pure-functional-javascript/), not trigger them. Every function has to have a meaningful return value.

I am a big fan of Elm. Whenever I choose to use TypeScript (or can’t use Elm), I try to keep Elm’s lofty goal in mind. Though Elm is not as popular as TypeScript, it’s very influential. That’s why you’ll find libraries in the JavaScript ecosystem that straight-up imitate Elm’s features. The most popular one might be Redux, which is an approximation of Elm’s state management. Let me introduce you to [io-ts](https://gcanti.github.io/io-ts/) which is an FP/Elm-flavored alternative to `runtypes`.

## Either way, no runtime exceptions

Take a look at another version of the fetch example.

import \* as t from 'io-ts'
import { Either, isRight } from 'fp-ts/lib/Either'

const Todo \= t.type({
  userId: t.number,
  id: t.number,
  title: t.string,
  completed: t.boolean
})

type Todo \= t.TypeOf<typeof Todo\>

function getTodo(id: number): Promise<Either<t.Errors, Todo\>> {
  return fetch(\`https://jsonplaceholder.typicode.com/todos/${id}\`)
    .then(response \=> response.json())
    .then(Todo.decode)
}

getTodo(1)
  .then(result \=> {
    // Success
    if (isRight(result)) {
      console.log(\`Todo: #${result.right.id}: ${result.right.title}\`)
    // Failure
    } else {
      console.error(result.left)
    }
  })
  .catch(e \=> console.error(e))

At a glance, the structure of this example resembles the `Result` version of the `runtypes` example. Same guarantees, no type-related exceptions. Even the way I defined the Todo record is very similar to previous work.

* * *

### More great articles from LogRocket:

*   [Learn how LogRocket's Galileo AI](https://logrocket.com/products/galileo-ai) watches user sessions for you, proactively surfaces the most impactful issues, and gives you the context to fix them
*   [See how Meilisearch](https://blog.logrocket.com/meilisearch-logrocket-mcp/) improved free trial experience and feature adoption with LogRocket's MCP
*   Keep up with which AI frontend dev tech reigns supreme with our [AI dev tool power rankings & comparison](https://blog.logrocket.com/ai-dev-tool-power-rankings/)
*   [Check out the CSS features](https://blog.logrocket.com/switching-between-node-versions-during-development/) currently shaping frontend development
*   These [10 React Native UI libraries](https://blog.logrocket.com/creating-custom-mouse-cursor-css/) could speed up development and polish your design
*   Which AI CLI tool should you use? [This comparison could help you decide](https://blog.logrocket.com/tested-5-ai-cli-tools/)

* * *

Notice the `fp-ts` import? It’s a collection of common data types from the world of functional programming. `io-ts` builds upon it. There’s an [ecosystem of libraries](https://gcanti.github.io/fp-ts/introduction/ecosystem) that share the core types. If you take the time to understand concepts like [Task](https://gcanti.github.io/fp-ts/modules/Task.ts) in relation to what folks normally use with TypeScript (Promises), you can learn advanced functional programming in the context of a familiar language. To truly immerse yourself in functional programming, I recommend that you at least try Elm.

The `Result`\-like `Either` type is split into the left and right sides. By convention, the left side denotes an error, and the right side denotes a valid value. If this naming convention seems hard to remember, I don’t blame you; I prefer the naming in `Result` myself. You can remind yourself by saying to yourself, “Seems like I have the `Right` data.” The type definition is as follows.

interface Left<E\> {
  readonly \_tag: 'Left'
  readonly left: E
}

interface Right<A\> {
  readonly \_tag: 'Right'
  readonly right: A
}

type Either<E, A\> \= Left<E\> | Right<A\>

There are some benefits of `runtypes`‘ `Result`. The `E` value on left side allows other representations for errors than just strings — remember `message`s? Having strings instead of booleans as tags makes it more compatible with other [tagged unions](https://mariusschulz.com/blog/tagged-union-types-in-typescript) (strings allow more than two possible values in a union).

So far, the only tangible benefits of using `io-ts` over `runtypes` seems to be related to naming and compatibility. Other benefits become apparent if we take a step back and use our validated data as part of a chain of operations. Forget about the to-do app — the next example has actual business logic.

I want to print out a receipt like this from the summary of a purchase:

Receipt
\========
Date: 2019\-12\-01T12:21:28.478Z
Total: 12.80€
Tax: 3.07€

Once I am comfortable with the data types of `fp-ts` and their operations, the app comes naturally.

import \* as t from 'io-ts'
import { map, fold } from 'fp-ts/lib/Either'
import { fold as foldMonoid, monoidSum } from 'fp-ts/lib/Monoid'
import { map as mapArray } from 'fp-ts/lib/Array'
import { pipe } from 'fp-ts/lib/pipeable'

const Purchase \= t.type({
  vat: t.number,
  items: t.array(
    t.type({
      name: t.string,
      amount: t.number,
      priceEur: t.number
    })
  )
})

const Receipt \= t.type({
  date: t.string,
  totalEur: t.number,
  taxEur: t.number
})

type Purchase \= t.TypeOf<typeof Purchase\>
type Receipt \= t.TypeOf<typeof Receipt\>

const data: unknown \= {
  vat: 24,
  items: \[
    { name: 'banana', amount: 3, priceEur: 0.7 },
    { name: 'coffee', amount: 1, priceEur: 3.5 },
    { name: 'beer', amount: 6, priceEur: 1.2 }
  \]
}

function purchaseToReceipt(purchase: Purchase): Receipt {
  const total \= pipe(
    purchase.items,
    mapArray(item \=> item.amount \* item.priceEur),
    foldMonoid(monoidSum)
  )

  return {
    date: new Date().toISOString(),
    totalEur: total,
    taxEur: (purchase.vat / 100) \* total
  }
}

function formatReceipt(receipt: Receipt): string {
  return \`
Receipt
========
Date: ${receipt.date}
Total: ${receipt.totalEur.toFixed(2)}€
Tax: ${receipt.taxEur.toFixed(2)}€
          \`
}

function formatErrors(errors: t.Errors): string {
  return \`Invalid data: ${JSON.stringify(errors)}\`
}

const summary: string \= pipe(
  Purchase.decode(data),
  // "map" only changes the "Right" value and keeps Left intact
  map(purchaseToReceipt),
  // Apply a certain function to left and right values (if present)
  fold(formatErrors, formatReceipt)
)

console.log(summary)

What’s so great about using a functional approach? See the `pipe`lines I’ve built? As long as the return value of an operation is a valid parameter to the next, the operations compose. Since values with types like `Either` are structurally the same, they can be transformed using common functions. There are two transformation pipelines:

1.  Calculating a sum of items’ prices (`purchaseToReceipt`)
2.  Transforming unknown `data` into a summary string

You are probably familiar with how good ol’ `Array`s can be transformed with operations like `items.filter(fn)`. Those are operations bound to an array instance. Here, you can use values from anywhere and compose them as you like.

I’ve only scratched the surface of what you can do with the `fp-ts` family. If this felt like your thing, go ahead and build your own apps using (only) these new concepts. You can also try the example in [CodeSandbox](https://codesandbox.io/s/dw1me?fontsize=14&hidenavigation=1&theme=dark). Now let’s wrap up what we have done during this journey.

## Plug: identify and eliminate runtime errors in production

Tracking down the cause of a production TypeScript exception or error is time consuming and frustrating. If you’re interested in monitoring errors and seeing how they affect users, [try LogRocket](https://logrocket.com/signup/).[![LogRocket Dashboard Free Trial Banner](https://blog.logrocket.com/wp-content/uploads/2019/10/errors-screenshot.png)](https://logrocket.com/signup/)[https://logrocket.com/signup/](https://logrocket.com/signup/)

[LogRocket](https://logrocket.com/signup/) is like a DVR for web apps, recording literally everything that happens on your site. LogRocket enables you to aggregate and report on errors to see how frequent they occur and how much of your user base they affect. You can easily replay specific user sessions where an error took place to see what a user did that led to the bug.

LogRocket instruments your app to record requests/responses with headers + bodies along with contextual information about the user to get a full picture of an issue. It also records the HTML and CSS on the page, recreating pixel-perfect videos of even the most complex single-page apps.

Enhance your JavaScript error monitoring capabilities – – [Start monitoring for free](https://logrocket.com/signup/).

## Conclusion

We started by discussing runtime exceptions and building a working but unreliable static site generator. We added `runtypes` definitions to the generator and had it stop early if the configuration was off.

Then we moved into the frontend and tried to fetch some to-dos. We noticed that runtime type checking helps to recognize differences between our expectations and API responses. Our app was still throwing exceptions around, so we tried a different way using errors as data: `Result`s.

We then compared `runtypes` to `io-ts` to see if this `Result` thing was any good (under the name `Either`). Once it seemed like there was a good reason to use this two-sided pattern, we explored how things look if we immerse ourselves in the `fp-ts` ecosystem. Functional programming had a chance to show its strength in a receipt generating script. We applied operations on the the results of other operations in a clear way.

Which one of these different flavors of runtime type checking should you use? It depends on what kind of application you are building. A simple top-down script might be fine if it just crashes when an exception is thrown. A long-running app, such as a mobile app, might benefit from recovering from exceptions or, better yet, work with errors as data. Catching exceptions and working with errors gives you the freedom to choose whether you need a user interaction or should retry the thing that just failed. Some minor things can even be ignored in a controlled fashion. In any case, you’ll likely end up with a more reliable app.

I have focused on validating completely external data. Apps create data from user input too. A TypeScript-based form library such as [Formik](https://jaredpalmer.com/formik) understands your interfaces. It can help you handle possible errors that stem from unreliable user input. This is different from API calls because the application determines how the data is gathered. You can use `runtypes` and `io-ts` for form validation using either [constraints](https://github.com/pelotom/runtypes#constraint-checking) or [encoders](https://github.com/gcanti/io-ts#the-idea). It might be more ergonomic to use whatever the form library uses. Formik uses [yup](https://github.com/jquense/yup).

In addition to input and output, apps often have internal state of a UI. You can validate your app’s logic by using a state machine. State machines define controlled runtime state transitions and document your intention. They can also trigger side-effects. See: [XState](https://github.com/davidkpiano/xstate), written in TypeScript.

## LogRocket understands everything users do in your web and mobile apps.

[![LogRocket Dashboard Free Trial Banner](https://blog.logrocket.com/wp-content/uploads/2017/03/1d0cd-1s_rmyo6nbrasp-xtvbaxfg.png)](https://logrocket.com/)

[LogRocket](https://logrocket.com/) lets you replay user sessions, eliminating guesswork by showing exactly what users experienced. It captures console logs, errors, network requests, and pixel-perfect DOM recordings — compatible with all frameworks, and with plugins to log additional context from Redux, Vuex, and @ngrx/store.

With Galileo AI, you can instantly identify and explain user struggles with automated monitoring of your entire product experience.

Modernize how you understand your web and mobile apps — [start monitoring for free](https://logrocket.com/).
