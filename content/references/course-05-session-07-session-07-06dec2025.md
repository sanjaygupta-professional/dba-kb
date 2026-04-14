---
title: "Deep Learning and Variants — Session 07: Autoencoders, Embeddings, and Principal Component Analysis"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/foundations"]
sources:
  - "_raw/dba-course/Course_05_Deep_Learning_and_Variants/02_Recordings_and_PPTs/Session_07_06Dec2025/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Introduces autoencoders as mirror-symmetric identity networks for dimensionality reduction and cross-modal generation, contrasts them with PCA via eigenvalue decomposition, and closes with encoder-decoder composition as the architectural root of generative AI."
---

# Deep Learning and Variants — Session 07: Autoencoders, Embeddings, and Principal Component Analysis

**Instructor**: Dr. Srinivasa Varadharajan (Rajan)
**Date**: 2025-12-06
**Course**: [[course-05-overview-deep-learning-and-variants|Deep Learning and Variants]] (Course 05)

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=_dv6HxbIngc)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/IgBgkkg5XtdhQowhsym7L61cAX5sX0D7U27YLhxNqWNVw4Q?e=aNqYe4)
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/64249/393713/1187589/5918762)

---

## Key Concepts

### 1. Deep Neural Network Parameters — Recap
Learning in a DNN means fixing **weights** (synaptic strengths between neurons) and **biases** (neuron-level intercepts). The challenge of deep networks stems from two compounding factors: depth itself and the nonlinearities introduced by activation functions.

### 2. Vanishing Gradients and the ReLU Fix
Sigmoid activations have a maximum derivative of ~0.25. During backpropagation, this factor is multiplied layer-by-layer, driving gradients toward zero in early layers and halting weight updates — the **vanishing gradient problem**. The solution: replace hidden-layer sigmoids with **ReLU** (a thresholding / ramp function), which preserves gradient magnitude. Output layers retain sigmoid or softmax as appropriate.

### 3. Gradient Descent Variants — Momentum, RMSProp, Adam
- **Mini-batch gradient descent**: a compromise between online (one sample) and full-batch processing; one pass through all mini-batches constitutes one **epoch**.
- **Learning rate scheduling**: step decay (halving every N epochs), exponential decay, or hyperbolic decay — all reduce the learning rate progressively to accelerate convergence.
- **Momentum**: instead of raw gradients, use an **exponential moving average (EMA) of gradients** to smooth the optimization path and reduce oscillations.
- **RMSProp**: normalizes the learning rate using the EMA of the **variance** of gradients (root-mean-squared deviation), so the effective step size adapts per-parameter.
- **Adam (Adaptive Momentum)**: combines momentum and RMSProp; the industry-standard optimizer for large neural networks.

### 4. Dropout Regularization
During each mini-batch, a fixed percentage of weights are randomly set to zero. This prevents co-adaptation: every neuron is forced to learn generalizable features rather than relying on specific neighbors. At inference time, retained weights are scaled by the survival probability (e.g., weights × 0.8 when dropout rate is 20%). The effect is mathematically analogous to **L2 / ridge regularization**.

### 5. Batch Normalization
Inputs at each hidden layer are standardized (zero mean, unit variance) within each mini-batch. This prevents variables at very different scales from dominating optimization and keeps activations in a healthy range throughout training. Dropout and batch normalization are typically used as complementary alternatives (usually one or the other per architecture, though exceptions exist).

### 6. Autoencoders — Architecture and Intuition
An **autoencoder** is a neural network trained to reproduce its own input as output. It is structured with **mirror symmetry** around a bottleneck: if the input layer has N neurons, the output layer also has N neurons, and hidden layer sizes decrease then increase symmetrically. The bottleneck layer produces a **lower-dimensional vector representation** of the input — called an **encoding** or **embedding** — which is a compressed, learned representation. The encoder half compresses; the decoder half reconstructs. The entire encoder-decoder stack is trained jointly.

Key insight: if the bottleneck has fewer dimensions than the input, the network is performing **nonlinear dimensionality reduction**. The MNIST example in session demonstrated encoding 784-pixel images into 32-element vectors, then reconstructing visually recognizable digits.

### 7. Encoder-Decoder Composition and Cross-Modal Generation
Encoders and decoders trained independently on different modalities can be **mixed and matched**:
- English encoder + French decoder = machine translation (reported as Google's ~2016 approach)
- Text encoder + image decoder = text-to-image generation
This compositional property is the architectural foundation of **generative AI**: outputs (translated text, images, audio) are *generated*, not retrieved, from learned latent representations.

### 8. Principal Component Analysis (PCA)
PCA is a classical **linear** dimensionality reduction technique. Core procedure:
1. Compute the **covariance matrix** of the input features (N × N for N features).
2. Solve the **eigenvalue problem**: find eigenvectors (principal directions) and eigenvalues (variance along each direction). For an N × N matrix there are exactly N eigenvectors, and they are mutually perpendicular (uncorrelated).
3. Sort eigenvectors by descending eigenvalue (i.e., by variance explained).
4. **Transform** the original data by projecting onto the eigenvectors (matrix multiply: data × eigenvector matrix).
5. Retain only eigenvectors that cumulatively explain a target threshold of variance (e.g., 90%). Drop the rest.

In the wine dataset example (13 chemical features, 178 samples, 3 grape-region classes): 8 of 13 principal components explained >92% of variance. The first two principal components alone yielded visible class separation (Barolo, Grignolino, Barbera) in a 2D scatter plot.

### 9. PCA vs. Autoencoders — The Key Distinction
| Property | PCA | Autoencoder |
|---|---|---|
| Combination type | Linear (weighted sum of original vars) | Nonlinear (weighted sum + activation function) |
| Multicollinearity handling | Yes — eigenvectors are orthogonal | Yes — implicitly through learned representation |
| Interpretability | Low — each PC mixes all features | Low — embeddings are abstract |
| Expressiveness | Limited to linear manifolds | Can capture curved, nonlinear structure |
| Computational approach | Eigenvalue decomposition | Gradient descent |

PCA's trade-off: lose **explainability** (each PC is an uninterpretable linear combination of all features), gain dimensionality reduction. When data lies on a nonlinear manifold, autoencoders outperform PCA because activation functions introduce curvature into the representation space.

---

## Algorithms / Architectures Covered

| Algorithm / Architecture | Category | Key Property |
|---|---|---|
| ReLU activation | Activation function | Solves vanishing gradient; max(0, x) |
| Mini-batch gradient descent | Optimization | Epoch = full dataset traversal via batches |
| Momentum | Optimizer component | EMA of gradients smooths update path |
| RMSProp | Optimizer | Normalizes LR by EMA of gradient variance |
| Adam | Optimizer | Momentum + RMSProp; industry standard |
| Dropout | Regularization | Random weight zeroing per mini-batch; ~ridge penalty |
| Batch normalization | Regularization / stability | Per-layer standardization; prevents scale dominance |
| Autoencoder | Architecture | Mirror-symmetric network; learns compressed encoding |
| Encoder-decoder (cross-modal) | Architecture | Compose encoders/decoders from different domains |
| PCA | Classical dim-reduction | Eigendecomposition of covariance matrix |
| Xavier / Glorot initialization | Weight init | Uniform distribution with range scaled to layer size |

---

## Important Intuitions & Examples

**Dropout as team cross-training**: Rajan compared dropout to removing 20 of 100 staff — the remaining 80 must absorb extra responsibilities, forcing generalization. During inference, weights are re-scaled by the retention probability to maintain expected activation magnitude.

**Batch normalization and scale asymmetry**: A dataset containing body weight (60–110 kg) alongside micronutrient intake (micrograms) would allow the large-scale variable to dominate optimization. Normalizing at every layer gives equal update opportunity to all neurons regardless of input scale.

**Autoencoder as identity network**: "If I gave you the two compressed numbers and sent them back through the decoder, could you reconstruct the original four inputs?" — yes, if the encoder-decoder pair is jointly optimized. The MNIST demonstration (784 → 32 → 784) produced visually recognizable digit reconstructions with some minor quality loss.

**LLMs as regression/classification at the core**: Next-token prediction in LLMs is, at the mathematical level, predicting continuous-valued vector components for the next token — a form of regression in embedding space, not a fundamentally different operation class.

**PCA eigenvalue interpretation**: The wine dataset covariance matrix (13 × 13) yields eigenvalues summing to total variance. Eigenvalue of 5.51 vs. 0.02 immediately signals that the first eigenvector captures ~99.6% of variance in that 2D subspace — the low-eigenvalue direction is discardable.

**PCA limitation — linear only**: PCA identifies straight-line directions of maximum variance. When the data manifold is curved, the optimal directions are curved too — and PCA misses them. Autoencoders handle nonlinear manifolds via activation functions.

**Preview — categorical embeddings**: Next session will cover encoding for categorical variables, extending beyond one-hot encoding to learned dense embeddings, and explore further applications of encoder-decoder architectures.

---

## Related

- [[deep-learning|Deep Learning]]
- [[transfer-learning|Transfer Learning]]
- [[ensemble-methods|Ensemble Methods]]
- [[ai-paradigms|AI Paradigms]]
