---
url: "https://dev.to/ko31/linux-commands-useful-when-performing-heavy-processing-2bdc"
captured_at: "2026-11-16T00:51:46+00:00"
title: "Linux commands useful when performing heavy processing"
domain: "dev-to"
---

[![Ko Takagi](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F43017%2F8f272011-29a5-4e93-b26a-95260e3fdb5e.jpeg)](https://dev.to/ko31)

[Ko Takagi](https://dev.to/ko31)

Posted on Dec 28, 2019 Edited on Dec 29, 2019

## [](#sleep)sleep

The `sleep` command suspends processing for a certain period of time.

For example, when running a heavy shell script, using the sleep command moderately can reduce the load.  

```
# Delay 10 seconds(no option)
sleep 10

# Delay 10 seconds
sleep 10s

# Delay 5 minutes
sleep 5m

# Delay 3 hours
sleep 3h
```

Enter fullscreen mode Exit fullscreen mode

## [](#nicerenice)nice/renice

The `nice` command can be executed with priorities.

For example, when performing a backup or batch process, the process can be performed without affecting other processes.

You will be able to batch process more safely, even at lunchtime when the website is crowded by many people.  

```
# Without option, run at +10 priority
nice /path/to/command

# Run at +10 priority
nice -n 10 /path/to/command
```

Enter fullscreen mode Exit fullscreen mode

Priority options can be specified from -20 (higher) to 19 (lower). However, negative values can only be specified by superuser.

You can also use the `renice` command to adjust the priority of already running processes.  

```
# Adjust the priority of pid 99999 process
renice 10 -p 99999
```

Enter fullscreen mode Exit fullscreen mode

## [](#nohup)nohup

If you use the `nohup` command, you can continue processing even if you log out of the terminal.

After executing the command, you can close the computer and go to bed calmly.  

```
nohup /path/to/command &
```

Enter fullscreen mode Exit fullscreen mode

Standard output during execution of the nohup command is saved in the `nohup.out` file.
