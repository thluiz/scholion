---
url: "https://aigeec.com/installing-node-js-on-windows-10-bash/"
captured_at: "2017-02-28T09:31:26-03:00"
title: "Installing basic Node.js dev env on Windows 10 bash"
domain: "aigeec-com"
---

# Installing basic Node.js dev env on Windows 10 bash

tl;dr here's a quick script to install git, node and npm. Run it at your own risk etc, explanation is below

```
# Get root up in here
sudo su

# Update and begin installing some utility tools
apt-get -y update

#install git
apt-get install git

# Change to what ever version you want here see link to versions below
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
apt-get install -y nodejs
```

### Explaining the code

Windows users may or may not be familiar with bash so here is a quick guide for getting set up with node.js on the new Windows 10 bash feature.

Basically it is the same as doing it on Ubuntu.

NOTE: You might have to prefix these commands with sudo e.g. the next one would be `sudo apt-get -y update` this give you elevated permissions.

Update your apt-get package index   
`apt-get -y update`

> The apt-get command is a powerful command-line tool, which works with Ubuntu's Advanced Packaging Tool (APT) performing such functions as installation of new software packages, upgrade of existing software packages, updating of the package list index, and even upgrading the entire Ubuntu system.
> -- [apt-get](https://help.ubuntu.com/12.04/serverguide/apt-get.html)

Install git - if you don't use git you need to take a good hard look at yourself   
`apt-get install git`

Update (2016-08-19): this used to read `git-all`, it installs [some extra packages](http://askubuntu.com/questions/796600/difference-between-installing-git-vs-installing-git-all) `git` should work fine in most cases. It seems `git-all` is causing some issue for people on the latest version of windows bash.

*Thanks to [Andrew Skaper](https://disqus.com/by/andrewskaper/) for letting me know about the issue with git-all*

Get the latest version on node.js. If you do a apt-get install without this step you will get version 0.10.x.   
`curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -`

You can now install node.js   
`sudo apt-get install -y nodejs`

Node gets installed as nodejs which is annoying because it is just referred to as node almost everywhere. This was not necessary for me and may not be for you.   
`` ln -s `which nodejs` /usr/bin/node ``

If its not it will just tell you the file exists   
`ln: failed to create symbolic link ‘/usr/bin/node’: File exists`

You should at this point be good to go.

You should have node, npm and git installed the world in you oyster.

### Version

New versions of Nodejs are released regularly. Check out these links for what is the latest bleeding edge and stable releases.

[Full list of available versions from nodesource](https://github.com/nodesource/distributions/tree/master/rpm) and update the setup\_7.x as appropriate.

Check out the [nodejs site](https://nodejs.org/) to find out which versions is best for you.

### Upgrading

See [Upgrading your version of Nodejs on Windows 10 bash](https://aigeec.com/upgrading-your-version-of-nodejs-on-windows-10-bash/) for details on upgrading.
