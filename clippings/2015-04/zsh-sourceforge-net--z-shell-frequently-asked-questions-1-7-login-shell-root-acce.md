---
url: "http://zsh.sourceforge.net/FAQ/zshfaq01.html#l3"
captured_at: "2015-04-03T19:29:05-03:00"
title: "Z-Shell Frequently-Asked Questions"
domain: "zsh-sourceforge-net"
---

## 1.7: I don't have root access: how do I make zsh my login shell?

Unfortunately, on many machines you can't use `chsh` to change your
shell unless the name of the shell is contained in /etc/shells, so if
you have your own copy of zsh you need some sleight-of-hand to use it
when you log on. (Simply typing `zsh` is not really a solution since
you still have your original login shell waiting for when you exit.)

The basic idea is to use `exec <zsh-path>` to replace the current
shell with zsh. Often you can do this in a login file such as .profile
(if your shell is sh or ksh) or .login (if it's csh). Make sure you
have some way of altering the file (e.g. via FTP) before you try this as
`exec` is often rather unforgiving.

If you have zsh in a subdirectory `bin` of your home directory,
put this in .profile:

```
    [ -f $HOME/bin/zsh ] && exec $HOME/bin/zsh -l
```

or if your login shell is csh or tcsh, put this in .login:

```
    if ( -f ~/bin/zsh ) exec ~/bin/zsh -l
```

(in each case the `-l` tells zsh it is a login shell).

If you want to check this works before committing yourself to it,
you can make the login shell ask whether to exec zsh. The following
work for Bourne-like shells:

```
    [ -f $HOME/bin/zsh ] && {
            echo "Type Y to run zsh: \c"
            read line
            [ "$line" = Y ] && exec $HOME/bin/zsh -l
    }
```

and for C-shell-like shells:

```
    if ( -f ~/bin/zsh ) then
            echo -n "Type Y to run zsh: "
            if ( "$<" == Y ) exec ~/bin/zsh -l
    endif
```

It's not a good idea to put this (even without the -l) into .cshrc,
at least without some tests on what the csh is supposed to be doing,
as that will cause \_every\_ instance of csh to turn into a zsh and
will cause csh scripts (yes, unfortunately some people write these)
which do not call `csh -f' to fail. If you want to tell xterm to
run zsh, change the SHELL environment variable to the full path of
zsh at the same time as you exec zsh (in fact, this is sensible for
consistency even if you aren't using xterm). If you have to exec
zsh from your .cshrc, a minimum safety check is `if ($?prompt) exec
zsh`.

If you like your login shell to appear in the process list as `-zsh`,
you can link `zsh` to `-zsh` (e.g. by `ln -s ~/bin/zsh
~/bin/-zsh`) and change the exec to `exec -zsh`. (Make sure
`-zsh` is in your path.) This has the same effect as the `-l`
option.

Footnote: if you DO have root access, make sure zsh goes in
/etc/shells on all appropriate machines, including NIS clients, or you
may have problems with FTP to that machine.
