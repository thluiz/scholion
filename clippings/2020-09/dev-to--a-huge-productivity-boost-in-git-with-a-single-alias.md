---
url: "https://dev.to/xoubaman/a-huge-productivity-boost-in-git-with-a-singe-alias-3pij"
captured_at: "2020-09-12T19:01:02-03:00"
title: "A huge productivity boost in git with a single alias - DEV Community 👩‍💻👨‍💻"
domain: "dev-to"
---

# A huge productivity boost in git with a single alias

3 de ago. de 2019
・1 min read

> *Small details can make a huge difference* -- Somebody at some point, I guess

Add an alias in your shell to use `g` for `git`. You will save a lot of typing at the end of the day.

```
# in your .bashrc or equivalent
alias g='git'
```

So now you will do `g pull` instead of the extremely verbose `git pull`.

As bonus points, some bits from my Git configuration. All the following is in `~/.gitconfig`:

- Using a global `.gitignore` with the usual suspects (.DS\_Store, Thumbs.db, etc.)

```
[core]
excludesfile = ~/.gitignore-global
```

- I always want to `pull --rebase`, so I have it enabled by default:

```
[pull]
    rebase = true
```

- Git comes with a pretty much unknown autocorrect feature. If you mistype some command, it will execute it after some configured time. Enable it with the tenths of a second to do so:

```
[help]
    autocorrect = 5
```

- And my current list of git aliases, in case it is inspiring to somebody. They print the actual command to do not forget what I am doing:

```
[alias]
    s        = !echo 'git status -s' && git status -s
    aa       = !echo 'git add .' && git add .
    c        = !echo 'git commit -m' && git commit -m
    co       = !echo 'git checkout' && git checkout
    amend    = !echo 'git commit --amend --no-edit' && commit --amend --no-edit
    amendall = !echo 'git add . && git commit --amend --no-edit' && git add . && git commit --amend --no-edit
    syncwith = !echo 'git pull --rebase origin' && git pull --rebase origin
    lg       = log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)%Creset' --abbrev-commit
```

Final advice: try to optimize what you do over and over again during the day.
