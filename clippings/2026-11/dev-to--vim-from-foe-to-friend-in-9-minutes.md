---
url: "https://dev.to/omerxx/vim-from-foe-to-friend-in-9-minutes-2np0"
captured_at: "2026-11-16T18:56:09+00:00"
title: "Vim: from foe to friend in 9 minutes"
domain: "dev-to"
---

### [](#lessons-from-3years-of-intensive-learning)Lessons from 3-years of intensive learning

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fyzcybd3wlguqnou9nqeb.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fyzcybd3wlguqnou9nqeb.png)

> **TL;DR**  
> Using Vim is by-far the most productiveness-enhancing, enjoyable and rewarding tool you’ll ever adopt. This post was an idea I had for a long time; there are literally endless pieces of information about Vim out there, and every time I started writing I thought I was just adding to the chaos. I feel it became too important to ignore, too much of a productivity change, and probably the best tool I have ever decided to take upon learning, and so I’m sharing my process. This is an opinionated post about how I think anyone should start. As I usually prefer to get solid procedures and actual action items, this is what I tried to create here so readers don’t lose themselves in the sea of information out there.

For years Vim was a stranger to me. In one of my first job interviews as a junior, the recruiting manager wanted to test my limited set of skills and asked what my favorite IDE was. My answer was something like “Notepad++”. Needless to say, it wasn’t quite what he was expecting.  
He dug further and asked, “What do you think about Vim?”  
I replied: “Vim?? isn’t that this console thing no one knows how to exit?”  
Long story short, I didn’t get the job…

To me, Vim was this CLI editor sysadmins used in videos and a kind of a hack-tool used by hipster developers around the world. “_Why would anyone do that to themselves?_” — I asked myself and others more than a few times trying to understand whenever I met another enthusiastic user. I genuinely wanted to know why are people talking about it so much, why would anyone use it? How can anyone be so motivated to use and improve their flow with Vim continuously when it’s such a **_terrible_** tool to use.  
_What’s wrong with modern editors?_

So I tried it out. A lot.  
I took vim for many, many test drives. I wanted to prove to myself I could use it. It was my nemesis and I would not accept defeat. I got to a point I made up my mind that Vim is a _religion._ There’s a bunch of people who believe in it with all their hearts and just the same amount of opposers, like me that couldn’t see the light. So I left Vim aside, but couldn’t help keep thinking about it as I kept noticing other professionals across dev communities speak so highly of it. Heck, even on Silicon-Valley _\[[s03e06](https://www.youtube.com/watch?v=SsoOG6ZeyUI)\]_ the fight is over spaces vs. tabs and Vim vs. Emacs. “Really?” I thought, “Vim vs. Emacs?”, people don’t use \*standard \*editors?

The real change happened when I met one of the most talented backend developers I had ever worked with. He was so enthusiastic about Vim, had so much knowledge, and most importantly worked so freaking quickly and smoothly I had to know what he was doing. This leads to the beginning of my “why”…

## [](#why)Why

1.  Vim is **always there** on any \*nix machine, Mac and soon even Windows machines. You can always find it running natively on your OS. Vim ([or its predecessor VI](https://askubuntu.com/a/418413)) are already installed, so even if you’re not going to utilize it for everything, you probably want to know it pretty well. You want to be able to find your away around remote-servers-editing quickly.
    
2.  **It’s productive**  
    This is the holy grail of using Vim; once you master the basics, you’ll become so ridiculously fast, you really won’t able to go back. You’ll start looking for those quick moves when writing messages or when chatting online. Writing any code or editing blocks of it becomes smooth and fluent in a way you probably never knew possible.
    
3.  **Integrations**  
    Vim is so powerful it has integrations with just about anything you can think if. I don’t even leave it to git commit, push, browsing through history and what not. Took it one step further and [created my flow of solving merge conflicts](https://medium.com/prodopsio/solving-git-merge-conflicts-with-vim-c8a8617e3633) right from Vim!
    
4.  **Awesomeness**  
    Not sure if I should address this as a real factor, but being honest, Vim is an enjoyable tool. Every time I use it, including when editing these lines, I enjoy my shortcuts, movement abilities, macros, and repeatable commands.  
    Think of yourself in the office using it; your colleagues are going to be so impressed they’d start asking for resources and tips. I know because that’s how I started and how other colleagues of mine started after me. We all can say the same thing, after reaching a medium proficient level: you become so _freaking fast_, other editors stop making sense. You can think fast, work quickly, and never feel an idiot again.
    
5.  **It’s right**  
    Hands down, how many times did you find yourself editing over 20 locations in a single file, reaching for your mouse over and over, knowing in your heart what you’re doing is either wrong? How many times did you feel like you were wasting time on reaching UI buttons or looking for the right click to help you make the change? For me, the answer was dozens if not hundreds of times, until one decided to put a stop to it.
    
6.  **It’s light; it’s** so light it takes 10% of your machine’s resources. Check out the comparison below describing average memory consumption of popular IDEs:
    

[![A comparison of VIMs average memory consumption taken on multiple Linux servers](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqos071cy1atrqqlz429z.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqos071cy1atrqqlz429z.png)_A comparison of VIMs average memory consumption taken on multiple Linux servers_

## [](#how)How

Honestly, Vim is not the most accessible tool to adopt. Hell, it’s **hard**.  
Vim has a very steep learning curve, but rest assured: if you try, don’t give up, and be consistent, it’s **1000%** rewarding.

[![Time vs. Productivity of IDEs](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxphmhe2uvpiolqvq8ohd.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxphmhe2uvpiolqvq8ohd.png)_Time vs. Productivity of IDEs_

The visual above is a simple demonstration of my learning curve experience. With any other IDE, I became semi-productive quite quickly (“semi” is only said in retrospect after knowing what Vim can do..). However, the green Vim curve shows my starting struggle which, after a while turned into an incredible skill.

### [](#how-did-i-do-it)How did I do it?

After a few brutal fights where I returned to my fallback IDE with my tail between my legs, I made a decision to actually LEARN Vim. Here’s how I did it:

1.  Got a [nice small notebook](https://www.baronfig.com/products/shopconfidant?variant=35638867020) I could carry around
    
2.  I bought the [awesome Practical Vim by Drew Neil](https://www.amazon.com/Practical-Vim-Thought-Pragmatic-Programmers/dp/1934356980/) both in hardcover and for my iPad to read on the move
    
3.  Every night before going to bed, I read one tip — the book is very intelligently built like that for easy, slow studying
    
4.  The IDEs on my mac were removed, no more VSCode or PyCharm's arms to run back to. It was Vim alone
    
5.  I’ve signed up for “[Mastering Vim Quickly](https://jovicailic.org/mastering-vim-quickly/)” newsletter and followed them on [Twitter](https://twitter.com/MasteringVim), where I was constantly learning new tips
    
6.  I’ve started my online list of tips I learned and picked up on the way, which I maintain to this day  
    [**Talking about new tips**, they are endless](https://github.com/omerxx/vim-notebook/blob/master/VIM_NOTEBOOK.md): even after years of work you’ll find yourself applauding another feature you never knew of. Vim is an infinite jar of candy
    

[![Rotating the joke on VIM… don’t quit the fight; it’s worth it](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0zlqwx7981nqcwj8zp9m.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0zlqwx7981nqcwj8zp9m.png)_Rotating the joke on VIM… don’t quit the fight; it’s worth it_

### [](#gradual-learning)Gradual learning

After a few days of reading, I slowly started getting the grasp of movement in Vim using the famous `hjkl`, and learned to search and save keystrokes. I began understanding how Vim _operates_. What's the fastest and most elegant way for doing every single change. I started finding myself getting out of bed after reading a tip to try it out and writing it down in my notebook.

Diving right in may not be for everyone. If you’re not yet willing to drop everything else and use Vim alone, you may want to try out some excellent integrations for IDEs; a popular one is [VSCode’s V](https://github.com/VSCodeVim/Vim)im [mode](https://github.com/VSCodeVim/Vim) which adds most of Vims functionality and abilities right in your beloved (and soon to be ditched 😉) IDE. I tried it and had a hard time finding 100% of the functionality I was used to, so I went straight back to full-on Vim.

## [](#when)When

Funny question to ask, but — right now. You may be launching a new project or starting a new job; these are just a trigger to adopt a new life-changing tool. Nothing has to be dramatic; you can pick it up as you go. As long as you’re consistent and determined, within a few weeks, you’ll get to the point discussed earlier where no other tool is required anymore. You'll be past the point of just being productive: you'll be faster in vim than anything else.

## [](#who)Who

Jokes aside, mastering Vim is a life changer for any writer. Yes, it’s designed to edit code, but I got to a point I’m writing my text there since I feel more confident, productive, and comfortable. Here’s a nice piece: “[Vim for writers](https://hackernoon.com/vim-for-writers-ee15d2a8f512)”.

Whether you’re in IT, DevOps, full-on developer, the occasional script writer (and scriptwriter 😁), or data analyst: everyone can use Vim and enjoy it to the max. I got to write Python, Golang, Crystal, TypeScript Bash and a lot of text (these lines right now, for example). There's no text editing situation I can think of for which vim is not a perfect solution.

## [](#customizing)Customizing

By now, you learned that Vim is one of the most versatile, customizable tools out there. Not only it has endless plugins, but you can also change your configuration file (the .vimrc) and can pretty much change **everything**. Having that said, you may want to start [Vanilla](https://peteraba.com/blog/my-vanilla-vim-cheatsheet/). [Here’s a good video](https://www.youtube.com/watch?v=XA2WjJbmmoM) that can save you a lot of plugin installations just by knowing Vim’s built-in abilities. The one thing that is recommended to use is [Tim Pope](https://dev.toundefined/)’s [Vim-sensible plugin](https://github.com/tpope/vim-sensible).

### [](#plugins)Plugins

Having one of the largest enthusiasts communities out from there, Vim has endless plugins, most of them can be found on GitHub. A word of warning though, while plugins are helpful and enjoyable, they have a few downsides with them:

*   They’re heavy on Vim: you may notice lagging and longer response times with some highly demanding plugins
    
*   They may be conflicting with other plugins/configurations: (usually, you won’t notice that with popular plugins)
    
*   They’re masking some of Vim’s abilities. You install a plugin that has pretty good vanilla functionality in Vim already — Check yourself before running to every shiny plugin
    
*   They may be slowing down your leaning, adopt them with care, slowly, and only when you feel the need
    

Here’s a rather short list of plugins that I use (I try to maintain them by removing the ones I don’t use anymore occasionally). [you can also find the full list of them together with my .vimrc on GitHub.](https://github.com/omerxx/dotfiles/blob/master/vim/.vimrc)

*   [**tpope/vim-sensible**](https://github.com/tpope/vim-sensible) — Sensible configurations discussed above in “customizing”
    
*   [**tpope/vim-surround**](https://github.com/tpope/vim-surround) — Change / create / remove surroundings  
    in VIM: “ < ‘ ( \[
    
*   [**tpope/vim-commentary**](https://github.com/tpope/vim-commentary) — Quickly comment out blocks of code
    
*   [**tpope/vim-fugitive**](https://github.com/tpope/vim-fugitive) — VIM git integration — No reason to ever leave the IDE!
    
*   [**VundleVim/Vundle.vim**](https://github.com/VundleVim/Vundle.vim)— A plugin manager
    
*   [**Valloric/YouCompleteMe**](https://github.com/Valloric/YouCompleteMe) — Much useful integration for autocompletion while producing lines of code
    
*   [**w0rp/ale**](https://github.com/w0rp/ale) — a Basic static code analysis
    
*   [**airblade/vim-gitgutter**](https://github.com/airblade/vim-gitgutter)
    
*   [**junegunn/vim-easy-align**](https://github.com/junegunn/vim-easy-align) — Aligning code by a delimiter
    
*   [**vim-airline/vim-airline**](https://github.com/vim-airline/vim-airline) — A useful toolbar visualizing mode, word count, encoding, etc.
    
*   [**scrooloose/nerdtree**](https://github.com/scrooloose/nerdtree) — A popular but rarely used plugin by myself showing an index tree like most IDEs
    
*   [**junegunn/fzf.vim**](https://github.com/junegunn/fzf.vim) — A better replacement for nerdtree and generally finding files on projects
    
*   [**airblade/vim-rooter**](https://github.com/airblade/vim-rooter) — Sets the root of the project regardless of where Vim was launched from (useful with fzf)
    
*   [**python-mode/python-mode**](https://github.com/python-mode/python-mode) — Python static code analysis (complying with all the PEP right away, a fantastic piece of the addon)
    
*   [**jiangmiao/auto-pairs**](https://github.com/jiangmiao/auto-pairs) — Automatically and conveniently generating the pair of you opening bracket or parentheses
    

* * *

## [](#thats-it-and-thanks-for-making-it-this-far)That’s it, and thanks for making it this far!

I hope this post helps you get started and find your way towards an enjoyable productivity change. I know the internet is full of information and ideas, but since I had to figure out for myself what works best, and made it only after a few attempts, I thought of sharing the process with some other people looking for some guidance. I hope you enjoyed reading and will share this with anyone looking to make his first steps into Vim!

Big thanks to [fuzzymidget](https://www.reddit.com/user/fuzzymidget/) Reddit user who offered his help with styling and language corrections, commenting on [my post](https://www.reddit.com/r/vim/comments/c91090/my_vim_journey_and_suggestions_in_a_blog_posts/) on subreddit `r/vim`.

[I invite you to take a peek at my own .vimrc configuration, suggest changes or take ideas.](https://github.com/omerxx/dotfiles/blob/master/vim/.vimrc)

_My name is Omer, and I am an engineer at [ProdOps](http://prodops.io/) — a global consultancy that delivers software in a Reliable, Secure, and Simple way by adopting the DevOps culture. Let me know your thoughts in the comments below, or connect with me directly on Twitter [**@**omergsr](https://twitter.com/omergsr)._

* * *

##### [](#edit-july-5th)Edit \[July 5th\]:

With his permission, adding [@russellbateman](https://dev.to/russellbateman)'s comment which gives another angle and some insights I couldn't have come up with on my own:

> I have used Vim/vi for 35+ years. One problem in the (rather religious) discussion of editors is that folk only compare editors. Vim/vi isn't merely an editor; it is a full, raging text processor! Mere editors, even really fine ones like Notepad++, typically don't walk very far down the road of text processing. They're present as editors only.  
> Until comparatively recently, IDEs that offered vi compatibility really only offered the skin-deep face of modeful editing--that part of vi that is what puts people off. They did not offer .exrc or .vimrc support nor keystroke power much deeper than the mode. A lot of people were and still are left perplexed as to why anyone would ever be masochistic enough to learn Vim/vi just so they can switch it on in their IDE.  
> Fortunately today, while exhibiting some annoying practices in terms of integration, first-rate IDEs like JetBrains IntelliJ IDEA offer more complete Vim integration than the silliness early IDE attempts made two decades ago. Personally, and because I grew up a UNIX command-line guy, I am not the least bit bashful about popping up a console outside my IDE to run Vim/gVim even though I know that IDEA's vi emulation is probably up to it.  
> Last, I generally never install any plug-ins despite recognizing their utility. I'm not hostile to plug-ins, it's that, just as vi/Vim is everywhere nowdays (and the only game in town on freshly brought-up Linux systems), plug-ins are not ubiquitous, so I don't even think about them until I'm doing something really specialized, not a frequent situation.
