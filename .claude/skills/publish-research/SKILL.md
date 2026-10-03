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

Links internos do Scholion (`/notes/...`, `/research/...`, `/tags/...`) precisam virar URLs absolutas para o site do Scholion:
- `/notes/slug/` → `https://scholion.thluiz.com/notes/slug/`
- `/research/slug/` → `https://scholion.thluiz.com/research/slug/`
- `/tags/slug/` → `https://scholion.thluiz.com/tags/slug/`

Links externos (https://...) ficam como estão.

### 4. Extrair fontes

As pesquisas não têm seção de referências separada (regra da skill `research`): cada fonte verificada é um bloco marcado ✓ com uma linha `Links:` ao final. Montar as `sources` do post a partir de:

1. Linhas `Links:` dos blocos marcados ✓ em qualquer seção (título do bloco → `title`; cada URL da linha → uma `url`). Blocos sem `Links:` ficam de fora.
2. Entradas de `## Notas do Scholion já relacionadas` e `## Notas extraídas` → `title` da nota, `url: https://scholion.thluiz.com/notes/<slug>/`.
3. Se a pesquisa tiver uma seção `## Fontes*` (pesquisas antigas: `## Fontes ✓`, `## Fontes verificadas`, `## Fontes (data)`), incluir as entradas dela também.

Cada source no frontmatter do Silvae:

```yaml
  - title: "Título"
    url: "URL"
```

Fontes de imagens usadas no texto (fotos, capas, screenshots) devem incluir `kind: image` e, se conhecidos, `author`. A lista montada entra no preview (ver Regras) para o autor cortar o que o texto publicado não usa.

### 5. Criar post no Silvae

Criar pasta `E:/silva/src/content/post/<slug>/` e escrever `index.md`:

```yaml
---
title: "<título da pesquisa, sem 'Pesquisa Viva:'>"
description: "<summary da pesquisa>"
publishDate: "<YYYY-MM-DD de hoje>"
tags: [<tags da pesquisa, sem "pesquisa-viva", em kebab-case como no Scholion; o schema do Silvae só aplica lowercase>]
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

   Publicado em <YYYY-MM-DD> no Silvae: [<título>](https://silva.thluiz.com/posts/<slug>/)

   <resumo substancial do texto publicado — cobre os tópicos principais, não só o summary do frontmatter>
   ```
   O resumo deve permitir que alguém lendo apenas a pesquisa entenda o que foi publicado sem precisar abrir o link. Incluir os temas centrais, nomes, conceitos e a conclusão do texto.

   **Voz e forma do resumo:**
   - **Primeira pessoa.** O autor é o Thiago; nunca referir-se a ele como "o Thiago" ou "a fala do Thiago". Usar "na minha vez", "puxei", "complemento".
   - **Parágrafos curtos**, não um único bloco corrido. Quebrar por seção lógica do post (abertura, cada bloco temático, fechamento).
6. Manter as demais seções (Rascunhos, Notas extraídas, Fontes, Notas de contexto) intactas.

### 7. Build e commit

1. `hugo --quiet` em `E:/scholion` — abortar se falhar.
2. No Scholion: `git -C E:/scholion add content/research/<slug>.md` + commit `"research: publicar [tema]"` + push.
3. No Silvae: `git -C E:/silva add src/content/post/<slug>/` + commit `"feat: [título]"` + push.

### 8. Reportar como "pushed", não "publicado"

Após o push do Silvae, o deploy para S3+CloudFront ainda está rodando. Relatar "pushed" / "enviado" e seguir; não ficar monitorando o pipeline. Só dizer "publicado" / "no ar" / "live" se o autor pedir confirmação e `gh run list --repo thluiz/silva --limit 2` mostrar o workflow "Deploy to S3 + CloudFront" como `completed success`.

Se a pesquisa tiver dossiê de voz ou página de treino (`fontes-privadas/voz/<slug>/README.md`), avisar o autor que eles passam a refletir o texto congelado em `## Texto Publicado`; `/dossie-voz` e `/treinar-apresentacao` não são atualizados por esta skill.

## Regras

- Sem `Co-Authored-By Claude` nos commits.
- **Voz e estilo**: o texto já passou pelo ghost-writer durante a pesquisa. Não re-editar na publicação.
- Confirmar com o usuário antes de executar, mostrando preview do frontmatter do Silvae e do que ficará no Scholion.
- Se a pesquisa tiver `status: "publicada"`, avisar que já foi publicada e perguntar se quer republicar.
