---
title: "Foundations of ML and AI — Session 07: Logistic Regression and Classification Metrics"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/ml"]
sources:
  - "_raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_07_11Oct2025/20251011_LogisticRegression_ClassificationMetrics.extracted.txt"
created: 2026-04-12
updated: 2026-04-12
summary: "Logistic regression via sigmoid function, classification metrics (confusion matrix, ROC-AUC), and model calibration."
---

# Foundations of ML and AI — Session 07: Logistic Regression and Classification Metrics

**Instructor**: [[dr-sridhar-pappu|Dr. Sridhar Pappu]]  
**Date**: 2025-10-11

Covers why linear regression fails for classification tasks, how the sigmoid (logistic) function fixes that, and the full suite of classification evaluation metrics.

## Why Logistic Regression?

Linear regression outputs ŷ ∈ (−∞, ∞), but for classification we need P(Y=1|X) ∈ [0,1]. The **sigmoid / logistic function** maps any real number to [0,1]:

```
P(Y=1|X=x) = 1 / (1 + e^(−(β₀ + β₁x)))
```

Parameters β are estimated via **Maximum Likelihood Estimation (MLE)** rather than Ordinary Least Squares.

## Key Concepts

- **Decision Threshold** — default 0.5; lower threshold increases sensitivity (recall) at the cost of precision; adjust for business context (e.g., cancer screening → lower threshold)
- **Confusion Matrix** — 2×2 table of TP, FP, TN, FN:
  - *Precision* = TP / (TP + FP) — of predicted positives, how many are real
  - *Recall / Sensitivity* = TP / (TP + FN) — of actual positives, how many caught
  - *Specificity* = TN / (TN + FP) — of actual negatives, how many correctly rejected
  - *F1-Score* = harmonic mean of precision and recall
  - *Accuracy* — misleading on imbalanced data
- **ROC Curve** — plots Sensitivity vs (1−Specificity) across all thresholds; area under curve (**AUC**) = 1 is perfect, 0.5 = random
- **Class Imbalance** — when positives are rare (fraud, disease), accuracy is uninformative; use AUC, precision-recall curve, or SMOTE for resampling

## Applications Covered

- Flight delay prediction, spam detection, diabetes prediction, loan default, tumour classification

## Related

- [[dr-sridhar-pappu|Dr. Sridhar Pappu]]
- [[course-04-session-07-session-07-11oct2025|Session 07 Notes]]
- [[course-04-session-05-20251004-linearregression|Session 05: Linear Regression]] — contrast with regression approach
- [[linear-regression|Linear Regression]]
- [[logistic-regression|Logistic Regression]]
