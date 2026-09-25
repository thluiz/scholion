---
url: "https://www.infoq.com/articles/architecture-experimentation/?ref=dailydev"
captured_at: "2026-09-25T22:28:48+01:00"
title: "Software Architecture and the Art of Experimentation"
domain: "infoq-com"
---

### Key Takeaways

*   When it comes to software architecture, being wrong is inevitable. The art of architecting is to spend only a little bit of time going down the wrong path. The only way to decide is to run experiments and gather data that can inform these decisions.
*   Minimum Viable Architectures (MVAs) consist of experiments that test the viability of architectural decisions. These experiments gather feedback that enables the development team to revise their decisions.
*   MVAs are also experiments about their MVPs; they test the viability of the MVP from a technical perspective. If the MVP isn’t technically viable, then there is no business value in the MVP.
*   An experiment is more than just trying something to see if it works. Each product release is a set of experiments about value and supportability. Feedback from these experiments helps development teams improve both the product’s value and its supportability.
*   Architectural experiments also need to anticipate "support and change" work.

Being wrong is frustrating, wasteful, sometimes embarrassing, and yet… inevitable. Especially with respect to software architecture, If you are never wrong you are not challenging yourself enough, and you are not learning. But being wrong is psychologically painful enough that most people avoid it, primarily by never checking their work.

Some people think that they can’t test the architecture of a software product without building the whole thing. But a software architecture is not a single thing, it’s the result of lots and lots of decisions, each of which can be isolated and evaluated through experimentation.

And while we can’t avoid being wrong some of the time, we can reduce the cost of being wrong by running small experiments to test our assumptions and reverse wrong decisions before their costs compound. But here time is the enemy: there is never enough time to test every assumption and so knowing which ones to confront is the art in architecting.

Successful architecting means experimenting to test decisions that affect the architecture of the system, i.e. those decisions that are "fatal" to the success of the thing you are building if you are wrong.

Knowing what to test is half the problem; the other half is devising effective but low-cost experiments that reveal flaws in one’s assumptions.

This is the key idea behind the concept we call the _Minimum Viable Architecture_ (MVA), which is a set of decisions that you believe will make the increment of the system or product, the _Minimum Viable Product_ (MVP), you are working on able to sustainably deliver value over time.

In this article, we explore the attributes of a good experiment.

## MVAs are experiments that test the viability of architectural decisions

In the aforementioned article, we observed:

![](https://imgopt.infoq.com/fit-in/3000x4000/filters:quality\(85\)/filters:no_upscale\(\)/articles/architecture-experimentation/en/resources/13figure1-1734346585300.jpg)

The only way to know if these decisions are reasonable is by conducting experiments and gathering data. These experiments test the affordability, viability, sustainability, and supportability of the MVP. The MVA reflects the trade-offs the development team makes to achieve the architectural goals of the MVP. Since every release is an MVP with an associated MVA, every release is a set of experiments about value and supportability. The purpose of the release is to deliver value to customers and to gather feedback on how well the release meets the needs of its customers, both today and over the lifetime of the system.

If the team does not run architectural experiments, their decisions are simply guesses, based on assumptions, about what the solution needs to be. If the guesses turn out to be wrong then, because of their impact, they will be very expensive to reverse and may even kill the product/project.

For example, a team may decide to use a vector database to develop a proprietary fraud detection service in a financial institution using Machine Learning. Based on their research, using the vector database product might speed up the development of their MVP, and one of the team members has limited experience with that product. As an experiment, they decided to implement a small fraud detection use case using that product and measure the productivity improvement.

However, it turns out that the expected productivity gains were not realized because the product was much harder to use than expected. The programming interface to the vector database didn’t match the programming paradigms the team had chosen, and meeting the performance objectives using that product was also challenging. Based on their experiment, the team realized that using a vector database would delay and possibly threaten the delivery of their MVP, and they decided not to use the product.

## MVAs are also experiments that test the technical viability of the MVP

One way to think of an MVA is that it consists of one or more experiments that test the long-term sustainability of the value provided by the product increment, or MVP. As we observed in a [previous article](https://www.infoq.com/articles/minimum-viable-architecture/), the concept of a Minimum Viable Product (MVP) can help teams focus on delivering what they think is most valuable to customers, early, so that they can quickly and inexpensively gauge the size of the market for their product before investing significant time and resources. Each MVP is, therefore, a set of experiments that test the value that the product increment delivers to customers.

MVAs are important because an MVP is just smoke and mirrors (or wishful thinking) until you have an MVA that can support it. We’ve witnessed many examples where a business stakeholder comes up with a bold new business innovation that contains no consideration of how, or if, the idea can be realized.

MVPs are not limited to start-ups, since every application has an initial release that can be thought of as an MVP. MVPs are a useful component of product development strategies. Unlike mere prototypes, MVPs are not intended to be "thrown away".

The way we talk about MVAs sometimes makes it sound like they are separate experiments from the MVP but this isn’t the case, as we discussed in an [earlier article](https://www.infoq.com/articles/agility-architecture). What happens when a development team is working on their MVP is that they are constantly making architectural decisions about how the product will achieve its architectural goals. These decisions are the MVA.

## Characteristics of Effective Architectural Experiments

An experiment is more than just trying something to see if it works; it is a test that is specifically designed to confirm or reject a particular hypothesis. A hypothesis is a potential answer to a question that a team has about the fitness of their solution. Experiments can’t prove that something is right, only that something is wrong, but that’s still useful because it means that if you design your experiments correctly, you can tell which of your assumptions are incorrect - before they cause unpleasant surprises.

If you don’t run an experiment you are assuming you already know the answer to some question. So long as that’s the case, or so long as the risk and cost of being wrong is small, you may not need to experiment. Some big questions, however, can only be answered by experimenting. Since you probably can’t run experiments for all the questions you have to answer, implicitly accepting the associated risk, so you need to make a trade-off between the number of experiments you can run and the risks you won’t be able to mitigate by experimenting.

The challenge in creating experiments that test both the MVP and MVA is asking questions that challenge the business and technical assumptions of both stakeholders and developers. These experiments have to be small enough to gather feedback quickly but significant enough to confront the risks the team faces.

In the context of the MVA, this means confronting the risks that the architectural decisions the team is making may be wrong. The order in which the team does this is guided by asking, "which of the decisions we have made would be most damaging if it turns out to be wrong" and "which of these events are more likely to occur". We’ve found that this discussion is useful, but it doesn’t need to be a lengthy one; most teams have a fairly good idea of what decisions keep them up at night.

As we noted in another [article](https://www.infoq.com/articles/architecture-skeptics-guide/), every requirement, including Quality Attribute Requirements (QARs) that drive the architectural design, represents a hypothesis about value. Making these hypotheses explicit and consciously designing experiments helps the team avoid making assumptions about their solution.

Effective architectural experiments are:

*   **Atomic**. They deal with one question at a time. Running more than one experiment at a time muddles the results and usually delays obtaining important feedback.
*   **Timely**. They break risk down into small, manageable chunks to obtain feedback faster and simplify the interpretation of results.
*   **Unambiguous**. They have clear success criteria and measurable outcomes. An experiment is not simply trying something to see if it works.

To help to achieve this, every experiment needs:

*   **A clear hypothesis**. A team working for an insurer is considering using image recognition software to detect whether a house in a fire-prone zone has vegetation within a certain distance. They hypothesize that the software can detect vegetation and measure its distance from a structure to assess fire risk using an image taken from a satellite.
*   **An explicit and measurable goal or target**. The goal of the experiment is to determine whether the image recognition software can detect and identify two bushes and one tree within 30 feet of a specific house, using a clear high-resolution satellite photo.
*   **A method for running the experiment and mechanisms for measuring its success or failure**. Since the experiment has a limited scope and will attempt to identify well-defined shapes, it will use a pre-trained image recognition model which will only require limited training. The results of the experiment will be compared to ground-level photos of the house and its surroundings to validate the findings of the model.
*   **A plan for rollback if the experiment fails**. For the example above, since the experiment is non-destructive and does not change the state or content of existing data, a roll-back plan isn’t needed. In the case of some code changes, reverting to a prior version of the code may be necessary if the experiment fails. In other cases, where the experiment must be done in a release deployed to customers, as is the case where real-world usage feedback is essential to gather data needed to make a decision, the team will need a way to rollback the change using techniques like A/B testing or a rapid redeployment of the system if the experiment fails.
*   **An explicit timeline for the experiment**. Since we’re working in short cycles, the experiment needs to fit within the release’s timebox. In the context of an agile method like Scrum, the experiment needs to fit in a single Sprint. If it’s too much work to fit the experiment into the timebox for developing and testing the release, you’ll have to break it into smaller experiments.

Sometimes experiments fail to achieve the desired results and the team may be tempted to extend the experiment to give them time to refine their solution. This should be a new experiment, not an extension of the old one. Consider the case of the image recognition experiment described above. The team may be tempted to believe that additional model training may improve the results and make the experiment successful. However, this should be considered a separate experiment.

Some experiments may require the team to acquire hardware or software, hire (if only temporarily) someone with needed expertise, or acquire computing resources (such as cloud or test environments) that they don’t have. In these cases, they may need a budget and funding approval.

[Architectural retrospectives](https://www.infoq.com/articles/architectural-retrospectives) can help a team to consider whether they are experimenting enough, or perhaps too much. The problems of not running an experiment are obvious, but running too many experiments can be just as bad; if it doesn’t matter whether a decision turns out to be wrong, that decision isn’t really architectural, it’s simply a different design choice.

### Architectural experiments also need to anticipate "support and change" work

We value modularity in software systems because it makes the system easier to extend and evolve. But just as with a building, successive changes to a software system, if poorly conceived or executed, can eventually overwhelm the system and reduce its long-term viability. A good software architecture anticipates change and makes certain kinds of change easier and less destructive. But how does a team know how much to invest in anticipating and easing future change? And how do they know if their work in this regard is successful?

As with other kinds of architectural decisions, the only way to know is to run some experiments that focus on assessing the cost and impact of certain types of change. For example, consider an insurance underwriting system that deals with specific kinds of covered assets (household furniture, for example) and specific kinds of loss events (fire, for example). It would be useful for the team developing this system to consider how easy it is to add a new kind of covered asset (fine art, for example) and a new kind of loss event (a theft, for example). They may find that some kinds of change are easy while others require a whole new system.

This is one of the reasons why a homeowners policy does not cover automobiles because the risks and decision criteria for settling claims differ too much for one system to work for every kind of asset and every kind of risk. Knowing the boundaries of change is an important architectural decision.

Architecting work must also consider how that system will be supported over time. When it fails does it provide enough information to diagnose the problem? Answering this question requires understanding the knowledge and expertise of support staff as well as the kinds of events that could cause failure. Sometimes the only way to know this is to run experiments that are intended to cause the system to fail to see how it reacts and what information is needed to remedy the problem after it fails.

For example, an automobile policy system in an insurance company would usually use a rules engine for customizing and pricing coverages for the company’s customers. Configuring and testing the rules is an often challenging and time-consuming task. As suggested by Thomas Betts in a recent [article](https://www.infoq.com/articles/architectural-intelligence/), using a Large Language Model (LLM) to enter and validate these rules would be a good way to make that task significantly easier and faster, assuming that the insurance company has enough rule configuration examples to train the LLM.

However, the output of an LLM is sometimes difficult to explain, and the team should run experiments designed to make the LLM generate "wrong" information, to make sure that they can diagnose the problem if this happens in production. Doing this kind of experiment may avoid some nasty surprises once the system is implemented. It may convince the team to reconsider their LLM-based approach if they are unable to diagnose the problem.

## Conclusion

Software architecting work is not always predictable; systems are complex entities that sometimes behave in unexpected ways. Sometimes the only way to understand the boundaries between expected and unexpected behavior is to run experiments. One of the goals of an MVA is to provide a mechanism for running architectural experiments so that the development team can understand when and how their architectural decisions might fail. Armed with better information, the development team may make different choices, or at least know when their assumptions might fail.

When the risk of exceeding system limits is low, the development team may decide to accept the risk, but even in these cases, they should design the system so that it fails gracefully and provides support staff or future development team members with enough information to fix the problem without scrapping major parts of the system.

In software architecting, being wrong some of the time is inevitable; if you are never wrong you are not challenging yourself enough, and you are not learning. The essential thing is to test our decisions as much as possible with experiments that challenge our assumptions and to construct the system in such a way that when our decisions are incorrect the system does not fail catastrophically.

## About the Authors

[![Pierre Pureur](https://cdn.infoq.com/statics_s2_20260925154625/images/profiles/22c27753414b3827cb473ede92e13489.jpeg)](https://www.infoq.com/profile/Pierre-Pureur/)

#### **Pierre Pureur**

Pierre Pureur is an experienced software architect, with extensive innovation and application development background, vast exposure to the financial services industry, broad consulting experience and comprehensive technology infrastructure knowledge. His past roles include serving as Chief Enterprise Architect for a major financial services company, leading large architecture teams, managing large-scale concurrent application development projects and directing innovation initiatives, as well as developing strategies and business plans. He is coauthor of the books "Continuous Architecture in Practice: Scalable Software Architecture in the Age of Agility and DevOps"(2021) and "Continuous Architecture: Sustainable Architecture in an Agile and Cloud-Centric World" (2015) and has published many articles and presented at multiple software architecture conferences on this topic. 

Show moreShow less

[![Kurt Bittner](https://cdn.infoq.com/statics_s2_20260925154625/images/profiles/3789fc0e548a79744225f15083ab938c.jpg)](https://www.infoq.com/profile/Kurt-Bittner/)

#### **Kurt Bittner**

Kurt Bittner has more than 30 years of experience delivering working software in short, feedback-driven cycles. He has helped a wide variety of organizations adopt agile software delivery practices, including large banking, insurance, manufacturing, and retail organizations, as well as large government agencies. He has worked for or with large software delivery organizations including Oracle, HP, IBM, and Microsoft. He is also former technology industry analyst with Forrester Research, and has written widely on topics related to agile teaming and leadership.

Show moreShow less
