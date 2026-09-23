---
name: add-scholion-note
description: Cria uma nova nota no Scholion (E:/scholion/content/notes/) com schema completo (sources estruturadas, has_commentary). Recebe título, corpo e fonte(s). Pergunta o que faltar.
argument-hint: "[título] | [corpo] | [fonte]"
---

Cria uma nova nota no **Scholion** em `E:/scholion/content/notes/<slug>.md`.

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

Todas as demais checagens (search-first no vault, checklist ghost-writer em contexto, `/style-test` lexical) **somam** a este portão — nunca substituem. Este é o único passo cujo resultado pode ser reportado como "auditoria feita".

---

## Parâmetros

Os argumentos podem vir em `$ARGUMENTS` no formato livre. Extraia:
- **título** — string curta (~60 chars). Se não fornecido, pergunte.
- **corpo** — conteúdo principal em markdown. Se não fornecido, pergunte.
- **fonte(s)** — URL(s) ou referência(s) bibliográfica(s). Se não fornecido, pergunte. Pode ser múltiplas — separar por linha ou ` · `.

Se algum dos três estiver ausente, pergunte antes de continuar.

## Processo

1. **Search-first interativo** — **ANTES de compor qualquer texto**, buscar no vault (`Grep`/`Glob` em `E:/scholion/content/notes/` e `E:/scholion/content/research/`) por temas, autores e termos relacionados ao corpo. Mostrar os matches com contexto breve (1 linha por nota: título + slug + 1 frase do conteúdo) e **esperar o autor apontar** quais linkar, expandir, ou ignorar antes de redigir. Se nada relevante for encontrado, dizer explicitamente ("nenhuma nota relacionada encontrada") antes de seguir.

2. **Carregar ghost-writer** — **ANTES de compor qualquer texto**, ler a skill `ghost-writer` (SKILL.md) para ter a checklist carregada no contexto. A checklist não é revisão posterior — é filtro ativo durante a escrita. Se este passo não aconteceu, o preview NÃO está pronto para ser mostrado.

3. **Hora real do sistema** — rodar `date +"%Y-%m-%dT%H:%M:%S%:z"` para obter o `date` atual. Nunca inventar horários.

4. **Slug** a partir do título: lowercase, remover acentos, substituir espaços e pontuação por `-`, máx ~50 chars.

5. **Tags** inferidas a partir do conteúdo (2–4 tags, kebab-case). Idioma das tags acompanha o idioma da nota — PT para PT, EN para EN.

6. **Summary** — uma frase curta (~150–200 chars) que sintetiza o ponto da nota. Será usada nos cards do mosaico.

7. **has_commentary** — `true` se a nota tem texto/análise/conexão original do usuário; `false` se é só um excerto/citação/glosa de fonte externa. Na dúvida, `false`.

8. **sources** — array estruturado, **não** texto livre. Cada item:
   ```yaml
   - title: "Título da fonte"
     author: "Autor"        # opcional
     year: 2024             # opcional
     publisher: "Editora"   # opcional
     url: "https://..."     # opcional
     kind: book | article | wiki | podcast | video | paper | poem | repo | film | other
   ```
   Se a fonte vier como URL nua, inferir `kind` pelo domínio (wikipedia.org → wiki, vox.thluiz.com → podcast, youtube → video, arxiv/.pdf → paper, etc.).

9. **Criar o arquivo** em `E:/scholion/content/notes/<slug>.md` com este formato:

   ```markdown
   ---
   title: "<título>"
   date: <YYYY-MM-DDTHH:MM:SS±HH:MM>
   summary: "<frase curta>"
   tags: ["tag1", "tag2"]
   has_commentary: <true|false>
   sources:
     - title: "..."
       url: "..."
       kind: "..."
   ---

   <corpo em markdown>
   ```

   **Importante:** sem `Fonte:` no final do corpo — as fontes ficam **só** no frontmatter. Renderização é responsabilidade do template `single.html`.

10. **Auditoria de voz** — executar as duas auditorias sobre o corpo composto e mostrar os findings no preview:
    - **Lexical** — `/style-test <slug>` (regex, grátis, ~1s): PT-EU, vocabulário banido, travessões, frontmatter, datas.
    - **Estrutural/semântica** — chamada HTTP ao `ghost-audit` conforme o **PORTÃO OBRIGATÓRIO** no topo desta skill. Não há atalho: rodar o comando, ver o JSON, reportar o verdict. Sem chamada, sem "passou".

11. **Preview** ao usuário (nota + findings da auditoria) e aguardar confirmação antes de escrever (se for rodada interativa; se vier completo nos argumentos, escrever direto).

12. Após o autor aprovar e o arquivo estar escrito:
    1. `git add content/notes/<slug>.md`
    2. Gravar o marcador do commit-gate (a nota já foi auditada no passo 10 — evita re-auditoria no portão):
       ```powershell
       $o = git -C E:\scholion rev-parse ":content/notes/<slug>.md"
       New-Item -ItemType Directory -Force E:\scholion\.ghost-audit | Out-Null
       Set-Content "E:\scholion\.ghost-audit\$o.ok" $o
       ```
    3. `git commit -m "note: <título>"` + `git push` (se houver remoto configurado).

## Regras

- **Voz e estilo**: quando gerar texto para o corpo da nota, seguir **todas** as regras da skill `ghost-writer` — vocabulário banido, estrutura banida, tom banido, checklist pós-geração. Notas são mais curtas que posts, mas o filtro anti-IA se aplica igual.
- **`date` é OBRIGATÓRIO** com formato ISO 8601 + offset real do sistema (`YYYY-MM-DDTHH:MM:SS±HH:MM` — o comando `date` do passo 3 já devolve o offset correto; nunca copiar offset de exemplo).
- Título idealmente ≤ 72 chars (não há schema enforcer no Hugo, mas mantém os cards consistentes).
- Sem campo `lang`.
- Sem `Co-Authored-By Claude` no commit (conteúdo é do usuário).
- Não tocar em `E:/silva/src/content/note/` — silvae está congelado para notas.
- **Source-or-silence**: toda afirmação factual no corpo da nota precisa de citação de fonte inline. Se não houver fonte atestada, dizer isso explicitamente e omitir — nunca parafrasear de forma plausível para preencher.
- Build sanity check: rodar `cd /e/scholion && hugo --quiet` antes do commit final, abortar se exit ≠ 0.
