---
url: "http://kvz.io/blog/2009/12/15/run-nodejs-as-a-service-on-ubuntu-karmic/"
captured_at: "2013-04-15T11:21:46-03:00"
title: "Run Node.js as a Service on Ubuntu - Kevin van Zonneveld"
domain: "kvz-io"
---

# Run Node.js as a Service on Ubuntu

Dec 15th, 2009 | [Comments](#disqus_thread)

The core of [our new project](http://transload.it/ "Transload.it")  runs on [Node.js](http://nodejs.org/ "Node.js") . With Node you can write very fast JavaScript programs serverside. It’s pretty easy to install Node, code your program, and run it. But how do you make it run nicely in the background like a true server?

Clever chaps will have noticed you can just use the ‘&’ like so:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` node ./yourprogram.js & ``` |

and send your program to the background. But:

- if Node ever prints something and your console is closed, the STDOUT no longer exists and `yourprogram.js` will die
- what if the process crashes, what if your server reboots?

Ok, so we needed something more robust. More like a real daemon, one that’s recognized by the Operating System as such.

### Upstart

Our servers run Ubuntu’s latest: Karmic Koala, which packs a pretty decent version of [upstart](http://upstart.ubuntu.com/wiki/Stanzas "How to write upstart scripts") . Upstart will eventually replace the well-known `/etc/init.d` scripts, and will bring some additional advantages to the table like: speed, health checking, simplicity, etc.

## Writing an upstart script

Turns out, writing your own upstart scripts is way easier than building init.d files based on the `/etc/skeleton` file.

Ok so here’s how it looks like; You should store the script in `/etc/init/yourprogram.conf`, create one for each Node program you write.

(nodejs.conf) [download](http://kvz.io/downloads/code/kvzlib/bash/scraps/nodejs.conf) 

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` | ``` description "node.js server" author      "kvz - http://kevin.vanzonneveld.net"  # used to be: start on startup # until we found some mounts weren't ready yet while booting: start on started mountall stop on shutdown  # Automatically Respawn: respawn respawn limit 99 5  script     # Not sure why $HOME is needed, but we found that it is:     export HOME="/root"      exec /usr/local/bin/node /where/yourprogram.js >> /var/log/node.log 2>&1 end script  post-start script    # Optionally put a script here that will notifiy you node has (re)started    # /root/bin/hoptoad.sh "node.js has started!" end script ``` |

Wow how easy was that? Told you, upstart scripts are childsplay. In fact they’re so compact, you may find yourself changing almost every line cause they contain specifics to our environment.

### non-root

Node can do a lot of stuff. Or break it if you’re not careful. So you may want to run it as a user with limited privileges. We decided to go conventional and chose `www-data`.

We found the easiest way was to prepend the Node executable with a sudo like this:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` exec sudo -u www-data /usr/local/bin/node ``` |

Don’t forget to change your export HOME accordingly.

## Restarting your Node.js daemon

This is so ridiculously easy..

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` start yourprogram stop yourprogram ``` |

And yes, Node will already:

- automatically start at boottime
- log to `/var/log/node.log`

..that’s been defined inside our upstart script.

### initctl

But wait, `start` and `stop` are just shortcuts. Who’s really behind the wheel here, is `initctl`. You can play around with the command to see what other possibilities there are:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` initctl help initctl status yourprogram initctl reload yourprogram initctl start yourprogram # yes, this is the same start # etc ``` |

## Update from October 30th, 2012

The basic idea has not changed since 2009, but we did add some tricks to our upstart script. Here’s what we now use in production at [transloadit.com](http://transloadit.com) :

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` | ``` # cat /etc/init/transloaditapi2.conf # http://upstart.ubuntu.com/wiki/Stanzas  description "Transloadit.com node.js API 2" author      "kvz"  stop on shutdown respawn respawn limit 20 5  # Max open files are @ 1024 by default. Bit few. limit nofile 32768 32768  script   set -e   mkfifo /tmp/api2-log-fifo   ( logger -t api2 </tmp/api2-log-fifo & )   exec >/tmp/api2-log-fifo   rm /tmp/api2-log-fifo   exec sudo -u www-data MASTERKEY=`cat /transloadit/keys/masterkey` /transloadit/bin/server 2>&1 end script  post-start script    /transloadit/bin/notify.sh 'API2 Just started' end script ``` |

## More on Node.js

With Node you can write very fast JavaScript programs serverside. We’ve seen [examples](http://wiki.github.com/ry/node "Node wiki on GitHub shows links to many Node projects")  of chat, key-value store, and full blown http servers. Basically anything is possible as long as you know JavaScript and the concepts of parallel/evented processing. You don’t? Well if you’ve ever used `setTimeout()`, you’ll soon get the hang of it ; )

- [Node.js video presentation](http://jsconf.eu/2009/video-nodejs-by-ryan-dahl.html)  by creator Ryan Dahl
- [Node.js slides](http://nodejs.org/jsconf.pdf)  that accompany the presentation
- [About Node](http://nodejs.org/#about) on the official website
- [Node.js is genuinely exciting](http://simonwillison.net/2009/Nov/23/node/)  by Simon Willison
- [node.js](http://debuggable.com/posts/node-js:4ab4d9d7-b788-41d4-85c0-1b51cbdd56cb)  by Debuggable

### Imported comments

These were imported from my old blog. Please use disqus below for new comments

**[Remco](https://rem.co)**  on 2012-06-22 15:44:16   
 Thanks for sharing your wisdom! I’ve used your example in combination with ‘forever’ to keep everything running smoothly, as explained on SO:  
  
http://stackoverflow.com/questions/11084279/node-js-setup-for-easy-deployment-and-updating/11157223#11157223

**kinzeron**  on 2012-06-11 20:12:29   
 Won’t be a problem to daemonize nodejs like this ? AFAIK a daemon needs two forks. Doing :

```
 nodejs ./path/code.js &
amp;
```

  
 would only fork it once if memory serves well. The daemon might still take terminal control! no ?

**Arcadius**  on 2012-04-11 23:16:10   
 Hi.  
 I have seen your presentation nodejs-in-production on slideshare.  
 My question is: Why do you serve only a part of the site on node.js? I would have thought that node.js could handle it all and that the ngix/php bit would go away.  
  
Thanks.  
  
Arcadius.

**[mark](http://smartcall.cc/)**  on 2012-03-14 21:25:10   
 100% perfect!

**[h](http://kvz.io/blog/2009/12/15/run-nodejs-as-a-service-on-ubuntu-karmic/mahdijamal.com)**  on 2012-02-07 07:34:56

```
your_code_here();
```

**Andy**  on 2012-01-27 10:58:41   
 Do you think this could work on CentOs?

**[Rindra](http://twitter.com/rajrindra)**  on 2011-12-14 18:03:14   
 Hi,   
  
First i would like to say that this works really great as is. Thanks a lot!   
 Now I’ve tried to use the upstart script with a static file server I’ve created with node.js  
 When I run it from the terminal: node main.js everything works fine in the browser. The issue occurs when i start my server as a daemon, start app, nothing appears in the browser.  
  
I’m starting on node.js and i love the platform, so is this a misconception on my end? I would love to get your input on this.  
  
Thanks again!

**claude hussenet**  on 2011-11-27 13:12:37   
 Works like a charm !  
  
Claude Hussenet

**[Mauvis Ledford](http://www.readystate4.com)**  on 2011-09-18 20:17:23   
 Just a note that I followed your directions on Ubuntu 11.04 and everything worked except for on reboot.  
  
With some research I ended up modifying this line to get it working:  
  
from: start on started mountall  
 tp: start on (local-filesystems and net-device-up IFACE=eth0)  
  
I guess, the internet wasn’t ready when the script was executing.  
  
Cheers,  
  
Mauvis

**[Herman A. Junge](http://kvz.io/blog/2009/12/15/run-nodejs-as-a-service-on-ubuntu-karmic/hermanjunge.com)**  on 2011-09-12 18:01:36   
 Thanks a Lot. I was looking for an elegant solution to that problem.  
  
hermanjunge

**dale**  on 2011-07-07 23:00:58   
 i can’t seem to get this to work correctly. I have always type in `sudo start myapp` in order for this to start. So when i reboot my server, this script does not fire at all. I actually changed the user:group to my www-data:www-data user/group, and gave the file permissions of 774. but even with that, i still need to run sudo to get the file to start. any clues on what else i may be able to do to get this to start on server reboot?

**[Geoff Wagstaff](http://www.gosquared.com/)**  on 2011-05-12 23:28:01   
 Great write-up on getting upstart working. For those who want to have node processes persist after they close the terminal without upstart, you could use nohup:

```
nohup node script.js &
gt; /dev/null
```

**[Aaron Fay](http://aaronfay.ca/)**  on 2011-05-04 18:08:28   
 Simply awesome, thanks for the upstart info. Being able to ‘restart node-app’ is just bloody awesome.  
  
Thanks,  
 Aaron

**Kevin**  on 2011-04-17 16:56:53   
 @ Eran Hammer-Lahav: Thanks, changed it.  
  
@ Joey: Sure : ) I just like how small upstart scripts can be and that it can resuscitate crashed programs.

**Joey**  on 2011-03-30 06:30:05   
 Thanks for the init.d version, Peter!  
  
For anyone (like me) running a server on an older distro release, using Upstart is either not possible, impractical, or overkill when you already have init.d.  
  
And for anyone (again, like me) running a server on a new distro, you’re at least as likely to have systemd (which will replace Upstart in the long run) available to you as you are Upstart.  
  
I think I’ll stick with good ol’ init.d (which is available & amp; highly compatible on every distro I’ve installed) until the distros figure this out ;)

**[Eran Hammer-Lahav](http://hueniverse.com)**  on 2011-03-17 20:21:07   
 Should it be:  
  
exec /usr/local/bin/node /where/yourprogram.js & gt;& gt;/var/log/node.log 2& gt;& amp;1  
  
instead? The original version does not save exceptions to the log file.

**Kevin**  on 2011-03-04 13:22:34   
 @ peter host: Thanks for sharing. Keep in mind upstart will replace init.d in the long run though.

**[ipage](http://ipage.webhostingtop.co)**  on 2010-12-31 18:03:30   
 This is what I have been looking for! Thanks for this helpful tutorial!

**[peter host](http://www.oghme.com)**  on 2010-12-04 12:30:51   
 Clear and to the point :)  
 As a complement for users who like it the init.d way :  
 https://gist.github.com/715255

**[Ovidiu](http://www.thinkovi.com)**  on 2010-10-28 15:16:42   
 Awesome tutorial, thank you, works really well!

**Kevin**  on 2010-10-11 13:54:12   
 @ hellcats: well try debugging it a little.   
 what happens when you just run  
  
/usr/local/bin/node /where/yourprogram.js 2& gt;& amp;1 & gt;& gt; /var/log/node.log  
  
what about:  
  
/usr/local/bin/node /where/yourprogram.js ?

**[watch hellcats online](http://watch-hellcats-online.co.cc)**  on 2010-10-01 11:31:09   
 copy-pasted the example, only replacing /where/yourprogram.js for my program - but after & quot;sudo start myprogram& quot; it must crash. Nothing is logged. Using upstart 0.6.3-11 on karmic.

**[Sami Samhuri](http://samisamhuri.blogspot.com)**  on 2010-08-16 19:26:56   
 Thanks Kevin! This is exactly what I needed.

**Kevin**  on 2010-08-12 12:43:28   
 @ AFire: Read more carefully. The first message your script sends to STDERR, and your terminal is closed, your script is killed. But you've probably figured that out, or resorted to using monit by now.  
  
@ Xavier: The same way that I:  
 export HOME=\& quot;/root\& quot;  
  
You could export your PATH as well if that's required.  
 so first echo $PATH, and put that in there

**[Xavier](http://kvz.io/blog/2009/12/15/run-nodejs-as-a-service-on-ubuntu-karmic/xdamman.posterous.com)**  on 2010-07-15 03:58:43   
 For whatever reasons I cannot make it work. My program doesn't seem to run in the same environment and path.exists returns errors when node is launched via initctl.  
 I checked the require.paths array and it is exactly the same whether I run directly node app.js or if I do \& quot;start node\& quot;.  
  
I also tried to to run \& quot;env\& quot; before (sudo -u myuser env /usr/local/bin/node /path/app.js …) but doesn't help.  
  
I run out of ideas. Thanks for your support.

**AFire**  on 2010-07-13 17:41:24

```
 node ./yourprogram.js | tee -a node.log &
amp;
```

**Kevin**  on 2010-06-10 20:59:04   
 @ Francisco: Did you get it working? As for the real-world program, here it is: http://transloadit.com/

**Francisco**  on 2010-05-25 18:06:29   
 I was being a bit silly, I fixed my program to be executable from an absolute path.   
  
I copy-pasted the example, only replacing /where/yourprogram.js for my program - but after \& quot;sudo start myprogram\& quot; it must crash. Nothing is logged. Using upstart 0.6.3-11 on karmic.

**Francisco**  on 2010-05-25 16:49:23   
 Thanks for the write up!  
  
Hey guys did you manage to run a real-world program? Mine requires a library with a relative path so I can't call it from anywhere (like, node /path/to/my.js).  
  
I either need to cd /path/to & amp;& amp; node my.js , or use chdir - but none has worked for me. Any ideas?

**Kevin**  on 2010-02-26 13:41:06   
 @ George: Cool thanks for sharing!

**[George](http://illuminatikarate.com)**  on 2010-02-25 06:06:26   
 Thanks for this, worked like a charm.  
  
The only thing I had to change was that I change to the directory containing my .js file before launching node. For whatever reason, I otherwise have trouble loading static files into my node.js app.  
  
Cheers!

**Kevin**  on 2010-01-07 18:46:34   
 @ jz: Correct, I actually had to change it from /etc/event.d to /etc/init/ when we upgraded to Karmic. It looked as if they were going to stick with /etc/init in the long run though, so be prepared to change it back at one point ;)

**[jz](http://jzlabs.com)**  on 2009-12-25 21:41:11   
 thanks for the writeup!  
  
for some reason, on 8.10 i had to put the conf file in /etc/event.d for initctl to find it…

**sveisvei**  on 2009-12-16 09:56:01   
 Useful stuff, thanx :)

**Kevin**  on 2009-12-15 21:22:53   
 @ Mariano Iglesias: Hey. That's a trick I didn't know yet, thanks a lot Mariano!

**[Mariano Iglesias](http://www.marianoiglesias.com.ar)**  on 2009-12-15 21:16:30   
 @Felix: also, if you want to run a script in background, and not link it to your session (so if you logout it doesnt die), use nohup:  
  
$ nohup script & amp;

**Kevin**  on 2009-12-15 21:11:56   
 @ Felix Geisendörfer: Thanks for adding some sugar to the post! While screen won't give you healthchecks, or come online when your server recovers from a crash, it's definitely another great tool in our arsenal!

**[Felix Geisendörfer](http://www.debuggable.com/)**  on 2009-12-15 21:08:20   
 Cool article Kevin, glad you published this : )!  
  
If you just need something slightly better than \& quot;node ./yourprogram.js & amp;\& quot;, because you might just be doing a long running job, you can type in \& quot;screen\& quot; and then execute \& quot;node ./yourprogram.js\& quot; in the new terminal that opens. Screen sessions don't die if you log out, and you can even re-attach them using \& quot;screen -r\& quot; when you login the next time.
