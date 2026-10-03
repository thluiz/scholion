---
url: "http://bbhoss.io/remote-iex-access-via-ssh/"
captured_at: "2016-02-07T23:10:47-03:00"
title: "Remote IEx access via :ssh"
domain: "bbhoss-io"
---

# Remote IEx access via :ssh

14 January 2016

I was excited when I read how easy it was to [access a remote erlang node via ssh alone](https://www.erlang-solutions.com/blog/secure-shell-for-your-erlang-node.html), as the traditional way can be a bit of a challenge. Naturally, I wondered if it was possible to do this with Elixir, and it's quite easy!

Essentially, follow the instructions on the post above (translating to Elixir). The main change is that you have to start the ssh application first (`:ssh.start`), then when starting the ssh daemon, provide a different shell option, like this:

```
:ssh.daemon(12345, system_dir: 'ssh_dir', user_dir: 'ssh_dir', shell: {IEx, :start, []})
```

When you ssh to port `12345`, this is what you'll see now:

```
Interactive Elixir (1.2.0) - press Ctrl+C to exit (type h() ENTER for help)  
iex(1)>
```

There are some apparent caveats to this. Typing `h()` kills your connected shell due to an apparent [unicode issue](https://gist.github.com/bbhoss/5338192618f40d16982b)

Also, I was initially puzzled that `:observer.start` worked without any sort of X11 forwarding, but it appears that it starts the observer on the running node, which was my local machine.

Despite the caveats, this might be very useful for quickly debugging your application, using only SSH. I hope we can take this method and develop it further so that it becomes even more useful to Elixir developers.
