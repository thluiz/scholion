---
url: "http://www.pwrusr.com/system-administration/solved-centos-6-networking-and-hyper-v"
captured_at: "2014-03-22T21:27:02-03:00"
title: "[SOLVED] CentOS 6 networking and Hyper-V. | pwrusr.com"
domain: "pwrusr-com"
---

# [[SOLVED] CentOS 6 networking and Hyper-V.](http://www.pwrusr.com/system-administration/solved-centos-6-networking-and-hyper-v "Permanent Link to [SOLVED] CentOS 6 networking and Hyper-V.")

March 1st, 2012 by Andrea Matesi 12914 Views 

Recently I have been playing with CentOS on Hyper-V. My personal opinion is that both products are great.

My lab is made of:

- Microsoft Windows Server 2008 R2 w/SP1.
- Hyper-V Role enabled.
- CentOS 6.2 x64 minimal iso.
- Linux Integration Services for Hyper-V version 3.2 w/ synthetic drivers.

I experienced networking problems while CentOS was booting, more specifically:

/var/log/dmesg:eth0: Dropping NETIF\_F\_SG since no checksum feature.  
/var/log/messages:Mar  1 11:00:25 pwrusrdev1 kernel: eth0: Dropping NETIF\_F\_SG since no checksum feature.

This specific issue seems related to the fact that the "Checksum offload feature" is missing from the virtual ethernet interface. But since we're speaking about a *virtual* interface, and the feature we're talking about is a *hardware* feature, implemented by manufacturers such as intel inside their ethernet silicon to offload the Checksum calculations from the CPU, consider this thing just a naggie and no more.

CentOS minimal doesn't have a gui, so no network config here, but I can live with that :)

Now many people are wondering "why CentOS minimal" and "CentOS minimal *sucks*", but on my next article series I'm gonna show you how great CentOS minimal is and how to put this smart Linux distribution to good use.

Consider this article as an *entréé* on CentOS6-minimal networking configuration.

So, I was configuring networking by creating a \_single\_ config file inside /etc/sysconfig/network-scripts/ifcfg-eth0   
with the following lines:

nano /etc/sysconfig/network-scripts/ifcfg-eth0   
DEVICE=eth0  
BOOTPROTO=static  
ONBOOT=yes  
NETWORK=192.168.1.0  
NETMASK=255.255.255.0  
IPADDR=192.168.1.4

As you can see, I was trying to setup a static IP address on eth0. But generating only this file for CentOS networking simply isn't enough.

[**UPDATE 03/APR/2012**]: After Mr. Matt Gorecki comment, I've researched a more viable and efficient alternative and I've found a very clever description from Mr. Mark Wagner at the following address: <http://serverfault.com/questions/189445/what-is-the-order-of-precedence-for-redhat-network-configuration-files>.

Basically, he explains that CentOS Network Manager scripts create hard links instead of what I suggested.

My original description was (**ignore it!**):

> You'll have to copy this file inside 2 other directories, like so:
>
> cp /etc/sysconfig/network-scripts/ifcfg-eth0 /etc/sysconfig/networking/devices/  
> cp /etc/sysconfig/network-scripts/ifcfg-eth0 /etc/sysconfig/networking/profiles/default/
>
> And make sure their permissions are set correctly, like so:
>
> chmod 644 /etc/sysconfig/network-scripts/ifcfg-eth0  
> chmod 644 /etc/sysconfig/networking/devices/ifcfg-eth0  
> chmod 644 /etc/sysconfig/networking/profiles/default/ifcfg-eth0

The following is my new explanation (**follow it!**):

Since CentOS scripts seems to create hard links when defining ethernet devices, to maintain uniformity with what CentOS does, you can:

ln /etc/sysconfig/network-scripts/ifcfg-eth0 /etc/sysconfig/networking/devices/ifcfg-eth0  
ln /etc/sysconfig/network-scripts/ifcfg-eth0 /etc/sysconfig/networking/profiles/default/ifcfg-eth0

Once this is done, you'll have to name you computer with the hostname command:

hostname my-system-name

Then you need to edit another file, /etc/sysconfig/network

NETWORKING=yes  
HOSTNAME=my-system-name  
GATEWAY=192.168.1.1

Save and set its permissions to 644 like so:

chmod 644 /etc/sysconfig/network

Reboot and your networking should be working just fine.

Bonus: once we're at it, let's set up name resolution! Open /etc/resolv.conf and input a "nameserver statement" like this:

nameserver 192.168.1.1
