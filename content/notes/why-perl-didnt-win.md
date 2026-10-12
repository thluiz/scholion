---
title: "Why Perl Didn't Win"
date: '2014-07-07T14:18:22-03:00'
category: webclip
summary: 'The essay argues that Perl lost not because it was useless, but because CGI was costly, PHP was easier to deploy, CPAN’s edge faded, and Perl 6 split attention without delivering a clear future.'
tags: ["perl", "programming-languages", "web-development", "open-source-ecosystems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why Perl Didn't Win | Outspeaking"
    url: "http://outspeaking.com/words-of-technology/why-perl-didnt-win.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-07/outspeaking-com--why-perl-didnt-win.md"
    kind: repo
---

The essay says Perl succeeded early because it fit Unix systems, handled strings well, and had a large library ecosystem. It was practical for CGI-era web work, where HTML, HTTP, and server-side scripts were all handled as strings.

It argues that Perl lost ground because CGI was expensive and hard to configure, PHP was easier to deploy for simple web pages, CPAN’s advantage weakened as ecosystems aged, and the Perl 6 split made the language’s future unclear. The result was a decline in attractiveness for new projects.

## Reading notes

- Perl won early through momentum, ubiquity on Unix, and usefulness for system administration and string processing.
- CGI made web programs possible, but launching a new process for each request became costly and awkward at scale.
- mod_perl improved speed and flexibility, but it was hard to install and introduced shared-memory risks.
- mod_php was easier to deploy, so it became the default answer for dynamic web pages.
- CPAN was a major strength, but library ecosystems depend on active growth and on the needs of current projects.
- Older ecosystems become less attractive when they focus on maintaining existing code instead of supporting new work.
- The Perl 6 project split attention in 2000 and never gave adopters a clear migration path or a clear timeline.
- The lack of a defined future reduced Perl’s appeal for new projects even while Perl 5 remained in use.
- The essay concludes that languages win by being compelling for new things, not only by being technically adequate.
