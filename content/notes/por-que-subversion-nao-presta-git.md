---
title: "Jogar Pedra em Gato Morto: por que Subversion não presta"
date: '2015-01-29T06:25:50-03:00'
category: webclip
summary: 'O texto defende que Subversion foi útil, mas já passou da hora de mudar para um VCS distribuído, sobretudo GIT, porque branches e merges continuam difíceis e tediosos.'
tags: ["git", "subversion", "version-control"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Jogar Pedra em Gato Morto: por que Subversion não presta | AkitaOnRails.com"
    url: "http://www.akitaonrails.com/2007/09/22/jogar-pedra-em-gato-morto-por-que-subversion-no-presta#.VMn7_MtqbqA"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-01/akitaonrails-com--por-que-subversion-nao-presta-git.md"
    kind: repo
---

O texto parte de uma defesa de GIT como alternativa a Subversion e aos demais VCS citados. A ideia central é que sistemas distribuídos como GIT, Mercurial, Bazaar e Darcs respondem melhor ao fluxo de trabalho com commits frequentes, branches e merges do que ferramentas centralizadas.

Subversion aparece como um avanço sobre CVS, com menos corrupção de repositório e branches mais fáceis, mas ainda com merges ruins e uma experiência que o autor considera insuficiente. O texto também menciona git-svn como caminho para usar GIT em ambientes que ainda exigem Subversion e cita limitações práticas no Windows e em ferramentas gráficas.

## Fichamento

- GIT é apresentado como um sistema distribuído de controle de código-fonte e como a recomendação principal para quem procura um VCS.
- Darcs, Mercurial e Bazaar também são tratados como bons projetos, e o texto os agrupa entre as opções distribuídas.
- CVS é descrito como ruim, com branches problemáticos, arquivos corrompidos e tags fracas.
- Subversion é reconhecido como melhor que CVS e mais estável, com branches mais simples e amplo ecossistema de ferramentas.
- Mesmo assim, o texto diz que Subversion ainda torna merges tediosos e que já passou da hora de trocar de ferramenta.
- O vídeo de Linus Torvalds é usado para reforçar a crítica a Subversion e a defesa de GIT.
- O fluxo de commits frequentes funciona bem sozinho, mas fica complicado quando há mais de um desenvolvedor e é preciso evitar interferência no trabalho alheio.
- git-svn é apresentado como solução para manter Subversion no centro e trabalhar com GIT localmente.
- O texto observa que migrar totalmente para GIT exigiria abrir mão de algumas ferramentas, embora Capistrano possa vir a suportar GIT com pouca adaptação.
- Há ressalvas práticas sobre Windows, Cygwin e a escassez de ferramentas gráficas para GIT.
