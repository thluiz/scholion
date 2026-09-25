---
title: "More Testing Tips With C#"
date: '2026-09-25T08:48:53+01:00'
category: webclip
summary: 'The post shares testing tips for C#: generating fake data with Faker.NET or Bogus.NET, using seeds to reproduce randomized tests, comparing output against reference files, and finding free ports or loopback IPs for integration tests.'
tags: ["csharp","testing","bogus-net","faker-net"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "More Testing Tips With C#"
    url: "https://gamlor.info/posts-output/2024-12-11-csharp-testing-stuff/en/?utm_source=newsletter.csharpdigest.net&utm_medium=newsletter&utm_campaign=the-impact-of-locks-and-waits-on-latency&_bhlid=c6a32769d7d59536ee2ffdf5867fbd7fbe6a953b"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/gamlor-info--more-testing-tips-with-csharp.md"
    kind: repo
---

The post gathers a few C# testing tips around test data, reference outputs, and integration-test setup. It says test data generators help when hand-written data gets tedious, seeds make randomized tests reproducible, and reference files work well for stable rendering output.

It also shows how to find a free TCP port with `Socket`, and notes that the whole `127.0.0.0/8` loopback range can be used when a fixed port is required. ## Reading notes

- In tests, data generators help when creating examples by hand becomes tedious and the data ends up unrealistic.
- The text presents `Faker` as an option that produces data in English and more “human” data, without focusing on edge cases.
- `Bogus.NET` is shown as a broader library, with test object factories, support for multiple locales, and additional data sets.
- When using random data in tests, the text recommends controlling the seed so that a failure can be reproduced with the same data set.
- The seed can be set globally in `Bogus.Randomizer.Seed` or per instance with `UseSeed`.
- This style of testing is described as a simple form of property-based testing, because it generates random data and checks whether a system property holds.
- Another technique is to save a good reference of the result and compare it with the current output, which works well for rendering code such as HTML, images, or SVG.
- When the test fails in this model, the text suggests inspecting the differences and, if the change is expected, copying the files from `current` to `reference` and committing.
- For integration tests, the text shows how to discover a free TCP port using `Socket` bound to `127.0.0.1:0`.
- If a fixed port is required, the text says the `127.0.0.0/8` range belongs to the local machine and allows using many loopback IPs, such as `127.0.0.2` and `127.0.0.3`, on the same port.
