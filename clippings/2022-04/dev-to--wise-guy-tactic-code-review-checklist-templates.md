---
url: "https://dev.to/emphie/a-wise-guy-tactic-for-effective-code-review-practice-use-checklist-templates-3mel"
captured_at: "2022-04-06T08:59:58-03:00"
title: "A ‘wise’ guy tactic for effective code review practice? Use checklist templates!"
domain: "dev-to"
---

I think everybody agrees on how important and useful practicing code review is. It helps you catch bugs early in the process and reduces long-term development time. It also has the benefits of sharing knowledge, improving estimation skills, and keeping the code consistent with established conventions within the project. In one sentence - it improves the overall quality of code. But how do you do it like the 'wise guy' from this article's title? The answer is simple.

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fv4i4wxieomdmr41gq7tc.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fv4i4wxieomdmr41gq7tc.jpg)

Sometimes being a developer is all about trying to be structured - simply following rules and using the right tools. I know that performing Code Review (CR) can be a problem for some devs. To avoid all the traps and make the whole process easy and effective I recommend using checklists. They should be the first choice when you're performing semi repetitive tasks. So what's the argument against using them as templates? Yea, I don't know any either.

**Basic rules - keep the lists short**  
The principal rule is to keep it simple. Lists that are too long are overwhelming and can backfire. Stick to the fundamentals and focus on the most important parts, however, it is meant to be useful so don’t hesitate to fit it to your needs. Rules should be listed in a specific order, because in most cases if one of the points is not fulfilled you should stop reviewing and contact the author. Of course, a checklist is beneficial not only for the reviewer, but the author of the code should be able to use it before submitting PR to remove obvious mistakes.

**Automated tools are the key**  
Any automated tools that are used in a project must succeed. If any static program analysis or automated test reports a problem it has to be fixed before review. Automats are the first obstacle you need to overcome to start CR.

**Are changes ready to be merged?**  
If PR has conflicts with the target branch there is no point in checking the code because you will probably need to perform a review one more time. This should be obvious, but often changes that are merged earlier can lead to new conflicts, and resolving them is the responsibility of the PR author.

**Are commits messages correct?**  
Before you take a look at the code, check the commits messages. Comments like “Minor fix” or “Added new feature” are meaningless. Developers must stick to the commit convention used in the project, with no excuses.

**Is PR small enough?**

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fyti67qy98w6uww58eip4.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fyti67qy98w6uww58eip4.png)  
Neither you nor me have Chuck Norris' skills. Our perception is limited, so if PR consists of 3000 changed lines, you will have problems understanding changes. Remember to keep it small, but without forcing strict limits, because it needs to be flexible. If you have worries that your PR is too big, it probably is, so just check out the new children’s branch.

**Are requirements met?**  
Requirements are the reason why the feature branch exists, so always check if changes fulfil them. Believe me - you don't want to spend time reviewing the whole code if requirements are not met. Been there, done that. Don't recommend it. Check ticket description, look if something is missing or is incorrectly implemented, and immediately report to the author if there is a problem.

**Do you understand the code?**  
The question may seem odd, but it's important. To perform CR you must understand the code and be able to do it in a reasonable time. So code should be self-explanatory. If some functions don’t make sense or classes look messy, the code probably needs to be reorganized. You may be the next developer working on this part of the code, so take into account that this code will be merged to the main branch after your acceptance. Clicking the merge button or accepting the code review means you are now sharing responsibility.

**Dev's first commandment - stick to the coding guide**  
I'll say it one more time - always stick to the coding guide. No excuses. Ever. Check if everything is correctly named, files have the correct structure and if the approach is consistent with principles, DRY, SOLID, or any other clean code rules team is using.

**Do we need a library for that?**  
Libraries are a double-edged sword. Sometimes developers import huge and resource-consuming libraries and use only one function. It is only justified in cases when we can use more of it in future tasks. The second case is when developers add libraries that are similar to one already present in the project and duplicatesare never welcome. The last thing is to check is if the library is not maintained any longer or marked as deprecated

**Duplication is not welcome**  
In most cases finding unnecessary duplications can be a part of the coding guidelines, but it is worth mentioning it as a separate point on the checklist. New team members in particular can have problems with creating duplications, so just point out which part of the code they should use. There is no need to reinvent the wheel, use language features and already existing functions instead of implementing similar features.

**Test, test, test!**  
Yes, writing tests is also part of a task so check if they are correctly implemented and cover all coding paths. Just like normal code, tests should also meet coding guide standards and be consistent with project assumptions. Verify that all tests are passing for the right reason and take a second and think if there are any edge cases that haven’t been tested.

**Documentation is a must**  
Right now you and the author of the code know what is going on. But will other team members be able to easily catch up and use or develop it? If you are reviewing API - check if all endpoints are correctly notated and documented. For frontend checks, you can confirm if everything is available at Storybook or another component explorer. Any libraries used or architecture solutions must be put into a decision log.

**A ‘wise-guy’ conclusion ;)**  
This article provides you with several suggestions, but a good CR checklist must be agreed with the whole team. Keep in mind that checklists should be a live organisms, if you encounter problems in the development process just add new points or keep more than one type of CR template based on task type.

**_There you have it. Good luck with your next code review!_**
