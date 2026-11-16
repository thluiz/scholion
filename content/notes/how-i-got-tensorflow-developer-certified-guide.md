---
title: "How I got TensorFlow Developer Certified (and how you can too)"
date: '2026-11-16T20:13:01+00:00'
category: webclip
summary: 'Author explains what the TensorFlow Developer Certification is, why it matters, the study resources and routine used to pass it, exam logistics, a technical hiccup faced, and post-exam steps.'
tags: ["tensorflow", "machine-learning", "certification", "study-plan"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "How I got TensorFlow Developer Certified (and how you can too)"
    url: "https://www.mrdbourke.com/how-i-got-tensorflow-developer-certified/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/mrdbourke-com--how-i-got-tensorflow-developer-certified-guide.md"
    kind: repo
---

The author describes deciding in May 2020 to take the TensorFlow Developer Certification exam, preparing with a self-designed curriculum, and passing on June 3rd. The article explains what TensorFlow is, what the certification tests, reasons you might pursue it, concrete resources to study from, how the author structured daily learning, what happens during the exam, a Python/TensorFlow environment issue encountered, and what to expect after finishing. The author stresses that certificates are optional compared to skills, but can complement personal projects and signal competency to employers.

## Reading notes

- TensorFlow is presented as an open-source numerical computing framework that handles data preprocessing, modeling with deep learning, and deployment, commonly written in Python or JavaScript on top of C implementations.
- The author notes TensorFlow underpins Google’s machine learning services and likely runs on devices readers already use.
- The TensorFlow Developer Certification focuses on using TensorFlow (Python) to build deep learning models for regression, computer vision, natural language processing, and time series forecasting.
- Motivations given for taking the exam include having a fun challenge, gaining foundational skills for ML-powered applications, and showcasing skills to potential employers.
- Hacker News “Who’s Hiring” data is cited to suggest TensorFlow appears more often in job postings than some other deep learning frameworks, while overall software hiring is down.
- The author cautions that a paid certificate does not guarantee a job but can help demonstrate capability amid commoditized online learning.
- Certificates are framed as additions alongside personal projects: courses give foundation, projects provide specific experience.
- Before building the curriculum, the author read the official certification site and TensorFlow Developer Certification Handbook to understand exam topics.
- The author mentions having prior hands-on TensorFlow project experience before exam-focused study.
- Experienced practitioners are told they might complete the suggested curriculum in about three weeks, whereas beginners should take as long as needed.
- For each resource, the author lists approximate timelines, US dollar costs, and how helpful it was toward passing the exam.
- The TensorFlow Developer Certification Handbook is labeled mandatory, free, about an hour to read, and should be read more than once to understand covered topics.
- Newcomers might find the handbook intimidating, but the author says the subsequent resources help make the topics familiar.
- The TensorFlow in Practice Specialization on Coursera is described as the most relevant resource for the exam, with an outline similar to the handbook.
- This specialization is taught by Laurence Moroney and Andrew Ng, and the author would choose it if only one exam-prep resource were possible.
- The author highlights short videos, hands-on examples, and multiple end-of-section code notebooks as valuable for practical learners.
- A specific tip is to rewrite full solutions for programming exercises instead of only filling code gaps.
- “Hands-on Machine Learning with Scikit-Learn, Keras and TensorFlow” (2nd ed.) is recommended as a broad ML foundation, though some chapters are not directly relevant to the exam.
- The author notes the book’s 700+ pages cover most of ML and suggests it can be challenging for beginners, but emphasizes that gaining useful skills takes time.
- They share that reading the first edition on commutes often led to using that material during the same workday as a machine learning engineer.
- The second edition is praised for updates to TensorFlow 2.x, matching the exam’s version.
- For exam-focused reading, the author points to chapters on neural networks with Keras, deep network training, custom models and training, data loading and preprocessing, CNNs for computer vision, sequence models with RNNs/CNNs, and NLP with RNNs and attention.
- The MIT “Introduction to Deep Learning” course is recommended as free, high-quality material, especially lectures on general deep learning, CNNs, and RNNs.
- The author suggests motivated learners can benefit from completing the whole MIT course and checking its GitHub labs, particularly the TensorFlow introduction, while writing code themselves.
- Since the exam runs in PyCharm, the author recommends JetBrains’ PyCharm “getting started” materials to become familiar with the IDE before test day.
- The author used PyCharm YouTube tutorials to learn the interface, then verified TensorFlow 2.x worked locally and that their machine could train deep neural networks at an acceptable speed.
- To test their setup, they reproduced TensorFlow official tutorials on image classification and text classification with RNNs on their local machine.
- The author lists additional supporting materials: deeplearning.ai videos to understand math concepts, TensorFlow API docs for practice reading documentation, and a YouTube playlist overlapping with the TensorFlow in Practice specialization.
- Using these resources, the author created a Notion Kanban board to track tasks, resources, and notes, and shares a template link for others to duplicate.
- Their daily routine in May included writing, walking, one hour of book reading, then 2–3 hours of TensorFlow in Practice lectures and Colab exercises, followed by the related MIT lecture for each module.
- The author describes this combination of book, Coursera course, and MIT videos as reinforcing concepts, where reading introduced ideas, coding exercises solidified them, and lectures summarized them.
- They studied from May 11th to June 3rd and report averaging about 20 book pages per hour and roughly a week of course content per focused 2–3 hour block.
- A few days before the exam, they installed PyCharm and re-ran code examples locally to ensure everything worked in that environment.
- The exam costs $100 USD per attempt, and failing requires waiting two weeks before trying again, with longer waits after further failures.
- The time limit is five hours, which the author found generous; they estimate finishing in about three hours without technical issues, with extra time intended for model training.
- The author declines to reveal exam details but advises reading the official handbook to understand sections and practicing each technique it lists.
- They mention that if local training is slow, candidates can train models on Google Colab with a free GPU, then download and place them in the expected exam directories before submitting through PyCharm.
- An update notes the exam environment later shifted to TensorFlow 2.5 and Python 3.8, pointing readers to an environment setup handbook.
- During the author’s exam, TensorFlow broke in the provided environment using Python 3.7.3, throwing a “dictionary changed size during iteration” runtime error whenever TensorFlow code ran.
- After searching an old GitHub issue, they applied a quick fix by changing a loop in Python’s linecache.py to iterate over a list copy of sys.modules values.
- This source code change allowed them to complete the exam, though they label it a quick workaround with unknown long-term implications.
- From this incident, the author emphasizes repeatedly verifying that TensorFlow runs correctly in PyCharm within the exam environment before starting the test.
- After submission, candidates receive an email indicating only pass or fail, with no detailed feedback.
- The author notes that during the exam, model submissions are scored, giving a sense of whether you are on track to pass.
- Passing candidates are instructed to fill out a form from the email to be added to the TensorFlow Certified Developers network.
- Registration in Google’s Global Certification Network lets potential clients or employers search for certified TensorFlow developers by certification, experience, and region.
- Within a couple of weeks of passing, candidates receive an official TensorFlow Developer Certificate and badge, which they can present alongside their project portfolio.
- In a Q&A, the author affirms that it is possible to learn the material without getting certified and that skills should be the main aim, with certificates treated as optional extras.
- They explain they pursued the certificate to set a firm goal and deadline, which encouraged consistent study.
- For those wanting to rely on free resources, the author suggests using the TensorFlow documentation, copying example code line by line, adding comments, and then rewriting from memory.
- When asked about PyTorch, the author expresses appreciation for it but notes PyTorch has no comparable certification and remarks that both frameworks have become more similar, with TensorFlow having an advantage in enterprise contexts based on the earlier job posting graph.
- People who do not yet know machine learning are directed to the author’s separate article on five beginner-friendly steps to learn ML.
- For those who have passed and joined the Google Developers Certification network, the author advises using the new skills to build things they want to see and sharing their work.
- The article closes by inviting readers with unanswered questions to email the author and mentions there is a video version of the article on YouTube.
