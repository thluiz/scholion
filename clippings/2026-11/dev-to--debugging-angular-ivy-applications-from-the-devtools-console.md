---
url: "https://dev.to/angular/debugging-angular-ivy-applications-from-the-devtools-console-415j"
captured_at: "2026-11-16T00:57:25+00:00"
title: "Debugging Angular Ivy Applications from the Devtools Console"
domain: "dev-to"
---

[![Cover image for Debugging Angular Ivy Applications from the Devtools Console](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fjuristr.com%2Fblog%2Fassets%2Fimgs%2Fdebugging-ivy-bg.jpg)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fjuristr.com%2Fblog%2Fassets%2Fimgs%2Fdebugging-ivy-bg.jpg)

[![Angular profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Forganization%2Fprofile_image%2F802%2F39aa2792-6183-496a-8513-1a38c76dbfb6.png)](https://dev.to/angular) [![Juri Strumpflohner](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F149479%2F2951f479-1bfc-45de-8fdd-46eca0930856.JPG)](https://dev.to/juristr)

_This post has originally been published on [https://juristr.com/blog/2019/09/debugging-angular-ivy-console](https://juristr.com/blog/2019/09/debugging-angular-ivy-console). Go to [juristr.com/blog](https://juristr.com/blog) for more content_

* * *

Do you remember how in AngularJS (v1.x) we could easily debug/change the state of our components from the browser's devtools. Guess what: now with Ivy a new easy API returns that openes up a variety of new ways. Let's see how that works.

Do you remember the good old AngularJS days 😉, where you could simply write...  

```
> angular.element($0).scope()
```

Enter fullscreen mode Exit fullscreen mode

...to your browser's devtools console and get access to the scope of your component to manipulate and inspect it? About 3 years ago (man time passes by), I wrote a blog post about [Debugging Angular Applications](https://juristr.com/blog/2016/02/debugging-angular2-console/). It highlighted how you could easily inspect the component state from the browser devtools console with AngularJS and how that changed with the early versions of Angular (2+). In fact starting from the early versions of Angular 2+ the `ng.probe` API has been introduced to allow you to interact with the component state from your console.

> "Ivy is an enabler" Igor Minar

With Ivy new APIs have been added to the global `ng` object. If you open up your devtools (i.e. Chrome's Devtools) and type `ng`, you'll see something like this:

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fjuristr.com%2Fblog%2Fassets%2Fimgs%2Fivydebug-ng-api.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fjuristr.com%2Fblog%2Fassets%2Fimgs%2Fivydebug-ng-api.png)

What we can do now is to go to the "Elements" panel in the devtools and choose for instance the `<mat-drawer>` component (which comes from [Angular Material](https://material.angular.io/components/sidenav/overview)).

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fjuristr.com%2Fblog%2Fassets%2Fimgs%2Fivydebug-select-item-inspect.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fjuristr.com%2Fblog%2Fassets%2Fimgs%2Fivydebug-select-item-inspect.png)

When you click on an element, you then have it at disposal as `$0` in the devtools console (`$1` the second last, `$2` the third last etc..you get the idea). We can now use the `ng.getComponent(...)` and directly pass it the DOM tag we've selected previously, basically `$0`. We can store the component in a variable and then start to interact with it.

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fjuristr.com%2Fblog%2Fassets%2Fimgs%2Fivydebug-matdrawer-instance.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fjuristr.com%2Fblog%2Fassets%2Fimgs%2Fivydebug-matdrawer-instance.png)

For instance let's invoke the `toggle()` function of the `<mat-drawer>` to close the side menu.

(check [out the vid in the original post](https://juristr.com/blog/2019/09/debugging-angular-ivy-console))

The commands executed are:  

```
// grab the component instance of the DOM element stored in $0
let matDrawer = ng.getComponent($0);

// interact with the component's API
matDrawer.toggle();

// trigger change detection on the component
ng.markDirty(matDrawer);
```

Enter fullscreen mode Exit fullscreen mode

## [](#whats-happening-to-the-raw-ngprobe-endraw-api)What's happening to the `ng.probe` API?

It most probably won't be supported by Ivy

> In Ivy, we don't support NgProbe because we have our own set of testing utilities with more robust functionality. We shouldn't bring in NgProbe because it prevents DebugNode and friends from tree-shaking properly.

[More details here](https://github.com/angular/angular/blob/master/packages/platform-browser/src/dom/debug/ng_probe.ts#L40-L47).

## [](#conclusion)Conclusion

This new API allows us to quickly interact with components and test out things without having to go back and forth between our editor and browser. But even more, new devtools extensions can be developed on top of these APIs to facilitate our lifes even more. For instance, if you take a look at the components, they have a `__ngContext__` attached which has a `debug` object with lots of interesting methods to query the component and it's template properties. Note however, these APIs (or some of them) are only available in development mode and will be compiled away in production mode.
