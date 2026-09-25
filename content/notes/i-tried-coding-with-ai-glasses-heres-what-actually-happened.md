---
title: "I Tried Coding With AI Glasses. Here’s What Actually Happened."
date: '2026-09-25T00:15:06+01:00'
category: webclip
summary: 'The author says the glasses were a gift and that he would not have bought them himself, but used them to see whether they could improve his life as a developer. His first tests with AI help for code explanations were disappointing, so he shifted to a different use case focused on recording daily life.'
tags: ["ai-glasses","coding","self-tracking"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "I Tried Coding With AI Glasses. Here’s What Actually Happened."
    url: "https://dev.to/javz/i-tried-coding-with-ai-glasses-heres-what-actually-happened-27fh?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--i-tried-coding-with-ai-glasses-heres-what-actually-happened.md"
    kind: repo
---

The author says the glasses were a gift and that he would not have bought them himself, but used them to see whether they could improve his life as a developer. His first tests with AI help for code explanations were disappointing, so he shifted to a different use case focused on recording daily life.

He proposes “life commits”, where the glasses capture moments during the day, classify the image with Apple’s Vision framework, and attach an emotional score through hand gestures or manual input. The resulting timeline is meant to show where time is spent, which environments are common, and how they relate to mood. He says the glasses do not fundamentally change coding, but they do change how he captures and reflects on his life.

## Reading notes

- Received the AI glasses as a gift and wanted to evaluate whether they would improve his life as a developer.
- Tried using the integrated AI to explain code on the screen, but the results were bad because the system did not accurately recognize the visual context.
- Thought about a more complex chain with image capture, OCR, vision model, and LLM, but considered this solution cumbersome, expensive, and less reliable than asking for help directly in the editor.
- Shifted the focus to “life commits”, an idea in which the glasses record moments of the day as if they were Git commits.
- Describes a flow in which the app asks for a capture every hour and classifies the image with the Apple Vision framework into categories such as workspace, outdoors, social, exercise, indoors and screen time.
- Associates an emotional score with each moment through manual gestures detected with `VNDetectHumanHandPoseRequest()` or through manual input in the app.
- Says this creates a timeline of what the person does, the environments they stay in, and how these environments relate to emotional state.
- States that music through the glasses, talking to the AI during code, and quickly capturing photos and videos are convenient uses.
- Concludes that the glasses still seem like early-stage hardware, do not fundamentally change how he codes, but can be useful for capturing and reflecting on life.
