---
title: "GenAI and Pretrained Models — Session 03: Transformer Architectures, Pretrained Models, and the RLHF Pipeline"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/llm", "#ai/transformers"]
sources:
  - "_raw/dba-course/Course_06_GenAI_Pretrained_Models/02_Recordings_and_PPTs/Session_03/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "A technically dense walkthrough of the full Transformer encoder-decoder architecture, the three families of LLM designs (encoder-only BERT, decoder-only GPT, encoder-decoder), BERT's masked language model and next sentence prediction pretraining tasks, the supervised fine-tuning and RLHF pipeline that produced ChatGPT, and the neural scaling laws that drove the brute-force era of LLM growth."
---

# GenAI and Pretrained Models — Session 03: Transformer Architectures, Pretrained Models, and the RLHF Pipeline

**Instructor**: Professor (Physics PhD; previously contributed to DL curriculum including CNN/transfer-learning modules)
**Course**: [[course-06-overview-genai-and-pretrained-models|GenAI and Pretrained Models]] (Course 06)
**Session date**: *not recorded in transcript*
**Recording**: [YouTube](https://www.youtube.com/watch?v=t53r2vaP61c)

---

## Key Concepts

### Transformer Block Recap (from Session 02)
The session opened by consolidating what was established in the previous lecture. A single **transformer block** consists of:

1. **Input embedding** — raw words converted to dense vectors (e.g., Word2Vec-style embeddings). At this stage the vector is context-free; "cat" gets a generic representation regardless of whether the sentence is about an animal or Caterpillar Inc. stock.
2. **Positional encoding** — a positional signal is added to each embedding so the model knows word order (1st, 2nd, 50th word, etc.).
3. **Multi-head attention** — the core linear operation. Multiple attention heads look at *all* words simultaneously, each head learning to attend to different aspects (subject/object relationships, verb–adverb pairs, etc.). The weights are learned, not hand-crafted; the "verbs" or "nouns" framing is a pedagogical approximation.
4. **Feed-forward network** — a non-linear layer that sits after the attention step and adds expressive capacity. Output: the same number of vectors as input, but now **context-rich** (each vector encodes the word in context of the whole sentence).

Multiple transformer blocks are stacked (the original "Attention Is All You Need" paper used 6; GPT variants may use 25+). Each additional layer extracts higher-order patterns, analogous to hierarchical feature extraction in CNNs.

### Encoder–Decoder Architecture
The full transformer from the 2017 paper is an **encoder–decoder** system:

- **Encoder** — ingests the entire input sentence in one shot and produces context-rich vectors. A 600-word question is processed *once*, all in parallel (no sequential bottleneck). The output is a compressed representation of the full input meaning.
- **Decoder** — takes those encoder vectors and generates output tokens **autoregressively** (one token at a time). After each predicted token, that token is fed back as additional input to condition the next prediction. The decoder performs **multi-class classification** over the full vocabulary at every step: if the vocabulary is 10,000 words, 10,002 output logits are produced (10,000 words + sentence-end token + answer-end token). The highest-probability class is selected as the next word. Generation halts when the answer-end token achieves the highest probability.

Key insight: the encoder's work is a **one-time parallel operation**; the iterative cost lives entirely in the decoder. Unlike RNNs/LSTMs (which processed sequentially and could not be parallelized), transformer attention can be distributed across many GPUs, making the architecture economically scalable.

### Masked Multi-Head Attention (in decoder)
During *training*, the decoder uses **masked** multi-head attention to prevent it from "seeing the future" — it can only attend to tokens generated so far. This is primarily a training-time construct enabling teacher forcing; at inference the model generates left-to-right anyway.

### Three Families of Transformer Models
| Architecture | Example | Primary Strength |
|---|---|---|
| Encoder-only | BERT (Google, 2018) | Classification, understanding, embedding |
| Decoder-only | GPT series (OpenAI) | Text generation, completion |
| Encoder–decoder | Original transformer, T5 | Translation, seq2seq tasks |

### Emergent Phenomena and the LLM Motivation
The instructor drew an analogy from **condensed matter physics** — specifically the Ising model and phase transitions: in a 1D or 2D world, no phase transition (discontinuous jump in properties, e.g., solid→liquid) exists. It only emerges in 3D. This is a canonical example of **emergent phenomena**: qualitative new behavior that arises only at sufficient scale and does not exist at smaller scale.

Neural networks exhibited the same property. Smaller models improved gradually on language tasks but showed no sign of approaching human-level understanding. The transformer architecture was the first to show that *with scale*, emergent linguistic competence could appear. This insight, combined with the transformer architecture, drove the "large language model" era — **LLM = transformer architecture + massive parameters + massive training data**.

---

## Models and Architectures

### BERT — Bidirectional Encoder Representations from Transformers (Google, 2018)
- **Architecture**: Encoder-only. No decoder; no text generation.
- **Context window**: 512 tokens (vs. ~100 for RNNs/LSTMs of that era).
- **Parameters**: ~110–340 million (BERT-Base / BERT-Large). At announcement, this felt enormous; today a "small language model" has ~3B parameters.
- **Training compute**: 16 Google TPU chips, 4 days, ~$500 in compute — a historical benchmark that highlights how costs have since exploded by many orders of magnitude.
- **Training data**: 800 million words, primarily from the **Google Books Project** corpus (Google's massive book-scanning effort).
- **Naming note**: "Bidirectional" is technically a misnomer — transformers already process all positions simultaneously. Google used the term to convey parity with older bidirectional RNN approaches (which ran one pass left-to-right and one right-to-left then combined them). The transformer does this holistically.
- **Why it was landmark**: (1) Contextual word understanding — "cat" in a financial report vs. a nature documentary got different vectors. (2) Released **open-source as a pretrained model**, enabling transfer learning at scale.

#### BERT Pretraining Tasks
Two fake supervised tasks trained on the books corpus, generating enormous training examples without human labeling:

1. **Masked Language Model (MLM)**: Randomly mask ~15% of tokens in a sentence; train the network to predict the masked tokens. From a single sentence, hundreds of distinct masked examples can be generated. Forces the model to understand context from both sides of a gap — analogous to fill-in-the-blank tasks humans do intuitively.

2. **Next Sentence Prediction (NSP)**: Given sentence A and sentence B, classify whether B follows A in the original text (label = 1) or is randomly drawn from an unrelated passage (label = 0). Teaches logical coherence across sentences.

Both tasks together make BERT an excellent general language representation model. After pretraining, downstream users freeze the encoder and fine-tune only a lightweight classifier head on their specific task (sentiment, spam detection, QA), training only thousands of parameters instead of millions — achievable on commodity hardware.

### GPT Series — Generative Pretrained Transformer (OpenAI, 2018–present)
- **Architecture**: Decoder-only.
- **Pretraining task**: Next-token prediction — given the first N words of a sentence, predict word N+1. Training examples are naturally generated by sliding a window over the corpus.
- **Evolution in scale**:
  - GPT-1: 117 million parameters
  - GPT-2: ~1.5 billion parameters
  - GPT-3: 175 billion parameters (first to capture mass attention)
  - Current models: Trillions of parameters; training costs far beyond $10M (Sam Altman explicitly dismissed $10M as insufficient to build a frontier LLM when speaking to Indian VCs)

---

## Important Intuitions and Examples

### From Language Model to ChatGPT: The Three-Stage Pipeline

**Stage 1 — Unsupervised Pretraining**
Train on internet-scale text using self-supervised tasks (masked LM, next token prediction). The model becomes a powerful next-token predictor but has no concept of Q&A structure. If asked "What is the capital of India?" it may respond with "What is the capital of France? What is the capital of Brazil?" — continuing the rhetorical pattern it has seen in text, not answering the question.

**Stage 2 — Supervised Fine-Tuning (SFT)**
Human contractors write ~10,000–15,000 (prompt, ideal response) pairs. These are used to directly fine-tune the model, teaching it that a question expects a direct answer, not a continuation. SFT guarantees grammatically correct, appropriately structured responses, but cannot guarantee *human-preferred* responses. A technically correct answer can still be too vague, too technical, or inappropriate in register.

**Stage 3 — Reinforcement Learning from Human Feedback (RLHF)**

The key OpenAI innovation that made ChatGPT feel magical:

1. Use the SFT model to generate multiple candidate responses to the same prompt (e.g., 4 responses).
2. Present pairs of responses to human raters; ask "which do you prefer?" (pairwise comparison proved more reliable than ranking 4 options simultaneously — cognitive science insight).
3. Train a separate **Reward Model** (RM) — a standard ML classifier — to predict human preference given (prompt, response-A, response-B). This RM encapsulates human taste at scale.
4. Use the RM as an automatic reward signal inside a reinforcement learning loop. The LLM generates responses; the RM scores them; the LLM's weights are updated via **Proximal Policy Optimization (PPO)** to produce more human-preferred outputs.

**PPO intuition**: The LLM before RLHF is already capable. PPO makes *gentle, proximal* adjustments to the existing weight distribution — it doesn't relearn from scratch, it nudges the policy toward the reward signal while staying close to the pretrained weights.

**Scaling the reward signal**: Once the RM is trained, human raters are no longer needed continuously. The loop runs automatically at scale. Human feedback is only periodically re-collected to refresh the RM. This is why ChatGPT surfaces "which response do you prefer?" prompts to users — crowd-sourced updates to the RM.

**DeepSeek note** (mentioned at session close): DeepSeek dramatically cut training cost by skipping SFT and using RL directly from the base model, demonstrating that engineering choices around the pipeline can yield equivalent quality at lower cost — though large parameter counts remain necessary for quality.

### Neural Scaling Laws (OpenAI, 2020 paper)
Three axes independently reduce model error as a power law:
- **Compute** (FLOP-seconds of training)
- **Model size** (parameter count)
- **Dataset size** (token count)

This produced the "compute-optimal frontier" — a boundary that no model can cross, but moving along the frontier (scaling any of the three axes) reliably lowers error. The laws hold regardless of specific architectural choices, as long as the architecture is reasonable.

**Implication**: For ~4 years, companies did not need new research ideas — they just needed capital. Larger model + more data + more compute = guaranteed performance improvement. This predictability de-risked AI investment and triggered the current VC frenzy.

**Current state (instructor's view, ~2026)**: The scaling-law era is reaching its limits. Internet-scale training data has been largely exhausted. Future improvement will likely require genuine architectural innovation, not just brute-force scaling. DeepSeek's efficiency gains and new training paradigms are early signals of this next phase.

### Transfer Learning in Language (the BERT Breakthrough)
Prior to BERT, every company needing an NLP model had to train from scratch — requiring enormous compute and expertise. BERT replicated the transfer learning paradigm already standard in computer vision (e.g., pretrain AlexNet on ImageNet → freeze conv layers → retrain final FC layers for X-ray fracture detection) and applied it to language for the first time at commercial scale. Google released BERT's pretrained weights openly, enabling enterprises to fine-tune only the final classifier head on domain-specific data using ordinary hardware.

---

## Related

- [[deep-learning]] — CNN analogy for hierarchical feature extraction; backpropagation as the universal training mechanism across all neural architectures
- [[transfer-learning]] — the BERT-to-downstream-task fine-tuning paradigm; frozen encoder + lightweight task head
- [[ai-paradigms]] — unsupervised pretraining → supervised fine-tuning → RLHF as the three-stage pipeline behind instruction-following LLMs; emergent phenomena as the physics-grounded motivation for scale
