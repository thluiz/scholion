---
url: "http://blog.rlmflores.me/git/2015/03/31/8-small-git-tips/"
captured_at: "2015-04-01T10:59:05-03:00"
title: "8 Small git tips · Rodrigo Flores's Corner"
domain: "blog-rlmflores-me"
---

# 8 Small git tips

31 Mar 2015

As git is one of my daily tools, I've compiled 8 useful (and short) tips that I use almost everyday.

## Selectively add with -p

When you want to commit something, you can either: select all the files through `git commit -am` or add a specific file through `git add file`. However, you may want to only add only a part of a file to the commit. You can use `git add -p` and select interactively what parts you want to add to your commit.

After selecting interactively all the chunks you want to commit, just do a git commit (without `-a`) and you will only commit the selected parts. There is also the `git checkout -p` to select changes to be reverted. After adding, you can see what you have selected using `git diff --cached`.

## Interactive Rebase

If you're working on a branch and you made some WIP commits that you want to squash or you want to remove a commit plus the reversion of this commit, you can do a interactive rebase to reorganize your commits.

To do it, you just need to run `git rebase -i <commit>` where the `<commit>` is the sha1 of a commit before the one you want begin rewriting. Then it will open on your editor (the one specified on `$EDITOR` env var or the one specified on your git config) some instructions to change your commits history where you can pick, squash (merge two commits on a single one), reword (change the commit message), edit or even remove a commit.

Be aware that this change the history, so if you have pushed this commits, you will have to force to push it again, so never do this on master branches or branches that you're not the only one using.

## Stashing

If you in the middle of something and you have to change a context to fix something else, you can `git stash` the current changes. However, you may end up forgetting about this stashed changes some time later. So I try to keep a stash zero (just like inbox zero but for stashes) policy. Every time I have a stash a dollar sign appears on my prompt and then I check it through `git stash show -p` and then I can pop it through `git stash pop` or discard it through `git stash clear`.

## Global gitignore

You can specify what files git should ignore through a `.gitignore` file on the root of a project. But if you have files that git should ignore but you're the only one that generates that files (like vim's bkp files or something that your editor or OS generates like `.DS_Store` files for OSX), you can specify on your configure a global gitignore file that uses the same syntax of a project `.gitignore` that will .

```
git config --global core.excludesfile=/Users/flores/.gitignore
```

## Warn whitespace

I have to admit: sometimes I forget some trailing whitespaces on my code. But I normally don't commit them because I use this option: `apply.whitespace=warn`. Every time I'm adding a chunk of a file through `git add -p`, and this chunk contains trailing whitespaces, git warns me of it so I can fix it before committing.

## Auto setup rebase

Another cool tip is to auto setup rebase: if you have a branch with some commits that aren't pushed and someone else also commits and pushes on that branch, when you pull, git will create a commit merging your commits to the commits upstream. As this commit is meaningless, I prefer to setup auto rebase on pull through the configuration: `branch.autosetuprebase=always`. Doing so, on every pull, git will try to reapply your commits with the current version of the upstream branches.

## Better logging

Have you tried to find an specific commit merged from a branch ? `git log` provides some basic information, but you can use git log with a more useful message:

```
git log --graph --decorate --pretty=oneline --abbrev-commit
```

`--graph` will generate lines between commits and will expose branches, `--decorate` shows where branches are located in this commits, `--pretty=oneline` will show only the `sha1` and the title line and `--abbrev-commit` will reduce the sha1 to the first 7 chars (which is normally unique in your repository). You can check a more detailed explanation of these options (and a whole lot more) on [explain shell](http://explainshell.com/explain?cmd=git+log+--graph+--decorate+--pretty%3Doneline+--abbrev-commit).

## Rewrite a commit message

So you've commited something but did a poor job describing it. Or else, you just made a typo. You can rewrite the message with `git commit --amend`. You can use the `-m` to set a message through the command line or it will open the default editor with the commit message so you can change. You can also include new things with git add and add it to the previous commit. Remember that just like `Interactive Rebase`, it changes the history, so if you have pushed that commit, you will need to force push this changes.

If you use git on your job, you probably know a git trick that increases your productivity. Can you share it on the comments ?
