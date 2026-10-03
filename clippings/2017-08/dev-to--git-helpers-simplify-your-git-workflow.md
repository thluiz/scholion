---
url: "https://dev.to/gyandeeps/git-helpers---simplify-your-git-workflow"
captured_at: "2017-08-15T14:18:47-03:00"
title: "Git helpers - Simplify your git workflow"
domain: "dev-to"
---

# Git helpers - Simplify your git workflow

### 

*This was originally posted [here](https://gyandeeps.com/git-helpers/)*

Being a git lover, I got tired of typing same commands over and over again. This motivated me to build some alias for my git workflow I use every day. Most of the alias was inherited from [Nicholas C. Zakas's gist](https://gist.github.com/nzakas/c6c98856a5eac76f06e3#file-alias-sh). I took that a step further by creating more alias which I use every time I contribute to open source projects like [Eslint](http://eslint.org/).

## Commands

Actual code for all the commands is [here](https://gist.github.com/gyandeeps/c7872187585de4fa7153)

### Work on an issue

When you plan to work on an issue on an open source project, you will want to create a new branch on your project and then start work on it. For that you have to go through couple of steps. To stream line that process now on top of your project you can just run the command:

```
ws 34
```

This command will update the master branch with the updates from the remote and then create a new branch on it with name `issue34`.

### Remove a branch after work is done

Once you are done with your work on the branch. Then you can simply run the below command to delete the branch from local and remote git.

```
wd 34
```

### Update your branch (all changes commited) with master

let’s say after working on your branch, you want to update your branch with latest content from the master. This is important in scenarios where you want to rebase your branch with latest content from `master` branch.

```
update
```

### Update your branch (uncommited changes) with master

let’s say after working on your branch, you want to update your branch with latest content from the master. But at this time you have not commited your changes. Using `updateD`, it will stash your changes then update your branch from master and then pick the changes from stash and apply it back on the current branch.

```
updateD
```

### Squash your commits

I always prefer to keep my changes history clean by squashing my commits. Once you are working on a branch and you want to squash your commits, simple run the following command to rebase. You can pass in a parameter of how many commits you want to include in your rebase from the HEAD. By default it will run rebase on last 2 commits.

```
rebase 4 # This will rebase on last 4 commits, default is 2
```

### Push your changes to remote

After you have finished your work, you want to push your changes to remote. Here mostly you will be doing a regular `push` but if you have done some rebases on your branch then your only option is to `force push`. We use `--force-with-lease` flag for force ppush just to be little more safe.

Regular push:

```
push # This will push your branch changes but will not push on master
```

Force push:

```
fpush # This will push your branch changes but will not push on master
```

Both commands will not allow you to push it to master because it considered a good practice to always branch off your changes and then merge it to master using a PR. This is completely my view.

### Pull changes from origin

Running this command will pull thhe changes from upstream and merge them into thhe current branch. It uses `--rebase --prune` flags.

```
pull
```

### Update fork

Quick way to update your fork from the upstream repo. It will go to the master branch, get thhe upstream master, merge that upstream master into local master and then push thhe master to origin master. Its a complete cycle.

```
uf
```

It expects you to setup `upstream` before running this command.

### Quick commit

Quick way to commit your changes by supplying the commit message. Itt will add the currently changed files using the `-a` flag.

```
c "<message>"
```

### Log commits

Quick and easy way to view your commit log in oneline. Its formatted in a way where you can see the commit message, date and author along with some other info.

```
log
```

### Git status

Get the current status of the branch.

```
s
```

## Setup

To use all these command, follow the steps below to setup:

1. Go to your user directory, for windows user it will be `C:\Users\<your user>`.
2. Create a `.bashrc` file, if you do not have that file.
3. Add/append the content from the below gist to that file.
4. Open bash window. If already open then close it and then reopen bash window.
5. Run `alias` command and you should see the list of all the alias defined.

**Note:** Feel free to change the function based on your need.

## Gist for all the above commands

[Click here to see the gist](https://gist.github.com/gyandeeps/c7872187585de4fa7153)

I hope this helps people to streamline their git workflows. Please share your suggestions.
