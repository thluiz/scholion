---
name: research-status
description: Lista pesquisas vivas do Scholion com status atual (em foco, próximo passo, etapa do dossiê de voz). Use quando o autor pergunta "o que tenho em andamento?", "quais pesquisas abertas?", ou simplesmente invoca /research-status.
argument-hint: "[opcional: 'todas' para incluir pausadas/concluídas/publicadas]"
---

# Status das Pesquisas Vivas

Lista todas as pesquisas em `E:/scholion/content/research/` com seu estado atual. Skill apenas de leitura — não modifica arquivos.

## Processo

1. Listar todos os arquivos `.md` em `E:/scholion/content/research/`.
2. Para cada arquivo, ler o frontmatter e extrair:
   - `title`
   - `status` (em andamento | pausada | concluída | publicada)
   - `summary`
   - `slug` (nome do arquivo sem `.md`)
3. Da seção `## Estado` do corpo, extrair:
   - **Em foco**: linha após `**Em foco**:`
   - **Próximo**: linha após `**Próximo**:` (ou variantes como `**Próximo na leitura X**:`)
4. Dossiê de voz (skill `dossie-voz`): checar `E:/scholion/fontes-privadas/voz/<slug>/` (ver seção abaixo).
5. Filtrar conforme `$ARGUMENTS`:
   - Vazio (default): mostrar apenas pesquisas com `status: "em andamento"`.
   - `todas`: incluir todas, agrupadas por status.
6. Apresentar em lista organizada (ver formato abaixo).

## Formato de saída

```
**Em andamento (N)**

1. **<title>** — [/research/slug](/research/slug)
   - Em foco: <em foco>
   - Próximo: <próximo>
   - Dossiê: <etapa do dossiê de voz>
   - Treino: <página de treino, só se houver>

2. ...
```

Ao final da lista, uma linha de totais: `Dossiês de voz: N ativos, M sem dossiê. Páginas de treino: T.`

Se argumento for `todas`, adicionar seções **Pausadas**, **Concluídas** e **Publicadas** abaixo, com mesmo formato (mas ocultando "Em foco/Próximo" se a pesquisa estiver pausada/concluída e tiver `Status` próprio nessas categorias). Em **Publicadas**, no lugar de Em foco/Próximo mostrar a linha `Publicado em <data> no Silvae: <link>` que `/publish-research` grava na seção `## Texto Publicado`.

Se nenhuma pesquisa em andamento: dizer explicitamente *"Nenhuma pesquisa em andamento."*.

## Pesquisas anteriores à convenção "Estado"

Algumas pesquisas (criadas antes de "Estado" virar padrão) não têm a seção. Para essas, mostrar:

```
N. **<title>** — [/research/slug](/research/slug)
   - <summary do frontmatter>
   - *(sem seção Estado — pesquisa anterior à convenção)*
   - Dossiê: <etapa do dossiê de voz>
```

Não tentar inferir Em foco/Próximo dessas. Listar como informação disponível e seguir.

## Dossiê de voz

O dossiê é o Claude Doc privado de marcos consolidados que a skill `dossie-voz` mantém para conversas de voz. O registro local fica em `fontes-privadas/voz/<slug>/` (submódulo privado). Etapas, da menos para a mais avançada:

| Etapa | Como detectar | Linha a mostrar |
|---|---|---|
| Sem dossiê | pasta `voz/<slug>/` não existe | `Dossiê: —` |
| Só fluxo antigo | pasta existe, mas `README.md` não tem link `claude.ai/artifact/` | `Dossiê: só arquivos do fluxo antigo (anexados à mão)` |
| Ativo, sem conversa | `README.md` com link, `fechamentos/` vazio ou ausente | `Dossiê: ativo, v<N>, sincronizado em <data> · nenhuma conversa incorporada` |
| Ativo, com conversas | `README.md` com link e arquivos em `fechamentos/` | `Dossiê: ativo, v<N>, sincronizado em <data> · N conversas incorporadas (última: <AAAA-MM-DD> <tema>)` |

- `<data>`: a da linha `Última sincronização:` do README. Sem essa linha, usar a data do último commit do README no submódulo (`git -C fontes-privadas log -1 --format=%as -- voz/<slug>/README.md`).
- `v<N>`: da mesma linha do README. Sem `v`, mostrar `v?` (dossiê anterior à convenção de versão; recebe v1 na próxima atualização).
- **Divergência**: comparar o hash de commit da linha `Última sincronização:` com `git -C E:/scholion log -1 --format=%h -- content/research/<slug>.md`. Diferentes → acrescentar `· pesquisa avançou desde a sincronização (agora em <hash atual>)`. Sem hash no README, não afirmar nada.
- `<tema>`: nome do arquivo de fechamento mais recente, sem a data e sem `.md`.
- Se o submódulo tiver alteração não commitada em `voz/<slug>/` (`git -C fontes-privadas status --short voz/<slug>`), acrescentar `· alterações locais não commitadas`.
- Se `fontes-privadas/` estiver vazio (submódulo não inicializado), omitir a linha Dossiê de todas as pesquisas e avisar uma vez no fim.

Fechamentos ainda não incorporados vivem só na caixa de entrada do doc (comentários `FECHAMENTO:`), que esta skill não lê. Quando houver dossiê ativo, lembrar no fim: `/dossie-voz sincronizar <slug>` para puxar conversas novas.

A pasta `voz/skills/` não é pesquisa; ignorar.

## Página de treino

Se o README da pesquisa em `fontes-privadas/voz/<slug>/` tiver uma linha `Página de treino` com link (skill `treinar-apresentacao`), mostrar `Treino: página publicada em <data> (roteiro no commit <hash>)`, com a data e o hash dessa seção do README. Aplicar a mesma checagem de divergência: se o último commit da pesquisa for outro, acrescentar `· roteiro da pesquisa mudou depois (agora em <hash atual>)`. Sem a linha no README, omitir `Treino:`.

## Pesquisas sem `status:` no frontmatter

Tratar como `em andamento` por default (todas pesquisas pré-convenção implicitamente eram).

## Sem efeitos colaterais

Esta skill apenas lê arquivos. Não modifica, não commita, não pusha. Se o autor quiser **atualizar** o estado de uma pesquisa após listar, isso é tarefa separada (editar o arquivo manualmente ou pedir alteração específica).
