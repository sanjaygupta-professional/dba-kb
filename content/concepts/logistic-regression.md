---
title: "Logistic Regression"
category: concepts
tags: ["#ai/ml", "#dba/coursework"]
sources:
    - _raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_07_11Oct2025/20251011_LogisticRegression_ClassificationMetrics.extracted.txt
created: 2026-04-12
updated: 2026-04-12
summary: "Classification algorithm mapping linear inputs to [0,1] via sigmoid; evaluated with confusion matrix, ROC-AUC, precision/recall."
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
---

# Logistic Regression

A **supervised classification** algorithm. Linear regression fails for classification because its output is unbounded (−∞ to +∞), but probabilities must lie in [0, 1]. The **sigmoid (logistic) function** provides this mapping:

`P(Y=1|X) = 1 / (1 + e^(−(β₀ + β₁x₁ + ...)))`

Parameters are estimated by **Maximum Likelihood Estimation (MLE)**, not least squares.

## Prediction Pipeline

```mermaid
flowchart LR
    A["Features<br/>x₁, x₂ … xₙ"] --> B["Linear combination<br/>z = β₀ + β₁x₁ + …"]
    B --> C["Sigmoid function<br/>P = 1 ÷ (1 + e⁻ᶻ)"]
    C --> D["Probability<br/>P ∈ [0, 1]"]
    D --> E{"Decision threshold<br/>default = 0.5"}
    E -->|"P ≥ threshold"| F(["Predict: Positive ✓"])
    E -->|"P < threshold"| G(["Predict: Negative ✗"])

    style F fill:#efe,stroke:#060
    style G fill:#fee,stroke:#c00
```

**Threshold tuning:** lower it → catches more positives (↑ Recall, ↓ Precision). Raise it → fewer false alarms (↑ Precision, ↓ Recall). Tune for business context.

## Classification Metrics

| Metric | Formula | Use when… |
|---|---|---|
| **Accuracy** | (TP+TN) / N | Classes are balanced |
| **Precision** | TP / (TP+FP) | False positives are costly |
| **Recall (Sensitivity)** | TP / (TP+FN) | False negatives are costly (e.g., disease screening) |
| **F1-Score** | 2 × Precision × Recall / (P+R) | Balanced trade-off |
| **ROC-AUC** | Area under sensitivity vs (1−specificity) curve | Model ranking ability across all thresholds |

## Decision Threshold

Default = 0.5. Lowering increases recall (catches more positives) but reduces precision. Tune for business context — e.g., fraud detection may tolerate more false positives to avoid missed fraud.

## Class Imbalance

When positives are rare (fraud, disease), accuracy is misleading. Remedies: adjust threshold, use precision-recall curve, SMOTE oversampling, class weights.

## Related

- [[linear-regression|Linear Regression]] — regression analogue; motivation for why regression fails at classification
- [[decision-trees|Decision Trees]] — non-probabilistic alternative for classification
- [[ensemble-methods|Ensemble Methods]] — random forest and boosting improve on single logistic models
- [[course-04-session-07-20251011-logisticregression-classificationmetrics|Session 07 Slides]]
- [[dr-sridhar-pappu|Dr. Sridhar Pappu]]
