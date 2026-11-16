---
url: "https://dev.to/janis_t/awesome-command-line-tools-204n"
captured_at: "2026-11-16T00:52:59+00:00"
title: "Awesome Command-Line Tools"
domain: "dev-to"
---

Most of the time, when I'm not using Vim, I'm probably hanging around in the command line. Thankfully, there is no lack of excellent CLI tools. Here I'd like to share some of them and how I use them.

> **For a TL;DR**, scroll to the bottom where you'll find a short list with the links.

## [](#tldr)tldr

[![Man vs. tldr](https://res.cloudinary.com/practicaldev/image/fetch/s--_gb3U7zX--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://d3ep7iiirnq25a.cloudfront.net/assets/man-tldr-a499fa8f74758f78c2c3ec83cdcdd945c9670f6a0764cb5899f6cc3ea8e06cdd.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--_gb3U7zX--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://d3ep7iiirnq25a.cloudfront.net/assets/man-tldr-a499fa8f74758f78c2c3ec83cdcdd945c9670f6a0764cb5899f6cc3ea8e06cdd.png)

Man pages is a fantastic place to look for a documentation and learn how a program works but sometimes what we need is to quickly have a look at examples of how a particular tool should be used. For example I never remember how should to send a POST request with `curl`.

[tldr](https://github.com/tldr-pages/tldr) does just that — prints a short description and then gives you the possible ways of usage. With the most common example at hand I can quickly copy what I need and run.

*   For [Alfred](https://www.alfredapp.com/) users, [here is the workflow for it](https://github.com/cs1707/tldr-alfred).
*   And yes, there's a [Vim plugin](https://github.com/wlemuel/vim-tldr) but somehow I don't find it too useful.

## [](#rupaz)rupa/z

I can't imagine living without [this little script](https://github.com/rupa/z). It tracks my most frequently used directories along with the frequency, and then it lets me jump to a directory by typing a partial path.

For example, when I want to get to `~/projects/web/vimfromscratch`, I just type `z vimf` and then hit `Enter`.

I would also suggest changing the default command name from `z` to `j` (as this is much easier for your fingers). You can either create an alias, or set the global env variable:  

```
export _Z_CMD="j"
```

I have to mention, there are some alternatives you can try:

*   [autojump](https://github.com/wting/autojump)
*   [bashmarks](https://github.com/huyng/bashmarks)
*   [fasd](https://github.com/clvv/fasd)

## [](#diffsofancy)diff-so-fancy

[![diff-so-fancy](https://res.cloudinary.com/practicaldev/image/fetch/s--_lupEjyc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://d3ep7iiirnq25a.cloudfront.net/assets/diffsf-9e7be84e9ef78034d3f198b68b6a3054df67514069b8c89b0a8edfa880d54e91.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--_lupEjyc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://d3ep7iiirnq25a.cloudfront.net/assets/diffsf-9e7be84e9ef78034d3f198b68b6a3054df67514069b8c89b0a8edfa880d54e91.png)

[This tool](https://github.com/so-fancy/diff-so-fancy) is a drop-in replacement for `diff` or `git diff`. It does the same thing but does it with style. The default colors are much nicer, and the diff shows changes within the same line (see the screenshot).

In order to make it your default Git pager, run this:  

```
git config --global core.pager "diff-so-fancy | less --tabs=4 -RFX"
```

Then also, you can replace your default `diff` by setting an alias:  

```
alias diff="diff-so-fancy"
```

## [](#bat)Bat

[![Cat vs. Bat](https://res.cloudinary.com/practicaldev/image/fetch/s--ny70G1ty--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://d3ep7iiirnq25a.cloudfront.net/assets/cat-vs-bat-964daf1c0a508e43b338ba7d3890f38260884b5d06e592608a7839e01a1b93dc.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--ny70G1ty--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://d3ep7iiirnq25a.cloudfront.net/assets/cat-vs-bat-964daf1c0a508e43b338ba7d3890f38260884b5d06e592608a7839e01a1b93dc.png)

Now that we started talking about syntax highlighting, have you ever thought of how `cat` is a bit boring? Wouldn't it be nice if it was able to highlight the syntax of a file that it's printing out?

The answer to this question is [bat](https://github.com/sharkdp/bat). `bat` adds a syntax highlighting for a large number of languages. Plus, it is integrated with Git, so it will show what has changed in the file you're viewing.

You would want to replace your older model:  

```
alias cat="bat"
```

You can colorize you man page by exporting:  

```
export MANPAGER="sh -c 'col -bx | bat -l man -p'"
```

For other interesting integration, please have a [look at the README](https://github.com/sharkdp/bat).

## [](#ripgrep)ripgrep

[![Searching for a React component with ripgrep](https://res.cloudinary.com/practicaldev/image/fetch/s--BFwyM5Qh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://d3ep7iiirnq25a.cloudfront.net/assets/ripgrep-c796b44132acbe6c0688f9aa8e7bc4dc3bdc4b4a9c13b8f26eb9bbda8616bb1b.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--BFwyM5Qh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://d3ep7iiirnq25a.cloudfront.net/assets/ripgrep-c796b44132acbe6c0688f9aa8e7bc4dc3bdc4b4a9c13b8f26eb9bbda8616bb1b.png)

[Ripgrep](https://github.com/BurntSushi/ripgrep) is an alternative to `ag` (the silver searcher). It is significantly faster, and also it comes with some sane default behaviour, like respecting your `.gitignore` file.

As you can see on the screenshot, the output is clear, and the search pattern is highlighted in the output results which is nice.

## [](#exa)exa

[![Regular \`ls\` vs \`exa\`](https://res.cloudinary.com/practicaldev/image/fetch/s--2fmkTH_R--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://d3ep7iiirnq25a.cloudfront.net/assets/exa-685149d4582530e42f6cf70dc530b9dd8fceac35a91a9d8db7917a556d62b363.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--2fmkTH_R--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://d3ep7iiirnq25a.cloudfront.net/assets/exa-685149d4582530e42f6cf70dc530b9dd8fceac35a91a9d8db7917a556d62b363.png)

Another drop in replacement you can use instead of the build-in `ls` command is [Exa](https://github.com/ogham/exa). Again, as some other tools in this article `exa` provides color highlighting and some sane defaults but overall remains compatible with `ls` API.  

```
alias ls="exa"

# I usually use this command instead
alias l="exa -lahF"
```

## [](#fd)fd

[![Regular \`find\` vs \`fd\`](https://res.cloudinary.com/practicaldev/image/fetch/s--JP7Gqr4T--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://d3ep7iiirnq25a.cloudfront.net/assets/fd-vs-find-a8601a4cf6987eb88e948ef6ec7773057f32b4929f1aa4f388c52da48479265d.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--JP7Gqr4T--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://d3ep7iiirnq25a.cloudfront.net/assets/fd-vs-find-a8601a4cf6987eb88e948ef6ec7773057f32b4929f1aa4f388c52da48479265d.png)

By this time, you probably already figured out that if there is a replacement for some built-in command, I would probably have it installed.

Meet [fd](https://github.com/sharkdp/fd), a faster alternative to `find`. The problem with `find` is that as I can never remember how to use it. Should it be `find myfile.py`, or `find --name myfile.py`, or is it with a single dash? Should I add `.` before or after the search pattern? Argggh.

With `fd`, it's always straightforward `fd myfile.py`. Again that's about saner defaults and beautiful colorized output (see the screenshot).

Don't forget to  

```
alias find="fd"
```

### [](#fzf)Fzf

[![Fzf with a file preview](https://res.cloudinary.com/practicaldev/image/fetch/s--FBK3yexP--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://d3ep7iiirnq25a.cloudfront.net/assets/fzf-preview-38df213a8843c333be881f2097fb9e5455276483e9549a763d6526ce95ecbd83.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--FBK3yexP--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://d3ep7iiirnq25a.cloudfront.net/assets/fzf-preview-38df213a8843c333be881f2097fb9e5455276483e9549a763d6526ce95ecbd83.png)

Oh yes, I saved the coolest for the end. [Fzf](https://github.com/junegunn/fzf) (fuzzy finder) is a super fast tool written in Go which does just one thing: It takes a list of lines as an input and then let's a user fuzzy search in them for some text.

While that may not sound too impressive, the fun part begins with the applications.

For example, try  

```
vim $(fzf)
```

You'll be prompted with a list of files, and you can search among those. After you press `enter`, the selected file will open in Vim.

Or, you try pressing `Ctrl+R` (the command that runs the command history in the shell). You can now fuzzy search among your commands, then press `enter` to execute it.

While searching for a file, `Fzf` can give you a nice preview (see the screenshot), you just need to specify the preview command:  

```
fzf --preview="bat {} --color=always"
```

Remember the `rupa/z` script? `Fzf` integrates with it nicely, so if you run `z` without arguments you can fuzzy search among your most frequently used directories.

Honestly, the list of possibilities how you can use it is really endless. Sky is the limit. Try browsing [this page with examples](https://github.com/junegunn/fzf/wiki/examples).

## [](#what-is-this-thing-youre-using)What is this thing you're using?

In case you want to know, here is what my setup is based on:

*   [iTerm2](https://iterm2.com/) terminal
*   [Menlo typeface](https://en.wikipedia.org/wiki/Menlo_\(typeface\))
*   [Afterglow colorscheme](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/schemes/Afterglow.itermcolors)
*   [Z shell](https://en.wikipedia.org/wiki/Z_shell) with [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) configuration framework
*   [Custom theme](https://github.com/hiquest/dotfiles/blob/master/yanis.zsh-theme) for `oh-my-zsh`
*   The numbers you see on the screenshots are `ruby` and `node` versions.

## [](#tldr)Tl;DR

*   [tldr](https://github.com/tldr-pages/tldr) for quickly viewing the usage examples
*   [rupa/z](https://github.com/rupa/z) for jumping between directories
*   [diff-so-fancy](https://github.com/so-fancy/diff-so-fancy) for better diffing
*   [bat](https://github.com/sharkdp/bat) to replace `cat` with
*   [ripgrep](https://github.com/BurntSushi/ripgrep) for searching pattern within text files
*   [exa](https://github.com/ogham/exa) a colorful and fast `ls`
*   [fd](https://github.com/sharkdp/fd) a drop-in replacement for `find`
*   [Fzf](https://github.com/junegunn/fzf) for fuzzy search

P.S.: I'm writing a book on Vim for developers. Feel free to [check it out](https://gumroad.com/l/vimfromscratchbook).
