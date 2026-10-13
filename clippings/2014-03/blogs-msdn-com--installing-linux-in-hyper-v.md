---
url: "http://blogs.msdn.com/b/visualstudiouk/archive/2013/11/20/installing-linux-in-hyper-v.aspx"
captured_at: "2014-03-22T21:26:47-03:00"
title: "Installing Linux in Hyper-V - Microsoft Visual Studio UK Team - Site Home - MSDN Blogs"
domain: "blogs-msdn-com"
---

# Installing Linux in Hyper-V

This is one of two “side posts” that have come out of putting together [What does Team Foundation Server 2013 offer the non-Windows user](http://blogs.msdn.com/b/visualstudiouk/archive/2013/11/20/what-does-team-foundation-server-2013-offer-the-non-windows-user.aspx "What does Team Foundation Server 2013 offer the non-Windows user?")? In order to take a look at the new Web Test capabilities in TFS 2013 I wanted to try them out in a non-Windows environment, so I decided to create a Linux desktop virtual machine.  I wanted to record a few points that I found made the installation and use of the virtual machine that much easier. I’ve also posted an equivalent note on installing Team Explorer Everywhere in Eclipse.

## Preparing the virtual machine

Installing Linux in Hyper-V is essentially straightforward:

- Get hold of your Linux distro. In my case [Fedora 19](http://fedoraproject.org/).
- In Hyper-V Manager create a new  Virtual Machine:

> [![image](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/1172.image_5F00_thumb_5F00_30C64B9B.png "image")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/5342.image_5F00_1EE7271D.png)

- I assign 2048 MB for RAM, as that’s plenty for general use, but I make it dynamic in case it’s needed:

> [![image](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/8311.image_5F00_thumb_5F00_440992EB.png "image")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/8468.image_5F00_06E5D766.png)

- Leave Configure Networking as Not Connected and we’ll sort that in the section below:

> [![image](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/3326.image_5F00_thumb_5F00_29CBBA78.png "image")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/7271.image_5F00_6F50BAA3.png)

- I set my hard disk size to be 20GB as that should be plenty for a standard install with Eclipse:

> [![image](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/1261.image_5F00_thumb_5F00_070D136C.png "image")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/2870.image_5F00_5512E230.png)

- Then just add the Linux distro iso file as a bootable DVD:

> [![image](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/5270.image_5F00_thumb_5F00_1A505ABC.png "image")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/7558.image_5F00_2F3F4C7E.png)

That’s it, the virtual machine is ready to be used. But before starting the machine for the first time see the section below.

## Important networking step before starting the installation

Networking. It’s much easier to get the Linux installation to do the configuration, and I think the easiest way to do that is to setup a legacy network adapter in the virtual machine. If you’re using a Linux distro that’s supported in Hyper-V you can use the Linux Integration Services, but here I’m using an “unsupported” distro, as this is more likely for desktop installs.

- With the virtual machine selected in Hyper-V Manager, select the virtual machine settings
- Then select Add Hardware and choose Legacy Network Adapter:

> [![image](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/3515.image_5F00_thumb_5F00_4285247F.png "image")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/7776.image_5F00_706FE686.png)

- Click Add and select a virtual switch that gives the connectivity you want. In my case using my network card for external access. If this isn’t available, you need to set it up in Hyper-V Manager as a virtual switch.

> [![image](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/6558.image_5F00_thumb_5F00_1CB18ECD.png "image")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/5621.image_5F00_18A4B04A.png)

- Click Apply
- Next, remove the “non legacy” Network Adapter:

> [![image](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/5086.image_5F00_thumb_5F00_596BA80E.png "image")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/6012.image_5F00_555EC98B.png)

- Click OK
- Now, you can start the virtual machine and follow the installation steps for the distro. Once you’ve installed it, ejected the bootable DVD and restarted you should be in and with a working network connection:

> [![image](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/3247.image_5F00_thumb_5F00_1A9C4217.png "image")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/2781.image_5F00_1D426D17.png)

- In my case the network settings were setup for me on my network:

> [![image](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/4617.image_5F00_thumb_5F00_373B4E9B.png "image")](http://blogs.msdn.com/cfs-file.ashx/__key/communityserver-blogs-components-weblogfiles/00-00-01-50-54-metablogapi/6305.image_5F00_60AF8FDB.png)

That’s it. You should now have a clean Linux install with networking configured, enabled and working.

Cheers,   
Giles

Windows Live Tags: [Linux](http://windows.live.com/connect/tag/Linux),[Hyper-V](http://windows.live.com/connect/tag/Hyper-V),[Team Foundation Server](http://windows.live.com/connect/tag/Team Foundation Server),[installation](http://windows.live.com/connect/tag/installation),[Eclipse](http://windows.live.com/connect/tag/Eclipse),[Fedora](http://windows.live.com/connect/tag/Fedora),[configuration](http://windows.live.com/connect/tag/configuration),[setup](http://windows.live.com/connect/tag/setup),[legacy](http://windows.live.com/connect/tag/legacy),[adapter](http://windows.live.com/connect/tag/adapter),[settings](http://windows.live.com/connect/tag/settings),[Hardware](http://windows.live.com/connect/tag/Hardware),[Network](http://windows.live.com/connect/tag/Network)
