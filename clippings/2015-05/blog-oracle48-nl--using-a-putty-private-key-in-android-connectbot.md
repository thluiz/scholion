---
url: "http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/"
captured_at: "2015-05-01T14:16:41-03:00"
title: "Using a Putty private key in Android ConnectBot"
domain: "blog-oracle48-nl"
---

# [Using a Putty private key in Android ConnectBot](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/)

I have been trying to import a **private key** into **ConnectBot** for **Android**.  
The key I’m using is working fine when using [**Putty**](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html "Putty"), but does not work for ConnectBot.

To make it work for ConnectBot, you need to have a **OpenSSH** version of this file.  
Luckily one can also use [PuTTYgen](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html "PuTTYgen") to create an [OpenSSH](http://en.wikipedia.org/wiki/OpenSSH "OpenSSH") key.

## **Puttygen**

In Puttygen, do the following:

1. Load the private key [File] -> [Load Private Key] (\*.ppk)
2. Enter passphrase if applicable
3. Goto [Conversions] -> [Export OpenSSH key] and save

## Android

Now find a way to get this OpenSSH key to your Android /sdcard (root) folder.

## **Connectbot**

In Connectbot, do the following:

1. [Menu] -> [Manage Pubkeys]
2. [Menu] -> [Import]
3. Choose the OpenSSH key from /sdcard
4. Click the red lock icon to load the key into memory
5. Enter passphrase/password if applicable
6. (Disconnect current session)
7. Connect!

You don’t assign a private key to a connection, but ConnectBot will just try any loaded key instead.

Cheers!

### 17 Comments on “Using a Putty private key in Android ConnectBot”

1. new2openssh
     
   [March 22nd, 2011 at 05:39](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-5042) 

   Please help I’m literally pulling my hair out and keep on getting timed out. I don’t have a password. Putty connecting through lan works ok with the priv key but when connecting with connectbot keeps timing out. I can ping both my dyndns name and ip associated with it currently and it’s ok. I know that you don’t need to open ports if you do the tunnelling.  
   Don’t know what else to do.

   Thanks.
2. Ian Hoogeboom
     
   [April 8th, 2011 at 12:29](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-5705) 

   Are you sure you access the machine through lan (wi-fi) when connecting with connectbot? Aren’t you using a data connection set up by your device using the data connection from your provider?
3. [5169.info](http://5169.info/)
     
   [July 3rd, 2011 at 01:11](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-8880) 

   Is connectbot only work with lan/wifi ?
4. Ian Hoogeboom
     
   [July 3rd, 2011 at 07:26](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-8886) 

   It also works when connected through a mobile operator. I have it working with T-Mobile Netherlands.

   When you use your router’s outside/WAN ip address as ‘host’ and a ‘port’ which are both forwarded/redirected (called [NAT](http://en.wikipedia.org/wiki/Network_address_translation)) on your router to the machine you have ssh running on, you should be able to connect!
5. voytek
     
   [August 8th, 2011 at 03:59](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-10149) 

   thanks, excellent guide
6. noname
     
   [August 17th, 2011 at 21:12](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-10584) 

   Good. Thank you!
7. rsturk
     
   [October 1st, 2011 at 22:17](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-11959) 

   Thanks for posting this information! I wouldn’t have known to generate the OpenSSH key otherwise.
8. xicobandito
     
   [August 9th, 2012 at 18:15](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-29632) 

   Thank you. Worked like a charm.
9. pimptastic
     
   [October 1st, 2012 at 06:34](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-32977) 

   this worked perfectly. Thank you for your assistance.
10. Frapi
      
    [November 15th, 2012 at 11:50](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-35620) 

    Thanks a lot !  
    I did not notice the point of the different key format between putty and open ssh
11. Grisbouille
      
    [December 29th, 2012 at 15:28](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-36273) 

    Great guide, thanks for that explanation.  
    However, what way could I devise if I don’t have access to a windows pc (I.e. can’t run puttygen)??  
    I’ve been on the lookout for an android equiv. but nothing so far… Any idea how to bypass the absence of windows?
12. Ian Hoogeboom
      
    [December 29th, 2012 at 17:24](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-36274) 

    Hi, on Linux you can use “ssh-keygen -i -f input\_keyfile > output\_keyfile” to generate an OpenSSH keyfile.
13. [klipse](http://www.pinblasterapp.com/)
      
    [April 18th, 2013 at 17:38](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-37575) 

    Well done! This has really solved my needs on the fly. I converted my putty key and it works like a charm. Thanks!
14. Subhash Surampudi
      
    [May 6th, 2013 at 13:56](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-37861) 

    Thank you. This was very helpful.
15. Sardog
      
    [March 6th, 2014 at 06:27](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-39306) 

    Thanks, it worked just like you explained. I used Openbox by the way to move my key quickly and then deleted the key off of Openbox. I know, I know, maybe not the most secure way but at least I could do it all remotely with my laptop and and tablet in hand, while watching TV.
16. Yuengling
      
    [July 4th, 2014 at 16:29](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-73996) 

    Hi. Your instructions say “Now find a way to get this OpenSSH key to your Android /sdcard (root) folder.” – can you kindly explain how to do this? I have been unable to locate any helpful instructions.
17. Ian Hoogeboom
      
    [July 6th, 2014 at 11:13](http://blog.oracle48.nl/using-a-putty-private-key-in-android-connectbot/#comment-74807) 

    Hi. You can do this is a lot of different ways. You can mail the file to yourself and open the mail on your phone and save it on the SDcard (I use ES File Explorer to move files around on my phone); you can take the SDcard out and put it into your PC, copy it on the SD card and place the SDcard back in the phone; you can connect the phone to your PC with USB and save the file in the SDcard folder… etc… a lot of different ways to do this.  
    Regards, Ian.
