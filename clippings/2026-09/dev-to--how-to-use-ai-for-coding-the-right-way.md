---
url: "https://dev.to/jasonleowsg/how-to-use-ai-for-coding-the-right-way-4cdn?ref=dailydev"
captured_at: "2026-09-25T00:14:18+01:00"
title: "How to use AI for coding the right way"
domain: "dev-to"
---

Devs: "Yeah Cursor/ChatGPT/AI is great and all, but you still need to know what you want, or know how to check for hallucinations. A complete beginner won't be able to code working apps with it."

Not really true anymore..

I've been coding in an unfamiliar language (Ruby) for a freelance gig, and PHP for personal projects, so I’m often unsure how correct looks like.

What I do to make sure it's correct:

– **Overall approach**: Using AI for coding is like having a super knowledgeable programming intern who's knows everything but not so good at applying said knowledge to the right context, and we just have to help nudge it along. Put another way, Claude/Cursor are like outsourced devs, and my work mostly is managing them, pointing them to the right direction. More creative direction than actual coding. I think 80% of my code written by AI now, but that doesn't mean I can fall asleep at the wheel. I got to stay alert to errors, follow conventions, check their work all the time.

– Before I start, I chat with Claude 3.5 Sonnet on Cursor on the **broad steps to take**, the overall architecture. Progressive prompting. I can reference the whole codebase with Cursor for context. Only use Sonnet. Not Opus. Not Haiku.

– I also add **system prompts** or "rules" for Cursor to give it a better context frame from which to answer. Adapted the prompt from the [Cursor forum](https://forum.cursor.com/t/share-your-rules-for-ai/2377/3). It goes something like "You are an expert AI programming assistant in VSCode that primarily focuses on producing clear, readable Python code. You are thoughtful, give nuanced answers... "

– In Cursor setting, you can also **upload documentation** of the framework, language or gems/packages you're using, so that it can refer to it for best practices and conventions.

– **AI can be not just coder but also code reviewer**. Get it to review its own code, using prompts like "Any mistakes in this code?", "Does this follow best practices for Rails/PHP?" Sometimes I ask "Does it follow convention in this codebase?" and @ the entire codebase and @ the documentation of the language.

– Sometimes I use a **different LLM to as a checker**. I open a separate window, and get Llama 3.1 or GPT-4o to double check the code for bugs. It's like getting a second opinion from a doctor.

– Share error messages, highlight the code, cmd-L and link the right files to **give it enough context**. I can't emphasize this enough but with Cursor, using the @ to link the right files/components, or even a docs on the internet, is killer. It's tempting to @ the entire codebase every time but from personal experience/observation, giving too much context might hinder too, make it 'confused' and it starts hallucinating or giving weird suggestions. There seems to be a sweet spot in terms of amount of context given - more art than science.

– Or use cmd-K to edit the line directly. Otherwise I ask it to **explain line by line** how it works, and ask it questions, reason with it. I learn from the process. Knowledge and skill goes up. This is an important step, because people are right that AI can make you lazy, waste away your coding muscles, but I think it's 100% _how_ you use it. I try not to use AI in a way that makes me lazy or atrophy, by asking questions, reasoning with it, learning something each time. Mental disuse would be simply copypasting without thinking/learning. It's a daily practice to stay disciplined about it. Kind of like eating your veges or going to the gym. Simple but ain't easy.

– Following these steps, I'm able to solves bugs 99% of time. The 1% is when there's some special configuration or a key part of the context is hidden or not part of codebase. That's when I tend to need help from the senior devs, or from code reviews or tests to pick up on. The usual way. The **processes are there to mitigate any potential drawbacks of AI** generated code.

Cursor + Claude Sonnet are like code superpowers.

* * *

_First published on [Lifelog](https://golifelog.com/posts/how-to-use-ai-for-coding-the-right-way-1724885853487)._
