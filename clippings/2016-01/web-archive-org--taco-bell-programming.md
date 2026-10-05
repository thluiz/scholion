---
url: "http://web.archive.org/web/20101202135616/http://teddziuba.com/2010/10/taco-bell-programming.html"
captured_at: "2016-01-04T13:32:30-03:00"
title: "Taco Bell Programming"
domain: "web-archive-org"
---

# Taco Bell Programming

by Ted Dziuba Thursday October 21 2010

![83a61d6ec7e1153f5c991d9c54eb321a.jpg](web-archive-org--taco-bell-programming/83a61d6ec7e1153f5c991d9c54eb321a.jpg)

Every item on the menu at Taco Bell is just a different configuration of roughly eight ingredients. With this simple periodic table of meat and produce, the company pulled down $1.9 billion last year.

The more I write code and design systems, the more I understand that many times, you can achieve the desired functionality simply with clever reconfigurations of the basic Unix tool set. After all, *functionality is an asset, but code is a liability*. This is the opposite of a trend of nonsense called DevOps, where system administrators start writing unit tests and other things to help the developers warm up to them - Taco Bell Programming is about developers knowing enough about Ops (and Unix in general) so that they don't overthink things, and arrive at simple, scalable solutions.

Here's a concrete example: suppose you have millions of web pages that you want to download and save to disk for later processing. How do you do it? The cool-kids answer is to write a distributed crawler in Clojure and run it on EC2, handing out jobs with a message queue like SQS or ZeroMQ.

The Taco Bell answer? `xargs` and `wget`. In the rare case that you saturate the network connection, add some `split` and `rsync`. A "distributed crawler" is really only like 10 lines of shell script.

Moving on, once you have these millions of pages (or even tens of millions), how do you process them? Surely, Hadoop MapReduce is necessary, after all, that's what Google uses to parse the web, right?

Pfft, fuck that noise:

> `find crawl_dir/ -type f -print0 | xargs -n1 -0 -P32 ./process`

32 concurrent parallel parsing processes and zero bullshit to manage. Requirement satisfied.

Every time you write code or introduce third-party services, you are introducing the possibility of failure into your system. I have far more faith in `xargs` than I do in Hadoop. Hell, I trust `xargs` more than I trust myself to write a simple multithreaded processor. I trust syslog to handle asynchronous message recording far more than I trust a message queue service.

Taco Bell programming is one of the steps on the path to Unix Zen. This is a path that I am personally just beginning, but it's already starting to pay dividends. To really get into it, you need to throw away a lot of your ideas about how systems are designed: I made most of a SOAP server using static files and Apache's `mod_rewrite`. I could have done the whole thing Taco Bell style if I had only manned up and broken out `sed`, but I pussied out and wrote some Python.

If you don't want to think of it from a Zen perspective, be capitalist: you are writing software to put food on the table. You can minimize risk by using the well-proven tool set, or you can step into the land of the unknown. It may not get you invited to speak at conferences, but it will get the job done, and help keep your pager from going off at night.
