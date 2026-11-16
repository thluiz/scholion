---
url: "https://web.archive.org/web/20200813205326id_/https://dev.to/whizzzoe/how-i-set-up-vscode-for-productivity-checklist-omc"
captured_at: "2026-11-16T07:52:04+00:00"
title: "How I set up VSCode for productivity? [Checklist]"
domain: "web-archive-org"
---

### [](#list-of-shortcuts-configuration-and-extension-that-i-use-in-vscode)List of shortcuts, configuration, and extension that I use in VSCode

_Note:_ This article is part of my [toolkit newsletters](https://whizzoe.substack.com/subscribe)↗️ where I share resources about building things. Join me :)

I made a code editor switch from Sublime Text to Visual Studio Code (VSCode). Like many developers, I couldn’t be happier.

As a newcomer to VSCode, I realized I needed to get the best out of it and explore what it has to offer.

In this post, I will share a list of configuration that I use, and how you can set them up to boost your productivity.

## [](#1-get-a-nice-theme)1\. Get a nice theme

Coding is a long-hour and creative task. Therefore, I prefer a code editor theme that I feel comfortable and inspired to use.

I used to love Dracula theme. But recently, I’ve become a fan of Field Lights theme:

[![Field Lights Theme](https://res.cloudinary.com/practicaldev/image/fetch/s--s0fsECHp--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/3840/1%2AiWIkMnvr9pXEaMNCf-iDkQ.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--s0fsECHp--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/3840/1%2AiWIkMnvr9pXEaMNCf-iDkQ.png)

## [](#2-configure-for-workflow)2\. Configure for workflow

I prefer a clean and minimalist view in VSCode. This allows me to focus on writing codes without seeing those extra panels.

#### [](#some-of-my-settings-in-view-gt-appearances)Some of my settings in “View” > “Appearances”:

*   Status Bar (disable)
*   Activity Bar (disable)
*   Toggle Panel (disable)
*   Zoom In (to your comfortable level)
*   Minimap (disable)
*   Wordwrap (enable)

#### [](#finetune-settingsjson-using-open-settings-json-editor)Fine-tune settings.json using Open Settings (JSON) editor:

I’ve enabled auto-save and wordWrap by adding few lines of code in the settings.json.

To edit this file, simply CTRL+SHIFT+P and type in search bar “Open Settings (JSON).

{
"workbench.colorTheme": "Field Lights",
"window.zoomLevel": 1,
"workbench.activityBar.visible": false,
"workbench.statusBar.visible": false,
"\[html\]": {
   "editor.defaultFormatter": "vscode.html-language-features",
   "editor.tabSize": 2
},
"breadcrumbs.enabled": false,
"window.menuBarVisibility": "default",
"editor.minimap.enabled": false,
"editor.renderControlCharacters": false
"files.autoSave": "afterDelay",
"files.autoSaveDelay": 5000,
"editor.wordWrap": "on",
}

#### [](#i-keep-these-panels-open-for-daytoday-navigation)I keep these panels open for day-to-day navigation:

*   Terminal (built-in terminal without having to open externally)
*   Explorer (browse through files or create new ones)

[![panels](https://res.cloudinary.com/practicaldev/image/fetch/s--vvTdqw0m--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/3840/1%2AW-rHvi9Rsnp-a2oYS0i-tg.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--vvTdqw0m--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/3840/1%2AW-rHvi9Rsnp-a2oYS0i-tg.png)

## [](#3-handy-shortcuts)3\. Handy shortcuts

Keyboard shortcuts are a huge time-saver. I’ve explored some VSCode shortcuts and applied on a daily basis.

#### [](#here-are-some-of-my-favorites)Here are some of my favorites:

*   Quickly search any project files in the folder **CTRL+P**
*   Command Palette **CTRL+SHIFT+P**
*   Show/hide sidebar **CTRL+B**
*   Open Terminal **CTRL+SHIFT+\`**
*   Jump between file tabs **CTRL+TAB**
*   Open files side-by-side \*_CTRL+\*_
*   Switch between editors side-by-side **CTRL+1 ; CTRL+2 ; CTRL+3**
*   Fast scrolling **ALT+scroll**
*   Search by file name **CTRL+P**
*   Multi-occurrence editing **current selection+CTRL+SHIFT+L**
*   Duplicate a line Up or Down **SHIFT+ALT+UP/DOWN**
*   Move a line of code Up or Down **ALT+UP/DOWN**
*   Clear extra whitespaces **CTRL+K then CTRL+X**
*   Enable multi-cursor editing **ALT+click+select text**
*   Add or remove comment **CTRL+/**
*   Write HTML tags with Emmet abbreviation type **html:5+tab**
*   Zoom In or Out **CTRL+ ‘+’ / ‘-’**

You can also download the [full VSCode shortcut](https://code.visualstudio.com/assets/docs/getstarted/tips-and-tricks/KeyboardReferenceSheet.png) from the official website:

[![vscode shortcut](https://res.cloudinary.com/practicaldev/image/fetch/s--Dfi3ktDc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/1992/1%2AAWLaiwFBKGXywj8RUg6M-w.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--Dfi3ktDc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/1992/1%2AAWLaiwFBKGXywj8RUg6M-w.png)

## [](#4-cool-extensions)4\. Cool extensions

The awesome thing about VSCode is that it comes with a library of free extensions that can improve your workflow.

#### [](#some-extensions-that-i-use)Some extensions that I use:

*   Python extension (support your python programming)
*   Prettier — Code formatter (easily format your JavaScript / TypeScript / CSS)
*   Inline HTML (syntax Highlighting for html/css)
*   Indent 4-to-2 (convert indentation from tab or 4 spaces into 2 spaces)
*   IntelliSense for CSS class names in HTML (CSS class name autocomplete)

## [](#where-to-find-me)Where to find me? 👋

#### [](#1-find-me-on-personal-site-twitter-linkedin)\[1\] Find me on [Personal Site](https://whizzoe.com/) / [Twitter](https://twitter.com/whizzzoe/) / [LinkedIn](https://www.linkedin.com/in/whizzoe/) 🔥

#### [](#2-in-case-you-miss-out-i-can-send-my-upcoming-toolkit-to-your-inbox-click-here-to-join-my-newsletter)\[2\] In case you miss out, I can send my upcoming toolkit to your inbox — [Click here to join my newsletter](https://whizzoe.substack.com/subscribe) 💌

#### [](#3-if-youre-feeling-generous-today-you-can-buy-me-a-coffee)\[3\] If you’re feeling generous today, you can [buy me a coffee](https://www.buymeacoffee.com/whizzoe) ☕
