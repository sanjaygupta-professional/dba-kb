---
title: "Deep Learning and Variants — Session 01: Introduction to Neural Networks and the Perceptron Model"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/foundations"]
sources:
  - "_raw/dba-course/Course_05_Deep_Learning_and_Variants/02_Recordings_and_PPTs/Session_01_15Nov2025/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Rajan introduces the AI/ML/Deep Learning hierarchy, the biological neuron, Hebbian learning, and the perceptron as a mathematical model of a single neuron — laying the conceptual foundation for the rest of the course."
---

# Deep Learning and Variants — Session 01: Introduction to Neural Networks and the Perceptron Model

**Instructor**: [[dr-srinivasa-varadharajan|Dr. Srinivasa Varadharajan (Rajan)]]  
**Date**: 2025-11-15  
**Course**: Deep Learning and Variants (Course 05)

Session 1 is an orientation and conceptual foundation session. Rajan establishes the vocabulary and mental model that will anchor the rest of the course: the hierarchy from Data Science to Machine Learning to Deep Learning to (true) AI, the biology of the neuron, Hebbian learning, and the perceptron as a mathematical neuron. No code, minimal equations — the goal is to build intuition before the mathematics begins in Session 2.

## Key Concepts

- **Data Science as the alphabet of AI** — Rajan defines data science as a "hodgepodge" of statistics, probability, calculus, linear algebra, programming, and domain expertise. It is the prerequisite toolkit, not a discipline in itself.
- **Machine Learning (precise definition)** — A system that determines the relationship between input and output *without being explicitly programmed*. The system is given a model (an idea, e.g. "fit a linear combination") and training data; it adjusts internal parameters until its outputs match desired outputs. Rajan stresses: we are still doing machine learning, not true AI, even with LLMs.
- **Model vs. Model Fit vs. Class of Models** — A *model* is an idea (e.g., "explain y as a linear combination of two variables"). A *model fit* is the specific equation with determined coefficients. A *class of models* (e.g., "regression") encompasses many different model ideas. Conflating these causes conceptual errors.
- **Deep Learning defined** — Machine learning using models built on the architecture of biological neural systems (neurons, synapses, dendrites, axons). Deep learning = neural network learning. The word "deep" specifically means more than two hidden layers between input and output.
- **Artificial Intelligence (Rajan's take)** — A system that can *behave like humans*, not just imitate outputs. Rajan holds that true AI does not yet exist; even systems that pass the Turing Test are doing sophisticated ML. The key barrier: we do not understand what natural intelligence *is*, so we cannot claim to have replicated it artificially.
- **Turing Test** — A test where humans interact with an unknown system; if the humans cannot reliably determine whether they are talking to a machine or a person, the system is considered intelligent. Many modern systems pass some versions, but Rajan is skeptical of the deeper claim.
- **Biological Neuron mechanics** — A neuron has dendrites (input channels), a cell body, and an axon (output channel). Neurons communicate chemically at junctions called *synapses* via neurotransmitters (e.g., dopamine, GABA). A neuron fires when the sum of weighted inputs plus background activity exceeds a threshold. This background activity is always present (called baseline or noise).
- **Hebbian Learning** — The foundational model of how neural networks learn: if a synapse receives repeated strong inputs, its synaptic strength is increased relative to other synapses. "Neurons that fire together, wire together." This strengthening is modeled mathematically as increasing the *weight* of that connection. The human brain applies this by dedicating specialized regions (e.g., the fusiform gyrus for face processing) to frequently encountered stimuli.
- **Synapses as the seat of intelligence** — Neuron count alone does not determine intelligence; synaptic density does. The human brain has ~86 billion neurons but ~1,000 trillion synapses (10^15), meaning ~10,000 connections per neuron on average. LLMs with billions of *parameters* (weights + biases) correspond to far fewer neurons — roughly frog-scale (~10–15 million neurons) — demonstrating how far artificial systems still are from human-scale connectivity.
- **Parameters in LLMs** — Every neuron has (n inputs × 1 weight each) + 1 bias = n+1 parameters. A "10-billion parameter model" with 1,000-dimensional inputs implies roughly 10 million neurons — not 10 billion neurons. Parameters count weights and biases, not neurons.
- **Hyperparameter tuning** — The number of layers and number of neurons per layer are *hyperparameters*, not learned from data. Choosing them is trial-and-error; there is no algorithmic rule. This is why model architecture design remains an art alongside a science.

## Algorithms / Models Covered

| Model / Concept | Type | Key Property |
|---|---|---|
| Perceptron | Single artificial neuron | Weighted linear sum of inputs → activation function → threshold → output |
| Single-Layer Neural Network | Layer of perceptrons | Can solve nonlinear classification; cannot handle complex non-linearity alone |
| Deep Neural Network | Multi-layer perceptron network | More than 2 hidden layers; can approximate any function (Universal Approximation Theorem) |
| Dense (Fully Connected) Network | DNN variant | Every neuron in layer L connects to every neuron in layer L+1 |
| Feed-Forward Neural Network | DNN variant | Information travels only forward (input → output); no feedback loops |
| Recurrent Neural Network (RNN) | DNN variant | Has feedback connections; introduced as a preview for later sessions |
| LSTM (Long Short-Term Memory) | RNN variant | Mentioned as a topic for later in the course |
| Convolutional Neural Network (CNN) | DNN variant | Mentioned as a topic for later in the course |

## Important Intuitions and Examples

- **Child learning cartwheel (YouTube clip)** — Used to illustrate supervised learning. The child's performance improves with each practice attempt. Each attempt = one training iteration; the "desired output" (perfect cartwheel) gives feedback that adjusts the system.
- **Pigeon distinguishing Monet from Chagall** — A classic behavioral experiment demonstrating supervised learning in animals. Pigeons were trained to correctly identify the painter of an unseen painting with ~85% test accuracy. Key insight: the pigeon is not memorizing paintings — it is *generalizing* the painting style. This mirrors what a classification model does.
- **Mouse solving a maze (YouTube clip)** — Used to illustrate unsupervised learning. The mouse is not given explicit directions; it explores and discovers the path to the exit by trial and error. Rajan frames this as clustering: the mouse's brain is segregating "paths that lead out" from "paths that do not lead out."
- **Supermodel analogy for model vs. fit** — A fashion model showcases an idea ("this is how you'll look in this apparel"). Many people can wear the apparel but only the supermodel exemplifies it well. Similarly, many linear combinations are *possible* (the model class), but only one coefficient set fits the data well (the model fit).
- **Face processing and the fusiform gyrus** — Rajan draws on his neuroscience background to explain Hebbian strengthening concretely: because humans encounter faces more than any other pattern, the brain creates a dedicated processing "highway" and region (fusiform face area). Babies can recognize upside-down faces; adults lose that ability because the brain has specialized and optimized for upright faces. This is biological hyperparameter tuning — the brain chose the architecture that works best for the most frequent task.
- **Circuit analogy for neural networks** — Understanding deep networks requires first understanding a single neuron, just as understanding an electronic circuit requires understanding resistors and capacitors first. The neuron is the only component type in a neural network; a deep network is what you get when you wire thousands of them together in a structured way.
- **Activation function selects the task** — A single perceptron can perform either regression (linear activation function) or classification (sigmoid/logistic activation function) just by swapping the activation function. This is one of the most powerful properties of the neuron-based model.

## Related

- [[dr-srinivasa-varadharajan|Dr. Srinivasa Varadharajan (Rajan)]]
- [[deep-learning|Deep Learning]]
- [[logistic-regression|Logistic Regression]] — sigmoid function = activation function used in classification perceptrons
- [[linear-regression|Linear Regression]] — linear activation function in perceptrons enables regression
- [[transfer-learning|Transfer Learning]] — mentioned as a future topic; enabled by deep network architecture
- [[decision-trees|Decision Trees]] — contrasted with neural networks in terms of explainability
- [[ensemble-methods|Ensemble Methods]] — referenced as prior-course supervised learning methods
- [[clustering|Clustering]] — mouse maze example reframed as an unsupervised clustering problem
- [[association-rule-mining|Association Rule Mining]] — mentioned as prior-course unsupervised learning method
- [[ai-paradigms|AI Paradigms]] — Rajan's hierarchy: Data Science → ML → Deep Learning → (true) AI
