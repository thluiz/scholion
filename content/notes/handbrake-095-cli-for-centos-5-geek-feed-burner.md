---
title: "Handbrake 0.9.5 CLI for Centos 5"
date: '2012-07-02T00:17:12-03:00'
category: webclip
summary: 'The post gives a step-by-step process to build the Handbrake 0.9.5 CLI on CentOS 5, including EPEL setup, required packages, a separate autoconf install, source download, and compilation.'
tags: ["handbrake", "centos-5", "cli", "build-from-source"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Handbrake 0.9.5 CLI for Centos 5 « Geek Feed Burner"
    url: "http://gfb.baccanasta.com/?p=88"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-07/gfb-baccanasta-com--handbrake-095-cli-for-centos-5-geek-feed-burner.md"
    kind: repo
---

The post outlines a build procedure for Handbrake 0.9.5 CLI on CentOS 5. It starts by adding the EPEL repository, then installs the packages needed to build a binary, installs autoconf in /opt, downloads the HandBrake source, and runs the build with GTK disabled.

## Reading notes

- Add the EPEL RPM repository for either 32-bit or 64-bit CentOS 5.
- Install the build dependencies with yum, including libtool, jam, rpmdevtools, bzip2-devel, zlib-devel, subversion, git, yasm-devel, yasm, intltool, gcc-c++, and make.
- Install autoconf 2.61 separately under /opt/autoconf instead of replacing the system version.
- Download HandBrake 0.9.5 source code and extract it.
- Set PATH to include /opt/autoconf/bin, run configure with --disable-gtk, then go into build and run make.
