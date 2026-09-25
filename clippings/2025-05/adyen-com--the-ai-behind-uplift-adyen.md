---
url: "https://www.adyen.com/knowledge-hub/the-ai-behind-uplift"
captured_at: "2025-05-08T08:47:12-03:00"
title: "The AI behind Uplift - Adyen"
domain: "adyen-com"
---

---
### Connected holistic decisioning

One of the most head-scratching decisions is connecting a collection of unaware machine learning models to a common goal. The current version of Uplift uses message passing, which provides a simple but efficient approach to create awareness that models can condition their estimates on and thus converge closer to a global optimum. 

We have tried with bigger artifacts and complex deep learning models that can combine multiple decisions, and we have found that they would often compromise the engineering requirements (latency, uptime) of online deployments in a critical flow. We do however keep on investigating this line of thinking as well as pushing what is possible in engineering terms and we are expecting to move the whole pipeline to deep learning architectures in the short future (see below).

We are doing active research in this area: we have funded a full PhD position with UVA’s AMLAB to help us work out this problem from a Reinforcement Learning perspective. We have already shared some work with the community in this direction in this [conference talk](https://www.youtube.com/watch?v=PpFu-qa3oVg). 

### Off-policy Evaluation

Running AB Tests is expensive in terms of time and money. If you field a bad variant it costs money and the amount of traffic it takes to reach significance can take a long time. Also you have an upper-bound on the number of experiments you can run in a year potentially delaying the discovery of a winning variant and realizing lost revenue. Additionally, it takes operational and cognitive load as well as simply “sacrificing” the traffic split to test a hypothesis. Also in mature product orgs, AB tests often come back flat or insignificant resulting in wasted time.

For that purpose, we have done research on Off-Policy Evaluation that allows us to essentially run offline AB Tests. New variants can be tested instantly w/ high correlation (+80%) to On-policy Estimates (actual AB Tests). This has saved us an estimated 20 weeks/year of time wasted on flat AB tests and an incremental 9-54 million transactions over a six-month period.

This research has been submitted to RecSys ’25, and a preprint is available on [arXiv](https://arxiv.org/abs/2501.10470).

### Counter-factuals and Causal Inference

At our scale, understanding the causes that drive the results of an experiment is more of a need than an interest, as it would allow us to detect systemic sources of entropy that we could avoid in the future.

On the same wavelength, once we apply a decision on a transaction (e.g. block it for fraud likelihood) we do not have access to the outcome if we wouldn’t have acted on it. In statistical terms, this is called a counterfactual. To learn the full distribution of the traffic then you would then need not to act on the traffic, beating the point of the system. 

Control groups, randomization and exploration traffic help with that but diving in disciplines like Causal Inference allows us to better understand the underlying reasons of the experiments’ outcomes as well as bypassing counterfactuals. 

We’re also investing in research in the field by funding another PhD position with UvA’s AMLAB to work on causal inference for datasets like ours at our scale. Researchers working on their PhD have the purpose of pushing research boundaries and publishing papers while they can team up with Adyen’s engineering team to implement and test hypotheses. As an example, we are working on a transaction simulator with Generative AI that would generalize over distributions, counterfactuals and PII information and would allow us to benchmark algorithms and techniques before running experiments with real traffic splits.

### Weak Supervision

Labels are hard for two reasons: quantity and quality. Given our data size, we have enough labels to train models and thus we could use balancing techniques such as downsampling and still get enough data to train our models.

However, we are leaving some predictive power behind as labels normally come later, don’t come or come in incomplete. To solve this we have been engaging in research around Weak Supervision. The premise of Weak Supervision is that the modeling process benefits more from a larger quantity of data, even if it is noisy, than from a smaller amount of high-quality data. More precisely, for a fixed quantity of high-quality data, adding noisy data can be more beneficial.  Weak Supervision feeds into the “Adyen’s Data Flywheel” that combines efforts on increasing label quality and quantity together with Active Learning (future work, see below). Using Weak Supervision in production we have increased recall by +22%, reduced auth rate loss by -46%, and achieved a +13% issuer refusal rate gain by improving fraud detection efficiency.

### Non-uniform Random Exploration for Contextual Bandits

When running an experiment in real time with real traffic over a RL system one faces the dilemma of executing the action that provides the best reward, based on the knowledge up to that point (exploitation), and also ensuring that this knowledge is still valid and you are not blindly executing in old truth (exploration).

The simplest technique that one can adopt is called epsilon-greedy, where a random traffic split of epsilon percent is allocated to explore (typically by choosing a suboptimal action from the available action space). There are several research avenues on choosing the best next action that would allow you to keep exploring while maintaining a suboptimal but competitive baseline in the exploration. We have been researching and deploying platform-wide experiments with several techniques and we have found significance in techniques around Regression Oracles. 

This research has been submitted to WWW ’25, and a preprint is available on arxiv: [\[2412.00569\] Contextual Bandits in Payment Processing: Non-uniform Exploration and Supervised Learning at Adyen](https://arxiv.org/abs/2412.00569).

### Deep Learning & Ensembling

It is one of our cultural tenets to strive for simplicity and to create solutions to problems,not problems for the solutions we want to use. As such, classical ML algorithms such as boosted trees still provide a strong baseline for the majority of classification and regression problems whose input is structured data and have constituted, and sometimes still do, our principal baselines. We have run, and are running, experiments (see experimentation engine) where we deploy complex Heterogeneous Ensembles of Neural Networks for online scoring in payment flow and have not only achieved performance parity with boosting baselines but also surpassed them, with performance improvements that justify the delta in operational load and complexity.

**Note**: strictly speaking, using Generative AI (i.e. an LLM) is not a technology that would help solve this problem. However, we have taken inspiration in our work from companies like Hyperplane (great product, great team) who have created offline models through bigger networks based on the Transformer architecture removing the need for explicit feature design (next point). 

### Transformer architectures

We are experimenting with leveraging Unsupervised Pretraining and Transformers to unlock the full scale of our data and incorporate the correct inductive biases in our modeling process.

On top of our efforts to utilize more data such as weak supervision or active learning, we are also thinking of approaches to change the supervised paradigm completely and allow us to unlock the full potential of our data. Inspired by recent breakthroughs in Self-Supervision applied to language modeling, we are applying the same patterns of Unsupervised Pretraining to payments data. By inferring labels from the structure of the data itself, we can achieve human-free supervision and unlock the full potential of our datasets.

Just like sentences are sequences of words, shoppers are sequences of transactions – this is the core data structure of Adyen: shopper transactions sequences. Traditional approaches to modeling often ignore this assumption and model sequences independently or attempt to model the assumption with workarounds like point-in-time shopper aggregations, however the Transformer architecture allows us to offer an alternative approach to extract the predictive power of these structures. 

Therefore, Transformers and Self-supervision are enabling us to build a foundational payments model trained on billions of transactions, allowing us to bootstrap any modeling process with unparalleled scale. Through downstream fine-tuning and entity embeddings, we are enhancing shopper insights, improving fraud detection, and opening up new research opportunities like synthetic data generation.

### Observability

Once the models are deployed and quantified through an experiment we constantly run diagnostics to ensure the performance stays in place. We run classic drift detection (classically under the umbrella of MLOps) as well as more complex algorithms to detect business performance drifts and biases such as combinations of MIST (Multiple Irregular Seasonalities and Trend decomposition) and DTW (Dynamic Time Warping) algorithms. We covered [these aspects in PyData 2024.](https://www.youtube.com/watch?v=NGgVDd2o5i0)

### Fairness and explainability

Inherently to delegating decisions to the machine there come challenges around ensuring that these decisions do not come with biases that can segment demographics or be considered unfair from a human perspective.

For this we have established an internal working group of technical and legal experts to be on top of regulation, including GDPR and the AI act, and we have made procedural changes to ensure that Adyen stays close to its cultural ethos: a highly ethical company. All products and models need to be evaluated for biases and screened for ways where they could violate handbooks and regulations. Once the workgroup has approved we monitor through observability tooling that certain sensitive features do not overfit.

All decisions taken by AI are meant to be explained. For this every inference call is recorded and algorithms that reason around the underlying reasons are scored (e.g. SHAP values). The UI of Adyen Uplift offers an explanation on every decision per transaction.
