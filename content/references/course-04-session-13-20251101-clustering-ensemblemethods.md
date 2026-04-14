---
title: "Foundations of ML and AI — Session 13: Clustering and Ensemble Methods"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/ml"]
sources:
  - "_raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_13_01Nov2025/20251101_Clustering_EnsembleMethods.extracted.txt"
created: 2026-04-12
updated: 2026-04-12
summary: "Agglomerative hierarchical clustering, K-Means deep dive, ensemble methods (bagging, boosting, Random Forest, XGBoost)."
---

# Foundations of ML and AI — Session 13: Clustering and Ensemble Methods

**Instructor**: [[dr-sridhar-pappu|Dr. Sridhar Pappu]]  
**Date**: 2025-11-01

Deepens clustering coverage (hierarchical methods) and introduces ensemble learning — the idea that multiple weak models combined outperform any single model.

## Clustering Algorithms

**K-Means** (continued from Session 12):
- Partitional: assigns each point to exactly one of K clusters via centroid proximity
- Centroid = mean of all points in the cluster; recomputed after each assignment

**Agglomerative Hierarchical Clustering**:
- Bottom-up: starts with N singleton clusters; at each step merges the two closest clusters
- Continues until a single all-encompassing cluster remains
- Result: **dendrogram** (tree diagram) allows choosing K after the fact by cutting at any level
- Linkage criteria for cluster distance: single, complete, average, Ward's method

**Choosing K (for K-Means)**:
- Elbow method: plot within-cluster sum of squares vs K; pick the "elbow" point
- Silhouette score: measures how similar a point is to its own cluster vs the nearest neighbor cluster

## Ensemble Methods

Core idea: combine predictions from multiple models to reduce variance (bagging) or bias (boosting).

**Bagging (Bootstrap Aggregating)**:
- Train multiple models on different bootstrap samples (random with replacement)
- Average predictions (regression) or majority vote (classification)
- Reduces variance without increasing bias

**Random Forest** (Leo Breiman, 2001):
- Bagging of decision trees with an additional twist: at each split, only a random subset of features is considered
- Double randomization (rows + features) creates diverse trees → lower correlation → better ensemble

**Boosting**:
- Sequential: each model focuses on correcting errors of the previous
- **AdaBoost** — upweights misclassified samples
- **Gradient Boosting / XGBoost** — fits the residuals of the previous model; state-of-the-art for tabular data

**Key Trade-offs**:
- Bagging ↓ variance (helps over-fitting)
- Boosting ↓ bias (helps under-fitting); risk of over-fitting on noisy data
- Random Forest: robust, interpretable via feature importance; XGBoost: faster convergence, often better accuracy

## Related

- [[dr-sridhar-pappu|Dr. Sridhar Pappu]]
- [[course-04-session-12-20251026-arm-clustering|Session 12: ARM + K-Means intro]]
- [[course-04-session-13-session-13-01nov2025|Session 13 Notes]]
- [[association-rule-mining|Association Rule Mining]]
- [[clustering|Clustering]]
- [[decision-trees|Decision Trees]]
- [[ensemble-methods|Ensemble Methods]]
