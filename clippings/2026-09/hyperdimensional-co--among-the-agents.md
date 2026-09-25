---
url: "https://www.hyperdimensional.co/p/among-the-agents?utm_source=tldrai"
captured_at: "2026-09-25T22:14:33+01:00"
title: "Among the Agents"
domain: "hyperdimensional-co"
---

In the past month I have:

1.  Automated invoice creation, sending, and tracking;
    
2.  Created scientifically realistic simulations of hydrological systems as a learning project;
    
3.  Automated my research process of gathering and analyzing all proposed state legislation related to AI (though this is no substitute for reading the bill for anything I am going to write about);
    
4.  Orchestrated a complex chain of autonomous data collection, processing, analysis, and presentation steps related to manufacturing and industrial policy;
    
5.  Created a machine-learning model capable of predicting US corn yields with what appears to be very high accuracy (the proof will be in the pudding), based on climate, soil, Earth-observation satellite, and other data sources;
    
6.  Replicated three machine-learning research papers and modified the approach to suit my own research ends;
    
7.  Performed hundreds of experiments with Byte-level language models, an emerging interest of mine;
    
8.  Created an autonomous prediction market agent;
    
9.  Created an autonomous options trader based on a specific investment thesis I developed;
    
10.  Built dozens of games and simulations to educate myself about various physical or industrial phenomena;
     
11.  Created an agent that monitors a particular art market in which I am potentially interested in making an acquisition;
     
12.  Created a new personal blog complete with a Squarespace-style content management system behind the scenes;
     
13.  Other things I cannot talk about publicly just yet.
     

Of course, I did not do these things alone. I did them in collaboration with coding agents like Gemini 3 Pro (and the [Gemini Command-Line Interface system)](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/), [OpenAI Codex](https://chatgpt.com/features/codex?utm_source=google&utm_medium=paid_search&utm_campaign=GOOG_M_SEM_GBR_Codex_TEM_BAU_ACQ_PER_MIX_ALL_NAMER_US_EN_111325&c_id=23226110534&c_agid=188421385415&c_crid=782421044798&c_kwid=%7Bkeywordid%7D&c_ims=&c_pms=9007535&c_nw=g&c_dvc=c&gad_source=1&gad_campaignid=23226110534&gbraid=0AAAAA-I0E5euPXesOYj5Wl90lTFVca7JZ&gclid=Cj0KCQiApfjKBhC0ARIsAMiR_ItwlupyypRUt-B0GGU1FtPEc-El4LhNg956gPmxWX9wgQGufFZPFscaAsUaEALw_wcB) using GPT 5.2, and most especially, Claude Opus 4.5 in [Claude Code](https://code.claude.com/docs/en/overview).

These agents have been around for almost a year now, but in recent weeks and months they have become so capable that [I believe](https://x.com/deanwball/status/2001068539990696422?s=20) they meet some definitions of “artificial general intelligence.” Yet the world is mostly unchanged. This is because AGI is not the end of the AI story, but something closer to the beginning. Earlier this year, I wrote:

> The creation of “artificial general intelligence,” if it can even be coherently defined, is not the _end_ of a race. If anything, it is the _start_ of a race. As AI systems advance by the month, the hard work of building the future with them grows ever more pressing. There is no use in building advanced AI without _using_ those systems to transform business, reinvent science, and forge new institutions of governance. This, rather than the mere construction of data centers or training of AI systems, is the true competition we face—and our work begins now.

The individuals and firms that discover more and better ways to work with this strange new technology will be the ones who thrive in this era. The countries where those people and businesses are most numerous will be the countries that “win” in AI. It is up to all of us, together, to figure out how to put machine intelligence to its highest and best uses. The world won’t change until human beings change it.

I joke sometimes that using AI, and especially using coding agents, is a bit like playing the piano. The piano is the easiest instrument to begin playing (anyone can produce a satisfying tone with no training or skill on a piano, which is not true of, say, a flute or a violin), yet the hardest to master in the long run. AI presents the greatest opportunity and the greatest challenge computers can muster: a white sheet of paper, a blinking cursor in an empty text input box. You can type anything you like, but figuring out what to type, is, indeed, the hard part.

It is especially important, I think, that as intellectually diverse a group as possible experiment with these coding agents, which I have taken to calling “infant AGI.” Because while the primary focus of these tools is indeed coding, they are useful to far more than just coders. Whether you are a scientist or a policy professional, a linguist or a diplomat, a literary critic or a musician, or just a curious person, I am confident these tools have something to offer you.

I am a somewhat odd duck in all this, being a “humanities person” who also learned to code and hack around on a computer at a young age. Therefore I feel it is especially incumbent upon me to demonstrate how coding agents can be useful to non-coders of all backgrounds, ages, and interests. Today, I’d like to do just that. I hope it is useful to as broad a range of people as possible, and in service of that goal, I am going to write assuming no prior experience with coding agents, command-line interfaces, or coding. I apologize to the more technically inclined people in my audience, for whom some of this will be old news. After that, I will close with some brief and tentative observations about what these new coding agents might mean in 2026 and beyond.

Coding agents are language models situated within attendant software infrastructure (variously referred to as an “AI system,” “agent scaffolding,” or an “agent harness). There are many apps you can download that allow you to use coding agent, like [Cursor](https://cursor.com/), [Windsurf](https://windsurf.com/), Cognition’s [Devin](https://devin.ai/) (which is more focused on enterprise uses), [Factory AI’s Droid system](https://factory.ai/product/ide), or Google DeepMind’s [Antigravity](https://antigravity.google/). But if you are new to coding, I think many of these tools could overwhelm you at first (though you may want to try them after you gain experience). They are what are known as integrated development environments (IDEs), with more of an emphasis on looking at and editing code than is in fact necessary for most new users.

Ironically enough, I think the best way to begin using these decidedly futuristic tools is within the most ancient personal computing interface there is: the command line. A command line is a text-based way of controlling computers. It is often far more efficient, if less intuitive, than using a graphical user interface (GUI) with windows, a mouse cursor, and the like.

For example, say there was a file on my computer called “agi\_is\_here.txt” but I decided that I wanted to replace every usage of the acronym “AGI” with “transformative AI” instead. With the GUI on my Mac, I’d open Finder, navigate to my Documents folder (or wherever the file was saved), open the file in a text editor, and then use the editor’s “find and replace” function. To do this at the command line, I would open the “Terminal” app on my Mac and type:

```
cd ~/Documents && sed -i ‘’ ‘s/agi/transformative ai/gI’ ‘agi_is_here.txt’
```

This may look alien to those who are not familiar with command-line interfaces, but it is a remarkably compact expression of a complex user intent written in a scripting language called “bash.” Just as one example, the “/gI” flag at the end stands for “global,” meaning by desire is to replace the phrase throughout the whole document, and “Insensitive,” meaning I want my search for instances of “AGI” to be case insensitive (“agi,” “aGi,” and so on).

One important note: terminal apps are called “emulators” because they emulate the experience of using a pre-GUI computer. This applies to input devices: there were no mice back then, so there are no mice in emulators now either. You cannot click anything within the window of a terminal emulator. All input is keyboard only. Some of the keyboard shortcuts you are used to will still work, while others will not (for example, on a Mac, Command-A as “select all” will likely not work the way you expect in Terminal, and what you are probably looking for is instead Control-U). A list of default macOS Terminal keyboard shortcuts is available [here](https://support.apple.com/guide/terminal/keyboard-shortcuts-trmlshtcts/2.15/mac/26).

Anthropic’s Claude Code, OpenAI’s Codex, and Google’s Gemini CLI are, properly speaking, applications that run through the command line on your computer. After you install them, you open the terminal emulator on your computer (on a Mac, this is the app called “Terminal”) and you type, variously: “claude,” “codex,” or “gemini.” The app will then launch. At this point you are communicating with a language model.

The language model is running in the cloud, but it can read and modify files on your local computer. So, to continue the above example, instead of writing the complex bash command above, you could simply say “I’d like you to find the file called agi\_is\_here on my computer and replace all references to ‘agi’ with ‘transformative ai.’” This is trivially easy for a frontier coding agent, yet this alone is a more sophisticated use of computers than the vast majority of people are capable of doing.

Because command-line interfaces are entirely text based, it should not surprise you that language models have gotten _very_ good at using them. _This means they can use your computer_, _and the computer is one of the most powerful tools mankind has ever invented._ You talk to these agents just like you talk to the chatbots, but they can do vastly more than a chatbot can do, because they are operating your computer for you.

Agents like this have been around for almost a year now, but I found them insufficiently reliable until roughly a few months ago (it also did not help that between April and August I was working for the government, and in addition to being too busy to play around with new tools, you cannot, for obvious reasons, run coding agents on computers owned by the Executive Office of the President). And reliability matters tremendously here, because it is easy for things to go wrong. For example, you could type somethings as simple as:

```
rm -rf ~
```

This command deletes everything in your user directory, which probably means all your files, photos, downloads, and the like. There is no dialogue box asking you if you are sure you wish to do this. It will just happen. Command lines can be dangerous. It is incumbent upon model developers to train progressively better models that avoid these kinds of failures, and to design interfaces that allow for appropriate human oversight of agents. But just as importantly, it is incumbent upon users to understand what agents on their computers are doing and understand when circumstances merit additional scrutiny.

This is why all coding agents will require explicit user permission to perform certain actions (though you can configure this). If you have any uncertainty about an action a model is requesting your approval for, remember that you can always ask the model itself why it wants to do what it is doing.

Even with user permission, there are some failures modes to be aware of. First of all, coding agents tend to be quite sloppy in their use of APIs, the means by which a software engineer makes use of some service or software in code. Agents tend to expect APIs to be robust and performant; this is often not the case in the real world. They also tend to not think about things like rate limits. This can mean that, unless they are specifically directed to carefully examine the API documentation and design around its constraints, they will end up getting blocked for violating API rules or rate limits.

It is also the case that agents still tend to be overly confident in tackling ambitious tasks. They seem to have an innate desire to “wow” the user with an impressive result delivered on the first try. This desire gives them an incentive to declare victory too early. I deal with this problem by asking agents to write robust plans before beginning work, and if they are building software apps, to craft complete lists of features along with methods of verifying the completion and quality of each feature.

Once you get going, there are three important and non-obvious-to-a-beginner facts to internalize. One we have already discussed: coding agents can operate _a lot_ of your computer’s functionality_,_ but importantly not all of it, purely through the command line. Second, coding agents can download arbitrary files from the internet. Third, agents can orchestrate cloud computing infrastructure; they can manage cloud-based virtual machines, and AI hardware, from your command line. They can also, themselves, use the APIs for any LLM or other AI tool; your agents can, themselves, use AI. Used with appropriate discretion, each of these capabilities is profound.

There are many finer points, and other AI coding applications beyond the raw command line (even Codex, Claude Code, and Gemini have GUI-based apps as well). I recommend reading Claude Code creator Boris Cherny’s [recent thread](https://x.com/bcherny/status/2007179832300581177?s=20) as a starting point for learning about these finer points.

What do the coding agents mean? I have only tentative thoughts to offer at present, and much is unknown. A few things, however, seem clear:

1.  Coding agents mean that you can try more things for yourself, instead of being dependent upon companies or expert individuals to intermediate. In the last one to two decades, the digital world has become complicated, so filled with walled-garden services, that most of us have become infantilized. Coding agents mean you can, once again, become something more like a digital frontiersman.
    
2.  Because you can speed run the creation of so many complex software engineering projects, you can learn more quickly the tradeoffs, largely unspoken limitations, and other tacit knowledge intrinsic to all complex endeavors. Intermediate-level knowledge of this kind—things like, “oh yes, that API regularly breaks in this silent way,” or, “oh yes, there is an intrinsic tradeoff between X and Y that must be balanced appropriately”—can now be acquired rapidly in a process of human-AI hybrid exploration.
    
3.  The fundamentals of many disciplines, most especially computer science, still seem quite relevant to me. Learning the basics of why computers work is extremely useful for making the most of coding agents; it will make you a better “prompter.” Learning the foundational aspects of programming languages similarly seems important. Understand how to think computationally now matters more. Understand the specific syntax of a particular programming language now matters less. This same lesson may well apply in other disciplines. It may therefore be possible to be a renaissance man once again.
    
4.  Proprietary access to data will become even more of a key differentiator than it already has been. On the flip side, publicly releasing datasets is one of the highest leverage things researchers, governments, and research institutions can do. The social status of releasing differentiated datasets is probably still too low.
    
5.  The definition of a good “user experience” in software will change profoundly. The value of a highly polished UI in many heretofore consumer and even many enterprise applications will decrease; the value of a performant, reliable, extensible API will increase. Walled gardens will be an increasing source of hassle and frustration for general consumers. This frustration with walled gardens has always existed within software-engineering and otherwise technically savvy communities; coding agents will make those cultural trends more prevalent among “normal” people. I would therefore expect more members of the general public to adopt, on the margin, the dispositions, preferences, habits, predilections, and the like of software engineers.
    
6.  The value of unsexy services that provide access to raw capabilities or data with minimal intermediation will go up. Currently, consumer and enterprise software-as-a-service prioritizes a great user interface—making it easy for a nontechnical user to get started. But the tradeoff is often that they impose a lower ceiling of capability. Now, there are many software services where human usability is a far lower priority, and instead the premium will be services that give AI agents maximal leverage and flexibility to accomplish a wide variety of goals. A simple—probably too simplistic—way of phrasing this would be to say that applications will come to matter less than infrastructure.
    
7.  This may well apply to hardware as well. One can imagine, for example, that home automation devices that charge a premium for a great consumer experience will become somewhat less desirable when compared to cheaper, equally capable, and far more extensible competitors. Think about the difference between companies like Ubiquiti and Eero in the world of wireless networking; Ubiquiti is extremely high quality but requires much more technical expertise to manage. One can imagine many areas of consumer goods where this will be true.
    
8.  Very few people have made truly great products and services that target the “prosumer using coding agents” market. Those that have, have largely done so unintentionally. There is probably a large and growing opportunity here.
    
9.  While the above trends create opportunities for new firms, they will also create opportunities for incumbent firms to put up roadblocks. Firms that control some proprietary service, data, or other well-defended moat may be disinclined to offer their products in ways that maximally enable AI agents, fearing that their differentiation will be eroded into a commodity over time. I expect this dynamic, which is common with new technologies, to persist for years if not longer and represent one of the most concrete barriers to AI adoption in the real world.
    
10.  I would no longer be surprised if we saw AI in the macroeconomic statistics by the end of this year, both on the upside (growth, productivity) and downside (labor market dislocation).
     
11.  Defining what good looks like, and convincing others your conception of “good” is the right one in a particular context, will remain the human touch. Jobs that require this already, of which there are many, will be well-defended. Jobs that solely require the production of discrete, well-defined outputs are vulnerable.
     
12.  State governments will introduce hundreds of bills about artificial intelligence; almost none of them—perhaps even literally zero—will be written with coding agents in mind. They will be chatbot regulations. It is quite possible policy debate America will have in 2026 is already antiquated.
     
13.  By the end of this year, the least important thing you will be able to do with frontier AI systems will be getting chatbots to answer questions, but this is still how most people will think of “AI.” Expect cognitive dissonance as a result.
