---
title: "Motion sensing using the doppler effect"
date: '2015-03-10T21:53:24-03:00'
category: webclip
summary: 'The page explains how a laptop speaker and microphone can detect motion by sending an inaudible tone, measuring the Doppler shift in the microphone input, and using bandwidth differences for sensing, scrolling, and sound control.'
tags: ["doppler-effect", "motion-sensing", "audio", "scrolling"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Motion sensing using the doppler effect"
    url: "https://danielrapp.github.io/doppler/"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-03/danielrapp-github-io--motion-sensing-using-the-doppler-effect.md"
    kind: repo
---

The page describes a way to detect motion on a normal computer with only a speaker and a microphone. It sends a 20 kHz sinusoid, watches how motion shifts the frequency spectrum around that tone, and uses the left-right bandwidth difference as the signal for interaction.

## Reading notes

- A moving object changes the frequency of reflected sound, so motion can be detected without special hardware.
- The method sends an inaudible 20 kHz tone and reads shifts in the microphone spectrum near that frequency.
- The page says Chrome needs a fairly high speaker volume for the setup to work well.
- Moving a hand toward the mic shifts the bulge toward higher frequencies, and moving away shifts it toward lower frequencies.
- The bandwidth difference can drive a box that gets smaller when the hand moves toward the microphone and larger when it moves away.
- The same signal can be used for scrolling, with fast movement toward the computer and slow movement away from it.
- The page also sketches a Theremin-like instrument that modulates a 440 Hz tone from the bandwidth difference.
- A small library is provided to experiment with the technique.
