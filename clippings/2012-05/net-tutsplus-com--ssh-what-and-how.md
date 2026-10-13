---
url: "http://net.tutsplus.com/tutorials/tools-and-tips/ssh-what-and-how/"
captured_at: "2012-05-24T11:19:19-03:00"
title: "SSH: What and How | Nettuts+"
domain: "net-tutsplus-com"
---

# SSH: What and How

[Jonathan Cutrell](http://net.tutsplus.com/author/jonathan-cutrell/ "Posts by Jonathan Cutrell") on May 22nd 2012 with [15 comments](http://net.tutsplus.com/tutorials/tools-and-tips/ssh-what-and-how/#comments "Comment on SSH: What and How")

##### Tutorial Details

- **Program**: SSH, Shell
- **Difficulty:** Medium
- **Estimated Completion Time:** 30 Minutes

Many web developers use SSH (“Secure Shell”) on a daily basis to manage their servers, back up files, work remotely, and a myriad of other tasks. Today, I’ll explain what SSH is, do a brief history review, and, lastly, teach you how to set it up on your remote server or even your local network. Let’s get started!

---

## A Starting Explanation

If you’re reading this, it’s likely that you’re at least somewhat acquainted with Terminal (or on Windows, something like Cygwin). If so, then you will understand this quick functional explanation of SSH.

> SSH is essentially using a network connection to get into Terminal on another computer.

If you aren’t familiar with Terminal, there are a [lot of explanations](http://net.tutsplus.com/articles/web-roundups/10-terminal-commands-that-will-boost-your-productivity/) and beginner’s guides to Terminal, both here on Nettuts+ and elsewhere. The power of SSH is reliant on its simplicity; by offering you access to the Terminal of another machine, SSH cuts to the chase and gives you full control over a remote machine. If you understand the power of Terminal and its direct connection to the inner workings of your local machine, then you understand the power of SSH!

---

## A Brief History

SSH was developed in its infant state in 1995. The primary developer, Tatu Ylonen, developed it as the first secure way to administrate a remote UNIX system. Previous to SSH, the only tools that existed sent information like passwords in clear text.

---

## So, How Do I Use It?

There are a million guides out there on how to get set up with SSH. We will specifically cover one method today. First things first, you’ll want to make sure you have SSH on your system.

- **Mac –** A version of OpenSSH comes preinstalled.
- **Windows –** Follow a guide [like this one](http://pigtail.net/LRP/printsrv/cygwin-sshd.html) or [this one](http://inside.mines.edu/~gmurray/HowTo/sshNotes.html) to get Cygwin and the “openssh” package installed.
- **Linux –** OpenSSH is highly likely to be installed already, but if it isn’t, you can follow [the same guide](http://inside.mines.edu/~gmurray/HowTo/sshNotes.html) to get it installed.

To determine if SSH is installed, run `` `which ssh` ``. If Terminal returns something along the lines of `/usr/bin/ssh`, then you’re good to go! Otherwise, follow one of these guides to get it installed.

In this article, I will assume the version you are using is OpenSSH; there are some configuration differences that depend on your version of SSH. We will be explaining how to set up a Mac to connect to a MediaTemple server through a single SSH command. Once you have SSH installed on your machine, you will need to make sure your target host has SSH enabled. SSH runs over port 22 by default; you can use a command line tool like `nmap` to ping your server to determine if port 22 is accepting incoming connections, like this:

|  |  |
| --- | --- |
| 1 | `sudo` `nmap -sS` `hostname``.com` |

Of course, you probably have access to the administrative interface for the server. Make sure you look through the options and enable SSH. On a Mediatemple server, this configuration is located under the Server Control panel. Mediatemple SSH is accessible by using root@primarydomain.com. You can add users to the account, but for the sake of keeping things simple, we will use root@primarydomain.com.

Once SSH is enabled (and you have set a root password in your server admin), you can run the following line to SSH into your server.

|  |  |
| --- | --- |
| 1  2 | `ssh` `root@primarydomain.com` |

…where primarydomain.com is your MediaTemple primary domain. You will then be prompted for your password (which is the root password you set in the control panel). If you are not using MediaTemple, you can SSH directly to the IP address of your server as well.

If using shared hosting, it is likely that you will not be logging in as root. Instead, you will log in with a user account name. For example, if you are using a service like Site5, you may log in with a username at a subdomain, like this:

|  |  |
| --- | --- |
| 1  2 | `ssh` `username@malta.site5.com` |

Ultimately, these configurations will depend on your specific web server company. Refer to your host’s documentation for more information.

Once you are “shelled in”, you can execute commands and traverse the file system within Terminal. Depending upon on your level of access, you may be able to install things on your server using apt-get or wget commands. You can manage your Apache server, edit configuration files with a Terminal-based text editor, view error logs, clear caches, view files directly on a server to make sure they are the correct version, and plenty of other lower-level system administration tasks. Now, what if you wanted to do *more, faster* with SSH?

---

## How Do I Use It… Better?

There are a ton powerful things that SSH opens you up to. We will skip a few of them (as quite a few are more sysadmin-related, like tunneling). But we will go over a few useful tricks.

### Super-quick Log-in

You’re thinking to yourself, “seems like there should be a faster way to do this.” You’re right. And there is. Instead of having to remember your domain, password, and username for every server, you can set up a few configurations that will allow you to speed up the process to something along these lines.

|  |  |
| --- | --- |
| 1  2 | `ssh` `myserver` |

With the right configuration, you could run this, and without having to enter any passwords, IP addresses, or long domain names, you’re in! Again, we will assume you are logging into a MediaTemple server. First, we will generate *ssh keys*. This is basically a set of encrypted keys that live in `~/.ssh` on your local machine. You have a “public” key and a “private” key. So, first things first, open a new Terminal window and create the .ssh folder in your home directory.

|  |  |
| --- | --- |
| 1 | `mkdir` `~/.``ssh` |

Next you will generate your keys with the following line. (This comes directly from MediaTemple’s documentation.)

|  |  |
| --- | --- |
| 1 | `ssh``-keygen -t rsa -b 2048 -f ~/.``ssh``/id_rsa` `-C` `"Comment about your key goes here."` |

This line will generate an ssh key of type rsa, with 2048 bits (for security), at the file location specified, with the comment specified. You will be promprted for a password, but it isn’t mandatory or necessary; not providing a password will enable you to automatically log in. The RSA type is for SSH protocol version 1. Type DSA is for protocol version 2. Check with your web server to find out which version they are using. Once your keys are generated, you will then run this to make sure your SSH configurations are set to the right permissions.

|  |  |
| --- | --- |
| 1 | `chmod` `700 ~/.``ssh` `&&` `chmod` `600 ~/.``ssh``/*` |

Next, you will upload your public key to your server. There are quite a few ways to do this; this way comes from MediaTemple’s docs as well.

|  |  |
| --- | --- |
| 1 | `cat` `~/.``ssh``/id_rsa``.pub |` `ssh` `root@example.com` `'cat - >> ~/.ssh/authorized_keys'` |

This code is echoing your id\_rsa.pub through a `|` (pipe) into the next command, which is an SSH into root@example.com, where you will run an echo and concatenation of what you piped in the first command. It sounds a bit complicated, so there are a few alternative ways to handle this. Essentially, you are going to want no line breaks and your public key on its own line in a file, called `authorized_keys` on your server in the ~/.ssh/ directory. So, if this is the first or only key you want on your server, you could run this command to copy it directly to that location.

|  |  |
| --- | --- |
| 1 | `scp` `~/.``ssh``/id_rsa``.pub root@example.com:.``ssh``/authorized_keys` |

This line is essentially saying, “copy this first file through SSH to the server at this location relative to my current home directory.”

Once your authorized\_keys contains your public key, you can attempt to login to the server with ssh username@example.com. If you put your public key in the root user directory’s SSH configuration files, you will be able to login directly to root. You will be asked about a rsa fingerprint; go ahead and allow this action. It adds the server you are connecting to to a known\_hosts file. This file can be used for a lot of different things, but particularly to secure yourself against what is called a “man-in-the-middle” attack. If you’d like to read a little more about this, check out [this explanation](http://www.jfranken.de/homepages/johannes/vortraege/ssh1_inhalt.en.html#ToC17).

If you can successfully log into your server, as if you had entered a password, your keys are working properly. The next step is to add a couple of lines for a shortcut to a configuration file on your machine . Open ~/.ssh/config in your favorite text editor (create it if it doesn’t exist) and add the following:

|  |  |
| --- | --- |
| 1  2  3 | `Host shortname`  `HostName somehost.com`  `User username` |

Where “shortname” is a nickname for the server you want to log into. For instance, “Host myserver” would allow me to do `ssh myserver`. The HostName is your server location, and of course the User is your username. You may have `User root` at this spot. Once this file is saved, you should be able to run a simple command to log into your server, like this:

|  |  |
| --- | --- |
| 1 | `ssh` `shortname` |

### Git Without a Hub

*Please Note: this section requires a bit of familiarity with [Git](http://net.tutsplus.com/tutorials/other/easy-version-control-with-git/).*

You can use SSH to set up your own Git repos on your server! This is useful for companies who don’t want to expose their code on GitHub for whatever reason, and it’s great to be able to push directly from a local machine to a Git repo on your own server.

To set this up, make sure Git is installed on both the host and your local machine. You may have to go through your web server company to have Git installed. Next, run `git init` on your server in the location that you want your Git repo to be. Of course, you can do this a hundred different ways, but if you prefer to not have a bare repository, you can use branches to push to from your local machine. Here is a common workflow.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16 | `ssh` `user@example.com`  `cd` `/path/to/repo`  `git init`  `git checkout -b staging`  `git checkout master`  `# disconnect from shell session using ctrl-d`  `cd` `/local/repo`  `git init`  `git add .`  `git commit -am` `"some message"`  `git remote add origin user@example.com:``/path/to/repo`  `git checkout -b staging`  `git push origin staging`  `ssh` `user@example.com`  `cd` `/path/to/repo`  `git merge staging` |

Essentially what is happening here is you are logging into the server, changing to the desired repo path, creating a repository and adding a “staging” branch which you can push to from your local machine. Then, you are creating your local repo and a corresponding “staging” branch on your local machine, and adding files to track to the repo. Next comes an initial commit. You are then adding the remote repository as an alias of “origin”. Next, you are pushing the local staging branch to the “origin” alias’s staging branch. Finally, you are ssh’ing back into the server and merging the “staging” branch with the default “master” branch.

### SFTP > FTP

You can also use SSH-powered FTP (file transfer protocol), which is essentially a more secure (encrypted) version of FTP that runs over port 22 (rather than the default FTP port 21). Most FTP clients support SFTP as well. [FileZilla](http://filezilla-project.org/) (for Windows) and [Fetch](http://fetch.en.softonic.com/mac/download) (for Mac) are two popular (and free) SFTP/FTP clients.

### Easy Access to Your Server Almost Anywhere

As long as you are around a computer that is connected to the internet, has a Terminal, and has SSH installed (any Mac connected to WiFi, for instance), you can get access to your server, via SSH. That’s the best part. You don’t require any configuration (assuming you haven’t set up any restrictions that *require* a matching pubkey), you can log in with your username and password from practically anywhere. There are even SSH clients for iOS and other mobile devices. This is a very powerful feature of SSH that is only paralleled in portability by browser-based applications.

### A Local Code Repo

> Hopefully you can see the power of SSH in a daily development cycle.

Let’s imagine that you and a few buddies are working on some code together. Let’s also say you have a local computer that you have full control over that you use as a development LAMP server with a few VM’s installed on it. You can use SSH locally to move files to and from your computer and the development machine. You can even set up a local Git (or svn, or Mercurial) repo, powered by SSH to keep everything in check. Perhaps you could even make the development machine the only machine that is connected to the remote server via SSH, so that the code *has* to go through a specific staging process before it can be put into production. The backbone of all of these actions is SSH!

Hopefully you can see the power of SSH in a daily development cycle, especially for teams using version control. As I noted previously, there is plenty of documentation and a myriad of other network-level tools based on or reliant upon SSH that will give you more control and power over your development process and your server. Who knows? Maybe, one day, you could double as a sysadmin after all!

---

## Some Other Helpful Links

Here are some other helpful links to get you started with SSH. It’s been around for a while, so there is plenty of documentation floating around.

- [The official OpenSSH manual](http://www.openssh.com/manual.html)
- [Linux Journal’s introduction to SSH](http://www.linuxjournal.com/article/4412?page=0,0)
