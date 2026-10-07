---
url: "http://www.mkyong.com/linux/how-to-find-a-file-in-linux/"
captured_at: "2012-08-02T10:27:57-03:00"
title: "How to find a file in linux"
domain: "mkyong-com"
---

# How to find a file in linux

In \*nix, you can use “`find`” command to find a file easily.

```

$find {directory-name} -name {filename}

```

#### 1. Find file in the root directory

If you have no idea where the file is located, you can search the entire system via the “/” root directory. Below example show you how to find a file ‘testing.txt’ in the entire system drive.

*P.S To find in “/” root, you need permission, just issue `sudo`.*

```
$ sudo find / -name 'testing.txt'
 
find: /dev/fd/3: Not a directory
find: /dev/fd/4: Not a directory
/Users/mkyong/Documents/workspace/JavaTesting/testing.txt
/Users/mkyong/testing.txt
```

#### 2. Find file in a specified directory

Find file ‘testing.txt’ in directory ‘/Users/mkyong’ and all its subdirectory..

```
$ sudo find /Users/mkyong -name 'testing.txt'
/Users/mkyong/Documents/workspace/JavaTesting/testing.txt
/Users/mkyong/testing.txt
```

#### Reference

1. [Linux ‘find’ command tutorial](http://content.hccfl.edu/pollock/unix/findcmd.htm)
