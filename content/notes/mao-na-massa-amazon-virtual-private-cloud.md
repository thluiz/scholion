---
title: "Mão na Massa – Amazon Virtual Private Cloud"
date: '2013-01-10T11:47:56-03:00'
category: webclip
summary: 'O artigo mostra como criar uma VPC com subredes pública e privada no wizard da AWS, explica os objetos gerados e ensina a lançar instâncias EC2 e testar conectividade com Elastic IP.'
tags: ["amazon-vpc", "ec2", "subredes", "elastic-ip"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Mão na Massa – Amazon Virtual Private Cloud"
    url: "https://web.archive.org/web/20130626102722/http://imasters.com.br/desenvolvimento/mao-na-massa-amazon-virtual-private-cloud/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/web-archive-org--mao-na-massa-amazon-virtual-private-cloud.md"
    kind: repo
---

O artigo mostra como usar o wizard de VPC para criar uma VPC com subredes pública e privada e depois explica os objetos criados nesse processo. Também apresenta o lançamento de instâncias EC2 em cada subnet, a associação de um Elastic IP ao servidor público e o teste de conectividade.

## Fichamento

- Usar o wizard da AWS para criar uma VPC com subredes pública e privada.
- Definir a subnet pública como 10.0.0.0/23 e a privada como 10.0.10.0/23 para reservar espaço de crescimento.
- O wizard cria uma instância NAT para permitir acesso à Internet a partir das subredes privadas.
- O wizard cria e associa tabelas de rotas, um Internet Gateway, opções de DHCP, um Elastic IP, uma NACL padrão e um security group padrão.
- A subnet pública usa uma rota para o Internet Gateway, enquanto a subnet privada usa a instância NAT como rota padrão.
- A tabela de rotas main define o tratamento padrão para subredes que não têm associação explícita com outra tabela.
- O Internet Gateway fica anexado à VPC e pode ser anexado ou desanexado de forma independente.
- As opções de DHCP podem definir DNS, NTP e configurações ligadas a NetBIOS para a VPC.
- A instância NAT é uma instância Amazon Linux com masquerading de IP habilitado via iptables, e com source/destination check desabilitado.
- Para criar um servidor privado, escolher a subnet privada, manter as opções padrão e criar um security group para acesso privado.
- A instância privada recebe apenas IP privado e não recebe public DNS nem Elastic IP.
- Para criar um servidor público, escolher a subnet pública e criar um security group que permita ping e SSH.
- Uma instância na subnet pública ainda precisa de um Elastic IP para ficar acessível de fora.
- Depois de alocar um novo Elastic IP de VPC, associá-lo à instância pública para habilitar a conectividade externa.
- Antes de apagar a VPC, terminar as instâncias e liberar o Elastic IP.
