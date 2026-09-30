---
url: "https://blog.devgenius.io/the-hardest-thing-about-engineering-is-requirements-28a6a70c4db4"
captured_at: "2022-03-26T19:52:50-03:00"
title: "The Hardest thing about Engineering is Requirements"
domain: "blog-devgenius-io"
---

Top highlight

# The Hardest thing about Engineering is Requirements

One of the hardest things about being a software architect is gathering requirements. You can work with the greatest team of rockstar engineers on the planet and build the most amazing piece of tech ever seen. So great that you could trick most people who see it into believing it is magic but yet if it is not what the stakeholders wanted or what the market needs it is as worthless as a USB hamster wheel.

USB Hamster Wheel

## Why is it So Difficult

If you are willing to sit and analyze for a few minutes the statement “The hardest thing about engineering is gathering requirements” you might realize you can generalize that statement a bit more and get to the actual root cause of the problem. The hardest thing about engineering is communication. Engineers are constantly working to communicate complicated abstract ideas. Most often these ideas fall into a problem space that requires some domain knowledge to understand. The conversations are full of acronyms and invented terminology that have become the nomenclature of the target industry. It is different for every industry and worse than that it is different for every discipline. The software engineers don’t speak the same language as the firmware engineers who barely understand the electrical engineers who don’t even want to talk to the mechanical engineers. This whole situation makes for a communication nightmare.

## List of Shalls

Now that we agree communicating ideas is hard let’s investigate some techniques to do just that. The first technique, it seems that every fledgling engineer tries is capturing requirements as “The product shall” statements.

- The product shall interface with the user.

- The product shall not catch on fire.

- The product shall fetch the user coffee.

Ok so not quite so absurd but if you give stakeholders a laundry list of features the product could do they will likely respond by nodding their head yes and then adding a couple of additional requirements that the product shall do. What seems to be going on here is that it is cheap and easy to add requirements to the product. No real thought needs to be put into why the requirement should exist. No work is required to add the requirement to the list. Any crazy idea that comes into the stakeholder's head can be captured as a requirement and now the development team must try to implement it.

The inevitable feature creep that comes with the laundry list of requirements causes more problems than just causing the dev team a lot of work. Oftentimes these requirements are conflicting making the product actually impossible to build.

- The product shall draw red lines

- The product shall use blue ink

Some requirements analysis would quickly uncover an issue as blatant as this but most of these types of conflicts will be more subtle. All will cause an additional meeting with the stakeholders to decide which requirement should be upheld.

Perhaps the biggest problem with the list of shalls is the fact that it doesn’t give the stakeholder a feeling of how the product behaves. There is a long list of things the product needs to do but no information about how the product will do it. Without a feeling for how the user will interact with the product stakeholders often seem to be less engaged. They start to take the approach of indifference with the requirements solicitation phase so that development can “hurry up and start” so that they can see how the product works. This ends badly because it results in changes at the end of the project when refactoring is expensive.

## User Stories

The agile boys use user stories to capture requirements. A user story is a statement in the format “As some user, I want to do some action so that some reason”. This is a slight improvement over the list of shells. These encourage the stakeholders to at least think about who and why a requirement should exist. When a stakeholder blurts out some requirement it gives the architect a chance to have a conversation. “That is a great idea Mr. Stakeholder! Let’s try to capture this as a user story. As a… which user wants this again?”. The negotiation can begin and the group can decide if this is a real requirement or not.

The problem with user stories is that they are designed for teams where the stakeholders are working closely with the development team. In these environments, stories are constantly added, removed, reprioritized, and discussed. Before every story is built the team gets together and discusses the details of how the feature should work. The development team also has access to the stakeholders while the feature is getting built so that any questions can be immediately clarified. In many situations, this is not possible. Stakeholders are not accessible don’t have time or maybe have even moved on to other projects or left the company. When this happens the development teams are left with a bunch of sentences that really don’t describe what the product should do but rather only contain a high-level vision of what some users might like to do in a science fiction version of the world.

The other shortfall of user stories is that they are not detailed enough to be used as any sort of agreement between two parties. If a contract is required I would not sign my name on a list of user stories that should be built on any sort of budget. It is too easy to interpret a one-line sentence in multiple ways. Saying that one interpretation of a user story is better than another is like saying that the Catholic interpretation of a bible verse is better than the Mormon interpretation. Leave theological discussions out of engineering whenever possible.

## Use Cases

Use cases are a more formal way of capturing requirements than user stories. Wikipedia defines them as “a list of steps, typically defining interactions between a role”. Similar to user stories use cases talk about the user that will be performing the activity but unlike user stories, they are not a single sentence. Instead, they go into the detail of exactly how the user will interact with the system step by step. Well written use cases will also cover error conditions and alternative flows.

Development teams love all this detail. It is exactly what they want to be able to build and test the system the users want. Stakeholders seem to be on the opposite side of the fence here. In my experience, they hate use cases. All these details are boring to read and tedious to write. Finding stakeholders who are willing to review even a small set of use cases is unlikely. Stakeholders who are willing and able to help write use cases are unobtainium.

## User Cases

We have determined that user stories are too vague to be used by the development team to work independently and use cases are too detailed to be useful for communicating with stakeholders. What we need is something that meets in the middle. My current solution for this is what I’m going to call a user case. A user case is just the combination of a user story and a use case. The stakeholder writes a standard user story. This is used as the title of the requirement and has the same effect of creating some overhead, thought, and discussion before the requirement is added. The discussions that take place about how the user story should actually function are captured as use cases of the user story. Additional use cases, alternative flows, and error paths should be added as the details of the story become more clear.

This method has some fairly interesting results. First stakeholders continue to be engaged because they are writing the user stories and perhaps even the initial happy path use case at a high level. They have the time to review these requirements because they only read carefully the user stories and perhaps a couple of use cases where they are concerned with the functionality. In other words, they don’t get bogged down in details that they don’t have time for. On the other hand, the development team is able to add the detail they require right in line with the text designed to communicate with the stakeholders. That gives them some level of comfort that when this document is finally agreed upon there is enough detail to avoid those arguments over the interpretation of the feature.

Yes, I realize I contradicted myself above because I said that the stakeholders will not read and understand all the use cases and the development team assumes they did. This is sort of the dirty trick of this method. Basically, the development team is asking “You read all the fine print didn’t you? Ok then initial here and sign here”. Unfortunately, if stakeholders do not have time to be involved during development and also do not have time to fully understand all the details then the third best is all we can hope for. The third best seems to be to provide stakeholders with a summary and all the details and let them decide how best to use their time.

## Rapid Prototyping

The last method I have been considering to capture requirements is rapid prototyping. Unfortunately, stakeholders often need to “feel” the product to understand what they want. None of the techniques mentioned above are capable of communicating a feeling.

I have little experience with rapid prototyping tools but recently I played with one and was quite impressed with the progress that has been made. The tool was easy to use and still gave a good impression of how the user would interact with the product. It was capable of generating documentation from the prototype that resulted in a nice set of screenshots that could be augmented to create a paper trail. It seems possible that very soon, if not already, it will take less time to prototype a solution than it will to properly document the requirements.
