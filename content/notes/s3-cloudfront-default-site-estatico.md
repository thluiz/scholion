---
title: "S3 + CloudFront como default para sites estáticos"
date: 2026-04-16T10:41:55+01:00
summary: "Depois de migrar o Scholion do Azure, o padrão S3 + CloudFront (bucket privado, OAC, CloudFront Function, cache diferenciado) revela-se como o default comoditizado."
tags: ["aws", "deploy", "infraestrutura", "sites-estaticos"]
has_commentary: true
sources:
  - title: "Getting started with a secure static website (CloudFront + S3)"
    publisher: "AWS Documentation"
    url: "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/getting-started-secure-static-website-cloudfront-s3.html"
    kind: other
  - title: "Restricting access to an Amazon S3 origin (OAC)"
    publisher: "AWS Documentation"
    url: "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html"
    kind: other
  - title: "Customize at the edge with CloudFront Functions"
    publisher: "AWS Documentation"
    url: "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html"
    kind: other
---

Migrar o Scholion do Azure Static Web Apps para AWS S3 + CloudFront levou uma tarde. Nesse processo percebi que o desenho já é o default comoditizado: bucket privado atrás de CDN, ACM, uma função no edge.

Os componentes:

- **S3 privado**, com public access block completo. O bucket guarda os arquivos e ninguém fala com ele diretamente.
- **Origin Access Control** (OAC). Substituiu a velha OAI. Só aquela distribution específica pode ler o bucket, identificada pelo `AWS:SourceArn` na bucket policy.
- **CloudFront Function**. JS nos edges, com runtime mais leve que Lambda@Edge. Reescreve `/notes/` para `/notes/index.html` antes do cache. Hugo gera pretty URLs, S3 não serve diretórios, o CDN faz a ponte. 10M invocações grátis por mês.
- **ACM wildcard**. Um cert para `*.thluiz.com`, renova automaticamente via CNAME de validação. Grátis.
- **Cache split** no deploy: HTML com `max-age=3600`, assets estáticos com `max-age=31536000, immutable`. Hugo gera nomes estáveis para CSS/JS/imagens, então o `immutable` é literal. Invalidar `/*` a cada push custa cêntimos e poupa raciocínio sobre versionamento.

### Comparação

- **Azure Static Web Apps**: em PaaS, quando algo quebra fora do teu código, os caminhos de diagnóstico e correção são os que o provider oferece. Se o suporte é lento ou ausente, o site fica offline e você não tem como destravar. O GitHub Actions continua a reportar deploy com sucesso enquanto o CDN serve vazio.
- **GitHub Pages**: sem controle de `cache-control`, sem regras de rewrite, sem cert no apex sem salto. Serve para READMEs.
- **Netlify / Vercel / Cloudflare Pages**: o bastidor é o mesmo padrão (object store + CDN) com UI por cima e política de free tier mutável. A UI custa dependência de uma política que eles podem mudar.

### Por que S3 + CloudFront venceu

O acoplamento é baixo. Cada componente é comoditizado: GCS + Cloud CDN fazem o mesmo, R2 + Cloudflare Workers fazem o mesmo. Migrar para outro provider é trocar um script, não reescrever uma aplicação. O lock-in está na automação (workflow YAML, CLI), não na arquitetura.

Custo estimado do Scholion: ~$0.10/mês. Free Tier AWS cobre a maior parte, o restante é tráfego residual de um blog pessoal. O custo zero da Azure custa caro quando não há suporte adequado.
