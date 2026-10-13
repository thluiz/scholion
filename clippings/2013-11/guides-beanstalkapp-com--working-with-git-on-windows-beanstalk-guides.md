---
url: "http://guides.beanstalkapp.com/version-control/git-on-windows.html"
captured_at: "2013-11-17T19:46:56-03:00"
title: "Working with Git on Windows  •  Beanstalk Guides"
domain: "guides-beanstalkapp-com"
---

## Installing SSH keys on Windows

To access your Git repositories you will need to create and install SSH keys. You can do this in two ways:

- by using [OpenSSH](http://www.openssh.com/) (generating SSH keys with `ssh-keygen` which comes with Git)
- by using [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) (free Telnet and SSH client)

OpenSSH and PuTTY are free implementations of Telnet and SSH for Windows. They encrypt all traffic and provide secure communication with your remote Git repositories by using SSH keys.

**We recommend OpenSSH over PuTTY**, and it’s installed with your Git copy. PuTTY is recommended only for advanced users who are already familiar with how Git with SSH keys work.

### Using OpenSSH and generating SSH keys with ssh-keygen

To communicate with the remote Git repository in your Beanstalk account from your Windows computer, you will need to generate an SSH key pair for that computer. This process requires only a few steps, but you do first need to install msysGit using the full installer as described above.

#### Generating a key pair

To do this you need to run Git Bash, which can be found in your `Start` menu. Run the command:

```
ssh-keygen -t rsa
```

It will ask for location and pass phrase. Accept the default location (usually `C:\Documents and Settings\username\.ssh\` or `C:\Users\username\.ssh`) by pressing `Enter`. After that, make sure to [set a strong pass phrase](http://guides.beanstalkapp.com/version-control/tips-for-using-ssh-keys.html#ssh-keys-with-passphrase-or-without) for the key.

Now that the keys are generated, open the file `id_rsa.pub` (found in the default location from the previous step) with a text editor. The contents of this file is your new public key. If you copy it to your clipboard, you can add it to your Beanstalk profile (under the `Profile and Settings → Keys=` section).
