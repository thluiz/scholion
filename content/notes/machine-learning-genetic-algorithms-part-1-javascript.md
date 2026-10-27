---
title: "Machine Learning: Genetic Algorithms Part 1 (Javascript)"
date: '2012-09-10T09:01:43-03:00'
category: webclip
summary: 'The post introduces genetic algorithms as a way to search for solutions through cost functions, crossover, mutation, and populations, using a Javascript Hello, World example.'
tags: ["genetic-algorithms", "machine-learning", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Machine Learning: Genetic Algorithms Part 1 (Javascript) | Burak Kanber's Blog"
    url: "http://burakkanber.com/blog/machine-learning-genetic-algorithms-part-1-javascript/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-09/burakkanber-com--machine-learning-genetic-algorithms-part-1-javascript.md"
    kind: repo
---

The post introduces genetic algorithms as a machine learning approach that is less practical than many others, but useful for showing cost functions, local and global optima, crossover, and mutation. It uses a contrived Javascript example that tries to reproduce “Hello, World!” and explains the basic pieces of a genetic algorithm through that task.

## Reading notes

- Genetic algorithms generate many answer candidates and score them with a cost or fitness function.
- In the example, the chromosome is a 13-character string that should match “Hello, World!”.
- The cost function compares each character’s ASCII value to the target and squares the difference.
- Mating, or crossover, combines two chromosomes by splitting them at a pivot point and swapping halves.
- Mutation changes a random character so the search does not stay trapped in a local optimum.
- A population is a group of chromosomes that goes through generations of scoring, sorting, killing weaker members, mating stronger ones, mutating, and checking for completion.
- The example starts from random strings and stops when the cost reaches 0.
- The code defines Gene and Population objects with methods for random generation, cost calculation, mating, mutation, sorting, and advancing generations.
