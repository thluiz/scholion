---
url: "https://addyosmani.com/blog/ai-coding-workflow/?utm_source=tldrnewsletter"
captured_at: "2026-01-05T18:49:55-03:00"
title: "AddyOsmani.com - My LLM coding workflow going into 2026"
domain: "addyosmani-com"
---

AI coding assistants became game-changers in 2025, but harnessing them effectively takes skill and structure. These tools dramatically increased what LLMs can do for real-world coding, and many developers (myself included) embraced them.

At Anthropic, for example, engineers adopted Claude Code so heavily that today ~90% of the code for Claude Code is written by Claude Code itself. Yet, using LLMs for programming is not a push-button magic experience - it's "difficult and unintuitive" and getting great results requires learning new patterns. Critical thinking remains key. Over a year of projects, I've converged on a workflow similar to what many experienced devs are discovering: treat the LLM as a powerful pair programmer that requires clear direction, context and oversight rather than autonomous judgment.

In this article, I'll share how I plan, code, and collaborate with AI going into 2026, distilling tips and best practices from my experience and the community's collective learning. It's a more disciplined "AI-assisted engineering" approach - leveraging AI aggressively while staying proudly accountable for the software produced.

## Start with a clear plan (specs before code)

Don't just throw wishes at the LLM - begin by defining the problem and planning a solution.

One common mistake is diving straight into code generation with a vague prompt. In my workflow, and in many others', the first step is brainstorming a detailed specification with the AI, then outlining a step-by-step plan, before writing any actual code. For a new project, I'll describe the idea and ask the LLM to iteratively ask me questions until we've fleshed out requirements and edge cases. By the end, we compile this into a comprehensive spec.md - containing requirements, architecture decisions, data models, and even a testing strategy.

Next, I feed the spec into a reasoning-capable model and prompt it to generate a project plan: break the implementation into logical, bite-sized tasks or milestones. This upfront investment might feel slow, but it pays off enormously. As Les Orchard put it, it's like doing a "waterfall in 15 minutes" - a rapid structured planning phase that makes the subsequent coding much smoother.

## Break work into small, iterative chunks

Scope management is everything - feed the LLM manageable tasks, not the whole codebase at once.

A crucial lesson I've learned is to avoid asking the AI for large, monolithic outputs. Instead, we break the project into iterative steps or tickets and tackle them one by one. LLMs do best when given focused prompts: implement one function, fix one bug, add one feature at a time.

This approach guards against the model going off the rails. If you ask for too much in one go, it's likely to get confused or produce a "jumbled mess" that's hard to untangle. Developers report that when they tried to have an LLM generate huge swaths of an app, they ended up with inconsistency and duplication - "like 10 devs worked on it without talking to each other," one said.

## Provide extensive context and guidance

LLMs are only as good as the context you provide - show them the relevant code, docs, and constraints.

Expert LLM users emphasize this "context packing" step: doing a "brain dump" of everything the model should know before coding, including high-level goals and invariants, examples of good solutions, and warnings about approaches to avoid.

There are now utilities to automate context packaging, like gitingest or repo2txt, which essentially "dump" the relevant parts of your codebase into a text file for the LLM to read.

I think Claude Skills have potential because they turn what used to be fragile repeated prompting into something durable and reusable by packaging instructions, scripts, and domain specific expertise into modular capabilities that tools can automatically apply when a request matches the Skill.

## Choose the right model (and use multiple when needed)

Not all coding LLMs are equal - pick your tool with intention, and don't be afraid to swap models mid-stream.

The key is: if one model gets stuck or gives mediocre outputs, try another. This "model musical chairs" can rescue you when you hit a model's blind spot.

Personally I gravitate towards Gemini for a lot of coding work these days because the interaction feels more natural and it often understands my requests on the first try. But I will not hesitate to switch to another model if needed.

## Leverage AI coding across the lifecycle

Supercharge your workflow with coding-specific AI help across the SDLC.

Claude Code, OpenAI's Codex CLI and Google's Gemini CLI are CLI tools where you can chat with them directly in your project directory. I've used Google's Jules and GitHub's Copilot Agent as well - these are asynchronous coding agents that actually clone your repo into a cloud VM and work on tasks in the background, then open a PR for you.

We're not at the stage of letting an AI agent code an entire feature unattended and expecting perfect results. Instead, I use these tools in a supervised way. There are also orchestration tools like Conductor that let you run multiple agents in parallel on different tasks.

## Keep a human in the loop - verify, test, and review everything

AI will happily produce plausible-looking code, but you are responsible for quality - always review and test thoroughly. As Simon Willison aptly says, think of an LLM pair programmer as "over-confident and prone to mistakes." I treat every AI-generated snippet as if it came from a junior developer: I read through the code, run it, and test it as needed.

I weave testing into the workflow itself. If I'm using a tool like Claude Code, I'll instruct it to run the test suite after implementing a task, and have it debug failures if any occur.

I also use Chrome DevTools MCP, built with my last team, for my debugging and quality loop to bridge the gap between static code analysis and live browser execution.

No matter how much AI I use, I remain the accountable engineer. In practical terms, that means I only merge or ship code after I've understood it.

## Commit often and use version control as a safety net. Never commit code you can't explain.

Frequent commits are your save points - they let you undo AI missteps and understand changes.

When working with an AI that can generate a lot of code quickly, it's easy for things to veer off course. I mitigate this by adopting ultra-granular version control habits. I commit early and often, even more than I would in normal hand-coding. One practitioner likened it to treating commits as "save points in a game."

Don't be afraid to use branches or worktrees to isolate AI experiments. One advanced workflow I've adopted (inspired by folks like Jesse Vincent) is to spin up a fresh git worktree for a new feature or sub-project.

## Customize the AI's behavior with rules and examples

Steer your AI assistant by providing style guides, examples, and even "rules files" - a little upfront tuning yields much better outputs.

I have a CLAUDE.md file that I update periodically, which contains process rules and preferences for Claude to follow (and similarly a GEMINI.md when using Gemini CLI). This includes things like "write code in our project's style, follow our lint rules, don't use certain functions, prefer functional style over OOP," etc.

The community has also come up with creative "rulesets" to tame LLM behavior, like adding a "no hallucination/no deception" clause to prompts: "If you are unsure about something or the codebase context is missing, ask for clarification rather than making up an answer."

## Embrace testing and automation as force multipliers

Use your CI/CD, linters, and code review bots - AI will work best in an environment that catches mistakes automatically.

I actually include linter output in the prompt sometimes. If the AI writes code that doesn't pass our linter, I'll copy the linter errors into the chat and say "please address these issues." The model then knows exactly what to do.

AI coding agents themselves are increasingly incorporating automation hooks. Some agents will refuse to say a code task is "done" until all tests pass.

## Continuously learn and adapt (AI amplifies your skills)

Treat every AI coding session as a learning opportunity - the more you know, the more the AI can help you, creating a virtuous cycle.

This pattern holds generally: if you come to the table with solid software engineering fundamentals, the AI will amplify your productivity multifold. If you lack that foundation, the AI might just amplify confusion. As Simon Willison notes, almost everything that makes someone a senior engineer (designing systems, managing complexity, knowing what to automate vs hand-code) is what now yields the best outcomes with AI.

## Conclusion

I've fully embraced AI in my development workflow - but in a considered, expert-driven way. My approach is essentially "AI-augmented software engineering" rather than AI-automated software engineering.

I've learned: the best results come when you apply classic software engineering discipline to your AI collaborations. It turns out all our hard-earned practices - design before coding, write tests, use version control, maintain standards - not only still apply, but are even more important when an AI is writing half your code.

The bottom line for me: AI coding assistants are incredible force multipliers, but the human engineer remains the director of the show.

I'm excited to share I've released a new AI-assisted engineering book with O'Reilly. There are a number of free tips on the book site in case interested.
