---
name: treinar-apresentacao
description: Publica e mantém uma página web privada (Artifact) para ensaiar uma apresentação oral cujo roteiro está no "Texto em andamento" de uma pesquisa viva do Scholion: relógio real por bloco, texto do roteiro como teleprompter, transcrição ditada pelo teclado, avaliação pelo Claude contra o roteiro e as fontes de cada ponto, histórico de tentativas. Depois, lê as tentativas e propõe ajustes no roteiro da pesquisa. Use quando o autor quiser treinar, ensaiar ou cronometrar uma apresentação, fala, aula ou gravação, ou quando pedir para revisar o roteiro a partir dos treinos.
argument-hint: "<slug da pesquisa> | atualizar <slug> | revisar <slug>"
---

# Treinar apresentação

Complementa a skill `dossie-voz`, que serve para *discutir* uma pesquisa em voz. Esta serve para *ensaiar* uma fala: o que a conversa de voz não consegue fazer (medir tempo de verdade, ouvir um bloco inteiro sem interromper, guardar cada tentativa) a página faz.

Onde cada coisa vive:

```
claude.ai (Artifact privado, com db)            "Ensaio <tema>" — a página de treino
fontes-privadas/voz/<slug>/treino/roteiro.json  dados que a página lê (blocos, pontos, fontes, perguntas)
fontes-privadas/voz/<slug>/treino/index.html    cópia do template, só para publicar
fontes-privadas/voz/<slug>/README.md            link da página + data da última sincronização
.claude/skills/treinar-apresentacao/page.html   template da página (um só para todas as pesquisas)
```

A fonte de verdade do roteiro continua sendo `content/research/<slug>.md`, seção "Texto em andamento". O `roteiro.json` é derivado dela; se divergir, refaz-se a partir da pesquisa. As tentativas (transcrições, tempos, avaliações) ficam só no banco do artifact; esta skill as lê com `ArtifactData`, não as copia para o repositório sem o autor pedir.

## Como a página funciona (para explicar ao autor)

- Escolhe um bloco ou a apresentação inteira. O texto do bloco aparece como teleprompter; dá para esconder e falar de memória.
- Relógio real, com alvo por bloco (proporcional ao peso do bloco dentro do alvo total da apresentação).
- Campo "O que você disse": o autor toca no campo e usa o microfone do teclado do celular para ditar enquanto fala. A página não acessa o microfone (o viewer de artifacts bloqueia); o ditado é do sistema.
- "Avaliar" manda roteiro, tabela de pontos com fontes, exceções declaradas, duração e transcrição ao Claude (capacidade `sample`, na conta do autor) e devolve: cobertura ponto a ponto (dito / parcial / faltou), desvios da fonte, acréscimos, comentário de tempo, um ajuste para a próxima tentativa.
- "Guardar tentativa" grava no banco do artifact (coleção `attempts`). O histórico aparece embaixo, com transcrição e avaliação.
- "Perguntas da plateia": sorteia uma pergunta provável para treinar resposta.
- "De onde vem cada ponto" e "Pendências": a mesma honestidade com as fontes do dossiê de voz, para o autor e para a avaliação.

## Modo 1 — Criar ou atualizar a página

Argumento: slug da pesquisa (ou `atualizar <slug>`).

1. **Ler a pesquisa inteira.** O roteiro é a seção "Texto em andamento". Se ela não existir ou não for um texto para falar, dizer isso e parar: a skill não compõe roteiro (isso é `research` + `ghost-writer`).
2. **Ler `fontes-privadas/voz/<slug>/README.md`.** Se já há link da página de treino, é atualização: mesmo `url`, só os dados mudam.
3. **Montar `roteiro.json`** (esquema abaixo). Blocos = subdivisões do roteiro (títulos `###`, ou parágrafos em negrito numerados, ou o que o autor indicar). Texto dos blocos **literal**, como está na pesquisa. Tabela de pontos: uma linha por afirmação factual do bloco, com a fonte como a pesquisa a dá (nota do Scholion, encontro, obra). O que a pesquisa marca ⚠ ou `?` entra com `"flag": true` e vai também para `pending`. Exceções declaradas pelo autor (leitura própria, sem fonte) vão em `exceptions`. Perguntas da plateia: se o dossiê de voz já as tem, reaproveitar; senão, propor até 10, marcadas como sugestão da IA em `questions_note`.
4. **Preview para o autor**: lista dos blocos (título + primeira linha), pesos e alvos de tempo, número de pontos por bloco, exceções, perguntas. Esperar aprovação antes de publicar.
5. **Publicar**:
   - `cp .claude/skills/treinar-apresentacao/page.html fontes-privadas/voz/<slug>/treino/index.html` e, na cópia, trocar a primeira linha `<title>Ensaio</title>` por `<title>Ensaio <tema curto></title>` (o `<title>` do arquivo é o nome do artifact; o parâmetro `title` da ferramenta não vence o tag).
   - Página nova: `Artifact` publish com `file_path` = esse `index.html`, `files: {"data/roteiro.json": "fontes-privadas/voz/<slug>/treino/roteiro.json"}`, `capabilities: {db: {}, user: {}, sample: {}}`, `icon: "microphone"`, `description` de uma frase.
   - Página existente: mesma chamada com `url` do README; omitir `capabilities` e `icon` (ficam como estão). Antes de publicar numa página de sessão anterior, `Artifact` `read` da `url` (a publicação exige leitura prévia).
   - Mudou o template `page.html`: republicar todas as páginas listadas em `fontes-privadas/voz/*/README.md` que tenham link de treino, uma por vez.
6. **Verificar**: `Artifact` `read` com `path: "data/roteiro.json"` devolve o arquivo; `ArtifactData` `list` da coleção `attempts` responde (vazia numa página nova). Só então dizer que publicou.
7. **Registrar** no README da pesquisa em `fontes-privadas/voz/<slug>/`, seção "Treino": link, data, commit da pesquisa de onde o roteiro saiu. Commit no submódulo + push, e ponteiro no Scholion (como na skill `dossie-voz`).
8. **Entregar**: o link e, na primeira vez, três linhas de uso: abrir no celular, tocar no campo de transcrição e usar o microfone do teclado, "Guardar tentativa" no fim.

### Esquema de `roteiro.json`

```json
{
  "slug": "<slug>",
  "page_title": "Ensaio <tema curto>",
  "title": "<título da apresentação>",
  "situation": "<para quem, onde, quanto tempo; uma ou duas frases>",
  "research": "https://scholion.thluiz.com/research/<slug>/",
  "synced": { "date": "AAAA-MM-DD", "commit": "<hash curto da pesquisa>" },
  "target_minutes": [5, 10],
  "sources_note": "<como ler a coluna fonte>",
  "questions_note": "<de onde vêm as perguntas; se são sugestão da IA, dizer>",
  "exceptions": ["<leitura própria do autor sem fonte, declarada no roteiro>"],
  "blocks": [
    {
      "id": "b1", "short": "1. <rótulo curto>", "title": "<título do bloco>", "weight": 2,
      "text": "<texto literal do bloco, parágrafos separados por linha em branco>",
      "points": [
        { "claim": "<afirmação>", "source": "<nota/encontro/obra>", "note": "<observação>", "flag": false }
      ]
    }
  ],
  "pending": ["<o que a pesquisa marca ⚠ ou ? e a avaliação não deve tratar como fato>"],
  "questions": ["<pergunta provável da plateia>"]
}
```

`weight` distribui o alvo de tempo entre os blocos (omitido = 1). `flag: true` = afirmação sem fonte; a página mostra ⚠ e a avaliação sabe que não é fato.

## Modo 2 — Revisar o roteiro a partir dos treinos

Argumento: `revisar <slug>`.

1. Ler o link no README. `ArtifactData` `list` da coleção `attempts` (com `out_dir` no scratchpad se forem muitas). Cada documento: `block`, `blockTitle`, `startedAt`, `durationSec`, `transcript`, `feedback` (pode ser `null`), `scriptSynced`.
2. **Resumir para o autor**, por bloco: quantas tentativas, duração mínima/máxima contra o alvo, pontos que ficaram `faltou` ou `parcial` em mais de uma tentativa, desvios recorrentes, acréscimos que apareceram mais de uma vez (candidatos a entrar no roteiro, se tiverem fonte), e tentativas feitas com roteiro antigo (`scriptSynced` anterior ao `synced.date` atual).
3. **Search-first** só se algum acréscimo pedir fonte nova: buscar no vault e listar; esperar o autor apontar.
4. **Preview da atualização da pesquisa**: o que muda no "Texto em andamento" (cortes, reordenações, frases que o autor passou a dizer melhor de improviso do que no texto, com as palavras dele), e a linha do Estado ("Revisão de AAAA-MM-DD após N treinos: …"). Source-or-silence: acréscimo sem fonte não entra no texto, a não ser como exceção declarada do autor.
5. **Gravar só depois da aprovação.** `hugo --quiet`, commit `research: ajustar roteiro após treinos em <tema>`.
6. **Atualizar a página** (Modo 1, passos 3 a 7) para que o roteiro na página seja o novo. Atualizar `synced`.
7. As tentativas antigas ficam no banco; se o autor quiser arquivar transcrições, gravar em `fontes-privadas/voz/<slug>/treino/tentativas/<AAAA-MM-DD>.md` e commitar no submódulo. Nunca apagar documentos do banco sem o autor pedir.

## Regras

- **Source-or-silence vale no `roteiro.json`.** A avaliação repete como fato o que está na coluna fonte. Afirmação sem fonte entra com `flag: true` ou não entra.
- **Texto literal.** Não reescrever o roteiro ao copiá-lo para o JSON. Mudança de texto é mudança na pesquisa primeiro.
- **Privado.** A página nunca é compartilhada: as transcrições são fala bruta do autor.
- **Sem `Co-Authored-By`** em commit nenhum.
- Se o autor quiser *discutir* o tema em vez de ensaiar, é `dossie-voz`.
