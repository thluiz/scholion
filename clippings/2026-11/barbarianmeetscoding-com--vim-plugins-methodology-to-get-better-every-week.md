---
url: "https://barbarianmeetscoding.com/blog/2019/05/31/exploring-vim-plugins-a-methodology-to-become-1-percent-better-every-week"
captured_at: "2026-11-16T02:06:55+00:00"
title: "Vim Plugins: A Methodology to Become 1% Better Every Week | Barbarian Meets Coding"
domain: "barbarianmeetscoding-com"
---

Raise your hand if you have installed a bunch of plugins in your editor, only remember about half of them and barely use a small portion of that good half. If you have that problem, then I might just have what you need to take more advantage of your plugins and **become even more awesome**.

One of the most powerful features of Vim is its customizability and extensibility. These two features are commonplace in modern text editors but Vim brings its own special flavor to both. In Vim, you can customize and extend your experience by defining your own operators, motions, commands, mappings, settings, macros, etc. Any experienced Vim user will be comfortable with updating and tailoring their Vim configuration using a `vimrc` to include any of the things mentioned above. The interesting fact here though, is that, in order to customize Vim, you’ll find that oftentimes you’ll use the same features of the editor you normally use when programming. For instance, Vim macros are reusable units of text-editing that you create by recording your interaction with code and which you can later reuse to your heart’s content. As such, they are built of common operators and motions you use every day for coding. The same happens with custom commands and mappings.

You can get extremely far using only Vim core features. And you can get even further by slowly customizing and extending Vim using the methods mentioned earlier, growing your `vimrc` as you go adapting Vim to your development workflow. But there’s another amazing (and faster) way in which you can enhance your Vim experience: **plugins**. Like with other editors, plugins extend and customize your editor with new and exciting functionality. The cool thing about Vim plugins is that they are inbued by the spirit of Vim and take advantage of its modal nature, its preference for command composition, and the obsession of its community with being productive when coding. Because of that, using Vim plugins can truly enhance the way you work.

Oftentimes however, you will install a plugin and won’t take full advantage of it. In fact, most of the times you’ll install a plugin and forget about it. This article and this entire series on Vim plugins attempts to put an end to that Vim plugin underuse. It will provide you with a methodology and a guide to get the most out of your Vim plugins so that you can be more productive when using Vim.

## [](#how-to-discover-plugins)How to Discover Plugins

The best place to find Vim plugins is [VimAwesome](https://vimawesome.com/). [VimAwesome](https://vimawesome.com/) is a directory of plugins sourced from [GitHub](https://github.com/) (you’ll find most Vim plugins in GitHub these days), [vim.org](https://vim.org/) and which also includes plugins [submitted by users](https://vimawesome.com/submit).

So if there is some feature that you’re missing from Vim, you can visit [VimAwesome](https://vimawesome.com/) and just search for that missing functionality. Alternatively, you can browse around and see if you find anything interesting. Vim is very different from other editors so it is very likely that you’ll find something unexpected (yet awesome) like [vim-surround](https://vimawesome.com/plugin/surround-vim), [targets.vim](https://vimawesome.com/plugin/targets-vim) or [vim-sneak](https://vimawesome.com/plugin/vim-sneak).

**If you’re up for a more curated approach to discovering plugins then look out for more articles on my favorite plugins in the upcoming weeks and months.**

## [](#installing-plugins)Installing Plugins

Vim improved the way it manages plugins with Vim 8 and the addition of packages (a way to group and load plugins in your Vim editor). However, installing, removing and updating plugins still requires quite a bit of manual work and, therefore, Vim users normally rely on plugin managers. Using a plugin manager you can:

*   Configure your plugins declaratively in your `vimrc` (like you do with any other Vim configuration)
*   Install, remove and update plugins with the swipe of a command (which is extremely convenient)

These are some popular options with a very similar feature set and philosophy:

*   [Vundle](https://github.com/VundleVim/Vundle.vim)
*   [vim-plug](https://github.com/junegunn/vim-plug)
*   [Dein](https://github.com/Shougo/dein.vim)

Just follow the installation instructions of any of these plugin managers and update your `vimrc` accordinly. Once you’ve done that, adding a new plugin to Vim will be as easy as:

1.  Adding something like this to your `vimrc` where you declare the intention of having that plugin in your Vim editor:

```
Plug 'scrooloose/nerdtree'
```

2.  Executing a command (`:PlugInstall` in the case of _vim-plug_ for instance)

## [](#configuring-plugins)Configuring Plugins

Some plugins have sensible defaults and work out-of-the-box. But you will find that, oftentimes, there will be some additional configuration needed in order to take the full advantage of a plugin. When that is the case, you will be surprised at the lack of information available on the web (in most cases). You will then raise your fist to the sky and shout in anger and frustration, and wonder how the heck people can enjoy using Vim over other editors that aren’t as painful. Take a deep breath. It always helps. If you have some patience and dig a little deeper you’ll find that most Vim plugins are **extremely well documented**. The docs are just not where you expect them to be (_because why use the world wide web, right?_).

Where can one find that excellent documentation, then? Right within Vim [1](#fn-1).

If you type the `:help` ex-command you’ll be transported to Vim’s help. And if you scroll down from that main help page you’ll be happy to find that all your locally installed plugins have a help listed under the header **LOCAL ADDITIONS**:

![A Screenshot of Vim's help showing help files for installed plugins](https://barbarianmeetscoding.com/images/learning-vim-plugin-help.jpg "Learning Vim Plugin Help")

In fact, you will find that you can often access the documentation of a specific plugin just by typing `:help {name-of-the-plugin}` (e.g. `:h unimpaired`).

Ok, so you’ve found the documentation of a plugin. What’s next? The most important parts, at least at the beginning, will often revolve around mappings, commands and configurations:

*   **Mappings and Commands** will be two different APIs to access the plugin functionality. Some plugins will come with mappings that you can start using right away, or which you can configure to your liking. Other plugins will only provide commands which you can use directly or map to your own mappings.
*   **Configurations** let you either customize mappings wholesale, enable and disable plugin features or configure them to your heart’s content.

You can either search for any of these terms (e.g. `/mappings`, `/commands`, `/configuration`) or look at the documentation table of contents, find what you want and then with the cursor on top of a link (highlighted bits of text on the right) type `C-]` to be transported to that section of the documentation.

### [](#customizing-plugin-mappings)Customizing Plugin Mappings

Most plugins take advantage of the `<Plug>` keyword (`:h <Plug>`) to ease mapping customization. A plugin that uses `<Plug>` will define its mappings as follows:

```
" This is an example taken from the coc.vim plugin
" https://github.com/neoclide/coc.nvim

nnoremap <Plug>(coc-rename) :<C-u>call CocActionAsync('rename')<CR>

" nnoremap           => Create a non recursive normal mode mapping
" <Plug>(coc-rename) => so that when <Plug>(coc-rename) is typed
" :<C-u>call ...     => the function CocActionAsync('rename') is called
"                       to rename something in your code
```

Which effectively means that the `<Plug>(coc-rename)` is a placeholder that can be changed by the user. Some plugins will provide a default key mapping associated to this placeholder, but if they don’t you can define your own mapping like so:

```
" Remap for rename current word
nmap <leader>rn <Plug>(coc-rename)

" nmap               => create a normal mode mapping
" <leader>rn         => to map <leader>rn
" <Plug>(coc-rename) => to the <Plug>(coc-rename) placeholder
" so that when you type <leader>rn you'll rename some code
```

If a plugin that you’re using doesn’t rely on `<Plug>` you can always remap the plugin mappings to your liking (but it won’t be as convenient).

### [](#mapping-plugin-commands)Mapping Plugin Commands

Another common plugin API are Vim commands. For instance, [NERDTree](https://github.com/scrooloose/nerdtree), the most common file explorer for Vim only provides commands[2](#fn-2). For instance:

*   `:NERDTreeToggle` opens the file explorer
*   `:NERDTreeFind` opens the file explorer in the current file

In this case, it is convenient to provide a mapping for the commands you tend to use often:

```
nnoremap <leader>n :NERDTreeFind<CR>

" nnoremap          => create normal mode mapping
" <leader>n         => so that when I type <leader>n
" :NERDTreeFind<CR> => the :NERDTreeFind command will be executed and I'll open the file explorer
"                   => on the current file
```

Now you can type `<leader>n` and open the file explorer on the current file. That is much faster and convenient that typing the full `:NERDTreeFind` command.

## [](#learning-and-practicing-plugins)Learning and Practicing Plugins

An important part of adopting and taking advantage of plugins is spending some time perusing the docs and practicing. There’s a lot of ways to do things in Vim, and **it is very easy to do things in an un-optimal way just because it is comfortable and that’s the way you’ve always done it**.

Take this piece of text:

```
What a wonderful age we're living in
```

You can surround it in quotes by typing `I"<ESC>A"<ESC>`, or you can learn to use `vim-surround` effectively and type `yss"` (surround sentence in quotes).

```
"What a wonderful age we're living in"
```

This approach is superior not only because you have to type less, but also because it is repeatable and can be applied to multiple sentences by just typing the dot command `.`. On the grand scheme of things, the existence of a **surround** operator pays off by itself, as you can combine it with all the Vim motions you already know to greater effect.

In general, you can **follow this process when adopting a new plugin**:

1.  Skim the docs and find useful stuff
2.  Make a cheatsheet with that stuff
3.  Pick the most useful and start using it. If you find it really helpful, consider creating suitable mappings.
4.  When it is part of your workflow go back to 3. and pick the next most useful thing.

A great way to really focus on a feature is to just write it down on a post it in big letters and paste it under your computer screen. That will be your thing to practice for the upcoming week.

You don’t always need to follow this process. In fact, lots of plugins will fit right into your current development workflow and you can’t help but use them. You don’t need to limit yourself to learning one thing per week either. But it is great to have a baseline goal so that you can improve a little, and become better and better, every week.

## [](#pruning-plugins)Pruning Plugins

Just like it is great to take advantage of the plugins you use to be more effective, it is also important to be on the lookout for plugins you don’t use. This will happen for either of two reasons:

1.  You installed it because you thought it was cool and you’d need it but you didn’t
2.  You found a better way to solve the problem the plugin was trying to solve using Vim core features or another plugin

Whichever the reason, you just don’t need the plugin anymore and it’s better to delete it. Plugins don’t come for free. Some will affect Vim’s performance and speed (one of Vim’s greatest features), others will collide with other plugins, and yet others will occupy the precious keymap real state. So if you don’t take any advantage from a plugin just send it on its way to oblivion.

## [](#the-summary-at-the-end)The Summary At The End

Vim plugins are an amazing way to enhance your development experience with Vim. Sadly, you’ll find that oftentimes you’ll install a ton of plugins that you’ll use very rarely or won’t use at all. **In order to take advantage of these plugins and truly improve your development productivity you need to be more intentional about adopting a plugin**:

1.  Peruse the plugin documentation (`:h {name-of-plugin}`) and find things that are useful to you
2.  Make a cheatsheet with these things
3.  Pick the most useful one and practice it. This will normally involve replacing a previous habit for solving a problem that is less effective than the new one. That takes time and effort. Keep at it!
4.  If it is really useful make sure to have a mapping that makes it easy to access
5.  When you’ve incorporated it in your workflow, celebrate! **You’re now 1% better than you were before**. Wihoo!! Now pick the next most useful thing and practice it
6.  Repeat _ad infinitum_
7.  Every so often prune the plugins you don’t use.

**Up next we’ll go through a bunch of awesome different plugins and we’ll follow this methodology to learn to really take advantage of them and kick ass coding.** Until then, take care and be kind to other people.

* * *

1.  If you still want to use the web, you can find the documentation for a plugin in its GitHub repo inside the docs folder. This ain’t optimal and accessing the documentation from within Vim will be faster and more convenient.[↩](#fnref-1)
2.  Although NERDTree does come with lots of mappings when you’re inside the file explorer itself.[↩](#fnref-2)
