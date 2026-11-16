---
title: "Realize Deploy Automático de Projetos Estáticos com Azure Static Web Apps!"
date: '2020-07-05T14:10:46+00:00'
category: webclip
summary: 'O artigo explica como o Azure Static Web Apps faz deploy automático de sites estáticos a partir de um repositório GitHub via GitHub Actions, com hospedagem grátis, SSL, staging e suporte ao Azure Functions.'
tags: ["azure-static-web-apps", "github-actions", "jamstack", "sites-estaticos"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Realize Deploy Automático de Projetos Estáticos com Azure Static Web Apps!"
    url: "https://dev.to/azure/realize-deploy-automatico-de-projetos-estaticos-com-azure-static-web-apps-2nfj"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--realize-deploy-automatico-de-projetos-estaticos-com-azure-st.md"
    kind: repo
---

O artigo apresenta o Azure Static Web Apps como um serviço que cria e faz deploy automático de aplicações web a partir de um repositório no GitHub. O fluxo usa GitHub Actions, então push e pull requests monitorados podem disparar o deploy para o Azure. O texto também diz que a hospedagem de conteúdo estático é gratuita e inclui certificados SSL, versões de staging, integração com GitHub e suporte ao Azure Functions.

## Fichamento

- Azure Static Web Apps cria e faz deploy automático de aplicações web a partir de um repositório GitHub.
- O fluxo de implantação é baseado nas interações do GitHub e no GitHub Actions.
- Um push ou um pull request monitorado pode acionar o deploy automático para o Azure.
- A hospedagem de HTML, CSS, JavaScript e imagens é gratuita.
- O serviço inclui integração com Azure Functions, integração com GitHub, certificados SSL gratuitos e versões de staging.
- Os frameworks e geradores citados são Angular, React, Vue, Gatsby, Hugo, VuePress, Next.js e Nuxt.js.
- A demo usa Visual Studio Code, Vue, conta Azure e conta no GitHub.
- Para estudantes, o Azure for Students oferece crédito de USD 100 sem cartão de crédito.
- O processo usa um template de repositório no GitHub e depois a criação do recurso no Portal Azure.
- Na configuração do Azure, o repositório é conectado por meio de login no GitHub e autorização.
- As definições de build usam "/" em App Location, removem "api" de Api location e usam "dist" como pasta de saída no Vue.
- Depois da criação, o repositório recebe a pasta .github/workflows com um arquivo YAML do GitHub Actions.
- O fluxo criado gera CI e CD para que push, pull request ou commit disparem build e deploy.
- O artigo direciona para documentação oficial e cursos de aprendizado sobre Azure Static Web Apps.
