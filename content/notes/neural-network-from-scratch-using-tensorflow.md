---
title: "Neural Network from Scratch Using Tensorflow"
date: '2020-04-19T09:12:29+00:00'
category: webclip
summary: 'The article shows a small TensorFlow neural network built from scratch, with random parameter initialization, one hidden layer, MSE loss, gradient descent, and a loop that trains until loss drops under 0.1.'
tags: ["tensorflow", "neural-networks", "gradient-descent", "machine-learning"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Neural Network from Scratch Using Tensorflow"
    url: "https://dev.to/lankinen/neural-network-from-scratch-using-tensorflow-1kc8"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--neural-network-from-scratch-using-tensorflow.md"
    kind: repo
---

The article walks through a minimal TensorFlow neural network built from scratch. It uses one input example, initializes weights and biases with a normal distribution, applies two linear layers with a non-linear step between them, and measures error with mean squared error.

It then trains with `GradientTape` by making a prediction, computing loss, taking gradients, and updating the parameters with a learning rate. The loop continues until the loss is at or below 0.1, and the article ends by plotting how the loss changes over the training steps.

## Reading notes

- Builds a simple network from scratch in TensorFlow without hiding implementation details.
- Uses random input data `x` and a single target value `y`.
- Initializes `weights_1`, `bias_1`, `weights_2`, and `bias_2` with a normal distribution.
- Defines the network as two linear functions with a non-linear `maximum` step between them.
- Defines the loss as mean squared error.
- Uses a small learning rate stored in `lr`.
- Training follows three steps: predict, compute loss and gradients, then update parameters.
- Repeats training until the loss is less than or equal to `0.1`.
- Plots the loss over the number of steps after training.
