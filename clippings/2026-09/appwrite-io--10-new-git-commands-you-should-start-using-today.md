---
url: "https://appwrite.io/blog/post/10-git-commands-you-should-start-using"
captured_at: "2026-09-23T17:39:29+01:00"
title: "10 new Git commands you should start using today · Appwrite"
domain: "appwrite.io"
---

10 new Git commands you should start using today_

Learn these Git commands to make your workflow smoother, faster, and flexible.

Ebenezer Don

Developer Advocate

DEC 12, 2024
10 MIN READ

If you've worked with Git long enough, you've probably hit some common frustrations like operations getting slower as repositories grow, accidentally overwriting changes when switching branches, or struggling with massive monorepos.

Thankfully, just like every other tool, Git is constantly evolving and adding new features to make our lives easier. While some of these commands aren't particularly recent, they remain lesser-known gems that can significantly improve your workflow. If you're already familiar with some of the core tips and tricks (like those covered in 15 Git command line tips every developer should know), this article will introduce you to ten additional commands that can take your Git skills to the next level.

1. git switch - A safer way to change branches

Before Git 2.23, git checkout was the main command for switching branches, but it did much more than that. You could use it to restore files, create branches, or check out specific commits. This made it powerful but potentially confusing - especially when you just wanted to switch branches without touching your files.

That's why Git 2.23 introduced git switch as a more focused alternative for branch operations. With git switch, you can focus solely on branch management:

Bash
Copy
# Move to another branch
git switch feature-branch

# Create and switch to a new branch
git switch -c new-branch



This clarity reduces the risk of accidentally overwriting files or making unintended changes. If you've ever hesitated to use git checkout for fear of doing something wrong, git switch simplifies the process.

2. git restore - Safely undo changes

Undoing changes often involved using git checkout to revert files or git reset to move the branch HEAD. However, both commands had the potential to alter your branch state if used incorrectly: git reset could move your branch HEAD, while git checkout could switch branches or check out a different commit, disrupting the current branch.

Git 2.23 introduced git restore to focus solely on undoing changes to files. It provides a safer and more straightforward way to revert changes in your working directory or staging area, clearly separating file operations from branch management tasks:

Bash
Copy
# Discard working directory changes
git restore main.js

# Unstage changes from the index
git restore --staged main.js



This is especially useful for beginners or in high-stakes situations where precision matters. You can undo changes without worrying about accidentally switching branches or resetting commits.

3. git maintenance - Automate repository health

As repositories grow, performance can degrade. Operations like git fetch, git status, or git log may slow down, and unused data can clutter your repository. Before Git 2.29, you'd have to manually run commands like git gc (garbage collection) or git repack to keep your repository optimized.

Git 2.29 introduced git maintenance, which automates these tasks for you:

Bash
Copy
# Enable automatic maintenance
git maintenance start

# Run cleanup tasks immediately
git maintenance run



What's happening behind the scenes?

Garbage Collection: Removes unreachable objects, such as commits discarded during rebases or branch deletions.
Repacking: Consolidates fragmented packfiles for better storage efficiency.
Commit Graph Updates: Optimizes commit history traversal, speeding up commands like git log and git blame.

Using git maintenance will help you keep your repository healthy without manual effort.

4. git sparse-checkout - Efficiently handle large repositories

Monorepos are great for managing multiple projects, but cloning an entire repository when you only need a specific directory can be inefficient. Git 2.25 introduced git sparse-checkout to solve this.

Bash
Copy
# Enable sparse-checkout mode
git sparse-checkout init

# Fetch only specific directories
# You can specify multiple directories separated by spaces
git sparse-checkout set services/ docs/



With git sparse-checkout, you can include only the directories or files you need in your working directory, leaving the rest untouched. This is useful for large teams working on distinct parts of a monorepo, and will save you time and disk space.

5. git log --remerge-diff: Understand merges better

Merge commits often show which branches were merged, but they don't always explain the specific changes introduced, especially when conflicts were resolved during the merge.

Starting with Git 2.35, you can use:

Bash
Copy
git log --remerge-diff

This option reconstructs the merge commit by replaying the recorded merge strategy and showing the exact changes it introduced. It's useful for debugging merge conflicts or reviewing a complicated merge history.

6. git blame --ignore-rev - Ignore noisy commits

When your team makes a bulk formatting change, git blame can lose its utility, as every line ends up pointing to the formatting commit instead of the original author.

Introduced in Git 2.23, the --ignore-rev option allows you to exclude such commits:

Bash
Copy
git blame --ignore-rev commit-hash



To persist this exclusion, you can set up an ignore-revs file:

Bash
Copy
# Add the commit hash to the ignore-revs fileecho commit-hash >> .git-blame-ignore-revs

# Tell Git to use the file
git config blame.ignoreRevsFile .git-blame-ignore-revs



This helps you focus on meaningful authorship and can be useful in codebases with frequent style updates.

7. git range-diff - Compare and track changes between commit ranges

Rewriting history, whether through rebasing, cherry-picking, or interactive editing, can be tricky. After a rebase, you might wonder how the rewritten commits differ from the originals. git range-diff helps by comparing two commit ranges, showing how one evolved into the other and highlighting changes to individual commits:

Bash
Copy
git range-diff



This command can be used to understand the evolution of a feature or bug fix across different branches.

8. git worktree - Work on multiple branches simultaneously

Switching branches in a single working directory can disrupt your workflow, especially when you need to work across multiple branches. With git worktree, you can create additional working directories tied to the same repository.

Bash
Copy
# Add a new worktree for a specific branch
git worktree add ../feature-branch feature-branch

# Remove a worktree when you're done
git worktree remove ../feature-branch



git worktree allows you to work on different branches without switching or stashing. You can also create throwaway worktrees with detached HEADs for testing, or isolate builds and deployments in separate working directories.

9. git rebase --update-refs - Keep references in sync

Rebasing rewrites history by replacing old commits with new ones, but this often leaves branch pointers or tags referencing outdated commits. Git 2.38 introduces the --update-refs option to handle this automatically:

Bash
Copy
git rebase --update-refs



With this command, Git ensures that related branches and tags referencing rewritten commits are updated to match the new history. This eliminates the need for tedious manual updates and ensures consistency across your repository.

For even more control, you can configure git rebase to always update specific refs by setting:

Bash
Copy
git config rebase.updateRefs true



This is useful in collaborative workflows or when managing multiple refs tied to the same history.

10. git commit --fixup and git rebase --autosquash - Fixup commits

While not a new feature (introduced in Git 1.7.4, back in 2011), git commit --fixup is often overlooked despite being a useful tool for maintaining clean commit histories. When working on a feature, you might realize that you need to fix or improve a previous commit. Manually editing your commit history to include these changes can lead to errors. Git provides git commit --fixup and git rebase --autosquash to automate this process.

Bash
Copy
# Create a fixup commit targeting a specific commit
git commit --fixup=<commit-hash>

# Later, during an interactive rebase, automatically squash fixup commits
git rebase -i --autosquash <base-branch>



The --fixup option creates a commit that's marked to be automatically squashed into the target commit during an interactive rebase with --autosquash. This streamlines the process of cleaning up your commit history before merging changes, and will ensure that related changes are grouped together without manual effort.

Conclusion

The commands we've discussed in this article can help you solve real problems you might be facing every day as a Git user. Whether you're managing a monorepo, handling large histories, or trying to keep your repository clean, these practical solutions can make a difference. Start with one or two that fit your current workflow, and you might be surprised by the improvements in your productivity.

If you liked this article, you might also enjoy 15 Git command line tips every developer should know.

More resources

How to implement Sign in with GitHub

SQL vs NoSQL: Choosing the right database for your project

Deno 2 vs Bun: which JavaScript runtime is right for you?

Frequently asked questions
