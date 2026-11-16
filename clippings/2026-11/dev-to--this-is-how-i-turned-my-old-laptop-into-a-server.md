---
url: "https://dev.to/jayesh_w/this-is-how-i-turned-my-old-laptop-into-a-server-1elf"
captured_at: "2026-11-16T01:40:16+00:00"
title: "This is how I turned my old laptop into a server."
domain: "dev-to"
---

I had a working old laptop and was itching to do something with it. And then I decided to turn it into a personal home server. This post will also work on any machine, you just need a monitor,keyboard,ethernet cable and an USB port.  
**Let’s start!**

## [](#1-choosing-an-operating-system)1\. Choosing an Operating System

When we hear about servers one thing that comes in our mind is Linux.Some of them do run windows but I’d personally go with Linux. Because it’s fast, has a whole community and is open source( an I’ve been using Linux for past 1 year )  
Before choosing an operating system I’d like to share my machine’s specification :  
4 GB RAM,Intel core 2 duo processor, 512 GB HDD.

**Which Flavor of Linux to choose from?**  
Many people are confused while migrating from windows or mac OS to Linux platform.  
This is because Linux itself has many flavors but most of them are based on  
1.Debian  
2.Arch  
3.Red Hat  
**So which one to go with?**  
I’ve Tried all three of them and for beginners the most recommended system is any Debian based OS ( Ubuntu, Kali, Debian , Lubuntu, ParrotOS,Mint)  
Most of the servers work on RHEL(Red Hat Enterprise Linux) and its flavors such as CentOS or Fedora.

**Why didn't I go with CentOS?**  
CentOS is based on RHEL which is quite tricky for beginners also my system is old and has low end hardware. That is the reason why I selected Ubuntu server for my machine.

## [](#2-downloading-ubuntu-server-2004-and-making-a-live-bootable-usb)2\. Downloading Ubuntu Server 20.04 and making a live bootable USB

Download the ubuntu server from the following [link](https://ubuntu.com/download/server)  
After downloading it, ensure you have an empty usb device to make it bootable.  
If you are using windows download [rufus software](https://rufus.ie/) and run it.  
Google if you have any problems while making bootable usb with rufus as it is pretty easy.  
For Linux Users download any usb Image writer tool and you are good to go.

## [](#3-booting-into-the-usb-and-setting-up-the-server)3\. Booting into the USB and setting up the Server.

Make sure that your files are moved to another computer as we are using the whole space for our server. We are going to erase the entire disk for the same purpose.

Plug in the live bootable usb and start the machine. Press F12 to go to boot options. Select the USB option and click enter.  
Use **arrow keys** and the **enter key** to select options.

After Few seconds there will be an option to choose your language.

### [](#welcome-screen)**Welcome Screen**

[![Welcome](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fuatxjtlcyavfuph78ete.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fuatxjtlcyavfuph78ete.png)  
Select your language (English) and click enter.

### [](#keyboard-configuration)**Keyboard Configuration**

Select Keyboard type English US and click enter.

_(Now here comes the tricky part.)_

### [](#network-connections)**Network Connections**

[![Network Config](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Foko99y1pqolm9fp5cc3g.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Foko99y1pqolm9fp5cc3g.png)

If you have plugged in your ethernet cable from your wifi Router you don’t really have to worry a lot. The installer will automatically detect the **DHCP** settings from the router and you just have to click enter. But if you don’t have any ethernet cable you have to go through a series of package installations only to connect to internet.

### [](#configure-proxy)**Configure Proxy**

If your system requires any http proxy to connect to the internet enter the proxy address otherwise, just click on Done.

### [](#guided-storage-configurations)**Guided Storage Configurations**

[![Guided Storage config](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fucpdvjdynkkggw8bnek3.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fucpdvjdynkkggw8bnek3.png)  
As mentioned earlier we are going to utilize the entire HDD space for our home server and that's why select Use and Entire Disk option and click on done.

### [](#storage-configuration)**Storage Configuration**

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fxgvfg1yts9o3zx0js0c0.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fxgvfg1yts9o3zx0js0c0.png)  
Your Hard disk space will be now divided into two partitions: one for the operating system itself and the other for GRUB Bootloader.  
Review your settings and click on done.

### [](#profile-setup)**Profile Setup**

[![Install](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F5p1nz586kttzkjbfgfxy.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F5p1nz586kttzkjbfgfxy.png)  
Enter your name , Your Server’s name(this name will be visible to other devices) , Your username and password. Click on done.

### [](#ssh-setup)**SSH setup**

[![Featured](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F33o7acsr5mx6sermgk95.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F33o7acsr5mx6sermgk95.png)  
Select on Install OpenSSH server because that’s how you will connect to your server inside a private network.

### [](#featured-server-snaps)**Featured Server Snaps**

[![ssh](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fgvr8ojjhwc9mvgpcfxm6.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fgvr8ojjhwc9mvgpcfxm6.png)  
Select any desirable feature for your server, I selected none because We will install them manually as per future requirements.

### [](#installing-system)**Installing System**

[![Profile](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F8oun7h6vybe5o9g2n4ga.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F8oun7h6vybe5o9g2n4ga.png)  
Now you have to wait for a few minutes for your system to install. After Installation is complete the prompt will ask you to remove your USB device and reboot. Follow the reboot process and the system will automatically boot up. And You will see a terminal like this

There you go ! you have turned your old laptop into a personal home server.

## [](#4-changing-the-root-password)4\. Changing the root password

Type the following command  
**_sudo -i_**  
It will ask for your password.  
After entering your password you will be logged in as root with # sign  
Type the command  
**_passwd_**  
Type suitable root password twice and you have changed your root password  
Type **_exit_** to exit as root  
Type **_su_** to log in as root

## [](#5-connecting-your-server-via-wifi)5\. Connecting Your server via Wi-Fi.

Assuming you still have your ethernet wire plugged in, Install the following packages  
rfkill , wireless-tools , net-tools and wpasupplicant  
With following commands  
**_sudo apt install rfkill wireless-tools net-tools wpasupplicant_**  
After installing them go through the following [link](https://www.linuxbabe.com/command-line/ubuntu-server-16-04-wifi-wpa-supplicant) for detailed explanation to connect to your WiFi

After a reboot plug out the ethernet cable run the following command  
**_ifconfig_**  
and view the private ip address.

Now from another computer  
If you are using windows download Putty or if you are Linux or MacOS user run the command  
**_ssh username@ip\_addr_**  
Enter your password  
Voila! You have just accessed your system inside your private network.  
[![login](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fzi6rs3nhrqocnc71bkew.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fzi6rs3nhrqocnc71bkew.png)  
\*\*\* you will see a welcome screen like this\*\*\*

## [](#6-installing-webmin)6\. Installing Webmin

[![Webmin](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F5o1gx6isxm3ctzj60pk8.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F5o1gx6isxm3ctzj60pk8.png)  
Webmin is a web-based interface for sysadmins. Using any modern web browser, you can setup user accounts, Apache, file sharing and much more. Webmin removes the need to manually edit Unix configuration files like /etc/passwd, and lets you manage a system from the console or remotely.  
Follow this [guide](https://linuxize.com/post/how-to-install-webmin-on-ubuntu-18-04/) to install webmin.

## [](#cool-things-to-do-with-this-home-server)Cool Things to do with this home server.

1.  Store Backup of your files
2.  Install a LAMP server to run websites.
3.  Install SMTP server to send mails.
4.  Use it as a database backup server.
5.  Test your Apps on this server before deploying them.
6.  Create a private git repository server.
7.  Save your videos and music and stream them over the web.
8.  For machine learning enthusiast save your training data on this server and train your model so that there is less stress on your working machine(It requires high end server)
9.  Use it as a ftp server.
10.  Install nginx to run and test web apps.
11.  Download and install OwnCloud to maintain your files.

On this server I save my web projects (LAMP stack). I also use it to backup my database and website from the public server by setting up a cron job.I saved a lot of movies and steam them by just writing a small php script :)

**__\-_\-_Thank you!_\-_\-__**
