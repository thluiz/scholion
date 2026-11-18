---
url: "https://thepalindrome.org/p/matrices-and-graphs"
captured_at: "2026-11-18T10:53:45+00:00"
title: "Matrices and graphs"
domain: "thepalindrome-org"
---

The single most undervalued fact of linear algebra: matrices are graphs, and graphs are matrices.

[

![](https://substackcdn.com/image/fetch/$s_!50Fu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb99e7f0a-d78c-4e23-b76b-ba63577a3eb5_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!50Fu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb99e7f0a-d78c-4e23-b76b-ba63577a3eb5_1920x1080.png)

A (nonnegative) matrix and its graph

Encoding matrices as graphs is a cheat code, making complex behavior simple to study.

Let me show you how!

_📌 The Palindrome breaks down advanced math and machine learning concepts with visuals that make everything click._

_[Join the premium tier](https://thepalindrome.org/subscribe) to get access to [the upcoming live courses](https://thepalindrome.org/p/announcing-the-palindrome-lecture) on Neural Networks from Scratch and Mathematics of Machine Learning._

If you looked at the example above, you probably figured out the rule.

Each row is a node, and each element represents a directed and weighted edge. Edges of zero elements are omitted. The element in the _i_\-th row and _j_\-th column corresponds to an edge going from _i_ to _j_.

The resulting graph is called _the directed graph_ (or _digraph_) _of the matrix._

To unwrap the definition a bit, let's check the first row, which corresponds to the edges outgoing from the first node.

[

![](https://substackcdn.com/image/fetch/$s_!VRjJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7589034c-9945-41c8-ae03-c99cd611299a_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!VRjJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7589034c-9945-41c8-ae03-c99cd611299a_1920x1080.png)

The first row corresponds to the edges outgoing from the first node

Similarly, the first column corresponds to the edges incoming to the first node.

[

![](https://substackcdn.com/image/fetch/$s_!yR_v!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15bc5c5f-bef6-426a-ad89-1827814422e4_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!yR_v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15bc5c5f-bef6-426a-ad89-1827814422e4_1920x1080.png)

The first column corresponds to the edges incoming to the first node

Here is the full picture, with the nodes explicitly labeled.

[

![](https://substackcdn.com/image/fetch/$s_!Xh34!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4d9b1c5-38ee-4168-b29b-ce57426021d6_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!Xh34!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4d9b1c5-38ee-4168-b29b-ce57426021d6_1920x1080.png)

Why is the directed graph representation beneficial for us?

For one, the powers of the matrix correspond to walks in the graph.

Take a look at the elements of the square matrix. All possible 2-step walks are accounted for in the sum defining the elements of A².

[

![](https://substackcdn.com/image/fetch/$s_!ZOK0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2614d942-33c0-4c5b-aa8c-e237e92d86be_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!ZOK0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2614d942-33c0-4c5b-aa8c-e237e92d86be_1920x1080.png)

Powers of the matrix describe walks on its directed graph

If the directed graph represents the states of a Markov chain, the square of its transition probability matrix essentially shows the probability of the chain having some state after two steps.

There is much more to this connection.

For instance, it gives us a deep insight into the structure of nonnegative matrices.

To see what graphs show about matrices, let's talk about the concept of strongly connected components.

A directed graph is strongly connected if every node can be reached from every other node.

If this is not true, the graph is not strongly connected.

Below, you can see an example of both.

[

![](https://substackcdn.com/image/fetch/$s_!a9vq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd755da7-42c3-4220-9543-4da6019ccc47_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!a9vq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd755da7-42c3-4220-9543-4da6019ccc47_1920x1080.png)

Strongly connectedness

Matrices that correspond to strongly connected graphs are called irreducible. All other nonnegative matrices are called reducible. Soon, we'll see why.

(For simplicity, I assumed each edge to have a unit weight, but each weight can be an arbitrary nonnegative number.)

[

![](https://substackcdn.com/image/fetch/$s_!b6qf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79544ec4-06fb-4306-ae05-17ba51b7095f_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!b6qf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79544ec4-06fb-4306-ae05-17ba51b7095f_1920x1080.png)

Strongly connected digraphs and

Back to the general case!

Even though not all directed graphs are strongly connected, we can partition the nodes into strongly connected components.

[

![](https://substackcdn.com/image/fetch/$s_!bDNH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff46d79d0-6d58-4a7b-8083-1e797fcd1ec0_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!bDNH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff46d79d0-6d58-4a7b-8083-1e797fcd1ec0_1920x1080.png)

Strongly connected components

Let's label the nodes of this graph and construct the corresponding matrix!

[

![](https://substackcdn.com/image/fetch/$s_!x5R6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73453e6e-e1f4-47a1-b016-4bad6c19b3e6_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!x5R6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73453e6e-e1f4-47a1-b016-4bad6c19b3e6_1920x1080.png)

(For simplicity, assume that all edges have unit weight.) Do you notice a pattern?

The corresponding matrix of our graph can be reduced to a simpler form!

[

![](https://substackcdn.com/image/fetch/$s_!5yyV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd486b27a-2fce-476f-b165-e067383016bb_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!5yyV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd486b27a-2fce-476f-b165-e067383016bb_1920x1080.png)

Its diagonal comprises blocks whose graphs are strongly connected. (That is, the blocks are irreducible.) Furthermore, the block below the diagonal is zero.

Is this true for all nonnegative matrices?

You bet. Enter the Frobenius normal form.

In general, this block-matrix structure that we have just seen is called the Frobenius normal form.

[

![](https://substackcdn.com/image/fetch/$s_!Evb_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb081d3dd-7a20-4ce9-8814-349313083134_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!Evb_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb081d3dd-7a20-4ce9-8814-349313083134_1920x1080.png)

The Frobenius normal form

If you have a sharp eye with a hint of OCD, you probably noticed that I switched up the colors a bit. From now on, irreducible blocks (a.k.a. matrices that correspond to strongly connected graphs) will be colored maize, while reducible ones will be light blue.

Let's reverse the question: can we transform an arbitrary nonnegative matrix into the Frobenius normal form?

Yes, and with the help of directed graphs, this is much easier to show than purely using algebra.

Here is the famous theorem in full form.

[

![](https://substackcdn.com/image/fetch/$s_!VqN3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01132c7f-4adb-4aa5-bf99-881b16c9c80c_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!VqN3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01132c7f-4adb-4aa5-bf99-881b16c9c80c_1920x1080.png)

But what are permutation matrices?

Let’s look at a special case: what happens if we multiply a _2 x 2_ matrix with

[

![](https://substackcdn.com/image/fetch/$s_!5WsX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77d93a2d-6332-4136-ac75-9587cc9a28e5_1920x700.png)

](https://substackcdn.com/image/fetch/$s_!5WsX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77d93a2d-6332-4136-ac75-9587cc9a28e5_1920x700.png)

a simple zero-one matrix? With a quick calculation, you can verify that

1.  it switches the _rows_ when multiplied from the left,
    
2.  and it switches the _columns_ when multiplied from the right.
    

Just like this:

[

![](https://substackcdn.com/image/fetch/$s_!j1In!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27ae5eff-61d1-4854-a0a6-0f6492a63152_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!j1In!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27ae5eff-61d1-4854-a0a6-0f6492a63152_1920x1080.png)

Multiplying with _P_ from both left and right compounds the effects: it switches rows and columns.

[

![](https://substackcdn.com/image/fetch/$s_!H1P9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff386d43f-e34d-491f-9144-ac25e1d95524_1920x700.png)

](https://substackcdn.com/image/fetch/$s_!H1P9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff386d43f-e34d-491f-9144-ac25e1d95524_1920x700.png)

(By the way, this is a similarity transformation, as our special zero-one matrix is its own inverse. This is not an accident; more about it later.)

Why are we looking at this? Because behind the scenes, this transformation doesn’t change the underlying graph structure, just relabels its nodes!

You can easily verify this by hand, but I visualized it for you below.

[

![](https://substackcdn.com/image/fetch/$s_!0oNj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78da0e89-6149-4840-9572-543daa9b9150_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!0oNj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78da0e89-6149-4840-9572-543daa9b9150_1920x1080.png)

A similar phenomenon is true in the general _n x n_ case. Here, we define the so-called transposition matrices by switching the _i_\-th and _j_\-th rows of the identity matrix:

[

![](https://substackcdn.com/image/fetch/$s_!8mMd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea175486-c32b-4fdd-8c8d-576f4747411d_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!8mMd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea175486-c32b-4fdd-8c8d-576f4747411d_1920x1080.png)

Multiplication with a transposition matrix has the same effect: switches rows from the left, and switches columns from the right.

We are not going to spell it out in detail (as the overcomplicated notation makes it especially painful), but you can verify by hand that this is indeed what’s going on.

Here is a brief summary. Take note of these, as they’ll be essential in a bit.

[

![](https://substackcdn.com/image/fetch/$s_!ywYA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0c3db35-152b-4526-9eba-9fbb0a93baa8_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!ywYA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0c3db35-152b-4526-9eba-9fbb0a93baa8_1920x1080.png)

Properties of transposition matrices

The most important property for us: similarity transformations with transposition matrices just relabel two nodes, but otherwise leave the graph structure invariant.

Now, about the aforementioned permutation matrices. A _permutation matrix_ is simply a product of transposition matrices.

[

![](https://substackcdn.com/image/fetch/$s_!Xcrg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F982ee614-b6e4-4380-a75c-0bf0813b47ff_1920x700.png)

](https://substackcdn.com/image/fetch/$s_!Xcrg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F982ee614-b6e4-4380-a75c-0bf0813b47ff_1920x700.png)

Permutation matrices inherit some properties from their building blocks. Most importantly,

1.  their inverse is their transpose,
    
2.  and a similarity transformation with them is just a relabeling of nodes that leave the graph structure invariant.
    

To see this latter one, consider the following argument below.

[

![](https://substackcdn.com/image/fetch/$s_!loVL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6815dd8a-a30c-44bb-9bf5-163999c06ff8_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!loVL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6815dd8a-a30c-44bb-9bf5-163999c06ff8_1920x1080.png)

(Recall that transposing a matrix product switches up the order, and transposition matrices are their own transposes.)

Conversely, every node relabeling is equivalent to a similarity transformation with a well-constructed permutation matrix.

Why are we talking about this? Because the proper labeling of nodes is key to the Frobenius normal form.

Now, let’s talk about graphs. We’ll see how _every_ digraph decomposes into strongly connected components. For that, let’s see a concrete one.

[

![](https://substackcdn.com/image/fetch/$s_!bO4M!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb28c6668-2e85-4f8b-b7da-9b375ad30742_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!bO4M!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb28c6668-2e85-4f8b-b7da-9b375ad30742_1920x1080.png)

This’ll be our textbook example.

How many nodes can be reached from a given node? Not necessarily all. Say, for the one at the bottom right, only a portion of the graph is accessible.

[

![](https://substackcdn.com/image/fetch/$s_!_kR0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00781278-c87e-4432-95f7-a8c1e2371611_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!_kR0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00781278-c87e-4432-95f7-a8c1e2371611_1920x1080.png)

However, the set of mutually reachable nodes is much smaller.

[

![](https://substackcdn.com/image/fetch/$s_!ern2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84ee626b-17e8-41b7-9a18-266c88ef6099_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!ern2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84ee626b-17e8-41b7-9a18-266c88ef6099_1920x1080.png)

Algebraically speaking, the relation _“a and b are mutually reachable from each other“_ is an equivalence relation. In other words, it partitions the set of nodes into disjoint subsets such that

1.  two nodes from the same subset are mutually reachable from each other,
    
2.  and two nodes from different subsets are _not_ mutually reachable.
    

(Equivalence relations are the workhorses of mathematics. If you are not familiar with them, check out [this Wikipedia article about partitions](https://en.wikipedia.org/wiki/Partition_of_a_set#Partitions_and_equivalence_relations) to see how they relate.)

The subsets of this partition are called the _strongly connected components_, and we can always decompose a directed graph in this way.

[

![](https://substackcdn.com/image/fetch/$s_!MmAu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c45e6ff-bfb5-4968-89b7-080c5be39b1f_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!MmAu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c45e6ff-bfb5-4968-89b7-080c5be39b1f_1920x1080.png)

Now, let’s connect everything together! (Not in a graph way, but you know, in a wholesome mathematical way.)

We are two steps away from proving that every nonnegative square matrix can be transformed into Frobenius normal form with a permutation matrix.

Here is the plan.

1.  Construct the graph for our nonnegative matrix.
    
2.  Find the strongly connected components.
    
3.  Relabel the nodes in a clever way.
    

And that’s it! Why? Because, as we have seen, relabeling is the same as a similarity transform with a permutation matrix.

There’s just one tiny snag: what is the clever way? I’ll show you.

First, we “skeletonize” the graph: merge the components together, as well as any edges between them. Consider each component as a black box: we don’t care what’s inside, only about their external connections.

[

![](https://substackcdn.com/image/fetch/$s_!_D4A!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a595a59-706d-4ede-8e1c-0fd20c969db9_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!_D4A!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a595a59-706d-4ede-8e1c-0fd20c969db9_1920x1080.png)

In this skeleton, we can find that components that cannot be entered from another components. These will be our starting points, the zeroth-class components. In our example, we only have one.

[

![](https://substackcdn.com/image/fetch/$s_!pezM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7ab529a1-b01e-441b-9b15-f13080fb1543_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!pezM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7ab529a1-b01e-441b-9b15-f13080fb1543_1920x1080.png)

Now, things get a bit tricky. We number each component by the longest path from the farthest zero-class component from which it can be reached.

This is hard to even read, let alone to understand. So, here is what’s happening.

[

![](https://substackcdn.com/image/fetch/$s_!_2hm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2f1d470-3cda-48b3-9670-27d55a401b39_1920x700.png)

](https://substackcdn.com/image/fetch/$s_!_2hm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2f1d470-3cda-48b3-9670-27d55a401b39_1920x700.png)

The gist is that if you can reach an _m_\-th-class from an _n_\-th-class, then _n < m_.

In the end, we have the following.

[

![](https://substackcdn.com/image/fetch/$s_!Ih0h!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06dc244b-79a7-4e00-9060-0b64d0be730c_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!Ih0h!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06dc244b-79a7-4e00-9060-0b64d0be730c_1920x1080.png)

Numbering of the classes

This defines an ordering on the components. (A [partial ordering](https://en.wikipedia.org/wiki/Partially_ordered_set), if you would like to be precise.)

Now, we label the nodes inside such that

*   higher-order classes come first,
    
*   and consecutive indices are labeling nodes from the same component if possible.
    

This is how it goes.

[

![](https://substackcdn.com/image/fetch/$s_!rfxJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a105527-482e-406d-85e5-137f622672d3_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!rfxJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a105527-482e-406d-85e5-137f622672d3_1920x1080.png)

That ominous clever node labeling

If the graph itself is coming from an actual matrix, such a relabeling yields the Frobenius normal form!

Here is the matrix in this particular example, with zeros and ones for simplicity:

[

![](https://substackcdn.com/image/fetch/$s_!ZaDO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc26804da-7d73-46d7-8213-1d208689de06_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!ZaDO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc26804da-7d73-46d7-8213-1d208689de06_1920x1080.png)

The adjacency matrix of our cleverly labeled graph

Now we have everything, and the “proof” behind the transformation to Frobenius normal form is complete!

To remind you, this is the theorem in its full form:

[

![](https://substackcdn.com/image/fetch/$s_!GcAa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6810ee8e-f9e2-4151-aefc-6ee0120a9feb_1920x1080.png)

](https://substackcdn.com/image/fetch/$s_!GcAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6810ee8e-f9e2-4151-aefc-6ee0120a9feb_1920x1080.png)

What we have seen is just the tip of the iceberg. For example, with the help of matrices, we can define the eigenvalues of graphs! This idea gave birth to the fascinating topic of spectral graph theory, a beautiful field of mathematics.

Utilizing the relation between matrices and graphs has been extremely profitable for both graph theory and linear algebra.

If you are interested in the details, I have two books to recommend to you. One is the fantastic [A Combinatorial Approach to Matrix Theory and Its Applications](https://www.taylorfrancis.com/books/mono/10.1201/9781420082241/combinatorial-approach-matrix-theory-applications-richard-brualdi-dragos-cvetkovic) by Richard A. Brualdi and Dragos Cvetkovic, my favorite learning resource on the topic.

Second, I recently finished writing my [Mathematics of Machine Learning book](https://www.packtpub.com/en-us/product/mathematics-of-machine-learning-9781837027873). This post is a part of that book! Besides the connection between graphs and matrices, there are about 700 pages of intuitive and richly illustrated explanations about essential concepts from mathematics. Check it out!
