---
title: "Deep Learning and Variants — Session 05: Regularization, Dropout, and Batch Normalization"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/foundations"]
sources:
  - "_raw/dba-course/Course_05_Deep_Learning_and_Variants/02_Recordings_and_PPTs/Session_05_29Nov2025/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Session covering bias-variance trade-off, L1/L2/elastic-net regularization, k-fold cross-validation, dropout regularization, and batch normalization as the final pillars for training robust deep neural networks."
---

# Deep Learning and Variants — Session 05: Regularization, Dropout, and Batch Normalization

**Instructor**: Dr. Srinivasa Varadharajan (Rajan)
**Date**: 2025-11-29
**Course**: [[course-05-overview-deep-learning-and-variants|Deep Learning and Variants]] (Course 05)

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=9OVy6zWjHIQ)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/IgDvdn58Zg5_Q6Ati_NJqnYmAVDedWvk3B6yUpC7xqmzhfI?e=f0Q7Us)
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/64249/393713/1186780/5915028)

## Key Concepts

### 1. Session Context — Prior Topics Recap
The session opened with a structured recap of previous sessions: vanishing gradients (and the shift from sigmoid to ReLU-family activations), mini-batch gradient descent with momentum (exponential moving average of gradients), learning-rate decay (exponential, hyperbolic, step), RMS-prop (EMA of gradient variance to adapt per-parameter step sizes), Adam (combining momentum and RMS-prop), and Xavier/Glorot weight initialization.

### 2. Train / Validation / Test Split Protocol
Data is partitioned into three stratified sets: ~72% training, ~8% validation, ~20% test (held in "cold storage" until a candidate model is confirmed). Stratification ensures the distribution of the target variable is identical across all three splits. If test performance fails after validation success, heterogeneity in the splits is the prime suspect.

### 3. K-Fold Cross-Validation
The training + validation data (~80%) is split into K equal folds (K = 10 is standard; K = 5 is an alternative). Each fold serves as the validation set exactly once while the remaining K-1 folds form the training set. This yields K validation errors per model configuration; the mean and standard deviation of those errors jointly characterize model quality. The goal: low mean error AND low standard deviation across folds.

### 4. Bias-Variance Trade-Off
- **Underfitting (high bias)**: too few parameters; training and validation errors are both high and similar. The model is too rigid to capture true patterns.
- **Overfitting (high variance)**: too many parameters; training error near zero but validation error explodes. The model memorizes training noise; performance collapses on new data.
- **Optimal model**: a compromise — moderate training error and validation error close together, both acceptably low. Rajan's consulting anecdote: a demand-forecasting model showed ~2–3% training error and ~200% validation error — a textbook overfit corrected by feature pruning until both converged near 20–40%.
- The bias-variance curve (validation error vs. model complexity) forms a characteristic U-shape; the minimum of the U defines the optimal complexity.

### 5. L2 Regularization (Ridge)
The cost function is augmented: **Loss = SSE + λ₂ · Σ βᵢ²**. Lambda (λ₂) is a hyperparameter supplied by the practitioner. When λ₂ → 0, the term vanishes and we are purely minimizing SSE (overfit risk). As λ₂ → ∞, the penalty dominates and forces all βᵢ toward zero (underfit risk). By sweeping λ₂ from near-zero to large values and plotting validation error, the optimal regularization strength is identified. Ridge never forces coefficients exactly to zero but shrinks them toward zero; a threshold must be applied manually for feature selection. Ridge is preferred when n (data rows) << p (features) and multicollinearity is expected.

### 6. L1 Regularization (Lasso)
**Loss = SSE + λ₁ · Σ |βᵢ|**. The absolute value penalty drives some coefficients to exactly zero, performing hard feature selection. LASSO stands for Least Absolute Shrinkage and Selection Operator. Preferred for large datasets without severe multicollinearity. Key differentiator from Ridge: genuine dimensionality reduction.

### 7. Elastic Net
A convex combination of L1 and L2 controlled by hyperparameter α: **α·L1 + (1−α)·L2**. When α = 0 → pure Ridge; α = 1 → pure Lasso. Elastic net handles multicollinearity (via the L2 term) while still driving some coefficients to zero (via L1). Used when neither Ridge nor Lasso alone is clearly superior.

### 8. Regularization in Neural Networks
In neural networks, the β parameters are replaced by weights W_{kl} and biases b_i across all neurons. Ridge-style regularization adds λ₂·(Σ bᵢ² + Σ W_{kl}²) to the loss. This is tractable for small networks but becomes computationally intractable for networks with billions of parameters, motivating the specialized techniques below.

### 9. Dropout Regularization
At each mini-batch iteration, a random proportion p of neurons (excluding the output layer, optionally including input) is "dropped" — their activations set to zero. Back-propagation updates only the active sub-network. The drop proportion is a hyperparameter (common values: 10–50%). On successive batches, different neurons are randomly dropped, so over training every synapse gets updated via different sub-network configurations. Biologically inspired by neural plasticity — analogous to surviving neurons compensating after brain injury or stroke.

**At inference time**: all neurons are present, but each weight is scaled by (1 − dropout rate) — the probability that the neuron was active during training — to correct for the fact that each weight was only present for a fraction of updates.

**Effect**: analogous to Ridge — no neuron is permanently removed, but the network learns robust, distributed representations. Dropout reduces the gap between training and test accuracy without pushing training accuracy to 100%.

### 10. Batch Normalization
Even if inputs are normalized (z-scored or min-max scaled to [0,1]), the weighted sums inside hidden layers are not guaranteed to remain normalized — weights and biases can re-introduce scale disparity at every layer. Batch normalization computes the mean and variance of each neuron's pre-activation output over the current mini-batch and normalizes it. This is applied after every hidden layer (not the output layer). During inference, the empirical mean and variance accumulated across all training batches are used as fixed normalization statistics.

**Practical impact**: Google's Inception model on ImageNet-scale data required ~31 million epochs to reach 72.2% accuracy without batch normalization; with batch normalization the same accuracy was reached in ~13 million epochs (≈58% reduction), and with further tuning in ~3 million epochs (≈90% reduction), while also improving peak accuracy to ~75%.

**Relationship to dropout**: batch normalization and dropout are considered complementary but competing approaches — modern practice leans toward batch normalization alone; using both simultaneously is generally avoided.

## Algorithms / Architectures Covered

| Technique | Type | Key Hyperparameter | Primary Use Case |
|---|---|---|---|
| K-Fold Cross-Validation | Evaluation protocol | K (default 10) | Model selection and error estimation |
| Ridge Regularization (L2) | Weight penalty | λ₂ | Small n, multicollinearity present |
| Lasso Regularization (L1) | Weight penalty + feature selection | λ₁ | Large n, hard feature elimination needed |
| Elastic Net | Combined L1 + L2 penalty | λ, α | When neither Ridge nor Lasso alone fits |
| Dropout | Noise-based regularization | Drop rate p | Large networks; alternative to batch norm |
| Batch Normalization | Layer-wise input normalization | — (placement is the design choice) | Deep networks; speeds convergence dramatically |
| Adam Optimizer | Adaptive gradient descent | β₁, β₂, ε | Standard optimizer for all deep networks |
| Xavier/Glorot Init | Weight initialization | Layer sizes nᵢ, nᵢ₊₁ | Prevents vanishing/exploding gradients at init |

## Important Intuitions & Examples

**The U-curve**: validation error as a function of model complexity (number of parameters) is the single most important diagnostic curve in supervised ML. Training error monotonically decreases toward zero; validation error decreases then rises. The minimum of validation error defines optimal model complexity.

**Regularization as a dial**: starting from an overfit model (all features, λ = 0) and increasing λ sweeps the model continuously from right to left on the bias-variance curve. The practitioner reads off the λ that minimizes validation error.

**Dropout as a random forest analogue**: Rajan drew an explicit parallel — dropping neurons randomly per batch is analogous to random subspace sampling in random forests; different sub-networks learn complementary representations of the same output.

**Batch normalization example (Inception / ImageNet)**: without batch normalization, 31 million epochs for 72.2% accuracy; with batch normalization, 3 million epochs for the same accuracy — a 10x speedup plus a 3 percentage-point accuracy gain. This was Rajan's central quantitative evidence for why batch normalization is now the default choice over dropout in modern deep networks.

**Standardization vs. Normalization**: standardization (z-score = (x − μ)/σ, range ≈ [−3, +3]) and normalization (min-max = (x − min)/(max − min), range [0, 1]) both put features on equal footing. In neural-network practice, standardization is more commonly used despite the API often being called "normalization."

**Practical consulting story**: demand forecasting for 2,500 spare-parts SKUs — heavily over-engineered features produced 2–3% training error but 200% validation error (maximum possible for the MAPE variant used). Systematic feature pruning brought validation error down to 20–40%, converging with training error, illustrating the textbook overfit-to-optimal transition.

## Related

- [[deep-learning|Deep Learning]]
- [[transfer-learning|Transfer Learning]]
- [[ensemble-methods|Ensemble Methods]]
- [[ai-paradigms|AI Paradigms]]
