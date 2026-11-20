---
title: "Comparative Study of WebRTC SFUs for Video Conferencing"
date: '2020-04-20T21:22:27+00:00'
category: webclip
summary: 'Paper presents a KITE-based load-testing method to compare four open-source WebRTC SFUs for video conferencing, detailing setup, metrics and observed scalability, bitrate, latency and quality results.'
tags: ["webrtc", "media-server", "load-testing", "sfu"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Comparative Study of WebRTC Open Source SFUs for Video Conferencing"
    url: "https://uploads-ssl.webflow.com/5c6853c495409838d874a0d2/5cbed66cae2b88609106befa_IPTComm_2018_LoadTesting-12%5B23229%5D.pdf"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/uploads-ssl-webflow-com--comparative-study-webrtc-sfus-video-conf.md"
    kind: repo
---

The paper describes a comparative load-testing study of four open-source WebRTC SFUs (Jitsi, Janus, Medooze, Kurento/OpenVidu) in a video conferencing scenario using the KITE interoperability test engine. It reviews prior dedicated and generic WebRTC testing tools, then details a unified AWS-based setup, client modifications, controlled media, and metrics collection (getStats, video activity checks, image-based quality scoring) to run identical scenarios across SFUs. Results cover success/failure rates, bitrate behavior, RTT and objective video quality as load grows, with Medooze generally performing best under the tested conditions and Jitsi, Janus, and OpenVidu showing distinct limitations.

## Reading notes

- WebRTC applications now commonly go beyond one-to-one peer-to-peer and typically rely on at least one media server.
- Traditional interoperability with VoIP, PSTN and RTMP requires mixing capabilities and motivates MCU architectures, while newer servers often adopt SFU designs that reduce server CPU use and enable simulcast and SVC-based adaptation.
- Even restricting to SFU-implementable scenarios, key use cases include many-to-many video conferencing and one-to-many streaming/broadcasting.
- Existing server-specific tools (e.g., Jitsi-Hammer for Jitsi Videobridge, Janus’s internal tools and Jattack, Red5’s adapted RTMP load tool) hinder cross-server comparison because they assume particular signaling or use cases.
- WebRTCBench focuses on P2P connection and call performance and does not test media servers, and has not been maintained since 2015.
- Other frameworks such as WebRTC-test target specific platforms (e.g., RestComm) rather than generic SFU comparisons.
- Generic WebRTC testing efforts like Kurento Test Framework/ElasTest and KITE aim to be agnostic to OS, browser, application, network, signaling and media server.
- Kurento’s KTF, based on Selenium/WebDriver, combined load, quality, performance and functional testing but mainly reported results for a single streaming/broadcasting configuration using Kurento Media Server.
- Extensions to KTF added network instrumentation and mobile-device testing via Appium, but still centered on KMS and relied partly on fake WebRTC clients.
- KITE was developed around WebRTC 1.0 compliance testing, running large cross-browser suites daily and publishing results on webrtc.org.
- For WebRTC 1.0 simulcast testing, KITE needed an SFU, so tests were run against several well-known open-source SFUs, laying groundwork for generic SFU testing.
- Based on these capabilities, the authors chose KITE over KTF to conduct comparative SFU load tests for video conferencing in a single-server configuration.
- Tests were executed on AWS EC2 using separate VMs for each SFU and its clients, all within the same VPC to reduce network variability.
- Media server VMs used c4.4xlarge instances, while client VMs used c4.xlarge, providing dedicated compute capacity and specified RAM and bandwidth per Table I.
- Four SFUs were installed from latest public sources (or Docker for Kurento/OpenVidu) with default settings: Jitsi Meet (JVB 0.1.1043), Janus 0.4.3, Medooze 0.32.0, and Kurento/OpenVidu (KMS 6.7.0).
- Server-side bitrate caps differed: OpenVidu min/max at 600 kbps, Jitsi at 650 kbps, Janus and Medooze at 1.7 Mbps; these defaults were left unchanged.
- Client web apps were modified to allow up to 40 participants per room, multiple rooms via URL parameters, higher client-side send bitrate caps (up to 5 Mbps when configurable), uniform video layout (up to 9 streams at 540x360), and exposure of RTCPeerConnection objects for stats.
- Overlays in the client UI were rearranged so that textual elements sit above video regions, preserving clean video areas for quality analysis.
- Each client app ran on its own VM with sufficient resources for one send and six receive streams; Chrome 67 was driven by Selenium through a central hub managed by KITE.
- The Janus Video Room web client was adapted to show one self-view and six remote videos in a fixed arrangement and resolution, and to display identifiers and bitrates above, not over, the videos.
- Controlled media inputs used Chrome’s fake device flags, with all clients sending the same preprocessed Y4M video and WAV audio, preserving 540x360 resolution and 30 fps, plus frame/time overlays.
- Chrome was launched with a fixed window size large enough (1980x1280) to display seven 540x360 videos simultaneously.
- Client-side metrics used getStats to compute send/receive bitrates based on bytesReceived/bytesSent and timestamps, sampled twice during ramp-up and eight times at target load.
- A custom JS routine checked whether each HTML video element was active by summing pixel values twice at a 500 ms interval, flagging black (sum zero) or frozen (no change) frames as failures.
- Video quality was assessed from Selenium screenshots using BRISQUE features, contrast, CPBD, edge detectors, blur and HOG; these features fed a neural network trained on the IRCCyN IVC 1080i dataset to produce 0–100 quality scores.
- Test orchestration used KITE in Java with Selenium WebDriver: KITE spawned client VMs, then filled rooms in each SFU by launching Chrome, loading the app, and verifying self and remote videos.
- During room filling, getStats was sampled and screenshots taken as part of a “Measure and probe” phase, then repeated more extensively once the room reached full load.
- Pre-runs showed SFUs could not all sustain the same number of rooms, so final targets were adjusted: Jitsi 70 rooms (490 clients), Medooze 70 rooms, Janus 35 rooms, OpenVidu 20 rooms.
- OpenVidu was limited because it often failed before 20 rooms; Janus’s target was set where receive bitrates dropped below about 10 kbps after around 25 rooms.
- Each full load test per SFU was run at least twice to confirm result consistency.
- Quantitative results distinguished between page load success, sender video presence, and all-remote-videos checks, with no failures observed for self-video across SFUs.
- Failure in the “all video check” was defined as any of the six remote streams being missing, black, or frozen.
- Jitsi showed a 79% failure rate on the all-video check, mostly due to still images with zero measured bitrate.
- OpenVidu had a 42% failure rate on remote video checks, with frequent missing one or two videos per client.
- Medooze’s failure rate was 10%, and Janus’s was only 2% on the video check.
- During ramp-up, Medooze reached around 1 Mbps average sender bitrate, close to the controlled input’s encoding; Jitsi and Janus hovered near 500–530 kbps, OpenVidu around 350 kbps.
- Jitsi’s lower send bitrate during ramp-up matched its configured 650 kbps server cap, while Janus’s similar cap but slightly lower average was noted but not fully explained.
- At target load, sender bitrates dropped for all SFUs: OpenVidu decreased about 30% (350 to 250 kbps), Medooze about 80% (1 Mbps to ~215 kbps), Jitsi about 91% (500 to ~45 kbps), Janus about 94.5% (530 to <30 kbps).
- For receive streams during ramp-up, Medooze delivered ~1 Mbps per remote client stream, essentially mirroring sender bitrate for all six peers.
- Janus’s clients received around 440 kbps each versus about 530 kbps from the sender, showing moderate reduction.
- OpenVidu’s clients received about 300 kbps, near its 350 kbps sender bitrate, indicating relatively consistent distribution.
- Jitsi’s clients received only about 125 kbps versus the sender’s ~530 kbps, indicating a substantial reduction per remote stream.
- At target load, average Jitsi receive bitrate collapsed to roughly 435 bps per client stream, far below ramp-up levels and consistent with high rates of blank/still images.
- Janus clients averaged just over 10 kbps at target load, down from ~440 kbps, yet most videos still passed the activity check.
- OpenVidu clients averaged about 120 kbps receive bitrate at target load (down from 300 kbps), while Medooze clients averaged roughly 250 kbps (about a quarter of its ramp-up value).
- During ramp-up, average RTT from getStats remained low for Medooze (~10 ms) and Jitsi (~15 ms), while OpenVidu already showed ~576 ms and Janus over 2.6 seconds.
- At target load, RTTs approximately doubled: Medooze stayed low (~19 ms), Jitsi modest (~37 ms), OpenVidu above one second, and Janus over 6.5 seconds on average.
- Video quality scores over number of participants showed Medooze sustaining high quality up to around 400 participants, with degradation appearing only beyond that.
- Jitsi maintained relatively stable but lower quality scores throughout, up to 500 participants, a behavior attributed partly to simulcast, last-N, and thumbnail layouts lowering effective resolution for measured frames.
- The authors suggest that Jitsi’s advanced features, designed to improve scalability, likely bias quality metrics and would need special handling in future evaluations.
- Janus delivered good quality at low participant counts, but quality deteriorated quickly beyond about 70 participants and was very poor by 200 users.
- OpenVidu’s quality curve fluctuated with load: it dropped early, bottomed around 100 participants, then improved up to about 130 before dropping again as load increased.
- Only Jitsi and Medooze reached the highest tested load of 70 rooms/490 participants without catastrophic failure of the test scenario.
- OpenVidu remained nominally running beyond its 20-room target, but significant video check failures meant clients often missed or froze streams.
- Medooze combined high bitrates and low RTT at both ramp-up and full load, resulting in the best visual quality among the tested SFUs and relatively few video-check failures.
- The authors note that they did not measure server CPU, RAM or NIC usage, so comparative resource efficiency between SFUs under load remains unknown.
- They also remark that once Jitsi’s specific scalability features are factored into a customized quality metric, its perceived quality might be closer to Medooze than raw numbers suggest.
- Jitsi’s main pattern under high load is very low average bitrates, yielding poor quality when video flows, and many blank or frozen streams, as reflected in the 79% failure rate.
- Janus struggled with growing numbers of rooms/peers, with RTTs becoming several seconds and bitrates collapsing, making video quality unacceptable beyond roughly 140 participants.
- OpenVidu was unable to reliably handle more than about 150 participants in this test configuration.
- The study shows KITE can be used for comparative SFU testing and that conducting such tests can uncover bugs and unexpected behaviors across implementations.
- Future work the authors propose includes adding audio-quality metrics, server-side resource probes (CPU, RAM, bandwidth) and exploring parameterized video conferencing scenarios (varying room counts and participants per room).
- They also intend to test other use cases such as broadcasting/streaming and to reproduce existing SFU test results from prior Jitsi, Janus and Kurento research.
