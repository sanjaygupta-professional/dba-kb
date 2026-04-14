---
title: "Deep Learning and Variants — Session 15: NLP Applications — Chatbots, RAG, and Named Entity Recognition"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/foundations"]
sources:
  - "_raw/dba-course/Course_05_Deep_Learning_and_Variants/02_Recordings_and_PPTs/Session_15_11Jan2026/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Hands-on session covering practical NLP application development: building a cloud-based chatbot via the Groq API with LangChain, constructing a local RAG pipeline using FLAN-T5 and sentence transformers for PDF Q&A, and implementing Named Entity Recognition with spaCy and Gradio."
---

# Deep Learning and Variants — Session 15: NLP Applications — Chatbots, RAG, and Named Entity Recognition

**Instructor**: Dr. Srinivasa Varadharajan (Rajan)
**Date**: 2026-01-11
**Course**: [[course-05-overview-deep-learning-and-variants|Deep Learning and Variants]] (Course 05)

---

## Key Concepts

### 1. NLP Application Landscape
NLP underpins a broad class of production AI systems. Five primary application categories were enumerated: (1) chatbots and conversational AI, (2) semantic search and RAG, (3) named entity recognition (NER), (4) sentiment analysis, and (5) text summarization. Session 15 focused on hands-on implementation of the first three categories.

### 2. Open-Source vs. Closed-Source LLMs
LLMs bifurcate into open-source (freely available code and weights, e.g., Qwen, FLAN-T5, OpenAI GPT-2, DeepSeek) and closed-source (subscription/licensed, e.g., GPT-4, Claude, Gemini). Open-source models can be freely used, cloned, and modified but the derived work must remain open — the same model as Linux or Mozilla Firefox. Closed-source models typically deliver higher accuracy but carry API cost and data-privacy risks since inference happens on the vendor's infrastructure. The session used Groq exclusively because it hosts several open-source models and provides a free API tier.

### 3. Groq as an LLM Inference Provider
Groq (groq.com) is a cloud inference platform that hosts multiple open-source LLMs (Qwen, OpenAI GPT-OSS, Llama variants, etc.) and exposes them via a REST API. Users register, generate a one-time API key (displayed only once; expires after use), and call models without downloading weights. This eliminates local GPU/RAM requirements for the inference step. The trade-off: data submitted to Groq for inference is processed externally, making it unsuitable for confidential enterprise data without additional controls.

### 4. LangChain as an Application Framework
LangChain is a Python framework that abstracts the interface between application logic and LLM providers. It supplies pre-built integration code for Groq (`langchain-groq`, `ChatGroq` class), OpenAI, Anthropic, and many others. The workflow is: install (`pip install -q langchain-groq`) → configure API key via environment variable → instantiate the model object → call `llm.invoke("question")`. The raw LLM output is JSON-structured metadata including token counts, latency, and reasoning traces, not just a plain string — a parser or output formatter is needed for production UIs.

### 5. API Conceptual Model
An API (Application Programming Interface) acts as a lightweight bridge between a client application and a remote data/compute resource. Instead of downloading an entire LLM to local disk, the application sends a prompt over HTTPS and receives a response — analogous to embedding Google Maps in a navigation app without storing the entire mapping database locally. In the LLM context this means inference is stateless, scalable, and always uses the provider's latest model weights.

### 6. Retrieval-Augmented Generation (RAG)
RAG is the architecture for domain-specific or enterprise LLM applications. The pipeline is: (a) ingest a document corpus (here, a PDF), (b) chunk the text into sentences or paragraphs, (c) embed each chunk into a dense vector using a sentence transformer model, (d) store vectors in a vector database (FAISS-CPU was used), (e) at query time, embed the user question, retrieve the top-k most similar chunks by cosine similarity, (f) pass retrieved chunks as context to the generative LLM to produce a grounded answer. Because the LLM's generative step is conditioned on retrieved private content rather than on its general pre-training, responses are specific to the uploaded knowledge base and the model weights are never updated.

### 7. Local Model Hosting and Data Privacy
For enterprise data privacy, the model must be downloaded and run locally rather than calling an external API. Session demonstrated this with FLAN-T5 (~990 MB), downloaded from Hugging Face Hub into the Colab runtime. Running locally means the input data never leaves the execution environment. Google Colab with a T4 GPU was used as the local compute substrate; CPU runtime caused the download and inference to hang, confirming that even a small model like FLAN-T5 requires GPU acceleration for acceptable throughput.

### 8. Text Chunking and Embedding Pipeline
PDF text is processed in stages: (1) `PyPDF2` extracts raw text, (2) the text is split into overlapping chunks, (3) `sentence-transformers` (specifically `all-MiniLM-L6-v2`) encodes each chunk into a fixed-dimension embedding vector, (4) `faiss-cpu` indexes those vectors for efficient approximate nearest-neighbor search, (5) cosine similarity is computed between query embedding and chunk embeddings to find the most relevant passage. This is identical to the mechanism inside enterprise semantic search systems.

### 9. Transformers Architecture (Brief)
The Transformer architecture — introduced by the Google "Attention is All You Need" paper (2017) — replaced RNNs as the backbone for NLP. It stores word co-occurrence relationships as high-dimensional vectors with positional encodings; when a new token is seen, cosine distance in the embedding space predicts the most probable next token. FLAN-T5 and similar models are pre-trained transformers fine-tuned for instruction-following. A deeper treatment of encoder-decoder architecture, multi-head attention, and positional encoding is deferred to the subsequent GenAI course.

### 10. Named Entity Recognition (NER)
NER is an NLP sub-task that classifies spans of text into categories: PERSON, ORG (organization), GPE (geopolitical entity), DATE, MONEY, etc. It is used both as a standalone application (e.g., extracting entities from news) and as a data labeling pipeline to improve LLM training data quality. The session used spaCy, a production-grade Python NLP library, with a Gradio front-end. Example: "Steve Jobs founded Apple" → `Steve Jobs` labeled PERSON, `Apple` labeled ORG. spaCy's pre-trained English model correctly disambiguates context — "Apple" in "Steve Jobs founded Apple" is ORG, whereas "I ate an apple" yields no ORG tag.

### 11. Gradio for Rapid UI Prototyping
Gradio is a Python library that wraps any Python function (model inference, file processing, etc.) in an auto-generated web interface. It generates both an in-notebook iframe and a publicly shareable URL. The RAG notebook used Gradio's file-upload component to accept a PDF and a text box for questions; the NER notebook used a text input that returned highlighted entity spans. No HTML/CSS/JS knowledge is required.

### 12. Model Selection and Parameter Tradeoffs
Model size (parameter count) directly governs response quality and infrastructure cost. FLAN-T5-base (~250M parameters, 990 MB) was chosen for speed within Colab's free T4 tier. Larger open-source options — DeepSeek, Llama 3 70B, Qwen 30B — would improve quality but require 20–30 minutes to download or paid compute. The Hugging Face Model Hub provides benchmark leaderboards and linked research papers for each model so practitioners can make evidence-based selection decisions.

---

## Algorithms / Architectures Covered

| Model / Library | Type | Role in Session | Hosting |
|---|---|---|---|
| Qwen (30B) | Decoder-only LLM | Chatbot inference via Groq API | Groq cloud (API) |
| OpenAI GPT-OSS (120B) | Decoder-only LLM | Available alternative on Groq | Groq cloud (API) |
| FLAN-T5 base (~250M params) | Encoder-decoder (seq2seq) | Generative backbone in local RAG pipeline | Downloaded to Colab |
| all-MiniLM-L6-v2 | Sentence transformer | Chunk embedding for vector store | Downloaded to Colab |
| FAISS-CPU | Approximate nearest-neighbor index | Vector database for RAG retrieval | Local (Colab) |
| spaCy (`en_core_web_sm`) | Rule-based + statistical NER | Named entity recognition demo | Downloaded to Colab |
| LangChain (`langchain-groq`) | Framework | Orchestration layer between app and LLM | Python package |
| Gradio | UI library | Web interface for RAG and NER demos | Python package |

---

## Important Intuitions & Examples

**Why use an API instead of downloading a model?** Just as a navigation app does not store every road tile locally but queries Google Maps on demand, an LLM API lets the application stay lightweight. The Groq API key grants authorized access; the model computation and weights remain on Groq's infrastructure.

**RAG vs. general LLM for enterprise use:** Asking a generic model "What is our Q3 refund policy?" will hallucinate an answer based on public training data. A RAG pipeline indexes the company policy PDF, retrieves the relevant clause, and passes it as context — the answer is grounded in the actual document. Data never leaves the local machine if the model is run locally.

**Chunking analogy:** A full PDF cannot be embedded as a single vector without losing local semantics. Chunking breaks "paragraphs → sentences → words" so each embedding captures a coherent idea. Cosine distance then finds which chunk's embedding is closest to the query embedding in the same vector space.

**NER context disambiguation demo:** The sentence "Steve Jobs founded Apple" causes spaCy to tag `Apple` as ORG. The sentence "Yesterday I ate an apple" assigns no ORG label because "apple" appears without the organizational context the model learned during pre-training. Errors on edge cases can be corrected by adding domain-specific knowledge base entries or fine-tuning on flagged examples.

**Token usage transparency:** The raw Groq/LangChain response object exposes `prompt_tokens`, `completion_tokens`, and `total_tokens` alongside the text, plus latency. This metadata is essential for cost estimation and debugging when scaling to production.

**Install → Import sequence in Python:** `pip install` fetches a package from PyPI into the runtime environment (analogous to downloading an app). `import` then loads the package's namespace into the active Python interpreter session (analogous to launching the app). Both steps are always required when using an external library for the first time in a fresh Colab runtime.

---

## Related

- [[deep-learning|Deep Learning]]
- [[transfer-learning|Transfer Learning]]
- [[ensemble-methods|Ensemble Methods]]
- [[ai-paradigms|AI Paradigms]]
