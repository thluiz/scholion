---
url: "https://dev.to/frasertooth/combatting-burnout-with-the-go-to-sleep-a-tron-25f9"
captured_at: "2026-11-16T01:59:02+00:00"
title: "Combatting Burnout with the \"Go to Sleep-a-tron\""
domain: "dev-to"
---

A couple of weeks ago, I saw two things:

First, I saw a tweet from Charlie Gerard showing her great project to combine ML and Github culture to create a Github action to auto-admonish toxic comments on PRs and the like.  

Then I saw the [Actions Hackathon](https://dev.to/devteam/announcing-the-github-actions-hackathon-on-dev-3ljn) challenge announced and thought I should give it a go.

So, inspired by Charlie's idea of making Github culture a little better (and no small amount of using her code-base to figure out Github Actions), I hereby present my very silly Github Action [go-to-sleep](https://github.com/FraserTooth/go-to-sleep) aka **The Go-To-Sleep-a-tron** _[Hackathon Submission](https://dev.to/frasertooth/go-to-sleep-a-tron-1cmk)_

## The Github Go-To-Sleep-a-Tron Action

[![Sleepy Time](https://camo.githubusercontent.com/e275cc8148597c6b81c8992a96a6b7d0ffdcaac033a441d954e3c549292c3e1e/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f6d67755072564a416e454849592f67697068792e676966)](https://camo.githubusercontent.com/e275cc8148597c6b81c8992a96a6b7d0ffdcaac033a441d954e3c549292c3e1e/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f6d67755072564a416e454849592f67697068792e676966)

Stop coding and go to sleep!

**[Example Commit with Message](https://github.com/FraserTooth/go-to-sleep-action/commit/a46d6fd23defa2b5b9c974cebbc843eeb01a5ff9)**

## Inputs

### `GITHUB_TOKEN`

**Required**  
Just put `${{ secrets.GITHUB_TOKEN }}` and it should work fine.

### `custom_mesage`

**Optional**  
Put your custom message as a HTML formatted string:  
e.g. `custom_message: "Oh dear, its very late where you are.\nWe appreciate your hard work but maybe you should go to bed."`

Default: `"Its quite late, maybe you should go to sleep!"`

### `timezone`

**Required for any events other than commits (push)**  
Enter your team's timezone in the ISO format `(+/-)hh:mm`:  
e.g. `timezone: "+09:00"`

## How to use

_If you do not have any Github actions already set up in your repo, start by creating a .github/workflows folder._

Inside your workflows folder, create a new .yml file, for example `main.yml` and copy the following lines:

on
  \[
    push,
    pull\_request,                 # Slightly Supported
    pull\_request\_review,          # Not Supported
    pull\_request\_review\_comment,  # Not Supported
    issues,                       # Not

…

Enter fullscreen mode Exit fullscreen mode

In short, this Action will simply check the time of the commits pushed to the repo, and will post a comment to the commit if it was committed 'overnight', from the perspective of the committer's timezone. It will work on any branch and the message you send can be customised 😁

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fyl3kx9zh9t1n8bvj59z0.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fyl3kx9zh9t1n8bvj59z0.gif)

I've currently set it to trigger before 9am and after 7pm, because thats when you should be cooking, eating, sleeping and reading terrible dev.to articles instead of doing more work!

My intended user would be companies who want to discourage overworking, so if you want me to keep working on this, [let me know!](https://github.com/FraserTooth/go-to-sleep-action/issues)

## [](#how-it-works)How It Works

For the most part I followed the [Official Guides](https://docs.github.com/en/actions/creating-actions/creating-a-javascript-action) and [Charlie's Code](https://github.com/charliegerard/safe-space) but in general my code does the following:

1.  Takes in the Action Data and Inputs
2.  If its a Commit Action ('Push') it will check each commit for a `timestamp` field. Which contains the time, and thankfully, the timezone in which the commit was made.
3.  If the time is before 9am or after 7pm in a given day, a comment will be posted on the commit, using the custom or default message.

Pretty simple right, but there were some gotchas...

## [](#the-gotchas)The Gotchas

### [](#timestamps-in-github)Timestamps in Github

I initially wanted to have this trigger for any commentable Github action (Open PR, PR Review, Issues...) but for some reason, the **only** timestamp within the data provided both within the Github actions data and the Github API that contains the commiter's timezone is "commit data" inside Github Actions input data. Otherwise, the time is only available in UTC 🤷‍♀️ (you can check my [test data](https://github.com/FraserTooth/go-to-sleep-action/tree/master/test/fixtures) for examples of the data given)  
Naturally, the next step is to allow the addition of user-specific timezones as an input to the `workflows/main.yml` file, but this removed some of the magic and wasn't as fun 😔

### [](#timezones-in-javascript)Timezones in Javascript

Timezones are a known pain point in programming, and yes, there are some good libraries like [moment.js](https://momentjs.com/) to help with this...in a normal situation.  
The issue I had, was that these timezone libraries are built with the understanding that you will know where the person is before you need to make the conversion, such as the country.  
As far as I can tell, it's not possible to find out the location of a given Github user (profile location is too 'custom' and I found no usable data in the API), and plus...I didn't really need to care 😂. I **already had the timezone**, so I could just figure out if they were up late, regardless of their actual location.  
However, there isn't an easy way to retain 'original timezone' when parsing dates with these libraries, so upon parsing the datestring, I would be stuck in UTC 😒  
In the end, I just ended up using Regex to extract the timezone section of the string and do the 'is it bedtime' math manually. It was kind of painful, but I suppose I learnt something about dates in Javascript 😵...or something...

### [](#github-actions-dev-cycle)Github Actions Dev Cycle

Another gotcha was that its kinda annoying to get Github actions running locally, so in developing this I was stuck making commits and pushes to check the functionality...  
There is a rather neat tool called [act](https://github.com/nektos/act) which allows you to run Github actions locally 🙌 but I could only figure out how to get them from a remote source, so I just had to push the changes to Github anyway 😐  
While writing this, I found an [Issue](https://github.com/nektos/act/issues/307) in the repo that suggests getting local actions is doable, so that would be my next TODO.

## [](#future-feature-ideas)Future Feature Ideas

Aside from some small obvious things, if people think this idea is interesting (and encourage me to improve it!), I think these additions might be useful:

*   Add more Github Action types (despite the lack of magic)
    *   There might be a clever way to figure out a commenter/contributer's timezone, but short of keeping a database I'm not sure what it would be outside of...
*   Add a 'per Github contributor' timezone
    *   This would solve problem one, but it strikes me as clunky 🤔
*   Allow configuration of posting to a basic Slack webhook or sending an Email to send notifications outside of Github
    *   One key problem with this is that I never read emails from Github or look at the notifications 🤣, sending messages externally might be useful for a Manager to keep an eye out for unhealthy behaviour.

## [](#cheers-mdears)Cheers M'Dears

All in all, thank you for reading, check out my [Github](https://github.com/FraserTooth) for other projects and my [Twitter](https://twitter.com/FraserTooth) for inconsistent mutterings. Cheerio!
