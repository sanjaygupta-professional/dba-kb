---
title: "GenAI and Pretrained Models — Session 08: Hardware Architecture, Reasoning Models, and DSPy"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/llm", "#ai/transformers"]
sources:
  - "_raw/dba-course/Course_06_GenAI_Pretrained_Models/02_Recordings_and_PPTs/Session_08/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Covers the GPU/hardware evolution that enabled large-scale AI, the shift to inference-time compute and reasoning models trained via process reward models, and how DSPy formalizes prompt engineering as a software-engineering discipline."
---

# GenAI and Pretrained Models — Session 08: Hardware Architecture, Reasoning Models, and DSPy

**Course**: [[course-06-overview-genai-and-pretrained-models|GenAI and Pretrained Models]] (Course 06)
**Instructor**: Dr. Anand (industry practitioner / course lead)
**Recording**: [YouTube](https://www.youtube.com/watch?v=E00kuZEXgzU)

---

## Key Concepts

### 1. Why GPUs Matter for AI — From Graphics to General Compute

GPUs (Graphical Processing Units) were originally designed to accelerate 3D gaming by rapidly performing **matrix multiplication** — every change of camera perspective in a game is a matrix transformation applied to millions of 3D coordinate points simultaneously. Because deep learning's forward and backward passes decompose naturally into large matrix/tensor operations, GPUs are an ideal fit.

CPUs handle many heterogeneous tasks (memory management, I/O, OS) and are optimized for sequential, high-clock-speed execution. GPUs trade single-thread speed for **thousands of lower-power cores** executing matrix operations in parallel — a key shift from *scalar* computation to *parallel vector* computation.

In the early 2000s researchers in scientific computing (fluid dynamics, chemistry) began exploiting GPU programmability for non-graphics work. This set the stage for deep learning to arrive and find a ready hardware substrate.

### 2. Neural Network Operations Are Natively Matrix Operations

A single hidden-layer neuron computes `Σ(wᵢ · xᵢ) + b`. When you stack all neurons in a layer, the whole layer's computation becomes a **matrix–vector product** `Wx + b`. With mini-batch training (e.g., 32 samples simultaneously), it becomes a **matrix–matrix product**. This is why neural networks are "GPU-native": the hardware was already purpose-built for exactly this arithmetic.

### 3. GPU Architecture and Bandwidth-Limited Workloads

Modern AI workloads are **memory-bandwidth limited**, not clock-speed limited. What matters is how much data can be moved to and from GPU memory per second. Attention mechanisms in transformers (which process entire token sequences at once) are the canonical example: they require keeping large activation matrices in VRAM and are almost entirely bound by memory throughput.

### 4. CUDA, GPGPU, and Nvidia's Dominance

The pivot from fixed-function GPU pipelines to general programmability happened through Nvidia's **CUDA** framework (introduced ~2006). CUDA gave programmers fine-grained control over GPU threads, enabling code that wasn't graphics-related to run natively on the hardware. Other frameworks exist (AMD ROCm, Intel oneAPI) but CUDA's ecosystem lock-in remains dominant.

**TPUs** (Tensor Processing Units, designed by Google) represent the next step: custom silicon that abandons graphics entirely and is purpose-built for tensor arithmetic used in deep learning. Gemini's latest generation is trained entirely on TPUs.

### 5. Neural Scaling Laws and Their Limits

For roughly a decade, empirical *neural scaling laws* showed that model capability grows predictably when compute, data, and parameters are scaled up together. The rule of thumb: doubling compute yields a fixed, sub-linear gain in performance — meaning each increment of improvement requires an **exponentially larger** compute budget. This created unsustainable economics and forced the field to look for new axes of improvement.

### 6. The Inference-Time Compute Axis (System 1 vs. System 2 Thinking)

Daniel Kahneman's *Thinking, Fast and Slow* distinguishes:
- **System 1**: fast, intuitive, low-cost cognition (pattern recognition)
- **System 2**: slow, deliberate, step-by-step reasoning (strategic planning)

Standard LLMs operate as System 1 machines — they produce the next most-probable token immediately without pausing to reason. A TED-talk result from gaming AI research showed that allowing a poker-playing bot just 20 seconds to "think" before acting produced the same performance gain as scaling the model by **100,000×**. This insight introduced the **inference-time compute axis**: giving a fixed trained model more compute at query time to explore solution paths, rather than only scaling at training time.

This is the economic implication behind OpenAI's tiered pricing: the $200/month "deep research" tier is not a smarter model — it is the same model given more time and compute to deliberate before responding. The conceptual shift is from **CapEx-dominated intelligence** (spend billions training once) to **OpEx-allocated intelligence** (spend tokens per query at run time).

### 7. Reasoning Models: Definition and Architecture

A **reasoning model** is operationally defined as: an LLM that **spends compute tokens prior to producing the first word of the user-visible answer**. During that pre-answer phase it:
- Decomposes the problem into sub-steps
- Generates multiple candidate solution paths
- Evaluates and backtracks as needed
- Uses a hidden "scratch-pad" of intermediate tokens not shown to the user

This addresses hallucinations that arise when System-2 tasks (multi-step logic, counting letters in a word) are forced through a System-1 architecture.

### 8. How Reasoning Models Are Trained: Process Reward Models vs. Outcome Reward Models

Standard RLHF uses **outcome reward models (ORM)**: a model generates two answers, a human picks the preferred one, and a reward model learns to predict human preference. Training feedback is attached only to the final output — the reasoning path receives no credit. This is analogous to grading only the final answer on a math exam.

Reasoning models use **process reward models (PRM)**: a separate critic model grades each *intermediate reasoning step*, assigning reward at every step. The analogy is a teacher awarding partial credit for showing work. Training procedure:
1. Take a capable base LLM
2. Prompt it with chain-of-thought instructions to generate step-by-step solutions
3. Use a critic model to assign per-step rewards
4. Apply reinforcement learning (the LLM learns to maximize total step-reward, not just final correctness)

The critic model does not need to be better than the LLM at solving problems — like a coach who can evaluate whether a particular chess move was sound without being able to play as well as the grandmaster.

### 9. Compounding Error Risk in Long Reasoning Chains

Each step in a reasoning chain introduces an error probability. With 95%-accurate steps over 20 steps, overall accuracy is 0.95²⁰ ≈ 35%. Long reasoning chains can **amplify hallucinations** rather than eliminate them. External grounding (RAG, tool calls, verified databases) and human-in-the-loop review remain necessary for high-stakes applications.

### 10. Three Tiers of Reasoning Ability

1. **Implicit reasoning**: Model directly retrieves the answer (System 1 — e.g., "Capital of France?")
2. **Explicit chain-of-thought**: Model is prompted "think step by step" and produces visible steps, reducing errors on medium-complexity tasks
3. **Multi-path search reasoning**: Model generates multiple candidate solutions, evaluates each, backtracks, and synthesizes — what GPT-o1 and similar reasoning models do

### 11. DSPy: Treating Prompt Engineering as Software Engineering

**DSPy** (Declarative Self-improving Language Programs) addresses the enterprise problem of brittle, hand-crafted prompt pipelines. Key pain points it solves:
- Prompts are highly sensitive to phrasing; different engineers write different prompts, producing inconsistent outputs
- When the underlying LLM version changes, prompts that worked for GPT-4 may fail for LLaMA or Gemini
- Multi-step workflows (50+ chained prompts) become spaghetti code where one broken step cascades

DSPy approach:
1. **Declare the task** (input type → output type) rather than hand-write a prompt
2. **Provide labelled examples** (training data)
3. **Run an optimization pass**: DSPy automatically finds the best prompt phrasing for the given model on the given examples
4. When the model changes, re-run optimization — no manual re-prompting

Applied example from the instructor's actual banking project: classifying financial news sentiment (bullish / neutral / bearish) with confidence scores. DSPy was used to build a robust pipeline that automatically adapted its prompt strategy to different LLMs.

### 12. Inference Intelligence vs. Training Intelligence

A key architectural distinction: **training-time intelligence** is fixed in the weights after training ends (CapEx). **Inference-time intelligence** is variable — more compute tokens at query time yield better answers from the same model (OpEx). Modern AI deployment decisions now involve choosing the right balance across a three-dimensional axis: model size, training compute, and inference compute.

---

## Models / Tools Reference

| Name | Type | Notes |
|------|------|-------|
| GPT-o1 | Reasoning LLM | First commercial reasoning model; multi-path search at inference |
| Grok (xAI) | Large LLM | Built rapidly with massive compute investment; competitive but not leading |
| Gemini (Google) | LLM + TPU | Trained entirely on Google TPUs, no Nvidia hardware |
| CUDA | Programming framework | Nvidia's GPU programming platform; dominant ecosystem lock-in |
| TPU | Custom ASIC | Google Tensor Processing Unit; purpose-built for tensor arithmetic |
| DSPy | Python library | Declarative prompt optimization framework from Stanford |
| Nano Banana | Image generation tool | Used by instructor to create infographics with embedded text |

---

## Important Intuitions and Examples

**Matrix = Rotation and Scaling**: A 2×2 matrix applied to vector [1, 0] produces [0.5, −1/3] — the matrix rotated and scaled the vector. Graphics engines perform millions of such transforms per frame to shift camera perspective. This is the exact same arithmetic as a neural network layer.

**CPU as generalist brain, GPU as specialist muscle**: The CPU handles OS, I/O, scheduling — it cannot afford to dedicate all cores to matrix math. The GPU has thousands of simple cores doing exactly one class of operation, in parallel. Offloading matrix arithmetic to GPU frees the CPU and dramatically speeds training.

**Strawberry problem**: LLMs famously fail at counting letters in "strawberry" — a System-2 task (sequential counting) being forced through a System-1 architecture (probabilistic next-token prediction).

**Cricket analogy for retraining**: Training a T20 batter (fast-paced, reward for big shots) doesn't produce a Test-match batter (long-form, reward for patience). You cannot retrofit the skill; you need a player trained differently from the start. Similarly, you cannot fine-tune a standard LLM into a reasoning model by prompt alone — the model must be trained with process rewards from scratch.

---

## Related

- [[deep-learning]] — foundation for GPU acceleration and neural scaling laws
- [[transfer-learning]] — pre-training + fine-tuning paradigm underlying all LLMs
- [[ai-paradigms]] — System 1 vs. System 2 reasoning framing from cognitive science
- [[course-06-session-07-summary]] — previous session on diffusion models and vision transformers
- [[course-06-session-09-summary]] — next session on open-source LLMs and hands-on Groq/Colab lab
