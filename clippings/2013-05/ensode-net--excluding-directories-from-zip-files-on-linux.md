---
url: "http://www.ensode.net/roller/dheffelfinger/entry/excluding_directories_from_zip_files"
captured_at: "2013-05-20T10:50:12-03:00"
title: "Excluding directories from zip files on Linux : David R. Heffelfinger"
domain: "ensode-net"
---

I frequently have to turn in source code to one of my customers in zip files (not fancy nor sophisticated, but that's life).

Lately, I've been working on a project that uses good old plain ANT build files. I load this project into NetBeans as a free form project so that I can have a decent working environment. NetBeans of course creates its own folders and files so that it can open the project. I am also using [Mercurial](http://www.ensode.net/roller/dheffelfinger/entry/thoughts_on_distributed_version_control) for version control, which creates an .hg folder that I don't want to distribute.

 I wanted to zip up the code, while excluding the directories and files that were not meant to be distributed (.hg and the NetBeans specific files and folders). I'm on Linux, therefore I usually use [file roller](http://fileroller.sourceforge.net/), a graphical archive management tool for the GNOME desktop, to create my zip files. File roller is very easy to use, just right click the directory to be archived and select "create archive".

Unfortunately there is no way to easily exclude files or directories from the zip file, I thought I could zip up the whole thing, then delete the unwanted files and directories. This worked fine for files, but for directories it deleted the files in the directory, but left the directory in the zip file.

Obviously file roller wasn't meeting my needs here, it was time to go to the good old command line. Most Linux distributions come with a command line zip utility appropriately named "zip". I read the man page and found a way to tell zip to exclude files and directories from the created archive, all that needs to be done is use the -x switch and list the files and directories to be excluded, separated by spaces, for example:

`zip -r filename.zip directoryname/* -x directoryname/.hg\* directoryrname/nbproject\* directoryname/catalog.xml`

The above command will do exactly what I needed, which is to create a zip file without the Mercurial and NetBeans specific files and directories. Of course any file or directory name can be passed as a parameter to the -x switch.  

Posted by David R. Heffelfinger _@ 04:43 PM EST_
