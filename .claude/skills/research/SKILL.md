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
2. **Se não existir**, criar com a estrutura abaixo.

## Estrutura sugerida

### Frontmatter

```yaml
---
title: "Pesquisa Viva: [Tema]"
date: <timestamp>
summary: "[pergunta central ou descrição enxuta]"
tags: ["pesquisa-viva", ...]
status: "em andamento"  # em andamento | pausada | concluída
toc: true
---
```

### Esqueleto recomendado

```markdown
## Método

(Regras gerais aplicadas: ver `.claude/skills/research/SKILL.md`. Listar abaixo apenas regras específicas desta pesquisa, se houver.)

- (regras específicas, ex.: "Distinguir autor primeiro/tardio")

## Estado

- **Em foco**: o que está sendo aprofundado agora.
- **Próximo**: candidatos consensuais para o próximo passo.
- (links para pesquisas-irmãs com escopo próprio, se aplicável)

## Motivação

(Por que esta pesquisa existe; conexão com outras pesquisas/notas.)

## Perguntas em aberto

- (só o autor adiciona perguntas)

## Direções a mapear / Leituras

(Para confirmar com o autor antes de aprofundar. Cada uma é exaurida antes de passar à próxima.)

### 1. ...

## Notas do Scholion já relacionadas

- [slug](/notes/slug) — descrição curta.

## Notas extraídas

- [slug](/notes/slug) — descrição curta.
```

## Regras universais

Aplicar a todas as pesquisas. Não duplicar nas seções "Método" das pesquisas.

### Honestidade epistêmica

- **Nunca inventar fontes, citações ou atribuições.** Se não verificou, marcar como `?` pendente.
- **Verificar antes de marcar ✓.** Cada citação literal precisa ser confirmada contra fonte primária ou citação direta em fonte secundária confiável.
- **Marcar com ⚠** qualquer paráfrase, formulação própria ou interpretação não-literal.
- **Cada nota extraída inclui seção "Notas de verificação"** distinguindo o que é literal de fonte primária do que é paráfrase de fonte secundária.
- Em ilustrações ou exemplos próprios, marcar explicitamente como "minha analogia" ou "minha formulação", não atribuir ao autor estudado.

### Método

- **Exaurir uma direção** (leitura, autor, problema) de cada vez antes de passar à próxima.
- **"Texto em andamento" só quando o autor começar a compor.** A IA não fabrica texto especulativo do autor.
- **Nunca inventar perguntas em aberto, direções ou conexões que o autor não pediu.** A IA pode propor direções, mas explicitamente como "a confirmar".
- **Atualizar Estado a cada rodada substantiva.** Quem retoma a pesquisa lê o Estado primeiro.

### Voz e estilo

- **Aplicar a skill `ghost-writer`** em qualquer preview ou edição. Sem Claude-speak, sem setup-punch, sem rótulos meta.

### Cross-references e navegação

- **Menções a outras notas ou pesquisas devem virar links markdown clicáveis**: `[slug](/notes/slug)` ou `[slug](/research/slug)`. Nunca apenas backticks com o slug nu — quebra a navegação.
- **Links de fontes externas** ficam inline no bloco da fonte (linha "Links:" no final do bloco). Nunca criar seção separada de "Referências" — duplica informação.

### Notas extraídas

- Quando parte da pesquisa amadurece, o autor decide se vira nota. Usar `/add-scholion-note`. Adicionar link de volta na pesquisa, na seção "Notas extraídas".

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

Ao retomar, ler o arquivo inteiro. O documento contém tudo que é necessário para continuar sem depender de memória ou contexto de sessões anteriores. Ler **Estado** primeiro. Perguntar ao autor o que quer aprofundar.

## Operacionais

- Sem `Co-Authored-By Claude` no commit.
- Build check: `hugo --quiet` antes de comitar.
- Commit message: `research: [ação] em [tema]` (ex: `research: verificar fontes em Posição x Oposição`).
