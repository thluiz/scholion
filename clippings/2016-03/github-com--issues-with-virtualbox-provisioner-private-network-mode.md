---
url: "https://github.com/mitchellh/vagrant/issues/3860"
captured_at: "2016-03-13T21:04:28-03:00"
title: "Issues with virtualbox provisioner `private_network` mode in cloud ubuntu 14.04 box · Issue #3860 · mitchellh/vagrant"
domain: "github-com"
---

# Issues with virtualbox provisioner `private\_network` mode in cloud ubuntu 14.04 box #3860

Closed

[zerkms](https://github.com/zerkms) opened this Issue on 20 May 2014
· 47 comments

### Labels

None yet

### Milestone

No milestone

### Assignee

No one assigned

### Notifications

You’re not receiving notifications from this thread.

### 26 participants

and others

There are some issues related to `cloud-init-nonet` caused by virtualbox provisioner:

If you create a vm from `ubuntu/trusty64` box.

Then after it's up and running add

```
config.vm.network "private_network", type: :dhcp
```

private network, then after 2 reboots using `vagrant reload` the `cloud-init-nonet` process will spend 120 seconds waiting for something, followed by another 60 seconds from some other startup script. Eventually it will start but it will take at least 3 minutes.

Something relevant I've found:

<https://bugs.launchpad.net/cloud-init/+bug/1315501>  
<https://ask.openstack.org/en/question/28297/cloud-init-nonet-waiting-and-fails/>

Owner

I think this is just a bug with ubuntu, not with Vagrant. Please correct me if I'm wrong and advise on what approach Vagrant should take.

Well, I turned off the vagrant network configuration for host-only adapter using `auto_config: false` and just put

```
auto eth1
iface eth1 inet dhcp
```

to the `/etc/network/interfaces.d/eth1.cfg`.

Which solved the issue.

I assume that's what should be done by vagrant not manually.

Owner

That is what Vagrant does. It sounds like with this bug though on restart Ubuntu/cloud-init is actually changing that to a static definitoin.

Well, the thing is if it's added manually in a separate file - it works. If added by vagrant into a common `/etc/network/interfaces` - it doesn't (there is a difference though - I didn't drop the route as vagrant does, may be that is the issue).

I'm not confident enough to tell if it's a vagrant or that particular image or `cloud-init` or whatever else bug :-)

Owner

Ah I see what you're saying. Okay, let me take a closer look.

Any news on investigation?

Just experienced exactly the same on ubuntu 12.04 and bridged adapter...

Owner

Not yet, changing the networking stuff is quite scary because it isn't well tested (hard to test this), so work on this won't go until 1.7.

I can confirm, I also experience the same issue.

EDIT: Okay so it appears the issue is the line

```
post-up route del default dev $IFACE
```

Commenting this line out fixes the problem. I'll admit, I'm not really network savvy, so I'm not sure what this line does, or why it's important, or why we need it...but there's probably a good reason, and commenting it out is probably not the best solution.

Either way, until the problem is either fixed, or someone can tell me why the band-aid of deleting that line is a bad-idea, my temporary work-around is to have ~~my provisioner delete the line.~~

---

EDIT2: Never mind, vagrant is a jerk and keeps adding it back in because auto config is on (understandable)...the best band-aid would probably be to add it to the init process then, but now I'm getting to really hacky territory--it would be nice if a real solution was found.

---

EDIT3: Okay, I'm not proud of this, but this appears to be a valid work-around. If you use this, please paste a big fat comment block explaining why you have to do this awful thing, and it should be removed as soon as this bug is fixed (either by ubuntu or vagrant...whatever the problem is). If you have a script provisioner, stick this bad boy in it:

```
if [[ ! -f /etc/init/fix-network-hack.conf ]]; then
   echo "#Fix vagrant-ubuntu-network-bug
      start on mounted MOUNTPOINT=/ and starting cloud-init-local

      task

      console output

      script
         sed -i '/post-up route del default dev/d' /etc/network/interfaces
      end script" > /etc/init/fix-network-hack.conf
fi
```

This will, before cloud-init is run, delete all occurrences of "post-up route del default dev" from /etc/network/interfaces. Then, after the network is set up, vagrant will put it back...but who cares, we'll just delete it again on start up.

You should probably make sure this hack is really what you want to do before you do it.

Any news on this? Cannot get `config.vm.network "private_network", dhcp:true` to work.

For the record, this affects both Trusty and Precise.

[@mitchellh](https://github.com/mitchellh) May I draw your attention to this issue and ask you to consider reopening it? Even if it is a bug in Ubuntu, at the very least I think it is an issue worth mentioning in the README. Especially considering that old versions of Ubuntu with this bug will be around for a while. I observed connection failures on several machines (20+) with freshly installed Virtual Box and Vagrant. As it stands, there is no way I know of to get the Ubuntu cloud images to work reliably in a DHCP setup (apart from crazy hacks as mentioned by [@Houndie](https://github.com/Houndie)). Furthermore, can you please eleborate on why `post-up route del default dev $IFACE` is necessary?

[@trkoch](https://github.com/trkoch) I don't think it belongs in the README necessarily, but it would be nice if there was a more extended place where people could share their experiences and etc.

That was some of these nuances could be recorded in a friendlier way without keeping upstream issues open for Vagrant. I think the Mailing List scratches a bit of the itch for that, and there is also the IRC channel (which is a bit more ephemeral). Do you think there would be use for a forum or regularly updated extended documentation? Perhaps shifting some of the documentation load onto the community would be helpful in making these things friendlier to new users.

[@trkoch](https://github.com/trkoch) Do we know if it's an upstream issue? I'm not doubting it, just as far as I know it hasn't really been investigated thoroughly yet.

I think the answer probably lies in the "post-up" line. If it's necessary (which, okay sure it might be..I have no idea what it does), then it's probably an ubuntu issue. If it's not then, well, it might be an ubuntu issue too, but one that vagrant can easily avoid by changing one line of code.

[@drpebcak](https://github.com/drpebcak) Granted it doesn't have to be the README, but I think it should be a place people where people notice. Perhaps Vagrant (on failure of any sort) could point to a Wiki page with general troubleshooting advice? Better yet, we fix this bug!

[@Houndie](https://github.com/Houndie) We don't for sure. There are a lot of loosely related issues. I will try to dig into it.

Let's take a closer look at the interface configuration found in `/etc/network/interfaces`.

```
iface eth1 inet dhcp
    post-up route del default dev $IFACE
```

This basically means that after eth1 is brought up, the default route on eth1 should be removed. $IFACE is a variable that refers to the interface being configured and expands to eth1 in this example.

I deleted this line from my interface configuration, rebooted and ran this command manually (with root privileges).

```
$ route del default dev eth1
SIOCDELRT: No such process
```

As you can see, the command fails. I guess this is because there is no default route with the eth1 interface, as indicated by `route`. It turns out this command also fails if the machine was booted with the line in question.

```
post-up command
       Run command after bringing the interface up.   If  this  command
       fails then ifup aborts, refraining from marking the interface as
       configured (even though it has really been  configured),  prints
       an  error  message,  and exits with status 0.
```

In other words, if the post-up command fails, the interface remains unconfigured (no DHCP).

I still wonder what the purpose of that line might be? It was added in [33551ec](https://github.com/mitchellh/vagrant/commit/33551eca47d234510119a40e8bea6d28b93b377a) ("Delete default routes for bridged networking on coming up"). From what I can tell this command is no longer necessary in recent versions of Ubuntu (I don't know about Debian).

A workaround is to make sure that the post up command never fails

```
post-up route del default dev $IFACE || true
```

With this line I can reboot my virtual machine without waiting 3 minutes.

The post-up line is added in [templates/guests/debian/network\_dhcp.erb](https://github.com/mitchellh/vagrant/blob/master/templates/guests/debian/network_dhcp.erb#L6). When I remove that line, I no longer run into the problem.

Was this once necessary on some other Debian variant? If so, the `|| true` change would be more backward compatible. Seems like the worst case is that `route del…` fails for some other reason and the machine boots without it.

[@mitchellh](https://github.com/mitchellh) this seems to be pretty clearly a Vagrant issue.

I tried running the fixed version (without post-up) on Debian Squeeze (with private networking set to dhcp), and it works fine. Unsurprisingly, trying to delete eth1's default route results in an error:

```
$ sudo route del default dev eth1 ; echo $?
SIOCDELRT: No such process
7
```

Wild ass guess: was this to fix the case where eth1 came up before eth0 and established the wrong default route?

I've been experiencing this issue for a month, my "solution" has been destroying the *vagrant machine* and reprovisioning it.

I'm also experiencing this issue with the Ubuntu Trusty image.

bump. any movement on this? perhaps a PR would help expedite?

It seems to me that nobody really knows what this post-up command is meant to accomplish. A PR would fix this issue as far as I can tell, but could introduce another if we don't know what we are doing. I'm not sure if @mitchelhh is comfortable with appending '|| true' as described.

In the meantime, I am using the following hack in my Vagrantfile when using the trusty64 box.

```
sed --in-place -e "s:post-up route del default dev \\$IFACE$:post-up route del default dev \\$IFACE || true:g" /etc/network/interfaces
```

Appendeding `|| true` works fine, but `/etc/network/interfaces` is being reset; I’m guessing on this step:

> `==> default: Clearing any previously set network interfaces...`

Is it possible to fix this permanently without modifying `network_dhcp.erb`? (I don’t necessarily have access to that.) `chattr +i`ing it works, but leads to an ugly warning.

I was having a similar issue. This is in Windows 7 x64 with trusty64 and in my Vagrantfile I have `config.vm.network :private_network, ip: "192.168.50.4"`.

When issuing `vagrant up` to a box I had previously interrupted proper startup/shutdown for, vagrant attempted to create a new box. On resolving that issue and associating it with the old box, another `vagrant up` yielded multiple `Warning: Connection timeout. Retrying...` lines leading to a timeout. Increasing the timeout period did not help. When booting with gui, I saw the same `cloud-init-nonet` message mentioned by [@zerkms](https://github.com/zerkms) and it was giving up after the second wait period of 120 seconds. In my case the box would boot but have no network connectivity and I could not SSH into it. This is also similar to the issue described in [Varying-Vagrant-Vagrants/VVV#375](https://github.com/Varying-Vagrant-Vagrants/VVV/issues/375).

I went into the VirtualBox interface and manually removed all networking settings from the relevant box, then went into adapter settings and removed all of the (several) 'VirtualBox Host-Only Network' network adapters. Issuing `vagrant up` after taking those actions, and ensuring that the two relevant network interfaces in VirtualBox were connected, the box started successfully with only one or two connection timeout warnings, which seems to be normal.

For others who stumble across this bug report while searching, this bug has been fixed in Vagrant, but you can still get the "waiting for" delays if you're /etc/networking/interfaces file has extra ifaces in it.

Boot the machine with VBox Gui, wait the three or so minutes for the machine to boot, then login as root and edit /etc/networking/interfaces and **make sure it doesn't have duplicate or extra ethX interfaces.**

This happened to me when using Varying-Vagrant-Vagrants/VVV and abruptly halting the machine, and fiddling with VBox's network interfaces.

```
cloud-init-nonet[4.54]: waiting 10 seconds for network device
cloud-init-nonet[14.57]: waiting 120 seconds for network device
cloud-init-nonet[134.57]: gave up waiting for a network device.
```

Thanks [@Ramblurr](https://github.com/Ramblurr) I was struggling to figure out why sometimes I was still running into the problem. Your advice got it sorted for me and now I know how to resolve it every time I get into that situation.

Thanks [@Ramblurr](https://github.com/Ramblurr) for the **make sure it doesn't have duplicate or extra ethX interfaces** comment.

[@Ramblurr](https://github.com/Ramblurr), thanks!

> this bug has been fixed in Vagrant, but you can still get the "waiting for" delays if you're /etc/networking/interfaces file has extra ifaces in it.

Is it fixed? (not snarky, but genuine). I:

1. had a private network w/ a static IP in my Vagrantfile, booted and halted.
2. removed it from my Vagrantfile
3. booted

Then observed these long delay symptoms. I would have expected that Vagrant would have removed the entry in interfaces (perhaps on next boot?).

it is not fixed in the latest version of vagrant (1.7.4)  
problem can only be fixed manually (for latest `ubuntu/trusty32` box)

Vagrantfile:

```
...
config.vm.network "private_network", ip: "192.168.50.123", auto_config: false
...
config.vm.provider "virtualbox" do |vb|
 # Display the VirtualBox GUI when booting the machine
 vb.gui = true
end
...
```

start VM  
`vagrant up`

use VirtualBox GUI to login to VM as root  
create new network interface

/etc/network/interfaces.d/eth1.cfg:

```
auto eth1
iface eth1 inet static
    address 192.168.50.123
    netmask 255.255.255.0
```

reload VM  
`vagrant reload`

Same problem here.

This issue should definitely be reopened and looked forward.

[@wembernard](https://github.com/wembernard)   
you can try this:  
add this code to `/etc/rc.local` of your vm

```
ifdown eth0
sleep 1
ifup eth0
exit 0
```

or try to enable intel virtualization in BIOS, it worked for me, it seems virtualization is required even for 32 bit operation systems (ubuntu/trusty32), otherwise eth0 ipv4 network interface is not working until restart

Same issue. No real solution found.  
UP!

[@Jonasse79](https://github.com/Jonasse79) did you try one of the solutions from my post above?

[@alexkart](https://github.com/alexkart) Yep. First I checked if virtualization was enabled in the BIOS (OK) then I tried to "sudo" some specified instructions about VirtualBox GUI and SSH, then I tried to modify the vagrantfile...   
My host OS is ubuntu 64 bits 14.04 (LTS) and I'm currently trying to launch Open Edx (cypress) with VirtualBox 5 and Vagrant 1.7.4 on a virtualised ubuntu 12 64 bits server OS.  
I spent many hours reading posts but did not manage to solve my problem.

When I "vagrant up" everything is OK at launch, but then the connexion fails.  
And then I got the "Trying to connect .. fail" message again and again!!!

I have the same problem.  
But I noticed that when I start a headless instance of Ubuntu Trusty, Vagrant fails at almost every attempt to launch it (passing occasionally, though). When using GUI, however, `vagrant up` works most (but not all) of the time.

Here's the guest's `/interfaces.d/eth0.cfg`:

```
auto eth0
iface eth0 inet dhcp
```

And its `interfaces`:

```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

# Source interfaces
# Please check /etc/network/interfaces.d before changing this file
# as interfaces may have been defined in /etc/network/interfaces.d
# NOTE: the primary ethernet device is defined in
# /etc/network/interfaces.d/eth0
# See LP: #1262951
source /etc/network/interfaces.d/*.cfg
```

Anything wrong with those files?

What operating systems does Vagrant's `private_network` actually work under? Clearly not Ubuntu...

try to login to your guest with `vb.gui = true`  
and type `ifconfig` command, you should see `eth0` network interface if you do not see it then, try

```
ifdown eth0
ifup eth0
```

if you see `eth0` in `ifconfig` now and you can ssh to the guest, see this comment above [#3860 (comment)](https://github.com/mitchellh/vagrant/issues/3860#issuecomment-159664011)

[@ddugovic](https://github.com/ddugovic) I didn't setup any `private_network` inside my Vagrantfile. I use the NAT connection to access my guest machine which is, by the way a Windows 7 machine. But I'm curious: why (not 'what for') did you ask that question? I mean, what was in the files I pasted that seemed 'out of place' to you?

[@alexkart](https://github.com/alexkart) I just updated the said file and I'll see what will happen.

[@ahmedsaoudi](https://github.com/ahmedsaoudi) I am responding to [this comment](https://github.com/mitchellh/vagrant/issues/3860#issuecomment-156086822) and I have no problem with your Vagrantfile.

My needs are different since I need to use bridged mode for my guest which I need to be publicly accessible, and it sounds like bridged mode is completely broken (or not supported) for Vagrant.

[@ddugovic](https://github.com/ddugovic) Oh! I'm sorry ^^'

Hi everyone.  
I solve the problem. My solution relevant for vagrant 1.7.4 and virtualbox 5.0.12

Root a problem - ubuntu 14.04(trusty, 32 bit) incorrect work with Intel network adapter. Use AMD network adapter to resolve the problem.

Example Vagrantfile this <https://gist.github.com/Apach47/5277f9ac1ab4312b6ec5>

## Solution step by step

### Step 1 - require

Add or change in the vagrantfile provider section:

```
config.vm.provider "virtualbox" do |vb|
    ### Change network card to PCnet-FAST III
    # For NAT adapter
    vb.customize ["modifyvm", :id, "--nictype1", "Am79C973"]
    # For host-only adapter
    vb.customize ["modifyvm", :id, "--nictype2", "Am79C973"]
  end
```

### Step 2 - optional

- Add `auto_config: false` to network section
- Add follow code to provision section

```
config.vm.provision "shell", inline: <<-SHELL
    rm -f /etc/network/interfaces.d/eth1.cfg
    echo "auto eth1" >> /etc/network/interfaces.d/eth1.cfg
    echo "iface eth1 inet static" >> /etc/network/interfaces.d/eth1.cfg
    echo "address 192.168.35.25" >> /etc/network/interfaces.d/eth1.cfg
    echo "netmask 255.255.255.0" >> /etc/network/interfaces.d/eth1.cfg
    ifdown eth1 && ifup eth1
  SHELL
```

For default, vagrant change `/etc/network/interfaces` file and it is not a problem, but since ubuntu 14.04 setting for adapter store in `interfaces.d` folder. I suggest to follow this

@Apach47 Thanks, that works perfectly!

I can confirm the fix for these same versions of vagrant and virtualbox.

@Apach47 Thanks !

@Apach47 Amazing! Thanks it works !!!

I had no problems with the private\_network settings per se, but I had a similar problem, in which my VM would hang after the first reboot on the cloud-init screen, even after waiting out for 20m). It was cause by NFS mounts(the machine booted and rebooted fine when I commented out the NFS mounts from fstab) which I resolved by moving my mounts to rc.local.

This was with both ubuntu as host and guest btw.

[@kumaxim](https://github.com/kumaxim) Thanks, this appears to be working.

Attach files by dragging & dropping,
[selecting them](https://github.com/mitchellh/vagrant/issues/3860#), or pasting
from the clipboard.
[anexo ausente] Uploading your files…
Unfortunately, we don’t support that file type.
[Try again](https://github.com/mitchellh/vagrant/issues/3860#) with a
PNG, GIF, JPG, DOCX, PPTX, XLSX, TXT, PDF, or ZIP.
Attaching documents requires write permission to this repository.
[Try again](https://github.com/mitchellh/vagrant/issues/3860#) with a PNG, GIF, or JPG.
Unfortunately, we don’t support that file type.
[Try again](https://github.com/mitchellh/vagrant/issues/3860#) with a PNG, GIF, or JPG.
Yowza, that’s a big file.
[Try again](https://github.com/mitchellh/vagrant/issues/3860#) with a file smaller than 10MB.
This file is empty.
[Try again](https://github.com/mitchellh/vagrant/issues/3860#) with a file that’s not empty.
This browser doesn’t support file attachments.
We recommend updating to the latest
[Internet Explorer](http://windows.microsoft.com/ie),
[Google Chrome](https://chrome.google.com/), or
[Firefox](https://www.mozilla.org/firefox).
Something went really wrong, and we can’t process that file.
[Try again.](https://github.com/mitchellh/vagrant/issues/3860#)
