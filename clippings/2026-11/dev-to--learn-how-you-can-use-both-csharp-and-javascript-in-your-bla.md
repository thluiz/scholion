---
url: "https://dev.to/dotnet/blazor-learn-to-get-the-best-of-both-worlds-with-javascript-interop-58pp"
captured_at: "2026-11-16T00:59:08+00:00"
title: "Learn how YOU can use both C# and JavaScript in your Blazor app with the JavaScript interop"
domain: "dev-to"
---

Follow me on [Twitter](https://twitter.com/chris_noring), happy to take your suggestions on topics or improvements /Chris

> Blazor is the new framework from Microsoft that will make it possible to build applications for the Web using nothing but C#. It's easy at first look to think - Great I don't need to learn JavaScript. To be honest, I think this is the wrong way to look at it. Having a huge ecosystem of libraries written in JavaScript is an opportunity. At the end of the day, it's about solving the client's problem and doing so in a fast and efficient way. With Blazor we know have the opportunity to use the best of two worlds. The .NET Apis and the JavaScript ecosystem.

TLDR; This article will show how to use something called the JavaScript interop which allows us to call JavaScript code from Blazor. Learn to be the developer that leverages two powerful ecosystems .NET APIs and the JavaScript ecosystem.

In this article, we assume that you as a reader knows what Blazor is. It's recommended that if you are completely new to Blazor you first have a read through this introductory article:  

## [](#%C2%A0references) References

*   [JavaScript and Blazor doc](https://docs.microsoft.com/aspnet/core/blazor/javascript-interop?view=aspnetcore-3.0?wt.mc_id=devto-blog-chnoring)  
    This link describes everything this article has gone through but also covers how you would from JavaScript call your Blazor component and additionally it talks about lifecycles
    
*   [Introduction to Blazor doc](https://docs.microsoft.com/aspnet/core/blazor/?view=aspnetcore-3.0?wt.mc_id=devto-blog-chnoring)  
    This is a good introduction page to Blazor
    
*   [Introduction to Razor templating with Blazor](https://docs.microsoft.com/aspnet/core/mvc/views/razor?view=aspnetcore-3.0?wt.mc_id=devto-blog-chnoring)  
    New to Razor templating and especially what tags exist in Blazor? Then this page is for you
    
*   [Part one on Blazor, start here if you don't know anything about Blazor](https://docs.microsoft.com/aspnet/core/host-and-deploy/?view=aspnetcore-3.0?wt.mc_id=devto-blog-chnoring)  
    Want to know how to deploy your Blazor app? This goes through both a server hosted Blazor app as well as a WebAssembly version
    

## [](#why)WHY

As we mentioned at the beginning of this article. In my opinion, it's not good to limit ourselves to only use the .NET APIs. At the end of the day, it's about getting the job done. For that reason learning how to execute JavaScript from within Blazor is a skill worth having, especially if it means that we can leverage other existing libraries from for example NPM. Another reason for wanting to execute JavaScript from within Blazor might be that we need to use a specific Browser capability.

## [](#%C2%A0what) WHAT

This article covers something called the JavaScript interop. At our disposal, we have an abstraction called `IJSRuntime` and on it, we execute the method `InvokeAsync<T>()`. The method expects the name of the function you want to execute and a list of serialized JSON parameters. A typical call looks something like this:  

```
var result = await JSRuntime.InvokeAsync<string>("methodName", input);
```

Enter fullscreen mode Exit fullscreen mode

What happens in the above code is that the method `methodName()` is being invoked and the parameter `input` is being turned into a string.

### [](#different-ways-to-use-the-raw-ijsruntime-endraw-)Different ways to use the `IJSRuntime`

You can call the JavaScript interop from different places. Either:

*   **From the component**, If you want to use it from within a component you just need an inject statement at the top of the component like so:

```
@inject IJSRuntime JSRuntime
```

Enter fullscreen mode Exit fullscreen mode

*   **From the a C# class**, if you want to use the interop from within a class you need to inject it into the class's constructor like so:

```
class Something 
{
  Something(IJSRuntime jsRuntime) 
  {

  }
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#%C2%A0demo) DEMO

Ok, so what are we building? Well, let's do the following:

*   **Scaffold** a project, we need to create a Blazor project. We can do that from the command line
*   **Invoke** javascript functions, we will create a Blazor component where we will add some code to showcase different ways of calling the JavaScript code using the interop functionality.
*   **Download** and use a library from NPM, we will leverage the NPM ecosystem by downloading an NPM library and call that from our Blazor Component

### [](#scaffold-a-project)Scaffold a project

As Blazor is constantly updated, ensure you are looking at the latest instructions for installing it:

> [https://docs.microsoft.com/en-us/aspnet/core/blazor/get-started?view=aspnetcore-3.1&tabs=visual-studio](https://docs.microsoft.com/en-us/aspnet/core/blazor/get-started?view=aspnetcore-3.1&tabs=visual-studio)

There are two things that needs to be installed for us to be able to create a Blazor project:

1.  Blazor templates, we can easily install these from the command line with the command
2.  .NET Core, latest and greatest

You need to download .Net Core 3.0. Check out this link to find the correct distribution for your OS

> [https://dotnet.microsoft.com/download/dotnet-core/3.0](https://dotnet.microsoft.com/download/dotnet-core/3.0)

You want to be picking the latest and greatest on the above page cause it will give you the latest features of Blazor and usually Blazor templates rely on the latest possible version of .NET Core.

Additionally, you need templates so you can scaffold a Blazor app. Pop open a terminal and type  

```
dotnet new -i Microsoft.AspNetCore.Blazor.Templates::3.1.0-preview2.19528.8
```

Enter fullscreen mode Exit fullscreen mode

### [](#invoke-javascript-functions)Invoke JavaScript functions

So the first question is, of course, how can we be calling JavaScript functions and with what? We know the first part of the answer. We should be using `IJSRuntime` and the method `InvokeAsync()`. Next, we need to know where to place our JavaScript?

The answer is inside of a script file and we need to refer to this script file by placing a `script` tag in the directory `wwwwroot` and the file `index.html`.  

```
-| wwwroot/
---| index.html
```

Enter fullscreen mode Exit fullscreen mode

Let's say then that we create a file `library.js` in `wwwroot` so we know have:  

```
-| wwwroot/
---| index.html
---| library.js
```

Enter fullscreen mode Exit fullscreen mode

Then we need to open up `index.html` and add our script tag like so:  

```
<!-- index.html -->
<script src="library.js"></script>
```

Enter fullscreen mode Exit fullscreen mode

What about the content of `library.js` then? Well here it is:  

```
// library.js

function add(lhs, rhs) {
  return lhs+rhs;
}
```

Enter fullscreen mode Exit fullscreen mode

At this point, let's go to our `Pages` directory and create a new component `Jsdemo.razor`, like so:  

```
-| Pages
---| Jsdemo.razor
```

Enter fullscreen mode Exit fullscreen mode

give it the following content:  

```
@page "/jsdemo"
@inject IJSRuntime JSRuntime

<h2>JS Demo</h2>
Result : @result

<button @onclick="Add">Add</button>

@code {
  int result = 0;

  public async void Add() 
  {
    result = await JSRuntime.InvokeAsync<int>("add",1,2);
  }
}
```

Enter fullscreen mode Exit fullscreen mode

There are many things that go on here:

1.  We call `JSRuntime.InvokeAsync<int>("add",1,2)`, with the first arg being `add`, the name of the function. Followed by `1,2`, which are the arguments to the function.
2.  Then we notice `<int>`, this sets up the return type of the function
3.  Looking at the full function:

```
public async void Add() 
{
  result = await JSRuntime.InvokeAsync<int>("add",1,2);
}
```

Enter fullscreen mode Exit fullscreen mode

we see that we call `await` to wait for the response, which also means we need to mark our `Add()` function with `async` to make the compiler happy.

### [](#an-example-with-more-complex-parameters)An example with more complex parameters

Ok, we want to ensure that it still works by invoking functions with parameters that are arrays and even objects.

Let's add two functions to our `library.js` and update it's content to the following:  

```
// library.js

function add(lhs, rhs) {
  return lhs+rhs;
}

function commonElements(arr1, arr2) {
  return arr1.filter(a => arr2.find(b => b === a)).join(',');
}
```

Enter fullscreen mode Exit fullscreen mode

So how to call it? Well, just like we did before using `JSRuntime.InvokeAsync<int>("name-of-method",arg...)`.

Let's go update our Blazor component `Jsdemo.razor` to this:  

```
@page "/jsdemo"
@inject IJSRuntime JSRuntime

<h2>JS Demo</h2>
Result : @result

Common elements result:
@stringResult

<button @onclick="Add">Add</button>
<button @onclick="Common">Common elements</button>

@code {
  int result = 0;
  string stringResult = "";
  int[] arr1 = new int [2]{1,2};
  int[] arr2 = new int [2]{2,3};

  public async Common() 
  {
    stringResult = await JSRuntime.InvokeAsync<string>("commonElements",arr1,arr2);
  }

  public async void Add() 
  {
    result = await JSRuntime.InvokeAsync<int>("add",1,2);
  }
}
```

Enter fullscreen mode Exit fullscreen mode

Note above how we add some markup for this new result:  

```
Common elements result:
@stringResult

<button @onclick="Common">Common elements</button>
```

Enter fullscreen mode Exit fullscreen mode

We also need to create some new input parameters, two arrays:  

```
int[] arr1 = new int [2]{1,2};
int[] arr2 = new int [2]{2,3};
```

Enter fullscreen mode Exit fullscreen mode

Lastly we add the method `Common()`, like so:  

```
public async Common() 
  {
    stringResult = await JSRuntime.InvokeAsync<int>("commonElements",1,2);
  }
```

Enter fullscreen mode Exit fullscreen mode

As you can see there is really no difference between having primitives our arrays as inputs. The main reason is that everything gets serialized to JSON on the .NET side and is de-serialized right back when the JavaScript function is being invoked.

### [](#%C2%A0calling-npm-code) Calling NPM code

Ok, so let's talk about using JavaScript libraries. After all one of the strengths of Blazor lies in the ability to use both ecosystems, both .NET and NPM. So how do we do that?

Well, we need to consider the following:

1.  Large libraries, some libraries are really big out there, like `Lodash`. Fortunately, there is a way to import only the functions we are going to need, the rest can be omitted through a process called _tree shaking_
2.  If we are using only a part of a library like the above scenario we need a way to extract the code we need, so we need a tool like `browserify` or `webpack` to create a bundle of a subset of code

Ok then, we understand what we need to consider. Now let's do just that, let's extract a function from the library `lodash`. Let's list the steps we need to take:

*   **Create** a directory where our bundle and downloaded libraries will live
*   **Download** the NPM library
*   **Set up** up a tool like `browserify` to make it possible to create bundle with an `NPM command`
*   **Create** the bundle with `browserify` and include the resulting bundle as a script tag
*   **Try out** code from our bundle

**Create**

Let's create a directory under `wwwroot` called `npm-libs`, you can call it what you want.

It should now looks like this:  

```
-| wwwroot
---| npm-libs/
```

Enter fullscreen mode Exit fullscreen mode

We will treat this is as a Node.js project and with Node.js projects you want to initialize it using `npm init`, like so:  

```
npm init -y 
```

Enter fullscreen mode Exit fullscreen mode

This will give us a nice Node.js project with some good defaults and most of all a `package.json` file.  

```
-| wwwroot
---| npm-libs/
------| package.json 
```

Enter fullscreen mode Exit fullscreen mode

We will use this `package.json` file as a manifest file that tells us about the libraries we need and commands we can use to build our bundle.

**Download**

Inside of our `npm-libs` we now run the `npm install` command to give us the library we want, in this case, `lodash`:  

```
npm install lodash
```

Enter fullscreen mode Exit fullscreen mode

This means that our file structure now contains a `node_modules` directory, with our downloaded library, like so:  

```
-| wwwroot
---| npm-libs/
------| package.json 
------| node_modules/
```

Enter fullscreen mode Exit fullscreen mode

**Set up**

Next, we need to install our bundling tool `browserify`:  

```
npm install -g browserify
```

Enter fullscreen mode Exit fullscreen mode

We are now ready to define a command to run `browserify`,it should look like so:  

```
browserify -d index.js > bundle.js
```

Enter fullscreen mode Exit fullscreen mode

The above will take the file `index.js`, walk the tree over all its dependencies and produce a bundle, that we call `bundle.js`. Note also how we include `-d`, this is for source maps. Source maps mean our modules will be remembered for how they looked prior to _bundling_. We should lose the `-d` when in production because the source maps makes the bundle bigger.

Let's put this command in the `scripts` section of `package.json` so we now have:  

```
"build": "browserify -d index.js > bundle.js"
```

Enter fullscreen mode Exit fullscreen mode

Ok then, the next step is to create our `index.js` like so:  

```
-| wwwroot
---| npm-libs/
------| index.js
------| package.json 
------| node_modules/
```

Enter fullscreen mode Exit fullscreen mode

and give it the following content:  

```
// index.js

var intersect = require('lodash/fp/intersection');

window.intersect = function(arg1, arg2) {
  let result = intersect(arg1, arg2);
  return result.join(',');
};
```

Enter fullscreen mode Exit fullscreen mode

What we are doing above is asking for a subset of `lodash` by only loading the function `intersection`:  

```
var intersect = require('lodash/fp/intersection');
```

Enter fullscreen mode Exit fullscreen mode

this means that when this _tree-shakes_, it will only include the `intersection` code and our bundle will be at a minimum.

Next, we assign the `intersection` function to the `window` property and expose it so our C# code can call it.  

```
window.intersect = function(arg1, arg2) {
  let result = intersect(arg1, arg2);
  return result.join(',');
};
```

Enter fullscreen mode Exit fullscreen mode

At this point we run:  

```
npm run build
```

Enter fullscreen mode Exit fullscreen mode

This should produce a `bundle.js`. We should also add a reference to our `bundle.js` in our `index.html` file, like so:  

```
<script src="bundle.js"></script>
```

Enter fullscreen mode Exit fullscreen mode

**Try it out**

Lastly, we want to call this JavaScript code from our Blazor component. So we add the following code to our `@code` section, like so:  

```
 public async void Intersect() 
  {
     intersectResult = await JSRuntime.InvokeAsync<string>("intersect",arr1, arr2);
     Console.WriteLine(intersectResult);
  }
```

Enter fullscreen mode Exit fullscreen mode

and the following to our markup:  

```
<button @onclick="Intersect">Intersect</button>

Intersect:
@intersectResult
```

Enter fullscreen mode Exit fullscreen mode

## [](#full-code-of-our-blazor-component)Full code of our Blazor component

Let's show the full code in case you got lost somewhere:  

```
@page "/jsdemo"
@inject IJSRuntime JSRuntime

<h2>JS Demo</h2>
Result : @result

<button @onclick="Click">Press</button>
<button @onclick="Add">Add</button>
<button @onclick="Intersect">Intersect</button>

Intersect:
@intersectResult

@code {
  int result = 0;
  string intersectResult = "replace me";

  int[] arr1 = new int [2]{1,2};
  int[] arr2 = new int [2]{2,3};

  public async void Intersect() 
  {
     intersectResult = await JSRuntime.InvokeAsync<string>("intersect",arr1, arr2);
     Console.WriteLine(intersectResult);
  }

  public async void Add() 
  {
    result = await JSRuntime.InvokeAsync<int>("add",1,2);
  }

  void Click() 
  {
    JSRuntime.InvokeAsync<string>("alert","hello");
  }
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#summary)Summary

And that's all, that's what we wanted to achieve. We tried out different ways of calling our code, with primitive parameters, without it. We even showed how we could download a JavaScript library from NPM and make that part of our project.

I hope this was educational and that you are helped for the following scenarios:

*   **Occasional usage**, Calling JavaScript code occasionally
*   **Leveraging existing libraries**, you might have existing libraries you've written and don't want to reinvent the wheel or maybe there's a library on NPM that just does what you want it to.
