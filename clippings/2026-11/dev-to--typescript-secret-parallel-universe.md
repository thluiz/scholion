---
url: "https://dev.to/loilo/typescript-s-secret-parallel-universe-54i6"
captured_at: "2026-11-16T00:47:43+00:00"
title: "TypeScript's Secret Parallel Universe"
domain: "dev-to"
---

Almost four years ago, I was a new TypeScript user, amazed by the possibilities that this freshly learned JavaScript dialect opened up to me. But just like every TypeScript developer, I soon ran into some hard-to-debug problems.

![Animation showing a set of virtual switches labelled with ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0f9aovsuypypb0hz6tfj.gif)

In TypeScript land, those problems usually stem from the programmer's lack of understanding about the language itself.

* * *

I'd like to introduce you to one of these early problems I had, mostly because it is related to one of the (in my opinion) most underreported topics in the TypeScript tutorial world: the type scope. It's kind of obvious once you realize it exists, but for me it was a frequent source of confusion when I didn't know about it.

## [](#the-problem)The Problem

My problem was actually very simple: I was building a library with a bunch of classes distributed over various folders.

[![The Visual Studio Code file tree showing three TypeScript files (Console.ts, File.ts and Stream.ts) in a folder named ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2ea1ykc8q3z4tlthuinp.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2ea1ykc8q3z4tlthuinp.jpg)

For the library's public API, I wanted those classes to be exposed as a single nested object (e.g. the `Console` class from `Output/Console.ts` being available as `API.Output.Console`).

So I defined some [namespaces](https://www.typescriptlang.org/docs/handbook/namespaces.html#namespaced-validators), imported the classes — and then I struggled. I was just not able to re-export the classes from inside the namespaces. 🤨

* * *

First attempt, turned out to be invalid TypeScript:  

```
import Console from './Output/Console'

export namespace Output {
  export Console
  // TS Error 1128: Declaration or statement expected.
}
```

Enter fullscreen mode Exit fullscreen mode

Maybe I need to import it under a different name. Okay, second attempt:  

```
import ConsoleAlias from './Output/Console'

export namespace Output {
  export Console = ConsoleAlias
  // TS Error 2304: Cannot find name 'Console'.
}
```

Enter fullscreen mode Exit fullscreen mode

Third attempt — maybe doing it the ES Modules way cuts it. (Spoiler: It didn't.)  

```
import ConsoleAlias from './Output/Console'

export namespace Output {
  export { ConsoleAlias as Console }
  //TS Error 1194: Export declarations are not permitted in a namespace.
}
```

Enter fullscreen mode Exit fullscreen mode

Fourth attempt using `export const`. This actually compiled. 🎉  

```
import ConsoleAlias from './Output/Console'

export namespace Output {
  export const Console = ConsoleAlias
}
```

Enter fullscreen mode Exit fullscreen mode

But unfortunately, whenever I wanted to type hint something with that `API` object, I got the following error:  

```
import * as API from './API'

let console: API.Output.Console
// TS Error 2694: Namespace 'API.Output' has no exported member 'Console'.
```

Enter fullscreen mode Exit fullscreen mode

...but I exported that member! Why is it not there!?

Hum. Maybe the `export const` is the problem. I should sprinkle some magic TypeScript keywords over the problem and try `export type` instead.

So without further ado: Fifth attempt. It compiles! 🥳  

```
import ConsoleAlias from './Output/Console'

export namespace Output {
  export type Console = ConsoleAlias
}
```

Enter fullscreen mode Exit fullscreen mode

Okay, reality check: Does the type hint work? It does! 🕺

...but that joy was short-lived as well. When I tried to create a new `Console` instance, TypeScript errors were all over me again:  

```
import * as API from './API'

const console = new API.Output.Console()
// TS Error 2708: Cannot use namespace 'API' as a value.
```

Enter fullscreen mode Exit fullscreen mode

Oh come on.

Needless to say that I was pretty fed up with TypeScript at that point.

[![Video of a man throwing his computer into the dumpster](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3exdf7uzpm7zkfjxlzyb.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3exdf7uzpm7zkfjxlzyb.gif)

However, I did not want to believe that there was no solution to my problem, so I went to [StackOverflow](https://stackoverflow.com/questions/38655711/export-a-typescript-class-from-another-file-than-it-has-been-defined-in) and, after a couple of days with no answer, I created [an issue](https://github.com/microsoft/TypeScript/issues/10058) directly in TypeScript's GitHub repository.

## [](#the-solution)The Solution

[Ryan](https://twitter.com/SeaRyanC) from the TypeScript team was kind enough to answer my question just within a couple of minutes. To me, the solution seemed pretty obvious and pretty obscure at the same time:

[![Screenshot of Ryan Cavanaugh's answer to my question on GitHub, stating that I should be using both ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9ewtf60gp9rdd64x3sup.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9ewtf60gp9rdd64x3sup.jpg)

I applied that approach — and it worked like a charm.

## [](#why-it-works)Why It Works

Back then, I just accepted that answer and used it in my code. It sounded kind of plausible to me — both, `const` and `type`, worked in some way, so I just need to combine them to make both use cases working. But there was a sense of unease in it. Why could I export two things under the same name without producing a big fat compiler error?

It took me some more months (maybe even years) of TypeScript experience to fully understand why this works, but I think that insight might be valuable for others as well, so I'll share it here:

**TypeScript has a secret [scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope).**

TypeScript basically maintains a type scope which is completely independent of the variable scope of JavaScript. This means that you may declare a variable `foo` and a type `foo` _in the same file_. 🤯 They don't even need to be compatible:  

```
const foo = 'bar'
type foo = number

// ✅ This is absolutely fine for TypeScript
```

Enter fullscreen mode Exit fullscreen mode

Now classes in TypeScript are a little bit special. What happens if you define a class `Foo` is that TypeScript not only creates a variable `Foo` (containing the class object itself) it _also declares a type `Foo`_, representing an instance of the `Foo` class.  

```
class Foo {}

// We can use Foo as a type
let foo: Foo

// We can use Foo as a constructor (i.e. a value)
const bar = new Foo()
```

Enter fullscreen mode Exit fullscreen mode

Similarly, when importing a name from another file (like we do with `ConsoleAlias` in the second code sample), both — the `ConsoleAlias` class object and the `ConsoleAlias` type — are imported.

In other words, that single name — the imported `ConsoleAlias` — holds both the class object and the type declared in `Output/Console.ts`.

So if we re-export `Console` from inside the `Output` namespace by writing `export const Console = ConsoleAlias`, only the class _object_ is exported (because a `const` only ever holds a value, not a type). Similarly, if we'd do `export type Console = ConsoleAlias`, only the class _type_ would be exported.

In a nutshell: Because of the independent scopes, it's valid to export a value as well as a type under the same name. And in some cases (like the one above), this is not only valid but necessary.

* * *

I hope this helped refine your mental model of TypeScript. 🤓
