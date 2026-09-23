---
name: add-scholion-quote
description: Cria uma nota de citação no Scholion (E:/scholion/content/notes/). Recebe frase e possível autor, pesquisa autoria real, paráfrases e fontes, e cria a nota verificada. Baseada em add-scholion-note + ghost-writer.
argument-hint: "[frase] | [autor presumido]"
---

Cria uma nota de **citação verificada** no **Scholion** em `E:/scholion/content/notes/<slug>.md`.

> **Importante:** notas curtas (marginalia, glosas, fragmentos) **não vão mais para silvae**. Sempre criar em scholion. O silvae está congelado para notas — só recebe textos longos (`/text/`, `/post/`).

---

## PORTÃO OBRIGATÓRIO — nota NÃO ESTÁ PRONTA sem passar aqui

**Antes** de mostrar preview, **antes** de escrever no disco, **antes** de dizer "passou no ghost-writer", **antes** de qualquer commit, **antes** de mover para Silvae ou qualquer outro destino:

Rodar o `ghost-audit` no HTTP endpoint sobre o corpo composto (frontmatter + corpo) e mostrar o JSON de findings ao autor.

```powershell
$body = @{ content = '<frontmatter+corpo compostos>'; slug = '<slug>' } | ConvertTo-Json -Depth 5
$r = Invoke-RestMethod -Uri 'http://localhost:8080/api/vox-intelligence/presets/scholion/ghost-audit' -Method Post -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 120
$r.'x-parsed' | ConvertTo-Json -Depth 6
```

**Regras rígidas — sem exceção:**

- `verdict: red` → resolver **todos** os findings `block` (source-or-silence, PT-EU) antes do preview. Nunca declarar pronto com red.
- `verdict: yellow` → mostrar findings ao autor, ele decide caso a caso.
- `verdict: green` → seguir.
- **PROIBIDO substituir por checklist mental.** Rodar `grep` de vocabulário banido, ler o texto parágrafo a parágrafo, aplicar os 33 testes de cabeça e declarar "corpo limpo" **NÃO é rodar o ghost-audit**. Se a chamada HTTP não foi feita e o JSON não foi visto, a auditoria não aconteceu — diga isso ao autor em vez de fingir que passou. Esse é o erro recorrente que já quebrou a promessa da skill em pelo menos uma nota publicada.
- **Fail-open**: se o serviço estiver fora, dizer "auditoria estrutural não rodou — vox-intelligence offline" explicitamente. Nunca fingir verde nem simular findings.

Todas as demais checagens (search-first no vault, pesquisa de autoria, checklist ghost-writer em contexto, `/style-test` lexical) **somam** a este portão — nunca substituem. Este é o único passo cujo resultado pode ser reportado como "auditoria feita".

---

## Parâmetros

Os argumentos vêm em `$ARGUMENTS` em formato livre. Extraia:
- **frase** — a citação ou paráfrase que o usuário passou. Se não fornecida, pergunte.
- **autor presumido** — quem o usuário acredita ser o autor. Se não fornecido, pergunte.

Se algum dos dois estiver ausente, pergunte antes de continuar.

## Processo

### 1. Search-first interativo

**ANTES de compor qualquer texto**, buscar no vault (`Grep`/`Glob` em `E:/scholion/content/notes/` e `E:/scholion/content/research/`) pela frase, autor presumido, e temas adjacentes. Mostrar os matches com contexto breve (1 linha por nota: título + slug + 1 frase do conteúdo) e **esperar o autor apontar** quais linkar, expandir, ou ignorar antes de redigir o contexto de autoria. Se nada relevante for encontrado, dizer explicitamente ("nenhuma nota relacionada encontrada") antes de seguir.

### 2. Carregar ghost-writer

**ANTES de compor qualquer texto**, ler a skill `ghost-writer` (SKILL.md) para ter a checklist carregada no contexto. A checklist não é revisão posterior — é filtro ativo durante a escrita. Se este passo não aconteceu, o preview NÃO está pronto para ser mostrado.

### 3. Pesquisa de autoria

Usar `WebSearch` e `WebFetch` para investigar a citação. Consultar obrigatoriamente:

1. **Quote Investigator** (quoteinvestigator.com) — fonte primária para rastreio de citações
2. **Wikiquote** (en.wikiquote.org / pt.wikiquote.org) — verificar se consta e sob qual autor
3. **Busca geral** — a frase entre aspas + "quote" ou "citação"

Investigar e registrar:
- **Texto original exato** — a formulação mais antiga encontrada (pode diferir do que o usuário passou)
- **Autor real** — quem disse/escreveu primeiro, com obra e data se possível
- **Atribuições errôneas** — se a frase é frequentemente atribuída a outra pessoa, documentar
- **Paráfrases notáveis** — quem reformulou ou popularizou a frase
- **Contexto** — em que obra/discurso/carta apareceu originalmente

Se a autoria for **não verificável** (nenhuma fonte primária encontrada), dizer isso claramente — nunca inventar atribuição.

### 4. Hora real do sistema

Rodar `date +"%Y-%m-%dT%H:%M:%S%:z"` para obter o `date` atual. Nunca inventar horários.

### 5. Slug

A partir do conteúdo da citação ou do título escolhido: lowercase, remover acentos, substituir espaços e pontuação por `-`, máx ~50 chars.

### 6. Título

A frase completa da citação, sem o nome do autor. O autor vai nas tags e no corpo.
Se a frase for muito longa, o CSS do card trunca com `...` automaticamente (3 linhas).
Na página individual aparece inteira.
Exemplos:
- `It always seems impossible until it's done`
- `A ship in harbor is safe, but that is not what ships are built for`
- `Antes só do que mal acompanhado`

Sem limite rígido de caracteres — a frase inteira é o título.

### 7. Tags

2–4 tags em kebab-case. **Obrigatório**: incluir tag(s) com o(s) nome(s) do(s) autor(es) em kebab-case (ex: `nelson-mandela`, `epictetus`, `john-a-shedd`). Adicionar tags temáticas conforme o conteúdo (ex: `filosofia`, `estoicismo`, `liderança`). Idioma das tags acompanha o idioma predominante da nota.

### 8. Summary

Uma frase curta (~150–200 chars) que contextualize a citação: quem disse, onde, e se há controvérsia de atribuição. Será usada nos cards do mosaico.

### 9. has_commentary

- `false` se a nota é apenas a citação + contexto factual de autoria
- `true` se o usuário adicionar análise/conexão/comentário original próprio

### 10. type

Sempre `quote`.

### 11. Sources

Array estruturado no frontmatter. Cada fonte da pesquisa:
```yaml
- title: "Título da fonte"
  author: "Autor"        # opcional
  year: 2024             # opcional
  publisher: "Editora"   # opcional
  url: "https://..."     # opcional
  kind: book | article | wiki | podcast | video | paper | poem | repo | film | other
```

Fontes típicas para citações:
- Quote Investigator → `kind: article`
- Wikiquote → `kind: wiki`
- Obra original onde a frase aparece → `kind: book | paper | article` conforme o caso

### 12. Corpo da nota

**A citação NÃO vai no corpo** — ela já é o título, renderizado com estilo de citação (itálico, aspas decorativas) pelo CSS. O corpo contém apenas o contexto de autoria.

Formato:

```markdown
Contexto de autoria em prosa: quem disse, onde, quando. Se há atribuição errônea comum, explicar. Se há paráfrases notáveis, mencionar.
```

**Regras do corpo:**
- **Sem blockquote** — a citação é o título
- O contexto é factual e seco — sem floreio, sem "é uma frase fascinante"
- Seguir **todas** as regras da skill `ghost-writer` (vocabulário banido, estrutura banida, tom banido, checklist pós-geração)
- Sem `Fonte:` no final do corpo — fontes ficam **só** no frontmatter

### 13. Formato final do arquivo

```markdown
---
title: "<citação completa>"
date: <YYYY-MM-DDTHH:MM:SS±HH:MM>
category: quote
summary: "<frase curta>"
tags: ["autor-tag", "tema-tag"]
has_commentary: <true|false>
sources:
  - title: "..."
    url: "..."
    kind: "..."
---

Contexto de autoria.
```

### 14. Auditoria de voz

Executar as duas auditorias sobre o corpo composto e mostrar os findings no preview:

- **Lexical** — `/style-test <slug>` (regex, grátis, ~1s).
- **Estrutural/semântica** — chamada HTTP ao `ghost-audit` conforme o **PORTÃO OBRIGATÓRIO** no topo desta skill. Não há atalho: rodar o comando, ver o JSON, reportar o verdict. Sem chamada, sem "passou".

### 15. Preview e confirmação

Mostrar a nota completa ao usuário e aguardar confirmação antes de escrever.

### 16. Escrita e commit

Após confirmação:
1. Escrever em `E:/scholion/content/notes/<slug>.md`
2. Build sanity check: `cd /e/scholion && hugo --quiet` — abortar se exit ≠ 0
3. `git add content/notes/<slug>.md`
4. Gravar o marcador do commit-gate (a nota já foi auditada no passo 14 — evita re-auditoria no portão):
   ```powershell
   $o = git -C E:\scholion rev-parse ":content/notes/<slug>.md"
   New-Item -ItemType Directory -Force E:\scholion\.ghost-audit | Out-Null
   Set-Content "E:\scholion\.ghost-audit\$o.ok" $o
   ```
5. `git commit -m "note: <título>"`
6. `git push` (se houver remoto configurado)

## Regras

- **Voz e estilo**: o contexto de autoria segue as regras da skill `ghost-writer` — vocabulário banido, estrutura banida, tom banido, checklist pós-geração.
- **`date` é OBRIGATÓRIO** com formato ISO 8601 + offset.
- **`category: quote` é OBRIGATÓRIO** — é o que aciona o layout/ícone de citação nos cards.
- **Tags de autor são OBRIGATÓRIAS** — toda nota de citação deve ter pelo menos uma tag com o nome do autor.
- Sem campo `lang`.
- Sem `Co-Authored-By Claude` no commit.
- Não tocar em `E:/silva/src/content/note/`.
- **Nunca inventar atribuição** — se não encontrar fonte primária, marcar como "atribuída a" ou "não verificada".
- **Nunca fabricar fontes** — só incluir URLs e referências que foram efetivamente consultadas.
- Build sanity check: rodar `cd /e/scholion && hugo --quiet` antes do commit final, abortar se exit ≠ 0.
