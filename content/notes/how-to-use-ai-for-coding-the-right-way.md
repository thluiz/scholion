---
title: "How to use AI for coding the right way"
date: '2026-09-25T00:14:18+01:00'
category: webclip
summary: 'The author argues for using AI as programming support with context, prompts, review, and tests, while staying attentive to avoid errors, hallucinations, and lazy use.'
tags: ["ai-for-programming", "cursor", "code-review"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to use AI for coding the right way"
    url: "https://dev.to/jasonleowsg/how-to-use-ai-for-coding-the-right-way-4cdn?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--how-to-use-ai-for-coding-the-right-way.md"
    kind: repo
---

The author argues that AI for coding works best when treated like a very knowledgeable intern or outsourced dev that still needs direction. He says the key is to keep checking the output, use the right context, and learn from the process instead of just pasting code.

He describes a workflow built around Claude 3.5 Sonnet in Cursor, system prompts, uploaded documentation, error messages, file linking, and occasional second opinions from another LLM. He also recommends using AI to review its own code, asking it to explain code line by line, and relying on reviews, tests, or senior devs when the context is incomplete.

## Reading notes

- The author compares coding AI to a very competent intern, or to outsourced devs, who still need human direction to get the context and application right.
- He says he uses Claude 3.5 Sonnet in Cursor to think through the general steps and the architecture before writing code.
- He also uses system prompts and documentation sent to Cursor to give better framing to the responses.
- The text suggests using the AI itself as a reviewer, asking it to point out errors, check best practices, and verify codebase conventions.
- The author says that he sometimes opens another window with another model, such as Llama 3.1 or GPT-4o, to check bugs and get a second opinion.
- He emphasizes that providing the right file, error messages, and links to specific components helps more than tagging the entire codebase all the time.
- According to the text, too much context can also confuse the AI and generate strange suggestions.
- The author says he uses cmd-K to edit lines directly and also asks for line-by-line explanations to understand the code.
- He states that the discipline lies in not using AI just to copy and paste, but to ask questions, reason, and learn with each use.
- The text says that, with this process, he manages to solve bugs most of the time, and that the remaining cases usually require more senior devs, reviews, or tests.
