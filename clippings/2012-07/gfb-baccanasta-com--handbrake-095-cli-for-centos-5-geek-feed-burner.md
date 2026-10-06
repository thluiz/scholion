---
url: "http://gfb.baccanasta.com/?p=88"
captured_at: "2012-07-02T00:17:12-03:00"
title: "Handbrake 0.9.5 CLI for Centos 5 « Geek Feed Burner"
domain: "gfb-baccanasta-com"
---

# Handbrake 0.9.5 CLI for Centos 5 « Geek Feed Burner

Handbrake 0.9.5 is out and I’m going to post a new tutorial to install the CLI version on Centos 5. I found the following steps at [Julian’s Corner](https://julianscorner.com/wiki/linux/handbrake_centos) , site to wich I attribute the work.

1) Install the Extra Packages for Enterprise Linux (EPEL) RPM Repository (32-bit version):

|  |  |
| --- | --- |
|  | `rpm -Uvh http:``//download``.fedora.redhat.com``/pub/epel/5/i386/epel-release-5-4``.noarch.rpm` |

or 64-bit version:

|  |  |
| --- | --- |
|  | `rpm -Uvh http:``//download``.fedora.redhat.com``/pub/epel/5/x86_64/epel-release-5-4``.noarch.rpm` |

2) Install required packages to build a binary file:

|  |  |
| --- | --- |
|  | `yum` `install` `libtool jam rpmdevtools` `bzip2``-devel \`  `zlib-devel subversion git yasm-devel yasm \`  `intltool gcc-c++` `make` |

3)Install a newer version of autoconf without overwriting the original one; just put it into a different location:

|  |  |
| --- | --- |
|  | `wget http:``//ftp``.gnu.org``/gnu/autoconf/autoconf-2``.61.``tar``.bz2`  `tar` `xjf autoconf-2.61.``tar``.bz2`  `cd` `autoconf-2.61`  `.``/configure` `--prefix=``/opt/autoconf`  `make`  `make` `install`  `cd` `..` |

(/opt path is intended for optional software packages)

4) Download Handbrake source code and extract all files into a folder:

|  |  |
| --- | --- |
|  | `wget http:``//handbrake``.fr``/rotation``.php?``file``=HandBrake-0.9.5.``tar``.bz2`  `tar` `jxf HandBrake-0.9.5.``tar``.bz2` |

5) Finally, build the program:

|  |  |
| --- | --- |
|  | `cd` `HandBrake-0.9.5`  `export` `PATH=``/opt/autoconf/bin``:$PATH`  `.``/configure` `--disable-gtk`  `cd` `build`  `make` |
