---
url: "https://medium.com/@idankoch_32247/the-ultimate-checklist-to-becoming-a-development-team-leader-77faf921208d"
captured_at: "2024-12-04T22:59:44+00:00"
title: "The ultimate checklist to becoming a development team leader"
domain: "medium-com"
---

[

![Idan Koch](https://miro.medium.com/v2/resize:fill:88:88/0*EhG6uj-7kx6CUMsY.)

](https://medium.com/@idankoch_32247?source=post_page---byline--77faf921208d--------------------------------)

9 min read

Jun 27, 2024

\--

My name is Idan Koch, I’ve been working in high tech in various roles for over 2 decades. During this period I had the great pleasure of working with immense talents and great people. Over the years I took an active part in the team members growth process and was an observer of talented developers making the shift to different positions. The most common use case I encountered were developers moving from individual contributors to team leader roles. Usually the question is **“what do I need to do to show I’m ready?”**

Tesha leading by example

While navigating your career, sometimes it is unclear what needs to be done to advance to your next role, may it be as a technical leader, team leader, group management or anything else. There isn’t always a clear guideline in companies about what needs to be achieved to get from A to B. However, for the shift from IC to TL over the years I made a simple checklist for any developer wanting to make this shift to go over. This list is based on my experience, not all items are a must, some can be ruled out depending on previous experience or company’s expectation of the role. However, I will say from my extensive experience in this matter this list is pretty solid across the board.

1.  **Conquer your domain**

Becoming a TL will require you to represent your team in various technical and design meetings, answering questions from inside the team and outside of it and either be responsible or assist in production incidents. In order to be up to the task you should do the following:

_1.1. Deliver like a motherf#%&r_

You can read documents, watch recorded sessions and be in meetings. For me there is no substitute for writing as much code in as many services/business flows as you can. Even if you become a TL in a different group/company this skill of diving head first into various chunks of code helps you understand the domain faster, learn your stack faster and understand the pain points of development. Sometimes your team’s responsibilities are very extensive with many services, so it is hard to cover everything. My advice would be to try to do a bunch of small tasks around those services. Small tasks lead to quick wins which is always a great feeling to check off tasks, but more importantly give you a taste of everything. You will cover different flows, different solution considerations, different SLAs and different technologies.

_1.2. Become a production hero_

This section depends on your job description, some developers are detached from production. However, if you are lucky enough to have production responsibility, then as a technical leader you will either be in the driver’s seat when shit hits the fan or provide backup to your colleagues. Handling production incidents will help you grow. A few key points about production incident management:

_Tools of the trade_ — learning tools such as: profiling, log tracing, testing in production, mitigating different issues with different solutions will give you understanding not only how to solve issues, but mainly will give you a way to think about problem solving.

_Stress reduction —_ There are developers that are inherently calm under any production pressure by default, it is OK if your not. One way to lower your production anxiety is exposing yourself to it as much as possible. The only way to learn is to jump in. You can start by “shadowing” the oncall person and assume incident management gradually over time. After a while you just get used to it.

_Bug hunts —_ You don’t need to wait for an incident to happen, you can be proactive to find issues. At times incidents fly under the radar and go unnoticed, could be missing alerts or old service that dont have new requirements and are neglected. In my group we do periodic bug hunts where as part of your oncall you select a service and deep dive it and present it to the rest of the group. In the bug hunt we start with service spotlight where you discuss the service responsibility product concerns showing examples of user flows in UI. After that we take a look at the service technically. Examining resilience issues, think about fallbacks in case of failures, check which health tests are running, find cutting cost opportunities, go over exceptions see if there is anything interesting to handle, make sure you have all the dashboards and alerts you expect there to be, go over past post mortems and most importantly create action items and create backlog of items that will improve the quality of the service.

_1.3. providing support_

Often your team receives inquiries from other teams. The questions may vary from API questions, to how flows work, production assistance and more. This usually leads to deep diving into old code and asking around why things are like they are. Answering questions will help you establish your knowledge on the team’s domain outside of your daily tasks. Additionally, answering as many questions as you can will help you become a focal point of knowledge.

**2\. Onboarding**

Leading others will require you to juggle between your tasks and helping someone else with theirs, having constant context switches and knowing how to handle them. For example, a new team member turns to you every 2 minutes with a question. You can answer every question immediately, but you might not get anything done. An alternative would be to say “Let’s set a 1 hour meeting after lunch. I want to put the final touches on my PR so I can focus on your questions”. Fortheremore, You will learn the subtle art of knowing when to let others “struggle” a bit so they can learn how to learn and when to dive in and help. So how do you practice those skills before becoming a TL?

I personally find it extremely useful to have the last person that has boarded on the team to be the “buddy” of a new team member. Helping them get a handle on things, understand key personnel to turn to, what are the processes used in the company/team, help them with coding style, lead them to the “right” place to eat lunch … all questions big and small (lunch is by far the biggest). This phase is great since it first tests your own knowledge. Best way to know that you actually know what you are talking about is by explaining it to someone else. You will find gaps in information, that is OK, it is even great. Most importantly, it is a hands on experience in leading someone else, this will help you understand if you actually like it or not.

**3\. Big tasks**

From time to time you will get a task that is not a quick win. Handling big tasks will require months of development, Integrations with other teams and setting expectations with the product team. As a team leader you will have to not only know how to do this yourself but also help others. When you start your development career you start this journey with the help of your manager while focusing on:

_requirements_ — Collect all the requirements and give feedback, ask hard questions (like this be phase 2?). Understand current flows how and why they are implemented as they are? Make sure you know the impact of this new feature, how will this make the life of our users better?

_Design —_ So you collected all requirements, now you need to meet them. You need to have a design that addresses all requirements (usually there is more than one). Design reviews with all technical parties are needed to get feedback and create action items to flow up. This process can have several iterations, at times even going back to the requirement phase. It is your job to make those iterations as short as possible. You will find “shortcuts” like getting feedback from specific technical focal points before the review to raise concerns faster or even just creating a slack channel dedicated to the feature which allows you to share information and questions to a wider audience.

_Dependencies —_ Even though it is part of the design part it deserves its own section. Often than not you depend on other teams. You need to understand their domain to some extent. You need to understand their challenges, is what you are requesting of them is even feasible with their current system. You need to understand how long it will take them to hold up their end. Lastly, you need to understand where their priority is. Can they meet you at the integration points? Do you need to raise a red flag when there is risk of non commitment from other teams? Know who to ask for help to get priority from other teams. Maybe code contribute if needed.

_Have a plan —_ Break everything down to small tasks. Mark dependencies between tasks, which task blocks other tasks. Mark tasks that can be done in parallel (in case you get extra hands to help you). Set exact timelines (as much as possible) for deliverable and integration.

Time estimation is always tricky, the process of time estimations, at times, teaches you not to be too optimistic, sounds depressing but actually it is key to free yourself from future stress. You will need to remember when you are oncall, when there is a company meetup, when your kid’s soccer game is held, holidays or any other obligation you might have will have an impact on delivery dates. If possible leave some room to breathe, big tasks are marathons. There are unexpected events happening along the way, context switches will happen. My rule of thumb is if you don’t know how to estimate the unknown make sure you have an additional 20% of time. Usually extra time needed for integrations, production testing, bugs or those wonderful days when the build is broken and you need to spend a day figuring out why. So for example: if the task takes a month to complete probably more realistically you will need an extra week for it.

_periodic checks —_ Periodic check meetings with your manager and peers will help you to make sure you are on track. Sometimes when we are in the thick of things we lose sight of the big picture. We need to zoom out of the task at hand and look at the whole board.

**4\. Big tasks — you are on your own**

This time do it yourself. obviously consult with your managers and peers but you lead the way. prepare the design document, talk to other companies, give the estimate, set the design meeting, basically do anything and everything to move things along.

**5\. Big tasks — lead others**

This is not a must, however, in my opinion a clear sign of readiness to be a TL. When you have a big task and you need to help lead other teams technically, product, timelines. This gives you a taste of being in other people’s shoes, understanding their challenges and helping them overcome them to get to the greater goal.

**6\. Meetings — optional step**

Big part of being a TL is being in meetings. Design reviews, technical consultations, brain storms, work process reviews. Even if you are not lecturing in a big conference you will find yourself standing in front of other managers and other big shots in your company while you explain technical issues, design concerns, lead discussions and answer to feedback. You will have to organize your thoughts in a clear way so you can deliver your message properly. Your managers will gain confidence in you when they actually see you in this setting. I will admit this step is a bit more mercurial, it’s not always a must and at times can be on the job training. However, if you get a chance to try it, it will help you progress and grow. Additionally, if you see someone else that holds complex meeting and navigate through the sea of challenges and ego to the promise land of action items — then ask yourself how did they achieve this? What preparation was needed? More specifically, if you see someone that you want to “model” or take “aspects” of their professional skills and adapt them, ask them questions. Maybe you will get lucky to get them to be your mentor. Mentorship is an awesome way to progress your process by having someone external follow challenges, give you advice and impartial feedback on your progression.

**In Summary:**

When a team member wants to journey and transition from developer to team lead I would reflect them my expectations:

1.  Deliver as much as possible.
2.  Be on top of all production issues and support questions.
3.  Get a taste by onboarding others.
4.  Take on big tasks first together with your TL, then lead the way alone.
5.  If possible, lead “important” meetings.

Feel free to hit me up in the comments section, I would love to get feedback on what you think about this list or just learn what are the processes you have installed to help teammates grow to technical leadership positions.
