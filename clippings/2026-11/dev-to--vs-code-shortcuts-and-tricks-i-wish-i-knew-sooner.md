---
url: "https://dev.to/hannahgooding/vs-code-shortcuts-and-tricks-that-i-wish-i-knew-sooner-3mcj"
captured_at: "2026-11-16T01:02:02+00:00"
title: "VS Code shortcuts and tricks that I wish I knew sooner"
domain: "dev-to"
---

## [](#introduction)Introduction

After teaching myself for a year I started coding full time when I joined the Founders and Coders web development bootcamp in March 2020. Two weeks into the course we went into lockdown in the UK and our cohort had to go remote for the remaining 16 weeks. Thanks to the collaborative power of the VS Code Live Share extension we were still able to pair program and go through the syllabus as planned, but one of the things we missed out on from not being in person was organically sharing the little tips and tricks that you would normally pick up from working next to each other.

You can watch someone demonstrate something while sharing their screen, but unless you see them typing on the keyboard you don't necessarily pick up on the key presses that could also save you seconds of your day! As a result there are a lot of nifty VS Code tricks that I have learned since starting my first role as a Full Stack Developer that I wish I had know during the course.

I compiled these into a talk for the next Founders and Coders cohort, entitled "Why The F\*\*\* Didn't I Know This Sooner?!", and I also wanted to share them here for those starting out on their own coding journeys.

## [](#vs-code-shortcuts)VS Code shortcuts

[Emmet](https://code.visualstudio.com/docs/editor/emmet) gives you some default abbreviations for a range of file types including `.html` and `.css` which expand into useful code snippets. Emmet support is built into VS Code so it does not require downloading an extension.

## [](#html-boilerplates)HTML boilerplates

If you type `!` into an `html` file in VS Code and then press enter, you get the following HTML skeleton:

```


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>

</body>
</html>


```

Enter fullscreen mode Exit fullscreen mode

A lot of my frequently used HTML tags are missing from this boilerplate so I have configured my own.

I made `!!` into a custom shortcut for my VS Code editor that includes the `<meta>` tag for SEO, as well as the tags for for linking CSS stylesheets and JavaScript files, and a few other frequently used semantic tags.

To do this you need to navigate to Code > Preferences > User Snippets and search for 'html.json'. Then you add your custom snippets into this file.

I would recommend writing out the desired structure into an HTML file first, and then you can copy it into a tool like [this](https://www.freeformatter.com/json-escape.html) to parse your HTML file into a JSON string with escaped characters to get the right indentation.

My `html.json` file looks like this:

```


{
  "HTML boilerplate": {
    "prefix": "!!",
    "body": [
      "<!DOCTYPE html>\r\n<html lang=\"en\">\r\n<head>\r\n  <meta charset=\"UTF-8\">\r\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\r\n  <meta name=\"description\" content=\"\">\r\n  <link rel=\"stylesheet\" type=\"text\/css\" href=\"styles.css\">\r\n  <title>Document<\/title>\r\n<\/head>\r\n<body>\r\n  <header>\r\n  <\/header>\r\n  <main>\r\n  <\/main>\r\n  <footer>\r\n  <\/footer>\r\n  <script src=\"scripts.js\"><\/script>\r\n<\/body>\r\n<\/html>"
    ],
    "description": "HTML boilerplate with custom tags"
  }
}


```

Enter fullscreen mode Exit fullscreen mode

And the finished boilerplate looks like this:

```


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="">
  <link rel="stylesheet" type="text/css" href="styles.css">
  <title>Document</title>
</head>
<body>
  <header>
  </header>
  <main>
  </main>
  <footer>
  </footer>
  <script src="scripts.js"></script>
</body>
</html>


```

Enter fullscreen mode Exit fullscreen mode

## [](#html-abbreviations)HTML abbreviations

Sometimes you can spend longer learning to type out shortcuts than if you just manually typed the code. I personally don't find Emmet abbreviations a time saver for writing CSS, but some of the HTML abbreviations I find useful include:

### [](#nested-elements)Nested elements

The shortcut `nav>ul>li` creates:

```


<nav>
  <ul>
    <li></li>
  </ul>
</nav>


```

Enter fullscreen mode Exit fullscreen mode

### [](#multiple-elements)Multiple elements

The shortcut `li*5` creates:

```


<li></li>
<li></li>
<li></li>
<li></li>
<li></li>


```

Enter fullscreen mode Exit fullscreen mode

### [](#tags-with-text)Tags with text

The shortcut `a{Click Me}` creates:

```


<a href="">Click Me</a>


```

Enter fullscreen mode Exit fullscreen mode

### [](#elements-with-multiple-classes)Elements with multiple classes

The shortcut `div.first-class.second-class` creates:

```


<div class="first-class second-class"></div>


```

Enter fullscreen mode Exit fullscreen mode

### [](#elements-with-ids)Elements with IDs

The shortcut `div#main` creates:

```


<div id="main"></div>


```

Enter fullscreen mode Exit fullscreen mode

A full list of shortcuts for can be found on the [Emmet Docs Cheat Sheet](https://docs.emmet.io/cheat-sheet/).

* * *

## [](#vs-code-source-control-tab)VS Code Source Control Tab

Using VS Code's built in Source Control feature, you can stage your files and write commit messages with the VS Code UI, rather than using the terminal.

What I like about this is:

*   You can stage particular files easily without having to type out the file path into your terminal.
*   You can format your commit messages more easily.
*   When you write a commit message, it warns you if you go over the "recommended" character count in a line.
*   If you are using the Live Share extension, your collaborator's co-authoring credentials appear (they have to be signed in with their GitHub account).

* * *

## [](#useful-vs-code-extensions)Useful VS Code extensions

## [](#bracket-pair-colorizer-2)[Bracket Pair Colorizer 2](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2)

This extension colorizes matching opening and closing brackets in your code so you can scope your functions and statements at a glance.

Without extension:

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F109jb5q6w1ocb9hnm5gt.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F109jb5q6w1ocb9hnm5gt.png)

With extension:

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fs7s3vwukwx4v1mhq3tfh.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fs7s3vwukwx4v1mhq3tfh.png)

Edit: This article originally linked to Bracket Pair Colorizer v1, thank you to [@indcoder](https://dev.to/indcoder) for pointing out in the comments that there is a v2 out there which is faster and more accurate!

## [](#relative-file-path)[Relative File path](https://marketplace.visualstudio.com/items?itemName=jakob101.RelativePath)

This extension gives you a shortcut for getting the relative filepath of another file from your current file. This is really helpful in a large codebase with lots of nested folders where you have a lot of imports and exports between files, for instance in a React.js project.

Use the shortcut to bring up the file search (Windows `Ctrl+Shift+H`, Mac `Cmd+Shift+H`):

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9jx5yye4yxx9mgldc79a.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9jx5yye4yxx9mgldc79a.png)

Search for the file you want the relative path for:

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fri33y0sxmkvgudf3zmwv.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fri33y0sxmkvgudf3zmwv.png)

The relative path will appear:

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8jd4z3k34jrpb8826wc5.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8jd4z3k34jrpb8826wc5.png)

## [](#gitlens)[GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

This extension is Git supercharged for your editor with loads of features that I don't yet know how to use.

What I do use it for is the Git blame feature, which annotates the most recent commit history for each line in your files. This is especially useful when working on a group project so you can see at a glance when the last changes were made, who made them, and the relevant commit message.

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fn3nt52852d69yhoti5pp.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fn3nt52852d69yhoti5pp.png)

## [](#prettier)[Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

Prettier is a lifesaver because it automatically formats your code! You can download it as an extension on VS Code, and it will run your settings that you configure in the application (go to Settings and search for 'Prettier').

To format your current file, right click and select Format Document, or to turn on automatic formatting when you save your files go to Settings and search for 'format on save' and tick the checkbox.

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffeknlabevgy7fjyyaqlc.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffeknlabevgy7fjyyaqlc.png)

It's a good idea to have a `.prettierrc` config file in the root folder of your group projects where you specify how many spaces you want for intentation, single or double quotes, whether all lines should finish with a semi-colon, etc.

The config file overrides your local VS Code Prettier settings so everyone on the team will have the same formatting rules applied to their code - avoiding nasty conflicts!

I use this [Prettier Config Generator](https://michelelarson.com/prettier-config/) to generate the JSON for the file, and the [Prettier docs](https://prettier.io/docs/en/options.html) explain more about what each of the format options mean.

The following JSON in a `.prettierrc` file:

```


{
    "printWidth": 80,
    "tabWidth": 2,
    "useTabs": false,
    "semi": true,
    "singleQuote": false
}


```

Enter fullscreen mode Exit fullscreen mode

Reformats this:

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4rei8g2bycot3okr00og.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4rei8g2bycot3okr00og.png)

Into this, with consistent spacing, an average line width of roughly 80 characters, 2 spaces for indentation and _not_ tabs, semicolons printed at the end of every statement, and double quotes instead of single quotes:

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fumxmhu17291b0ugvuvvo.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fumxmhu17291b0ugvuvvo.png)

This is just an example to demonstrate the formatting changes Prettier applies, and is not a recommendation of code style. Most of the time you won't have to play around with the settings too much and you can go with the [basic config](https://prettier.io/docs/en/configuration.html) to keep your codebase consistent, or when you start working as a developer your company will already have a "house style".
