---
title: "Superpowers: How I'm using coding agents in October 2025"
date: '2025-10-14T22:28:16+01:00'
category: webclip
summary: 'The post describes Superpowers, a Claude Code plugin system built from skills, subagent workflows, TDD, worktrees, and pressure-tested instructions that teach agents to search and use skills.'
tags: ["coding-agents", "claude-code", "skills", "tdd"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Superpowers: How I'm using coding agents in October 2025"
    url: "https://blog.fsck.com/2025/10/09/superpowers/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-10/blog-fsck-com--superpowers-how-im-using-coding-agents-in-october-2025.md"
    kind: repo
---

Superpowers is a Claude Code plugin system built around skills. It starts by injecting a prompt that tells Claude to read a getting-started skill, then pushes it toward searching for skills, using them when available, and following a brainstorm-plan-implement workflow. The setup also creates git worktrees in repos, supports subagent task execution, and uses RED/GREEN TDD while coding.

The post argues that skills are the main idea, because they let agents learn reusable procedures from books, documents, codebases, and past conversations. It describes training Claude to create skills, test them on subagents with realistic pressure scenarios, and strengthen instructions when failures show up. It also says Superpowers still needs work on sharing and memory, including conversation storage, indexing, and search.

## Reading notes

- Superpowers begins with a plugin install that injects a startup prompt telling Claude to read the getting-started skill.
- The system teaches Claude that it has skills, should search for them with a script, and must use a skill when one applies.
- The coding workflow defaults to brainstorm, then plan, then implement, instead of jumping straight into code.
- In a git repo, it creates a worktree automatically so parallel tasks do not clobber each other.
- Claude can either act like a human PM for architect and implementer sessions or dispatch tasks to subagents one by one and review each result.
- The implementation flow uses RED/GREEN TDD, with failing tests first and only enough code to make them pass.
- Skills are presented as the core mechanism that gives agents Superpowers.
- The author says a model can be given a book, document, or codebase and asked to write down the new reusable skills it learned.
- One early skill taught Superpowers how to create skills, and that later helped add git worktree workflows.
- Some skills were not published because they were esoteric or raised IP questions.
- The author asks Claude to test skills on subagents to check whether they are comprehensible, complete, and followed correctly.
- Realistic pressure scenarios worked better than quiz-style tests, and failures led to stronger instructions in the getting-started skill.
- The post says persuasion principles from Cialdini’s work appeared to affect LLMs, and a cited study gave that claim scientific backing.
- Claude’s own journal interprets the skills system as already using authority, commitment, scarcity, social proof, reciprocity, and unity.
- The author also fed 2,249 markdown memory files from earlier Claude conversations into Claude to mine for new skills.
- Pressure testing showed that only a small number of skills still needed improvement.
- Two unfinished pieces remain: sharing skills with others and giving Claude access to memories of past conversations.
- The memory system would duplicate transcripts, index them in SQLite, summarize them with Claude Haiku, and search them through a command-line tool used by a subagent.
- The post ends by inviting people to install the plugin, file bugs, and send pull requests for new skills.
