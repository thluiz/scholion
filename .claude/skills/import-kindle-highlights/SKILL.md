---
name: import-kindle-highlights
description: "Importa ou sincroniza os destaques de um livro do Kindle (via kindle-scrapper) como notas category:quote no Scholion, agrupadas por livro com uma tag própria e uma página em /tags/<livro>/. Cruza com o vault para não duplicar, nunca chuta autoria, confere mecanicamente que cada nota é idêntica ao destaque e grava uma nota por commit. Use quando o autor pedir para importar, sincronizar ou procurar as quotes/destaques de um livro."
argument-hint: "{livro} (título, parte do título ou slug do arquivo em library/)"
---

Transforma os destaques de **um livro** (`E:\kindle-scrapper\library\<slug>.md`) em notas `category: quote` no Scholion, sem duplicar o que já existe e com o livro como agrupador.

Base: `add-scholion-quote` (formato e regras da nota) + `add-scholion-note/references/note-pipeline.md` (passos 1–3, 7–11, 13). Aqui só o que é específico da importação. Nasceu da importação de *O livro das citações* (Giannetti), 2026-11-02.

## Regras que valem sempre

- **Source-or-silence.** Autor e ano só entram se o **livro** (o destaque) os traz. Destaque sem autor, cortado no meio ou ambíguo **não vira nota**: perguntar ao autor, que confere no livro. Busca na web serve de **indício** (ex.: apontou Hampshire), nunca de fonte para gravar; só vale o que o autor confirmar.
- **Nunca resumir a listagem.** Ler o texto completo de cada destaque. Em antologias o autor fica no **fim** do destaque (`nietzsche (1886)`); listar truncado levou a concluir "11 sem autor" quando eram 2.
- **Voz.** A nota de citação não tem prosa autoral: título = a frase, corpo = contexto factual. Nota manual do Kindle (`📝`) é do autor: se existir, perguntar se vira `has_commentary: true` e como entra; nunca compor por ele.
- Sem `Co-Authored-By`. Um commit por nota, `--only` com caminho explícito. Push só no fim.
- Idioma PT-BR; tags sem acento; chaves do frontmatter em inglês.

## Processo

### 1. Sincronizar e localizar o livro

```powershell
Set-Location E:\kindle-scrapper; node bin/kindle.js sync     # se não for o caso de uma sync recente
node bin/kindle.js list                                       # achar o livro e o nº de destaques
```

- Sessão expirada (`Não achei a lista de livros`) → o login é interativo: pedir ao autor `! kindle login` (cwd `E:\kindle-scrapper`). Não tentar contornar.
- Resolver `{livro}` para um arquivo de `library/`. Ambíguo → listar e perguntar.
- Frontmatter do arquivo: `title`, `author`, `asin`, `highlights`, `updated`. Usar o título sem `(Portuguese Edition)`.

### 2. Cruzar com o vault

```powershell
$env:PYTHONIOENCODING='utf-8'
python -I E:\scholion\.claude\skills\import-kindle-highlights\scripts\crossmatch.py E:\kindle-scrapper\library\<slug>.md --json <scratchpad>\hl.json
```

(`python`, não `python3`: este não existe na máquina.) O script compara contra **todas** as notas, não só as com a tag do livro: no primeiro uso, 7 destaques já tinham nota pesquisada, sem tag.

- **Já tem nota** → não criar outra; só garantir a tag do livro (passo 7).
- **Pendentes** → mostrar numerados, texto completo, e **esperar o autor apontar** quais entram. "Todos" é resposta válida.
- Search-first em lote: não linkar temas; só as duplicatas acima importam.

### 3. Agrupador do livro (uma vez por livro)

Se `E:/scholion/content/tags/<slug-do-livro>/_index.md` ainda não existe, criar:

```markdown
---
title: "<título do livro>"
description: "<uma frase; ex.: Antologia organizada por X. As citações guardadas daqui aparecem abaixo.>"
book:
  author: "<autor do livro>"
  publisher: "<editora>"
  year: <ano>
---
```

O `layouts/_default/term.html` mostra título + `autor · editora · ano` quando há `book:`. Conferir editora/ano em fonte (ficha da edição); sem fonte, omitir o campo. Tag do livro = slug do título sem acento (`o-livro-das-citacoes`). Toda nota importada leva essa tag.

### 4. Gerar os drafts (em lote, no scratchpad)

Um arquivo por nota em `<scratchpad>\drafts\<slug>.md`, com `date: 'DATE'` como marcador (a hora real entra na gravação). Modelo:

```yaml
---
title: "<frase completa, sem o autor do fim; \ e " escapados>"
date: 'DATE'
category: quote
summary: 'Citação de <Autor>, datada de <ano> em <Livro>, de <Autor do livro> (<Editora>, <ano>).'
tags: ["<autor-da-frase>", "<autor-do-livro>", "<tag-do-livro>"]
has_commentary: false
sources:
  - title: "<título do livro>"
    author: "<autor do livro>"
    year: <ano>
    publisher: "<editora>"
    kind: book
---

Passagem de <Autor>, datada de <ano> em <Livro>, de <Autor do livro>.
```

- **Fonte idêntica em todas** as notas do livro (mesmo `title`, `author`, `year`, `publisher`): é o que mantém `/sources/` agrupado. Se o autor tiver o link do trecho (`url`), manter por nota.
- Ano: só quando o livro o traz junto à frase; senão "reunida por <Autor do livro> em <Livro>". Em livro de autor único (não antologia), a frase é do próprio autor: tags `<autor>` + `<tag-do-livro>`, corpo "Passagem de <Livro>, de <Autor>."
- Tag do autor da frase: reaproveitar a que já existe no vault (`Grep` em `tags:`); nomes completos quando inequívocos.
- Slug: primeiras palavras do título, ≤ 50 caracteres, conferir colisão. Se colidir, **parar**: é nota existente (voltar ao passo 2), não sufixar `-2`.
- Título com artefato de captura (letra solta no fim, destaque cortado) → não gerar; perguntar.
- Gerar com script Python (`python -I`), sem heredoc aninhado; para escapar `\` e `"` usar `chr(92)`/`chr(34)` se o shell mangar as barras.

### 5. Conferência mecânica (no lugar do ghost-audit)

O ghost-audit julga prosa autoral (voz, PT-EU, fecho aforístico, fonte). Aqui o título é a frase do livro e o corpo é um molde fixo, então o audit não acrescenta nada e não pode pedir mudança. O risco real é a nota divergir do livro. Conferir com:

```powershell
python -I E:\scholion\.claude\skills\import-kindle-highlights\scripts\verify.py E:\kindle-scrapper\library\<slug>.md <tag-do-livro> --drafts <scratchpad>\drafts
```

- **ERRO** (sai com código 1, não gravar): ano da nota diferente do destaque; fonte diferente das demais notas do livro.
- **Título**: tem de ser idêntico ao destaque sem a atribuição. Draft sem destaque idêntico sai como AVISO e **bloqueia a gravação** (corrigir o gerador, nunca editar a frase à mão).
- **AVISO "ano não consta no destaque"**: legítimo só quando o autor confirmou o ano (ex.: Paley 1785, Hampshire 1960); senão, remover.
- Rodar o mesmo comando sem `--drafts` depois de gravar (confere as notas do vault com a tag do livro). Avisos de notas antigas (título editado à mão, ano não registrado) são informativos.

**Exceção ao pipeline (decisão do autor, 2026-11-02):** em nota importada literalmente de livro, o marcador `.ghost-audit/<oid>.ok` (passo 7) é gravado após esta conferência passar sem ERRO, sem rodar o ghost-audit. Vale só para este fluxo e só enquanto o corpo for o molde acima. Se o autor acrescentar comentário próprio (`has_commentary: true`), esse texto passa pelo ghost-audit normal.

### 6. Preview e aprovação

Mostrar: o modelo completo (um draft inteiro), a tabela numerada `nº · autor · ano · slug`, o resultado da conferência mecânica, e o que ficou de fora e por quê. **Só gravar após aprovação explícita.**

### 7. Gravar

Script `.ps1` único, em loop, **uma nota por vez**:

1. `Get-Date -Format 'yyyy-MM-ddTHH:mm:sszzz'` novo para cada nota (nunca reaproveitar).
2. Escrever em `content/notes/<slug>.md` (UTF-8 sem BOM, LF), `git add`.
3. Marcador do gate (`.ghost-audit/<oid>.ok`, blob staged) só se a conferência mecânica do passo 5 passou sem ERRO.
4. `git commit --only -F <arquivo-de-mensagem> -- <caminho>` com mensagem `note: <título>`. Mensagem por arquivo (`-F`), não inline: títulos têm aspas.
5. Notas **já existentes** sem a tag do livro: acrescentar a tag via regex em `^tags: \[(.*)\]` (preservar EOL), um commit cada (`note: tag do livro ... em <slug>`).

Depois: `git push` uma vez, relatar "pushed `<hash>`" (nunca "publicado"). Conferir contagem: `grep -l '"<tag-do-livro>"' content/notes/*.md | wc -l`. Se faltar conferir a renderização, `hugo --quiet -d <scratchpad>\public` (~1,5 min) e olhar `public/tags/<tag>/index.html`.

### 8. Sincronização posterior (livro já importado)

Mesmo fluxo; o passo 2 já separa o que é novo. Se não há pendente, dizer isso e parar. Destaques novos de um livro com a tag/`_index.md` existentes só precisam dos passos 4–7.

## Armadilhas já vividas

- `python3` inexistente: um script de merge não rodou, e deleções de duplicatas foram commitadas antes das edições; verificar o `git diff` **antes** de commitar.
- Edição de arquivo com regex pode misturar CRLF/LF e produzir diff do arquivo inteiro; conferir `git diff --stat` e normalizar.
- Duplicatas aparecem quando o mesmo trecho é mandado duas vezes: a nota que fica ganha as tags da outra e um `aliases: ["/notes/<slug-removido>/"]`.
- O hook de push gera `data/git_history/*.json` não rastreados; não são seus, não commitar.
