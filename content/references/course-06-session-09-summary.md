---
title: "GenAI and Pretrained Models — Session 09: Open-Source LLMs — Platforms, Models, and Hands-On Lab"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/llm", "#ai/transformers"]
sources:
  - "_raw/dba-course/Course_06_GenAI_Pretrained_Models/02_Recordings_and_PPTs/Session_09/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Hands-on lab session covering the distinction between closed-source and open-source LLMs, the Groq cloud inference platform, Hugging Face as a model hub, and practical exercises running open-source models (Qwen, GPT-2, FLAN-T5) via API and Google Colab."
---

# GenAI and Pretrained Models — Session 09: Open-Source LLMs — Platforms, Models, and Hands-On Lab

**Course**: [[course-06-overview-genai-and-pretrained-models|GenAI and Pretrained Models]] (Course 06)
**Instructor**: Dr. Yogish (lab/hands-on session instructor)
**Recording**: [YouTube](https://www.youtube.com/watch?v=MNcMPaV01Tc)
**Session Type**: Hands-on lab (second lab of the course; first lab covered Azure OpenAI chatbot and RAG)

---

## Key Concepts

### 1. Closed-Source vs. Open-Source Software — Foundational Distinction

Before approaching LLMs, the session established the open-source software model using familiar examples:

**Closed-source software**: Source code is not visible; implementation details, architecture, and weights are proprietary. Monetization is via subscriptions. Examples: Windows, ChatGPT (OpenAI), Gemini API.

**Open-source software**: Source code is publicly visible on repositories such as GitHub; anyone can inspect, clone, fork, modify, and contribute. Monetization strategies include donations/crowdfunding (Linux Foundation), certification programs, enterprise customization contracts, and dual licensing (community edition free; enterprise edition paid). Examples: Linux kernel, VLC, Firefox, Chromium (the open-source base of Chrome), VS Code (from Microsoft), TypeScript.

Key governance point: Open-source does not mean uncontrolled. Repository maintainers gate contributions — a pull request cannot reach the main branch until the maintainer reviews and merges it. This prevents malicious code injection at the core level (though wrappers and downstream distributions can introduce vulnerabilities, as seen in recent supply-chain incidents).

### 2. Licensing in Open-Source Projects

Open-source licenses (MIT, Apache 2.0, GPL) specify permitted uses. Common obligations:
- Attribution: Cite the source (Chrome's "About" page credits Chromium and other open-source libraries)
- Redistribution: May redistribute copies with the same license
- Commercial use: Generally permitted, but selling a derivative product may require a commercial license (Red Hat model: community free, enterprise paid)

### 3. Closed-Source LLMs — What Is Hidden and Why It Matters

For closed-source LLMs (ChatGPT/GPT-4, Claude, Gemini):
- Exact parameter counts are not disclosed or only approximate
- Weight files are not downloadable
- Training data composition is not revealed
- User data handling policies are opaque
- Architectural choices are proprietary competitive information

Data privacy is a specific enterprise concern: when an organization sends queries to a closed-source LLM API, it cannot verify how that data is stored, used, or shared for future model training.

Recent example discussed: Anthropic alleged that a competitor performed a "distillation attack" — using Anthropic's model outputs as training data for a competing model without authorization.

### 4. Open-Source LLMs — What Is Accessible

For genuinely open-source LLMs (Meta LLaMA, Mistral, Qwen, GPT-2):
- Architecture and implementation code on GitHub
- Weight files (tensors/safetensors) downloadable for local inference
- Training data disclosures (to varying degrees)
- Ability to run locally, ensuring data never leaves the enterprise perimeter

The term "open-source" is used loosely in AI: some models release weights but not training data or architecture code. True open-source requires all three.

### 5. OpenAI's Open-Source History

Despite being named "OpenAI," the company has progressively closed its most capable models. However, it does maintain some open releases:
- **GPT-2**: Fully open; the instructor recommends it as the starting point for anyone beginning their LLM engineering journey
- **OpenAI 120B OSS** (via Groq): A larger openly accessible model (~120 billion parameters, ~75 GB storage)
- **OpenAI 20B OSS**: Smaller variant

### 6. Groq Cloud — Inference Platform for Open-Source Models

**Groq** (not to be confused with xAI's Grok chatbot) is an inference-as-a-service platform built on Groq's proprietary LPU (Language Processing Unit) hardware, optimized for low-latency token generation. Key characteristics:
- Hosts multiple open-source LLMs (Qwen, LLaMA variants, Mistral, Gemma, safety models)
- Free tier with rate limits: ~60 requests/minute, ~6,000 tokens/minute per model
- API-compatible interface (similar syntax to OpenAI API)
- Playground for interactive model testing with configurable parameters (temperature, top-p, max tokens, system prompt)

Rate limits vary by model; heavier models like 120B OSS have tighter limits than lighter ones like Qwen-32B.

**Access flow**: Create account → generate API key → use key in Python code or Groq Playground.

### 7. Models Used in the Lab

| Model | Provider | Parameters | Notes |
|-------|----------|------------|-------|
| GPT-2 | OpenAI | ~117M–1.5B | Fully open; first model to start with for learning |
| FLAN-T5 | Google | 80M–11B | Encoder-decoder; fine-tuned for instruction following |
| Qwen-32B | Alibaba | 32B | Lightweight enough for free Groq tier; multilingual |
| OpenAI 120B OSS | OpenAI | 120B | High quality; large storage (~75 GB) |
| OpenAI 20B OSS | OpenAI | 20B | Smaller variant of above |

### 8. Google Colab as the Lab Environment

Google Colab provides:
- **Free GPU access** (T4 or similar) up to a daily usage limit
- Cloud-based Jupyter notebooks shareable via link
- Runtime → "Change runtime type" to switch to GPU/TPU
- `pip install` of dependencies within the notebook

Colab is appropriate for model experimentation, training, and testing but not for production web applications. Production requires a full backend (Flask, Django, FastAPI) and frontend stack deployed on a cloud service.

The instructor shared a pre-built Colab notebook via Zoom chat; participants saved their own copy via File → "Save a copy in Drive" before running cells.

### 9. API Key Management and Security Best Practices

- API keys are shown only once at creation time — copy immediately
- Store keys in environment variables or secrets managers, never in code
- Set expiration dates (7 days, 30 days) for lab/temporary keys
- Delete cloud resources after practice sessions to avoid unexpected billing
- Monitor usage dashboards (Groq Playground shows token consumption per model)

### 10. Hugging Face as the Central Open-Source Model Hub

Hugging Face hosts hundreds of thousands of open-source models, datasets, and Spaces (demos). Key features:
- Model cards with architecture descriptions, training details, license terms
- Downloadable weight files (`.safetensors`, `.bin`)
- Inference API (paid; Groq is positioned as a free alternative for hosted inference)
- `transformers` Python library for local model loading

Models on Hugging Face include text generation, speech-to-text, text-to-speech, vision, multilingual, and safety/guardrail models (e.g., safety-GPT for prompt injection detection).

### 11. Task Categories Available on Open-Source Platforms

Both Groq and Hugging Face expose models across multiple modalities:
- **Text to text**: Chat completion, summarization, translation, classification
- **Text to speech**: TTS synthesis
- **Speech to text**: ASR (automatic speech recognition)
- **Text to image**: Diffusion-based generation
- **Vision**: Image classification, object detection
- **Safety/guardrail**: Models that inspect prompts for policy violations before passing to the main LLM

### 12. Choosing the Right Open-Source Model

Selection criteria discussed:
- **Parameter count**: More parameters generally means higher quality but greater compute and storage requirements
- **Training data**: What domain data was the model trained on? A model trained on code-heavy data will perform better at coding tasks
- **Benchmark scores**: Check leaderboards (MMLU, HumanEval, MT-Bench) for the task type
- **License**: Some models (LLaMA 2) have commercial-use restrictions above certain user thresholds
- **Quantization**: INT8 and INT4 quantized versions reduce storage and memory requirements at some quality cost

---

## Platforms Reference

| Platform | Type | Cost | Notes |
|----------|------|------|-------|
| Groq Cloud | Inference API | Free tier + paid | LPU hardware; very fast token generation |
| Hugging Face Hub | Model repository + Inference | Free + paid | Canonical open-source model repository |
| Google Colab | Notebook IDE + GPU | Free tier + paid | Best for experimentation; not production |
| Azure OpenAI | Enterprise API | Paid credits | Covered in previous lab session |
| Ollama | Local inference server | Free | Run models on local machine; used in deployment discussions |

---

## Important Intuitions and Examples

**Open source business model**: Red Hat takes the Linux kernel (open-source) and sells an enterprise distribution with support contracts. Google took Chromium (open-source) and shipped Chrome (proprietary). The pattern repeats in LLMs: Meta releases LLaMA weights openly, while companies like Groq build paid services on top.

**"Open" is a spectrum**: ChatGPT is fully closed. LLaMA-3 releases weights but not full training data. True open-source (architecture + weights + data) is rare; EleutherAI's models and GPT-NeoX are among the closest to the academic ideal.

**Why use open-source LLMs in enterprise**: (1) Data stays on-premises, (2) no per-token costs at scale, (3) full control over fine-tuning and alignment, (4) no dependency on a vendor's uptime or pricing changes, (5) auditability of model behavior.

**Rate limits matter**: At 6,000 tokens/minute on Groq's free tier, a single long document analysis can exhaust the limit. Production systems need paid tiers or self-hosted inference.

---

## Related

- [[deep-learning]] — foundation for all LLM architectures
- [[transfer-learning]] — pretrained model paradigm; open-source models enable fine-tuning
- [[ai-paradigms]] — closed vs. open-source AI development philosophies
- [[course-06-session-08-summary]] — previous session on reasoning models and DSPy
- [[course-06-session-10-summary]] — next session on AI agents and agentic workflow design
