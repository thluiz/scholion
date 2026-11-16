---
title: "How to Create a Machine Learning Decision Tree Classifier Using C#"
date: '2020-02-22T12:11:49+00:00'
category: webclip
summary: 'The article shows how to build a decision tree classifier from scratch in C# using Gini impurity, a list-based tree structure, and a small Iris dataset example in Visual Studio.'
tags: ["csharp", "decision-tree", "machine-learning", "gini-impurity"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Create a Machine Learning Decision Tree Classifier Using C# -- Visual Studio Magazine"
    url: "https://visualstudiomagazine.com/articles/2020/01/21/decision-tree-classifier.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/visualstudiomagazine-com--how-to-create-machine-learning-decision-tree-classifier-csha.md"
    kind: repo
---

The article explains how to turn splitting and disorder code into a working decision tree classifier in C#. It uses a 30-item subset of Fisher’s Iris dataset, builds a 7-node tree, reports 100% accuracy on the training items, and predicts the class of a new iris flower.

## Reading notes

- A decision tree classifier generates rules from predictor values, and the author says he prefers building one from scratch rather than using a library implementation.
- Implementing the classifier from scratch has two main tasks: repeatedly split training data into smaller subsets, then use those splits to build a tree that predicts a class.
- The demo uses 30 Iris data items with four predictors: sepal length, sepal width, petal length, and petal width.
- The three iris species are encoded as 0, 1, and 2.
- The tree node structure stores a node ID, the rows assigned to the node, the split column, the split value, class counts, and the predicted class.
- The demo stores nodes in a List<Node> in level order, so child and parent positions can be computed by index.
- The root node uses all 30 rows, has classCounts [10, 10, 10], and ties are broken by choosing the first tied class.
- The program is built as a C# console app in Visual Studio 2019 and can run as either .NET Core or .NET Framework.
- The DecisionTree class provides methods to build the tree, show nodes, predict a class, and compute accuracy.
- A SplitInfo helper class holds split-related values for dividing a node into left and right children based on Gini impurity.
