---
title: "How I built a sub-500ms latency voice agent from scratch"
date: '2026-09-25T22:39:57+01:00'
category: webclip
summary: 'The post argues that voice agents are an orchestration problem, and shows how a streaming pipeline with turn detection, cancellation, geography, and fast model choice cut latency from about 1.6s to around 400ms.'
tags: ["voice-agents", "latency", "orchestration", "llm"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How I built a sub-500ms latency voice agent from scratch | Nick Tikhonov"
    url: "https://www.ntik.me/posts/voice-agent?utm_source=weeklyfoo&utm_medium=email&utm_campaign=weeklyfoo"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/ntik-me--how-i-built-a-sub-500ms-latency-voice-agent-from-scratch.md"
    kind: repo
---

The post argues that voice agents are hard because speech is continuous and real time, so the system has to know when the user is speaking, when they are listening, and when to stop or start the agent immediately. It shows that the core problem is not one model, but coordination across turn detection, transcription, generation, text to speech, buffering, and network hops.

It then walks through a build that starts with VAD and a prerecorded reply, moves to Deepgram Flux for turn detection, and later uses a streaming pipeline where LLM tokens flow straight into TTS and audio goes back to Twilio. Moving the orchestration layer to the EU and using region-matched services cut latency from about 1.6s locally to about 790ms, and swapping in Groq’s llama-3.3-70b brought average end-to-end latency to about 400ms.

## Reading notes

- Voice agents need continuous coordination, because the system must decide at each moment whether the user is speaking or listening.
- Turn-taking is the core loop: when the user starts speaking, the agent must stop generation and audio immediately; when the user stops, the agent must begin responding with minimal delay.
- A first prototype used FastAPI, Twilio audio, Silero VAD, and a simple state machine that played a prerecorded WAV file when speech ended.
- VAD alone is not enough for real turn-taking, because pauses inside a sentence can look like the end of a turn.
- The next version used Deepgram Flux to combine streaming transcription and turn detection, with start-of-turn and end-of-turn events.
- The agent turn was built as a streaming pipeline: transcript and history to the LLM, first token into TTS over WebSocket, and audio packets straight back to Twilio.
- Keeping TTS WebSocket connections warm reduced latency by about 300ms.
- Barge-ins were handled by canceling LLM generation, tearing down TTS, and flushing queued audio when Flux detected that the user started speaking.
- Running the orchestration locally from southern Turkey produced about 1.6s end-to-end latency, with Twilio adding about 100ms more.
- Deploying to Railway in the EU and using EU regions for Twilio, Deepgram, and ElevenLabs reduced server-measured latency to about 690ms and total end-to-end latency to about 790ms.
- A comparison of first-token latency across providers showed Groq’s llama-3.3-70b as much faster than the OpenAI model used earlier.
- Replacing gpt-4o-mini with Groq’s llama-3.3-70b brought average end-to-end latency to about 400ms.
- The technical takeaways emphasize latency, TTFT, pipelining, immediate cancellation, and geography as major factors in voice systems.
- The post argues that off-the-shelf platforms still provide useful APIs, observability, reliability, and config depth, but building a stripped-down system helps explain what the parameters actually do.
