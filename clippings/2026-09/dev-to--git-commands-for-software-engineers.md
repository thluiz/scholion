---
url: "https://dev.to/iamcymentho/git-commands-for-software-engineers-51n8?context=digest"
captured_at: "2026-09-25T00:07:53+01:00"
title: "Git Commands for Software Engineers"
domain: "dev-to"
---

## [](#introduction)Introduction

Git is an essential tool for software engineers, enabling efficient version control, collaboration, and project management. Whether you're working on a solo project or part of a large team, mastering Git commands is crucial for streamlining your development workflow. This guide covers the most common Git commands you'll need, providing a solid foundation for managing your codebase, tracking changes, and coordinating with other developers. By familiarizing yourself with these commands, you can enhance your productivity and ensure smooth project progress. Let's dive into the key Git commands every software engineer should know.

**Configuration**

> **1\. git config**  
> `Purpose: Configure Git settings, such as user name and email.`
> 
> ```
> Example: git config --global user.name "Your Name"
> ```
> 
> **2\. git init**  
> `Purpose: Initialize a new Git repository.`
> 
> ```
> Example: git init
> ```
> 
> **3\. git clone**  
> `Purpose: Clone an existing repository.`
> 
> ```
> Example: git clone https://github.com/user/repo.git
> ```
> 
> **4\. git status**  
> `Purpose: Show the working directory and staging area status.`
> 
> ```
> Example: git status
> ```
> 
> **5\. git add**  
> `Purpose: Add file contents to the index (staging area).`
> 
> ```
> Example: git add . (add all files)
> ```
> 
> **6\. git commit**  
> `Purpose: Record changes to the repository.`
> 
> ```
> Example: git commit -m "Commit message"
> ```
> 
> **7\. git push**  
> `Purpose: Update remote refs along with associated objects.`
> 
> ```
> Example: git push origin main
> ```
> 
> **8\. git pull**  
> `Purpose: Fetch from and integrate with another repository or local branch.`
> 
> ```
> Example: git pull origin main
> ```
> 
> **9\. git branch**  
> `Purpose: List, create, or delete branches.`
> 
> ```
> Example: git branch new-branch (create new branch)
> ```
> 
> **10\. git checkout**  
> `Purpose: Switch branches or restore working tree files.`
> 
> ```
> Example: git checkout new-branch (switch to branch)
> ```
> 
> **11\. git switch**  
> `Purpose: Switch branches.`
> 
> ```
> Example: git switch new-branch
> ```
> 
> **12\. git merge**  
> `Purpose: Join two or more development histories together.`
> 
> ```
> Example: git merge new-branch (merge new-branch into current branch)
> ```
> 
> **13\. git rebase**  
> `Purpose: Reapply commits on top of another base tip.`
> 
> ```
> Example: git rebase main
> ```
> 
> **14\. git log**  
> `Purpose: Show commit logs.`
> 
> ```
> Example: git log --oneline
> ```
> 
> **15\. git diff**  
> `Purpose: Show changes between commits, commit and working tree, etc.`
> 
> ```
> Example: git diff (show unstaged changes)
> ```
> 
> **16\. git show**  
> `Purpose: Show various types of objects.`
> 
> ```
> Example: git show HEAD (show changes in the last commit)
> ```
> 
> **17\. git stash**  
> `Purpose: Stash the changes in a dirty working directory away.`
> 
> ```
> Example: git stash
> ```
> 
> **18\. git stash pop**  
> `Purpose: Apply the changes recorded in the stash to the working directory.`
> 
> ```
> Example: git stash pop
> ```
> 
> **19\. git clean**  
> `Purpose: Remove untracked files from the working directory.`
> 
> ```
> Example: git clean -fd
> ```
> 
> **20\. git remote**  
> `Purpose: Manage set of tracked repositories.`
> 
> ```
> Example: git remote add origin https://github.com/user/repo.git
> ```
> 
> **21\. git fetch**  
> `Purpose: Download objects and refs from another repository.`
> 
> ```
> Example: git fetch origin
> ```
> 
> **22\. git remote -v**  
> `Purpose: Show the URLs that a remote name corresponds to.`
> 
> ```
> Example: git remote -v
> ```
> 
> **23\. git tag**  
> `Purpose: Create, list, delete, or verify a tag object.`
> 
> ```
> Example: git tag -a v1.0 -m "Version 1.0"
> ```
> 
> **24\. git push origin --tags**  
> `Purpose: Push all tags to the remote repository.`
> 
> ```
> Example: git push origin --tags
> ```
> 
> **25\. git reset**  
> `Purpose: Reset current HEAD to the specified state.`
> 
> ```
> Example: git reset --hard HEAD~1 (reset to previous commit)
> ```
> 
> **26\. git revert**  
> `Purpose: Create a new commit that undoes the changes from a previous commit.`
> 
> ```
> Example: git revert HEAD
> ```
> 
> **27\. git checkout --**  
> `Purpose: Discard changes in the working directory.`
> 
> ```
> Example: git checkout -- file.txt (discard changes in file.txt)
> ```
> 
> **28\. git cherry-pick**  
> `Purpose: Apply the changes introduced by some existing commits.`
> 
> ```
> Example: git cherry-pick <commit-hash>
> ```
> 
> **29\. git branch -d**  
> `Purpose: Delete a branch.`
> 
> ```
> Example: git branch -d branch-name
> ```
> 
> **30\. git branch -D**  
> `Purpose: Force delete a branch.`
> 
> ```
> Example: git branch -D branch-name
> ```
> 
> **31\. git merge --no-ff**  
> `Purpose: Create a merge commit even when the merge resolves as a fast-forward.`
> 
> ```
> Example: git merge --no-ff new-branch
> ```
> 
> **32\. git rebase -i**  
> `Purpose: Start an interactive rebase.`
> 
> ```
> Example: git rebase -i HEAD~3
> ```
> 
> **33\. git diff --staged**  
> `Purpose: Show changes between the index and the last commit.`
> 
> ```
> Example: git diff --staged
> ```

**34\. git blame**

`Purpose: Show what revision and author last modified each line of a file.`  

```
Example: git blame file.txt

```

Enter fullscreen mode Exit fullscreen mode

> **35\. git log --graph**  
> `Purpose: Show a graph of the commit history.`
> 
> ```
> Example: git log --graph --oneline
> ```
> 
> **36\. git reflog**  
> `Purpose: Show a log of all references.`
> 
> ```
> Example: git reflog
> ```
> 
> **37\. git stash list**  
> `Purpose: List all stashes.`
> 
> ```
> Example: git stash list
> ```
> 
> **38\. git stash apply**  
> `Purpose: Apply a stash to the working directory.`
> 
> ```
> Example: git stash apply stash@{1}
> ```
> 
> **39\. git stash drop**  
> `Purpose: Remove a single stash entry from the list of stashes.`
> 
> ```
> Example: git stash drop stash@{1}
> ```
> 
> **40\. git remote show**  
> `Purpose: Show information about the remote repository.`
> 
> ```
> Example: git remote show origin
> ```
> 
> **41\. git remote rm**  
> `Purpose: Remove a remote.`
> 
> ```
> Example: git remote rm origin
> ```
> 
> **42\. git pull --rebase**  
> `Purpose: Fetch and rebase the current branch on top of the upstream branch.`
> 
> ```
> Example: git pull --rebase origin main
> ```

**43\. git fetch --all**

`Purpose: Fetch all remotes.`  

```
Example: git fetch --all
```

Enter fullscreen mode Exit fullscreen mode

> **44\. git bisect**  
> `Purpose: Use binary search to find the commit that introduced a bug.`
> 
> ```
> Example: git bisect start
> ```
> 
> **45\. git submodule**  
> `Purpose: Initialize, update, or inspect submodules.`
> 
> ```
> Example: git submodule update --init
> ```
> 
> **46\. git archive**  
> `Purpose: Create an archive of files from a named tree.`
> 
> ```
> Example: git archive --format=tar HEAD > archive.tar
> ```
> 
> **47\. git shortlog**  
> `Purpose: Summarize git log output.`
> 
> ```
> Example: git shortlog -s -n
> ```

**48\. git describe**

`Purpose: Give an object a human-readable name based on an available ref.`  

```
Example: git describe --tags
```

Enter fullscreen mode Exit fullscreen mode

> **49\. git rev-parse**  
> `Purpose: Parse revision (or other objects) and retrieve its hash.`
> 
> ```
> Example: git rev-parse HEAD
> ```
> 
> **50\. git tag -d**  
> `Purpose: Delete a tag from the local repository.`
> 
> ```
> Example: git tag -d v1.0
> ```
> 
> **51\. git checkout -b**  
> `Purpose: Create and switch to a new branch.`
> 
> ```
> Example: git checkout -b new-branch
> ```
> 
> **52\. git push origin --delete**  
> `Purpose: Delete a remote branch.`
> 
> ```
> Example: git push origin --delete branch-name
> ```
> 
> **53\. git cherry**  
> `Purpose: Find commits not merged upstream.`
> 
> ```
> Example: git cherry -v
> ```
> 
> **54\. git rm**  
> `Purpose: Remove files from the working tree and from the index.`
> 
> ```
> Example: git rm file.txt
> ```
> 
> **55\. git mv**  
> `Purpose: Move or rename a file, directory, or symlink.`
> 
> ```
> Example: git mv oldname.txt newname.txt
> ```
> 
> **.56 git reset HEAD**  
> `Purpose: Unstage changes.`
> 
> ```
> Example: git reset HEAD file.txt
> ```
> 
> **57\. git log -p**  
> `Purpose: Show changes over time for a specific file.`
> 
> ```
> Example: git log -p file.txt
> ```
> 
> **58\. git diff --cached**  
> `Purpose: Show changes between the index and the last commit (same as --staged).`
> 
> ```
> Example: git diff --cached
> ```
> 
> **59\. git apply**  
> `Purpose: Apply a patch to files and/or to the index.`
> 
> ```
> Example: git apply patch.diff
> ```
> 
> **60\. git format-patch**  
> `Purpose: Prepare patches for e-mail submission.`
> 
> ```
> Example: git format-patch -1 HEAD
> ```
> 
> **61\. git am**  
> `Purpose: Apply a series of patches from a mailbox.`
> 
> ```
> Example: git am < patch.mbox
> ```
> 
> **62\. git cherry-pick --continue**  
> `Purpose: Resume cherry-picking after resolving conflicts.`
> 
> ```
> Example: git cherry-pick --continue
> ```
> 
> **63\. git fsck**  
> `Purpose: Verify the connectivity and validity of objects in the database.`
> 
> ```
> Example: git fsck
> ```
> 
> **64\. git gc**  
> `Purpose: Cleanup unnecessary files and optimize the local repository.`
> 
> ```
> Example: git gc
> ```
> 
> **65\. git prune**  
> `Purpose: Remove unreachable objects from the object database.`
> 
> ```
> Example: git prune
> ```
> 
> **66\. git notes**  
> `Purpose: Add or inspect object notes.`
> 
> ```
> Example: git notes add -m "Note message"
> ```
> 
> **67\. git whatchanged**  
> `Purpose: Show what changed, similar to git log.`
> 
> ```
> Example: git whatchanged
> ```
> 
> \*_68\. git show-branch \*_  
> `Purpose: Show branches and their commits.`
> 
> ```
> Example: git show-branch
> ```
> 
> **69\. git verify-tag**  
> `Purpose: Check the GPG signature of tags.`
> 
> ```
> Example: git verify-tag v1.0
> ```
> 
> **70\. git show-ref**  
> `Purpose: List references in a local repository.`
> 
> ```
> Example: git show-ref
> ```

`LinkedIn Account` : [LinkedIn](https://www.linkedin.com/in/matthew-odumosu/)  
`Twitter Account`: [Twitter](https://twitter.com/iamcymentho)  
**Credit**: Graphics sourced from [LinkedIn](https://www.linkedin.com/pulse/day-8-basic-git-github-devops-kartik-bhatt-caphf/)
