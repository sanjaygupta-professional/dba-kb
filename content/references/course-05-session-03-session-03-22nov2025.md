---
title: "Deep Learning and Variants — Session 03: Backpropagation and Gradient Descent Deep Dive"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/foundations"]
sources:
  - "_raw/dba-course/Course_05_Deep_Learning_and_Variants/02_Recordings_and_PPTs/Session_03_22Nov2025/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Deep mathematical treatment of backpropagation and gradient descent in multi-layer perceptrons, covering notation, chain-rule derivations, weight-update strategies (online, batch, mini-batch), vanishing gradients, and three core challenges of deep networks."
---

# Deep Learning and Variants — Session 03: Backpropagation and Gradient Descent Deep Dive

**Instructor**: Dr. Srinivasa Varadharajan (Rajan)
**Date**: 2025-11-22
**Course**: [[course-05-overview-deep-learning-and-variants|Deep Learning and Variants]] (Course 05)

## Key Concepts

### 1. Perceptron as a Unifying Model
A single perceptron computes a **transfer function** — the sum of bias plus weighted inputs — then passes that through an **activation function**. With an identity activation it replicates [[linear-regression]]; with a sigmoid activation plus a decision threshold it replicates [[logistic-regression]] as a binary classifier. The inputs x1…xn are features of a single data point, not separate data points.

### 2. Multi-Layer Network Notation
Rajan formalised a precise indexing scheme: bias terms use **B^L_k** (superscript = layer number L, subscript = neuron index k within that layer) and weights use **W^L_jk** (superscript = destination layer L, first subscript = destination neuron j, second subscript = source neuron k in layer L-1). Weights form a **matrix** between adjacent layers; biases, activations, and inputs form **vectors**. This notation is essential for tracking gradient flow in large networks.

### 3. Transfer and Activation Functions
The transfer function for neuron j in layer L is:
`Z^L_j = B^L_j + sum_{k=1}^{n^{L-1}} W^L_{jk} * A^{L-1}_k`
The activation A^L_j = sigma(Z^L_j). For the first hidden layer only, the inputs are raw feature values X; for all subsequent layers the inputs are the activations A of the previous layer. The weight matrix between layers is therefore the core learned structure propagating representations forward.

### 4. Cost Function and Learning Objective
Training a neural network means finding values for all weights and biases that minimise a cost function J. Common choices: **sum of squared errors** (regression), **negative log-likelihood / cross-entropy** (classification). The supervised signal is the squared difference (y - y_hat)^2 summed over all training samples. All parameters — every B and W across every layer — are adjusted simultaneously in each update step.

### 5. Gradient Descent
The update rule for any parameter P is: `P_new = P_old - eta * (dJ/dP)`, where eta is the **learning rate** (step size). The gradient dJ/dP is a multi-dimensional vector of partial derivatives. Stopping criteria: gradient approaches zero, change in parameter values falls below a tolerance, or a maximum iteration count is reached. The learning rate is a key hyperparameter controlling convergence speed and stability.

### 6. Backpropagation via Chain Rule
To compute `dJ/dW^L_{jk}`, the chain rule decomposes the derivative into three factors:
`dJ/dW = (dJ/dA) * (dA/dZ) * (dZ/dW)`
- `dJ/dA`: sensitivity of cost to output activation — for MSE this yields (A^L - y)
- `dA/dZ`: derivative of sigmoid: A * (1 - A)
- `dZ/dW_k`: the activation from the previous layer A^{L-1}_k

This product is computed **backwards from the output layer** toward earlier layers. The error term propagated to earlier layers (called lambda in Rajan's notation, delta in standard texts) multiplies exponentially many such factors as depth increases — the root cause of vanishing gradients.

### 7. Weight Update Strategies: Online, Batch, Mini-Batch
Three variants of gradient descent differ in how many data points trigger one weight update:
- **Online (SGD)**: update after each individual sample — fast but noisy, can oscillate around the minimum.
- **Batch**: update after all training samples — stable but computationally expensive per iteration.
- **Mini-batch**: update after a random subset (e.g., 512 samples from 500,000) — the practical standard, balancing stability and speed.

An **epoch** = one complete pass through the full training set. Mini-batch SGD completes many updates per epoch (e.g., ~1,000 mini-batches per epoch for a 500K dataset with batch size 512). Typical training runs span 10–1,000+ epochs depending on dataset complexity.

### 8. Structured vs. Unstructured Data and Network Depth
For **structured (tabular) data**, two hidden layers are theoretically sufficient to approximate any function. A single wide layer can also work but is inefficient. **Deep networks (>2 hidden layers) are warranted for unstructured data** — images, text, audio, video — where hierarchical feature extraction across many layers is needed. For structured data, depth beyond two is rarely necessary; for image classification (e.g., CIFAR-10, MNIST), even a flattened single-layer network can achieve near-zero training error.

### 9. Three Core Challenges of Deep Networks
Rajan identified three fundamental problems that session 4 would address:
1. **Vanishing gradients**: Sigmoid derivatives are always < 0.25 (maximum at midpoint); multiplying dozens of such values during backpropagation drives gradients to near-zero, freezing early-layer weights. Solution: replace sigmoid in hidden layers with non-saturating activations (ReLU family).
2. **Optimisation inefficiency**: Large parameter spaces with many iterations make gradient descent slow. Addressed by advanced optimisers (momentum, Adam, RMSProp — flagged as next-session content).
3. **Overfitting**: With unconstrained depth and width, networks easily memorise training data. Requires regularisation, dropout, or architecture constraints.

### 10. Explainability as an Open Problem
Neural networks are effectively black boxes — individual weight values carry no human-interpretable meaning. Tools like **SHAP** and **LIME** provide approximate, feature-level explanations rather than neuron-level insight. Explainability is critical in regulated domains (insurance, medicine, law, HR) where algorithmic decisions must be auditable. Rajan noted the HR discrimination case — a network that learned systematic bias from biased training data — as a concrete cautionary example.

## Algorithms / Architectures Covered

| Name | Type | Key Detail |
|---|---|---|
| Perceptron | Single neuron | Linear regression (identity activation) or logistic regression (sigmoid + threshold) |
| Fully-Connected Feedforward DNN | Architecture | Every unit in layer L connected to every unit in layer L+1; information flows left to right only |
| Gradient Descent (Batch) | Optimiser | Full dataset per update; stable but expensive |
| Stochastic Gradient Descent (Online) | Optimiser | One sample per update; fast but oscillatory |
| Mini-Batch SGD | Optimiser | Subset per update; practical standard for DNNs |
| Backpropagation | Training algorithm | Chain-rule decomposition of gradients from output to input layer |
| Sigmoid | Activation | Output in (0,1); used only at output layer for classification; avoided in hidden layers due to vanishing gradients |
| ReLU | Activation | Mentioned as solution to vanishing gradients; to be covered in depth next session |

## Important Intuitions & Examples

**Why sigmoid fails in deep hidden layers**: The derivative of sigmoid, A*(1-A), is bounded above by 0.25. In a 10-layer network, backpropagating through 10 sigmoid derivatives produces a factor of at most 0.25^10 ≈ 0.000001 — effectively killing the gradient before it reaches early layers.

**Mini-batch as a middle ground**: With 500,000 training samples and mini-batch size 512, each epoch contains ~977 gradient updates. A model that takes 15 epochs to converge performs ~14,600 weight updates total — fast enough to be practical yet stable enough to converge.

**Neural network as universal approximator**: Any nonlinear function can be represented by a sufficiently wide single hidden layer, or by multiple layers with fewer neurons each. Deep architectures are not theoretically required for structured data — they are practically required for unstructured data where spatial/temporal hierarchy is exploitable.

**Sigmoid of sigmoid nonlinearity**: With two sigmoid layers the activation already becomes `1/(1+exp(-1/(1+exp(-z))))` — analytically intractable, justifying numerical optimisation. Adding more layers compounds this to entirely non-analytical forms.

**Black-box practical stance**: As a practitioner, only the input configuration (number of layers, neurons per layer, activation functions, cost function, optimiser choice) needs to be specified. The software handles all gradient computation and weight updates internally. Inspecting individual weight values post-training is rarely informative.

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=IHBq-ZO2MIo)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/IgAur1wYP0LSTKNFCjcx9J0XAa-qrLNdZU5eEJi51lawFQU?e=fGqzCR)
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/64249/393713/1186251/5913517)

## Related

- [[deep-learning|Deep Learning]]
- [[transfer-learning|Transfer Learning]]
- [[ensemble-methods|Ensemble Methods]]
- [[linear-regression|Linear Regression]]
- [[logistic-regression|Logistic Regression]]
- [[ai-paradigms|AI Paradigms]]
