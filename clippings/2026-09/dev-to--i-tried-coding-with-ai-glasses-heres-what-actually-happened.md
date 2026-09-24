---
url: "https://dev.to/javz/i-tried-coding-with-ai-glasses-heres-what-actually-happened-27fh?context=digest"
captured_at: "2026-09-25T00:15:06+01:00"
title: "I Tried Coding With AI Glasses. Here’s What Actually Happened."
domain: "dev-to"
---

I was recently gifted a pair of AI glasses. This is not the kind of purchase I would make for myself. But since I now own a pair, I saw this as an interesting opportunity to assess whether these glasses could improve my daily life as a developer.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fckghbiieq58lkdrirfxv.jpeg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fckghbiieq58lkdrirfxv.jpeg)

* * *

## [](#initial-experiments)Initial experiments

The first thing I tried was using the integrated AI to ask me to explain code on my screen. The results were… disappointing. I tried different situations:

*   Explaining a simple HTML file
*   Debugging a specific line of code
*   Providing context-aware explanations

It couldn’t reliably identify what I was looking at. It lacked precise understanding of the visual context.

I started thinking about a better pipeline:

1.  Capture frame from glasses camera
2.  Apply OCR to extract visible text
3.  Feed image + extracted context into a capable vision model
4.  Send result to an LLM
5.  Return explanation as audio through the glasses

In theory, this could turn the glasses into a real-time coding assistant. However this felt like too much work, complex and expensive. And less reliable than simply prompting an assistant directly inside the editor.

## [](#a-different-idea-life-commits)A different idea: Life commits

That’s when I realized something.

Maybe AI glasses aren’t useful because they help you code better. Maybe they’re useful because they help you understand yourself better.

So I tried something different.

What if I used my glasses to capture my life? I call them life commits. Just like Git commits capture the evolution of code, life commits capture the evolution of your day.

It is very seamless to take photos with your glasses on the fly, unlike a phone which you need to take out of your pocket, creating friction.

The idea is simple:

Every hour, the app prompts you to capture a moment.

The captured image is automatically classified using Apple's Vision framework:  

```
VNClassifyImageRequest()
```

Enter fullscreen mode Exit fullscreen mode

This allows categorization of environments like:

*   workspace
*   outdoors
*   social
*   exercise
*   indoors
*   screen time

Then, I associate an emotional score with each moment.

This can be done in two ways:

Hand gestures, detected using:  

```
VNDetectHumanHandPoseRequest()
```

Enter fullscreen mode Exit fullscreen mode

Or manually, through the app.

Over time, this creates a timeline of:

*   where you spend your time
*   what environments you inhabit
*   how those environments correlate with your emotional state

The insights and patterns could be interesting to look at over time to improve your daily life and improve your emotional state.

Here is a demo of the flow I built:  
[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpdlwldk3nf2ypksaoux2.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpdlwldk3nf2ypksaoux2.gif)

Here is the working prototype to test this idea: [https://github.com/JulienAvezou/ai-glasses](https://github.com/JulienAvezou/ai-glasses)

## [](#would-i-recommend-buying-ai-glasses)Would I recommend buying AI glasses?

I surprisingly enjoy listening to music through my glasses. While it doesn’t replace a comfy headset, it’s nice to hear music clearly without having anything on or above your ears.

Prompting the AI to provide simple explanations while coding is nice too, as it’s very convenient to just have a conversation on the go whether at the desk or moving around.

The ease of taking photos or videos on the fly is nice too.

But right now, AI glasses still feel like early hardware.

Not useless. But not essential.

They don’t fundamentally change how I code.

But they do change how I capture and reflect on my life.

That might be their real potential.

* * *

**So what do you think? Gadget or useful?**

Curious to know if someone out there is actively using AI glasses.

How do you incorporate them into your daily routine? (exercising, coding, …)
