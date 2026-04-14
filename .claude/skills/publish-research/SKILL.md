---
name: publish-research
description: Publica uma pesquisa viva do Scholion como post no Silvae. Extrai o "Texto em andamento", converte URLs internas, e marca a pesquisa como publicada.
argument-hint: "[slug da pesquisa]"
---

# Publicar Pesquisa Viva → Silvae

Extrai a seção "Texto em andamento" de uma pesquisa viva em `E:/scholion/content/research/<slug>.md` e publica como post em `E:/silva/src/content/post/<slug>/index.md`.

## Parâmetros

O argumento em `$ARGUMENTS` é o slug da pesquisa (ou parte do título). Se ambíguo, listar candidatos e perguntar.

## Processo

### 1. Ler a pesquisa

Ler o arquivo completo em `E:/scholion/content/research/<slug>.md`.

### 2. Extrair o texto

Extrair apenas o conteúdo da seção `## Texto em andamento` (do heading até o próximo `## ` de mesmo nível ou fim do arquivo). Não incluir rascunhos, fontes, notas extraídas, notas de contexto.

### 3. Converter URLs internas

Links internos do Scholion (`/notes/...`, `/tags/...`) precisam virar URLs absolutas para o site do Scholion:
- `/notes/slug/` → `https://scholion.thluiz.com/notes/slug/`
- `/tags/slug/` → `https://scholion.thluiz.com/tags/slug/`

Links externos (https://...) ficam como estão.

### 4. Extrair fontes

Extrair todas as entradas da seção `## Fontes ✓` da pesquisa. Cada entrada no formato `- Título — [Site](URL) ✓` vira uma source no frontmatter do Silvae:

```yaml
  - title: "Título"
    url: "URL"
```

Fontes de imagens usadas no texto (fotos, capas, screenshots) devem incluir `kind: image` e, se conhecidos, `author`.

### 5. Criar post no Silvae

Criar pasta `E:/silva/src/content/post/<slug>/` e escrever `index.md`:

```yaml
---
title: "<título da pesquisa, sem 'Pesquisa Viva:'>"
description: "<summary da pesquisa>"
publishDate: "<YYYY-MM-DD de hoje>"
tags: [<tags da pesquisa, sem "pesquisa-viva", formato silvae com espaços>]
lang: "pt"
sources:
  <fontes de imagens primeiro (kind: image), depois fontes textuais>
---
```

Corpo: o texto extraído no passo 2, com URLs convertidas no passo 3.

### 6. Atualizar a pesquisa no Scholion

No arquivo original da pesquisa:

1. **Título**: trocar `"Pesquisa Viva: [Tema]"` → `"Publicado: [Tema]"`
2. **Status**: trocar `status: "em andamento"` → `status: "publicada"`
3. **Adicionar atributo**: `research: published`
4. **Remover tag**: retirar `"pesquisa-viva"` do array de tags
5. **Seção "Texto em andamento"**: trocar o heading para `## Texto Publicado` e substituir todo o conteúdo por:
   ```markdown
   ## Texto Publicado

   Publicado em <YYYY-MM-DD> no Silvae: [<título>](https://silva.thluiz.com/p/<slug>/)

   <summary da pesquisa>
   ```
6. Manter as demais seções (Rascunhos, Notas extraídas, Fontes, Notas de contexto) intactas.

### 7. Build e commit

1. `cd /e/scholion && hugo --quiet` — abortar se falhar.
2. No Scholion: `git add content/research/<slug>.md` + commit `"research: publicar [tema]"` + push.
3. No Silvae: `cd /e/silva && git add src/content/post/<slug>/` + commit `"feat: [título]"` + push.

## Regras

- Sem `Co-Authored-By Claude` nos commits.
- **Voz e estilo**: o texto já passou pelo ghost-writer durante a pesquisa. Não re-editar na publicação.
- Confirmar com o usuário antes de executar, mostrando preview do frontmatter do Silvae e do que ficará no Scholion.
- Se a pesquisa tiver `status: "publicada"`, avisar que já foi publicada e perguntar se quer republicar.
