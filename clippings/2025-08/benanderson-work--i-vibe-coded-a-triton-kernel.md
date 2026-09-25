---
url: "https://benanderson.work/blog/vibe-coded-kernel/?utm_source=tldrai"
captured_at: "2025-08-18T15:24:53+01:00"
title: "I Vibe-Coded a Triton Kernel"
domain: "benanderson-work"
---

---
OpenAI released GPT-OSS around a week ago. While the model's performance appears impressive, the release itself left a lot to be desired, especially when it comes to fine-tuning. The recommended setup with HuggingFace involves de-quantizing MXFP4 weights to BF16 (increasing memory consumption by ~4x), and the bespoke attention algorithm means that Flash Attention and Pytorch SDPA don't work, so a slow and memory-hungry "eager" attention is the only option.

A Triton implementation of the model was included in the [release](https://github.com/openai/gpt-oss), but the kernels are forward-only, so they're no good for training. I decided to see if I could fix that myself. I started with attention, since that forward kernel appears a bit less hairy than the kernel for the MXFP4 MoE.

## Background

Before I describe the approach I took to create the Triton kernel, I thought I should share a bit about my experience writing kernels. Or rather, lack thereof. While I have substantial machine learning knowledge, my kernel expertise basically amounts to skimming 3 chapters of [Programming Massively Parallel Processors](https://www.amazon.com/Programming-Massively-Parallel-Processors-Hands/dp/0323912311/133-9975079-9912066) and walking through 1 or 2 Colab notebooks where you use CUDA to do stuff like transform a picture of a dog to grayscale.

I understand basic concepts like "break the work down into little pieces and then use lots of for loops," and "use guards to make sure you aren't reading memory outside of the chunk you're supposed to." I can't write a tiled matmul, I don't know how to do fancy things with shared memory, I don't know what swizzling is, and I can't read Triton without my eyes glazing over.

Nevertheless, I managed to produce (what appears to be) a correct Triton kernel for GPT-OSS attention. (If it isn't correct, come yell at me on Twitter. Also, I don't know if it's fast, I still need to time it.)

## The Testing Harness

The most important part of writing a kernel, or so I'm told, is making sure it is mathematically correct. Otherwise, your model will just get stupider, faster. It's easy to write something that appears correct, but fails in some weird edge cases. (It's definitely possible that my kernel falls into this category.) So, the first thing to do is write tests.

Of course, I ignored that and just made Cursor CLI spit out a backward kernel, given the existing forward kernel and Pytorch reference implementation. Luckily, the Cursor agent made me some tests without being asked. (Note: I am not a regular Cursor CLI user, I was just trying it because it was new. It seems fine, no complaints.)

Now, I had to figure out if the dang thing was correct. I started out with a notebook. Modal Labs has a cool new [Notebooks product](https://modal.com/docs/guide/notebooks-modal) that gives you a Jupyter-like environment, backed by any container image and GPU you want. Unfortunately, this was a disaster. It turns out that running hundreds of tests produces a lot of console output, and notebooks don't like thousands of lines of console output (Jupyter would have been a disaster too). Woopsy-daisy.

Take two: A regular Modal App for testing, which dynamically loads in the kernel from `attention.py` and the tests from `test_attention.py`, runs them all on an H100, and saves the output locally as JSON. This worked great, 10/10 would recommend to a friend.

## Getting to Green

All the tests failed immediately. Even some tests for the forward, which was direct from OpenAI! I think maybe Cursor (or someone, but not me!) added in some extra weird shapes or offsets in the test cases. The immediate problem was invalid memory accesses. Once again, I do not know Triton or kernels, so I was not able to fix this. But maybe GPT-5, the smartest model ever, could?

My initial policy iteration loop was: (1) Paste failing tests into ChatGPT; (2) Paste new kernel from ChatGPT into IDE; (3) Run the tests again. This gave me at least a little control over what was happening. I could ask annoying questions like "Isn't that going to be slower?" or "Should we change that in the forward too?" This basic loop was able to resolve the simple issues with invalid memory accesses, but Chatty and I eventually got stuck when the math didn't match the PyTorch reference implementation.

At this point, lost and tired of copy-pasting, I decided to give up all control and go full-auto. I booted up Claude Code in the attention repo, with just the following prompt:

> We have a setup here with a triton kernel, and a test harness on Modal you can run with modal run modal\_tests.py -k \[commands to forward to pytest\]. Right now the backward is failing, you can see the command and resulting failure in test\_results.json. Your job is to fix the backward kernel so the failing test passes: `modal run modal_tests.py -k "test_backward_grads_match_reference and num_queries_129 and num_keys_193 and sliding_window_128 and start_q_63"` each run, the results get put in test\_results.json

That's it! Claude appeared to make some progress, but eventually gave up:

> I've investigated the backward kernel failure extensively and made several important fixes to improve the implementation \[...\]:
> 
> -   ✅ Simple cases (without padding) work perfectly with ~1e-6 error
> -   ✅ Key padding alone works fine
> -   ✅ Forward pass works correctly even with complex padding cases
> -   ❌ Backward pass still fails for query padding cases with ~91% mismatched elements

I decided to turn to GPT-5 again, this time fully autonomous, via Codex CLI. I made Claude summarize what it changed and the remaining issues in `BUG.md`, and started GPT-5 on the same improvement/testing loop. It seemed to get stuck at first, and I noticed it's not naturally as "agentic" as Claude; it kept saying it couldn't run tests on Modal and I had to remind it that it could, in fact, just do things. I was feeling hopeless, but then after getting distracted for 5-10 minutes, I looked back at my laptop and all the tests had passed. Cool.

## Conclusion: Recursive Self-Improvement?

If my experience is anything to judge by, the time of [AI automating AI research](https://www.youtube.com/watch?v=htOvH12T7mU) is here! AGI 2027! I have my doubts about this somewhat simplistic narrative, which I might elaborate on in another post. Nevertheless, it was cool to experience firsthand "babysitting" a model to do something I couldn't do myself.

If you want to dissect the code and testing harness for yourself, it's [here](https://github.com/andersonbcdefg/gpt-oss-attention). Tell me why it's stupid and wrong! Also, if you're seriously interested in automating kernel-writing with AI, you should follow my buddy [Lewis](https://x.com/ctjlewis), who has done some really interesting [work](https://kernelbench-evo.vercel.app/) in this space.
