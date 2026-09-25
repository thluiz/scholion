---
title: "How Adyen does AI"
date: '2025-05-08T08:46:59-03:00'
category: webclip
summary: 'Adyen says it uses ML on every transaction for fraud, authentication, routing, and conversion, while its GenAI work focuses on support, human-in-the-loop workflows, and open-source models hosted in-house.'
tags: ["machine-learning", "fraud-detection", "genai", "open-source"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How Adyen does AI - Adyen"
    url: "https://www.adyen.com/knowledge-hub/how-adyen-does-ai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-05/adyen-com--how-adyen-does-ai.md"
    kind: repo
---

Adyen says it has invested heavily in ML and AI talent and infrastructure, and that these systems already affect core business flows. Its approach combines real-time decisioning on every transaction, risk monitoring with transaction and KYC data, and newer GenAI work for operational support.

## Reading notes

- Every transaction is processed with ML inference in real time on Adyen’s self-hosted big data platform.
- The company says it uses supervised, semi-supervised, and reinforcement learning to combat fraud, authenticate users, and improve payment completion.
- Adyen runs A/B/n testing with control groups and retrains or redeploys models on demand or on a weekly cadence.
- Its risk engine uses transaction and KYC data to monitor activity and detect behavioral patterns during onboarding and purchase.
- Detection methods include graph structures, graph neural networks, and deep neural networks.
- For checkout, fraud, authentication, authorisation, routing, and retry, the article describes a sequential ML setup with different models for different steps.
- Adyen says merchant rules can complement ML models, including policy rules and other rules for patterns not yet learned by the models.
- The company says it is researching ways to make decisions across the full funnel and combine fraud, conversion, and cost in one payment flow.
- It is also funding research with the University of Amsterdam’s AMLAB on causal inference and off-policy evaluation.
- Adyen describes its platform data as mostly structured and relational, with graph modeling used to capture deeper connections between entities.
- With banking licenses and financial services, the graph becomes larger and more directed, with more node types and more edges.
- The article says this leads to research on graph databases, sampling, graph features, and Graph Neural Networks for complex pattern detection.
- On GenAI, Adyen says it uses open-source foundational models hosted and fine-tuned in-house, and contributes back to the open-source community.
- GenAI work is focused on customer support and operations, especially ticket routing, summarisation, and context augmentation with RAG.
- The company says human-in-the-loop workflows are deliberate for privacy, security, and quality reasons.
- Adyen says LLM-based routing did not outperform a simpler TF IDF classifier in its use case.
- The GenAI stack is deployed on-prem on Adyen’s data clusters with GPUs, and is also made available internally to employees.
- The article closes by saying Adyen is exploring future topics such as hallucinations, synthetic data, self-alignment, and transformer-based architectures for mixed structured and unstructured data.
