---
title: "How to Use DeepSeek R1 for Free in Visual Studio Code with Cline or Roo Code"
date: '2026-09-24T23:58:07+01:00'
category: webclip
summary: 'The page shows how to run DeepSeek R1 locally for free and connect it to Visual Studio Code with Cline or Roo Code using LM Studio, Ollama, or Jan.'
tags: ["deepseek-r1", "visual-studio-code", "cline", "roo-code"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Use DeepSeek R1 for Free in Visual Studio Code with Cline or Roo Code"
    url: "https://dev.to/dwtoledo/how-to-use-deepseek-r1-for-free-in-visual-studio-code-with-cline-or-roo-code-3an9?"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--how-to-use-deepseek-r1-for-free-in-vscode.md"
    kind: repo
---

The page argues that DeepSeek R1 is a free, open-source option that performs well in reasoning, mathematics, and code generation. It then explains how to run it locally with LM Studio, Ollama, or Jan and connect it to Visual Studio Code through Cline or Roo Code.

## Fichamento

- DeepSeek R1 is presented as a free, open-source model that competes with and outperforms models such as GPT-4, o1-mini, and Claude 3.5 in the author's test.
- The model can be used for chat at chat.deepseek.com, but running it locally avoids token or API costs.
- The author says local use keeps data on the PC and does not send it to external servers.
- The text recommends smaller or quantized models for less powerful PCs and mentions using LLM Calc to estimate minimum RAM.
- Model choice depends on hardware: 1.5B for simple tasks and modest PCs, 7B for intermediate setups, and 70B for complex tasks and high-end machines.
- LM Studio is one way to run the model locally: install the app, download DeepSeek R1 in the Discover tab, load it, and start the local server.
- For Apple processors, the text says to keep the MLX option selected in LM Studio; for Windows or Linux, choose GGUF.
- Ollama is another route: install it, run `ollama pull deepseek-r1`, and start the server with `ollama serve`.
- Jan is presented as a third option, with the model found through Hugging Face and then loaded in Jan, which starts the server automatically.
- To integrate with VSCode, the author instructs installing Cline or Roo Code and setting the API provider, base URL, and model ID.
- For Jan or LM Studio, the provider should be set to LM Studio; for Ollama, the provider should be set to Ollama.
