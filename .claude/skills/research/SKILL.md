---
name: research
description: Inicia ou retoma uma pesquisa viva no Scholion. Pesquisas são documentos públicos que acumulam fontes verificadas, citações e conexões ao longo de várias sessões. Notas do Scholion são extraídas quando maduras.
argument-hint: "[tema ou pergunta]"
---

# Pesquisa Viva

Pesquisas vivas são documentos em `E:/scholion/content/research/<slug>.md` que evoluem ao longo de sessões. Servem para pesquisas que precisam de várias idas e vindas antes de virar notas.

## Iniciar ou retomar

O argumento em `$ARGUMENTS` é o tema ou pergunta. Ao receber:

1. **Verificar se já existe** pesquisa sobre o tema em `E:/scholion/content/research/`. Se existir, ler o arquivo e retomar de onde parou.
2. **Se não existir**, criar com o frontmatter abaixo.

## Frontmatter

```yaml
---
title: "Pesquisa Viva: [Tema]"
date: <timestamp>
summary: "[pergunta central]"
tags: ["pesquisa-viva", ...]
status: "em andamento"  # em andamento | pausada | concluída
---
```

## Corpo — formato livre

O corpo é markdown livre. Não tem estrutura rígida. O conteúdo evolui conforme a pesquisa avança. Alguns elementos que podem aparecer:

- **Texto em andamento** — rascunho do autor. Ele vai compondo o texto conforme a pesquisa avança. A IA salva o material bruto como o autor mandou, sem editar. Pode ter subtítulos internos (###). Trechos marcados com "(em aberto)" indicam passagens que o autor ainda não resolveu. A IA não tenta resolver essas passagens por conta própria
- **Perguntas em aberto** — só o autor adiciona. Nunca inventar perguntas, direções ou conexões que o autor não pediu
- **Fontes verificadas** — com status: ✓ verificada, ? pendente, ✗ descartada. Incluir citação exata, obra, ano, e o que foi verificado. **Links de referência ficam inline na própria fonte**, numa linha "Links:" no final de cada bloco. Nunca criar seção separada de links/referências — duplica informação e fica redundante
- **Não verificados** — fontes mencionadas mas que ainda precisam de confirmação contra primárias
- **Notas extraídas** — índice de notas do Scholion geradas a partir desta pesquisa, com links

O formato é o que for útil para que o autor leia e entenda, e para que a IA retome sem perder contexto. Não forçar estrutura. Deixar o documento crescer organicamente.

## Regras

- **Voz e estilo**: seguir regras da skill `ghost-writer` ao gerar texto. Pesquisa não é artigo acadêmico.
- **NUNCA inventar fontes, citações ou atribuições.** Se não verificou, marcar como ? pendente.
- **Verificar antes de publicar.** Cada citação precisa ser confirmada contra fonte primária antes de receber ✓.
- **Notas são extraídas, não geradas.** Quando uma parte da pesquisa amadurece, o autor decide se vira nota. Usar `/add-scholion-note` para criar. Adicionar link de volta na pesquisa.
- Sem `Co-Authored-By Claude` no commit.
- Build check: `hugo --quiet` antes de comitar.
- Commit message: `research: [ação] em [tema]` (ex: `research: verificar fontes em Posição x Oposição`)

## Marcações inline `{{...}}`

O autor pode deixar marcações no texto com duplas chaves para a IA resolver. Ao retomar ou revisar, buscar todas as ocorrências de `{{...}}` e processar cada uma:

1. Tentar resolver (buscar nota, ideograma, link, fonte, verificar facto)
2. Se encontrar, substituir a marcação pelo conteúdo resolvido
3. Se não encontrar, perguntar ao autor com opções próximas

Convenções:

- `{{ideograma de 尋橋}}` — buscar ideograma ou nota de etimologia
- `{{link para Moy Kat Jo}}` — buscar link interno no Scholion
- `{{fonte para X}}` — buscar referência/URL
- `{{verificar: afirmação Y}}` — fact-check contra fontes

## Retomando em nova sessão

Ao retomar, ler o arquivo inteiro. O documento contém tudo que é necessário para continuar sem depender de memória ou contexto de sessões anteriores. Perguntar ao autor o que quer aprofundar.
