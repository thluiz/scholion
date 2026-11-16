---
url: "https://web.archive.org/web/20200521080947id_/https://dev.to/codingsafari/how-to-setup-a-remote-development-server-46ln"
captured_at: "2026-11-16T07:49:02+00:00"
title: "How to setup a Remote Development Server"
domain: "web-archive-org"
---

![Cover image for How to setup a Remote Development Server](https://res.cloudinary.com/practicaldev/image/fetch/s--fKfglOPz--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://res.cloudinary.com/practicaldev/image/fetch/s--gGLP7EMZ--/c_imagga_scale%2Cf_auto%2Cfl_progressive%2Ch_420%2Cq_auto%2Cw_1000/https://dev-to-uploads.s3.amazonaws.com/i/9ox3acmjm67mw71l1of5.png)

###  [![codingsafari profile image](https://res.cloudinary.com/practicaldev/image/fetch/s--Wh1mMp65--/c_fill,f_auto,fl_progressive,h_50,q_auto,w_50/https://dev-to-uploads.s3.amazonaws.com/uploads/user/profile_image/110572/1ef9aa10-44d5-41e3-b8dd-5d24e3965afc.jpg) Nico Braun](https://web.archive.org/codingsafari) [twitter logo](http://twitter.com/codingsafari) [github logo](http://github.com/bluebrown) May 12 _Updated on May 14, 2020_ ・5 min read  

Setting up a development environment on a remote server yields several benefits. For example, It is easier to work on projects from different locations, one can simply ssh into remote and have all the tooling at hand. Or, Low tier machines aren't that much of a problem as the remote server, and not the local machine, has to use its resources to do the computing.

Since this server is not meant to serve production applications, most connection to the outside world can be blocked. In fact, all incoming connections except for a couple whitelisted IPs should be dropped without any response. We want to allow only our own machine/s to be able to connect via ssh. Nothing else. This will reduce the risk of attacks drastically.

## [](#table-of-contents)Table of Contents

*   [Prerequisites](#prerequisites)
*   [Super User](#sudo-user)
*   [SSH Keys](#ssh-key)
*   [SSH Config](#ssh-config)
*   [Firewall](#firewall)
*   [Disable IPV6](#ipv6)
*   [Fail2Bann](#failb2ann)
*   [Workflows](#workflows)
*   [Port Forwarding](#port-forwarding)
*   [Wrapping Up](#wrapping-up)

## [](#prerequisites)Prerequisites

In order to follow along, you need access to a remote server or have a VM installed your machine. The commands shown here are based on RHEL CentOS 8.

## [](#super-user)Super User

As good measure, create a user and add it to the wheel group. Use this user instead of root. The user can run commands that require root privileges with sudo.

SSH as root into the server and create the user. At this occasion upgrade the kernel, before exiting.  

```
ssh root@remote_host
adduser username && passwd username
usermod -aG wheel username
dnf distro-sync -y
dnf upgrade -y
exit
```

## [](#create-and-deploy-ssh-key)Create and deploy SSH Key

Add a public ssh key to users authorized keys file. The easiest way to achieve to is to copy the public key from the local machine via ssh onto the remote host.  
Make sure you are connecting with the created user and not with root.  

```
cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && \
     touch ~/.ssh/authorized_keys && \
     chmod -R go= ~/.ssh && \
     cat >> ~/.ssh/authorized_keys"
```

_You can create the key with a tool called [ssh-keygen](https://www.ssh.com/ssh/keygen/)._

## [](#configure-ssh)Configure SSH

Connect back to remote and edit the config file.  

```
ssh username@remote_host
sudo vim /etc/ssh/sshd_config
```

Add the following lines to the config file.  

```
LoginGraceTime 1m
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no
IgnoreRhosts yes
Protocol 2
AllowUsers username
```

**Before disabling password authentication**, test the public key authentication by restarting `sshd`, exiting the session and reconnecting.  
If it is not asking for your password anymore but logs you in, the key is working.

Restart the service.  

```
sudo systemctl restart sshd
```

## [](#configure-the-firewall)Configure the Firewall

The next part step is to configure the firewall. [Firewalld](https://firewalld.org/) is pre installed in CentOS.

Change the default zone to block so that all incoming traffic is blocked without any acknowledgment. Add the public IP of your local machine to the public resource group. You can add multiple sources to each group, so this is essentially your IP whitelist. Lastly remove the two services not being used and leave only SSH available.  

```
sudo firewall-cmd --set-default-zone=block
sudo firewall-cmd --permanent --zone=public --add-source=my.public.ip.address
sudo firewall-cmd --permanent --zone=public --remove-service=cockpit --remove-service=dhcpv6-client
sudo firewall-cmd --reload
```

Check the config.  

```
sudo firewall-cmd --list-all
sudo firewall-cmd --zone=public --list-all
```

## [](#disable-ipv6)Disable IPV6

Next, disable IPV6 all together as it's not needed and reduces the attack surface.  

```
sudo vim /etc/sysctl.d/disableipv6.conf
```

Place the following entry to disable IPv6 for all adapter  

```
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
# A particular network card instead of default can be accessed
# for example for the imaginary card enp0s3
# net.ipv6.conf.enp0s3.disable_ipv6 = 1
```

Restart the Service  

```
sudo systemctl restart systemd-sysctl
```

If the below command does not return anything, ipv6, is disabled.  

```
ip a | grep inet6
```

## [](#setup-fail2ban)Setup Fail2Ban

Lastly, install [Fail2ban](https://www.fail2ban.org/wiki/index.php/Main_Page). fail2ban scans log files (e.g. /var/log/apache/error\_log) and bans IPs that show the malicious signs.  

```
sudo dnf install epel-release
sudo dnf install fail2ban
sudo systemctl start fail2ban
sudo systemctl enable fail2ban
```

Everything is blocked except for SSH. Add some configuration for this particular use case.  

```
sudo vim /etc/fail2ban/fail.d/ssh.conf
```

The following setting will ban any IP forever, after three failed login attempts withing two hours. At this point, We don't expect anyone to be able to connect other than us. Some redundancy cannot hurt though.  

```
[DEFAULT]
bantime = -1
findtime = 2h
maxretry = 3

[sshd]
enabled = true
```

## [](#workflows)Workflows

Now the development environment is secure. All connections to the outside world and are cut off and only the ssh connection to the local machine is open. How does the actually workflow look like now? There are essentially two major ways, old and new school.

### [](#old-school-aka-vim-me-out-bro)Old School a.k.a. Vim me out, Bro

The first method is how it's been done for a long time. The primary work environment will be [Vim](https://www.vim.org/) which is installed on the remote host. Some people like to use [tmux](https://github.com/tmux/tmux/wiki) and or [zsh](https://www.zsh.org/) alongside. It is actually a very powerful combination. If you master these tools, you won't have to miss any feature.

[![vim](https://res.cloudinary.com/practicaldev/image/fetch/s--by8AJJXU--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://d3nmt5vlzunoa1.cloudfront.net/pycharm/files/2013/06/vim3.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--by8AJJXU--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://d3nmt5vlzunoa1.cloudfront.net/pycharm/files/2013/06/vim3.gif)

### [](#new-school-aka-vs-code-gui)New School a.k.a. VS Code GUI

[VS Code](https://code.visualstudio.com/) has awesome remote development support. You can install extensions on the remote host and use the GUI locally.

[![vscode](https://res.cloudinary.com/practicaldev/image/fetch/s--FuPKmRvP--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://code.visualstudio.com/assets/docs/remote/ssh/architecture-ssh.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--FuPKmRvP--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://code.visualstudio.com/assets/docs/remote/ssh/architecture-ssh.png)  
Read more in the [official docs](https://code.visualstudio.com/docs/remote/remote-overview).

## [](#port-forwarding-ssh-tunnel)Port Forwarding / SSH Tunnel

Ok, you can write some code now, that's great but how can an application actually be viewed? The answer is simple, run the app on the remote server on some port. Then forward whatever is sent on this port to the local machine.

Let's say you just started a React dev server on the remote host. The React app is being served at `localhost:8080`. You can now connect with a new shell but this time, only to forward the ports.  

```
ssh -L -O localhost:6000:localhost:8080 username@remote_host
```

Navigate to `localhost:6000` in the browser of your local machine and see the application.

VS Code has some built in functionality around SSH Tunneling as well. You can read more in the [official docs](https://code.visualstudio.com/docs/remote/ssh#_forwarding-a-port-creating-ssh-tunnel).

## [](#wrapping-up)Wrapping Up

We have learned how to secure a remote development server, taking care of various configurations such the firewall and ssh. We have also looked at possible workflows for our environment and at SSH Tunneling.

It was an exiting trip, I hope you enjoyed it as much as I did.

Thank you.

 [![twitter logo](https://practicaldev-herokuapp-com.freetls.fastly.net/assets/twitter-ff4bdab814039c4cb172a35ea369e0ea9c6a4b59b631a293896ae195fa26a99d.svg)](https://twitter.com/intent/tweet?text=%22How%20to%20setup%20a%20Remote%20Development%20Server%22%20by%20@codingsafari%20%23DEVCommunity%20https://dev.to/codingsafari/how-to-setup-a-remote-development-server-46ln)[DISCUSS (5)](#comments)

![Copy to Clipboard](https://practicaldev-herokuapp-com.freetls.fastly.net/assets/content-copy-a7e427c8a25ce35374a1ba06f645ee6a2160808b89a700c62508e173627a0f56.svg)

[![codingsafari profile](https://res.cloudinary.com/practicaldev/image/fetch/s--FKbJYsIE--/c_fill,f_auto,fl_progressive,h_180,q_auto,w_180/https://dev-to-uploads.s3.amazonaws.com/uploads/user/profile_image/110572/1ef9aa10-44d5-41e3-b8dd-5d24e3965afc.jpg)](https://web.archive.org/codingsafari)
