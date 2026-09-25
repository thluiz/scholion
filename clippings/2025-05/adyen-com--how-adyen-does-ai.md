---
url: "https://www.adyen.com/knowledge-hub/how-adyen-does-ai"
captured_at: "2025-05-08T08:46:59-03:00"
title: "How Adyen does AI - Adyen"
domain: "adyen-com"
---

---
## Abstract = TLDR = “ChatGPT summarize the article”

_Adyen has made substantial investments in the past few years in the areas of Machine Learning (ML) and Artificial Intelligence (AI) in talent and infrastructure. These have already proven to have material business impact:_

-   _Every transaction processed by Adyen is driven by ML inference (decisioning) in real time, using models trained and deployed by Adyen on our self-hosted big data platform. We use various techniques including supervised, semi-supervised and reinforcement learning to combat fraud, authenticate users, and maximize successful completion of payments. We continually run A/B/n testing with control groups to optimize for performance. Adyen also invests in research to evaluate offline reinforcement learning policies and detect counterfactuals._
    
-   _Adyen’s risk engine uses vast amounts of transaction and KYC data to monitor transactions, and identify behavioral patterns during shopper onboarding and at the time of purchase. Our detection methods use graph structures, graph neural networks and deep neural networks._
    
-   _More recently, Adyen is making investments in Gen AI in talent, infrastructure and production value. In line with our open source philosophy, we use open-source foundational models that are hosted and fine-tuned in-house. We also make contributions back to the open source community. We have consciously chosen this approach for data privacy and security reasons and first-principle knowledge. In addition, all our GenAI-powered workflows are designed for Human in the Loop. Operational support is already reaping the benefits._
    

## Dictionary

In this article we refer to Machine Learning (ML) as techniques such as supervised learning (random forests, classification, regression, neural networks), unsupervised learning (e.g. clustering, autoencoders, isolation forests), reinforcement learning (e.g. contextual bandits), A/B testing, graph neural networks, and semi-supervised learning. The term Deep Learning refers to neural network architectures with multiple layers and a large number of coefficients, including multilayer perceptrons (MLPs) or convolutional neural networks (CNNs). We use the term GenAI (generative AI) to refer to transformer-based architectures pretrained on unstructured data using self-supervision. We refer to AI (Artificial Intelligence) as an umbrella term covering Machine Learning, Deep Learning and GenAI.

## Understanding Adyen

In our journey to become the financial technology platform of choice for leading companies, Adyen has made and stuck to some unobvious choices compared to other players in the same space. These choices are cemented by our cultural tenets, which provide a reference frame for the implementation choices we have made through the years:

-   **Long-term thinking**: every choice at Adyen is proof-validated against our long-term view. Will it scale 20x? Are we getting a head-start or are we gaining speed in the long term?
    
-   **Control and flexibility**: as a best-in-class fintech we offer reliability and innovation at the same time. Doing one or the other is relatively easy, doing both is extremely difficult. Whenever we are deploying services, storing data or any other choice we always balance control and flexibility to provide reliability (e.g. not depending on external partners for core flows) and capacity to introduce change and innovate.
    
-   **Staying curious and following closely**: Adyen has been successful by being extremely customer-centric. We listen to our customers and we provide solutions for them. While this is a simple equation for a set of financial products, it requires more to offer truly innovative products. We have always remained curious to stimulate creativity and encourage inspiring ideas. We have always taken calculated risks to safely harness change and maintain a leading position, thus being very pragmatic in our exploration efforts.
    

These three tenets significantly influenced the choices we have made in how we have grown the company, chosen our tech stack and broadened our product catalog:

-   _We do not outsource knowledge, instead we invest in talent_. We are experts of our core business but we do not need to be experts in everything. We lean on partners and communities for specialized expertise, however we have the curiosity to understand how things work, challenge assumptions and build together.
    
-   _We build one platform_. Adyen has not made an M&A to-date because we prefer to organically grow our platform, even though this takes more time. We typically say, “don’t confuse a headstart with speed.”
    
-   We have largely built our tech-stack on-prem using modern cloud practices and mature open-source tooling. Being “cloud-based” does not mean using someone else’s datacenter, but rather how you can scale and deploy.
    

## Every transaction at Adyen is driven by ML

![AI hand recognizes a pattern.](https://cdn-assets-eu.frontify.com/s3/frontify-enterprise-files-eu/eyJwYXRoIjoiYWR5ZW5cL2ZpbGVcL2F5S0ZZUHN3d0Q4ZTZKbU12dXVILnN2ZyJ9:adyen:Vina_5GLI9P19S4TfvIcrlQ_l3tayj68sL_pG3fmXGs)

In 2023, Adyen’s platform processed 1 trillion USD in transaction volume. While this is a huge milestone in terms of business and technological scale, it becomes even more impressive with the knowledge that each of these transactions were powered by ML inference end-points in real time to create significant funnel uplift. For context, each of these endpoints is currently processing north of 2000 requests per second at an average latency of 20ms and 100ms p99, with the ability to expand elasticity as it is horizontally scalable. We are also able to re-train and re-deploy models on-demand if needed or on a default weekly cadence.

Machine Learning in production at our scale requires algorithmic rigor and engineering excellence. Therefore, our engineering team has made choices that provide value in both dimensions while also creating the runway for long-term product innovation.

What are we optimizing for? Here is a simplified, step-by-step look.

![Graph for AI Tech blog](https://cdn-assets-eu.frontify.com/s3/frontify-enterprise-files-eu/eyJwYXRoIjoiYWR5ZW5cL2ZpbGVcL01iWVpERkFxSGNMN1FFbWFjZlVjLnN2ZyJ9:adyen:gDRqeAvGx1TH-gint7LG6N-lD5dyQHvO-jYviSZYWnk)

The first step would be to use ML to personalize the Checkout experience for conversion - we are running experiments there to validate hypotheses still. After that, we check for fraud by leveraging a set of models that look for different fraud signals and are currently based on tree-based ensembling models. Given that our data is mostly structured and tabular, proven algorithms like boosting provide a good default baseline performance when fed with hundreds of features . So far we have not seen proof that more complex flows such as Deep Learning would increase the ROI given the operational load, reliability and latency requirements. Note that at this step in isolation we have only defined fraud as an optimization function: this is, minimize the amount of fraud while also minimizing false positives; however it goes beyond that.

We also allow merchants to complement the ML models with custom-made rules. We see two types of rules: _policy rules_ which are merchant’s decisions but not per se fraud and also _other rules_ to cover for patterns the ML algorithm has not learned yet.

The authentication, authorisation, routing and retry steps are based in reinforcement learning. The idea behind those models is that each interacts with an environment (issuer network, schemes), has a policy (create conversion, payment authorized) and a set of actions to choose from (payment flags, authentication flows, routes, etc.). Our current implementation is largely based in contextual bandits but we are looking at ways to introduce state for multi-step decision making à la Reinforcement Learning.

Rather than one model per step, we have several that are executing different strategies simultaneously over different traffic splits and we constantly measure over an A/B/n framework. When we have confidence that a variant model outperforms the production model, we graduate the variant to production. This way we can confidently roll out innovation and increase uplift.

With this picture, we are looking at the journey of a transaction as a sequential process; we think that this can evolve since Adyen’s power resides in being able to connect the full-funnel. Therefore we are investing and researching ways to make holistic optimal decisions across the funnel by either merging decisions together or message passing. Either way, it creates complexity in the performance, engineering rails (e.g. how big can an artifact be) and quantification of the flows. We are researching and building towards having a payment flow that resonates with a unique vector consisting of \[fraud, conversion, cost\] which merchants can tune based on importance and tolerance.

That also has implications in how we measure uplift, which isn’t straightforward. To this end we are investing in research and partnering with the University of Amsterdam’s AMLAB to fund PhD candidates that will help Adyen productionize advancements in the area of Causal Inference and Off-Policy Evaluation.

To understand all of these investments, it is important to consider that, at our volumes, a few bps of uplift go a long way in terms of impact and that we are moving the world of payments from an authorization rate centric mindset to a full-funnel conversion mindset, connecting the worlds of fraud, tokens, data sharing and machine learning.

## Our data is mostly structured, or graphs

There are other cases where we are also investing heavily in AI to solve classic finance problems. One of them is in monitoring the activity within the Adyen Platform. This becomes a very exciting problem given the sheer amount of transactions and individuals interacting with our platform and also in addition to the fact that we are extending to financial services using our banking licenses.

For a PSP (Payment Service Provider) the data arriving to the platform is primarily structured given that it glides over the rails of well-defined APIs. It is also mainly describing attributes of shoppers (consumers). This is a luxurious advantage as our data workflows are straightforward in a sense that schemas and relationships are clear and that for meeting our primary goals, we do not need to crawl thousands of logs, comments or other sources of unstructured data to add value.

Looking at this data as relational tables is straightforward but the transactions contain relationships with a deeper sense. We have been using simple linking logic to derive entity resolution and that is helping enormously in our optimization and decisioning. In mathematical terms this means that, with consumer-only attributes, we have an undirected heterogeneous graph with nodes being payment instruments (e.g. card) or personal details (e.g. emails) with a topology based on disconnected communities (individuals or households), i.e. star architecture.

However, given that Adyen has secured banking licenses in US and Europe we can also offer other financial services such as payouts, KYC, cash advancements and money transfers which means that we also recognize an entity different from consumers (think of it as “businesses” or sellers). We are partnering with companies like Lightspeed or Zenoti so they can leverage our platform services.

As such, with platforms and financial services we increased the color of the graph by adding more node types (e.g. passport) as well as adding vectors and becoming a directed graph. Also, and most importantly, we created a new graph texture, so we went from disconnected communities to a scale-free network.

This allows us to mathematically model the data and apply research to extract patterns on top of it. However, this comes at a price since the scale of the graph, which was already billions big, became exponentially bigger given the explosion of edges created; thus creating an exciting challenge ahead for our engineering team.

To this end we have been doing thorough research on tech stack (would graph databases perform at this scale?) as well as sampling algorithms (where do you split an interconnected graph?), extracting graph features for aforementioned algorithms in the transaction flow and also training and deploying Graph Neural Networks for detection of complex patterns.

![AI at Adyen: scale of the platform 2022.](https://cdn-assets-eu.frontify.com/s3/frontify-enterprise-files-eu/eyJwYXRoIjoiYWR5ZW5cL2ZpbGVcL0RydjI4Mkh6QW90enplOXlDTHRWLm1wNCJ9:adyen:vkDoPrXsvFPvV0RQzxr3n8RDbJTCtd69NWb9joTGSfg?width=654&height=368&format=webp&crop=fp&fp=0.5,0.5)

_The engineering team managed to render a partial snapshot of the Adyen platform graph in 2022. The current one is orders of magnitude bigger, but one can get a sense of the scale._

## We see the value of GenAI

As engineers, practitioners and data scientists we already were following the evolution of the field and therefore we were familiar with the Transformer architecture. While we have been closely following the rise of BERT and GPT architectures, we must admit that ChatGPT was an eye-opener. ChatGPT was great at demonstrating the value of LLMs in today’s world and, being honest, it catalyzed our efforts on trying to understand how we could use this technology to our advantage.

Remaining true to our tenets, joining in on the development was not just cutting a partnership with a bigger player and ensuring a fast-track on their APIs. We always build one platform with a first knowledge principle, for the long term, and thus we accelerated our efforts to recruit the talent that would get us there. We also opted to diversify from Amsterdam, following our Tech Hub global expansion and expanded the AI team to Madrid.

As engineers, we find solutions to problems, not problems to the solutions or technologies that we want to use. In this light, we could act on an existing problem where we could add real value while also learning that technology; In the same way that when you learn a programming language you don’t just start by reading the documentation, but instead you focus on a project and learn from there.

For us, like many other industries, we chose to focus our GenAI efforts on our customer support service and operations. Alleviating the operational pressure by increasing the efficiency of our support team was a primary objective that would benefit the company and would also make the life of our colleagues happier by making their job more interesting. We also started by partnering with startups and vendors that would offer this service while we were recruiting, ramping up the team and pointing them to work on both benchmarking vendor quality and to build our internal service for the correct routing of tickets.

![AI-hand and human-hand do a handshake.](https://cdn-assets-eu.frontify.com/s3/frontify-enterprise-files-eu/eyJwYXRoIjoiYWR5ZW5cL2ZpbGVcL0tFUFNZQW1rbk1KM2VhN3NjVWFELnN2ZyJ9:adyen:WM89QDZi604TjXXW1Olap23ods6JYQxveBfj6jkWT30)

It is worth dwelling for a moment on why support was an easy choice. First, data consists primarily of text (i.e. no multimodal) which eases the learning curve. Second, it has huge impact for the business as, for example, routing accuracy would reduce the amount of hours designated to read and understand cases just to figure out it was from someone else; Third, we already had a team in place and thus we could count on the “human in the loop” therefore ensuring quality of our output while also augmenting efficiency. Given we are a B2B company, our enquiries tend to be complex and long. Often on the other side of those enquiries is a company with an expert asking a good question and expecting an adequate answer back. Here we can leverage the human to either improve the labeling and annotation of datasets or to correct the model at inference time.

Interestingly enough, our engineers and scientists figured that LLM-based routing wouldn’t out-perform a more simple TF IDF (Term Frequency Inverse Document Frequency) classifier. Our system was just performing better than the choices provided by the vendors and it was completely within our control and a fraction of the operational and energy cost. It is indeed important to be measured in times of hypes.

From there on we have added ticket summarisation and context augmentation through RAG to the support use case. We are now researching whether we can further improve our routing, summarisation, and context retrieval capabilities by offering keywords coming from TF IDF, in the same way that you might read a book that has been highlighted by an expert before so you get a hint at the important takeaways.

Since we also created the backend to leverage GenAI in-house for operational support, we decided to open it up to every Adyener. In this way, any Adyen employee can use internally hosted LLMs, contextualize with a data source, and use GenAI for productivity without having to worry about information leakage through the prompt.

We deployed our GenAI capabilities on-prem on our data clusters, that we also equipped with GPUs, that engineers and data-scientists can leverage for exploration and production flows. We leveraged not only the open source models but the open-source ML infrastructure that was developing fast in the community.

A quick one on open source. The technological developments in GenAI these last years and its impact on society have been fascinating. While closed-source models seem to have a performance advantage, today the speed and advancements that the open-source community have made are remarkable. The fact that players like Meta or Mistral are opening up their models to the community has created an explosion of research papers and infrastructure that also has benefited the closed-source players. Being part of the open-source community does not only mean using code and weights from someone else. It also means contributing back, and as such we take a bit of pride in bug fixing and adding capabilities in frameworks such as HuggingFace’s TGI, ChatUI or LangChain.

We have been extremely pragmatic in this approach and we feel that while being focused on execution is of the utmost importance, a company cannot lose its grip in the developments and also, at some point, contribute with their own. To this end, as we are maturing, we are lining up our plans to not just be a “fast follower” but also to have a say in some advancement before the journey. Topics like trust and confidence in evaluations (i.e. hallucinations), synthetic data, self-alignment or transformer-based architectures for mixes of structured and unstructured data are catching our attention and curiosity.

This also means that we are being very curious and listening to partners for other features and compute options, next to our on-prem platform, for exploration and for production flows that are less data sensitive. Indeed, an agent that crawls the web and finds relevant patterns for us doesn’t need to live inside our data center per se. By the same principle, we are very curious and learning from founders and players in the AI space.

This was a broad snapshot of what we are mainly doing today, and the direction we are taking with AI at Adyen. We will be addressing in greater depth more topics in a talk at KDD2024.

This piece was still written word-by-word by a human.

## Fresh insights, straight to your inbox

Make the right decisions with the latest insights and advice on business growth and payments innovation.

By submitting your information you confirm that you have read Adyen's [Privacy Policy](https://www.adyen.com/privacy-policy) and agree to the use of your data in all Adyen communications.
