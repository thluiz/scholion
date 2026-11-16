---
url: "https://github.com/emilybache/GildedRose-Refactoring-Kata"
captured_at: "2026-11-16T03:09:39+00:00"
title: "GitHub - emilybache/GildedRose-Refactoring-Kata: Starting code for the GildedRose Refactoring Kata in many programming languages."
domain: "github-com"
---

_Support this and all my katas via [Patreon](https://www.patreon.com/EmilyBache)_

## Gilded Rose Refactoring Kata

[](#gilded-rose-refactoring-kata)

You can find out more about this exercise in my YouTube video [Why Developers LOVE The Gilded Rose Kata](https://youtu.be/Mt4XpGxigT4). I also have a video of a worked solution in Java - [Gilded Rose Kata, Hands-on](https://youtu.be/OdnV8hc9L7I)

I use this kata as part of my work as a technical coach. I wrote a lot about the coaching method I use in this book [Technical Agile Coaching with the Samman method](https://leanpub.com/techagilecoach). A while back I wrote this article ["Writing Good Tests for the Gilded Rose Kata"](http://coding-is-like-cooking.info/2013/03/writing-good-tests-for-the-gilded-rose-kata/) about how you could use this kata in a [coding dojo](https://leanpub.com/codingdojohandbook).

## How to use this Kata

[](#how-to-use-this-kata)

The simplest way is to just clone the code and start hacking away improving the design. You'll want to look at the ["Gilded Rose Requirements"](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.md) which explains what the code is for. I strongly advise you that you'll also need some tests if you want to make sure you don't break the code while you refactor.

You could write some unit tests yourself, using the requirements to identify suitable test cases. I've provided a failing unit test in a popular test framework as a starting point for most languages.

Alternatively, use the Approval tests provided in this repository. (Read more about that in the section "Text-based Approval Testing").

The idea of the exercise is to do some deliberate practice, and improve your skills at designing test cases and refactoring. The idea is not to re-write the code from scratch, but rather to practice taking small steps, running the tests often, and incrementally improving the design.

### Gilded Rose Requirements in other languages

[](#gilded-rose-requirements-in-other-languages)

*   [English](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.md)
*   [Español](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements_es.md)
*   [Français](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements_fr.md)
*   [Italiano](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements_it.md)
*   [日本語](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements_jp.md)
*   [Português](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements_pt-BR.md)
*   [Русский](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements_ru.md)
*   [Українська](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements_ua.md)
*   [ไทย](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements_th.md)
*   [中文](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements_zh.txt)
*   [한국어](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements_kr.md)
*   [German](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements_de.md)
*   [Euskara](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements_eu.md)
*   [Galego](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements_gl.md)

## Text-Based Approval Testing

[](#text-based-approval-testing)

Most language versions of this code have a [TextTest](https://texttest.org/) fixture for Approval testing. For information about this, see the [TextTests README](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main/texttests)

## History of the exercise

[](#history-of-the-exercise)

This Kata was originally created by Terry Hughes ([http://twitter.com/TerryHughes](http://twitter.com/TerryHughes)). It is already on GitHub [here](https://github.com/NotMyself/GildedRose). Bobby Johnson described the kata in an article titled "Refactor This: The Gilded Rose Kata", but unfortunately it is no longer on the internet. I found it on the Wayback Machine [here](https://web.archive.org/web/20240525015111/https://iamnotmyself.com/refactor-this-the-gilded-rose-kata/).

I translated the original C# into a few other languages, (with a little help from my friends!), and slightly changed the starting position. This means I've actually done a small amount of refactoring already compared with the original form of the kata, and made it easier to get going with writing tests by giving you one failing unit test to start with. I also added test fixtures for Text-Based approval testing with TextTest (see [the TextTests](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main/texttests))

As Bobby Johnson points out in his article "Why Most Solutions to Gilded Rose Miss The Bigger Picture" (on the Wayback Machine [here](https://web.archive.org/web/20230530152324/https://iamnotmyself.com/why-most-solutions-to-gilded-rose-miss-the-bigger-picture/)), it'll actually give you better practice at handling a legacy code situation if you do this Kata in the original C#. However, I think this kata is also really useful for practicing writing good tests using different frameworks and approaches, and the small changes I've made help with that. I think it's also interesting to compare what the refactored code and tests look like in different programming languages.

## Contributing

[](#contributing)

I have been struggling for some time with the maintenance burden for the Gilded Rose respository. I get frequent spurious pull requests from people who have been assigned to work on it as an exercise by some other organization (I don't know who) and mistakenly send me a pull request with their solution. I get so many of these it's a significant amount of work to check that they aren't a legitimate contribution. It's really annoying. I have sadly now added a restriction now so that only prior contributors can now open issues, comment, or create pull requests.

If you would like to make an actual contribution that improves the starting position of the exercise, please see [CONTRIBUTING.md](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/CONTRIBUTING.md) for some ideas about how to get involved.
