---
title: "The Game of Go: A Programmer's Perspective"
date: '2012-04-21T08:54:05-03:00'
category: webclip
summary: 'The post explains why Go is hard for AI programs and summarizes the methods that improved them: random playouts, bandit algorithms, limited expert knowledge, parallelization, and reinforcement learning.'
tags: ["go", "artificial-intelligence", "machine-learning", "game-programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Game of Go: a Programmer's Perspective - Need for Air"
    url: "http://needforair.com/blog/2012/04/18/game-of-go/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-04/needforair-com--the-game-of-go-a-programmer-s-perspective.md"
    kind: repo
---

The post argues that Go is a difficult AI problem because of its large game-tree complexity, the lack of a good heuristic, and the importance of pattern recognition. It also says that programs such as MoGo improved by using random play-outs, multi-armed bandit algorithms, some expert knowledge, parallelization, and reinforcement learning.

## Reading notes

- Go is presented as interesting for AI programmers because it is hard to build a computer that can compete with a strong human.
- The post says that randomly played games helped computers get much stronger.
- Go is described as popular in Asia but little known in the Western world.
- The board starts empty in Go, while chess begins with an army already on the board.
- Go has simpler rules than chess and only one type of stone.
- Even with simple rules, it has been very hard to build a good Go-playing program.
- Top chess programs can compete with the best humans, but strong amateur Go players can beat top Go programs.
- Go has a much larger game tree than chess because it has more turns and more possible moves per turn.
- Another difficulty is the lack of a good heuristic for evaluating positions.
- Strong Go players rely heavily on pattern recognition, and computers are worse at it in game time.
- The post identifies MoGo as a program that led to a spectacular improvement.
- MoGo evaluates positions by playing many random games from that position and using the win percentage as the score.
- Multi-armed bandit algorithms are used to reduce the branching factor.
- The program tries to balance exploration and exploitation when choosing moves.
- A small amount of expert knowledge is used to avoid trivially bad moves and to favor classic opening positions.
- The random games are not fully random, because some simple patterns are avoided.
- Parallelization makes MoGo-like programs run well on computer clusters because the random game part can use multiple CPUs.
- Reinforcement learning lowers the probability of responses that lead to bad results.
- The post says current Go programs can compete with professional players on 9x9 boards and with strong amateurs on 19x19 boards.
