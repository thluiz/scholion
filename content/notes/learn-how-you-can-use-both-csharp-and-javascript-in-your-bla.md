---
title: "Learn how YOU can use both C# and JavaScript in your Blazor app with the JavaScript interop"
date: '2020-02-22T12:12:02+00:00'
category: webclip
summary: 'Explains how Blazor uses JavaScript interop through IJSRuntime to call JavaScript from C#, pass primitive and array parameters, and wrap NPM code in a bundle for use in a Blazor app.'
tags: ["blazor", "javascript-interop", "ijsruntime", "npm"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Learn how YOU can use both C# and JavaScript in your Blazor app with the JavaScript interop"
    url: "https://dev.to/dotnet/blazor-learn-to-get-the-best-of-both-worlds-with-javascript-interop-58pp"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--learn-how-you-can-use-both-csharp-and-javascript-in-your-bla.md"
    kind: repo
---

The article argues that Blazor should not be treated as a way to avoid JavaScript altogether. It presents JavaScript interop as a practical way to combine .NET APIs with the JavaScript ecosystem when the goal is to solve a client problem quickly and use existing browser capabilities or libraries.

It shows how to call JavaScript from a Blazor component or from a C# class through `IJSRuntime.InvokeAsync<T>()`, how parameters are serialized to JSON, and how to use the same approach with arrays. It also describes loading an NPM library, bundling a subset of Lodash with Browserify, exposing the function on `window`, and calling it from Blazor.

## Reading notes

- Blazor is presented as a way to use .NET APIs and the JavaScript ecosystem together.
- The article focuses on JavaScript interop as a skill for calling JavaScript code from Blazor.
- `IJSRuntime` and `InvokeAsync<T>()` are the main API used to run JavaScript methods.
- The JavaScript function name and JSON-serialized arguments are passed to `InvokeAsync<T>()`.
- JavaScript interop can be used from a component with `@inject IJSRuntime JSRuntime`.
- It can also be injected into a C# class through the constructor.
- The demo creates a Blazor project, adds a `library.js` file under `wwwroot`, and references it from `index.html`.
- A simple `add(lhs, rhs)` JavaScript function is called from a Blazor component.
- The component uses `await` and an `async` handler to wait for the JavaScript result.
- The same pattern is shown with arrays passed to a `commonElements(arr1, arr2)` function.
- The article says primitives and arrays work similarly because values are serialized to JSON on the .NET side and deserialized in JavaScript.
- It then shows how to use an NPM library by creating an `npm-libs` directory and initializing it with `npm init -y`.
- `lodash` is installed, `browserify` is used to bundle code, and the build command is added to `package.json`.
- The bundle imports only `lodash/fp/intersection` and exposes an `intersect` function on `window`.
- The Blazor component calls that bundled JavaScript through `JSRuntime.InvokeAsync<string>()`.
- The summary says the approach is useful for occasional JavaScript calls and for reusing existing libraries instead of rewriting them.
