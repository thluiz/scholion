---
title: "Why I still self host my servers (and what I've recently learned)"
date: '2026-09-24T23:13:41+01:00'
category: webclip
summary: 'O autor explica por que ainda self-hosting vale a pena: independência, aprendizado prático e melhor entendimento de sistemas complexos, apesar do trabalho e das falhas recentes.'
tags: ["self-hosting", "linux", "distributed-systems", "sysadmin"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why I still self host my servers (and what I've recently learned)"
    url: "https://chollinger.com/blog/2024/08/why-i-still-self-host-my-servers-and-what-ive-recently-learned/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/chollinger-com--why-i-still-self-host-my-servers-and-what-ive-recently-learn.md"
    kind: repo
---

The post argues that self-hosting still pays off because it supports independence and forces hands-on learning. The author ties that learning to better reasoning about complex systems and to work on distributed infrastructure.

It also lists recent problems and fixes from the last six months, including power and UPS failures, redundant DNS, Proxmox on ARM, ZFS memory tuning, hardware crashes, VPS outages, storage performance, object storage tradeoffs, and CrowdSec for intrusion prevention.

## Fichamento

- Mantém quase tudo em casa, exceto email, num cluster Proxmox com vários serviços e um VPS externo.
- Defende self-hosting por dois motivos centrais: autonomia frente a grandes empresas e aprendizado prático.
- Liga a experiência de operar infraestrutura própria à capacidade de entender sistemas distribuídos no trabalho.
- Usa exemplos de Linux, networking, Kubernetes, Kafka, Flink e outros componentes para mostrar essa sobreposição entre hobby e profissão.
- Relata falhas recentes como falta de energia, baterias de UPS mortas, DNS sem redundância, um host Proxmox que caía toda noite e um VPS fora do ar por dias.
- Diz que é possível self-hostar VS Code no navegador com code-server, útil em dispositivos como iPad ou Mac.
- Observa que baterias de UPS domésticas morrem silenciosamente e rápido, e passou a testar a UPS mensalmente.
- Reorganizou DHCP e DNS para ter dois caches Pi-hole disponíveis aos clientes e mapear IPs e dispositivos físicos.
- Colocou um Raspberry Pi 5 como nó Proxmox com apoio de um projeto de GitHub, embora a solução seja não suportada.
- Ajustou o consumo de memória do ZFS no Proxmox para evitar OOM kills em VMs durante backups.
- Descobriu que uma falha noturna vinha de um disco antigo e não redundante usado em backup; trocar o drive resolveu.
- Passou a usar LibreNMS com SNMPv3 para monitoramento e mapeamento da rede.
- Desconfiou do VPS da Contabo após dias de indisponibilidade e suporte que atribuiu o problema a DNS sem base.
- Migrou para um VPS da Hetzner, que em benchmark apareceu mais rápido que o anterior.
- Testou armazenamento remoto via CIFS e SSHFS e concluiu que ambos ficaram lentos, sobretudo com latência transatlântica.
- Avalia storage de objeto como solução barata para arquivos do Nextcloud, mas reconhece lentidão em listas e arquivos pequenos.
- Usa Wasabi para dados do Nextcloud via external storage, aceitando o custo e as limitações de S3.
- Adota CrowdSec como ferramenta de prevenção de intrusão e destaca os banimentos e métricas mostrados pela CLI.
