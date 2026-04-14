---
title: "Decision Trees"
category: concepts
tags: ["#ai/ml", "#dba/coursework"]
sources:
    - _raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_02_21Sep2025/20250921_Overview-MLTerminology.extracted.txt
created: 2026-04-12
updated: 2026-04-12
summary: "Tree-based supervised model splitting data on feature thresholds; interpretable; used for both classification and regression tasks."
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
---

# Decision Trees

A **supervised learning** model that recursively partitions data by splitting on feature thresholds, producing a tree of if-then rules. Proposed in 1972. Used for both **classification** (Classification Trees) and **regression** (Regression Trees).

## How They Work

At each node, the algorithm selects the feature and split point that best separates the target:
- Classification: maximise information gain (entropy reduction) or Gini impurity reduction
- Regression: minimise within-node variance (SSE)

Splitting continues until a stopping criterion is met (max depth, min samples per leaf, or purity threshold).

## Key Properties

- **Interpretable** — the path from root to leaf is a human-readable rule
- **Non-parametric** — no distributional assumptions
- **Handles mixed data** — works with both numeric and categorical features natively
- **Prone to overfitting** — deep trees memorise training data; controlled via pruning or max depth

## Strengths vs Limitations

| Strengths | Limitations |
|---|---|
| Highly interpretable | High variance — small data changes produce very different trees |
| No feature scaling needed | Struggles with linear relationships |
| Handles missing data | Prone to overfitting without regularisation |

## Relationship to Ensembles

Single decision trees have high variance. [[ensemble-methods|Ensemble methods]] (Random Forest, boosting) combine many trees to dramatically reduce variance and improve accuracy.

## Related

- [[ai-paradigms|AI Paradigms]] — sits in the supervised classification block
- [[ensemble-methods|Ensemble Methods]] — Random Forest and XGBoost build on decision trees
- [[logistic-regression|Logistic Regression]] — probabilistic alternative
- [[course-04-session-02-20250921-overview-mlterminology|Session 02 Slides]] — ML taxonomy overview
