---
title: "Deep Learning and Variants — Session 02: Multi-Layer Perceptron"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/dl"]
sources:
  - "_raw/dba-course/Course_05_Deep_Learning_and_Variants/02_Recordings_and_PPTs/Session_02_16Nov2025/20251116_DL_C8S1_Multi-Layer-Perceptron.extracted.txt"
created: 2026-04-12
updated: 2026-04-12
summary: "MLP architecture: perceptron model, bias, activation functions, forward pass, backpropagation, and gradient descent."
---

# Deep Learning and Variants — Session 02: Multi-Layer Perceptron

**Instructor**: [[dr-srinivasa-varadharajan|Dr. Srinivasa Varadharajan (Rajan)]]  
**Date**: 2025-11-16

Builds up from the single-neuron perceptron to the full MLP. Core topics: neuron model, bias, activation functions, the forward and backward passes.

## Neuron Model (Perceptron)

A perceptron computes: `output = f(w₁x₁ + w₂x₂ + ... + wₙxₙ + bias)`

Where:
- **wᵢ** = synaptic weights (learned)
- **xᵢ** = inputs
- **bias** = background neural activity; shifts the activation threshold; treated as an always-on input with weight w₀

**Hebbian Learning**: "Inputs that consistently result in output strengthen the associated synapse." Weights for inputs correlated with output increase selectively.

## Key Architectural Concepts

- **Activation Function** — non-linear transformation applied after summation; includes threshold information
  - Step / sigmoid / ReLU / tanh — each shapes the output range and gradient behavior
- **Layers**: Input → one or more Hidden layers → Output
- **Depth** = number of hidden layers; "deep" network has ≥2 hidden layers
- **Width** = number of neurons per layer; controls representational capacity

## Learning (Backpropagation)

Forward pass: compute predictions layer by layer.  
Loss function: measures error between prediction and ground truth (MSE for regression, cross-entropy for classification).  
Backward pass: compute gradient of loss w.r.t. each weight via chain rule; update weights via gradient descent.

**Gradient Descent variants**:
- Batch GD: uses all data; stable but slow
- Stochastic GD (SGD): one sample at a time; noisy but fast
- Mini-batch GD: compromise; most practical

## Related

- [[dr-srinivasa-varadharajan|Dr. Srinivasa Varadharajan]]
- [[course-05-session-01-20251115-dl-c8s1-introduction|Session 01: DL Introduction]]
- [[course-05-session-02-session-02-16nov2025|Session 02 Notes]]
- [[deep-learning|Deep Learning]]
