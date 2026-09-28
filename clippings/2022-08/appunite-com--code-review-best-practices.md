---
url: "https://appunite.com/blog/code-review-best-practices"
captured_at: "2022-08-05T10:29:11-03:00"
title: "Code Review Best Practices | AppUnite"
domain: "appunite-com"
---

# Code Review Best Practices

Aug 02, 2022 | 5 min read

![large_2_X4_A8176_min_5e6a92ce1c.jpeg&w=1080&q=75](appunite-com--code-review-best-practices/695867b02f9d61c00296dc290c7c4b5d.jpg)

A chunk of every developer's work is a code review, but are you doing it well? I'll talk about how to do a good code review and the best practices I've learned over my years of experience as a developer. I'll also talk about what a person requesting a code review should do before asking for it.

*Maciej Kaszubowski has already written an article about the harm of doing a code review, and it's a slightly different perspective. If you're interested in that, you can read it [here](https://appunite.com/blog/is-code-review-harmful).*

Ok, without further due, let's jump right in.

## Be quick

Nobody wants to wait long for feedback while losing the momentum takes energy to get back to the given PR. That's why a code review should almost always be your priority. I'm not saying you should drop everything you're doing at the moment to start a code review. However, if you're using Pomodoro or taking regular breaks, check if there are any PRs then and don't let another person wait for you longer than expected. In a perfect scenario, you should do the review within an hour so the person submitting still has time to work on the necessary fixes while not losing too much focus.

## Be your own QA

It might be a bit controversial, but the idea is to checkout into the branch you're reviewing and live to test the features. It might take some time, but it ensures that the most apparent bugs won't appear on the staging app. Think of it as an investment that'll save your time later. Let me explain. If you send the app with a bug, your QA is wasting time reviewing the issue, then you need to waste time fixing that issue and the cycle continues. Once I started doing it, I began to feel like it was one of the most crucial parts of a code review, especially on frontend apps.

## Discuss the crux

Everyone has their unique way of writing code and it's all right! However, slight differences usually aren't worth discussing, so you shouldn't point them out, especially if you've already done them in previous attempts.

However, it's also worth agreeing on some code styling rules. It should reduce the number of differences to the most insignificant ones - you can always add something there, if you find it annoying.

The crucial best practice for a code review is readability. If you cannot understand a piece of code or it's taking too long, leave a comment or hop on a call to discuss it. Sometimes even debugging or reviewing the code in some IDE helps (unless it takes too long), but don't be afraid to express your confusion once something isn't clear.

## Automate the others

Adding lints or other analyzing options can save you a lot of time. You don't need to read into the code looking for these minor issues because they'd be automatically detected by the system, not by a human. The same goes for formatting. You can ensure that all files are formatted by setting some [githook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) or adding a script on CI - I cannot imagine reviewing unformatted code.

## Double check the changes

It might be a bit controversial as I agree that trusting your teammates is fundamental, but it's not as big of mistrust as you think. I don't mean going through every line of code again. Instead, it means quickly going through the code to spot any breaking changes or errors. And Github makes it easy once you mark the files as viewed.

## Things you should do before submitting a PR

### Make a description

Provide a clear explanation of what you've worked on in this PR since titles can also lack some context. It's also worth linking related documentation docs or taking a video or screenshot of the changes.

### Review PR yourself before you ask for a review

You can find all the minor errors, typos, etc., so double-check the PR before you ask someone else for the review. It can be highly annoying if you're asking someone to review broken code or something that doesn't look good, but you've forgotten about it and carried on. If you can't make the changes now, then leave a comment. It's much better than leaving nothing at all.

### Make sure tests don't fail.

I'm not talking only about the automated tests, nor about running the app yourself. Many programmers don't make such an effort because they think it's QA's job. Still, it's also your responsibility to provide and ensure the quality of your changes.
It's a good practice to run your automated tests and static analyses before every push and format your changes before committing them. You can quickly achieve it using git hooks. You can find more info about them [here](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks).

### Make your PRs as small as possible.

In the end, in my opinion, it's much easier to review a few smaller batches of code instead of one huge one, especially if they don't relate to the same thing. So make your pushes as small as possible. People will thank you later.

## Summary

If you've read Maciej's article, you can see that we agree and disagree on some of the points. In comparison, Maciej speaks more about what effects code review can have on a team. I have focused entirely on the code review best practices without reviewing if it's harmful or not, so if you're a person that prefers to stick to doing code reviews, then hopefully, you have found some of these tips helpful.
