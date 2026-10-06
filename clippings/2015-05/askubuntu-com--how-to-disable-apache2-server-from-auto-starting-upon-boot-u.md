---
url: "http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up"
captured_at: "2015-05-22T11:59:10-03:00"
title: "how to disable apache2 server from auto starting upon boot up"
domain: "askubuntu-com"
---

# [how to disable apache2 server from auto starting upon boot up](http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up)

|  |  |
| --- | --- |
| up vote down vote [favorite](http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up# "This is a favorite question (click again to undo)") **23** | I was wondering how can I disable the apache2 server from running upon boot up? I can't seem to find an option which disables it to auto start when I turn on the machine.  [apache2](http://askubuntu.com/questions/tagged/apache2 "show questions tagged 'apache2'") |
|  | |  |  | | --- | --- | |  | Perhaps someone can be more specific, but I can point you in the right direction... in /etc, there are directories for rc\*.d, which contain all the start/stop scripts, called, I think, init scripts. You'll see links to scripts that are in /etc/init.d, and starting with either "k" or "s", for "kill" or "start", and a number which is the ordering. –  [Marty Fried](http://askubuntu.com/users/39753/marty-fried "7963 reputation") [Aug 1 '12 at 2:27](http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up#comment210018_170640) | |  | Yes, I knew about the /etc/rcX.d directories, but I searched for it to find out about some nicer tool, than just manually renaming files (life is too short). `update-rc.d` has filled this void. –  [Tomasz Gandor](http://askubuntu.com/users/309037/tomasz-gandor "101 reputation") [Sep 26 '14 at 8:53](http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up#comment721316_170640) |  add a comment |

|  |  |
| --- | --- |
| up vote down vote accepted | Under the folder /etc/init.d/ you will find all the init scripts for different boot up services. like apache2 , networking etc.  depending on which runlevel the computer starts in, different services are started. so from the /etc/init.d/ folder each "service" is linked to one / many / no run level folders named from rc0.d to rc6.d  To keep things simple there is a tool for removing / adding these links, hence removing or adding scripts to and from start up.  to remove apache2 simply type:   ``` sudo update-rc.d -f  apache2 remove ```   and all run level folders that have apache2 linked to them will the apache2 service removed |
|  | |  |  | | --- | --- | |  | chkconfig may also help - " chkconfig {service\_name} off " –  [MCR](http://askubuntu.com/users/64201/mcr "171 reputation") [Aug 1 '12 at 7:10](http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up#comment210111_170645) | |  | Doesn't work anymore: `The script you are attempting to invoke has been converted to an Upstart job, but lsb-header is not supported for Upstart jobs. (...)` –  [TomDogg](http://askubuntu.com/users/166013/tomdogg "161 reputation") [Apr 29 at 9:34](http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up#comment867795_170645) |  add a comment |

![apple-touch-icon.png](askubuntu-com--how-to-disable-apache2-server-from-auto-starting-upon-boot-u/49585dfae0bc51bcb37b84dac577ed3c.png)

## Did you find this question interesting? Try our newsletter

Sign up for our newsletter and get our top new questions delivered to your inbox ([see an example](http://stackexchange.com/newsletters/newsletter?site=askubuntu.com)).

|  |  |
| --- | --- |
| up vote down vote | you could simply disable it by:   ``` sudo update-rc.d apache2 disable ```   and then if you would like to enable it again:   ``` sudo update-rc.d apache2 enable ```   depending on the project i am working on, it is handy to have the service conveniently available, if i wish to re-enable it. |
|  | |  |  | | --- | --- | |  | `enable` gave me an error like `runlevel arguments (none) do not match LSB Default-Start values`, but `sudo update-rc.d apache2 defaults` appears to have re-enabled it successfully. –  [here](http://askubuntu.com/users/146390/here "209 reputation") [Jan 13 '14 at 3:58](http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up#comment519467_355102) | |  | +1, this should be the accepted answer. –  [jutky](http://askubuntu.com/users/12540/jutky "180 reputation") [Jan 19 '14 at 11:34](http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up#comment524209_355102) | |  | @here `sudo update-rc.d apache2 enable` played as expected for me –  [George Pligor](http://askubuntu.com/users/112680/george-pligor "108 reputation") [Feb 9 '14 at 15:12](http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up#comment539499_355102) | |  | On Ubuntu Trusty it tells me "The disable|enable API is not stable and might change in the future." –  [Tanner](http://askubuntu.com/users/203040/tanner "101 reputation") [Jun 10 '14 at 0:31](http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up#comment639962_355102) | |  | Doesn't work - `error: no runlevel symlinks to modify, aborting!`. However, apache2 is running and autostarts. –  [Daniel](http://askubuntu.com/users/228344/daniel "295 reputation") [Dec 14 '14 at 11:05](http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up#comment771274_355102) |  [show **1** more comment](http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up# "expand to show all comments on this post") |

|  |  |
| --- | --- |
| up vote down vote | This GUI is very functional and easy: <http://www.marzocca.net/linux/bum.html> |
|  | |  |  | | --- | --- | |  | Welcome to Ask Ubuntu! Whilst this may theoretically answer the question, [it would be preferable](http://meta.stackexchange.com/q/8259) to include the essential parts of the answer here, and provide the link for reference. –  [fossfreedom](http://askubuntu.com/users/14356/fossfreedom "110012 reputation") [Dec 17 '13 at 21:01](http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up#comment501859_392253) |  add a comment |

## Your Answer

### Sign up or [log in](http://askubuntu.com/users/login?returnurl=%2fquestions%2f170640%2fhow-to-disable-apache2-server-from-auto-starting-upon-boot-up%23new-answer)

Sign up using Google

Sign up using Facebook

Sign up using Stack Exchange

### Post as a guest

|  |
| --- |
| Name  Email |

[discard](http://askubuntu.com/questions/170640/how-to-disable-apache2-server-from-auto-starting-upon-boot-up#)

By posting your answer, you agree to the [privacy policy](http://stackexchange.com/legal/privacy-policy) and [terms of service](http://stackexchange.com/legal/terms-of-service).

## Not the answer you're looking for? Browse other questions tagged [apache2](http://askubuntu.com/questions/tagged/apache2 "show questions tagged 'apache2'") or [ask your own question](http://askubuntu.com/questions/ask).
