---
title: "Deep Learning"
category: concepts
tags: ["#ai/dl", "#dba/coursework"]
sources:
    - _raw/dba-course/Course_05_Deep_Learning_and_Variants/02_Recordings_and_PPTs/Session_01_15Nov2025/20251115_DL_C8S1_Introduction.extracted.txt
created: 2026-04-12
updated: 2026-04-12
summary: "ML on unstructured data (images, text, audio, video) using deep ANNs; key enablers are massive datasets, GPUs, and transformer architectures."
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
---

# Deep Learning

**Deep Learning** is machine learning on **unstructured data** (images, text, audio, video) using Artificial Neural Networks (ANNs) with many hidden layers. The "depth" refers to the number of layers — deeper networks learn progressively more abstract representations.

## Three Enablers (Why Now)

1. **Massive datasets** — billions of labelled examples (ImageNet, Common Crawl, etc.)
2. **Multi-core GPU compute** — parallelism makes training feasible; TPUs further accelerate
3. **Algorithmic advances** — backpropagation, dropout, batch normalisation, attention mechanisms, transformers

## ANN Scale Timeline

| Era | Parameters | Milestone |
|---|---|---|
| 1955 | 5–10 | Perceptron |
| 1985 | 50–500 | Backpropagation |
| 2005 | 5K–50K | Deep architectures |
| 2015 | 500K–10M | ImageNet breakthroughs |
| 2020 | 50M–200M | BERT, GPT-2 |
| 2024 | 1B–3T | GPT-4, Gemini |

## Architecture Taxonomy

```mermaid
flowchart TD
    A([Deep Learning]) --> B["MLP<br/>Multi-Layer Perceptron"]
    A --> C["CNN<br/>Convolutional Neural Network"]
    A --> D["RNN · LSTM · GRU<br/>Recurrent Networks"]
    A --> E["Transformer<br/>Attention mechanism"]
    A --> F["Generative Models<br/>VAE · GAN · Diffusion"]

    B -->|"Tabular structured data"| G(["General purpose"])
    C -->|"Images · Video · Spatial"| H(["Computer vision"])
    D -->|"Sequences · Time series"| I(["Sequential data<br/>(largely superseded)"])
    E -->|"Text · Code · Multimodal"| J(["Modern LLMs — GPT, BERT"])
    F -->|"Image/text synthesis"| K(["Content generation"])

    style J fill:#fdf3e8,stroke:#cc6600
    style K fill:#f3e8fd,stroke:#6600cc
```

## Key Architectures

- **MLP (Multi-Layer Perceptron)** — dense layers; general-purpose [[deep-learning|foundation]]
- **CNN (Convolutional Neural Network)** — spatial hierarchy; images, video
- **RNN / LSTM** — sequential data; time series, text (largely superseded by transformers)
- **Transformer** — attention mechanism; text, code, multimodal — basis of all modern LLMs
- **Generative models** — VAEs, GANs, diffusion models, autoregressive LLMs

## Characteristic Properties

- **ML on unstructured data** — the defining feature vs classical ML
- **Feature learning** — the network learns its own features from raw data (no hand-engineering)
- **Expensive to train, cheap to run** — large upfront compute; inference is fast once trained
- **Mostly non-interpretable** — black-box (though attention weights provide partial insight)

## Related

- [[ai-paradigms|AI Paradigms]] — deep learning is the third paradigm, extending ML to unstructured data
- [[transfer-learning|Transfer Learning]] — reusing pre-trained deep models for new tasks
- [[vibe-coding|Vibe Coding]] — LLM-orchestrated development built on deep learning foundations
- [[course-05-session-01-20251115-dl-c8s1-introduction|Course 05 Session 01 Slides]]
- [[course-05-session-02-20251116-dl-c8s1-multi-layer-perceptron|Course 05 Session 02 Slides — MLP]]
- [[dr-srinivasa-varadharajan|Dr. Srinivasa Varadharajan]] — Course 05 instructor
