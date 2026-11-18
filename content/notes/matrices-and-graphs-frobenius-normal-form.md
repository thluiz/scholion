---
title: "Matrices and graphs"
date: '2023-12-07T11:14:27+00:00'
category: webclip
summary: 'Explains how nonnegative matrices correspond to digraphs, how matrix powers encode walks, and how strongly connected components and permutation matrices yield Frobenius normal form.'
tags: ["linear-algebra", "graph-theory", "matrix-theory"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Matrices and graphs"
    url: "https://thepalindrome.org/p/matrices-and-graphs"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/thepalindrome-org--matrices-and-graphs-frobenius-normal-form.md"
    kind: repo
---

The text presents the core idea that nonnegative matrices and directed graphs encode the same structure. Each matrix row/column corresponds to a node and each nonzero entry to a directed weighted edge, so powers of the matrix represent walks in the digraph, with applications such as Markov chains. Using this viewpoint, the article introduces strongly connected components, irreducible/reducible nonnegative matrices, and shows how a clever relabeling of nodes via permutation matrices brings any nonnegative matrix into Frobenius normal form.

## Reading notes

- A nonnegative matrix can be viewed as a directed, weighted graph where rows/columns are nodes and nonzero entries are directed edges with the corresponding weights.
- The entry in the i-th row and j-th column corresponds to an edge from node i to node j; edges for zero elements are omitted.
- Outgoing edges from a node correspond to the entries of its row, while incoming edges correspond to the entries of its column.
- Powers of the matrix encode walks in the associated digraph, with entries of A² aggregating all possible 2-step walks between nodes.
- When the digraph represents states of a Markov chain, powers of the transition probability matrix describe probabilities of being in various states after multiple steps.
- A directed graph is strongly connected if every node is reachable from every other node; otherwise, it is not strongly connected.
- Nonnegative matrices whose digraphs are strongly connected are called irreducible; other nonnegative matrices are reducible.
- Any digraph can be partitioned into strongly connected components, which are disjoint node subsets where nodes are mutually reachable within a subset but not between different subsets.
- The equivalence relation “a and b are mutually reachable” partitions the node set into strongly connected components.
- In the matrix corresponding to a digraph with strongly connected components, one can arrange indices so that diagonal blocks represent these components and the block below the diagonal is zero.
- This block upper-triangular structure, with irreducible diagonal blocks and zeros below, is called the Frobenius normal form for a nonnegative matrix.
- The article states a theorem asserting that every nonnegative square matrix can be transformed into Frobenius normal form using a permutation matrix.
- A simple 2×2 zero–one matrix is used to show that multiplying from the left swaps rows and multiplying from the right swaps columns.
- Multiplying a matrix from both left and right by this zero–one matrix swaps both rows and columns, which is described as a similarity transformation since the matrix is its own inverse.
- Such a similarity transformation does not change the underlying graph structure; it only relabels the graph’s nodes.
- In the n×n case, transposition matrices are defined by swapping the i-th and j-th rows of the identity matrix.
- Left-multiplication by a transposition matrix swaps rows; right-multiplication swaps columns, generalizing the 2×2 example.
- Transposition matrices satisfy specific properties summarized in the text, and similarity transformations with them just relabel two nodes while preserving graph structure.
- A permutation matrix is defined as a product of transposition matrices and inherits their properties.
- For permutation matrices, the inverse equals the transpose, and similarity transformations with them correspond to relabeling nodes without altering the digraph’s structure.
- Every node relabeling can be realized as a similarity transformation with a suitable permutation matrix.
- Proper node labeling is presented as the key ingredient for placing a matrix into Frobenius normal form.
- The article uses a concrete digraph example to illustrate how not all nodes are reachable from a given node, contrasting reachable sets with mutually reachable sets.
- Strongly connected components of a digraph are identified by grouping nodes that are mutually reachable; this decomposition is always possible.
- To use components for Frobenius form, the digraph is “skeletonized” by collapsing each strongly connected component into a single node and merging edges between components.
- In the skeleton graph, components that cannot be entered from any other component are designated zero-class components and serve as starting points.
- Each component is assigned a class number equal to the length of the longest path from the farthest zero-class component from which it can be reached.
- This classification ensures that if an m-th-class component is reachable from an n-th-class component, then n < m.
- The class numbers define a partial order on components and provide an ordering used for node labeling.
- Nodes are then labeled so that higher-order classes appear first and, where possible, consecutive indices are assigned to nodes within the same component.
- With this “clever” labeling, the adjacency matrix of the digraph exhibits the Frobenius normal form: irreducible blocks on the diagonal, zeros below, and possible nonzero blocks above.
- Because relabeling corresponds to similarity with a permutation matrix, this procedure gives the matrix form guaranteed by the Frobenius normal form theorem.
- The article highlights that this argument effectively completes the proof that any nonnegative square matrix can be permuted into Frobenius normal form.
- It notes that the matrix–graph connection extends further, enabling definitions of graph eigenvalues and leading to spectral graph theory.
- The author mentions that this connection has been fruitful for both graph theory and linear algebra and recommends further reading, including a book on matrix theory with a combinatorial approach and the author’s own book on the mathematics of machine learning.
