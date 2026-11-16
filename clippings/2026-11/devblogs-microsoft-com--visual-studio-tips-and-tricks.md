---
url: "https://devblogs.microsoft.com/visualstudio/visual-studio-tips-and-tricks/"
captured_at: "2026-11-16T18:44:49+00:00"
title: "Visual Studio tips and tricks"
domain: "devblogs-microsoft-com"
---

June 25th, 2019

![heart](https://devblogs.microsoft.com/visualstudio/wp-content/themes/devblogs-evo/images/emojis/heart.svg)1 reaction

![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2021/09/Mads-glasses-square-96x96.jpg)

Principal Product Manager

Whether you are new or have been using Visual Studio for years, there are a bunch of tips and tricks that can make you more productive. We’ve been sharing tips on Twitter using the [#vstip hashtag](https://twitter.com/search?q=%23vstip) for a while, and this is a collection of the best ones so far.

## Debugger

**Hitting F10** to build, run, and attach debugger instead of F5 will automatically break on the first time your own code is being executed. No breakpoints needed.

Supported from Visual Studio 2005

**Reattach to process** (Shift+Alt+P) is extremely helpful when you have to attach to the same process again and again.

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/debug-reattach.png)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/debug-reattach.png)

Supported from Visual Studio 2017 v15.8

**A blue dot in the margin** indicates a switch of threads while stepping through debugging.

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/debug-blue-dot.jpg)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/debug-blue-dot.jpg)

Supported from Visual Studio 2013

## Solution

Improve performance of solution load and reduce visual noise by **disabling restore of node expansions** in Solution Explorer as well as **Reopen documents on solution load**.

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/perf-restore-hierarchy.jpg)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/perf-restore-hierarchy.jpg)

Supported from Visual Studio 2019

For fast keyboard navigation, use **Ctrl+T to find anything in your solution** – files, classes etc.

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/go-to-all.jpg)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/go-to-all.jpg)

Supported from Visual Studio 2017

**Assign a keyboard shortcut to perform a “git pull”** so you don’t have to use CLI or Team Explorer to ensure your repo is up to date.

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/git-pull.png)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/git-pull.png)

Supported in Visual Studio 2019

**Make Solution Explorer automatically select the current active document**, so you never lose track of its location in the project.

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/track-active-item.jpg)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/track-active-item.jpg)

Supported from Visual Studio 2010

## Editor

Easily **surround HTML** elements with a <div> using Shift+Alt+W. The inserted <div> is selected so you can easily edit it to be any tag you’d like, and the end-tag matches up automatically.

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/editor-surround-with.jpg)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/editor-surround-with.jpg)

Supported from Visual Studio 2017

**Copy any JSON fragment** to the clipboard and paste it as strongly typed .NET classes into any C# or VB code file.

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/editor-paste-json-1.jpg)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/editor-paste-json-1.jpg)

Supported from Visual Studio 2013

**You don’t need to write quotation marks** around JSON property names, simply type a colon and Visual Studio will insert the quotes automatically.

Supported in Visual Studio 2015

**Make IntelliSense and tooltips semi-transparent** for the duration you press and hold the Control key.

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/transparent-presenters.jpg)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/transparent-presenters.jpg)

Supported from Visual Studio 2010

**Instead of retyping ‘(‘** to show parameter info in method signatures, use Ctrl+Shift+Space to display the currently used overload.

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/show-signature-help-1.jpg)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/show-signature-help-1.jpg)

Supported from Visual Studio 2010

## Miscellaneous

**Play a sound** when certain events occur within Visual Studio.

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/misc-sounds.jpg)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/misc-sounds.jpg)

Supported from Visual Studio 2010

**Create custom window layouts** for specific development scenarios or monitor setups and switch between them easily.

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/custom-window-layouts-2.jpg)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/custom-window-layouts-2.jpg)

Supported from Visual Studio 2017

**Specify which Visual Studio components** are required for any solution, and Visual Studio will prompt the user to install them if missing. Read more in the blog post [Configure Visual Studio across your organization with .vsconfig](https://devblogs.microsoft.com/setup/configure-visual-studio-across-your-organization-with-vsconfig/).

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/solution-vsconfig.png)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/solution-vsconfig.png)

Supported from Visual Studio 2019

## Extensions

[Visual Studio Spell Checker](https://marketplace.visualstudio.com/items?itemName=EWoodruff.VisualStudioSpellCheckerVS2017andLater). An editor extension that checks the spelling of comments, strings, and plain text as you type or interactively with a tool window. It can also spell check an entire solution, project, or selected items. Options are available to define multiple languages to spell check against.

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/spell-checker.png)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/spell-checker.png)

Supported from Visual Studio 2013

[Add New File](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.AddNewFile). A Visual Studio extension for easily adding new files to any project. Simply hit Shift+F2 to create an empty file in the selected folder or in the same folder as the selected file.

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/add-new-file.png)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/add-new-file.png)

Supported from Visual Studio 2015

[Git Diff Margin](https://marketplace.visualstudio.com/items?itemName=LaurentKempe.GitDiffMargin). Git Diff Margin displays live Git changes of the currently edited file on Visual Studio margin and scroll bar.

[![](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/git-diff-margin.png)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/06/git-diff-margin.png)

Supported from Visual Studio 2012

This was just a few of the thousands of available extensions. To see more extensions, go to the [Visual Studio Marketplace](https://marketplace.visualstudio.com/search?target=VS&category=All%20categories&vsVersion=vs2019&sortBy=Downloads).

## In closing

These were just a few hand-picked tips from the [#vstip hashtag](https://twitter.com/search?q=%23vstip) on Twitter. There are plenty more to check out. If you have some great tips, please share them using the #vstip hashtag so we can all easily find them.

## Author

![Mads Kristensen](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2021/09/Mads-glasses-square-96x96.jpg)

Principal Product Manager

Mads Kristensen is a Principal Product Manager at Microsoft, working to enhance productivity and usability in Visual Studio. He’s behind popular extensions like Web Essentials and File Nesting and is active in the open-source community. A frequent speaker, Mads is dedicated to making Visual Studio the most enjoyable IDE for developers.
