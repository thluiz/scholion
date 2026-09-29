---
title: "Linear Regression with Elixir, Phoenix and LiveView. Part I"
date: '2020-05-28T09:16:54-03:00'
category: webclip
summary: 'The post builds a simple linear regression model in Elixir, stores training points, and updates weights with gradient descent over multiple epochs to improve predictions.'
tags: ["elixir", "phoenix-liveview", "linear-regression", "gradient-descent"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Linear Regression with Elixir, Phoenix and LiveView. Part I ~ Tiemen"
    url: "https://tiemenwaterreus.com/posts/linear-regression-elixir-phoenix-liveview-i/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-05/tiemenwaterreus-com--linear-regression-elixir-phoenix-liveview-part-i.md"
    kind: repo
---

The post walks through a basic linear regression example in Elixir with Phoenix and LiveView as the project setup. It defines a model with weights m and b, a data struct for training points, and a train function that updates the model from X and Y pairs.

It explains training as repeated prediction, error calculation, and weight adjustment with a learning rate. The example shows how multiple epochs bring the prediction closer to the expected line, and it ends by pointing to a second part that will make the example interactive with LiveView.

## Reading notes

- Phoenix 1.5 makes it easier to start a new app with LiveView by passing the `--live` flag.
- The example project is created with `mix phx.new linreg --live --no-ecto`.
- The model keeps two values, `m` and `b`, and predicts with `b + m * x`.
- Training depends on prediction, error measurement, and repeated adjustment of the weights.
- The training data is a list of `(x, y)` points stored in a `%Data{}` struct.
- The `train/3` function computes average errors for `m` and `b` and subtracts them times the learning rate.
- The learning rate controls how small each update is so the model does not overshoot.
- One pass over the data is one epoch, and the post says multiple epochs are usually needed.
- The revised `train/3` function uses a `for` comprehension with `reduce` to run through the full dataset many times.
- With more training, the example moves closer to `Y = 2 * X + 0`, though it does not reach exact values.
- The post says the remaining gap comes from the learning rate and floating point arithmetic.
- The next part will use Phoenix LiveView to let clicks on a SVG plane generate training data and show the fitted line.
