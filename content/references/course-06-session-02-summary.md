---
title: "GenAI and Pretrained Models — Session 02: From Tokenization to Transformers"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/llm"]
sources:
  - "_raw/dba-course/Course_06_GenAI_Pretrained_Models/02_Recordings_and_PPTs/session_02/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "A technical walkthrough of how machines learn language, progressing from rule-based NLP and bag-of-words ML through word embeddings (Word2Vec), RNNs, LSTMs, encoder-decoder architectures, and finally the attention mechanism and transformer block that enabled modern LLMs."
---

# GenAI and Pretrained Models — Session 02: From Tokenization to Transformers

**Instructor**: Prof. Anand (GGU)
**Course**: [[course-06-overview-genai-and-pretrained-models|GenAI and Pretrained Models]] (Course 06)
**Session**: 02 of the module — approximately 3 hours
**Resources**: [YouTube Recording](https://www.youtube.com/watch?v=URwbBTEL4NE) | [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/IgCK9-T1FrzdQKukoeIYOUzuAdvAKv2VBbW0i4m-a6AlZYw?e=JIqnzy) | [UpGrad Page](https://learn.upgrad.com/course/8919/segment/64668/397034/1194730/5954594)

---

## Key Concepts

### The Two Layers of GenAI Work
The instructor framed the whole module around a critical distinction: the **model layer** (building foundational models like GPT-3) versus the **application layer** (using those models in products and organizations). Most practitioners will operate at the application layer. The first four sessions cover model-layer internals; from session five onward, the focus shifts to applications, agents, and LLM-ops.

### Why Language Understanding Is Hard
The session opened with an illustrative ambiguous sentence ("At last a computer that understands you like your mother") to demonstrate that language comprehension requires vast world knowledge, emotional context, and cultural background — none of which a machine inherently has. The goal of NLP is to approximate useful understanding without that baggage.

### Rule-Based NLP (Expert Systems Approach)
Early sentiment analysis relied on curated dictionaries of positive/negative words. Engineers applied **tokenization** to reduce vocabulary size: rather than storing every word variant (devastate, devastating, devastation), you store roots plus affixes. The canonical technique is **subword tokenization** — breaking words into meaningful sub-units (e.g., "misunderstanding" → "miss" + "under" + "stand" + "ing"). Modern systems including GPT use subword tokenization for the same reason.

The rule-based approach quickly hits walls: "The meal was not bad" contains the word "bad" (negative) and "not" (negation), but the double-negative rule breaks on "The customer was angry and sad." Rules proliferate without end. Similarly, "The cost exceeded the budget" (negative) vs. "The product exceeded my expectations" (positive) use the same word in opposite sentiment directions — context determines meaning, not word identity alone.

### ML-Based Approach: Bag of Words
The supervised ML solution: take N labeled tweets (human-annotated as positive/negative), create a matrix with one column per vocabulary word (~8,000 columns), and encode each tweet as a binary vector (1 = word present, 0 = absent). A classifier (random forest, XGBoost, etc.) then learns which word co-occurrences signal which sentiment. Limitations: (1) synonyms get separate columns — "cold" and "chilly" are unrelated in this representation; (2) vector dimensionality explodes with proper nouns; (3) no meaning is embedded — just presence/absence.

---

## Models / Architectures

### Word2Vec — Embedding Meaning in Numbers
Google's **Word2Vec** (introduced ~2013–2014) was the pivotal innovation: train a neural network on a large corpus (e.g., Wikipedia or the full web) and, for every word, learn a dense vector of 100–512 real numbers where similar words end up near each other in that high-dimensional space. Google's production representation is **512-dimensional**; modern LLMs use thousands of dimensions.

Key properties demonstrated live:
- Words near "orange" → yellow, red (colors), because orange appears in color contexts.
- Words near "apple" → Microsoft, Google, Samsung (tech companies), because in Wikipedia "Apple" appears next to tech firms.
- Words near "apples" (plural) → fruits, because Wikipedia discusses fruit in plural.
- Words near "Obama" → other US presidents and vice presidents.
- Vector arithmetic: **Paris − France + England ≈ London** (capital-of relationship is encoded). **Paris − France + India ≈ Delhi** (second result: Mumbai as financial capital; third: Bombay, alternate name). **Vishwanathan − India + Russia ≈ Russian chess players** (domain expertise embedded).

The algorithm does not care about character set or spelling — it learns from co-occurrence patterns, so it generalizes to any language (Hindi, Spanish, etc.) trained on its own corpus. The limitation: a word gets **one fixed vector regardless of context** — the word "cell" (phone / prison / biology) has a single embedding, ignoring which sense is active.

The broader principle: converting unstructured data into vector space is a universal technique. Spotify uses song vectors for recommendations; Netflix embeds movies in vector space (discovering that dark sci-fi clusters near dystopian anime); Amazon embeds products similarly. 80% of Netflix watch time originates from vector-based recommendations.

### RNN — Recurrent Neural Networks
To handle sequential language, researchers built **RNNs**, which process one word at a time and maintain a hidden state that carries information forward. At each time step, the current word vector and the previous hidden state are combined through a non-linearity to produce the new state. This gives the network memory — how much of the old state is retained vs. how much the new input dominates is controlled by learned weights.

Problems with RNNs:
1. **Sequential bottleneck**: word N cannot be processed until word N−1 is done. You cannot parallelize training across a long sequence.
2. **Vanishing gradients**: backpropagation through many time steps loses gradient signal — equivalent to whispering a message across 20 people; the message degrades.
3. **Short memory**: in practice, RNNs forget context beyond ~10–15 words.

### LSTM — Long Short-Term Memory
LSTMs added three **gates** (forget gate, input gate, output gate) to the RNN cell to selectively retain or discard information. The gates act like bureaucratic checkpoints: only relevant words update the memory state; sentence boundaries trigger partial forgetting. LSTMs extended useful context to ~100–200 words and powered early translation systems.

Remaining LSTM limitations: still sequential (no parallelism), maximum effective context ~200 words, difficult to train on internet-scale data.

### Encoder-Decoder Architecture
Translation models combined two LSTM stacks: an **encoder** that ingests the source-language sentence word-by-word and compresses it into a context vector, then a **decoder** that reads that context vector and emits one target-language word at a time. This worked for short sentences but degraded as sentence length increased and context compression became lossy.

### Attention Mechanism
Attention was introduced before the transformer paper as an add-on to encoder-decoder LSTM systems — and it improved results. The core idea: rather than compressing an entire sentence into a single context vector, let the decoder look at **all encoder hidden states** and compute a weighted sum that highlights which input words are most relevant for generating each output word.

Intuition: a human in a noisy restaurant can selectively focus on one conversation while filtering out background noise. The attention mechanism gives the model a similar ability — not just sequentially remembering, but dynamically deciding which parts of the input to emphasize for each output step.

Critically, attention addresses Word2Vec's polysemy problem. The sentence "I bought an Apple and an orange" vs. "My Apple phone is laggy" — Word2Vec gives "Apple" the same vector in both. In an attention block, the representation of "Apple" gets attracted toward the "fruit" axis when "orange" is in context, and toward the "tech" axis when "phone" is in context. The attention block is a **matrix multiplication** that operates on all word vectors simultaneously: the learned weight matrix determines how each word's embedding gets pulled toward or away from other words in the same context.

### Transformer Block ("Attention Is All You Need", 2017)
The 2017 Google paper (Vaswani et al.) — now the most-cited paper in all of scientific history — eliminated RNN/LSTM entirely and built models purely from attention plus feed-forward layers.

**Multi-headed attention**: Instead of one attention operation, run multiple attention blocks in parallel. Each head specializes in a different syntactic or semantic relationship:
- One head tracks adjective-noun links (e.g., "red" modifies "fox").
- Another tracks subject-object relationships.
- Another tracks temporal or causal relationships.
- Analogy: like multiple legal departments reviewing the same contract simultaneously, each focused on their specialty (timeline, liability, signatories).

**Transformer block**: Take the word embeddings → pass through multi-headed attention (each head produces a modified set of vectors) → concatenate/sum the outputs → pass through a feed-forward neural network for nonlinear mixing → output is the same number of vectors as input, but now **context-aware**. A word that entered as a generic "fox" vector exits as a "red, athletic fox" vector because the adjective-head wired in "red" and the verb-head picked up "jumps."

Stack six such blocks sequentially (like layers in a deep neural network) and you get the full transformer encoder from the original paper.

**Why it changed everything — economics of scale**:
- The 2017 paper demonstrated 512-token context (5× better than LSTM).
- Because attention processes all tokens simultaneously (one big matrix multiply), **training is massively parallelizable** — you can add GPUs and reduce wall-clock training time proportionally.
- Under LSTM, 100 GPUs still trained sequentially; parallelism was impossible.
- Under transformers, more money = more GPUs = larger context + faster training.
- Result: training on internet-scale data (previously impossible — would take longer than a human lifetime sequentially) became feasible in weeks.
- Today, Gemini's context window is **1 million tokens** — the entire transformer matrix multiplication handles 1M words at one shot, which is why large compute is required.

**Prompt engineering connection**: Because the transformer looks at the entire context window at once, adding role context ("You are a professional writer…") before the task ("clean up this email") changes how every word in the prompt is weighted — the vectors of the task words get modified by the presence of the role instruction. This is the mechanistic reason prompt engineering works.

---

## Important Intuitions and Examples

- **Spell-bee analogy for tokenization**: Elite spellers ask for a word's linguistic origin (Latin, Greek) to deduce spelling from roots and affixes — the same decomposition strategy that subword tokenization uses.
- **Translation failure of rule-based NLP**: "The spirit is willing but the flesh is weak" → Russian → English became "The vodka is good but the meat is rotten" — "spirit" → alcohol (Russian: vodka), "flesh" → meat.
- **Vector arithmetic as proof of semantic validity**: Paris − France + England = London. If the embedding were meaningless random numbers, this arithmetic would not produce the capital city of England. It does, demonstrating that relational human knowledge is encoded in the embedding geometry.
- **Netflix 80% recommendation stat**: 80% of content watched on Netflix originates from vector-similarity recommendations, not user search.
- **Telephone game analogy for RNN degradation**: Information passed sequentially through 20 people (RNN time steps) degrades — by the 20th step the original message is unrecognizable. Backpropagation through a long RNN suffers the same distortion (vanishing gradients).
- **LSTM as bureaucracy**: Three gates = three officials standing at a checkpoint deciding whether each incoming word is allowed to update the state, and whether old state should be forgotten.
- **Context length scaling**: RNN ≈ 10–15 words effective memory → LSTM ≈ 100–200 words → Original transformer ≈ 512 tokens → GPT-4 ≈ 128K tokens → Gemini ≈ 1M tokens.
- **Training data bias caveat**: Word2Vec learns meaning from whatever corpus it was trained on. "Book" for a general model means a novel; for Booking.com it means a hotel reservation. Training data composition shapes all downstream meaning — a key concern for fairness and domain relevance.

---

## Related

[[deep-learning]] | [[transfer-learning]] | [[ai-paradigms]] | [[course-06-overview-genai-and-pretrained-models]]
