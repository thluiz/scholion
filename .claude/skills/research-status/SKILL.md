---
name: research-status
description: Lista pesquisas vivas do Scholion com status atual (em foco, próximo passo). Use quando o autor pergunta "o que tenho em andamento?", "quais pesquisas abertas?", ou simplesmente invoca /research-status.
argument-hint: "[opcional: 'todas' para incluir pausadas/concluídas]"
---

# Status das Pesquisas Vivas

Lista todas as pesquisas em `E:/scholion/content/research/` com seu estado atual. Skill apenas de leitura — não modifica arquivos.

## Processo

1. Listar todos os arquivos `.md` em `E:/scholion/content/research/`.
2. Para cada arquivo, ler o frontmatter e extrair:
   - `title`
   - `status` (em andamento | pausada | concluída)
   - `summary`
   - `slug` (nome do arquivo sem `.md`)
3. Da seção `## Estado` do corpo, extrair:
   - **Em foco**: linha após `**Em foco**:`
   - **Próximo**: linha após `**Próximo**:` (ou variantes como `**Próximo na leitura X**:`)
4. Filtrar conforme `$ARGUMENTS`:
   - Vazio (default): mostrar apenas pesquisas com `status: "em andamento"`.
   - `todas`: incluir todas, agrupadas por status.
5. Apresentar em lista organizada (ver formato abaixo).

## Formato de saída

```
**Em andamento (N)**

1. **<title>** — [/research/slug](/research/slug)
   - Em foco: <em foco>
   - Próximo: <próximo>

2. ...
```

Se argumento for `todas`, adicionar seções **Pausadas** e **Concluídas** abaixo, com mesmo formato (mas ocultando "Em foco/Próximo" se a pesquisa estiver pausada/concluída e tiver `Status` próprio nessas categorias).

Se nenhuma pesquisa em andamento: dizer explicitamente *"Nenhuma pesquisa em andamento."*.

## Pesquisas anteriores à convenção "Estado"

Algumas pesquisas (criadas antes de "Estado" virar padrão) não têm a seção. Para essas, mostrar:

```
N. **<title>** — [/research/slug](/research/slug)
   - <summary do frontmatter>
   - *(sem seção Estado — pesquisa anterior à convenção)*
```

Não tentar inferir Em foco/Próximo dessas. Listar como informação disponível e seguir.

## Pesquisas sem `status:` no frontmatter

Tratar como `em andamento` por default (todas pesquisas pré-convenção implicitamente eram).

## Sem efeitos colaterais

Esta skill apenas lê arquivos. Não modifica, não commita, não pusha. Se o autor quiser **atualizar** o estado de uma pesquisa após listar, isso é tarefa separada (editar o arquivo manualmente ou pedir alteração específica).
