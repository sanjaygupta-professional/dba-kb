---
title: "Foundations of ML and AI — Session 09"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/ml", "#ai/model-evaluation"]
sources:
  - "_raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_09_18Oct2025/Session_09_18Oct2025.md"
  - "_raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_09_18Oct2025/Session-09.pdf"
created: 2026-04-12
updated: 2026-04-14
summary: "Bias-variance tradeoff, the SUB/COV mnemonics, and train/validation/test split strategy. Introduction to Decision Trees. Slide-enriched."
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
---

# Foundations of ML and AI — Session 09

**Course**: [[course-04-overview-foundations-of-ml-and-ai|Foundations of ML and AI]] (Course 04)  
**Date**: 2025-10-18
**Instructor**: [[dr-sridhar-pappu|Dr. Sridhar Pappu]]

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=_jkzz7ouung)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/EoeNzcagLqdBs0Ic4fCSIfQB2RcvtVGhMBh6x0BmpBLAow?e=09Y7Ao)
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/63316/389469/1180482/5886296)

## Bias-Variance Tradeoff

The fundamental tension in supervised learning between two sources of error:

| Term | Definition |
|---|---|
| **Bias** | How far the model's average prediction is from the true value |
| **Variance** | How much predictions change when trained on different samples |
| **Noise** | Inherent randomness in the data; irreducible |

Total error = Bias² + Variance + Noise (irreducible)

### The Bull's-Eye 2×2

Visualised as a shooting target (true value at centre):

|  | Low Variance | High Variance |
|---|---|---|
| **Low Bias** | Ideal — clustered at centre | Scattered but centred on average |
| **High Bias** | Consistently off-target | Scattered AND off-target |

### Mnemonics: SUB and COV

Dr. Pappu's memorable teaching devices:

- **SUB** = **S**imple model → **U**nderfits → **B**ias problem
- **COV** = **C**omplex model → **O**verfits → **V**ariance problem

The goal is to find the model complexity "sweet spot" between SUB and COV.

## Train / Validation / Test Splits

| Split | Purpose | Typical ratio |
|---|---|---|
| **Training** | Model learns from this data | 60–70% |
| **Validation** | Tune hyperparameters, compare models | 20% |
| **Test (holdout)** | Final unbiased performance estimate | 10–20% |

Critical rule: **the holdout set is never used during model building**. Using it for selection leaks information and inflates apparent performance.

Common splits: 70:20:10 or 60:20:20.

### Why this matters for DBA research

When publishing results, using a held-out test set is what makes performance claims credible. See [[doctoral-research-methodology|doctoral research methodology]] — the golden dataset strategy uses exactly this logic.

## Introduction to Decision Trees

Session 09 opened the Decision Tree topic (continued in Session 10):
- Non-parametric, tree-based classifier/regressor
- Splitting criterion based on information gain (entropy reduction)
- Key trade-off: tree depth ↔ bias-variance tradeoff

See [[course-04-session-10-session-10-19oct2025|Session 10]] for full entropy and ID3 treatment.

## Related

- [[decision-trees|Decision Trees]] — concept page
- [[ensemble-methods|Ensemble Methods]] — how Random Forest addresses the bias-variance tradeoff
- [[course-04-session-10-session-10-19oct2025|Session 10]] — entropy, information gain, ID3, KNN
- [[doctoral-research-methodology|Doctoral Research Methodology]] — golden dataset strategy
- [[dr-sridhar-pappu|Dr. Sridhar Pappu]]
