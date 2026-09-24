---
url: "https://dev.to/mikeyoung44/llms-will-lie-forever-3jd9?context=digest"
captured_at: "2026-09-25T00:37:49+01:00"
title: "LLMs will lie forever"
domain: "dev-to"
---

Can we ever really trust AI? As LLMs become more advanced, they still face a major issue: hallucinations—when they produce false or nonsensical information. A recent paper argues that this problem isn’t a temporary glitch, but a permanent feature of how AI works. If true, this could and probably _should_ change how we approach AI in the future.

**_By the way, you can check out a short video summary of this paper and many others on the_** [**_new Youtube channel_**](https://youtube.com/shorts/S8cBORGmFn8?feature=share)**_!_**

## [](#overview)Overview

The paper, titled "[LLMs Will Always Hallucinate, and We Need to Live With This,](https://www.aimodels.fyi/papers/arxiv/llms-will-always-hallucinate-we-need-to?utm_source=devto&utm_medium=referral)" makes a bold claim: hallucinations in AI are inevitable because of the way these systems are built. The authors argue that no matter how much we improve AI—whether through better design, more data, or smarter fact-checking—there will always be some level of hallucination.

Their argument is grounded in mathematical theory. By using ideas from computational theory and Gödel's Incompleteness Theorem, they show that certain limitations are unavoidable. If they’re right, we’ll have to rethink our goals for AI systems, especially when it comes to making them completely reliable.

The paper builds its case through a series of mathematical proofs, each explaining a different reason why hallucinations are baked into the nature of LLMs. It ends by discussing the real-world consequences of this, both practically and ethically.

## [](#simple-explanation)Simple Explanation

One way to think of how LLMs work is that they’re like basically playing a game where you’re asked to describe a picture, but you can only see parts of it. Sometimes, you can guess what’s missing, but other times you’ll get it wrong because you don’t have the whole image and there’s something unexpected in the obscured parts. That’s what AI hallucinations are: the system is filling in gaps, but it doesn’t always guess correctly.

The authors of the paper argue that this isn’t a sign of imperfect technology but instead it’s how AI operates at a fundamental level. No matter how much we tweak or improve these systems, they can never know everything perfectly. And even if they had access to all the data in the world, there are still deep mathematical reasons why they can’t always retrieve the right information.

The main takeaway is that instead of trying to make AI perfect, we should accept its flaws and focus on how to manage them effectively.

## [](#technical-explanation)Technical Explanation

The authors of the paper rely on mathematical proofs to explain why hallucinations are inevitable in large language models. First, they show that training data can never be complete, drawing on Gödel-like statements to demonstrate that no dataset can contain all facts. This means that hallucinations are unavoidable because of incomplete information.

Next, they explore information retrieval by comparing it to a well-known problem in computational theory, the [Acceptance Problem](https://people.computing.clemson.edu/~goddard/handouts/cpsc3500/MATERIAL/14b9-11.pdf), which is undecidable. In short, this means that AI models can’t be expected to retrieve the correct information 100% of the time. They apply the same reasoning to the issue of understanding user intent, concluding that it’s equally undecidable for AI systems to perfectly interpret what someone is asking.

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fsubstackcdn.com%2Fimage%2Ffetch%2Fw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep%2Fhttps%253A%252F%252Fsubstack-post-media.s3.amazonaws.com%252Fpublic%252Fimages%252F19f1c09d-ea48-4f1a-86ec-42c3077ce956_964x394.png%2520align%3D)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fsubstackcdn.com%2Fimage%2Ffetch%2Fw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep%2Fhttps%253A%252F%252Fsubstack-post-media.s3.amazonaws.com%252Fpublic%252Fimages%252F19f1c09d-ea48-4f1a-86ec-42c3077ce956_964x394.png%2520align%3D)

Finally, they examine the process of generating language itself. By proving that the [Halting Problem](https://en.wikipedia.org/wiki/Halting_problem)—determining when a process will finish—is undecidable for LLMs, they argue that AI systems can’t predict in advance what they will say. This opens the door for hallucinations.

The paper also shows that no fact-checking system can correct all hallucinations. Even a perfect fact-checker would still be unable to solve the underlying computational problems that cause hallucinations in the first place.

## [](#critical-analysis)Critical Analysis

While the paper presents strong mathematical evidence, some points need further exploration.

For one, the paper uses a broad definition of “hallucination.” The paper seems to suggest that any deviation from perfect knowledge is a hallucination, but in practical terms, many AI systems function well even with some margin for error. For many applications, “good enough” might suffice, even if hallucinations still happen occasionally.

Also, while the paper focuses on deterministic outcomes, modern AI systems operate probabilistically, which might mean the conclusions about undecidability don’t entirely apply. Even if perfect behavior is unreachable, it’s possible to reduce hallucinations to a level where they’re practically unnoticeable.

The paper could also benefit from more empirical evidence. Testing these ideas in real-world AI models would strengthen the argument. Additionally, the discussion is mostly centered on transformer-based models, leaving open the question of whether these limitations apply to other AI architectures as well.

Finally, the paper doesn’t address how humans deal with incomplete information and mistakes in their own thinking. Comparing AI hallucinations with human error could add a valuable perspective.

## [](#conclusion)Conclusion

If the paper’s conclusions hold true, we may need to rethink how we develop and use AI systems. Instead of aiming for perfection, we should focus on managing and minimizing the effects of hallucinations. We should also work on improving AI literacy so users understand these systems' limitations. Additionally, designing AI applications that can tolerate occasional mistakes could be the best way forward.

I think this research raises important questions. A few that come to mind…

*   How can we measure and reduce the real-world impact of hallucinations?
    
*   Are there new AI architectures that might avoid some of these problems?
    
*   How should regulations and ethical standards adapt to account for the fact that AI will always have flaws?
    

I’d love to hear your thoughts on this. Do you find the mathematical arguments convincing? How do you think this will affect the future of LLMs and, specifically, how we think about reliability? [Let me know in the Discord](https://discord.gg/Ae9nY5sdtC).

If you found this analysis useful, consider subscribing for more breakdowns of AI/ML research. And feel free to share this post with others interested in these kinds big questions about AI’s future. Thanks for reading!
