---
url: "https://dev.to/vaidotas/get-faster-vscode-navigation-without-a-mouse-3d0m"
captured_at: "2026-11-16T01:36:46+00:00"
title: "Get Faster - VSCode navigation without a mouse"
domain: "dev-to"
---

[![Cover image for Get Faster - VSCode navigation without a mouse](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F44mvyv6uidyqlzn32woy.jpg)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F44mvyv6uidyqlzn32woy.jpg)

[![Vaidotas Piekus](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F29177%2Fa03aa518-2087-46ef-97bf-7854875128c8.jpeg)](https://dev.to/vaidotas)

## [](#motivation)Motivation

Why should you care about mouseless experience when VSCode is a GUI editor tuned to a great mouse experience? The answer is speed.  
If you can do make tasks that you do every day but faster it will save you time and keep you in the "flow" longer. It is worth just looking through common default keybindings for VSCode and get a great view of what is possible and what is already available: [MAC](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf) / [Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)

However, the real value proposition is not to try and memorize dozens of keyboard shortcuts but to optimize the "hottest path" for your daily workflow. You want the least friction possible for things you do constantly and that means avoiding mouse/trackpad for most navigation and code editing. Let's dive in.

### [](#vscode-navigation-between-panels-files-and-tooltips)VSCode Navigation between panels, files, and tooltips

**(1) Activity Bar**

[![VSCode Activity Bar](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F96s7tr13l12dvb6fs5ii.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F96s7tr13l12dvb6fs5ii.png)  
Depending on the number of extensions and settings your activity bar can look different than mine. All menus in Activity Bar can be reached with keyboard, however, we do not need to work on remembering that obscure extension you maybe use once a month. Let's focus on the most important ones:

*   File Explorer `CMD+SHIFT+E` - we use this all the time, navigate between files and explore project file tree structure. One annoyance of default VSCode behavior in File Explorer is when you have file highlighted and hit `ENTER` it defaults to renaming a file. If you want to open it instead (which is what I want almost 100% of the time) you have to use `CMD+Down_Arrow`. This is funky but worth remembering.
    
*   Project Search `CMD+SHIFT+F` - extremely helpful to find anything within your project, open it up, enter search string hit `ENTER` and you are good to go. If you want to jump down to results without a mouse, hit `CMD+Down_Arrow` and now you can navigate through the files in results.
    
*   Source Control `CTRL+SHIFT+G`. I typically just launch this panel with the keyboard but switch to interacting with the mouse as I like to click through the files, take a look at the changes and commit them right in the panel I find mouse be a little more useful but you can do everything with the keyboard too if you so wish.
    

Okay, now that we got those down you should never need to break away from your keyboard to launch File Explorer or search within your project!

**(2) Navigation between your code, activity bar and terminal**

These 3 sections of VSCode are definitely the most used and important for anybody's workflow. I jump around Activity Bar, edit my code and go over to the terminal to restart the server or do any other action all the time. It is very frustrating to keep cycling between these panels with the mouse just to do a quick command.

*   Focus Left Panel (can be anything from Activity Bar selections) `CMD+0`
*   Focus Middle Panel (open files) `CMD+1` This technically focuses the first file that you have open, if you have another file opened in the split, you can do `CMD+2` and just jump the second file you've got opened.
*   Show terminal `CMD+J` or `` CTRL+` ``. Notice that this only shows terminal. If we have it already opened and want to focus it, it does not seem that VSCode provides default keybinding for such action. We can define it ourselves. Open Command Palette `CMD+SHIFT+P` and type "keyboard" and select the one with the JSON "Open Keyboard Shortcuts (JSON)", now we can add any keybinding for any action. Here is what I have: \`\`\`

{ "key": "ctrl+l", "command": "workbench.action.terminal.focus" },  
{ "key": "ctrl+l", "command": "workbench.action.focusActiveEditorGroup", "when": "terminalFocus" },

```
You can change that "key" string to whatever feels good, but the objective here is with these two settings you can cycle through editor focus and terminal focus with one keybinding. That is super nice!

**(3) Navigating within a file super fast**
Once you have a file that is opened it is tempting to reach for a mouse and start scrolling up and down the file to find the relevant spot in code or just to gauge the shape of the file. Here are a few key techniques to get you around any file with more efficiency:
  * `CMD+Up_Arrow/Down_Arrow` Jump to the beginning/end of the file. This is very useful when you need to quickly jump to the import section of the file or the export section which is usually at the end.
  * `CMD+SHIFT+O` Navigate between **symbols** within a file. This is the most useful command that nobody uses! It gives you a quick panel to cycle through function definitions/methods defined within a file.
![navigation](https://dev-to-uploads.s3.amazonaws.com/i/e7k17pvybh9f814u90cb.gif)
  * `CMD+F` Find in File. Very powerful and useful command. We all know how to use it but you can actually use this one to quickly jump to a certain section in the file. Say you have function called `adder` you hit `CMD+F` type `add` and with a quick ESC your cursor is already there, ready to edit. Handy!

---
That is it folks! General advice learning these keybindings is to start small, start wherever your "hottest path" is and try and optimize that a little to be more comfortable and faster. Don't try and do too much, memorize all the things, you will struggle to remember it all.

In Part2 of this series, we will be talking about fast code editing!
Let me know below your favorite shortcut and other tips and tricks you discovered.
```

Enter fullscreen mode Exit fullscreen mode
