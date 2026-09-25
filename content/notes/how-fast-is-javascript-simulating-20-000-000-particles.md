---
title: "how fast is javascript? Simulating 20,000,000 particles"
date: '2026-09-25T08:01:04+01:00'
category: webclip
summary: 'O texto mostra, passo a passo, como a simulação em JavaScript melhora ao usar TypedArrays, SharedArrayBuffers, web workers, double buffering e um shader final para chegar a 20 milhões de partículas.'
tags: ["javascript", "sharedarraybuffer", "web-workers", "particle-simulation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "how fast is javascript? Simulating 20,000,000 particles"
    url: "https://dgerrells.com/blog/how-fast-is-javascript-simulating-20-000-000-particles?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dgerrells-com--how-fast-is-javascript-simulating-20-000-000-particles.md"
    kind: repo
---

The page follows a particle simulation in JavaScript from a simple single-threaded approach to a version that uses TypedArrays, SharedArrayBuffers, web workers, double buffering, and finally a GPU-based render path. The main constraint is to keep the simulation in JS and on the CPU as much as possible, while reducing cache misses and data-transfer costs.

The later versions change the bottleneck from rendering on the main thread to memory access and buffer accumulation. In the final comparison, the simulation stays on the CPU but rendering uses a full-screen quad with a texture based on particle counts, which lets the project reach 20,000,000 particles on an M1 Mac and scale better with more CPU cores.

## Fichamento

- A meta inicial é simular 1.000.000 de partículas em JavaScript puro, a 60 fps, em um celular e usando só a CPU.
- O texto rejeita a solução baseada em GPU e também evita WebAssembly, para manter o trabalho em JavaScript.
- A primeira ideia usa array de objetos, mas o autor passa a preferir dados contíguos e compactos na memória.
- TypedArrays entram como alternativa para guardar os dados das partículas em um buffer plano e contíguo.
- O primeiro desenho divide o trabalho entre vários web workers com SharedArrayBuffer e uma sinalização compartilhada.
- Cada partícula passa a ter x, y, dx e dy, armazenados como números de ponto flutuante de 32 bits.
- A renderização inicial usa ImageData no canvas, com cada partícula ocupando um pixel.
- O autor observa que a maior parte do tempo vai para desenhar as partículas no thread principal, e não para a simulação nos workers.
- A segunda versão adiciona entrada do mouse e toque ao buffer de simulação para puxar as partículas para o ponto tocado.
- A força usada na interação é baseada em uma aproximação da gravidade com distância ao quadrado no denominador, mas ajustada para produzir um efeito mais interessante.
- A terceira versão leva a renderização para os workers, mas isso cria flickering porque os workers limpam buffers enquanto o thread principal lê os mesmos dados.
- A quarta versão corrige o flickering fazendo o thread principal esperar os workers terminarem antes de renderizar.
- A quinta versão usa double buffering para permitir que os workers preparem um buffer enquanto o thread principal desenha o outro.
- O texto explica que o acesso aos pixels fica lento porque o padrão de leitura é pouco contíguo e causa cache misses.
- O autor conclui que a quantidade de dados excede o que cabe em cache, o que limita o ganho de performance.
- Na sexta versão, cada partícula guarda também sua posição inicial, e a simulação passa a puxá-la de volta para esse ponto, produzindo um efeito de fluido ou gelatina.
- Na sétima versão, o buffer de pixels é substituído por uma grade com a contagem de partículas por pixel, reduzindo memória e pressão sobre o cache.
- O texto compara o desempenho de chips Apple e Ryzen e relaciona a diferença ao tamanho do cache L1.
- Na comparação final, o autor mostra que instancing em three.js ainda sofre com o custo de enviar dados da simulação para a GPU a cada frame.
- A solução final usa a grade de contagem como textura e desenha um quad de tela cheia com shader, mantendo os dados enviados à GPU fixos no tamanho da resolução.
- O resultado final alcança 20 milhões de partículas em um M1 Mac por volta de 20 fps, com escala melhor em CPUs com mais núcleos.
