---
url: "https://dev.to/tmr232/dont-amend-fix"
captured_at: "2017-04-11T11:15:08-03:00"
title: "Don't Amend, Fix"
domain: "dev-to"
---

# Don't Amend, Fix

### 

[git](https://dev.to/t/git)

As git users, we know that we should "commit early, commit often." While this is a wonderful thing to do, it does mean that from time to time we make a mistake and need to fix a commit. Maybe we forget to `git add` a new file, or missed a typo. So we go ahead and `git commit --amend`. Problem solved. Great.

But personally, I hate it.

For one thing, amending commits hides history. Once you amend, that past state is gone before you can properly test the new one. True, you can also restore it via `git reflog`, but no-one really likes using that. It should be a last resort.

For another thing, amending is very limited. Say I am writing some C code. I write my first module, add it and commit.

```
git add FirstModule.h
git commit -m "Added FirstModule"
```

I write my second module, and add it as well.

```
git add SecondModule.h SecondModule.c
git commit -m "Added SecondModule"
```

And now, after adding that second commit, I realize that I forgot to commit `FirstModule.c`. `git commit --amend` to the rescue? Not really. I now have to resort to the black, frightening voodoo magic called `git rebase`.

First, we commit the forgotten module

```
git add FirstModule.c
git commit -m "Added FirstModule.c, forgotten eariler."
```

And then rebase - `git rebase -i HEAD~3`

```
pick1db8687AddedFirstModule
pick336941bAddedSecondModule
pick7884909AddedFirstModule.c,forgotteneariler.
```

Change to

```
pick1db8687AddedFirstModule
fixup7884909AddedFirstModule.c,forgotteneariler.
pick336941bAddedSecondModule
```

Save & Quit, and we're done.

```
*1946e37d105ffebcbd91bb958f8a2fce6160c761(HEAD->master)AddedSecondModule
|createmode100644SecondModule.c
|createmode100644SecondModule.h
*8ffbb9f2915e060a6c4771e13f5a82442743724cAddedFirstModule
|createmode100644FirstModule.c
|createmode100644FirstModule.h
*815e7bab6ee1fa5bf1df10f5705919b48cbe214cFirstCommit
```

Not that hard, is it?

But still, moving between amending and rebasing can be cumbersome. Especially as most of the time there is no real need to rebase and it's easy to forget the process. Enter `git commit --fixup` (or `--squash`) and `git rebase -i --autosquash`.

These commands save us the work of reordering the commits and changing from `pick` to `fixup` or `squash`. Making our rebasing work a lot easier.

I like defining the following aliases:

```
[alias]
    ri = rebase -i --autosquash
    mri = rebase -i
    fix = commit --fixup
    squ = commit --squash
```

Using those aliases, the rebasing we did earlier would work as follows:

```
git add FirstModule.c
git fix HEAD~1
git ri HEAD~3
```

We'd get the following rebase automatically

```
pick1db8687AddedFirstModule
fixup50a3650fixup!AddedFirstModule
pick336941bAddedSecondModule
```

Exit the editor, and be done with it.

We can use `fix` as many times as we want (just go ahead and `git fix HEAD -a`) before the rebase. Our log may look funny

```
*fe0c2a0(HEAD->master)fixup!fixup!fixup!fixup!AddedSecondModule
*a53cd32fixup!fixup!fixup!AddedSecondModule
*9c19f2dfixup!fixup!AddedSecondModule
*b758a53fixup!AddedSecondModule
*902d65eAddedSecondModule
*67f1260AddedFirstModule
*815e7baFirstCommit
```

But the rebase doesn't care

```
pick902d65eAddedSecondModule
fixupb758a53fixup!AddedSecondModule
fixup9c19f2dfixup!fixup!AddedSecondModule
fixupa53cd32fixup!fixup!fixup!AddedSecondModule
fixupfe0c2a0fixup!fixup!fixup!fixup!AddedSecondModule
```

## Conclusion

Stop using `git commit --amend` and start using `git fix` (`git commit --fixup`) instead. It is a no-fear, low-overhead alternative, and it far more flexible.  
Here are the aliases again, in case you want them:

```
[alias]
    ri = rebase -i --autosquash
    mri = rebase -i
    fix = commit --fixup
    squ = commit --squash
```
