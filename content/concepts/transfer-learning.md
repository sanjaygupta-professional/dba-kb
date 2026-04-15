---
title: "Transfer Learning"
category: concepts
tags: ["#ai/dl", "#dba/coursework"]
sources:
    - _raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_02_21Sep2025/20250921_Overview-MLTerminology.extracted.txt
created: 2026-04-12
updated: 2026-04-12
summary: "Reusing a pre-trained model's learned weights on a new task; enables fine-tuning with limited labelled data; foundation of modern LLMs."
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
---

# Transfer Learning

**Transfer Learning** reuses the internal representations (weights) learned by a model trained on a large dataset to solve a different but related task — typically with far less data.

## Intuition

A deep model trained on millions of images (e.g. ImageNet) has learned to detect edges, textures, shapes, and objects. These features transfer to a new image classification task even if the new classes are completely different. Fine-tuning the last few layers with new labelled data is far cheaper than training from scratch.

## When to Use Which Mode

```mermaid
flowchart TD
    A([New Task]) --> B["Start with pre-trained<br/>foundation model<br/>BERT · GPT · ResNet"]
    B --> C{"Dataset size?<br/>Domain similarity?"}
    C -->|"Small dataset<br/>Similar domain"| D["Feature Extraction<br/>Freeze all layers<br/>Train only the output head"]
    C -->|"Larger dataset<br/>Different domain"| E["Fine-tuning<br/>Unfreeze top layers<br/>Low learning rate"]
    D & E --> F(["Task-specific model<br/>ready for deployment"])

    style D fill:#e8f4fd,stroke:#0066cc
    style E fill:#fdf3e8,stroke:#cc6600
    style F fill:#efe,stroke:#060
```

## Two Modes

| Mode | What you change | When to use |
|---|---|---|
| **Feature extraction** | Only retrain the final classification head; freeze all pre-trained layers | Small dataset; similar domain to pre-training data |
| **Fine-tuning** | Unfreeze some/all layers; train with a lower learning rate | Larger dataset; different domain; need higher accuracy |

## Why Transfer Learning Enables GenAI

Pre-trained foundation models (GPT, BERT, CLIP) have "looked at" so much data that they contain broadly useful world knowledge. Fine-tuning on a task-specific dataset (e.g. medical reports, legal documents) costs a fraction of pre-training. This is the economic basis of the LLM application economy.

## Key Examples

- **BERT** (Google, 2018) — pre-trained on Wikipedia + BooksCorpus; fine-tuned for NLP tasks
- **GPT series** (OpenAI) — pre-trained autoregressively; fine-tuned via RLHF for instruction-following
- **ResNet / EfficientNet** — ImageNet pre-trained weights used as feature extractors in medical imaging, satellite imagery, etc.

## Related

- [[deep-learning|Deep Learning]] — transfer learning is a training strategy within deep learning
- [[ai-paradigms|AI Paradigms]] — foundation models and composite AI paradigm rely heavily on transfer learning
- [[vibe-coding|Vibe Coding]] — LLMs powering vibe-coding are themselves products of transfer learning pipelines
- [[course-04-session-02-20250921-overview-mlterminology|Session 02 Slides]] — deep learning paradigm overview
- [[course-05-session-01-20251115-dl-c8s1-introduction|Course 05 Session 01 Slides]]
