---
url: "https://brajeshwar.com/2024/i-block-ads/"
captured_at: "2026-09-24T22:38:29+01:00"
title: "I Block Ads"
domain: "brajeshwar-com"
---

Thu, Sep 19, 2024

Open in

[](https://chatgpt.com/?q=Read%20https%3A%2F%2Fbrajeshwar.com%2F2024%2Fi-block-ads.md%20%E2%80%94%20I%20have%20questions%20about%20this%20post%20%28%22I%20Block%20Ads%22%29. "Open in OpenAI")[](https://claude.ai/new?q=Read%20https%3A%2F%2Fbrajeshwar.com%2F2024%2Fi-block-ads.md%20%E2%80%94%20I%20have%20questions%20about%20this%20post%20%28%22I%20Block%20Ads%22%29. "Open in Claude")[](https://brajeshwar.com/2024/i-block-ads.md "View as Markdown")

Growing up during the TV boom of the 1980s and 90s, I loved Advertisements.[1](#fn:Advertising) That was actually how one learned about new things. Advertisements (ads) are intended to let people know what they didn’t know and to reiterate if they might forget.

Recently, after I upgraded to [macOS Sequoia (version 15)](https://en.wikipedia.org/wiki/MacOS_Sequoia), I realized that my current AdBlocker,[2](#fn:Adblocking) [AdGuard](https://adguard.com/), was not working in Safari. This was [due to a conflict](https://github.com/AdguardTeam/CoreLibs/issues/1914) between Adguard and Apple [iCloud Private Relay](https://support.apple.com/en-us/102602).

![Safari > Privacy > Hide IP Address](https://brajeshwar.com/static/2024/safari-privacy-hide-ip-address.webp)

For now, I fixed it by turning the Private Relay `OFF` while waiting for Adguard/Apple to release a patch. In Safari, go to _Settings > Privacy > Turn off “Hide IP Address”_. Mine worked after I disabled it at the OS level too. Go to _System Settings > Apple Account > iCloud > Private Relay (Off)_.

In that short window of a few hours, I realized that the Internet is an unforgiving place to browse without an AdBlocker. As I was on my usual chore of collecting and sharing `interesting`, `weird`, and `strange` finds for [Hacker News](https://brajeshwar.com/2023/hacker-news/), I was stunned to see how unusable the browsing experience had become.

To all the friends, readers, and visitors of Hacker News, I’d like to extend my sincere apologies. I do realize that the majority of visitors there would likely be using some sort of ad blocker, and I’m a tad relieved about that. For everyone else, please find a solution that suits your needs.

For instance, my wife gets cranky without ads. Some time back, she thought the Internet was broken, “As soon as I enter our home, none of the Ads show up. I had to go outside on Mobile data or turn off Wi-Fi at home to see my ads.” She is now on a separate VLAN[3](#fn:VLAN) with all her fully loaded Internet traffic, away from our home network. She is prohibited from using her devices to interact with most devices inside our home network. ;-)

I pay for quite a few of the websites I visit and use, and most of them are just to remove the ads. I will do my part where I can and where I can afford to buy my way out of Ads. Unfortunately, that is a small portion; everywhere else is littered with ads.

The digital world has skewed intentions to such a degree that ads are now **targeted, trained, and tailored** to the point that if you divert your attention a few fractions elsewhere, they will **recalibrate and retarget** to get back to you to think and believe in what they intend you to.

Of course, I don’t hate ads. It is a legitimate business model. I’m just not too keen on the overdone ads that are everywhere and in everything. For reference, Google generated over $224 billion in 2022 and $237.86 billion in 2023 from ads.

![Ads Ads Ads](https://brajeshwar.com/static/2024/ads-ads-ads.webp)

These days, it is impossible to read/view the actual content of most websites—they are filled with the landmines of ads. There is no way to have a normal, decent web experience without an AdBlocker or a few of them. Someone rightly said, “Content” is an advertising term for whatever fills the space between all the ads.

Even the USA’s agency, [FBI suggest using Adblockers](https://www.ic3.gov/Media/Y2022/PSA221221). The reasoning, in this case, is to avoid falling prey to cybercriminals impersonating brands through search engine advertising services to defraud users. ([archive](https://archive.is/3Mioj))

> The best minds of my generation are thinking about how to make people click ads. — [Jeff Hammerbacher](https://en.wikipedia.org/wiki/Jeff_Hammerbacher)

I block ads in the browser (client) and at the DNS level. The combination of these two is effective enough for now. Here are a few tools to get you started;

![Google’s Newspaper Ad from 1999](https://brajeshwar.com/static/2024/google-newspaper-ad-1999.jpg)

## DNS Resolvers with AdBlockers

These tools help you resolve your internet queries by routing them through their servers worldwide. One feature of these services is ad blocking at the DNS level. You can use this and other client-side Ad blockers for a more effective ad-blocking setup.

*   [Mullvad DNS over HTTPS and DNS over TLS](https://mullvad.net/en/help/dns-over-https-and-dns-over-tls)
*   [AdGuard DNS](https://adguard-dns.io/) / [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome) controls all web traffic on your devices, blocks ads, trackers, and malicious domains.
*   [NextDNS](https://nextdns.io/) protects you from all kinds of security threats, blocks ads and trackers on websites and in apps, and provides a safe and supervised Internet for kids — on all devices and on all networks.
*   [Control D](https://controld.com/) is a customizable DNS service that blocks threats, unwanted content and ads.
*   [Pi-Hole](https://pi-hole.net/) network-wide ad blocking via your own Linux hardware. [I started with this](https://brajeshwar.com/2019/pi-hole-blocking-ads-at-home/).

## Ad-Blockers

*   [uBlock Origin](https://ublockorigin.com/) - Free, open-source ad content blocker.
*   [AdGuard](https://adguard.com/) - Surf the Web ad-free and safely.

## Others

*   [AdBlock Tester](https://adblock-tester.com/) tests your Browser’s AdBlocking effectiveness.
*   [How I Experience the Web Today](https://how-i-experience-web-today.com/) takes you on an adventure of how a normal persona experiences the Web today.

1.  [Advertising](https://en.wikipedia.org/wiki/Advertising) is the practice and techniques employed to bring attention to a product or service. Advertising aims to present a product or service in terms of utility, advantages and qualities of interest to consumers. It is typically used to promote a specific good or service, but there are a wide range of uses, the most common being commercial advertisement. [↩](#fnref:Advertising)
    
2.  [Ad blocking](https://en.wikipedia.org/wiki/Ad_blocking) or ad filtering is a software capability for blocking or altering online advertising in a web browser, an application or a network. This may be done using browser extensions or other methods. [↩](#fnref:Adblocking)
    
3.  A [VLAN](https://en.wikipedia.org/wiki/VLAN) behaves like a virtual switch or network link that can share the same physical structure with other VLANs while staying logically separate from them. VLANs can keep network applications separate despite being connected to the same physical network, and without requiring multiple sets of cabling and networking devices to be deployed. [↩](#fnref:VLAN)
