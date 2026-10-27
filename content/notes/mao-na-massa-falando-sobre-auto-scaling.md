---
title: "Mão na Massa – falando sobre Auto Scaling"
date: '2013-01-30T09:42:33-03:00'
category: webclip
summary: 'O texto explica Auto Scaling na AWS como monitoramento e ajuste automático de EC2, integrando launch configurations, groups, triggers, ELB, SNS e CloudWatch para escalar com base em CPU.'
tags: ["aws", "auto-scaling", "cloudwatch", "elastic-load-balancer"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Mão na Massa – falando sobre Auto Scaling"
    url: "https://web.archive.org/web/20140110125750/http://awshub.com.br/resources/amazon-web-services-hands-on-auto-scaling"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/web-archive-org--mao-na-massa-falando-sobre-auto-scaling.md"
    kind: repo
---

O texto apresenta Auto Scaling como um mecanismo para adicionar e remover instâncias EC2 e também para monitorar falhas. Ele descreve os componentes principais, os custos e atrasos envolvidos no escalonamento e o uso de AMI, launch configuration, auto scaling group, triggers, ELB, SNS e CloudWatch.

## Fichamento

- Auto Scaling é mais do que subir e descer servidores; ele também monitora falhas de modo parecido ao que um load balancer faz com servidores que não respondem.
- O artigo mostra como configurar um Auto Scaling para iniciar automaticamente, monitorar e atualizar um ELB ligado às instâncias EC2.
- O Auto Scaling usa regras para ajustar a capacidade da nuvem e parte do princípio de um conjunto homogêneo de servidores.
- Os quatro componentes-chave são launch configuration, auto scaling group, scaling triggers e scaling event.
- Launch configuration reúne os parâmetros usados para iniciar uma instância, como AMI, tipo de instância, key pair e security group.
- O auto scaling group define a AZ, o load balancer e os limites mínimo e máximo de servidores.
- As triggers determinam quando adicionar ou subtrair servidores, com exemplos baseados na média de CPU por alguns minutos.
- Um scaling event é o ato de aumentar ou reduzir a capacidade do grupo.
- O texto destaca que a cobrança mínima do EC2 é de uma hora e que ciclos curtos podem aumentar o custo.
- O escalonamento leva tempo por causa da coleta do CloudWatch, do processamento pelo Auto Scaling, do boot da instância e da checagem do load balancer.
- Para seguir o tutorial, o leitor precisa de uma AMI criada a partir de um web server anterior.
- O artigo usa a linha de comando para obter o ID da AMI e para criar a launch configuration e o auto scaling group.
- O grupo é criado com um mínimo de uma instância e um máximo de cinco, ligado ao ELB LabELB.
- Ao terminar uma instância, o Auto Scaling a recria porque o grupo caiu abaixo do mínimo.
- Ao desligar uma instância, o Auto Scaling detecta a falha, termina a instância e lança outra no lugar.
- As instâncias criadas por Auto Scaling não recebem nome automaticamente, mas o texto mostra como usar tags para identificá-las.
- O Auto Scaling pode ser integrado ao ELB para adicionar automaticamente as instâncias ao balanceamento de carga.
- O texto mostra a criação de um tópico SNS, a assinatura por email e o uso do ARN para notificar eventos do Auto Scaling.
- As notificações configuradas cobrem lançamento e término de instâncias.
- O artigo cria duas políticas de escalonamento, uma para subir a capacidade e outra para reduzi-la.
- Um alarme de CloudWatch aciona a política de scale up quando a CPU fica em 50% ou mais por três minutos.
- Outro alarme aciona a política de scale down quando a CPU fica abaixo de 30% por três minutos.
- O texto recomenda subir rápido e descer devagar para lidar melhor com tráfego e custo.
- No teste final, uma carga artificial eleva a CPU, dispara o alarme, gera notificação e faz o grupo crescer.
- Depois, o grupo reduz instâncias com base no comportamento do alarme e na ordem de criação das instâncias.
- O artigo mostra como listar atividades de escalonamento e como suspender ou retomar processos do Auto Scaling.
- Ao final, o texto orienta apagar o auto scaling group e a launch configuration, além de encerrar as instâncias e os demais serviços pagos.
