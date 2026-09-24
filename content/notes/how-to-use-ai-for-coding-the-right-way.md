---
title: "How to use AI for coding the right way"
date: '2026-09-25T00:14:18+01:00'
category: webclip
summary: 'O autor defende usar IA como apoio de programação com contexto, prompts, revisão e testes, enquanto mantém atenção para evitar erros, alucinações e uso preguiçoso.'
tags: ["ia-para-programacao", "cursor", "code-review"]
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

## Fichamento

- O autor compara IA de programação a um estagiário muito competente, ou a devs terceirizados, que ainda precisam de direção humana para acertar o contexto e a aplicação.
- Ele diz que usa Claude 3.5 Sonnet no Cursor para pensar as etapas gerais e a arquitetura antes de escrever código.
- Também usa system prompts e documentação enviada ao Cursor para dar um enquadramento melhor às respostas.
- O texto sugere usar a própria IA como revisora, pedindo que ela aponte erros, verifique boas práticas e confira convenções do codebase.
- O autor conta que às vezes abre outra janela com outro modelo, como Llama 3.1 ou GPT-4o, para conferir bugs e ter uma segunda opinião.
- Ele destaca que fornecer o arquivo certo, mensagens de erro e links para componentes específicos ajuda mais do que marcar todo o codebase o tempo todo.
- Segundo o texto, contexto demais também pode confundir a IA e gerar sugestões estranhas.
- O autor diz que usa cmd-K para editar linhas diretamente e também pede explicações linha a linha para entender o código.
- Ele afirma que a disciplina está em não usar IA só para copiar e colar, mas para perguntar, raciocinar e aprender a cada uso.
- O texto diz que, com esse processo, ele consegue resolver bugs na maior parte do tempo, e que os casos restantes costumam exigir devs mais seniores, reviews ou testes.
