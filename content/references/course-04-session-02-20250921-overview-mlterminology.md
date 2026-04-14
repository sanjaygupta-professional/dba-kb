---
title: "Foundations of ML and AI — Session 02: ML Taxonomy and Terminology"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/ml"]
sources:
  - "_raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_02_21Sep2025/20250921_Overview-MLTerminology.extracted.txt"
created: 2026-04-12
updated: 2026-04-12
summary: "Dr. Pappu's taxonomy of ML: supervised/unsupervised blocks, deep learning intro, and structured-data terminology."
---

# Foundations of ML and AI — Session 02: ML Taxonomy and Terminology

**Instructor**: [[dr-sridhar-pappu|Dr. Sridhar Pappu]]  
**Date**: 2025-09-21  
**Course**: Foundations of ML and AI (Course 04)

Establishes the conceptual map of ML — what each "block" of the ML stack does, when to use it, and how deep learning fits in. Also covers structured-data terminology (variables, measurement levels).

## Key Concepts

- **Supervised Learning** — Model trained on labeled input→output pairs. Two main tasks:
  - *Regression* — predicting a continuous number (e.g. customer lifetime value, salary)
  - *Classification* — predicting a category or state (e.g. churn, fraud, spam)
- **Unsupervised Learning** — Finding patterns without labels:
  - *Clustering* — grouping similar rows (K-Means, 1957)
  - *Association Rule Mining (ARM)* — discovering co-occurrence rules among items (Apriori, 1994)
  - *Anomaly Detection* — isolating outliers (Isolation Forest, 2008)
- **Discriminative vs. Generative Models** — Discriminative models separate classes but cannot generate new samples; generative models (Naïve Bayes, then LLMs) model the data distribution
- **Deep Learning** — ML on unstructured data (image, text, audio, video); characterized by large models with 50M–3T parameters; beginnings of GenAI
- **Transfer Learning** — Reusing a pre-trained DL model's learned features on a new, smaller task; enables fine-tuning with limited labeled data
- **Word Embeddings** — Numerical vectors (e.g. Word2Vec) that capture semantic relationships between words; foundation for language models
- **Tokenization** — Breaking text into characters, words, or sub-words for model input

## Algorithms Covered

| Algorithm | Type | Year Proposed |
|---|---|---|
| Logistic Regression | Classification | 1958 |
| Decision Trees | Classification / Regression | 1972 |
| K-Nearest Neighbors (KNN) | Classification | 1951 |
| Naïve Bayes | Generative / Classification | 1950s |
| Random Forest | Ensemble / Classification | 2001 |
| K-Means | Clustering | 1957 |
| Apriori | Association Rule Mining | 1994 |
| Isolation Forest | Anomaly Detection | 2008 |

## Structured Data Terminology

- **Dependent variable** (target/class variable) — what you predict; on y-axis
- **Independent variable** — input features; on x-axis
- **Categorical / Qualitative**:
  - *Nominal* — no order (gender, employee ID, zip code)
  - *Ordinal* — ordered but unequal intervals (fund risk ratings, movie ratings)
- **Numeric / Quantitative**:
  - *Discrete* — countable integers (complaints received, employees)
  - *Continuous* — measurable real values (height, weight, time, percentage returns)

## ML Blocks Taxonomy (from slides)

```
Symbolic AI (Rule/Logic Engines)
├── Machine Learning
│   ├── Supervised: Regression, Classification, Time Series
│   └── Unsupervised: ARM, Clustering, Anomaly Detection, Optimization
└── Deep Learning (unstructured data: text, image, audio, video)
```

## Related

- [[dr-sridhar-pappu|Dr. Sridhar Pappu]]
- [[ai-paradigms|AI Paradigms]] — symbolic / ML / agentic taxonomy covered in Session 01
- [[course-04-session-02-session-02-21sep2025|Session 02 Notes]]
- [[course-04-session-01-20250920-overview|Session 01 Overview (slides)]]
- [[association-rule-mining|Association Rule Mining]]
- [[clustering|Clustering]]
- [[decision-trees|Decision Trees]]
- [[deep-learning|Deep Learning]]
- [[ensemble-methods|Ensemble Methods]]
- [[logistic-regression|Logistic Regression]]
- [[transfer-learning|Transfer Learning]]
