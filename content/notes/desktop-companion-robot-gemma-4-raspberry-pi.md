---
title: "How we built a desktop companion robot with Gemma 4 and Raspberry Pi"
date: "2026-09-23T13:51:08+01:00"
category: webclip
has_commentary: false
summary: "A LEGO-bodied desk robot switches between a local Gemma 4 model for instant private chat and cloud Gemini for harder reasoning, its eyes and motors driven by a five-state machine."
tags:
  - ai
  - robotics
  - raspberry-pi
  - hardware
sources:
  - title: "How we built a desktop companion robot with Gemma 4 and Raspberry Pi - DEV Community"
    url: "https://dev.to/googleai/how-we-built-a-desktop-companion-robot-with-gemma-4-and-raspberry-pi-2oke"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--how-we-built-a-desktop-companion-robot-with-gemma-4-and-raspberry-pi.md"
    kind: repo
---

A Google AI team built DinoDesk AI, a LEGO-bodied desk robot running a hybrid local/cloud architecture. Gemma 4, running locally through LM Studio, handles routine chat with near-instant response and full privacy, since the robot has no camera. Gemini Flash takes over for heavier reasoning, coding help, or complex explanations, with a router on the user's PC deciding which engine answers each request. A five-state finite state machine coordinates the robot's LCD eyes, 8-bit sound, and motor movements so the character reads as alive rather than assembled from separate parts.

## Reading notes

- A Raspberry Pi on the desk sends identical requests over Wi-Fi to a Hybrid LLM Gateway on the user's PC, regardless of which engine ends up answering.
- Local mode, Gemma 4 via LM Studio, delivers about 200ms first-token latency for casual chat, fully offline and private. Cloud mode, Gemini Flash, takes over for coding help or deep explanations at roughly 800ms first token.
- Auto-Hybrid mode defaults to the local model and escalates to the cloud only when a prompt shows multi-step reasoning keywords like "explain," "compare," or "write code," visible to the user as the status light shifting from green to gold.
- The body is built from LEGO bricks and Technic mechanisms instead of a sealed 3D-printed shell, so it can be customized or repaired by hand.
- A five-state finite state machine, Sleeping, Idle, Listening, Thinking, Speaking, coordinates the LCD eye expressions, 8-bit sound cues, and neck and tail motor movement for each state.
- Four hardware buttons handle cancel and mute, servo re-centering, expression and engine switching, and a tail-wag test with volume control, alongside voice and sensor triggers.
