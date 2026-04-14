---
title: "GenAI and Pretrained Models — Session 01: Introduction to Generative AI — Landscape, Concepts, and Enterprise Adoption"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/llm"]
sources:
  - "_raw/dba-course/Course_06_GenAI_Pretrained_Models/02_Recordings_and_PPTs/session_01/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Introductory session covering the definition and taxonomy of generative AI, the Gartner hype cycle applied to AI, the discriminative vs. generative model distinction, the three-tier enterprise access model, LLM limitations, and a broad survey of industry use cases."
---

# GenAI and Pretrained Models — Session 01: Introduction to Generative AI

**Instructor**: Prof. Anand Raman (Chief Scientist, Suites Analytics; Program Co-founder)
**Date**: Session 1 of 10 (January, ~2026)
**Course**: [[course-06-overview-genai-and-pretrained-models|GenAI and Pretrained Models]] (Course 06)

---

## Key Concepts

### 1. Discriminative vs. Generative Models
All prior ML coursework (ML and Deep Learning modules) focused on **discriminative models** — those that learn the conditional probability P(Y | X) to make decisions: classify loan applicants, predict stock direction, estimate customer lifetime value. Examples include SVM, logistic regression, CNN, and LSTM. These models are relatively simple to train, targeted at a specific task, but cannot create new data.

**Generative models**, by contrast, learn the full joint probability distribution P(X, Y) or the marginal P(X) over the data. Because they model the whole distribution, they can **generate new samples** that resemble the training corpus. They excel at unsupervised learning, require far more data, and are substantially more complex to train. Generative AI is defined as the application of generative models to produce novel content — text, images, audio, video — at scale.

### 2. The AI Taxonomy (Field → ML → Deep Learning → GenAI → LLMs)
AI is a broad field of study dating from the 1956 Dartmouth Conference, where three paradigms were articulated:
- **Rules-based AI**: Explicit human-coded rules + input data → decision. Encompasses expert systems and RPA. Dominated through the 1970s–80s.
- **Machine Learning**: Data + labeled outcomes → automatically derived rules/model. The human specifies features; the algorithm finds patterns.
- **Deep Learning**: Raw data → automatic feature extraction → model. The critical innovation is end-to-end feature learning without human feature engineering.
- **Generative AI**: A subdomain of deep learning where the model learns from a large corpus and can synthesize new content from the learned distribution.
- **Large Language Models (LLMs)**: A specific class of generative models trained on text. ChatGPT, Gemini, Claude, and Llama are instances. LLMs are themselves a sub-slice of generative AI, which is a sub-slice of deep learning, which is a sub-slice of ML, which is a sub-slice of AI.

### 3. The Gartner Hype Cycle Applied to AI
The hype cycle (technology trigger → peak of inflated expectations → trough of disillusionment → slope of enlightenment → plateau of productivity) describes societal behavioral patterns around new technology, not a law of nature. Key examples discussed:
- **1970s–80s neural networks**: Universal Approximation Theorem created massive excitement (any complex function can be approximated by a single-hidden-layer network). Finance firms hired computer scientists to predict markets using neural networks; nearly all failed due to insufficient data and compute. Neural networks entered the trough — the word itself became toxic to investors.
- **2000 dot-com bubble**: Identical pattern. Companies received funding purely for having ".com" in their name; revenue reality caused the crash.
- **2018 Gartner cycle**: Deep learning was at the peak of inflated expectations; blockchain also near peak; AGI still early.
- **2025 Gartner cycle**: AI agents at the peak; foundation models on the downward slope; generative AI itself already trending toward trough. Google Trends data for "generative AI" searches shows a declining curve over 2024–2025 — consistent with movement into disillusionment.

Key statistic: An MIT study (2025) found **95% of generative AI pilots are failing**. A 2021 Gartner study found 87% of AI/ML projects broadly do not become profitable. The instructor's real-world anecdote: a Big Four auto manufacturer ran over 150 AI pilots across the company with no meaningful integration or value creation, and hired the instructor's firm specifically to develop a coherent strategy.

### 4. LLMs as Next-Word Prediction Engines
LLMs are fundamentally **next-token prediction engines**: given a sequence of text, the model assigns a probability distribution over the vocabulary and selects the most probable next token — recursively. This produces fluent, coherent text that can appear authoritative. The instructor used a neuroscience framing: the language region of the human brain is anatomically separate from the reasoning/thinking region. LLMs model only the language region — they produce plausible language, not verified reasoning.

This architecture directly explains two major failure modes:
- **Hallucinations**: The model generates statistically plausible but factually incorrect content — fake citations, nonexistent software features, fabricated statistics.
- **Bias and toxicity**: Training corpora (e.g., Reddit) contain unfiltered human biases — racist, sexist, and harmful content. The model absorbs and reproduces these biases. Microsoft's public chatbot (Tay) was taken down within 24 hours of release for this reason.

### 5. Historical Milestones Toward LLMs
- **1956**: Dartmouth Conference — birth of AI as a field.
- **1958**: Perceptron (first neural network formalization).
- **1961**: ELIZA — first chatbot; strictly rule-based, but convincing enough that the creator's secretary believed it had genuine intelligence.
- **1966**: Hidden Markov Models — foundational for language understanding.
- **1985**: Backpropagation becomes practical — neural network revival; hedge funds start using NNs for trading.
- **1997**: LSTM introduced — critical for sequence/language tasks.
- **2012**: AlexNet / CNN revolution — deep learning for images.
- **2013**: Word2Vec — distributed word embeddings; GANs introduced.
- **2017**: Transformer architecture ("Attention Is All You Need" paper).
- **2018**: BERT (bidirectional transformers, Google) and GPT-1 (OpenAI) — marquee year for language understanding.
- **Present**: GPT-5, Llama 3, Gemini, Claude — large foundation models. Average model stays at the top of leaderboards for approximately 20 days before being surpassed (down from ~60 days a year prior).

### 6. The Three-Tier Enterprise Access Model
Enterprise adoption of generative AI falls into three tiers based on data control, cost, and capability requirements:

| Tier | Description | Data Risk | Cost | Use Case |
|------|-------------|-----------|------|----------|
| 1 | Web interface (ChatGPT, Gemini, Claude chat) | High — shadow IT; data sent to public LLM | Low (subscription) | Individual productivity |
| 2 | API access to proprietary LLMs (OpenAI API, Azure OpenAI, Vertex AI) | Medium — data leaves org but not used for training per ToS | Medium — pay-per-token | Enterprise chatbots, RAG, internal tools |
| 3 | Self-hosted / fine-tuned open-weight LLMs (Llama on private cloud or on-prem) | Low — data never leaves org | High — infrastructure, GPU, maintenance | Regulated industries: finance, healthcare, defense, sovereign requirements |

**Shadow IT** is pervasive: employees routinely upload proprietary documents to public LLM interfaces (e.g., pasting a confidential quarterly report into ChatGPT) without realizing it constitutes a data breach. Studies by MIT and Gartner confirm this is widespread.

A real-world cost illustration: deploying a fine-tuned open-source model on Azure for a corporate training demo accumulated ~$400 (INR 25,000) in hosting costs over four days without any meaningful usage — simply from the model being available. Infrastructure cost for Tier 3 is significant and often underestimated.

Real-world nuance (from a Shell representative in the session): Shell started at Tier 3 for EU AI Act compliance but found it became a bottleneck for agility, and is now selectively moving some workloads to Tier 2 via contractual data-protection agreements. This illustrates that the tiers are not mutually exclusive — large organizations will operate across all three depending on use-case sensitivity.

### 7. The Generative AI Stack (Two-Layer → Three-Layer Evolution)
The industry stack has evolved:
- **~2023 view**: Model layer (foundation models for text, image, speech, video) + Application layer (apps built using those models).
- **2025/2026 view**: Model layer (now multimodal frontier models — text, audio, reasoning in one model; divided into proprietary vs. open-weight) + **Orchestration layer** (LangChain, CrewAI, Pinecone, Weaviate, DSPy) + Application layer.

The orchestration layer handles agent workflows, vector databases, retrieval pipelines, and prompt management — the connective tissue between raw model capability and production enterprise applications. This layer is where companies like LangChain and Pinecone operate.

Investment analogy: The current AI spend pattern mirrors the internet era. Massive capital goes into the model layer (OpenAI plans ~$20B in training spend for the year — comparable to the Manhattan Project in inflation-adjusted terms). Revenue, however, is expected to emerge primarily from the application layer (analogous to how Google, Facebook, and Amazon built on top of the fiber/infrastructure layer).

### 8. LLM Limitations for Corporate Use
- **Hallucinations**: Factually wrong outputs presented with high confidence.
- **Bias**: Reproduces training data biases — racial, gender, cultural.
- **Cost**: Training and inference are expensive; energy consumption is extreme (Microsoft pursuing nuclear plant restart; proposals for undersea and orbital data centers).
- **Rapid obsolescence**: Model leaderboard turnover ~20 days means application stability is challenging.
- **Data leakage risk** (Tier 1 shadow IT usage).
- **Governance gap**: Regulation is nascent; responsible AI considerations must be embedded in design.

---

## Models / Architectures Covered

| Name / System | Type | Key Property |
|---|---|---|
| Perceptron (1958) | Neural unit | First mathematical neuron model; foundation of all neural networks |
| ELIZA (1961) | Rule-based chatbot | Pattern-matching NLP; convincing without any learning |
| Hidden Markov Models (1966) | Statistical sequence model | Probabilistic state transitions; early language/speech modeling |
| LSTM (1997) | Recurrent neural network | Long-range sequence memory; solved vanishing gradient for language tasks |
| CNN (2012, AlexNet) | Deep convolutional network | Automatic spatial feature extraction; transformed image recognition |
| GAN (2013) | Generative adversarial network | Generator vs. discriminator training; first practical image generation |
| Word2Vec (2013) | Word embedding model | Distributed semantic representations; enabled modern NLP |
| Transformer (2017) | Attention-based sequence model | Parallelizable, global attention; core architecture of all modern LLMs |
| BERT (2018) | Bidirectional transformer (Google) | Pre-trained bidirectional language understanding; fine-tunable |
| GPT-1/2/3/4/5 (2018–present) | Autoregressive transformer (OpenAI) | Unidirectional next-token prediction; scaled to foundation model status |
| Llama 3 (Meta) | Open-weight LLM | Publicly available weights; enables Tier 3 self-hosting |
| Gemini (Google DeepMind) | Multimodal frontier model | Native multimodality (text, image, audio, video) |
| Claude (Anthropic) | Alignment-focused LLM | Constitutional AI training; emphasis on safety properties |

---

## Important Intuitions & Examples

**Universal Approximation Theorem and the first AI winter for neural networks**: The theorem guarantees that a single-hidden-layer neural network can approximate any continuous function to arbitrary accuracy — given sufficient neurons. In the 1980s, this was misread as "neural networks can solve any problem." Finance firms tried predicting stock markets; nearly all failed because the theorem says nothing about learnability from finite data or the compute required. The subsequent disillusionment was so severe that uttering "neural network" in front of hedge fund investors in the 2000s would end a pitch.

**LLMs as "one slice of the brain"**: Human language and human reasoning are neurologically dissociated — different brain regions. LLMs model the language region only. They produce fluent, contextually plausible language without any guarantee of reasoning or factual grounding. Hallucinations are not bugs to be patched; they are a structural consequence of the architecture.

**Google Trends as market sentiment proxy**: The instructor demonstrated that search trends for "generative AI" have been declining since mid-2024, consistent with the Gartner hype cycle. He also cited prior academic work showing that the ratio of "bull market" vs. "bear market" Google search terms predicted S&P 500 movements, beating passive indices — an early example of alternative data in finance.

**The 150-pilot trap**: A representative from a major auto manufacturer described 150+ siloed AI pilots across the company, none integrated, none delivering P&L impact. This is the modal corporate AI outcome and the driver of the MIT 95%-failure statistic. Root cause: lack of strategy, change management, and integration architecture — not the technology itself.

**Cost reality of Tier 3 deployment**: A fine-tuned open-source model deployed on Azure for a 4-day period (minimal usage) cost ~$400 USD purely in hosting fees. This is a commonly underestimated expense; it escalates further with dedicated GPU infrastructure, maintenance, and MLOps overhead.

**Coca-Cola generative marketing campaign**: Coca-Cola allowed consumers to generate custom images featuring the Coke brand and publish them to social media — turning every customer into a personalized brand ambassador at zero marginal content cost. Illustrates how generative AI compresses the economics of personalized marketing.

---

## Course Roadmap (Sessions 2–10 Preview)

| Session | Topic |
|---|---|
| 2 | Transformer architecture — how language models work; attention mechanism |
| 3 | Building LLMs — pre-training, scaling, BERT vs. GPT paradigms |
| 4 | Using LLMs via API; evaluation metrics (analogous to precision/recall for classifiers) |
| 5 | RAG (Retrieval-Augmented Generation) — enterprise knowledge base access |
| 6 | Image generation models; diffusion models; multimodal LLMs |
| 7 | Reasoning AI — chain-of-thought, reinforcement learning from human feedback (RLHF), o1-style models |
| 8 | Agentic AI — agent architectures, tool use, orchestration frameworks |
| 9 | Future trends and geopolitics of AI |
| 10 | Implementation — project lifecycle, change management, human-in-the-loop design |

---

## Related

- [[deep-learning]]
- [[transfer-learning]]
- [[ai-paradigms]]
- [[emerging-digital-technologies]]
- [[course-06-overview-genai-and-pretrained-models|GenAI and Pretrained Models (Course 06)]]
