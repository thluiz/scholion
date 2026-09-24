---
url: "https://dev.to/rionmonster/secret-productivity-tips-for-visual-studio-2017"
captured_at: "2026-09-25T00:50:18+01:00"
title: "Secret Productivity Tips for Visual Studio 2017"
domain: "dev-to"
---

_This was originally posted on [my blog](http://rion.io/)._

I've written a few blog posts thus far regarding Visual Studio 2017, so I thought I would take some time to discuss of the features that were introduced in this latest version that might help your productivity, or that you just may find useful.

You'll notice that the title of this post mentions that they are "secret". This is because **all of these features are disabled by default**, so you'll need to enable them, either locally (per project) or globally, to take advantage.

## [](#nuget-package-suggestion-for-unrecognized-types)NuGet Package Suggestion for Unrecognized Types

[![automatically import from nuget](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Flisynn6qnlw7bgv1l33x.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Flisynn6qnlw7bgv1l33x.gif)

In my opinion, one of the most useful additions to Visual Studio 2017 was the Nuget-based Using Suggestion feature. This feature will recommend installing a specific NuGet package to handle resolving an unrecognized type that is encountered within the editor.

It can be enabled via:

*   **Tools > Options > Text Editor > C# > Advanced > Suggest Usings for Types in Nuget Packages**

Again - a great feature to speed up your productivity and it sure beats wandering around NuGet or running off to manually download the packages.

## [](#query-syntax-in-go-to-all-ctrlt)Query Syntax in Go To All (Ctrl+T)

[![filtering query syntax](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fwgidy6i5wyt31xuxmkbs.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fwgidy6i5wyt31xuxmkbs.gif)

Another incredibly useful tool introduced within Visual Studio 2017 was query searching within the Go To All (Ctrl+T) search area. This allows you to now quickly search for any file / type / member / or symbol by prefacing your search using the following prefixes:

*   **f {file}**
    
*   **t {type}**
    
*   **m {member}**
    
*   **\# {symbol}**
    

This can allow you to easily narrow your search within your solution and find exactly what you need fast.

## [](#full-solution-analysis)Full Solution Analysis

[![errors, messages, and warnings for the entire solution](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2F6utmlypovbjd61j0doe7.PNG)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2F6utmlypovbjd61j0doe7.PNG)

The Full Solution Analysis feature is one that could be helpful to see every error, message, and warning throughout your entire solution (and not just the files that are currently open).

This feature can be enabled via:

*   **Tools > Options > Text Editor > C# > Advanced > Enable Full Solution Analysis**

If you are a stickler that can't stand seeing a non-empty Error List, then this is for you.

#### [](#lightweight-solution-load)Lightweight Solution Load

[![loading projects on demand](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fxkimuri8hwl70gln6v4t.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fxkimuri8hwl70gln6v4t.gif)

Another great feature that can add quite a bit of zing to Visual Studio 2017 is Lightweight Solution Load. This feature will initially load the _minimal_ amount necessary for each project to have them functional within Visual Studio. Individual project files and dependencies will not be loaded or expanded until requested, so you only load what you will need.

This feature can be enabled in two ways; locally:

*   **Right-click Project > Enable Lightweight Solution Load**

Or globally (for all projects):

*   **Tools > Options > Projects and Solutions > General > Lightweight Solution Load**

It's great for large solutions with multiple projects that maybe aren't all going to be touched for most scenarios or just if you just want Visual Studio to open up a project faster than normal.

## [](#live-unit-testing)Live Unit Testing

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Frxi29qsvml8msj7zaojj.PNG)](https://channel9.msdn.com/Events/Connect/2016/171/player)

Live Unit Testing was one of the features that was touted during the release of Visual Studio 2017, but it isn't actually enabled by default. This feature will figure out which unit tests are affected by any code changes and the tests will be automatically run. Additionally, it will decorate your code using icons to indicate which code is covered and the status of the test covering that code.

This feature can be enabled in two ways; locally:

*   **Test > Live Unit Testing > Start**

Or globally (for all projects):

*   **Options > Live Unit Testing**

Live Unit Testing is super handy for not only seeing what tests are passing and failing, but for examining code coverage as well. This feature is also highly configurable and will allow you to include / exclude specific tests, define the number of threads you want to dedicate to it, configure when the tests are run, and much more.

## [](#editorconfig-style-enforcement)EditorConfig Style Enforcement

[![update-editor-styles](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2F90dhch671o6cf74pl7b6.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2F90dhch671o6cf74pl7b6.gif)

Visual Studio 2017 adds support for [.editorconfig](http://editorconfig.org/) files within projects to help provide coding style recommendations, which can be useful for large development teams looking to maintain a consistent style across their code base.

You may notice that the ellipses can be incredibly difficult to notice, especially if you are on the dark side. This can easily be adjusted within the IDE to make them far more visible from:

*   **Tools > Options > Environment > Fonts and Colors > Suggestion Ellipsis**

You can then configure the color to make it "pop" out a bit more :

[![styled suggestions](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fx9q9t1dzr3743cxmle0s.PNG)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Fx9q9t1dzr3743cxmle0s.PNG)

While this feature _is_ enabled by default (if an .editorconfig file is present), you can make the process of editing it much easier through Mads Kristensen's [EditorConfig extension](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.EditorConfig), which can be downloaded and will provide full autocompletion, syntax highlighting, and much more.

## [](#keyboard-shortcuts)Keyboard Shortcuts

With many of the new additions and features that were added to Visual Studio 2017, you might be inclined to consider dropping support for the heavyweight Resharper extension to see how vanilla Visual Studio works at this point. Or if you are a developer coming from another editor such as IntelliJ, Eclipse, you are probably pretty accustomed to the keyboard shortcuts from those tools. Well, there's an extension that has you covered.

[Justin Clarebert](https://twitter.com/justcla78), a member of the Visual Studio team released the [HotKeys Keyboard Shortcuts extension](https://marketplace.visualstudio.com/items?itemName=JustinClareburtMSFT.HotKeys2017-KeyboardShortcuts), which allows you to easily configure Visual Studio 2017 to use the keyboard shortcuts from those other popular editors and tools, giving you the productivity you are accustomed to within a new environment.

Okay. So this is another feature that _isn't_ directly built in to Visual Studio 2017, but it's too big of a productivity enhancer to leave off this list (and since it's not built it, I suppose it still qualifies as a "secret").

## [](#in-closing)In Closing

Hopefully, this list introduced you to a few features that you may have not been aware of within Visual Studio 2017 (and if you were, hopefully it showed you how to go about enabling it).
