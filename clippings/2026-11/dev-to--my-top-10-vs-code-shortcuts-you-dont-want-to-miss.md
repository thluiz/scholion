---
url: "https://dev.to/terrytyli/my-top-10-vs-code-shortcuts-you-don-t-want-to-miss-nm9"
captured_at: "2026-11-16T01:17:16+00:00"
title: "My top 10 VS Code shortcuts you don't want to miss"
domain: "dev-to"
---

As a keyboard guy, I'd like to leverage all kinds of shortcuts as much as I can. It is especially true when it comes to coding. VS Code has been my favorite code editor for years, and I really love the way it allows me to use and customize shortcuts. Today I picked my top 10 super awesome shortcuts. Check it out!

### [](#1-go-to-last-edit-location-raw-%E2%8C%98k-%E2%8C%98q-endraw-)1\. Go to last edit location `⌘K ⌘Q`

Sometimes when I write the code, I need to pause a bit and go to different files to check other things. And after that, I need to quickly go back to the place where I was editing. This shortcut makes the move so easy.

[![Go to last edit location](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F6lq6e5q1j54oevh34l8o.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F6lq6e5q1j54oevh34l8o.gif)

### [](#2-go-to-bracket-raw-%E2%8C%98-%E2%87%A7-endraw-)2\. Go to bracket `⌘ ⇧ \`

Sometimes I want to quickly go to the end of a block to add some new code, and I can put the cursor on the opening bracket and type `⌘ ⇧ \` to jump to the closing bracket. This works better than scrolling down and visually searching the matching bracket. This also works when you want to jump from the closing bracket to the opening bracket.

[![Go to bracket](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F543mbpm20sssnz1v898f.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F543mbpm20sssnz1v898f.gif)

### [](#3-select-to-bracket)3\. Select to bracket

No default shortcut. I use `⌥ \`

This one allows me to quickly select everything between brackets. It is super handy when you want to copy or move some code out of a block.

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fp4v8ifxcccuafuwq0t7x.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fp4v8ifxcccuafuwq0t7x.gif)

VS Code doesn't have a default keybinding for this, so to enable it, you can type `⌘ ⇧ P` to open command palette and go to `Open keyboard shortcuts (JSON)`, and paste the code below.

```


{
  "key": "alt+\",
  "command": "editor.action.selectToBracket",
  "args": { "selectBrackets": false }
}

```

Enter fullscreen mode Exit fullscreen mode

###   
[  
](#4-go-to-matching-pair)

1.  Go to matching pair

No default shortcut. I use `⌘ H`

Similar to go to bracket, this allows you to quickly go to the matching tag. I really love this when I am writing React components, as I can easily move to the opening or closing tag and add new code from there.

[![Go to matching pair](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fkv1cyldu2vcacbgh08kn.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fkv1cyldu2vcacbgh08kn.gif)

Again, this one doesn't have a default shortcut. You can add the code below to enable it.

```


{
  "key": "cmd+h",
  "command": "editor.emmet.action.matchTag"
}

```

Enter fullscreen mode Exit fullscreen mode

###   
[  
](#5-go-to-the-previous-file-raw-%E2%8C%98-p-p-endraw-)

1.  Go to the previous file `⌘ P P`

I use this shortcut A LOT. Say I open file-A, and then switch to file-B, and if I want to go back to the file-A, I cannot really use `go back`, because `go back` is cursor-based. I cannot use `go to the last edit location` either as I haven't changed anything. So in such case, I hold `⌘` and press `P` twice and release `⌘`, it will bring me to the previous file.

[![Go to the previous file](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F7v6a7ochpxq5zlesi8l9.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F7v6a7ochpxq5zlesi8l9.gif)

### [](#6-go-to-symbol-in-editor-raw-%E2%8C%98-%E2%87%A7-o-endraw-)6\. Go to symbol in editor `⌘ ⇧ O`

Say I am looking at a file and I want to quickly jump to a function in the file, I can use this shortcut and type the name of the function, then hit enter to jump to it. This is quicker and more accurate than using `Find`.

[![Go to symbol](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F09698peakm7aagb9rzuh.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F09698peakm7aagb9rzuh.gif)

### [](#7-toggle-column-selection-mode)7\. Toggle column selection mode

No default shortcut. I use `⌘ ⇧ I`

This is super cool when I want to add/remove code on several consecutive lines. Instead of using the mouse to do multi cursor selection, I type `⌘ ⇧ I` to turn on the column selection mode and then hold `⇧` and press arrow keys to select multiple lines to edit. After finish it, I type the shortcut again to turn off the column selection mode.

[![Toggle column selection mode](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F5f27a8ywknfmw5joyzqk.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F5f27a8ywknfmw5joyzqk.gif)

You can add the code below to enable it.

```


{
  "key": "shift+cmd+i",
  "command": "editor.action.toggleColumnSelection"
}

```

Enter fullscreen mode Exit fullscreen mode

###   
[  
](#8-focus-on-files-explorer)

1.  Focus on Files Explorer

No default shortcut. I use `⌥ ⌘ J`

I use this shortcut to focus the current file in the explorer, so I can rename it or create a new file in the same folder. This is really handy as I don't need to click the mouse or manually look for the file in the file tree.

[![Focus on file explorer Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fd2duluy60ub2njeyn2ue.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fd2duluy60ub2njeyn2ue.gif)

You can add the code below to enable it.

```


{
    "key": "alt+cmd+j",
    "command": "workbench.files.action.focusFilesExplorer"
  }

```

Enter fullscreen mode Exit fullscreen mode

###   
[  
](#9-organize-imports-raw-%E2%87%A7-%E2%8C%A5-o-endraw-)

1.  Organize imports `⇧ ⌥ O`

Sometimes as I refactor the code, I might have some unused imports at the beginning of the file. Instead of manually deleting them, I use this shortcut to do the job automatically. This one also re-orders the imports to make them look clean.

[![Organize imports](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Ftvxrbpn5x32yxojpxygz.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Ftvxrbpn5x32yxojpxygz.gif)

### [](#10-add-all-missing-imports-raw-%E2%8C%98-endraw-)10\. Add all missing imports `⌘ .`

This shortcut is actually for `quick fix`. I found there is an option that allows you to add all the missing `import` statements, so you don't need to add them one by one. This option is available in typescript files.

[![Add missing imports](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fvt94nvcodedwz7ci7ljb.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fvt94nvcodedwz7ci7ljb.gif)

That's it. I hope you enjoy this post.

Feel free to ask me any questions. You can also [find me on twitter](https://twitter.com/terrytyli).
