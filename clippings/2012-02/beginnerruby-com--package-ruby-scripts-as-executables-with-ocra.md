---
url: "http://www.beginnerruby.com/ruby-executables/package-ruby-scripts-as-executables-with-ocra/"
captured_at: "2012-02-13T20:40:44-03:00"
title: "Package Ruby Scripts as Executables with Ocra | Beginner Ruby"
domain: "beginnerruby-com"
---

## Package Ruby Scripts as Executables with Ocra

I recently stumbled across a very interesting Ruby Gem, it’s called Ocra. Ocra allows a Ruby programmer to package a Ruby Script [and ALL DEPENDENCIES, i.e. Gems] as a Windows .exe file.

All you have to do is:  
`gem install ocra`  
Then you have the Ocra gem which will allow you to create executables using this command format:  
`ocra [-options] script.rb`  
Options are not required, really all you need is this:  
`ocra script.rb`

When you run this command, then Ocra runs your program while building it — in order to learn what dependencies the script has and it will need to include in the .exe environment. Then it packages this environment, into a nice tidy .exe file which you works on other Windows computers automatically — THEY DON’T EVEN NEED TO HAVE RUBY INSTALLED!! HOW AWESOME IS THAT!?!

I recently posted about how I created a [**domain name availability script**](http://www.beginnerruby.com/ruby-scripts/making-a-quick-domain-name-availability-checker-with-ruby/)  which I named [**Quickcheck**](http://www.beginnerruby.com/ruby-scripts/making-a-quick-domain-name-availability-checker-with-ruby/) . Well, when I found the Ocra Gem I decided it was time to create an executable.

I tried a few commands and was having some dependency issues, you see Ocra wasn’t including the Whois gem I needed it too in order for my Quickcheck script to work. Eventually I learned the correct command to make sure the whois gem got attached:  
`ocra quickcheck.rb --gem-full`

This makes Ocra include EVERYTHING. It made my script go from a **2kb** ruby script to **1,493kb** .exe but hey that sure beats only being able to run the script on machines w/ Ruby installed.

Ocra worked this time, and I have a nice little Quickcheck.exe program that I can use to check domain name availability.

Here is my **Quickcheck.exe** program–  
[**http://beginnerruby.com/downloads/quickcheck.exe**](http://beginnerruby.com/downloads/quickcheck.exe)

I do have one complaint, the .exe loads pretty slow. It takes like a solid 15-20 seconds of black prompt screen before the words finally appear. Some will say this is what I get for making an executable this way, and with Ruby, but I am not sure. Maybe I can compile with Ocra with different flags in order to trim down the .exe? I am not sure. Hopefully not all .exe’s made with Ocra lag like this. I think it’s just because I included the whois gem and its pretty large. I will need to experiment and see what I can do to slim down the loading time in the beginning of the executable.

In any event, I am happy with the executable I created with Ocra. I am very glad to have come across the Ocra Ruby Gem. I look forward to making many many executables with Ocra moving forward.

Here is the **official Ocra web site: <http://ocra.rubyforge.org/>**
