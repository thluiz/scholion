---
url: "https://github.com/git-tips/tips"
captured_at: "2016-08-29T09:18:19-03:00"
title: "git-tips/tips"
domain: "github-com"
---

# git-tips/tips

### README.md

## git-tips

> Collection of `git-tips`, want to add your tips? Checkout [contributing.md](https://github.com/git-tips/tips/blob/master/contributing.md)

[English](http://git.io/git-tips) | [中文](https://github.com/521xueweihan/git-tips)

### **Tools:**

- [git-tip](https://www.npmjs.com/package/git-tip) - A handy CLI to make optimum use of these tips.

P.S: All these commands are tested on `git version 2.7.4 (Apple Git-66)`.

## Everyday Git in twenty commands or so

```
git  everyday
```

## Show helpful guides that come with Git

```
git  -g
```

## Overwrite pull

```
git fetch --all  git reset --hard origin/master
```

## List of all files till a commit

```
git ls-tree --name-only -r commit-ish
```

## Git reset first commit

```
git update-ref -d HEAD
```

## List all the conflicted files

```
git diff --name-only --diff-filter=U
```

## List of all files changed in a commit

```
git diff-tree --no-commit-id --name-only -r commit-ish
```

## Unstaged changes since last commit

```
git diff
```

## Changes staged for commit

```
git diff --cached
```

**Alternatives:**

```
git diff --staged
```

## Show both staged and unstaged changes

```
git diff HEAD
```

## List all branches that are already merged into master

```
git branch --merged master
```

## Quickly switch to the previous branch

```
git checkout -
```

## Remove branches that have already been merged with master

```
git branch --merged master  grep -v   xargs -n 1 git branch -d
```

**Alternatives:**

```
git branch --merged master  grep -v ^\*\|  master  xargs -n 1 git branch -d # will not delete master if master is not checked out
```

## List all branches and their upstreams, as well as last commit on branch

```
git branch -vv
```

## Track upstream branch

```
git branch -u origin/mybranch
```

## Delete local branch

```
git branch -d local_branchname
```

## Delete remote branch

```
git push origin --delete remote_branchname
```

**Alternatives:**

```
git push origin :remote_branchname
```

## Delete local tag

```
git tag -d tag-name
```

## Delete remote tag

```
git push origin :refs/tags/tag-name
```

## Undo local changes with the last content in head

```
git checkout -- file_name
```

## Revert: Undo a commit by creating a new commit

```
git revert commit-ish
```

## Reset: Discard commits, advised for private branch

```
git reset commit-ish
```

## Reword the previous commit message

```
git commit -v --amend
```

## See commit history for just the current branch

```
git cherry -v master
```

## Amend author.

```
git commit --amend --author=Author Name <email@address.com>
```

## Reset author, after author has been changed in the global config.

```
git commit --amend --reset-author --no-edit
```

## Changing a remote's URL

```
git remote set-url origin URL
```

## Get list of all remote references

```
git remote
```

**Alternatives:**

```
git remote show
```

## Get list of all local and remote branches

```
git branch -a
```

## Get only remote branches

```
git branch -r
```

## Stage parts of a changed file, instead of the entire file

```
git add -p
```

## Get git bash completion

```
curl http://git.io/vfhol  /.git-completion.bash   [ -f ~/.git-completion.bash ] && . ~/.git-completion.bash >> /.bashrc
```

## What changed since two weeks?

```
git log --no-merges --raw --since=2 weeks ago
```

**Alternatives:**

```
git whatchanged --since=2 weeks ago
```

## See all commits made since forking from master

```
git log --no-merges --stat --reverse master..
```

## Pick commits across branches using cherry-pick

```
git checkout branch-name  git cherry-pick commit-ish
```

## Find out branches containing commit-hash

```
git branch -a --contains commit-ish
```

**Alternatives:**

```
git branch --contains commit-ish
```

## Git Aliases

```
git config --global alias.handle command 
git config --global alias.st status
```

## Saving current state of tracked files without commiting

```
git stash
```

**Alternatives:**

```
git stash save
```

## Saving current state including untracked files

```
git stash save -u
```

**Alternatives:**

```
git stash save --include-untracked
```

## Show list of all saved stashes

```
git stash list
```

## Apply any stash without deleting from the stashed list

```
git stash apply stash@{n}
```

## Apply last stashed state and delete it from stashed list

```
git stash pop
```

**Alternatives:**

```
git stash apply stash@{0}  git stash drop stash@{0}
```

## Delete all stored stashes

```
git stash clear
```

**Alternatives:**

```
git stash drop stash@{n}
```

## Grab a single file from a stash

```
git checkout stash@{n} -- file_path
```

**Alternatives:**

```
git checkout stash@{0} -- file_path
```

## Show all tracked files

```
git ls-files -t
```

## Show all untracked files

```
git ls-files --others
```

## Show all ignored files

```
git ls-files --others -i --exclude-standard
```

## Create new working tree from a repository (git 2.5)

```
git worktree add -b branch-name path start-point
```

## Create new working tree from HEAD state

```
git worktree add --detach path HEAD
```

## Untrack files without deleting

```
git rm --cached file_path
```

**Alternatives:**

```
git rm --cached -r directory_path
```

## Before deleting untracked files/directory, do a dry run to get the list of these files/directories

```
git clean -n
```

## Forcefully remove untracked files

```
git clean -f
```

## Forcefully remove untracked directory

```
git clean -f -d
```

**Alternatives:**

```
git clean -df
```

## Update all the submodules

```
git submodule foreach git pull
```

**Alternatives:**

```
git submodule update --init --recursive
```

```
git submodule update --remote
```

## Show all commits in the current branch yet to be merged to master

```
git cherry -v master
```

**Alternatives:**

```
git cherry -v master branch-to-be-merged
```

## Rename a branch

```
git branch -m new-branch-name
```

**Alternatives:**

```
git branch -m [old-branch-name] new-branch-name
```

## Rebases 'feature' to 'master' and merges it in to master

```
git rebase master feature  git checkout master  git merge -
```

## Archive the `master` branch

```
git archive master --format=zip --output=master.zip
```

## Modify previous commit without modifying the commit message

```
git add --all  git commit --amend --no-edit
```

## Prunes references to remote branches that have been deleted in the remote.

```
git fetch -p
```

**Alternatives:**

```
git remote prune origin
```

## Retrieve the commit hash of the initial revision.

```
 git rev-list --reverse HEAD  head -1
```

**Alternatives:**

```
git rev-list --max-parents=0 HEAD
```

```
git log --pretty=oneline  tail -1  cut -c 1-40
```

```
git log --pretty=oneline --reverse  head -1  cut -c 1-40
```

## Visualize the version tree.

```
git log --pretty=oneline --graph --decorate --all
```

**Alternatives:**

```
gitk --all
```

## Deploying git tracked subfolder to gh-pages

```
git subtree push --prefix subfolder_name origin gh-pages
```

## Adding a project to repo using subtree

```
git subtree add --prefix=directory_name/project_name --squash git@github.com:username/project_name.git master
```

## Get latest changes in your repo for a linked project using subtree

```
git subtree pull --prefix=directory_name/project_name --squash git@github.com:username/project_name.git master
```

## Export a branch with history to a file.

```
git bundle create file branch-name
```

## Import from a bundle

```
git clone repo.bundle repo-dir -b branch-name
```

## Get the name of current branch.

```
git rev-parse --abbrev-ref HEAD
```

## Ignore one file on commit (e.g. Changelog).

```
git update-index --assume-unchanged Changelog git commit -a git update-index --no-assume-unchanged Changelog
```

## Stash changes before rebasing

```
git rebase --autostash
```

## Fetch pull request by ID to a local branch

```
git fetch origin pull/id/head:branch-name
```

**Alternatives:**

```
git pull origin pull/id/head:branch-name
```

## Show the most recent tag on the current branch.

```
git describe --tags --abbrev=0
```

## Show inline word diff.

```
git diff --word-diff
```

## Show changes using common diff tools.

```
git difftool -t commit1> commit2> path
```

## Don’t consider changes for tracked file.

```
git update-index --assume-unchanged file_name
```

## Undo assume-unchanged.

```
git update-index --no-assume-unchanged file_name
```

## Clean the files from `.gitignore`.

```
git clean -X -f
```

## Restore deleted file.

```
git checkout deleting_commit^ -- file_path
```

## Restore file to a specific commit-hash

```
git checkout commit-ish -- file_path
```

## Always rebase instead of merge on pull.

```
git config --global pull.rebase
```

## List all the alias and configs.

```
git config --list
```

## Make git case sensitive.

```
git config --global core.ignorecase false
```

## Add custom editors.

```
git config --global core.editor $EDITOR
```

## Auto correct typos.

```
git config --global .autocorrect 1
```

## Check if the change was a part of a release.

```
git name-rev --name-only SHA-1>
```

## Dry run. (any command that supports dry-run flag should do.)

```
git clean -fd --dry-run
```

## Marks your commit as a fix of a previous commit.

```
git commit --fixup SHA-1>
```

## Squash fixup commits normal commits.

```
git rebase -i --autosquash
```

## Skip staging area during commit.

```
git commit --only file_path
```

## Interactive staging.

```
git add -i
```

## List ignored files.

```
git check-ignore
```

## Status of ignored files.

```
git status --ignored
```

## Commits in Branch1 that are not in Branch2

```
git log Branch1 ^Branch2
```

## Reuse recorded resolution, record and reuse previous conflicts resolutions.

```
git config --global rerere.enabled 1
```

## Open all conflicted files in an editor.

```
git diff --name-only  uniq  xargs $EDITOR
```

## Count unpacked number of objects and their disk consumption.

```
git count-objects --human-readable
```

## Prune all unreachable objects from the object database.

```
git gc --prune=now --aggressive
```

## Instantly browse your working repository in gitweb.

```
git instaweb [--local] [--httpd=<httpd] [--port=<port] [--browser=<browser]
```

## View the GPG signatures in the commit log

```
git log --show-signature
```

## Remove entry in the global config.

```
git config --global --unset entry-name
```

## Checkout a new branch without any history

```
git checkout --orphan branch_name
```

## Extract file from another branch.

```
git show branch_name:file_name
```

## List only the root and merge commits.

```
git log --first-parent
```

## Change previous two commits with an interactive rebase.

```
git rebase --interactive HEAD~2
```

## List all branch is WIP

```
git checkout master  git branch --no-merged
```

## Find guilty with binary search

```
git bisect start                    # Search start 
git bisect bad                      # Set point to bad commit 
git bisect good v2.6.13-rc2         # Set point to good commit|tag 
git bisect bad                      # Say current state is bad 
git bisect good                     # Say current state is good 
git bisect reset                    # Finish search
```

## Bypass pre-commit and commit-msg githooks

```
git commit --no-verify
```

## List commits and changes to a specific file (even through renaming)

```
git log --follow -p -- file_path
```

## Clone a single branch

```
git clone -b branch-name --single-branch https://github.com/user/repo.git
```

## Create and switch new branch

```
git checkout -b branch-name
```

**Alternatives:**

```
git branch branch-name  git checkout branch-name
```

## Ignore file mode changes on commits

```
git config core.fileMode false
```

## Turn off git colored terminal output

```
git config --global color.ui false
```

## Specific color settings

```
git config --global specific command e.g branch, diff , false or always
```

## Show all local branches ordered by recent commits

```
git for-each-ref --sort=-committerdate --format=%(refname:short) refs/heads/
```

## Find lines matching the pattern (regex or string) in tracked files

```
git grep --heading --line-number foo bar
```

## Clone a shallow copy of a repository

```
git clone https://github.com/user/repo.git --depth 1
```

## Search Commit log across all branches for given text

```
git log --all --grep=<given-text>
```

## Get first commit in a branch (from master)

```
git log master..branch-name --oneline  tail -1
```

## Unstaging Staged file

```
git reset HEAD file-name
```

## Force push to Remote Repository

```
git push -f remote-name branch-name
```

## Adding Remote name

```
git remote add remote-nickname remote-url
```

## Show the author, time and last revision made to each line of a given file

```
git blame file-name
```

## Group commits by authors and title

```
git shortlog
```

## Forced push but still ensure you don't overwrite other's work

```
git push --force-with-lease remote-name branch-name
```

## Show how many lines does an author contribute

```
git log --author=_Your_Name_Here_ --pretty=tformat: --numstat  gawk { add += <!-- @doxie.inject start -->; subs += <!-- @doxie.inject end -->; loc += <!-- @doxie.inject start --> - <!-- @doxie.inject end --> } END { printf "added lines: %s removed lines: %s total lines: %s
", add, subs, loc } -
```

**Alternatives:**

```
git log --author=_Your_Name_Here_ --pretty=tformat: --numstat  awk { add += <!-- @doxie.inject start -->; subs += <!-- @doxie.inject end -->; loc += <!-- @doxie.inject start --> - <!-- @doxie.inject end --> } END { printf "added lines: %s, removed lines: %s, total lines: %s
", add, subs, loc } - # on Mac OSX
```

## Revert: Reverting an entire merge

```
git revert -m 1 commit-ish
```

## Number of commits in a branch

```
git rev-list --count branch-name
```

## Alias: git undo

```
git config --global alias.undo !f() { git reset --hard $(git rev-parse --abbrev-ref HEAD)@{${1-1}}; }; f
```
