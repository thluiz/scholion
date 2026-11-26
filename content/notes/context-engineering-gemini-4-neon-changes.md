---
title: "How my context engineering changed for Gemini 4 Neon"
date: '2026-11-26T16:27:52+00:00'
category: webclip
summary: 'Author explains how they simplified rules, tools, skills, visual checks, and session flow to let Gemini 4 Neon use its large context more effectively during daily coding.'
tags: ["llm-agents", "context-engineering", "gemini-4-neon", "developer-workflows"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "How my context engineering changed for Gemini 4 Neon"
    url: "https://www.philschmid.de/gemini-4-neon-context-engineering"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/philschmid-de--context-engineering-gemini-4-neon-changes.md"
    kind: repo
---

The author describes how daily use of Gemini 4 Neon as a coding agent led them to simplify context design. Older setups accumulated strict rules, long ban lists, duplicated tool instructions, and bloated project docs that conflicted with current requests and burned thinking tokens. With Gemini 4 Neon, they now keep user-level rules minimal, encode tool behavior once in schemas or CLI interfaces, load skills only when needed, lean on images and video for visual tasks, and favor explicit handoff files over mid-session compaction.

They report that removing rigid constraints and duplicated rules made the model more accurate and faster on edge cases it can already handle. Skills and tools are structured so the agent reads only relevant files and definitions. Large contexts are managed by splitting work into phases with written handoffs and by forking sessions when tasks branch, instead of compressing active threads and losing detail.

## Reading notes

- In real agent use, a single prompt is only a slice of context; system instructions, files, tools, skills, and history fill most of the window.
- Persistent instructions outlive individual requests, so very specific rules eventually collide with what the user later asks for.
- After weeks of evals with Gemini 4 Neon, older guardrails and rules slowed it down or caused failures on edge cases it could otherwise solve.
- Old system rules accumulated reactively, such as bans added when previous models wrote noisy comments or edited too broadly.
- Over time, user rules, project rules, and the current request began to contradict one another.
- A blanket ban on comments conflicts as soon as the user asks the agent to document a public function.
- When instructions conflict, Gemini 4 Neon spends extra thinking tokens resolving them and often follows older rules instead of the new request.
- The author removed rigid code-style bans and replaced them with judgment cues like matching existing style, naming, and comment density.
- This shift reduced wasted thinking and improved accuracy of the model's responses.
- Their user-level GEMINI.md now fits on one screen, keeping only habits that apply to every session.
- Persistent user rules focus on safety around approvals, verification of sources, and handling long-running jobs.
- They also keep short preferences for how the agent should format replies at the user level.
- Task-specific guidance is moved into skills instead of living in global instructions.
- Previous generations required tool behavior to be described both in system instructions and inside tool definitions.
- They also used few-shot examples to teach valid arguments and call patterns.
- Repeating tool rules across system prompts and descriptions created duplication and extra context overhead.
- Few-shot examples tended to work for common cases but constrained how the model handled rare or unusual inputs.
- When tasks diverged from examples, the model sometimes copied extra fields or wrong argument shapes from those examples.
- That copying behavior led to invalid tool calls on inputs that did not match the example pattern.
- The new approach is to encode usage rules once inside a rich tool interface, such as a JSON schema.
- For the update_plan tool, they define parameter types, required fields, enums, and property constraints in the schema.
- Strict schemas box the tool surface and guide the model without lengthy prose instructions.
- For everyday coding agents, the same principle is applied to repo helper scripts and CLI tools.
- Clear flags, constrained options, and direct error messages are used instead of long usage paragraphs.
- Tool surface area is kept small and outputs are bounded to prevent context from being filled with unnecessary data.
- They removed overlapping search tools and avoid streaming long command logs into the context.
- Instead of dumping large stdout blocks, logs are written to files to keep turns focused.
- They find that Gemini 4 Neon obeys a rule encoded once in the tool schema even over long sessions.
- Removing duplicated system-level tool rules reduces context clutter without sacrificing discipline in tool usage.
- The author deleted most project-level AGENTS.md and GEMINI.md files across repositories.
- Many of those files only restated directory layouts the model can already inspect from the repo itself.
- Some project docs had turned into append-only memory logs that drifted out of date.
- Now project instruction files are short, holding a brief repo summary and a few genuine gotchas.
- Gotchas include details the model cannot infer from code, such as a non-standard test command.
- They also include constraints like a single file where all shared types must be defined.
- Broader domain workflows are moved into skills with a one-line description in a central index.
- Examples of domain workflows shifted into skills are long-form editing, UI guidelines, API reviews, and CLI guides.
- Skills are kept lightweight and used to encode team conventions and required checks.
- The author advises against scripting every edge case inside skills to avoid bloat.
- For longer skills, they split material into a small tree of linked files.
- That structure lets the agent read only the skill segment relevant to the current task.
- Skills give the biggest benefit around quickly changing CLIs, SDKs, and internal APIs.
- Loading an up-to-date skill on demand limits guessing about flags or endpoints that might be deprecated.
- This reduces trial-and-error steps even when the skill itself costs tokens to load.
- Thanks to Gemini 4 Neon, skills and deferred tools are discovered and loaded reliably when needed.
- The model reads only files and tool definitions that match the task context and skips irrelevant ones.
- This behavior trims unused context in the first turn while still loading what matters.
- For ordinary backend code edits, a brief text request is usually adequate.
- When layout, diagrams, or motion are important, text alone leaves too much ambiguity.
- With Gemini 4 Neon, the author uses images and video more often as both references and checks.
- For styling or diagram tasks, they replace long textual CSS descriptions with screenshots or short recordings.
- Visual references show precise style, spacing, and motion that text might misrepresent.
- They also have the agent verify its work visually by rendering outputs and inspecting them.
- The agent is instructed to open actual PNGs, diagrams, or video clips it produces before marking tasks complete.
- Visual inspection helps catch issues like clipped text, wrapped labels, or broken alignment.
- These visual problems are easy to miss when relying only on text logs and descriptions.
- Even with a context window of about one million tokens, long sessions still degrade.
- As sessions grow, they get noisy, slow, and eventually require some form of compaction.
- Mid-task compaction is harmful because summarizing breaks the prompt cache.
- Summarization also discards line-level details that the model might still need later.
- After compaction, the model often has to reread files it had already opened before.
- To avoid that, the author now chooses to split work deliberately into phases instead of stretching one thread.
- When a task enters a new phase, they have the agent write a short handoff file.
- The handoff file records the goal, confirmed decisions, and precise file paths involved.
- They start a new session based on the handoff file rather than continuing the old thread.
- If a second task emerges mid-session, they fork the session instead of queuing tasks sequentially.
- One example workflow is running an eval suite and debugging failures in one thread first.
- After that, they write a handoff file and open a new session focused on preparing the write-up.
- In parallel, they fork the eval thread again to generate visualizations from the loaded results.
- For teams building their own agent loop, automatic compaction is kept as a fallback rather than a first resort.
- They recommend not triggering automatic compaction too early in the session.
- Roughly 500k tokens of context is their preferred threshold before compacting.
- Allowing the context to grow to that size avoids early cache resets and unnecessary file rereads.
- When compaction is needed, they pin active file paths and verified decisions inside summaries.
- This practice preserves key data the model needs to make progress after compaction.
- In their wrap-up, they propose simplifying each context layer when updating setups for Gemini 4 Neon.
- At the user level, GEMINI.md should stay short, focusing on global safety and response preferences, with style bans turned into judgment cues.
- For tools and scripts, each rule should live once in a typed JSON schema, with few-shot examples and repeated system rules removed.
- For everyday coding agents, they apply this by designing clear CLI flags and helper scripts rather than textual instructions.
- At the project level, they delete large AGENTS.md and GEMINI.md files and keep only non-obvious codebase details.
- Workflow instructions move into lightweight skills divided into linked files when they become long.
- For visual tasks, they recommend using screenshots or recordings as references and having the agent inspect rendered outputs.
- For session management, they avoid mid-task compaction by using written handoff files or forking threads when new tracks appear.
- They argue that many long prompts are remnants of working around weaker models.
- By eliminating conflicting instructions and duplicate tool rules, Gemini 4 Neon can devote its thinking tokens to the actual task being solved.
