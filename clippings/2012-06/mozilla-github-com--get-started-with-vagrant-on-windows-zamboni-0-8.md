---
url: "http://mozilla.github.com/zamboni/topics/install-zamboni/vagrant-on-windows.html"
captured_at: "2012-06-23T21:37:20-03:00"
title: "Get Started With Vagrant On Windows — zamboni 0.8 documentation"
domain: "mozilla-github-com"
---

# Get Started With Vagrant On Windows[¶](#get-started-with-vagrant-on-windows "Permalink to this headline")

Here is a guide to help you get started installing Zamboni inside a vagrant virtual machine on Windows. Once you’re done, you can go back to [*installing Zamboni with vagrant*](http://mozilla.github.com/zamboni/topics/install-zamboni/install-with-vagrant.html) .

## Install Virtual Box[¶](#install-virtual-box "Permalink to this headline")

Download and install Oracle’s VirtualBox if you haven’t already.
<http://www.virtualbox.org/>

## Install Git[¶](#install-git "Permalink to this headline")

Download and install mysysgit from: <http://code.google.com/p/msysgit/downloads/list>
This is needed so that Windows has git capablity.

In Git Setup you need to choose the following options:

> - On “Adjusting your PATH environment” dialog choose “Run Git from the Windows Command Prompt”.
> - On “Choosing the SSH executable” dialog choose “Use OpenSSH”.
> - **IMPORTANT**: On “Configuring the line ending conversions” dialog choose “Checkout as-is, commit Unix-style line ending”.

## Install Ruby[¶](#install-ruby "Permalink to this headline")

Download and install RubyInstaller from: <http://rubyinstaller.org/downloads/>
Make sure to select option to add ruby path executable paths.

Download and extract Development Kit from above URL. Probably easiest to extract to C:\DevKit

Then follow developer kit installation instructions at: <https://github.com/oneclick/rubyinstaller/wiki/Development-Kit>

Summary of instructions:

> - Using command prompt cd folder development kit was extracted into (e.g. cd c:\DevKit)
> - Run the command ruby dk.rb init. Then run the command ruby dk.rb install to install rubygems.
> - Confirm installation by running the following commands:
>   - gem install rdiscount --platform=ruby
>   - ruby -rubygems -e "require 'rdiscount'; puts RDiscount.new('\*\*Hello RubyInstaller\*\*').to\_html" command prompt should echo out <p><strong>Helo RubyInstaller </strong></p>

## Install Vagrant[¶](#install-vagrant "Permalink to this headline")

Run the command gem install vagrant

If you are running 64bit Windows you MUST use v0.9.6 or above otherwise Virtual Box will not be detected properly.

## Get Zamboni Code[¶](#get-zamboni-code "Permalink to this headline")

cd to the folder above where you want the zamboni folder and files to be placed (e.g. c:\)
Run the command git clone --recursive git://github.com/mozilla/zamboni.git
This will take some time, go get a cup of coffee, eat lunch, go for a walk, etc.

In the zamboni folder (e.g. c:\zamboni) find the file Vagrantfile and open it in your favorite text editor.

Look for the following lines:

```
# For convenience add something like this to /etc/hosts: 33.33.33.24 z.local
# config.vm.network :hostonly, "33.33.33.24"
config.vm.network "33.33.33.24"  # old 0.8.* way
```

Change them to:

```
# For convenience add something like this to /etc/hosts: 33.33.33.24 z.local
config.vm.network :hostonly, "33.33.33.24"
#config.vm.network "33.33.33.24"  # old 0.8.* way
```

## Start The Zamboni VM[¶](#start-the-zamboni-vm "Permalink to this headline")

It is time to build your zamboni virtual machine. In the command prompt, cd to the zamboni folder (e.g. cd c:\zamboni) and run the command vagrant up. This step will download the zamboni virtual machine from Mozilla and install it. Before warned that this archive is many hundred megabytes in size so it will take some time to download even if you are on a broadband connection.

### Configure SSH[¶](#configure-ssh "Permalink to this headline")

Download PuTTY SSH client and PuTTYgen from <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>. These are standalone executable files. You need to save them in their permanent location, (e.g. C:\Program Files (x86)\Putty).

You need to generate a private key for PuTTY. To do this, launch PuTTYgen and click on the “generate” button. You will be instructed to randomly move your mouse around the PuTTYgen window to generate the key. Once this is done, click on “load” and find the file “insecure\_private\_key”, it will probably be in your user folder under ”.vagrant.d” (e.g. on Win7 at C:\Users\{your username}\.vagrant.d). Now save your public key and then save your private key (use different file names for each).

Create a PuTTY SSH session for zamboni. Launch PuTTY. In the host name put “127.0.0.1” and in the port use “2222”. In the category pane find “data” under “connection” and place “vagrant” in the auto-login username field. Then expand out the “SSH” branch and select “auth”. Next to the “private key file for authentication” field click on browse and find the private key you just generated. Select it and click “open” in the folder browser window. Now go back to “session” in the category pane in PuTTY, add “vagrant” to the saved sessions field and then click “save”. This will save your session for future use.

Login to zamboni by clicking on “open” in the PuTTY window. This should automatically log you into the Zamboni VM. If you add the PuTTY file path to your system properties environment variable “path” (e.g. ;C:\Program Files (x86)\Putty) you should be able to reference PuTTY from the command prompt by simply calling “putty -load vagrant” once you reboot your computer.

The first time you log into Zamboni you should see a very long series of scrolling text with lots of SQL statements etc. This is the database migrations taking place. This phase could take quite a while to complete. Don’t do anything to your PuTTY VM session until it gives you back a command prompt.

Congratulations if things went well your Zamboni VM is up and running. You are now ready to start the Dev Server.

### Start the Dev Server[¶](#start-the-dev-server "Permalink to this headline")

From PuTTY VM session, enter the command ./project/vagrant/bin/start.sh.

You should now be able to access your development server on a special IP address set up by Vagrant. Point your web browser to <http://33.33.33.24:8000/>

More info on [*installing Zamboni with vagrant*](http://mozilla.github.com/zamboni/topics/install-zamboni/install-with-vagrant.html) .

page 2

## MySQL[¶](#mysql "Permalink to this headline")

On your dev machine, MySQL probably needs some tweaks. Locate your my.cnf (or
create one) then, at the very least, make UTF8 the default encoding:

```
[mysqld]
character-set-server=utf8
```

Here are some other helpful settings:

```
[mysqld]
default-storage-engine=innodb
character-set-server=utf8
skip-sync-frm=OFF
innodb_file_per_table
```

On Mac OS X with homebrew, put my.cnf in /usr/local/Cellar/mysql/5.5.15/my.cnf then restart like:

```
launchctl unload -w ~/Library/LaunchAgents/com.mysql.mysqld.plist
launchctl load -w ~/Library/LaunchAgents/com.mysql.mysqld.plist
```

some of the options above were renamed between MySQL versions

Here are [more tips for optimizing MySQL](http://bonesmoses.org/2011/02/28/mysql-isnt-yoursql/)  on your dev machine.

## Memcached[¶](#memcached "Permalink to this headline")

We slipped this in with the basic install. The package was
libmemcached-dev on Ubuntu and libmemcached on OS X. Switch your
settings\_local.py to use

```
CACHE_BACKEND = 'caching.backends.memcached://localhost:11211?timeout=500'
```

## RabbitMQ and Celery[¶](#rabbitmq-and-celery "Permalink to this headline")

See the [*Celery*](http://mozilla.github.com/zamboni/topics/install-zamboni/celery.html)  page for installation instructions. The
[*example settings*](http://mozilla.github.com/zamboni/topics/install-zamboni/installation.html#example-settings) set CELERY\_ALWAYS\_EAGER = True.
If you’re setting up Rabbit and want to use celeryd, make sure you remove
that line from your settings\_local.py.

## elasticsearch[¶](#elasticsearch "Permalink to this headline")

See [*elasticsearch*](http://mozilla.github.com/zamboni/topics/install-zamboni/elasticsearch.html)  for more instructions.

## Redis[¶](#redis "Permalink to this headline")

On OS X the package is called redis. Get it running with the launchctl
script included in homebrew. To let zamboni know about Redis, add this to
settings\_local.py:

```
CACHE_MACHINE_USE_REDIS = True
REDIS_BACKEND = 'redis://'
```

The REDIS\_BACKEND is parsed like CACHE\_BACKEND if you need something
other than the default settings.

## LESS CSS[¶](#less-css "Permalink to this headline")

We’re slowing switching over from regular CSS to LESS. You can learn more about
LESS at <http://lesscss.org>.

If you are serving your CSS from the same domain as the page, you don’t
need to do anything. Otherwise, see “Installing LESS (alternative)” below.

You can make the CSS live refresh on save by adding #!watch to the URL or by
adding the following to your settings\_local.py:

```
LESS_LIVE_REFRESH = True
```

If you want syntax highlighting, try:

### Installing LESS (alternative)[¶](#installing-less-alternative "Permalink to this headline")

You only need to do this if your CSS is being served from a separate domain, or
if you’re using zamboni in production and running the build scripts.

If you aren’t serving your CSS from the same domain as zamboni, you’ll need
to install node so that we can compile it on the fly.

First, we need to install node, npm and LESS:

```
brew install node
curl http://npmjs.org/install.sh | sh
npm install less
```

If you type lessc, it should say “lessc: no input files.”

Next, add this to your settings\_local.py:

```
LESS_PREPROCESS = True
LESS_BIN = 'lessc'
```

Make sure LESS\_BIN is correct.

Not working?
:   - If you’re having trouble installing node, try <http://shapeshed.com/journal/setting-up-nodejs-and-npm-on-mac-osx/>. You need brew, which we used earlier.
    - If you’re having trouble with npm, check out the README on <https://github.com/isaacs/npm>
    - If you can’t run LESS after installing, make sure it’s in your PATH. You should be
      able to type “lessc”, and have “lessc: no input files” returned.
