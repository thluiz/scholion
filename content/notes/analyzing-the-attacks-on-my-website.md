---
title: "Analyzing the Attacks on my Website"
date: '2020-02-22T12:11:42+00:00'
category: webclip
summary: 'The author audits a CentOS server log, extracts failed login IPs, blocks them with iptables, and uses MaxMind plus Go to map attack sources by continent, country, city, and subdivision.'
tags: ["linux", "security-logs", "iptables", "geolocation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Analyzing the Attacks on my Website"
    url: "https://web.archive.org/web/20200225120258id_/https://dev.to/pluralsight/analyzing-the-attacks-on-my-website-30jf"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--analyzing-the-attacks-on-my-website.md"
    kind: repo
---

The author reviews authentication logs on a CentOS-hosted blog and uses shell commands plus a Go program to pull attacker IP addresses from repeated failed-login messages. After deduplicating the addresses, the list is used to block those IPs with iptables.

He then looks up each IP with MaxMind and exports the results by continent, country, city, and subdivision. The counts show attacks coming from multiple regions, with China, the United States, and France among the top countries.

## Reading notes

- The author checked /var/log/secure on a CentOS server because it stores authentication logs.
- He searched for several failure strings that indicate unsuccessful attack attempts.
- The script extracted IP addresses from matching log lines and saved them to temp.txt.
- Duplicate IPs were removed and written to badguyips.txt.
- A bash loop added each IP from badguyips.txt to iptables with a DROP rule.
- He used MaxMind to find location data for the IP list.
- A Go program called "find the bad guys" wrote location results into text files.
- The locations were grouped by continent, country, city, and subdivision.
- The continent, country, city, and subdivision files were processed with sort and uniq.
- The top countries listed are China, the United States, France, India, Singapore, South Korea, Germany, Russia, Brazil, and the United Kingdom.
- The top cities listed include Beijing, Shanghai, Hefei, Amsterdam, Bengaluru, London, Xinpu, Clifton, and North Bergen.
- The top subdivisions listed include Beijing, Shanghai, Anhui, England, Jiangsu, New Jersey, North Holland, California, Sao Paulo, and Karnataka.
- The author says curiosity led him to keep experimenting with the data.
