---
title: "Migrando para o GitLab! Sim, vale a pena!"
date: '2026-11-16T03:27:59+00:00'
category: webclip
summary: 'O texto defende a migração para GitLab por custo, autonomia e CI integrado, comparando planos do GitHub e serviços externos com uma instalação própria do GitLab e GitLab Runner.'
tags: ["gitlab", "github", "continuous-integration", "cost-saving"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Migrando para o GitLab! Sim, vale a pena!"
    url: "https://akitaonrails.com/2016/08/03/moving-to-gitlab-yes-it-s-worth-it"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/akitaonrails-com--migrando-para-o-gitlab-sim-vale-a-pena.md"
    kind: repo
---

O texto sustenta que o GitLab se tornou a alternativa mais promissora ao GitHub, sobretudo depois das mudanças de preço do GitHub. A comparação central é econômica: GitLab com runner próprio pode sair muito mais barato do que GitHub somado a Travis ou outros serviços de CI, além de oferecer usuários e repositórios ilimitados.

Também descreve a migração como viável na prática. O GitLab CE permite importar repositórios do GitHub com metadados, há um caminho claro para instalar a versão comunitária e configurar o GitLab Runner com autoscaling, cache e registry locais. O autor relata que a migração dos próprios projetos levou alguns dias e funcionou sem grandes problemas.

## Fichamento

- O autor diz que começou a defender Git em 2007, quando ainda era difícil convencer as pessoas a adotá-lo.
- O GitHub virou o padrão de fato a partir de 2008, mas isso criou dependência de uma única plataforma para código e outros tipos de conteúdo.
- A motivação para buscar uma opção local veio cedo, primeiro com tentativas no Gitorious e depois com o GitLab.
- O GitLab aparece como a alternativa mais promissora ao GitHub porque oferece edição comunitária, hospedagem própria e versão enterprise.
- O autor considera o Bitbucket menos competitivo por causa de uma estratégia mais lenta e de uma suíte enterprise mais ampla para vender.
- A mudança de preço do GitHub torna a comparação financeira mais relevante, especialmente para equipes grandes.
- No exemplo de 100 desenvolvedores, GitHub mais Travis fica muito mais caro do que GitLab com GitLab Runner em infraestrutura própria.
- O GitLab Runner é apresentado como substituto funcional para Travis, Semaphore e CircleCI, com integração contínua dentro da interface do projeto.
- O autor recomenda instalar o GitLab CE primeiro em uma máquina simples, de preferência pela imagem de instalação automática da Digital Ocean.
- A instalação permite customizações como restrição por e-mail corporativo e login com OAuth2 por provedores externos.
- A importação de projetos grandes do GitHub pode levar horas porque as APIs públicas são lentas e têm limites de uso.
- O importador do GitLab traz não só o repositório, mas também labels, comentários e histórico de pull requests.
- Para projetos grandes do GitHub, o autor recomenda esperar uma versão mais madura do GitLab antes de migrar.
- Para o Bitbucket, o importador traz menos recursos e preserva principalmente o código-fonte.
- A configuração do GitLab em máquinas da Digital Ocean pede swap, ajustes de locale e atualizações automáticas de segurança.
- O GitLab Runner funciona como um servidor conectado ao GitLab que recebe comandos a cada push ou merge request.
- Sem muitos runners concorrentes, os desenvolvedores esperam mais pelo feedback e isso prejudica a produtividade e a disciplina de testes.
- O autoscaling do Runner permite criar máquinas sob demanda com docker-machine e APIs do provedor de nuvem.
- O exemplo usa três máquinas pequenas para registry, cache e runner, todas com rede privada na mesma região.
- O cache local com Minio e o registry proxy deixam os primeiros builds mais lentos e os seguintes mais rápidos.
- Cada projeto só precisa de um arquivo `.gitlab-ci.yml` para ativar o pipeline.
- O GitLab-CI também pode exigir que um merge request passe nos testes antes de ser aceito.
- Na conclusão, o autor diz que o GitLab é funcional, familiar para quem vem do GitHub ou Bitbucket e já permite abandonar parte da dependência de outras plataformas.
