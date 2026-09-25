---
url: "https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter"
captured_at: "2025-12-25T19:15:04-03:00"
title: "Interviewing for ML/AI Engineers"
domain: "moderndescartes-com"
---

---
2025-12-22

Tagged: [software engineering](https://www.moderndescartes.com/essays/tags/software_engineering), [strategy](https://www.moderndescartes.com/essays/tags/strategy), [machine learning](https://www.moderndescartes.com/essays/tags/machine_learning)

___

In my [recent job search for an ML/AI engineering position](https://www.moderndescartes.com/essays/2025_job_search/), I talked to ~15 companies, made it to onsites for ~10 companies and received 7 offers. I did ~70 separate interviews, not counting recruiter/team match calls.

My favorite interview by far was the one with Espresso AI’s CTO, where we commiserated about how much the ML system design interview format sucked. And that made me wonder - who ever thought these were a good idea?

In this essay, I’d like to rethink the ML engineer interview loop and suggest some alternatives to the ML system design interview.

## [What does an ML engineer do?](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#what-does-an-ml-engineer-do)

An ML engineer is someone who is basically otherwise qualified/capable of being a regular software engineer, but also has the ability to reason about the statistical and distributional nature of data.

Some companies need ML engineers who could rederive backprop on the spot, and others need ML engineers who can handle sysadmin-like tasks like scaling up GPU clusters. Some companies don’t actually need ML engineers, but call their software engineer positions ML engineer, as part of a mutually self-serving title inflation game.

You should require at least 2 of each SWE and ML skills below to actually call a job ML engineering.

### [SWE skillsets](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#swe-skillsets)

-   write maintainable, bug-free, performant code (in Python, C++, or CUDA).
-   implement and analyze algorithms and data structures.
-   understand distributed systems and feedback loops (useful for building reinforcement learning systems).
-   deploy, monitor, and debug production systems (useful for ML infra engineers).

### [ML skillsets](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#ml-skillsets)

-   write maintainable, bug-free, performant ML code (in array languages/DSLs).
-   implement and analyze ML methods (via statistics, calculus, and linear algebra.)
-   do exploratory data analysis to understand e.g., what is the generating process producing this data, what missingness/quality issues does it have, what distributional skews does it have, how might it be transformed into something an ML technique can process?
-   deploy and monitor ML systems, and diagnose data-related issues like schema/data drift.

These ML skillsets are relevant for structured data (numbers and categoricals), and unstructured data (images, text, pdf, etc.)

## [The ML engineering interview types](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#the-ml-engineering-interview-types)

### [Coding/algorithms](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#codingalgorithms)

Code a solution to a LeetCode-style problem.

These are necessary, because ML engineers write code. Indexing/search/graph/tree/heap flavored leetcode-ish problems are most appropriate for ML engineers, because that’s what often shows up in actual day-to-day work.

I’ve also seen ML-flavored coding problems, such as implementing a transformer layer or debugging a buggy transformer implementation. I find these relatively low-signal because 80% of the complexity lies in the obscurity of numpy-flavored indexing/broadcasting, and this complexity is entirely invisible and in the candidate’s head.

### [Data modeling](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#data-modeling)

Improve an existing modeling scaffold on a dataset/task in a live environment by fixing bugs, doing EDA to figure out there is a class imbalance, by changing the NN architecture, by changing the training methodology, etc.. One or more intentional bugs may be present.

This tests the candidate’s fluency in Python/numpy/pandas/pytorch, as well as their ability to debug and improve model performance. It offers a very specific testbed in which to answer ML questions in more than vague generalities. To spice up things, you can ask the candidate to explain why they think an improvement will work, introduce artificial constraints like a max number of NN weights, or have intentional quirks in the dataset.

This type of interview requires a lot of preparation and test-solving for a good dataset, modeling problem, and live coding environment, but I found it to be very rewarding as an interviewee and high-signal.

### [Math quiz](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#math-quiz)

Answer short, factual, math/statistics/ML questions on, e.g., computing a Bayesian update by hand, computing the derivative of the softmax function, explaining covariance matrices, or explaining why/how [KL-divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence) is asymmetric.

These questions can be useful in sprinkles, but they have high false negative rates (you shouldn’t fail the interview just because it’s your first time seeing KL divergence), and I wouldn’t spend a whole interview on these types of questions.

### [System Design](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#system-design)

Design a system that is one or more of ( large | scalable | distributed | high-throughput | low-latency | resilient ).

I think it’s good practice to have these interviews have concrete numbers and equations - e.g. estimating load factors, or making quantitative predictions about the impact of some retry policy on latency characteristics in the event of various types of subsystem failure.

### [ML System Design](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#ml-system-design)

Design a solution to an ambiguous product or business need. The ideal solution should be a system co-designed around product context, user experience, dataset availability, likelihood of modeling success, tasteful selection of key metrics, and production monitoring. The ideal problem starts from a real user need and leaves the solution space open-ended.

This tests the candidate’s ability to extract a plausible junior-engineer shaped ML modeling problem, as well as their taste and judgment is deciding what problems are worth throwing ML at, and what problems are worth throwing some quick-and-dirty heuristic, and whether they have a good intuition as to what flavor of dataset or training would make for a useful input to the ML system.

### [Project Deep Dive](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#project-deep-dive)

Present an ML project they worked on, and discusses the motivation, problem statement, difficulties encountered, impact, and any ancillary work. The interviewer should approach this conversation with a collaborative mindset, rather than a skeptical one, and focus on how the candidate personally experienced their project, rather than on the interviewer’s conception of how such a project should have been run. New grads can talk about a class project; PhD grads can talk about their research; self-learners can show off a portfolio project; industry hires can talk about a project they worked on.

This gives strong signal on the candidate’s seniority level, communication skills, and motivation for ML. It also offers a chance to demonstrate some valuable role-specific knowledge - e.g. if you’re hiring for a role on a recommender systems team, then the candidate that presents a great recsys projects can have a very in-depth conversation with the interviewers.

### [Career Chat](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#career-chat)

Discuss your career arc, relevant highlights, and goals for next role.

This gives signal on ambition, agency, growth potential, work flavor preferences, personality, and figures out whether the company’s needs match what they are looking to do next. This is a great call for the hiring manager to take. I think this is a strict improvement on the “tell me about a time when…” flavor of people interviews, which is susceptible to fake prebaked narratives.

## [Putting it all together](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#putting-it-all-together)

### [Goals of an interview loop](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#goals-of-an-interview-loop)

1.  We want to estimate the candidate’s current abilities.
2.  We want to estimate the candidate’s capacity and desire for growth.
3.  We want to identify factors that might prevent candidate from realizing their potential, like cultural mismatches, poor fit for remote work, misalignment in type of work, etc.
4.  We want to present a compelling pitch to the candidate that they should want to work here.

The process should be robust enough to avoid being fooled by people who are good at talking, and accurate enough to calibrate the candidate’s leveling as well as willingness to push out-of-band offers.

I also believe that for strong candidates, there is no stronger pitch to join, than to present a slate of talented and thoughtful interviewers who could be their future coworkers, and an interview process rigorous enough to assure them that all of their coworkers will have been as thoroughly examined.

### [Recommended interview loop](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#recommended-interview-loop)

The ideal interview loop for junior candidates should include 3 coding interviews, 1 coding interview with strong math flavor / math quiz flavor, 1 data modeling interview, and a project deep dive interview. An abbreviated loop (for startups) would include 1 coding interview, 1 data modeling interview, and a project deep dive interview.

For senior candidates, I would do 2 coding interviews, 2 data modeling interviews, a system design interview, a project deep dive, and a career chat with the hiring manager.

For staff+ candidates, I would do a coding interview, 2 data modeling interviews, 2 ML system design interviews, a project deep dive, and a career chat with the hiring manager.

You can vary the formula based on the precise skillset you need for your position (e.g for someone working on RL, sub out one data modeling interview for a system design interview).

### [British flavor?](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#british-flavor)

DeepMind and their alumni tend to offer more book-ish interviews, heavy on math quizzes, and having coding problems that are particularly algorithms-heavy. Finance companies will also have a heavy London presence. It’s a different culture, and perhaps this interview style works well with a population that grew up on the [Tripos](https://en.wikipedia.org/wiki/Tripos), but I think it would have a high false negative rate on the American population.

## [Appendix: ML system design failure modes](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#appendix-ml-system-design-failure-modes)

### [Not an ML question](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#not-an-ml-question)

A lot of “ML systems designs” are actually vanilla system design questions, but where you have to say some ML words along the way. In many cases, neither the interviewer nor candidate actually understand the ML words they recite to each other. I find this type of interview useless, because the ML questions aren’t detailed enough to exclude smooth talkers, and there’s less time to dive deep on the system design front, again enabling smooth talkers to slip through. Do a proper systems design interview.

### [Lack of pointed questions](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#lack-of-pointed-questions)

Some people are great at talking. If your interview can be passed by reciting “I would take the dataset, train a neural network on it using a softmax/cross-entropy loss, and then optimize hyperparameters while monitoring FP/FN rates. Class imbalance. Data missingness. Label noise. Overfitting.” then it is a bad interview. Do a proper data modeling interview instead.

### [Cog In A Machine](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#cog-in-a-machine)

Sometimes, the ML engineer administering the interview is relatively inexperienced, or has only worked on a small corner of the overall system. They start asking really detailed and specific questions about the experience they have, like data prep, evals, production scaling, etc. while glossing over other parts of the system. They don’t know how to talk about or evaluate the big picture. Due to inexperience, they may also expect answers that were maybe correct for the specific project they worked on, but not correct or relevant in general.

### [Too much “rederive major algorithmic advances from scratch”](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#too-much-rederive-major-algorithmic-advances-from-scratch)

One interview problem I got was “Design a data deduplication pipeline for a large web crawl dataset”. The answer is the [MinHash algorithm](https://en.wikipedia.org/wiki/MinHash) and its variants – and no, you will not rederive this algorithm in the course of 45 minutes if you hadn’t already studied it in depth previous to the interview.

In general you should test for the ability to learn and implement MinHash in a day or two, rather than prior knowledge of MinHash.

You can test this in a number of ways. First, give a hard coding interview. Second, filter for resumes showing the right background experience. Third, do a project deep dive on that background experience. Perhaps that project deep dive is a data deduplication pipeline for a large web crawl dataset. Perhaps it’s something else that is equally technically impressive. Either way, let the candidate choose, rather than ambushing them.

### [Outdated problem](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#outdated-problem)

Sometimes, interview problems go stale due to advancements in ML.

In one such interview, the interviewer gave me a text content classification problem and was seemingly looking for an approach involving some flavor of embedding + classifier training. I asked how many classes needed to be distinguished, and how ambiguous those classes might be (to a human), and then suggested that a small off-the-shelf LLM with system prompting would be quick to implement and do very well. They rejected on the basis that it was “too expensive”, and I ended up sketching out the tokenomics and estimated a very reasonable unit price for the task, which they accepted. But then the rest of the interview was sort of a bust because there was little left to talk about - the interviewer didn’t know enough about LLMs to ask good follow-up questions to my approach.

In another interview, I was asked to design a RAG-based chatbot. I explained the weaknesses of a fixed context-injection system and explained how I would design an agentic search system instead (with vector similarity search included as a “fuzzy\_lookup” tool). The interviewer seemed to have been expecting a discussion on chunking and scaling vector search. That’s okay, too – just drop the AI pretense and just do a systems design interview on vector database design!

### [Lack of scenariocrafting](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#lack-of-scenariocrafting)

Some questions are just so hopelessly vague that there’s nothing to discuss. A good scenario invites good questions from good candidates, and creates specific hooks to start making design decisions around.

-   Good scenario: “Our bank’s customers are being scammed, and they are losing their life savings. Find a way to prevent this from happening.”
-   Bad scenario: “Design a fraud detection system for a banking application”

The good scenario naturally invites good questions: “what are the downsides to preventing legitimate attempts at withdrawing large amounts in cash?” “what is the appropriate detection and intervention point?” “what levels of human discretion/override/fallback should be allowed?”.

-   Good scenario: “Build a Slack bot for a volunteer-run help channel that automatically @tags people who might be able to answer a question”
-   Bad scenario: “Automatically route JIRA tickets to the right subteam”

The good scenario, again, naturally invites good questions: “are all messages to the slack channel necessarily questions that need routing?” “how annoyed would people be if they’re @tagged on a question they can’t answer?” “can we @tag anyone in the company, or do we need an opt-in/opt-out mechanism?” “what if the same person gets too many @tags?” “how much slack history do we have from the channel?” “what supplementary data do we have on org chart, tenure, team affiliations for everyone?”

When you craft detail into a scenario, you should do due dilligence: can you find industry reports/papers/blog posts detailing the peculiarities and customization needed for that scenario?

### [Overall thoughts on ML Systems Design](https://www.moderndescartes.com/essays/ml_eng_interviewing/?utm_source=tldrnewsletter#overall-thoughts-on-ml-systems-design)

Many ML Systems Design interviews would actually be served better by either a Data Modeling interview, a System Design interview, or a Project Deep Dive.

The ML Systems Design interview has potential for very high signal, but it needs a staff-level ML engineer to execute well. Unfortunately, there’s a shortage of capable interviewers, given the 25% year-over-year growth in the field over the past decade. As a result, ML system design interviews should be limited to Staff+ candidates.

I think overall, the other interview formats give a lot more signal on hard technical ability. Please consider one of them before reaching for the ML Systems Design interview!
