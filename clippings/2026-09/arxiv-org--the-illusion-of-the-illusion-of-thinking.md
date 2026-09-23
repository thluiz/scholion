---
url: "https://arxiv.org/html/2506.09250v1"
captured_at: "2026-09-23T18:12:05+01:00"
title: "The Illusion of the Illusion of Thinking — A Comment on Shojaee et al. (2025)"
domain: "arxiv.org"
---
The Illusion of the Illusion of Thinking
A Comment on Shojaee et al. (2025)
C. Opus
†Anthropic
A. Lawsen
†Open Philanthropy
June 10, 2025
Abstract

Shojaee et al. (2025) report that Large Reasoning Models (LRMs) exhibit ”accuracy collapse” on planning puzzles beyond certain complexity thresholds. We demonstrate that their findings primarily reflect experimental design limitations rather than fundamental reasoning failures. Our analysis reveals three critical issues: (1) Tower of Hanoi experiments systematically exceed model output token limits at reported failure points, with models explicitly acknowledging these constraints in their outputs; (2) The authors' automated evaluation framework fails to distinguish between reasoning failures and practical constraints, leading to misclassification of model capabilities; (3) Most concerningly, their River Crossing benchmarks include mathematically impossible instances for N≥6 due to insufficient boat capacity, yet models are scored as failures for not solving these unsolvable problems. When we control for these experimental artifacts, by requesting generating functions instead of exhaustive move lists, preliminary experiments across multiple models indicate high accuracy on Tower of Hanoi instances previously reported as complete failures. These findings highlight the importance of careful experimental design when evaluating AI reasoning capabilities.

1Introduction

Shojaee et al. (2025) claim to have identified fundamental limitations in Large Reasoning Models through systematic evaluation on planning puzzles. Their central finding—that model accuracy ”collapses” to zero beyond certain complexity thresholds—has significant implications for AI reasoning research. However, our analysis reveals that these apparent failures stem from experimental design choices rather than inherent model limitations.

2Models Recognize Output Constraints

A critical observation overlooked in the original study: models actively recognize when they approach output limits. A recent replication by @scaling01 on Twitter [2] captured model outputs explicitly stating ”The pattern continues, but to avoid making this too long, I'll stop here” when solving Tower of Hanoi problems. This demonstrates that models understand the solution pattern but choose to truncate output due to practical constraints.

This mischaracterization of model behavior as ”reasoning collapse” reflects a broader issue with automated evaluation systems that fail to account for model awareness and decision-making. When evaluation frameworks cannot distinguish between ”cannot solve” and ”choose not to enumerate exhaustively,” they risk drawing incorrect conclusions about fundamental capabilities.

2.1Consequences of Rigid Evaluation

Such evaluation limitations can lead to other analytical errors. Consider the following statistical argument: if we grade Tower of Hanoi solutions character-by-character without allowing for error correction, the probability of perfect execution becomes:

	P(all correct)=p^T		(1)

where p is per-token accuracy and T is total tokens. For T=10,000 tokens:

• p=0.9999: P(success)<37%

• p=0.999: P(success)<0.005%

This type of ”statistical inevitability” argument has in fact been put forward in the literature as a fundamental limitation of LLM scaling [3], yet it assumes models cannot recognize and adapt to their own limitations, an assumption contradicted by the evidence above.

3The Impossible Puzzle Problem

The evaluation issues compound dramatically in the River Crossing experiments. Shojaee et al. test instances with N≥6 actors/agents using boat capacity b=3. However, it is a well-established result [4] that the Missionaries-Cannibals puzzle (and its variants) has no solution for N>5 with b=3.

By automatically scoring these impossible instances as failures, the authors inadvertently demonstrate the hazards of purely programmatic evaluation. Models receive zero scores not for reasoning failures, but for correctly recognizing unsolvable problems—equivalent to penalizing a SAT solver for returning ”unsatisfiable” on an unsatisfiable formula.

4Physical Token Limits Drive Apparent Collapse

Returning to the Tower of Hanoi analysis, we can quantify the relationship between problem size and token requirements. The authors' evaluation format requires outputting the full sequence of moves at each step, leading to quadratic token growth. If approximately 5 tokens are needed per move in the sequence:

	T(N)≈5(2^N−1)^2+C		(2)

Given the token budgets allocated (64,000 for Claude-3.7-Sonnet and DeepSeek-R1, 100,000 for o3-mini), maximum solvable sizes are:

	N_max≈⌊log2(L_max/5)⌋		(3)

		≈{7−8	Claude-3.7, DeepSeek-R1

8	o3-mini		(4)

The reported ”collapse” beyond these sizes is consistent with these constraints.

5Alternative Representations Restore Performance

To test whether the failures reflect reasoning limitations or format constraints, we conducted preliminary testing of the same models on Tower of Hanoi N=15 using a different representation:

Prompt: "Solve Tower of Hanoi with 15 disks. Output a Lua
         function that prints the solution when called."


Results: Very high accuracy across tested models (Claude-3.7-Sonnet, Claude Opus 4, OpenAI o3, Google Gemini 2.5), completing in under 5,000 tokens.1

The generated solutions correctly implement the recursive algorithm, demonstrating intact reasoning capabilities when freed from exhaustive enumeration requirements.

6Reevaluating Complexity Claims

The authors use ”compositional depth” (minimum moves) as their complexity metric, but this conflates mechanical execution with problem-solving difficulty:

Puzzle	Solution Length	Branching Factor	Search Required
Tower of Hanoi	2^N−1	1	No
River Crossing	∼4N	>4	Yes (NP-hard)
Blocks World	∼2N	O(N^2)	Yes (PSPACE)
Table 1:Problem complexity is not determined by solution length alone

Tower of Hanoi, despite requiring exponentially many moves, has a trivial O(1) decision process per move. River Crossing, with far fewer moves, requires complex constraint satisfaction and search. This explains why models might execute 100+ Hanoi moves while failing on 5-move River Crossing problems.

7Conclusion

Shojaee et al.'s results demonstrate that models cannot output more tokens than their context limits allow, that programmatic evaluation can miss both model capabilities and puzzle impossibilities, and that solution length poorly predicts problem difficulty. These are valuable engineering insights, but they do not support claims about fundamental reasoning limitations.

Future work should:

1.

Design evaluations that distinguish between reasoning capability and output constraints

2.

Verify puzzle solvability before evaluating model performance

3.

Use complexity metrics that reflect computational difficulty, not just solution length

4.

Consider multiple solution representations to separate algorithmic understanding from execution

The question isn't whether LRMs can reason, but whether our evaluations can distinguish reasoning from typing.

Acknowledgments

We thank Ryan Greenblatt, o3, Gemini 2.5, and all of the people who pointed out the parentheses mismatch in an earlier draft for helpful comments.

References
[1]
Shojaee, P., Mirzadeh, I., Alizadeh, K., et al. (2025). The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity. arXiv:2501.12948.
[2]
@scaling01. (2025). Twitter thread on LRM replication. https://x.com/scaling01/status/1931817022926839909/photo/1
[3]
Dziri, N., Lu, X., Sclar, M., et al. (2023). Faith and fate: Limits of transformers on compositionality. Advances in Neural Information Processing Systems, 36.
[4]
Efimova, E. A. (2018). River Crossing Problems: Algebraic Approach. arXiv:1802.09369.
