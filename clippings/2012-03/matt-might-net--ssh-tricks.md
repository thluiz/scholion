---
url: "http://matt.might.net/articles/ssh-hacks/"
captured_at: "2012-03-16T19:56:08-03:00"
title: "SSH tricks"
domain: "matt-might-net"
---

## Why SSH?

As recently as a 2001, it was not uncommon to log in to
a remote Unix system using telnet.

Telnet is just above netcat in protocol sophistication,
which means that passwords were sent in the clear.

As wifi proliferated, telnet went from security nuissance
to security disaster.

As an undergrad, I remember running ethereal (now wireshark) in the school
commons area, snagging about a dozen root passwords in an hour.

SSH, which encrypts and authenticates connections, had been in development
since 1995, but it seemed to become adopted nearly universally
and almost overnight around 2002.

It is worth configuring SSH properly:

- per-user configuration is in `~/.ssh/config`;
- system-wide client configuration is in `/etc/ssh/ssh_config`.
- system-wide daemon configurtion is in `/etc/ssh/sshd_config`.

## Key-based, passwordless authentication

Key-based passwordless authentication makes it
less cumbersome for other programs and scripts to piggyback atop
SSH, since you won't have to re-enter your password each time.

Key-based authentication exploits public-key cryptography
to prove to the server that the client owns the secret private
key without revealing the key.

[If you're curious about public-key cryptography,
see my post on a
[short implementation of RSA](http://matt.might.net/articles/implementation-of-rsa-public-key-cryptography-algorithm-in-scheme-dialect-of-lisp/) .]

To set this up, first log in to the client machine.

Then create a private/public key pair with `ssh-keygen`:

```
 $ ssh-keygen -t dsa
```

This will place the private key in `~/.ssh/id_dsa`
and the public key in `~/.ssh/id_dsa.pub`.

Guard the private key (set appropriate permissions) as if
the private key were your password. In effect, it is.

Now, append the contents of `~/.ssh/id_dsa.pub`
to the end of `~/.ssh/authorized_keys`
on the *remote* machine.

For example:

```
 $ cat .ssh/id_dsa.pub | ssh host 'cat >> ~/.ssh/authorized_keys'
```

(On Linux systems, you can use `ssh-copy-id` instead;
the technique above is more portable.)

Do *not* copy your private key over.

Now, when you connect to that account,
it won't require a password.

## Executing remote commands

To run a command on a remote system without logging in,
specify the command after the login information:

```
 $ ssh host command
```

For example, to check remote disk space:

```
 $ ssh host df
```

My favorite example for Linux is
[piping the microphone from
one machine to the speakers of another](http://www.commandlinefu.com/commands/view/350/output-your-microphone-to-a-remote-computers-speaker) :

```
 $ dd if=/dev/dsp | ssh -C user@host dd of=/dev/dsp
```

## Copying files with ssh

For copying data and files over SSH, there are a few options.

It's possible to copy with the command `cat`.
If you're trying to copy the output of a process instead of a file, this is certainly
a reasonable route.

If you're going to use SSH like this, disable the escape sequences:

```
 $ cat file | ssh -e none remote-host 'cat > file'
```

If these are going to be large files, you may want to use the `-C`
flag to enable compression.

For copying files, the program `scp` works like `cp`,
except it also accepts remote destinations.

For example:

```
 $ scp .bash_profile matt@example.com:~/.bash_profile
```

For an FTP-like interface for
copying files, use the program `sftp`.

## Per-host SSH client configuration options

You can set per-host configuration options
in `~/.ssh/config` by specifying
`Host hostname`,
followed by host-specific options.

It is possible to
set the private key and the user (among many other settings)
on a per-host basis.

Here's an example config file:

```
Host my-server.com
User admin
IdentityFile ~/.ssh/admin.id_dsa
BatchMode yes
EscapeChar none

Host mm
User matt
HostName might.net
IdentityFile ~/.ssh/matt.id_dsa

Host *.lab.ucaprica.edu
User u8193
```

The first example enables batch mode, which means
it will never ask for a passphrase or password
for this host.
It also disables an escape sequence, which
avoids any hiccups when transmitting
arbitrary data.
If `ssh` is to be invoked within scripts,
this is a good option.

The second example uses a `HostName` abbreviation,
so that `ssh mm` is equivalent to
`ssh -i ~/.ssh/matt.id_dsa matt@might.net`.

The third example sets the user to `u8193` for any
machine in the subdomain `lab.ucaprica.edu`.

See more options in `man ssh_config`.

## Configuring sshd

The options most frequently tweaked are:

- `Port`: set this to the port on which you want
  sshd to run. Unless you have a compelling reason to move it,
  keep it on 22.
- `PermitRootLogin`: set this to `no`
  and then configure `sudo` to add a little security;
  another good setting is `without-password`, which
  will force the use of public key authentication for `root`.
- `PasswordAuthentication`: set this to `no` to
  disallow password authentication entirely and to require public key authentication.

The man page for `sshd_config` summarizes the
remaining options well.

## Local port forwarding

SSH allows secure port forwarding.

For example, suppose you want to connect from
client `A`
to server `B`
but route traffic securely through server `C`.

From `A`, run:

```
 A$ ssh C -L localport:B:remoteport
```

Then, to connect to `B:remoteport`,
connect to `localhost:localport`.

If you use add `-g`, then
anyone that can reach `A`
may connect to `B:remoteport` through
`A:localport`.

This is useful for evading firewalls.

For example, suppose your work banned reddit.com.

Run this:

```
 # ssh yourserver -L 80:reddit.com:80
```

And, set the address of `reddit.com`
and `www.reddit.com`
to `127.0.0.1` in `/etc/hosts`.

You will also need to disable any local web server
running first.

Now, it will surreptitiously traffic to
`reddit.com` through your *yourserver*.

If you do this frequently, you might want to add a special host:

```
 Host redditfw
 HostName yourserver
 LocalForward 80 reddit.com:80
```

## Remote port forwarding

Alternatively, suppose you wanted to give remote machine `B`
access to another machine, `A`, by
passing securely through your local machine `C`.

Then, on *`C`*, you can run:

```
 C$ ssh B -R remoteport:A:targetport
```

At this point, local users on `B` can
connect to `A:targetport`
through `localhost:remoteport`.

If you want to to allow nonlocal users to be able to connect
`A:targetport`
through `localhost:remoteport`,
then set:

```
 GatewayPorts yes
```

in the `sshd_config` file.

Once again, if you do this frequently,
set up a special host in `~/.ssh/config`:

```
 Host exportme
 HostName B
 RemoteForward remoteport A:targetport
```

## Setting up a SOCKS proxy for Firefox

SSH can also set up a SOCKS proxy to evade a firewall.

It's remarkably simple:

```
 $ ssh -D localport host
```

In Firefox, under Preferences > Advanced > Network,
select "Settings."

Set your SOCKS5 proxy to `localhost` port *localport*.

Test it out by googling "what is my ip."

Firefox will now forward your web traffic through *host*.

A word of caution: this will *not* forward your DNS requests.

If you need to hide your DNS requests as well, I recommend
installing
[DNSCrypt](http://www.opendns.com/technology/dnscrypt/)  from
[OpenDNS](http://www.opendns.com/) .

In `about:config`, you can also tell Firefox to forward
your DNS requests;
set:

```
network.proxy.socks_remote_dns
```

to **true**.

## SSH as a filesystem: sshfs

Using the [FUSE](http://fuse.sourceforge.net/)  project
with [sshfs](http://fuse.sourceforge.net/sshfs.html) ,
it's possible to mount a remote filesystem over SSH.

On the Mac, use [Fuse4x](http://fuse4x.org/) .

From MacPorts, install it all with:

```
 $ sudo port install sshfs
```

And, once it's installed, run:

```
 $ sshfs remote-host: local-mount-directory
```

## SSH from windows

Sometimes, you need to get to your home machine from
windows. In these cases, you want
the
[PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) 
suite of tools.

## SSH from iOS

Using SSH from iOS can be cumbersome,
but the iSSH app is particularly
well-suited to administrative tasks.

The iSSH app allows storing configurations,
which enables per-machine
private keys and remote commands to run
upon connecting.

So, you can create a configuration that
logs in to run a shell script.

I have three command-based
configurations for might.net:

- a script to (re)start the web server;
- a script to (re)start the DNS server;
- a script to reboot the entire server.

## Related pages

---
