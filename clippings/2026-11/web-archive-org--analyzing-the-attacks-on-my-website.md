---
url: "https://web.archive.org/web/20200225120258id_/https://dev.to/pluralsight/analyzing-the-attacks-on-my-website-30jf"
captured_at: "2026-11-16T07:47:42+00:00"
title: "Analyzing the Attacks on my Website"
domain: "web-archive-org"
---

[![Pluralsight profile image](https://res.cloudinary.com/practicaldev/image/fetch/s--QJR4IPU5--/c_fill,f_auto,fl_progressive,h_50,q_auto,w_50/https://dev-to-uploads.s3.amazonaws.com/uploads/organization/profile_image/953/b41d3128-3536-43b5-9fe4-92393b3eea45.jpg) Pluralsight](https://web.archive.org/pluralsight)

### [twitter logo](http://twitter.com/JeremyCMorgan) [github logo](http://github.com/JeremyMorgan) Feb 8 _Updated on Feb 10, 2020_ ・5 min read

I was casually doing a security audit on my blog ([JeremyMorgan.com](http://bit.ly/JeremyMorganDotCom)) recently and decided to look a little deeper into my security logs. With a bit of Linux command line kung fu, some Golang, and Google sheets, I was able to get a pretty good idea of where the attacks are coming from.

To start, I'm using CentOS to host my site, so I checked out /var/log/secure. This log is where authentication logs are stored on my server.

This is what the log file looks like:

[![Analyzing attacks on my website](https://res.cloudinary.com/practicaldev/image/fetch/s--W4Bqr8vq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/za1ti2vgppyf4kffu2qy.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--W4Bqr8vq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/za1ti2vgppyf4kffu2qy.jpg)

and with **301,327** lines it's not likely I'm going to manually look around much. Let's automate this a bit.

## [](#getting-the-ip-address-of-attackers)Getting the IP Address of attackers

I wanted to extract the IP address of attackers from this file. That way I can block them.

I started to mess around with Linux commands until I came up with [this script](https://gist.github.com/JeremyMorgan/94af88899785ea725a55a382f3fd209b).

What it does is pretty simple, it's going to look for these strings:  

```
declare -a badstrings=("Failed password for invalid user"
                "input_userauth_request: invalid user"
                "pam_unix(sshd:auth): check pass; user unknown"
                "input_userauth_request: invalid user"
                "does not map back to the address"
                "pam_unix(sshd:auth): authentication failure"
                "input_userauth_request: invalid user"
                "reverse mapping checking getaddrinfo for"
                "input_userauth_request: invalid user"
                )
```

These are strings that identify logs of failed attacks. If they put in the wrong username or tried some other form of attack, it would have one of these strings.

So we loop through that list and search for these strings, then extract an IP address from the line the string exists in.  

```
cat /var/log/secure | grep "$i" | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" | awk '{print $0}' | sort | uniq >> "temp.txt"
```

It then dumps the IP into a **temp.txt** file. It will do this for all of the messages I have in my "badstrings" list.

That text file had a ton of duplicates in it, so I removed the duplicates and put only the unique IPs into a file:  

```
# grab unique ips from temp and put them in a file
cat "temp.txt" | sort | uniq > "badguyips.txt"
# remove the temp file
rm "temp.txt"
```

Cool, now I have a list of IP addresses ready to go.

[![Analyzing attacks on my website](https://res.cloudinary.com/practicaldev/image/fetch/s--lwePz_-f--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/4qcv7c3livboz06dbfpz.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--lwePz_-f--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/4qcv7c3livboz06dbfpz.jpg)

Yikes, I have **1,141** IP addresses here.

## [](#blocking-them)Blocking Them

Now I want to block these IP addresses. Since I'm running iptables, I can just drop them with this simple script:  

```
#!/bin/bash
input="badguyips.txt"
while IFS= read -r line
do
  iptables -A INPUT -s $line -j DROP
done < "$input"

service iptables save
```

Cool. Now the attackers blocked from my server.

Then I got curious. Where the heck are these attacks coming from?

## [](#getting-their-location-data)Getting their Location Data

Since I have a list of IP addresses, I thought I'd run them against a database like [Maxmind](https://www.maxmind.com/en/home) to find some location information. So I did just that.

I wrote this [Golang program called "find the bad guys"](https://github.com/JeremyMorgan/FindTheBadGuys) that would go through the text file of IP addresses, and look up their location information, then write it to a series of text files.

I wrote out locations based on:

*   Continent
*   Countries
*   Cities
*   Subdivisions of Cities

I wanted to see where the attacks are coming from and share that information. so I ran the program I built, and now have some helpful lists of location information:

[![Analyzing attacks on my website](https://res.cloudinary.com/practicaldev/image/fetch/s--HMsBwEc---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/r4yl9r8o9t357feaylmb.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--HMsBwEc---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/r4yl9r8o9t357feaylmb.jpg)

## [](#continents)Continents

So now I want to take a look at continents.txt.

[![Analyzing attacks on my website](https://res.cloudinary.com/practicaldev/image/fetch/s--KInKiLnV--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/w7oa8f9noy98mcs8nrx8.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--KInKiLnV--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/w7oa8f9noy98mcs8nrx8.jpg)

Well, that's going to be a problem, there are some duplicates.

I can run a quick command and get unique values:  

```
cat continents | sort | uniq
```

The results should come as no surprise if you've ever looked at a globe:

[![Analyzing attacks on my website](https://res.cloudinary.com/practicaldev/image/fetch/s--NHVydH_J--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/e8ra8lsu5jeyrov80hr6.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--NHVydH_J--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/e8ra8lsu5jeyrov80hr6.jpg)

But I want to see how many attacks from each continent. So I call on my old friend uniq for that:  

```
awk -F '\n' '{print $0}' continents.txt | sort | uniq -c
```

[![Analyzing attacks on my website](https://res.cloudinary.com/practicaldev/image/fetch/s--yE_CRf3J--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/1j63u04ex131x849x5jz.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--yE_CRf3J--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/1j63u04ex131x849x5jz.jpg)

Pretty sweet, right? So I'll remove the leading spaces, insert a comma after the count and drop it into a text file.  

```
awk -F '\n' '{print $0}' continents.txt | sort | uniq -c | awk '{$1=$1};1' | sed -r 's/\s+/,/'  > contintent-totals.txt
```

[![Analyzing attacks on my website](https://res.cloudinary.com/practicaldev/image/fetch/s--wGWbbfAD--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/4yc2g7i35kx9t9dnceiy.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--wGWbbfAD--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/4yc2g7i35kx9t9dnceiy.jpg)

Now I can drop it into Google sheets.

[![Analyzing attacks on my website](https://res.cloudinary.com/practicaldev/image/fetch/s--Xn9H8i4S--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/w18dwindj8mptfnra7j2.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--Xn9H8i4S--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/w18dwindj8mptfnra7j2.jpg)

and get this nice chart:

[![Analyzing attacks on my website](https://res.cloudinary.com/practicaldev/image/fetch/s--Jw9XOS-t--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/yi9twfbtsktgl2x9eddq.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--Jw9XOS-t--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/yi9twfbtsktgl2x9eddq.jpg)

This is the process I repeat for the other locations (country, city, subdivision), so I won't repeat it. So here are my results:

## [](#countries)Countries

[![Analyzing attacks on my website](https://res.cloudinary.com/practicaldev/image/fetch/s--lhwx1m6O--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/jnjtsnsn3tcf5rrzjqzk.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--lhwx1m6O--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/jnjtsnsn3tcf5rrzjqzk.jpg)

Here are the top 10 countries attackers are coming from:

*   China (304)
*   United States (138)
*   France (95)
*   India (46)
*   Singapore (43)
*   South Korea (38)
*   Germany (37)
*   Russia (37)
*   Brazil (35)
*   United Kingdom (29)

## [](#cities)Cities

[![Analyzing attacks on my website](https://res.cloudinary.com/practicaldev/image/fetch/s--dWDFtvan--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/e1q8xz4zu1so9w50mff9.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--dWDFtvan--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/e1q8xz4zu1so9w50mff9.jpg)

Attacks per city are a little more aggregated.

*   Beijing (57)
*   Shanghai (53)
*   Hefei (25)
*   Amsterdam (21)
*   Bengaluru (16)
*   London (14)
*   Xinpu (14)
*   Clifton (10)
*   North Bergen (9)

But still pretty interesting.

## [](#subdivisions)Subdivisions

[![Analyzing attacks on my website](https://res.cloudinary.com/practicaldev/image/fetch/s--SK8CjQSD--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/018bt087kui3oetwfr3e.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--SK8CjQSD--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/018bt087kui3oetwfr3e.jpg)

This one is aggregated even more. But it drills down a bit more. Here are the top 10 subdivisions attackers are coming from:

*   Beijing (145)
*   Shanghai (61)
*   Anhui (26)
*   England (22)
*   Jiangsu (22)
*   New Jersey (22)
*   North Holland (22)
*   California (18)
*   Sao Paulo (18)
*   Karnataka (16)

### [](#conclusion)Conclusion

Great things always come from curiosity. I'm curious about what other kinds of patterns and data I can extract from this, so I'm going to keep experimenting and playing with it.

If you decide you want to do this for your website, try it these steps, and [Let me know](http://bit.ly/JeremyCMorgan) if you need any help with it.

 [![twitter logo](https://practicaldev-herokuapp-com.freetls.fastly.net/assets/twitter-99c56e7c338b4d5c17d78f658882ddf18b0bbde5b3f42f84e7964689e7e8fb15.svg)](https://twitter.com/intent/tweet?text=%22Analyzing%20the%20Attacks%20on%20my%20Website%22%20by%20@JeremyCMorgan%20%23DEVcommunity%20https://dev.to/pluralsight/analyzing-the-attacks-on-my-website-30jf)[DISCUSS (20)](#comments)

![Copy to Clipboard](https://practicaldev-herokuapp-com.freetls.fastly.net/assets/content-copy-d564d822fccd292272dc5db1b788fe414691a408b10ccf1b34dfc366bd19eeeb.svg)

**👋 Hey [dev.to](https://dev.to/) reader.**

Do you prefer **sans serif** over **serif**?

You can change your font preferences in the "misc" section of **[your settings](https://web.archive.org/enter)**. ❤️

[![jeremycmorgan profile](https://res.cloudinary.com/practicaldev/image/fetch/s--XibKObL0--/c_fill,f_auto,fl_progressive,h_180,q_auto,w_180/https://dev-to-uploads.s3.amazonaws.com/uploads/user/profile_image/48220/509bdb41-2b32-4513-83dc-3a0c7276d6f2.jpg)](https://web.archive.org/jeremycmorgan)

#### [Jeremy Morgan](https://web.archive.org/jeremycmorgan)

Silicon Forest Developer/hacker. I write about .NET, DevOps, and Linux mostly. Once held the world record for being the youngest person alive.

With our technology skills platform, companies can upskill teams and increase engineering impact.

[![Pluralsight](https://res.cloudinary.com/practicaldev/image/fetch/s--THBff8wG--/c_fill,f_auto,fl_progressive,h_120,q_auto,w_120/https://dev-to-uploads.s3.amazonaws.com/uploads/organization/profile_image/953/b41d3128-3536-43b5-9fe4-92393b3eea45.jpg)](https://web.archive.org/pluralsight)
