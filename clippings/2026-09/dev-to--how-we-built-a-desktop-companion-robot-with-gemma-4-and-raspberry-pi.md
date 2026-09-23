---
url: "https://dev.to/googleai/how-we-built-a-desktop-companion-robot-with-gemma-4-and-raspberry-pi-2oke"
captured_at: "2026-09-23T13:37:33+01:00"
title: "How we built a desktop companion robot with Gemma 4 and Raspberry Pi - DEV Community"
domain: "dev.to"
---

bebechien for Google AI

Posted on Sep 16
•
Originally published at bebechien.github.io

19
6
5
5
7
How we built a desktop companion robot with Gemma 4 and Raspberry Pi
#
raspberrypi
#
gemma
#
gemini
#
robotics

Have you ever wished for a little desk companion—something with the tactile charm of a retro game character that could chat with you, keep track of your desk timers, or talk you through a tricky bug—without a camera staring at you all day?

That question sparked DinoDesk AI: our LEGO Dino AI Companion Robot.

I and my colleague Shama set out to build a smart, low-power desk robot that combines the nostalgia of 8-bit audio-visuals and LEGO Technic mechanics with a modern Hybrid LLM Switching Architecture (Local ↔ Cloud). By pairing a Raspberry Pi on the desk with a local PC gateway running Gemma 4 alongside Gemini Flash, we created a companion that offers 100% visual privacy (no camera), instantaneous zero-cost local chat, and deep cloud reasoning on demand.

Here is the full behind-the-scenes story of how we designed, wired, and programmed DinoDesk AI from the ground up.

1. The Hybrid Brain: Local Gemma 4 ↔ Cloud Gemini

One of the biggest dilemmas when building an AI hardware companion is choosing where the brain lives. If everything runs in the cloud, every casual "What time is it?" costs API tokens, adds network latency, and sends your voice data over the internet. On the other hand, if you strictly limit yourself to a small on-device model, the robot struggles the moment you ask it to create a new feature in your gigantic codebase, or explain a complex topic.

So we decided to build a Hybrid LLM Architecture, with a Unified LLM Gateway (Router) hosted on the user's main PC. The Raspberry Pi on your desk sends identical OpenAI-compatible requests over Wi-Fi regardless of which engine is active:


 ┌─────────────────────────────────────────────────┐
 │           [ Main PC / Local Gateway ]           │
 │                                                 │
 │   ┌─────────────────────────────────────────┐   │
 │   │      Dynamic Model Router / Switch      │   │
 │   └────────────────────┬────────────────────┘   │
 │                        │                        │
 │     ┌──────────────────┴──────────────────┐     │
 │     v                                     v     │
 │  [ LOCAL ENGINE ]              [ CLOUD ENGINE ] │
 │  LM Studio / Gemma 4           Gemini Flash /   │
 │  (Zero Latency, Private)       Gemini Live      │
 └────────────────────────┬────────────────────────┘
                          │
                          │ Wi-Fi (Unified OpenAI-Compatible Stream)
                          v
 ┌─────────────────────────────────────────────────┐
 │           [ DinoDesk AI (RPi) ]                 │
 │  - Pirate Audio LCD & I2S Beep Speaker          │
 │  - Push Button & Optional Sensors               │
 └─────────────────────────────────────────────────┘

Three Modes of Intelligence
Mode	Active Model	Strengths & Primary Use Case	How to Switch
🟢 Local Mode (Default)	Gemma 4 (via LM Studio)	Zero-cost, offline, 100% private. Delivers ~200 ms first-token latency for casual chats, desk timers, and quick status checks.	Double-click Pirate Audio Button X, 3s long-press on Capacitive Touch sensor, or voice command ("Switch to Cloud Mode")
🟡 Cloud Mode	Gemini Flash / Gemini Live	High reasoning & complex problem solving. Ideal for coding help, complex math, deep explanations, or language tutoring (~800 ms first token).	Same as above
⚡ Auto-Hybrid Mode	Automatic Routing	Defaults to Gemma 4 locally. When the complexity classifier detects multi-step reasoning keywords ("explain", "compare", "write code"), it transparently escalates the prompt to Gemini Flash.	Automatic System Routing

When Auto-Hybrid Mode escalates a question to the cloud, the robot's indicator temporarily shifts from 🟢 steady green to 🟡 steady gold for the duration of the response, then returns to green—so you always know at a glance which brain is answering.

2. Hardware & Tactile Mechanics: LEGO Meets Pirate Audio

We wanted DinoDesk AI to feel like a physical toy rather than a cold smart speaker. Instead of 3D-printing a sealed plastic shell, we built the body out of basic LEGO bricks and Technic lever mechanisms so anyone can customize or repair it.

Core Bill of Materials (BOM)
Main Controller: Raspberry Pi + 32GB MicroSD
Display & Audio Shield: Pimoroni Pirate Audio Speaker (1.3" 240×240 ST7789 IPS LCD + I2S 1W Speaker + 4 tactile buttons)
The Red Button: A mini push button switch that gives you a satisfying tactile click to start or stop voice capture
Audio Input: Compact USB Mini Microphone
Motion System: Motors driving Neck movements and Tail wagging

Before building the full body, I first prototyped the logic using a Raspberry Pi and a simple LEGO set.



GIF

Physical Button Controls

Even with voice and sensor triggers, dedicated hardware buttons feel good for instant physical control:

Button A (GPIO 5) — Cancel / Mute: Immediately stops the active response stream, silences audio, and returns the robot to Idle.
Button B (GPIO 6) — Home Re-Center: Resets all servos to their neutral center position without interrupting the current state.
Button X (GPIO 16) — Expression & Engine Switch: Single-click cycles facial expressions manually; double-click toggles Local ↔ Cloud Mode.
Button Y (GPIO 24) — Tail Test & Volume: Single-press fires a tail-wagging sequence to verify mechanical alignment; a 2-second long-press cycles beep volume (Low → Medium → High → Mute).
3. Bringing the Dino to Life: The 5-State Finite State Machine

A companion robot only feels alive when its eyes, voice, and body move together. We designed a 5-stage Finite State Machine (FSM) that coordinates the 240×240 LCD eye expressions, 8-bit beeps, and motor movements:


┌──────────┐  button     ┌───────────┐   release   ┌──────────┐   stream   ┌──────────┐
│ Sleeping │──────────>  │   Idle    │────────────>│Listening │─────────>  │ Thinking │
└──────────┘  (wake)     └───────────┘   (trigger) └──────────┘  (send)    └──────────┘
                             ^                                                  │
                             │              ┌──────────┐                        │
                             └──────────────│ Speaking │<───────────────────────┘
                               (done)       └──────────┘       (tokens arrive)

State	Entry Condition	Pirate Audio LCD Expression	8-Bit Audio Feedback	Motor Action (Neck / Tail)
1. Sleeping	Inactive for 3 mins OR room dark	(- _ -)
Closed eyes + zzz	Silent (or optional soft snore)	Motors relaxed; head tilted slightly down
2. Idle	Default standby	(• •)
Autonomous blinking	Occasional wake/blink chime	Head centers; neck sways slowly
3. Listening	Button click OR sensor trigger	(O O)
Eyes widen bright	"Beep-Boop!" rising tone	Head tilts 15° toward the user
4. Thinking	Audio sent; router inferring	(º º)
Spinning pupils + mode badge	Irregular processing ticks (tick-teek-poh)	Neck sways slowly side-to-side
5. Speaking	Receiving SSE token stream	Expressive blinking + scrolling subtitles	8-bit typewriter beep per token	Tail wags in sync with text length

Building DinoDesk AI reminded us that AI doesn't have to stay locked inside a browser tab or a cloud data center. When you give an open model like Gemma 4 a pair of pixel eyes, an 8-bit voice, a wiggling LEGO tail, and the ability to call on Gemini when things get heavy, your desk suddenly feels a whole lot more lively. 🦖✨

It's still a work in progress and not quite perfect yet, but I'll be back soon with fully implemented voice chat capabilities! Until then, please enjoy the fun little 8-bit sound effects every time you press the button. Beep-Boop!

Clone the repo here : https://github.com/google-gemma/dinodesk-ai-companion/

And drop a comment to share what you're planning to create.

DEV Community

Build Apps with Google AI Studio 🧱

This track will guide you through Google AI Studio's new "Build apps with Gemini" feature, where you can turn a simple text prompt into a fully functional, deployed web application in minutes.

Read more →

Top comments (7)
Subscribe
Submit
Preview
 
 
Onizuka
•
Sep 17

The hybrid switching architecture is the right call here — I ran a similar local/cloud split on a Pi project last year and the latency difference was brutal: 80ms local vs 600-900ms round-trip to the cloud for trivial queries. Routing "what time is it" through an API every time would've burned real money for zero value. Curious what your fallback behavior looks like when the cloud side times out or the gateway PC sleeps — does it degrade to local-only silently, or does the dino just... sit there?

1
 like
Like
Reply
 
 
Zira
•
Sep 16

The local/cloud split is a useful boundary, especially because the engine change is visible to the person using the robot. One detail I would add before treating the workflow as robust is a request-level state contract: record the selected engine, model version, cancellation state, and audio-playback state for each turn. If the Pi loses Wi-Fi after cloud escalation, the UI should distinguish a failed cloud request from a local fallback answer so it cannot produce stale or duplicate speech. Also, no camera does not automatically mean voice data stays local, so an explicit retention boundary for transcripts and audio would make the privacy claim easier to reason about. The physical cancel button plus the FSM looks like a good place to test those transitions.

1
 like
Like
Reply
 
 
Latrisha
•
Sep 23

This is such a fun example of combining AI with physical hardware. The hybrid local/cloud architecture is especially interesting because it gives the robot a useful balance between privacy, latency, and more advanced reasoning when needed. I also really like the FSM approach for coordinating the display, audio, and motor behavior—it makes the project feel much more like an actual companion than just a Raspberry Pi running an LLM.

I've been exploring similar AI and developer projects on Codecan.net, and projects like DinoDesk are a great reminder that there are still plenty of creative ways to bring AI beyond the browser.

1
 like
Like
Reply
 
 
Fayaz 
•
Sep 16

That's cute! 🥰

1
 like
Like
Reply
 
 
UnitBuilds
•
Sep 16

That's cool! you can likely use a little whisper, with gemini cloud backup, given that it's 8 bit, you dont really have to worry much about audio quality, would be good if you implement it so if you say 'sorry, I didnt get that', that it switches to high quality audio from the cloud model, that way if it's simple, gemma does the job, if you need clarity, you have the most capable voice AI as your backup. Pretty cheap too

1
 like
Like
Reply
 
 
Khawaja Khurram (MAK)
•
Sep 20

I am on "Day One", working to go beyond "One Day"

1
 like
Like
Reply

Some comments may only be visible to logged-in visitors. Sign in to view all comments.

Code of Conduct • Report abuse
