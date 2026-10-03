# Pipeline comum das notas Scholion

Passos compartilhados pelas skills `add-scholion-note`, `add-scholion-quote`, `add-scholion-movie`, `add-scholion-note-from-podcast-annotation`, `add-scholion-webclip` e `move-scholion-to-silvae`. Cada SKILL.md diz quais passos usa e onde difere; o que não estiver lá, vale como está aqui.

Raiz do vault: `E:/scholion/content/notes/`. Scratchpad: o diretório `<scratchpad>` informado no ambiente da sessão.

## 1. Hora real

Um único comando, rodado de novo para **cada** nota (nunca "incrementar 1 minuto", nunca copiar offset de exemplo):

```powershell
pwsh -NoProfile -Command "Get-Date -Format 'yyyy-MM-ddTHH:mm:sszzz'"
```

O output vai inteiro no campo `date` (`YYYY-MM-DDTHH:MM:SS±HH:MM`).

## 2. Slug

A partir do título: lowercase, sem acentos, espaços e pontuação viram `-`, máx ~50 chars. Conferir colisão antes de seguir:

```powershell
Test-Path E:/scholion/content/notes/<slug>.md; Test-Path E:/scholion/content/notes/<slug>/index.md
```

Nota simples: `content/notes/<slug>.md`. Bundle (nota com arquivo anexo, ex. poster): `content/notes/<slug>/index.md` + anexos na mesma pasta.

## 3. YAML do frontmatter

O build Hugo usa YAML estrito. Antes de gravar, varrer `title`, `summary` e qualquer campo de texto livre:

- Contém `:` → envolver em aspas simples: `summary: 'frase com : aqui dentro'`.
- Está entre `"..."` → toda `"` interna escapada como `\"` (o parser não detecta aspas mistas; se a abertura é `"`, todas as internas precisam de escape).

Sem isso o build quebra com `failed to unmarshal YAML: ... did not find expected key`.

Chaves do frontmatter sempre em inglês; valores no idioma da nota. Sem campo `lang`.

## 4. Schema de `sources` e `category`

`sources` é array estruturado, nunca texto livre; sem `Fonte:` no corpo (o template `single.html` renderiza as fontes).

```yaml
sources:
  - title: "Título da fonte"
    author: "Autor"        # opcional
    year: 2024             # opcional
    publisher: "Editora"   # opcional
    url: "https://..."     # opcional
    kind: <um dos valores abaixo>
```

`kind` (um só por fonte): `book`, `article`, `wiki`, `podcast`, `video`, `paper`, `poem`, `repo`, `film`, `web`, `news`, `site`, `interview`, `image`, `internal`, `other`. URL nua → inferir pelo domínio (wikipedia.org → `wiki`, vox.thluiz.com → `podcast`, youtube → `video`, arxiv/.pdf → `paper`, github → `repo`; sem pista → `web`).

`category`: nota genérica **não leva** o campo. `category: note` é no-op (nenhum layout o reconhece; não usar). Valores reconhecidos pelos layouts: `webclip`, `quote`, `etymology`, `podcast`, `disciple`, `tablature`, `comic`, `movie`, `walk`, `place`. Sem `category` + `has_commentary: true` rende o ícone de comentário.

## 5. Links internos

Sempre `[texto](/notes/<slug>)` (ou `/research/<slug>`). Nunca `../x.md`, nunca slug nu em backticks: os dois quebram a navegação no site.

## 6. Search-first

Vale **antes de redigir** nas skills de composição (note, quote, movie): buscar em `E:/scholion/content/notes/` e `E:/scholion/content/research/` por temas, autores, ideogramas e termos do assunto; listar os matches (1 linha por nota: título + slug + 1 frase); **esperar o autor apontar** quais linkar, expandir ou ignorar. Se nada relevante: dizer "nenhuma nota relacionada encontrada" antes de seguir. Nunca draftar primeiro e linkar depois.

Nas skills de extração automática (podcast, webclip) o texto não passa pela voz do autor: pular search-first e ghost-writer; só sugerir cross-links (`Grep` por 2–3 termos centrais) e perguntar quais entram.

## 7. Portão ghost-audit

Gravar o draft completo (frontmatter + corpo) em `<scratchpad>/<slug>.md` e invocar:

```
/ghost-audit <scratchpad>/<slug>.md
```

A skill lê do disco, tem try/catch e imprime o verdict + findings. Nenhum snippet HTTP inline aqui ou nas skills.

Tratamento do verdict:

- `red` → mostrar os `block` ao autor. Aplicar só as correções com mérito próprio (a edição é melhor por si). O resto o autor decide: corrigir, ou liberar no commit via marcador `.ghost-audit/<oid>.ok` (passo 10), registrado como override consciente. **Nunca** entrar em loop de reescrita até verde.
- `yellow` → mostrar, o autor decide caso a caso. Em nota `webclip`, yellow não exige decisão: listar no preview e seguir.
- `green` → seguir.
- `GHOST-AUDIT-OFFLINE` → dizer ao autor que a auditoria não rodou. Nunca fingir verde; nunca substituir por checklist mental.

Checklist ghost-writer em contexto e `/style-test` **somam** a este portão, não substituem.

## 8. Preview

Obrigatório, sem exceção (mesmo quando os argumentos vieram completos): mostrar frontmatter + corpo inteiros e os findings do passo 7, e aguardar aprovação explícita. Nenhum `Write` em `content/notes/` antes disso.

## 9. Write e style-test

Após a aprovação: `Write` em `content/notes/<slug>.md` (ou `<slug>/index.md`). Depois:

```
/style-test
```

Sem argumento (default = última nota modificada). Aplicar só fixes triviais (PT-EU, vocabulário banido, frontmatter). Mudança de conteúdo volta ao preview.

## 10. Marcador do commit-gate

`git add` o caminho (o marcador usa o blob staged) e gravar o marcador **só se** o verdict visto no passo 7 foi `green`, ou `yellow` aceito pelo autor, ou `red` liberado por override consciente. Se o audit não rodou (offline), **não** gravar: o hook de commit audita (fail-open, não trava o git).

```powershell
$o = git -C E:\scholion rev-parse ":content/notes/<slug>.md"
New-Item -ItemType Directory -Force E:\scholion\.ghost-audit | Out-Null
Set-Content -LiteralPath "E:\scholion\.ghost-audit\$o.ok" -Value $o
```

Bundle: `rev-parse ":content/notes/<slug>/index.md"`.

## 11. Commit

Um commit por nota. Sempre com `--only` e caminho explícito (o repo tem stagers concorrentes: outras sessões, tarefa agendada de histórico); nunca `git add` + `git commit` nu.

```bash
git -C E:/scholion commit --only -m "note: <título>" -- content/notes/<slug>.md
```

Bundle: `-- content/notes/<slug>/`. Sem `Co-Authored-By` (regra da máquina; o conteúdo é do autor). Rodar o commit pela tool Bash: o hook `ghost-audit-gate` só intercepta essa tool.

## 12. Build

`cd /e/scholion && hugo --quiet` uma vez antes da primeira nota da sessão, não por nota; abortar se exit ≠ 0. Webclip não builda (o scheduler `\Claude\ScholionPublish` publica).

## 13. Push e relato

```bash
git -C E:/scholion push && git -C E:/scholion rev-parse --short HEAD
```

Relatar "pushed `<hash>`". Nunca "publicado"/"no ar" antes do deploy terminar; não monitorar o pipeline (só se o autor pedir).

## 14. Silvae

Silvae está congelado para notas: nunca tocar em `E:/silva/src/content/note/`. Só textos longos (`/post/`) vão para lá, via `move-scholion-to-silvae` ou `publish-research`.
