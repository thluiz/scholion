---
url: "https://rewire.it/blog/why-foundation-models-in-pathology-are-failing-and-what-comes-next/"
captured_at: "2025-10-30T16:15:50+00:00"
title: "Why Foundation Models in Pathology Are Failing (and What Comes Next) | rewire.it | rewire.it Blog"
domain: "rewire-it"
---

---
## Why Foundation Models in Pathology Are Failing (and What Comes Next)

The model achieved 0.92 accuracy on our internal test set. At a neighboring hospital with different staining protocols, it performed barely above chance. After six months of debugging (checking data pipelines, retraining architectures, adjusting hyperparameters), the truth became clear.

We weren't facing an engineering problem. We were facing a category error.

The promise seemed straightforward. Foundation models had transformed natural language processing and general computer vision. Scale them up on unlabeled pathology data, went the reasoning, and you'd unlock the diagnostic patterns hidden in millions of histology slides. Hospitals would deploy them quickly. Clinical workflows would adapt to AI-assisted review.

But the reality I've observed across numerous pathology AI implementations tells a different story. Foundation models in pathology aren't failing because we haven't built them big enough or trained them long enough. They're failing because the field optimized for parameters we should have questioned: scale, generality, and architectural transplants from domains where tissue morphology simply doesn't follow the same rules.

This isn't a story of hopelessness. It's a story of misdirection, and how to correct course.

## The Performance Ceiling Nobody Talks About

Let's start with evidence. Recent clinical benchmarks evaluating 22 pathology tasks using publicly available self-supervised foundation models revealed a troubling pattern. The results looked promising on the surface: disease detection tasks achieved AUCs above 0.9 across all models tested.

But buried in that data was a different story.

When researchers moved from binary disease detection ("Is cancer present?") to biomarker prediction ("Which receptors are expressed?"), performance variability exploded. When they attempted immunotherapy response prediction, all tested models collapsed to approximately 0.6 AUC, barely above chance for binary classification.

Most revealing: **model size showed only weak correlation with downstream performance (r=0.055)**. The scaling laws that governed transformer scaling in NLP and general vision (where bigger almost always means better) simply don't apply to pathology.

![Foundation model performance comparison showing inconsistent results across clinical tasks](https://rewire.it/images/pdf-fig1-model-evaluation-chart.png)

_Figure 1: Performance evaluation reveals task-dependent results that contradict universal scaling assumptions. While detection tasks show strong performance, prognostic and predictive challenges that matter most clinically remain unsolved regardless of model size._

The implication is uncomfortable: foundation models have hit a performance ceiling on clinically important tasks, and throwing more parameters at the problem won't move that needle. We're not on a curve approaching clinical utility. We're on a plateau.

## Three Mechanisms Behind the Failure

### The Self-Supervision Problem

Foundation models rely on self-supervised learning (SSL) to learn representations without labels. They predict masked regions of images or compare similar augmentations. This works effectively for natural images. Predicting the next word in text carries enormous information. Reconstructing a masked region of a street scene teaches the model what matters visually.

Histopathology is fundamentally different.

When you mask a region of a pathology slide and ask a model to reconstruct it, what signal are you providing? Consider what a pathologist actually needs: the spatial relationships between glandular structures, the morphology of nuclei, the density of inflammatory infiltrate, the presence or absence of specific tissue architectures that indicate disease.

A self-supervised objective that predicts masked patches provides almost none of this information. The model learns texture, yes. But diagnostic relevance (the core of what a pathologist needs) isn't implicit in the reconstruction task. A foundation model trained to reconstruct pixels learns statistics about pixels, not about disease.

![Self-supervised learning architecture showing representation learning challenges in histology](https://rewire.it/images/pdf-fig3-ssl-architecture.png)

_Figure 2: Self-supervised approaches designed for natural images create weak training signals for tissue morphology. The model optimizes for pixel-level reconstruction rather than learning the structural patterns that indicate disease._

This is why dataset composition matters more than size. If your pretraining dataset emphasizes lung tissue, lung-related tasks improve modestly. But if it underrepresents your target tissue, performance doesn't magically emerge from scale. This reveals the contradiction in "foundation model": it's not truly foundational if performance depends critically on tissue prevalence in pretraining. You've built a specialized model with ambitious marketing.

### The Generalization Crisis

Here's a concrete finding that should concern every team implementing pathology AI: models generalize so poorly across institutions that they generate overconfident predictions about data they can't actually interpret.

Multi-institutional validation studies have found that models trained on single-center data experience **15-25% AUC performance drops** when evaluated on slides from different institutions. Stain color variations, scanner differences, sample preparation protocols, and population demographics create domain shifts that current approaches can't handle.

The paradox: these models report high confidence despite poor real-world performance. They're not saying "I'm uncertain." They're saying "I'm 95% confident" (incorrectly). This is domain miscalibration at scale.

![Domain shift failures across institutional boundaries](https://rewire.it/images/pdf-fig4-domain-shift-failures.png)

_Figure 3: Domain adaptation remains unsolved. Models trained at Institution A fail when deployed at Institution B, yet maintain high confidence scores. This visualization demonstrates how performance degrades across different clinical environments despite identical diagnostic tasks._

This is a safety problem dressed up as a technical one. Foundation models aren't robust to the natural variation inherent in clinical practice. They've been trained on curated, relatively homogeneous datasets and then deployed into messy reality. When a model trained on slides from Aperio scanners encounters Hamamatsu scanner output in production, it doesn't gracefully degrade. It fails while maintaining high confidence.

### The Complexity Trap

Foundation models, particularly transformer-heavy variants, are architecturally massive. A billion-parameter model for pathology represents engineering excess, not sophistication.

Research has shown these models face concerning adversarial vulnerabilities. Studies demonstrate that perturbations as small as 0.004 on a normalized scale (imperceptible to humans) can cause widespread misclassification in certain architectures. In many cases, architectural complexity correlates with increased vulnerability, particularly when models are overfit to training data characteristics.

Why does this matter clinically? Because in a hospital, there's stain drift, scanner variation, and equipment degradation. All small environmental changes that can appear as adversarial perturbations to an overfit model. A smaller, simpler model designed specifically for tissue morphology would be more robust to the noise inherent in clinical operations.

We've optimized for accuracy metrics on clean benchmark datasets. We've ignored robustness to the world as it actually exists.

## Why the Field Pursued This Path (And Why It Made Sense)

Before discussing solutions, we should understand why we got here. The path wasn't irrational. It was predictable.

Foundation models succeeded in NLP and general vision through a clear formula: scale up data collection, scale up model size, scale up computational resources, and performance improves. This worked so consistently it became accepted wisdom. Papers demonstrating scaling laws suggested that parameter count predicted capability with mathematical precision.

Academic incentives aligned with this approach. A billion-parameter model trained on a million slides is publishable in prestigious venues. A focused, task-specific model trained on a thousand carefully curated slides isn't, even if the latter works better clinically. Publication metrics influence careers. Scale influences publications.

Commercial incentives aligned similarly. A "foundation model" positions a company as having built something universal and defensible, something competitors can't easily replicate. A clinical-specific model admitting constraints feels smaller, less ambitious, harder to pitch to investors expecting transformative technology.

Regulatory and organizational environments encouraged it. Hospital IT departments know how to deploy general-purpose models into their existing infrastructure. Task-specific systems require domain expertise they don't have. A foundation model promises to be a platform, not a point solution.

**But clinical reality intervened.**

As of early 2024, no foundation models in pathology have FDA approval. Not one. The FDA has approved a small number of digital pathology AI systems, and all are task-specific, not foundation models. This isn't because FDA set impossibly high bars. It's because foundation models haven't cleared any bar. The clinical evidence isn't there.

No foundation models have been tested in randomized controlled trials. No foundation models have demonstrated better patient outcomes than alternatives in real clinical settings. The field is building at scale without validation.

## What Actually Works: The Alternative Approaches

Let me show you what clinical-grade pathology AI looks like when it's not pretending to be general-purpose.

Weakly supervised multiple instance learning (MIL) architectures have achieved **0.99 AUC on prostate cancer detection** and similar performance on basal cell carcinoma detection. No pixel-level annotations required. Only slide-level labels: the diagnosis that already exists in the pathology report.

One landmark study trained on **44,732 whole slide images** from 15,187 patients across multiple institutions. The model learned what diagnostic patterns matter without being told at pixel-level granularity. This is weakly supervised learning at scale, using the clinical data that naturally exists rather than demanding expensive expert annotations.

The critical finding: models trained this way **generalize better** to real-world data than fully supervised models trained on small, carefully curated datasets. A 20% performance drop often occurs when you take a fully supervised model trained on 1,000 perfect examples and apply it to real clinical data. Weakly supervised models trained on 40,000 messy, diverse real-world examples don't suffer that penalty.

This suggests something radical: the foundation model path (scaling up unlabeled pretraining and fine-tuning downstream) might be the wrong abstraction entirely for pathology. The data we need is already labeled at the level that matters clinically. We don't need self-supervised pretraining on unlabeled pixels. We need weakly supervised learning on naturally available slide-level diagnoses.

What about other directions?

**Geometric-aware architectures**: Tissue morphology has mathematical structure that transformers ignore. Spherical convolutions provide rotational invariance for tissue structures. Persistent homology (a technique from topological data analysis that captures multi-scale shape features) improves model accuracy and robustness. These approaches are simpler than transformers, require less data, and incorporate domain knowledge directly into architecture.

**Hybrid FM+MIL approaches**: If you must use foundation models, don't use them as end-to-end classifiers. Use them as feature extractors. Layer task-specific MIL aggregation on top. Recent research shows this maintains foundation model feature quality while recovering the interpretability and efficiency of MIL approaches. Different models dominate different tasks, which contradicts the foundation model premise anyway.

**Task-specific fine-tuning**: Stop pretending one model can handle all pathology. Build dedicated models for prostate cancer detection, separate models for breast biomarker prediction, different architectures for research vs. clinical deployment. Smaller, faster, more interpretable, and often more accurate on the specific task that matters.

These aren't theoretical alternatives. They're proven, deployed, sometimes FDA-cleared alternatives with real clinical evidence behind them.

## The Path Forward Requires Four Changes

If foundation models in pathology are failing due to conceptual misalignment rather than engineering limitations, then engineering alone won't save them. The field needs systemic change.

### First: Stop Conflating Scale with Capability

Abandon the assumption that bigger models and larger datasets automatically yield better clinical performance. The evidence doesn't support it. The r=0.055 correlation between model size and performance isn't just weak. It's devastating to the scaling narrative.

Instead, measure what actually matters: clinical accuracy on real-world data, generalization to new institutions, robustness to natural variation, safety under adversarial conditions, interpretability for clinical users. Pathology needs models that work in practice, not models that impress at conferences.

This means research incentives must shift. A task-specific model with prospective validation in three institutions and documented FDA submission matters more than a foundation model with state-of-the-art accuracy metrics on academic benchmarks. Publication venues should reward clinical validation, not parameter counts.

### Second: Make Interpretability Mandatory

Clinical adoption of AI depends on interpretability almost as much as accuracy. Pathologists need to understand why the model made its recommendation. Not for fairness audits, but for actual clinical decision-making. A 0.99 AUC model that's a black box is professionally useless. A 0.97 AUC model that highlights diagnostic regions and explains its reasoning is actionable.

Foundation models, by their nature, are less interpretable than task-specific alternatives. Transformers with attention across thousands of patches are harder to explain than attention-based MIL that explicitly aggregates evidence from localized regions. Billion-parameter models are harder to debug than models with millions of parameters and explicit architectural constraints.

If you're building for clinical deployment, start with interpretability as a hard constraint, not a nice-to-have feature. This single requirement eliminates many foundation model architectures from consideration. Which is the point.

### Third: Validate in Real Clinical Conditions

Foundation models in pathology have primarily been validated in-silico, on academic test sets, sometimes in single institutions with the same scanners and protocols used in training. This is insufficient. Clinical validation requires:

-   Multi-institutional testing with at least 5-10 different scanner types, staining protocols, and patient populations
-   Prospective evaluation in actual clinical workflow (not just retrospective analysis on archived slides)
-   Long-term performance monitoring post-deployment to catch degradation
-   Explicit testing of edge cases, failure modes, and adversarial robustness
-   Comparison to existing clinical alternatives (including pathologist performance), not just to baseline models

None of the major pathology foundation models have this evidence. Task-specific alternatives increasingly do. This validation gap isn't a minor oversight. It's the reason zero foundation models have FDA approval while task-specific systems do.

### Fourth: Invest in Domain-Specific Innovation

The most successful pathology AI systems in clinical deployment don't look like foundation models. They're specialized. They incorporate domain knowledge: tissue morphology, the diagnostic process, what clinicians actually need in real workflows.

Geometric approaches that respect tissue structure. Weakly supervised learning that works with naturally available labels. Attention mechanisms that localize diagnostic reasoning and produce interpretable evidence. Hybrid approaches that combine foundation model features with task-specific aggregation.

These aren't compromised versions of foundation models. They're fundamentally different approaches, better adapted to the actual pathology problem rather than the imagined one where histology is just another computer vision domain.

## What Foundation Models Should Actually Do

This isn't an argument against foundation models. It's an argument against false universality.

Foundation models excel at feature extraction when you have a domain-specific aggregation layer on top. They're useful for preprocessing and data synthesis when you need to augment limited training data. They can reduce annotation requirements for downstream tasks. In controlled settings with sufficient validation data, they contribute to ensembles that outperform single models.

The error was assuming they could be end-to-end diagnostic systems. That they could generalize from natural images to tissue without fundamental architectural changes. That scaling up would automatically solve domain adaptation, robustness, and interpretability problems. That one model could serve all pathology use cases.

The path forward isn't "abandon foundation models." It's "abandon the fantasy of universal foundation models and integrate them intelligently into domain-specific systems where they actually add value."

For healthcare AI professionals implementing systems today, this means:

-   **For detection systems** (benign/malignant classification): MIL approaches with attention mechanisms likely outperform foundation models, with better interpretability and lower computational cost
-   **For biomarker prediction or prognostication**: Task-specific models trained on your specific tissue type and your actual institutional data will generalize better than pretrained general models
-   **If using foundation models**: Use them as feature extractors with explicit domain-specific aggregation layers, not as end-to-end classifiers. Validate the hybrid system, not just the foundation model component.
-   **Before deployment**: Validate rigorously in real clinical conditions before going to production. Don't trust metrics from academic benchmarks. Test across multiple institutions, scanners, and staining protocols.

## A Question Worth Asking

The largest pathology foundation models represent enormous engineering effort and computational resources. The people building them aren't incompetent. They understand tissue morphology, deep learning, and clinical practice. Many have MD-PhD credentials and decades of combined experience.

So why haven't any achieved FDA clearance? Why do smaller, more focused approaches consistently beat them in real-world evaluation? Why does the scaling correlation hover around zero?

Because **optimization for the wrong target produces excellent results at that target while failing at the actual problem**. We optimized for model parameters, dataset size, and accuracy metrics on curated benchmarks. Pathology needed optimization for clinical utility, generalization across institutions, and robustness to real-world conditions.

This is fixable. It requires honesty about what's working and what isn't, and the discipline to pursue approaches that work even when they don't generate the same publication count or media attention as "billion-parameter foundation models."

The next generation of pathology AI won't be bigger. It will be smarter about what size and architectural approach actually fit the problem. It will be smaller, more interpretable, more rigorously validated, and more aware of its own limitations.

That's not a step backward. That's finally stepping in the right direction.

___

_Note: This article references several studies and findings in the pathology AI field. While specific citations have been generalized to protect ongoing research, the patterns described reflect consistent observations across multiple institutions and research groups. Healthcare AI professionals are encouraged to validate these findings against their own institutional experiences._
