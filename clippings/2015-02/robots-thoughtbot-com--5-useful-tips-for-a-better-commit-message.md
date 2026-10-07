---
url: "http://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message"
captured_at: "2015-02-05T21:06:41-03:00"
title: "5 Useful Tips For A Better Commit Message"
domain: "robots-thoughtbot-com"
---

# [5 Useful Tips For A Better Commit Message](http://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message)

You’re already writing decent commit messages. Let’s see if we can level you up
to awesome. Other developers, especially you-in-two-weeks and
you-from-next-year, will thank you for your forethought and verbosity when they
run `git blame` to see why that conditional is there.

1. The first line should always be [50 characters or less](http://stopwritingramblingcommitmessages.com/) and that it
   should be followed by a blank line. Vim ships with syntax, indent, and
   filetype plugins for Git commits which can help here.
2. Add this line to your `~/.vimrc` to add spell checking and automatic wrapping
   at the recommended 72 columns to you commit messages.

   autocmd Filetype gitcommit setlocal spell textwidth=72
3. Never use the `-m <msg>` / `--message=<msg>` flag to `git commit`.

It gives you a poor mindset right off the bat as you will feel that you have
to fit your commit message into the terminal command, and makes the commit
feel more like a one-off argument than a page in history:

```
 git commit -m "Fix login bug"
```

A more useful commit message might be:

```
 Redirect user to the requested page after login

 https://trello.com/path/to/relevant/card

 Users were being redirected to the home page after login, which is less
 useful than redirecting to the page they had originally requested before
 being redirected to the login form.

 * Store requested path in a session variable
 * Redirect to the stored location after successfully logging in the user
```

1. Answer the following questions:

   - **Why is this change necessary?**

   This question tells [reviewers of your pull request](https://github.com/thoughtbot/guides/tree/master/code-review) what to
   expect in the commit, allowing them to more easily identify and point out
   unrelated changes.
   \* **How does it address the issue?**

   Describe, at a high level, what was done to affect change. `Introduce a
   red/black tree to increase search speed` or `Remove <troublesome gem X>,
   which was causing <specific description of issue introduced by gem>` are
   good examples.

   If your change is obvious, you may be able to omit addressing this
   question.
   \* **What side effects does this change have?**

   This is the most important question to answer, as it can point out
   problems where you are making too many changes in one commit or branch.
   One or two bullet points for related changes may be okay, but five or six
   are likely indicators of a commit that is doing too many things.

   Your team should have guidelines and rules-of-thumb for how much can be
   done in a single commit/branch.
2. Consider making including a link to the issue/story/card in the commit
   message a standard for your project. Full urls are more useful than issue
   numbers, as they are more permanent and avoid confusion over which issue
   tracker it references.

This is generally done as the first paragraph after the summary, on line 3.

![git-branching-illustration.png](robots-thoughtbot-com--5-useful-tips-for-a-better-commit-message/fd9467dad174dd7a3111a54875f82357.png)

Having a story in your git log will make a huge difference in how you and others
perceive your project. By taking great care in commit messages, as you do in
your code, you will help to increase overall quality.

Special thanks to Tim Pope, whose [Note About Git Commit Messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
literally sets the standard for a good commit message.

Additional thanks to the creator of Git and a [real stickler for a good commit
message](https://github.com/torvalds/linux/pull/17#issuecomment-5659933), Linus Torvalds.
