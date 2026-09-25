---
title: "The AI behind Uplift"
date: '2025-05-08T08:47:12-03:00'
category: webclip
summary: 'Adyen describes the AI stack behind Uplift, from connected decisioning and offline evaluation to weak supervision, transformers, observability, fairness, and explainability in payment flow models.'
tags: ["machine-learning", "payments", "fairness", "explainability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The AI behind Uplift - Adyen"
    url: "https://www.adyen.com/knowledge-hub/the-ai-behind-uplift"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-05/adyen-com--the-ai-behind-uplift-adyen.md"
    kind: repo
---

Adyen presents Uplift as a system built around connected decisioning, offline evaluation, weak supervision, exploration strategies, deep learning, transformers, observability, and fairness checks. The text ties these methods to payment processing, fraud detection, and experimentation at scale.

## Reading notes

- Uplift uses message passing so separate machine learning models can condition their estimates on a shared goal and move closer to a global optimum.
- The team has tested larger deep learning artifacts, but online deployments in critical flows can suffer from latency and uptime requirements.
- Adyen funds research with UVA’s AMLAB on reinforcement learning and causal inference, including PhD positions and shared conference work.
- Off-policy evaluation is used to test new variants offline, with reported high correlation to on-policy estimates and savings in time and transactions.
- The text links counterfactual analysis to experiment outcomes and to cases where Adyen cannot observe what would have happened without an intervention.
- Weak supervision is presented as useful when labels arrive late, are missing, or are incomplete, and as a way to improve recall and fraud detection results.
- For contextual bandits, Adyen compares epsilon-greedy exploration with other techniques and says it found value in regression oracles.
- Classical ML baselines such as boosted trees remain important, but heterogeneous neural network ensembles have matched or exceeded them in some online scoring experiments.
- Transformers and unsupervised pretraining are being applied to payments data so the structure of shopper transaction sequences can inform modeling.
- The team uses drift detection and other diagnostics after deployment, including MIST and DTW-based approaches for business performance drift and bias.
- Fairness work includes internal review with technical and legal experts, screening for bias, and monitoring sensitive features after approval.
- Every AI decision is meant to be explainable, with inference calls recorded and methods such as SHAP used to score underlying reasons.
