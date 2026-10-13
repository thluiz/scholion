---
url: "http://www.howtogeek.com/howto/windows-vista/using-symlinks-in-windows-vista/"
captured_at: "2012-05-26T02:40:55-03:00"
title: "Using Symlinks in Windows Vista - How-To Geek"
domain: "howtogeek-com"
---

# [Using Symlinks in Windows Vista](http://www.howtogeek.com/howto/windows-vista/using-symlinks-in-windows-vista/ "Using Symlinks in Windows Vista")

One of the long-awaited features in Windows Vista was the ability to use symbolic links, the way you can in linux. Sadly, they don’t work quite as well as they could, but it’s a big upgrade from prior versions, and has solved a number of problems for me already.

### **Using the mklink Command**

The command that you need to use is *mklink*, which you’ll use from the command line. Just type it on the command line to see the options:

> ```
> C:\Users\geek>mklink
> Creates a symbolic link.
>
> MKLINK [[/D] | [/H] | [/J]] Link Target
>
>         /D      Creates a directory symbolic link.  Default is a file
>                 symbolic link.
>         /H      Creates a hard link instead of a symbolic link.
>         /J      Creates a Directory Junction.
>         Link    specifies the new symbolic link name.
>         Target  specifies the path (relative or absolute) that the new link
>                 refers to.
> ```

For instance, if you wanted to make the folder C:\Users\Geek\TestFolder available from C:\TestFolder as well, you could use the following command.

> C:\mklink /D C:\TestFolder C:\Users\Geek\TestFolder  
> symbolic link created for C:\TestFolder <<===>> C:\Users\Geek\TestFolder

Now if you look in C:\TestFolder directory, you’ll see whatever files were in the other directory.

### **Understanding the Options.**

**MKLINK link target**

Using the command without any extra options creates a soft link to a file.

**/D creates a symbolic link, or a soft link.**

This essentially acts like a shortcut to a folder in prior versions of Windows, except you don’t have to use an actual shortcut.

**/H creates a hard link, which points directly to the file.**

This option can’t be used for folders directly for some reason, you’ll have to use the next option.

**/J creates a “Directory Junction”**

A Directory Junction is actually just a hard link to a directory. This is a feature that existed prior to Vista as well. If you are trying to symlink to a directory using a hard link, then you should use this option.

### **Understanding Hard vs Soft Links**

**Hard Link**

A hard link directly points to the file, and acts to the operating system as if it is the file itself. You’ll want to use this option the majority of the time if you are trying to fake an application’s directory.

**Soft Link**

A soft link is essentially a shortcut to a file or folder – if you are using Windows explorer, you’ll be redirected to the directory if you double-click on a shortcut, it won’t pretend its part of the filesystem. You can still directly reference or open a file with the symlinked path, and it mostly works.

### **Using Symlinks from a Network Share**

One of the things that’s been extensively discussed is that you cannot use the Vista symlinks from another operating system (not surprising), but you cannot use them from a network share either. This is troublesome if you expect to use this feature on a web server or a file server.

### **Deleting Symlinks**

To delete a symlink, you can just delete the link. Just make sure you don’t delete the original file.

[Don't show again X](# "Click to hide")

|  |  |
| --- | --- |
| Subscribe | Daily Email Updates |
|  | You can get our how-to articles in your inbox each day for free. Just enter your email below:   |  |  |  | | --- | --- | --- | | Email: |  |  | |

### Comments (47)

1. Mike Scott

   Excellent post, that really laid it out for me. I figured the gist of what they were, but didn’t fully appreciate the differences. Thanks.
2. Alexandre

   Good post, but I have something to add to network shares: with Windows Longhorn Server you will be able to create link to network shares.

   Cheers  
   Alexandre
3. The Geek

   Alexandre,

   That’s very interesting, I hadn’t heard that. I’m going to have to look into that more.
4. brett

   Ya, but System Restore will NOT work properly. Temporary user accounts appear, and all user settings seem to be lost. Argh! :(
5. Bernard Kerckenaere

   To be a bit more correct:

   \* shortcut: on the operating system level (to applications who wish to read/write the link, it’s just a meaningless file)

   \* soft link (or symbolic link): like a shortcut, but on the filesystem level (applications reading/writing the link, will actually read/write the file linked to)  
   -> unfortunately this only works with folders on Windows, not with files (which is the reason I’m searching around for information at the moment, I need file symlinks, like in \*nix.)  
   -> this will work across partitions, or drives

   \* hard link: only for files, what happens is that there are multiple file entries that point to the same physical data, when you delete one entry, the other will still work, the data won’t be gone until all entries are deleted (if with a soft link you delete the original directory, the link won’t work anymore!)  
   -> you can obviously only create hard links to a file on the same partition
6. Knight

   I recommend this app: <http://schinagl.priv.at/nt/hardlinkshellext/hardlinkshellext.html>

   Easy Drag and Drop creation of hard links, symbolic links, etc for Vista and XP.
7. Concept nicely explained and simplified. Thanks.

   And now for a good laugh: try creating a link, within a folder, to itself, as in…

   1. We have a folder called C:\TestFolder  
   2. Within TestFolder, we create a link:  
   mklink /D myself C:\TestFolder  
   3. We now click on the new link and start laughing…. or crying ( your choice! )

   I just wonder: Should it be considered a bug ?
8. Steve Steele

   Could this be used to ‘move’ the C:\Users folder to D:\Users (or another drive) by making C:\Users a hard link to D:\Users ???

   I’m thinking that C:\Users would still exist but would link to and store files in D:\Users

   And ‘safer’ then the rather messy registry hack (which I’ve heard has some issues and limitations)
9. Ryan Beesey

   Yes Steve, you can do that. Actually Vista does something very similar when it installs to give legacy applications a psuedo Pre-Vista environment. Open a command prompt and cd to the root. Type dir. You’ll see Users as expected, but notice that Documents and Settings is no where to be found. Try to cd to Docu[tab]… it comes right up. Press ESC and now type dir /a. You’ll see that Documents and Settings has been made into a Junction. Try exploring your User directory, you’ll be surprised at how many places Microsoft has used Junctions and how few people know.
10. Frank

    Hi, I did not get the point about using Hardlinks on network shares.

    What I just tried:  
    1) created a network share BACKUP1 on E:\BACKUP1 (on vista)  
    2) cmd > e: > cd backup1 > mklink /J TEST1 W:\Music (on vista)  
    3) used mount -t smbfs \*\*someoptions\*\* //192.168.2.2/BACKUP1 /tmp/testsmb on my linux box  
    4) cd /tmp/testsmb/TEST1/\*\*somedeeperstructure\*\*/ (on linux box)  
    5) less a.txt (on linux box)

    Result: worx perfectly.

    BTW: no SP1 applied to Vista.  
    Cheers, Frank
11. Style14

    I’m having an error with this:

    ‘C:\mklink’ is not recognized as an internal or external command, operable program or batch file.

    Running Vista Ultimate with SP1.

    Any help?
12. I’m familiar with the concept of hard and soft (symbolic) links from Unix/Linux, and it’s good to see Microsoft attempting to add such a useful feature to Windows.

    It’s also the case in Unix/Linux that you can create soft links to a folder, but not a hard link — and there’s a logical reason for it. Whenever you create a new file or folder, it is automatically hard-linked to, anyway, from its directory entry. If you create additional hard links to a file, they’re additional directory entries that are just as “valid” as the original directory entry that was formed with the file’s creation. That’s why, as Bernard points out, a file pointed to by multiple hard links doesn’t get finally removed until the last hard link to it is deleted. A soft link, on the other hand, is not as “valid” as a hard link. You can create a soft link that points to a non-existent file or folder. You could remove a file/folder pointed to by a soft link, and the existence of the soft link will not prevent it happening. After the removal of the file/folder pointed to by a soft link, the latter will remain, uselessly pointing into fresh air.

    The logical problem with multiple hard links to a folder is that, in a hierarchical structure, there can only be one path upward from a folder (as when you do a “cd ..” command). If there are multiple hard links to a folder, then which one of them would be the appropriate path to follow upwards? After all, all hard links to a file/folder are equally “valid”.

    Again, as Bernard remarks, hard linking can only be done to a file within the same partition, as the directory entry will refer to what it points to by an internally-used number (called an “inode” in Unix/Linux, but I don’t know what the Windows term is). Such internal numbering will be unique \*within\* a partition, but can’t be unique \*across\* multiple partitions.
13. Meant to add …

    Soft links don’t point to an “inode” or similar. That’s why they’re not “hard”. They simply include a path to whatever they’re meant to point to, and hope for the best. Because they don’t rely on a unique “inode” number (or similar in Windows), there is no logical impediment to soft links pointing to files/folders in other partitions.
14. Peter

    Has anyone had any success circumventing the windows update failures with symlinks?  
    I have my program files, users, etc moved onto different partitions, but occasional windows updates fail because of the file copy mechanism they use (which doesn’t support symlinks) Occurs with the recent KB952287 update (if people want to try it), and the Hold Em poker game in Ultimate.

    Apart from that, the symlinks have been excellent
15. jdackle

    Question:  
    Will Windows symlinks (NOT shortcuts) be recognised as such by Linux with the NTFS-3G driver (or any other driver)?

    E.g.:  
    Vista symlink: C:\Testfolder -> C:\Users\me\Testfolder  
    In Linux: cd /mnt/vista/Testfolder = cd /mnt/vista/Users/me/Testfolder ?
16. Peter

    I can almost guarantee you that they wont. (Not natively), across a network I think they do, because it’s still Vista serving them, but I vaguely remember reading that they work completely differently internally to linux ones. Sorry :D
17. jd2066

    I have a dual boot with Linux and the symlinks are not recognized.  
    It seems like it should be possible for the NTFS-3G driver to do so. I can only guess it’s ether not a priority or is a hard thing to do.  
    Also NTFS-3G lets you store Linux symlinks on an NTFS partition but Windows Vista doesn’t recognize them.
18. jdackle

    I asked this same question on the NTFS-3G forum and the answer by its lead developper was:  
    “Only Interix style Windows symlinks are supported at the moment (Windows Services for Unix) and junction support is in the work.”

    Windows Services for Unix is not available for Vista mainly because a big part of it already ships with Vista, Interix included (according to the Wikipedia). :)
19. Fair DeLune

    On Vista Home Premium.

    As soon as I discovered symlinks I wanted to shift my Documents folder to D: So I followed some tutorial and it moved just fine. Except some program was still using one file in the original so the original Documents folder remained undeleted. So I had two entries in Explorer and their contents are different.

    I renamed one of them to “Documents on C” emptied that folder. So I should be able to delete that pesky original Documents (renamed). But no. Deleting that deletes the D: version, EEEK!! No worries I got it back from the bin.

    I will open a command window and make the necessary changes. I just wanted to warn folks symlinks could have lost me a lot of data.

    Thanks for the info.
20. abhishek

    hi Blue,  
    Nice finding , well one more thing which is definetly going to be considered as a bug.  
    if you create a symlink (or so called soft link) , of a directory inside that directory itself .Then we won’t be able to delete it also !!!!!  
    OoPPs!!!!!!!
21. Rene Lindsay

    Is there any way of making executable folders in Windows or Linux?  
    I have always hated symlinks and shortcuts, ever since I switched from RiscOS to Windows 95.  
    Executable folders in RiscOS was a far more elegant solution than the Windows Shortcuts, and Im looking for a way to bring this great feature to Windows.

    For those who dont know, an executable folder is an application folder which also has the features of a shortcut, all in one. This lets you treat a complex application as if it was a stand-alone executable.  
    Let me explain:  
    A simple application such as notepad.exe is completely portable and atomic. It consists of a single relocatable customised icon which can be placed on your desktop, or anywhere and just runs when clicked. There’s no need for an installer/uninstaller, since you just copy it to make more, or press delete to uninstall.

    The problems start if your application requires some external data files. Now you need a folder to keep your exe and all its data files together. Of course its still messy to have to open the folder to locate and run the exe among all its data files. So, you create a shortcut link to the exe, so you can run it without having to open its folder. This is where it all goes wrong: Now you have two seperate entities, the shortcut, and the folder. If only the folder could also act as the shortcut to the exe within, such as RiscOS does, then you wouldnt need to split them up.  
    By convention, the shortcut gets placed on your desktop or start menu, and the folder gets hidden in C:\Program Files. This causes more problems than it solves. The folder can no longer be moved, without breaking the shortcut, and now you need an installer/uninstaller to manage your app.  
    And the shortcut concept is not very intuitive for new windows users. How often have you seen new users delete a shortcut to uninstall an app, not knowing that the real app is still hidden in Program Files? Also, if they copy the shortcut to another computer, it will no longer work.

    An executable folder solves all these problems. It groups the app, its data files and its shortcut together in a single atomic icon, which wont break if you copy it to a new location, and can be uninstalled simply by pressing delete. Its so much simpler to use and more intuitive for beginners.  
    The executable folder takes on the icon of the exe, and runs the app when clicked. Or, you can still open it as a folder, by selecting “Explore” from its right-click context menu.

    So far I have found 2 windows features which ALMOST reproduces this functionality:  
    You can place an Autorun.inf file on a cd, to specify what icon to display on the CD drive icon, and what exe to run when its clicked. Unfortunately this only works in the root of a filing system, such as a cd or a Usb key, and it wont work on application folders on your desktop.

    I got even better results from junction points:  
    I created a folder, and set its system bit with: chmod +s MyFolder  
    I then placed notepad.exe, and a shortcut to notepad.exe in it, and called the shortcut “Target”  
    Finally I create a Desktop.ini file containing the following text:  
    [.ShellClassInfo]  
    CLSID={0AFACED1-E828-11D1-9187-B532F1E9575D}

    Suddenly MyFolder takes on the notepad icon, and its properties shows that it is now a sortcut to the Notepad.exe within. The only problem is, if you click the shortcut/folder, nothing happens. This type of Symlink only works if “Target” was linked to a folder, and not a file. Maybe its possible to make it work if I use the correct GUID in desktop.ini, or change some regitry settings?  
    Or maybe I need to write the COM class myself, but then I need to know more about exactly how the folder shortcut class works.  
    Does anyone know were I can find more info on this?  
    Any help would be greatly appreciated.

### Comments are closed on this post.

If you'd like to continue the discussion on this topic, you can do so at our forum.  
  
  
[Go to the Forum](http://www.howtogeek.com/forum/)

[anexo ausente]
