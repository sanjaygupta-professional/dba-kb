---
title: "GenAI and Pretrained Models — Session 04: LLM Inference Parameters, Prompt Engineering, and Evaluation Metrics"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/llm", "#ai/transformers"]
sources:
  - "_raw/dba-course/Course_06_GenAI_Pretrained_Models/02_Recordings_and_PPTs/Session_04/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Covers the user-facing side of LLM interaction — inference parameters (temperature, top-k, max tokens), the OpenAI API call structure with system/user/assistant roles, stateless API design and prompt chaining for memory, zero-shot and few-shot prompting strategies, chain-of-thought reasoning, and a three-tier framework for evaluating LLM outputs (traditional BLEU/ROUGE, LLM-specific metrics, enterprise ROI metrics)."
---

# GenAI and Pretrained Models — Session 04: LLM Inference Parameters, Prompt Engineering, and Evaluation Metrics

**Course**: [[course-06-overview-genai-and-pretrained-models|GenAI and Pretrained Models]] (Course 06)
**Instructor**: Dr. Anand (referred to as "Professor" / "Doctor" throughout)
**Recording**: [YouTube](https://www.youtube.com/watch?v=MaGIIepXZDg)
**Date**: Session recorded (exact date not stated in transcript)

---

## Key Concepts

### 1. LLM as a Probability Prediction Engine

The foundational mental model introduced in this session is that an LLM is not a lookup table — it is a **probability distribution engine**. At every generation step the model outputs a probability for every token in its vocabulary (often 10,000+ tokens). A separate **sampling algorithm** then chooses which token to actually emit. This distinction — model output vs. sampling policy — is critical for understanding all the tuning parameters discussed below.

### 2. Inference Sampling Parameters

Three parameters govern how a token is selected from the model's probability distribution, and all three are settable at API call time:

- **Temperature** (range 0–1, sometimes higher):
  - Inspired by statistical mechanics: at absolute zero (T=0), all atoms are motionless — analogously temperature=0 forces the model to always select the single highest-probability token (fully deterministic, identical outputs on every call).
  - Higher temperature widens the effective probability distribution, allowing lower-probability tokens to be selected. This produces more creative, varied, and human-like text.
  - Practical rule: use near-zero for factual/scientific queries; use 0.7–1.0 for creative writing, brainstorming, or poetry.
  - Temperature is also what gives LLMs their human-like quality — a person asked the same question twice will rarely use the exact same words.

- **Top-k Sampling**: Instead of sampling across the full vocabulary, restrict selection to only the top-k most probable tokens, then sample probabilistically among those k. This constrains creativity while still introducing variation.

- **Max Tokens** (output token limit):
  - This is **not** part of the prompt text; it is a separate API-level parameter.
  - The LLM will truncate its output when the limit is hit, even mid-sentence.
  - Enterprise importance: output tokens are billed at a much higher rate than input tokens (example given: GPT-5.2 input tokens cost ~$1.7/million; output tokens cost ~$14/million — roughly a 7–8x difference). Setting max_tokens is a direct cost-control lever.

### 3. API Call Structure: System, User, and Assistant Roles

When building enterprise applications, one interacts with LLMs through API calls (not the chat UI). The OpenAI API exposes three structured roles in the `messages` list:

| Role | Who controls it | Purpose |
|---|---|---|
| **system** | Application developer | Master instruction — sets tone, persona, domain restrictions, governance rules |
| **user** | End user | The actual question or request |
| **assistant** | LLM (read-back) | The model's previous response; used for context chaining |

The **system prompt is the enterprise governance lever**: the developer controls it completely, the end user never sees or modifies it. It is where you enforce polite tone, domain scope (e.g., "only answer tax-related questions"), content restrictions, output format requirements, and cost-limiting instructions.

Key code example shown (using `litellm` and then native `openai` libraries in Python):
- Model selection: `gpt-4-mini` for cost efficiency
- System role: `"You are a professional tax advisor. Answer concisely and accurately."`
- Temperature: `0.2` (low, for factual domain)
- Max_tokens: `200` (hard cap on output cost)

### 4. Stateless APIs and Prompt Chaining (Conversational Memory)

**LLM API calls are stateless by design**: each call is independent; the model has no memory of prior turns. This is deliberate — in a multi-user enterprise environment, you do not want one user's queries influencing another user's session.

The illusion of a multi-turn conversation (as seen in ChatGPT) is achieved by the **application layer**, not the model:

1. Each user message is appended to a `messages` list.
2. Each model response is saved back into the list under the `assistant` role.
3. On every subsequent call, the **entire message history** is resent to the API.

This creates **prompt chaining** / **chain of context**. Implications:
- Token costs grow linearly with conversation length (the full history is re-sent every turn).
- Very long conversations eventually exceed the model's **context window** and earlier messages are dropped, causing the model to "forget" prior context.
- ChatGPT's memory feature (available to paid users) implements a separate summarization loop: after each conversation, a background process compresses key facts about the user into a persistent memory store, which is injected at the start of new sessions. This is a **vendor-side context compression** strategy, not native model memory.
- Claude Code (mentioned explicitly) shows users a visible context-compression notification when the window fills and then replaces the raw history with a compressed summary.

### 5. Prompting Strategies

**Zero-shot inference**: Provide a task instruction with no examples. The model applies its pre-trained knowledge to respond. Suitable when the task type is general and well-represented in training data.

**Few-shot (multi-shot) inference**: Include labeled examples (input/output pairs) inside the system or user prompt before the actual query. This is essential when:
- The output format must be highly constrained (e.g., only return a raw SQL query, no prose).
- The downstream system consuming the output cannot handle natural language.
- The task is domain-specific or the desired response style differs from the model's default.

The instructor's analogy: giving the model example "question → answer" pairs in the prompt is equivalent to showing a new employee sample work before assigning them a task.

**Chain-of-thought (CoT) prompting**: Instead of asking the model for a direct answer, instruct it to articulate intermediate reasoning steps ("Think through this step by step"). This has been shown to dramatically improve accuracy on multi-step logical and mathematical problems. The famous illustration: directly asking how many letters 'r' appear in "strawberry" often produces wrong answers; asking the model to count letter by letter dramatically improves accuracy. CoT was also a key conceptual precursor to the development of **reasoning LLMs** (covered in a later session).

**DSPY** (briefly mentioned): A Python library that inverts the prompting problem — instead of a human crafting prompts manually, the developer declares the intent/signature and DSPY automatically optimizes the prompt using the LLM itself as a prompt-generation engine. Positioned as a path toward reproducible, programmatic prompt engineering rather than artisanal one-off prompts.

---

## Models / Architectures

This session is not primarily about model architecture, but the following models were referenced:

- **GPT-3.5 Turbo / GPT-4 Mini**: Used in code examples for API calls; positioned as the cost-efficient tier for production enterprise applications.
- **GPT-4 / GPT-5.2**: Used as the evaluation "judge" LLM (expensive, used periodically to assess cheaper model's outputs, not for daily-use production traffic).
- **BERT**: Referenced as the underlying architecture for toxicity classifiers (fine-tuned on toxic comment datasets using BERT + logistic regression).
- **Claude (Anthropic)**: Noted as the current preferred model the instructor would choose if designing slides from scratch; highlighted as dramatically disrupting the coding-assistant market.
- **Gemini**: Mentioned in context of context transfer challenges when switching between LLM providers.
- **DeepSeek**: Briefly referenced — removed supervised fine-tuning (SFT) entirely and trained directly with RLHF, making training cheaper; will be discussed more in the future-trends lecture.

---

## Important Intuitions and Examples

### The Klarna Case Study (Business Outcome Metrics in Practice)
Klarna deployed an OpenAI-powered assistant handling 2.3 million customer service conversations — representing two-thirds of their total customer service chat volume. The announcement, framed as an investor communication, cited the system as doing the equivalent work of 700 full-time agents and estimated a $40M profit contribution. The instructor noted the subtext: the announcement effectively signaled a large-scale workforce reduction. This illustrates how LLM ROI metrics at the enterprise level translate directly to headcount economics.

### Why Output Tokens Are Billed Differently from Input Tokens
The transformer encoder reads the entire input in a single forward pass (parallel computation). Output generation is autoregressive — the model runs a **full forward pass per output token**. Producing 200 output tokens means running the network 200 times. This explains the 7–8x cost differential between input and output tokens and why max_tokens is a cost-critical parameter, not a formatting afterthought.

### The Hallucination Risk Calculus
If an LLM provider guarantees only 1% hallucination rate and an enterprise chatbot receives 10,000 queries/day, 100 potentially wrong answers are produced daily. At scale, even a low hallucination rate translates to measurable lawsuit exposure, reputational damage, or cascading operational failures. A real example cited: a law firm was fined by a judge after submitting a brief in which LLM-generated citations referenced fabricated case law.

### Traditional Metrics Are Inadequate for Modern LLMs
**BLEU** (Bilingual Evaluation Understudy, precision-focused) and **ROUGE** (recall-focused) count exact word overlaps between generated text and a human reference. Both fail for modern LLM evaluation for two reasons:
1. Semantically identical answers using different vocabulary score near zero ("the weather is hot" vs. "the climate is uncomfortably warm").
2. Factually wrong text that happens to match reference words (e.g., memorized-sounding nonsense) scores perfectly.

### LLM-as-a-Judge for Hallucination Measurement
To assess factual accuracy and hallucination rate without human reviewers:
1. Maintain a **golden set** — a curated corpus of ground-truth question/answer pairs.
2. Run the production LLM (cheaper) against the golden set periodically.
3. Feed the production LLM's answers and the golden answers to a **more capable judge LLM** (e.g., GPT-4) which scores semantic equivalence — not word matching.
4. Hallucination rate = percentage of outputs unsupported by context/ground truth.

The judge LLM is used infrequently (batch evaluation), not on every production call, keeping costs manageable.

### Toxicity Measurement via `langfair`
The `langfair` Python library wraps a BERT-based toxic comment classifier. The evaluation workflow: send the same prompt to the LLM 25 times (to sample the output distribution), score each response for toxicity using the classifier, and compute the probability of toxic response and maximum expected toxicity across the distribution. This probabilistic approach accounts for the stochastic nature of LLM outputs.

---

## Three-Tier Evaluation Framework

| Tier | Metrics | Measured by | Purpose |
|---|---|---|---|
| **Traditional** | BLEU, ROUGE | Rule-based word overlap | Adequate only for pre-LLM NLP (translation, summarization circa LSTM era) |
| **LLM-specific** | Factual accuracy, hallucination rate, bias/fairness score, toxicity score, helpfulness | LLM-as-a-judge, specialized classifiers (e.g., BERT-based toxicity models via `langfair`) | Verify the model actually works correctly and safely |
| **Enterprise / Business** | Cost per query, latency (time to first token), throughput, cost per resolved issue, ROI vs. baseline, customer satisfaction, call deflection rate | Business analytics, API billing dashboards | Justify deployment, track operational impact, compare vs. traditional solutions |

---

## Related

- [[deep-learning]]
- [[transfer-learning]]
- [[ai-paradigms]]
- [[course-06-overview-genai-and-pretrained-models|GenAI and Pretrained Models — Course Overview]]
