---
url: "http://www.drdobbs.com/architecture-and-design/what-makes-a-good-check-in/240168601"
captured_at: "2014-07-19T02:39:15-03:00"
title: "What Makes a Good Check-in? | Dr Dobb's"
domain: "drdobbs-com"
---

# What Makes a Good Check-in?

By Sven Erik Knop, July 08, 2014

[Comments](http://www.drdobbs.com/architecture-and-design/what-makes-a-good-check-in/240168601#disqus_thread)

Few organizations have strong opinions and articulated policies on what a check-in should consist of. As long as the check-in is more or less usable in a code review, it's generally considered good enough. We can do better than this by making the contents of check-ins truly useful additions to the development process.

The central unit of work within any version-control system (VCS) is the check-in: committing one or more files into a repository. This records the current state of the files and preserves a record of their history. In this article, I examine the wide range of check-ins — from the minimal to the overly large — and identify the elements of a useful check-in and the costs of doing check-ins wrong.

A database transaction is often described by its ACID properties:

- Atomic: All changes are committed together or not all
- Consistent: The referential integrity of the data is preserved
- Isolated: No partial or incomplete changes are visible to other users
- Durable: A committed transaction is preserved in non-volatile storage

A check-in to a VCS follows similar principles. A check-in is an atomic operation that makes previously isolated changes visible to other users. A check-in can affect several files to keep the project consistent, just as a transaction can update multiple records and tables at once.  (To be accurate, some legacy VCSs such as CVS or Visual Source Safe only allow check-ins of single files. However, all modern VCSs support atomic commits across several files.)

Ideally, every check-in should move the project from one consistent buildable and tested state to the next. The VCS ensures that the history of these changes is stored durably.

A check-in differs from a database transaction in that it preserves the history of changes, including the author, and usually some documentation (a comment or link to a change request).

### Similarity to Storytelling

Together, all check-ins tell the story of how a project has developed. The best stories have a strong theme, a fascinating plot, a fitting structure, unforgettable characters, a well-chosen setting, and an appealing style.

A good check-in is like a sub-plot with its own theme; it makes it easy and interesting for others to read and understand the purpose and execution of each change.

### Characteristics of a Good Check-in

A good check-in enables reviewers to assess the change quickly. It allows team members to evaluate the impact of the change to their parts of the project. It alerts build and QA engineers to potential modifications in the setup and notifies those responsible for documentation of any required updates. Finally, a good check-in is easy to debug, fix, or even to back out in case of a problem.

To achieve these desired features, a good check-in should have these characteristics:

**Single intent**  
A good check-in has a single purpose, usually defined before the first file is changed. Such a check-in is part of a single task assigned to a developer, or a development team, such as adding a feature or fixing a bug.

A check-in should not be a backup. Checking-in all changes of the local files because it is the end of the day or the beginning of the weekend is not a good idea. Some VCSs allow users to store intermediate changes in the shared repository without checking them in, an ability called *shelving* or *stashing*. This is the right place for such types of backup.

**Scope**  
A task is normally broken down into small subtasks, each with a well-defined purpose. For example, it could have the following stages:

- Whitespace and indentation changes
- Add missing unit tests
- Remove dead code
- Structural work, such as refactoring and scaffolding
- Finally, user-visible changes

Each subtask may have its own individual check-in, although they may be combined together in a task branch or decentralized repository. By keeping the changes small with a very tight scope they become simpler, easier to review, and easier to verify.

Small size also makes it easier to undo the change before the check-in or to propagate the change to a different branch. For example, if there were five different modifications, one of which needs to be reverted before check-in, all other changes would be lost as well. Stashing/shelving or branching helps only slightly, since the required changes still need to be extracted and merged back into the original task branch — with all the potential problems this conveys.

By breaking down the task into smaller subtasks and checking these in individually, these problems can be avoided.

**Description**  
VCSs usually require that each check-in have a description, but the content often varies in size and quality. Some teams have strict rules for descriptions — they are governed by conventions or even triggers that look for certain keywords.

A good description explains the intent and scope of the check-in. In some cases, a simple "*Fixed Indentation. No functional change.*" is completely sufficient to convey the purpose. In other cases, a more elaborate explanation may be better.

It is usually not necessary and often counterproductive to explain the precise details of the modifications within a check-in. This information is normally available by looking at the code differences that any VCS can provide. In some especially tricky cases, an explanation of the algorithms used might aid the reader in understanding what has happened.

Keep the first line of a description short to give a general overview. Many VCSs list information on a check-in with the first line of the description; keeping this line informative makes it easier to identify each change.

**Consistency**  
Consistency in a database transaction is defined as a change that preserves the referential integrity and constraints of the data. For a VCS, a good definition of consistency is that the project can be built and that it passes its tests.

This is even true when checking-in to a distributed VCS (DVCS) such as Git or Mercurial. A common strategy to find a bad check-in is to reload and test older check-ins starting at a known "good" state and moving forward in time until the culprit is found. It is very hard to investigate problems created by an earlier check-in if older changes do not even build.

Consistency also implies that each check-in should include test cases that verify any changes. Keeping features and their tests together makes it *much* easier to propagate a change to a different branch or repository. It is also useful if a change needs to be backed out.

**Completeness**  
A check-in should contain all changes necessary to build and test, as well as updates to the release notes and other related documentation. And just as with test cases, this type of comprehensive check-in makes propagation of changes easier and safer.

Any new APIs introduced in a check-in should be implemented with at least a method stub. For example, checking-in a new or extended class in a C++ header file without its implementation might pass the local build and test stage, but other users could experience build or even runtime errors.

**Pre-check-in reviews**  
Code reviews are a good way to improve code quality. Reviews can help spot simple mistakes, enforce coding standards, and avoid unintended side effects. Reviews also raise code awareness within the team, improving the team's productivity through reuse and quality of output.

Code reviews can be done in different ways, such as emailing a change around or pair programming. Nowadays, teams often use commercial, open-source, or even VCS-provided review tools.

One common workflow provided by these tools is a pre-check-in review: before the check-in to the shared repository, the user sends the change for review to other members of the team, who can vote on the change to be accepted or rejected. This includes *pull requests* popular among users of DVCS tools like Git and Mercurial.

Pre-check-in review can also include automatic review tools that perform a heuristic analysis and automatic builds and tests.

A good check-in will usually complete a full build and review cycle for verification before it is finally committed to the shared repository.

**Traceability**  
Many regulated industries such as financial services or manufacturers of medical devices need to be able to provide an audit trail for all changes made to their software. Each check-in must provide details on the author and the date, as well as potential authorization and a link to an issue tracker or documentation.

Triggers or similar mechanisms in the VCS usually enforce inclusion of these kinds of information.

**Reversibility**  
The best pre-check-in reviews and build tests cannot always prevent unintended side effects that appear in later testing. In such cases, it might be necessary to back out a check-in, which returns the state of the project to an earlier time. This operation usually preserves history as well, so that the change can later be reapplied or analyzed and fixed as necessary.

Keeping check-ins small in scope and dedicated to a single purpose makes them easier to back out.

### Examples of a Bad and a Great Check-in

Two examples might shed more light on the subject.

A few years ago, I was hunting down a problem with software running on a prerelease build of Microsoft Windows 7. During testing, the application crashed in a piece of code I had not previously encountered, so I traced down its origin to an obscure check-in from 1996. The description read: "*This is a change.*" The check-in modified one file without any code comments to explain its rationale. In the end, the problem turned out to be a bug in the prerelease build of Windows 7, which was later fixed, but the feeble change description has stayed with me ever since.

Sometime later, we hired a new server engineer who altered how I look at check-in descriptions.

I subscribe to receive emails on new check-ins into a repository. These emails contain essential information on the check-in such as the author, date and time, the list of files changed, the original issue fixed by this check-in, and the check-in description. Usually, these descriptions are quite terse, but they give a rough overview on what the check-in is about.

Then a new style of check-in arrived courtesy of our new server engineer.

Some of these check-in descriptions are epic. They describe not just what changed, but also the original problem, the algorithm used to solve the issue, potential side effects of the solution, and suggestions how to address them. These descriptions are occasionally four pages long and read like a good book on computer science. By browsing through these descriptions, I easily understand the reason and impact of a check-in without any need to read the code.

Obviously, not every check-in description can and needs to be so elaborate. The majority of check-in descriptions you would find on our server are still only one or two short sentences long. But for those changes that have a wider impact on other team members and the consumers of the resulting product, a comprehensive description of a check-in is the approach I recommend.

### Anatomy of a Check-in

Given the characteristics described above, here are the elements you should expect to find in a good check-in:

- One or more files or file patches
- A description
- The author of the change
- A timestamp

A good check-in might also store information on:

- The origin of the change (an IP address or the hostname), which can be useful when tracking problems for other users, such as OS or tool chain dependencies.
- A list of reviewers (potentially with their comments)
- A list of testers
- The committer of a change if the author has no write permission
- One or more issues or requirements

The exact composition of a check-in depends on the VCS and the rules set up for a particular team.

### Conclusion

Using a VCS has become a universally accepted best practice for any kind of development, but organizations vary widely in the care they put into check-ins. Lack of care regarding check-ins, however, is a form of technical debt that can demand payment at the most inopportune moments. Fortunately, a little discipline and forethought pays dividends. It will make the lives of reviewers, build and test engineers, as well as downstream programmers easier, and it will help ensure that your products can withstand the test of time.

---

[*Sven Erik Knop*](https://plus.google.com/102948730781964629417?rel=author) *is a technical marketing manager at Perforce Software, a vendor of version management technology. He has a background in physics, programming, and database administration, and trains Perforce customers on a large variety of topics. He resides in the UK and is on Twitter at [@p4sven](https://twitter.com/p4sven).*
