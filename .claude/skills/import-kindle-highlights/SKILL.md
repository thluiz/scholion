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
- Título com artefato de captura (letra solta no fim, nota de rodapé grudada como "Tully1", número de seção no início) → não gerar; perguntar. Destaque apenas cortado entra se o autor mandar (`--accept`), com a tag `destaque-cortado`.
**Script:** `scripts/generate.py` faz tudo acima (modelo, escapes, slug, colisão). Entradas, todas no scratchpad:

- `book.json`: `{"title","short_title","author","publisher","year","tag","anthology","lang","pronoun","sections"}`. `short_title` = nome do livro nos textos; `anthology: false` para livro de autor único; `lang` = idioma das notas (`pt` padrão, `en`); `pronoun` = `ele` (padrão) ou `ela`, usado em "em que ele cita outro autor".
- `sections` (autor único com texto de outra pessoa: apêndice, prefácio): `[{"from_loc": 1072, "to_loc": null, "author": "David Hume", "tag": "david-hume"}]`. O destaque no intervalo vira "Citação de David Hume reunida por Simon Critchley em Notes on Suicide", tags `[autor-da-seção, tag-do-livro]`, mesma fonte do livro.
- `confirm.json` (opcional), **só** com o que o autor confirmou:
  - antologia: `{"<loc>": {"author","tag","year"}}` para destaque sem atribuição;
  - autor único: `{"<loc>": {"cites": true}}` (cita outro autor, não identificado), `{"<loc>": {"cites": "Montaigne", "tag": "michel-de-montaigne", "ref": "*Ensaios* I.20", "url": "https://…"}}` (identificado: corpo "em que ele cita Montaigne, *Ensaios* I.20 ([fonte](…))" + tag do citado) ou `{"<loc>": {"cites": false}}` (desfaz falso positivo das heurísticas).
- **Heurísticas** (autor único, fora de seção; o `confirm.json` prevalece), sempre ligadas:
  - **A**: destaque que abre com aspas (`«` `“` `‘` `"`) → "em que ele cita outro autor".
  - **B**: destaque que menciona o sobrenome do autor do livro → texto de outro autor sobre a obra (prefácio, apresentação): corpo "Trecho de <Livro>, de <Autor>, escrito por outro autor sobre a obra", sem a tag do autor do livro.
  - As duas acrescentam a tag de autor não confirmado **no idioma da nota**: `autor-nao-confirmado` (pt) ou `author-to-be-confirmed` (en). Marcar à toa é melhor do que atribuir errado. A não pega citação sem aspas (Blackstone, Blanchot, poema zen em *Filósofos mortos*): na listagem do passo 2, apontar ao autor o que parecer fala de terceiro.
- **Salvar primeiro, atribuir depois** (decisão do autor, 2026-11-02): na dúvida sobre a autoria, gravar com a tag de autor não confirmado em vez de deixar de fora; a atribuição se confirma depois (pesquisa na web serve de indício, o autor confirma) e a nota troca a tag pelo autor citado.
- Destaque curto/cortado importado (`--accept` ou rotina com `--auto`) leva a tag `destaque-cortado` (uma só, em qualquer idioma), para o autor achar todos depois.
- `--skip <locs>`: o que o autor mandou deixar de fora.
- `--accept <locs>`: destaques curtos ou cortados que o autor, depois de ver a listagem, mandou importar assim mesmo (o título continua idêntico ao destaque, com o corte).

```powershell
python -I E:\scholion\.claude\skills\import-kindle-highlights\scripts\generate.py --lib E:\kindle-scrapper\library\<slug>.md --hl <scratchpad>\hl.json --out <scratchpad>\drafts --book <scratchpad>\book.json [--confirm <scratchpad>\confirm.json] [--skip 76,100] [--accept 293,712]
```

Dois destaques podem ter a **mesma loc** (Notes on Suicide: 4 pares). O gerador trata cada um pelo par loc + texto, então os dois viram draft; `--skip`/`--accept` valem para a loc inteira.

Código de saída 2 = há `PENDENTE`: destaque sem autor, cortado (sem `--accept`), nome fora de `scripts/authors.json` ou slug que já existe. Nada disso vira draft; perguntar ao autor. Nome novo e inequívoco entra em `authors.json` (nome completo + tag; reaproveitar a tag que já existe no vault) com a confirmação do autor. Testado: reproduziu byte a byte os 33 drafts da importação de Giannetti.

Se o shell mangar barras ao escrever script, usar a tool Write (não heredoc) ou `chr(92)`/`chr(34)`.

### 5. Conferência mecânica (no lugar do ghost-audit)

O ghost-audit julga prosa autoral (voz, PT-EU, fecho aforístico, fonte). Aqui o título é a frase do livro e o corpo é um molde fixo, então o audit não acrescenta nada e não pode pedir mudança. O risco real é a nota divergir do livro. Conferir com:

```powershell
python -I E:\scholion\.claude\skills\import-kindle-highlights\scripts\verify.py E:\kindle-scrapper\library\<slug>.md <tag-do-livro> --drafts <scratchpad>\drafts [--plain]
```

**`--plain` em livro de autor único (`anthology: false`)**: lá o título é o destaque inteiro. Sem `--plain`, o `verify.py` tenta separar uma atribuição do fim (lógica de antologia) e compara com o texto errado.

- **ERRO** (sai com código 1, não gravar): ano da nota diferente do destaque; fonte diferente das demais notas do livro.
- **Título**: tem de ser idêntico ao destaque sem a atribuição. Draft sem destaque idêntico sai como AVISO e **bloqueia a gravação** (corrigir o gerador, nunca editar a frase à mão).
- **AVISO "ano não consta no destaque"**: legítimo só quando o autor confirmou o ano (ex.: Paley 1785, Hampshire 1960); senão, remover.
- Rodar o mesmo comando sem `--drafts` depois de gravar (confere as notas do vault com a tag do livro). Avisos de notas antigas (título editado à mão, ano não registrado) são informativos.

**Exceção ao pipeline (decisão do autor, 2026-11-02):** em nota importada literalmente de livro, o marcador `.ghost-audit/<oid>.ok` (passo 7) é gravado após esta conferência passar sem ERRO, sem rodar o ghost-audit. Vale só para este fluxo e só enquanto o corpo for o molde acima. Se o autor acrescentar comentário próprio (`has_commentary: true`), esse texto passa pelo ghost-audit normal.

### 6. Preview e aprovação

Mostrar: o modelo completo (um draft inteiro), a tabela numerada `nº · autor · ano · slug`, o resultado da conferência mecânica, e o que ficou de fora e por quê. **Só gravar após aprovação explícita.**

### 7. Gravar

```powershell
pwsh -NoProfile -File E:\scholion\.claude\skills\import-kindle-highlights\scripts\save.ps1 -Drafts <scratchpad>\drafts -Lib E:\kindle-scrapper\library\<slug>.md -Tag <tag-do-livro> -Scratch <scratchpad> -TagOnly slug1,slug2 [-Plain]
```

(timeout 600000 na tool call; `-Plain` em livro de autor único, pelo mesmo motivo do `--plain` do passo 5.) O `save.ps1` roda o `verify.py --drafts` primeiro e não grava nada se houver ERRO.

- **Outro git no repo** (rotina `auto-import`, `\Claude\ScholionPublish`, outra sessão): o script espera o `.git/index.lock` sumir (até 2 min) e repete o `add`/`commit` que falhar por lock.
- **Retomada**: se o lote parar no meio, rodar o mesmo comando de novo. Nota que já existe e é igual ao draft (fora a data) é deste lote: já commitada → `SKIP`; ficou só staged → é commitada (`RESUMED`). Nota existente **diferente** do draft continua sendo colisão e para tudo.

Em seguida, **uma nota por vez**:

1. `Get-Date -Format 'yyyy-MM-ddTHH:mm:sszzz'` novo para cada nota (nunca reaproveitar).
2. Escrever em `content/notes/<slug>.md` (UTF-8 sem BOM, LF), `git add`.
3. Marcador do gate (`.ghost-audit/<oid>.ok`, blob staged) só se a conferência mecânica do passo 5 passou sem ERRO.
4. `git commit --only -F <arquivo-de-mensagem> -- <caminho>` com mensagem `note: <título>`. Mensagem por arquivo (`-F`), não inline: títulos têm aspas.
5. Notas **já existentes** sem a tag do livro: acrescentar a tag via regex em `^tags: \[(.*)\]` (preservar EOL), um commit cada (`note: tag do livro ... em <slug>`).

Depois: `git push` uma vez, relatar "pushed `<hash>`" (nunca "publicado"). Conferir contagem: `grep -l '"<tag-do-livro>"' content/notes/*.md | wc -l`. Se faltar conferir a renderização, `hugo --quiet -d <scratchpad>\public` (~1,5 min) e olhar `public/tags/<tag>/index.html`.

### 8. Sincronização posterior (livro já importado)

Mesmo fluxo; o passo 2 já separa o que é novo. Se não há pendente, dizer isso e parar. Destaques novos de um livro com a tag/`_index.md` existentes só precisam dos passos 4–7.

## Rotina autônoma diária (04:00)

`scripts/auto-import.ps1`, pensada para a task `\Claude\KindleImport` (04:00, depois do `\Claude\KindleDaily` de 01:00 que baixa os destaques). Sem LLM: gerar → `verify.py` → `save.ps1` (um commit por nota) → push → aviso no GossipGate. Só avisa quando algo acontece.

- **Registro `books.json`** (nesta pasta): só entra livro que o autor liga explicitamente, porque as notas viram páginas públicas (há livros sensíveis na biblioteca). Campos: `library` (slug do arquivo), `mode` (`auto` importa; `notify` só avisa), `anthology`, `title`, `short_title`, `author` (o autor limpo, sem tradutores), `publisher`/`year` (opcionais, omitir se não conferidos), `tag`, `since` (só destaques adicionados nessa data ou depois; evita despejar o acervo antigo), `ignore_locs`.
- **Livro de autor único (`anthology: false`)**: título = destaque inteiro; autor = o do livro, salvo `sections` e as heurísticas A/B do passo 4, que marcam a nota com a tag de autor não confirmado (no idioma do `lang` do livro). Fragmento (menos de 25 caracteres, ou terminado em `,` `;` `…`) vira nota com a tag `destaque-cortado` (`--auto`). O aviso diz quantas notas saíram com autor a conferir e quantas cortadas.
- **Antologia**: fica em `mode: notify`; a rotina conta os destaques novos e avisa para rodar a skill. Autoria nunca é inventada (`--confirm` só existe no fluxo interativo).
- **Aviso de livros sem import ligado**: toda execução lista os livros **fora** de `books.json` com destaques adicionados nos últimos 7 dias (`-RecentDays`), no formato "• Título (nº de destaques)". Cada destaque é avisado uma só vez (estado em `%LOCALAPPDATA%\scholion-kindle-import\state.json`); a primeira execução avisa tudo o que estiver na janela.
- **Livro ligado é importado por inteiro** (decisão do autor, 2026-11-02): sem teto por execução (`-MaxPerBook 0`) e com `since` vazio entra o acervo antigo também. Teto opcional só via parâmetro `-MaxPerBook N`.
- **Salvaguardas**: `verify.py` com ERRO → nada é gravado; slugs que já existem viram pendência no aviso; autoria suspeita e fragmento cortado viram nota marcada (tags acima), não pendência. Tudo vira log em `%LOCALAPPDATA%\scholion-kindle-import\auto-import.log`.
- **Teste sem gravar:** `pwsh -NoProfile -File scripts\auto-import.ps1 -Registry <arquivo.json> -DryRun`.
- **Ligar um livro:** acrescentar a entrada em `books.json` com `mode: auto` e `since` = hoje (ou a data a partir da qual quer notas); o acervo anterior, se quiser, entra pela skill interativa.
- **Registrar a task** (uma vez, pelo autor): ver `scripts/register-task.ps1`.

## Armadilhas já vividas

- `python3` inexistente: um script de merge não rodou, e deleções de duplicatas foram commitadas antes das edições; verificar o `git diff` **antes** de commitar.
- Edição de arquivo com regex pode misturar CRLF/LF e produzir diff do arquivo inteiro; conferir `git diff --stat` e normalizar.
- Duplicatas aparecem quando o mesmo trecho é mandado duas vezes: a nota que fica ganha as tags da outra e um `aliases: ["/notes/<slug-removido>/"]`.
- O hook de push gera `data/git_history/*.json` e, às vezes, já os commita como `chore: update git history`, deixando o branch 1 commit à frente do remoto. Os JSON não rastreados não são seus: não commitar à mão. O commit `chore` do hook sobe no próximo push; não dar outro push só por causa dele.
