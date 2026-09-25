---
title: "Move fast and don't break (safety critical) things"
date: '2025-08-13T09:31:35+01:00'
category: webclip
summary: 'Boom describes how in-house engineering software, software engineers embedded in hardware teams, and rapid iteration helped the small XB-1 team design and fly a supersonic jet quickly and with less budget.'
tags: ["engineering-software", "hardware-development", "supersonic-aircraft", "iteration"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Move fast and don't break (safety critical) things"
    url: "https://bscholl.substack.com/p/move-fast-and-dont-break-safety-critical?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/bscholl-substack-com--move-fast-dont-break-safety-critical-things.md"
    kind: repo
---

Boom argues that fast hardware development depends on reducing the cost of iteration. The company says it built XB-1 with a small team and a fraction of the usual budget, and that it could have gone faster still if it had known then what it knows now.

## Reading notes

- Boom says its engineering culture is built around iteration and lowering the cost of repeating analysis.
- The company embeds software engineers inside hardware teams and expects hardware engineers to code as well.
- Engineers are expected to “invent together,” with software people learning the hardware domain and hardware people contributing code.
- Boom says it builds software practices like automated unit testing and continuous integration into hardware workflows.
- This approach produced mkBoom, its internal airplane design software.
- mkBoom automates aircraft-level analysis for weights, propulsion, and aerodynamics.
- Engineers can define an airplane parametrically in a configuration file and run a quick analysis in minutes.
- Overnight runs provide higher-fidelity simulations.
- Boom says this lets small teams evaluate many more designs and find better ones.
- The article gives an example from Overture passenger experience, where a cabin concept required fuselage changes that initially appeared to cost 1,000 miles of range.
- Boom used joint simulation of Overture and the Symphony engine inside mkBoom to search engine and airplane design options together.
- After evaluating multiple engine variants, Boom says it found a better design in two weeks.
- The chosen changes recovered more than 1,000 miles of range and preserved acoustic margin for quiet takeoff and landing.
- Boom connects those changes to Boomless Cruise on Overture.
- The article ends by saying better tools reduce repetitive work and help the company build small teams it can hire selectively into.
