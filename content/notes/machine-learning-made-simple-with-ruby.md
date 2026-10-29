---
title: "Machine Learning made simple with Ruby"
date: '2015-08-25T10:43:35-03:00'
category: webclip
summary: 'The post shows how to add automatic announcement classification in Ruby with classifier-reborn, choosing an LSI classifier, training it from existing labeled items, and saving predictions back to the database.'
tags: ["ruby", "machine-learning", "classification", "latent-semantic-indexing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Machine Learning made simple with Ruby"
    url: "http://www.leanpanda.com/blog/2015/08/24/machine-learning-automatic-classification/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-08/leanpanda-com--machine-learning-made-simple-with-ruby.md"
    kind: repo
---

The post describes a Ruby-based way to automate category assignment for announcements without external prediction services. It uses the classifier-reborn gem, settles on Latent Semantic Indexing instead of a Bayesian classifier, and notes that LSI can also find texts similar to a query.

## Reading notes

- It starts from a project where users add announcements by link, metadata is fetched from OpenGraph tags, and an administrator still needs to assign a category before publishing.
- The goal is to suggest an appropriate category automatically for newly inserted content so administration does not become harder.
- The author first considers a Bayesian classifier, then switches to classifier-reborn after reading the gem’s documentation.
- LSI is presented as a better fit because it relies on the idea that words used in a given context tend to share meaning.
- The gem is also shown supporting reverse use, which lets the software search for related texts.
- Training is required, and in this case it can be done from already manually classified publications.
- The training step is moved to an asynchronous task because it is time-consuming and only needs to run periodically.
- One command object receives the advertisements to classify and the training data, then feeds each training title and category id into the classifier.
- Another command object handles the actual classification, classifies each advertisement title, updates the category, and marks the advertisement as classified.
- If the classifier raises VectorZeroVectorError because it was not trained, the code logs the error and does not update the record.
- The example concludes with a successful classification result and mentions an unresolved issue: retraining currently uses all published announcements every time, and storing the trained structure for later updates could be a better approach.
