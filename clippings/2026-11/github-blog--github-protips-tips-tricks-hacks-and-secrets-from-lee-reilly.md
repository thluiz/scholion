---
url: "https://github.blog/2020-04-09-github-protips-tips-tricks-hacks-and-secrets-from-lee-reilly"
captured_at: "2026-11-16T03:12:56+00:00"
title: "GitHub Protips: Tips, tricks, hacks, and secrets from Lee Reilly"
domain: "github-blog"
---

_This is the second in a series of posts featuring protips from GitHubbers. This post highlights some great browser extensions, URL hacks, keyboard shortcuts, plus a few dad jokes._

* * *

I’ve been using GitHub as an engineering, business development, and marketing manager for over 10 years now—quite the career trajectory! Along the way, I’ve picked up a few tricks to manage my notifications, quickly locate content and create pull requests, push markdown to its limits, and personalize my experience with some third party extensions. I’m sharing a few of my favorites, and hopefully there’s something new and helpful for you.

## [1\. Fuzzy file finder ![🔎](https://s.w.org/images/core/emoji/17.0.2/svg/1f50e.svg)](#1-fuzzy-file-finder-%f0%9f%94%8e) 

I think I was working at GitHub for over a year before I discovered that we had a [fuzzy file finder](https://github.blog/2011-02-10-introducing-the-file-finder/). Press `t` in any repository to access it and start typing the name of the file you want to find. I used to find it invaluable jumping into new Rails projects and quickly looking for `schema.rb` to get a feel for the app.

![](https://i0.wp.com/user-images.githubusercontent.com/121322/78818953-5105be00-798a-11ea-9f48-5626b0f7cb58.gif?ssl=1)

## [2\. Browse files and directories with ease](#2-browse-files-and-directories-with-ease)

Speaking of searching for files, this great browser extension called [Octotree](https://github.com/ovity/octotree) helps you navigate directories, and open files with a familiar tree-like structure.

[![](https://i0.wp.com/user-images.githubusercontent.com/121322/78818701-ee142700-7989-11ea-9297-c3cf4e88f891.gif?ssl=1)](https://github.com/ovity/octotree)

**Bonus points:** It works with GitHub Enterprise ![🙌](https://s.w.org/images/core/emoji/17.0.2/svg/1f64c.svg)

**Fun fact:** I [reached out to the author about supporting GitHub Enterprise a few years ago](https://github.com/ovity/octotree/pull/47#issuecomment-43431767). If you’re building a browser extension for GitHub, and want to make sure it works for GitHub Enterprise, you can get a developer license by joining the [GitHub Developer Program](https://developer.github.com/program/).

## [3\. Be alerted to new notifications](#3-be-alerted-to-new-notifications)

On the topic of browser extensions, this [project](https://github.com/sindresorhus/notifier-for-github) from [@sindresorhus](https://github.com/sindresorhus) tells you exactly how many GitHub notifications are waiting with an unobtrusive icon on your toolbar. You can enable Desktop notifications too if that’s your jam.

![](https://i0.wp.com/user-images.githubusercontent.com/121322/78306110-73fe2100-74f7-11ea-8a54-1ba3d0a8db61.png?ssl=1)

It also works with GitHub Enterprise. All you have to do is change the API endpoint to match your instance’s URL (for example, `https://api.github.cyberdynesystems.com`).

## [4\. Make your @mentions stand out ![📝](https://s.w.org/images/core/emoji/17.0.2/svg/1f4dd.svg)](#4-make-your-mentions-stand-out-%f0%9f%93%9d) 

No matter how many elaborate email or notification filters you set up, there’s always one that slips through the cracks. [Mention Highlighter](https://github.com/benbalter/github-mention-highlighter), created by my buddy [@benbalter](https://github.com/benbalter), highlights all references to my name and wow, do they jump out! Even in a wall of text or when I’m quickly skimming comments, I’m able to see any mentions directed to me.

![](https://i0.wp.com/user-images.githubusercontent.com/121322/78305868-d9054700-74f6-11ea-863a-02f0b02a718c.png?ssl=1)

## [5\. Linking to code snippets](#5-linking-to-code-snippets)

This isn’t so much of a secret, but it’s definitely not known by everyone, and occasionally blows minds. You can link to specific lines of code by clicking the line number when you’re viewing a file. By default, the line number (for example, `#L1337`) is appended to the URL, which will always take you directly to that line.

If that file is edited, deleted, or renamed, unfortunately the link will no longer work as expected. You can press `y` or  click `Copy permalink` to generate the canonical URL that will always work.

![](https://github.blog/wp-content/uploads/2020/04/Screen-Shot-2020-04-08-at-9.32.56-PM.png?resize=1024%2C310)

You can also link to a line number range by holding down SHIFT and selecting the starting and ending lines.

**Added bonus:** If you add a code snippet link in a GitHub comment, a nice visualization of the code appears.

![](https://i0.wp.com/user-images.githubusercontent.com/121322/78825122-451ef980-7994-11ea-808b-628620714936.png?ssl=1)

I recall that this feature was originally [built by a few interns several years ago](https://github.blog/2017-08-15-introducing-embedded-code-snippets/). If you like hacking on fun stuff like this, consider [applying to our internship program](https://internships.github.com/)!

## [6\. Must-have Markdown formatting tips](#6-must-have-markdown-formatting-tips)

[GitHub Flavored Markdown](https://github.github.com/gfm/) is great for vanilla formatting of text and basic tables, but sometimes you need to get creative to make it do what you want.

### [Keyboard tags](#keyboard-tags)

You can use `<kbd>` tags to make text appear like a button, which is slightly different from regular backticked text. It’s perfect for documenting things like keyboard shortcuts or game controls in your READMEs/wikis.

```
Press <kbd>W</kbd> to go up, and <kbd>A</kbd> to go down.
If you can find the <kbd>ESC</kbd>, pressing that will fire missiles 
```

![](https://i0.wp.com/user-images.githubusercontent.com/121322/78515760-e7a86400-776b-11ea-8a19-d830b7b786a3.png?ssl=1)

### [Visualizing hex codes](#visualizing-hex-codes)

Placing hex colors in backticks renders a tile in that color. I think it’s totally **hex**cellent!

```
GitHub contribution graph colors: `#C6E48B` `#7AC96F` `#249A3C` `#196127`
```

![](https://github.blog/wp-content/uploads/2020/04/Screen-Shot-2020-04-08-at-9.35.53-PM.png?resize=1024%2C149)

### [Visualizing diffs ![🧡](https://s.w.org/images/core/emoji/17.0.2/svg/1f9e1.svg)![💚](https://s.w.org/images/core/emoji/17.0.2/svg/1f49a.svg)](#visualizing-diffs-%f0%9f%a7%a1%f0%9f%92%9a) 

You can visualize a diff using backticks and `diff` which highlights lines red or green as appropriate.

````
```diff
10 PRINT “BASIC IS COOL”
- 20 GOTO 11
+ 20 GOTO 10
```
````

![](https://i0.wp.com/user-images.githubusercontent.com/121322/78515746-dcedcf00-776b-11ea-8804-accb3834dac7.png?ssl=1)

In fact, if you add the language after the opening three backticks, the code is [syntax highlighted](https://help.github.com/en/github/writing-on-github/creating-and-highlighting-code-blocks#syntax-highlighting) accordingly.

### [The devil’s in the details](#the-devils-in-the-details)

Adding lengthy error logs or verbose program output to an issue can be helpful in resolving a bug, but if it takes up _pages_ of vertical space, consider using the `<details>` and `<summary>` tags.

```
Having some problems firing up the laser.

<details>
<summary>Click here to see terminal history + debug info</summary>
<pre>
488 cd /opt/LLL/controller/laser/
489 vi LLLSDLaserControl.c
490 make
491 make install
492 ./sanity_check
493 ./configure -o test.cfg
494 vi test.cfg
495 vi ~/last_will_and_testament.txt
496 cat /proc/meminfo
497 ps -a -x -u
498 kill -9 2207
499 kill 2208
500 ps -a -x -u
501 touch /opt/LLL/run/ok
502 LLLSDLaserControl -ok1
```

![](https://i0.wp.com/user-images.githubusercontent.com/121322/78515738-d2333a00-776b-11ea-9a08-fa8c19b2ae5f.gif?ssl=1)

### [Centering text and images](#centering-text-and-images)

It’s 2020 and I still struggle with centering anything in web pages. I find a combination of `<div align=”center”> [ Your content here ]</div>` works wonders. Perfect for centering a logo in your repository’s README, for example.

```
<div align="center">
<img src="https://octodex.github.com/images/dunetocat.png" width="200">
<p>This is some centered text.</p>
</div>
```

![](https://i0.wp.com/user-images.githubusercontent.com/121322/78515743-d95a4800-776b-11ea-92f0-1bcbe71bf4ea.png?ssl=1)

### [Smaller text](#smaller-text)

Wrap text in `<sup>` or <sub> tags to make it a little smaller. Perfect for adding things like “Fig 1: description” under images, or making text smaller in tables so it doesn’t scroll horizontally.

```
<div align="center">
<img src="https://octodex.github.com/images/megacat-2.png" width="200"><br>
<sup><strong>Fig 1:</strong> Megatocat into action</sup>
</div>
View more octocats on the [Octodex](https://octodex.github.com/)!
```

![](https://i0.wp.com/user-images.githubusercontent.com/121322/78515753-e37c4680-776b-11ea-9d90-eaed38ffc35b.png?ssl=1)

At this point, we’re basically back in the 90s with good old-fashioned, hand-crafted HTML. As someone who did that using Notepad and Netscape Navigator back in the day, I’m okay with that.

**Bonus Markdown Protip:** My buddy [@bitoiu](https://github.com/bitoiu) had some [great tips for working with Markdown tables](https://github.blog/2020-04-02-github-protips-tips-tricks-hacks-and-secrets-from-vitor-monteiro/#magic-markdown-tables-%e2%9c%a8) in the [last GitHub Protips post](https://github.blog/2020-04-02-github-protips-tips-tricks-hacks-and-secrets-from-vitor-monteiro/)—definitely check it out!

## [7\. URL-hacking topics](#7-url-hacking-topics)

One of my guilty pleasures is looking for new projects on GitHub tagged with [`#game`](https://github.com/topics/game), and playing testing them, or cloning them to “[change stuff and see what happens](https://twitter.com/ThePracticalDev/status/720257210161311744)”. It’s a great activity for coffee breaks or boring Sunday afternoons.

Our UI exposes ways for you to filter by a single topic and language (for example, [searching for all repositories categorized as `#game` written in JavaScript](https://github.com/topics/game?l=javascript)). The only way to view the search results for the combination of two topics is through a bit of URL hacking. Simply append a `?q=[TOPIC]` to the topic URL to combine the results of two topics. Some examples:

*   **All repositories tagged with `#covid-19` and `#visualization`:**  
    [https://github.com/topics/covid-19?q=visualization](https://github.com/topics/covid-19?q=visualization)
*   **All repositories tagged with `#chrome-extension` and `#github`:**  
    [https://github.com/topics/chrome-extension?q=github](https://github.com/topics/chrome-extension?q=github)
*   **All repositories tagged with `#unity` and `#shader`:  
    **[https://github.com/topics/unity?q=shader](https://github.com/topics/unity?q=shader)
*   **All repositories tagged with `#minecraft` and `#mod`:**  
    [https://github.com/topics/minecraft?q=mod](https://github.com/topics/minecraft?q=mod)

**Did you know**: [Applying topics to your repositories](https://help.github.com/en/github/administering-a-repository/classifying-your-repository-with-topics) helps people discover them, and even contribute to them? It’s as simple as clicking a button and typing a few keywords related to your project’s purpose and subject area:

![](https://github.blog/wp-content/uploads/2020/04/investing-app-take-3.gif?resize=800%2C181)

## [8\. Dark theme](#8-dark-theme)

For the **l33t h4x0rs** amongst you, the [unofficial GitHub Dark Theme](https://github.com/StylishThemes/GitHub-Dark) browser extension might be of interest. It works with Chrome, Firefox, Opera, and Safari, plus we finally [fixed that favicon issue](https://twitter.com/vdepizzol/status/1245090627508768768). Perfect for those late-night hacking sessions. ![😎](https://s.w.org/images/core/emoji/17.0.2/svg/1f60e.svg)

[![](https://github.blog/wp-content/uploads/2020/04/github-dark.png?resize=1024%2C640)](https://github.com/StylishThemes/GitHub-Dark)

**Did you know:** Most software engineers prefer to use dark mode because, wait for it… _light attracts more bugs_. `</dad_joke>`

## [9\. A numbers game](#9-a-numbers-game)

Sometimes it’s useful (or entertaining) to analyze a repository’s metadata and pull out metrics. Hopefully nobody’s judged on how many commits they make, but you can generate an ordered list of authors by commit count from the command line with `git shortlog -sn`.

```
$ git shortlog -sn

3164  Stanley Goldman
1549  Andreia Gaita
195  Don Okuda
191  Emil "AngryAnt" Johansen
15  Meaghan Lewis
9  Lee Reilly
8  Sarah Guthals
7  Sam Christiansen
7  Mauro Palumbo
6  Marcus Christensen
```

You can also exclude merge commits with `git shortlog -sn --no-merges`.

If it’s a public repository, [GitHub High Scores](https://leereilly.net/github-high-scores/) gives you an old-school, 8-bit, arcade-like view of your repository’s contributors. Perfect for showboating your dominance and printing out to pin on the office bulletin board or fridge. ![💪🏻](https://s.w.org/images/core/emoji/17.0.2/svg/1f4aa-1f3fb.svg)

[![](https://github.blog/wp-content/uploads/2020/04/image5.png?resize=1024%2C446)](https://leereilly.net/github-high-scores/)

Anyone who squashes their commits is going to be lower on the table—everyone’s a winner.

That’s just the commits, but what about lines of code? Every good engineer knows that’s the most important metric. There are tons of neat CLI projects to help you analyze the Git data.

[@arzzen](https://github.com/arzzen/)’s [git-quick-stats](https://github.com/arzzen/git-quick-stats) gives a nice overview of repository activity. You can even see contributions by day, hour, and month.

```
$ git-quick-stats

Stanley Goldman <StanleyGoldman@github.com>:
 insertions:    1800 (1%)
 deletions:     1455 (1%)
 files:         221 (2%)
 commits:       108 (3%)
 lines changed: 3255
 first commit:  Thu Apr 6 09:33:53 2017 -0700
 last commit:   Fri Jul 27 14:14:51 2018 -0400
```

[git-fame](https://github.com/casperdcl/git-fame) [from @casperdcl](https://github.com/casperdcl/git-fame) also summarizes contributions including lines of code.

```
$ git-fame

Total commits: 5190
Total ctimes: 17640
Total files: 1058
Total loc: 113683
| Author                   |   loc |   coms |   fils |  distribution   |
|:-------------------------|------:|-------:|-------:|:----------------|
| Stanley Goldman          | 75955 |   3164 |    414 | 66.8/61.0/39.1  |
| Andreia Gaita            | 34438 |   1549 |    477 | 30.3/29.8/45.1  |
| Emil "AngryAnt" Johansen |  2230 |    191 |     35 | 2.0/ 3.7/ 3.3   |
| Don Okuda                |   312 |    195 |     51 | 0.3/ 3.8/ 4.8   |
| Meaghan Lewis            |   228 |     15 |     31 | 0.2/ 0.3/ 2.9   |
```

[@IonicaBizau](https://github.com/IonicaBizau/)’s [git-stats](https://github.com/IonicaBizau/git-stats) includes all sorts of interesting data, including contributions and pie charts. Much like many of his projects, the CLI output is delightful. ![👏🏻](https://s.w.org/images/core/emoji/17.0.2/svg/1f44f-1f3fb.svg)

[![](https://i0.wp.com/user-images.githubusercontent.com/121322/78825418-cd9d9a00-7994-11ea-8fe4-9353059e0da9.png?ssl=1)](https://github.com/IonicaBizau/git-stats)

Hopefully you and your team understand your value is measured by more than lines of code and number of commits. If those metrics _are_ tied to your holiday bonus, it might be time to look for a new job. [We’re hiring](https://github.com/about/careers)!

## [10\. Morse code workout ![💪🏻](https://s.w.org/images/core/emoji/17.0.2/svg/1f4aa-1f3fb.svg)](#10-morse-code-workout-%f0%9f%92%aa%f0%9f%8f%bb) 

Last, but not least… have you ever dreamt for a way to get your exercise in _and_ practice your morse code?!? Wait no more! This [ingenious app](https://github.com/veggiedefender/open-and-shut) from [@veggiedefender](https://github.com/veggiedefender) generates morse code by repeatedly slamming your laptop shut, and comes with the greatest [feature list](https://github.com/veggiedefender/open-and-shut#features) I’ve ever seen. It’s great exercise while you’re stuck in the house, and still paying for that gym membership. [.-.. — .-..](https://morsify.net/)

[![](https://i0.wp.com/user-images.githubusercontent.com/121322/78318062-bab04300-7518-11ea-8b85-6184d0ae7f2e.gif?ssl=1)](https://github.com/veggiedefender/open-and-shut)

_Editor’s note: We honestly aren’t sure if Lee is joking, or serious with this one. Proceed with caution and at your own risk. ![🤷](https://s.w.org/images/core/emoji/17.0.2/svg/1f937.svg)_ 

That’s enough tips and dad jokes for one blog post. Thanks for reading! <3

## [Do you have a GitHub Protip?](#do-you-have-a-github-protip)

Do you have a tip, trick, or hack that makes your daily life easier on GitHub? Share it with us on social media with [#GitHubProtips](https://twitter.com/search?q=%23GitHubProtips&src=typed_query).

## Written by

 ![Lee Reilly](https://avatars.githubusercontent.com/u/121322?v=4&s=200)

Senior Program Manager, GitHub Developer Relations. Open source hype man, AI whisperer, hackathon and game jam wrangler. I write && manage programs, support dev communities, and occasionally ship something.

## Explore more from GitHub

![Docs](https://github.blog/wp-content/uploads/2024/07/Icon-Circle.svg)

### Docs

Everything you need to master GitHub, all in one place.

[Go to Docs](https://docs.github.com/)

![GitHub](https://github.blog/wp-content/uploads/2024/07/recirculation-github-icon.svg)

### GitHub

Build what’s next on GitHub, the place for anyone from anywhere to build anything.

[Start building](https://github.com/)

![Customer stories](https://github.blog/wp-content/uploads/2024/07/Icon_da43dc.svg)

### Customer stories

Meet the companies and engineering teams that build with GitHub.

[Learn more](https://github.com/customer-stories)

![GitHub Universe 2026](https://github.blog/wp-content/uploads/2025/06/Universe26-Icon.svg)

### GitHub Universe 2026

Catch up on the key announcements shaping the future of software development.

[See what's new](https://github.com/events/universe/recap?utm_source=blog-bottom-tile-home-k2k&utm_medium=blog&utm_campaign=universe-2026)
