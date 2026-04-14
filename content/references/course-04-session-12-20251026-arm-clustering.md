---
title: "Foundations of ML and AI — Session 12: Association Rule Mining and Clustering"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/ml"]
sources:
  - "_raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_12_26Oct2025/20251026_ARM-Clustering.extracted.txt"
created: 2026-04-12
updated: 2026-04-12
summary: "Unsupervised learning: ARM (Apriori algorithm, support/confidence/lift), K-Means clustering, and distance measures."
---

# Foundations of ML and AI — Session 12: Association Rule Mining and Clustering

**Instructor**: [[dr-sridhar-pappu|Dr. Sridhar Pappu]]  
**Date**: 2025-10-26

Covers two core unsupervised learning techniques: Association Rule Mining (finding co-occurrence patterns) and Clustering (grouping similar observations).

## Association Rule Mining (ARM)

Finds frequently co-occurring items in transaction data. Output: if-then rules.

**Apriori Algorithm** (proposed 1994) — generates candidate itemsets of increasing length, pruning those below a minimum support threshold.

**Rule Anatomy**:
- **Antecedent** (LHS): condition {x, y, z}
- **Consequent** (RHS): result {A}
- **Rule length**: number of antecedents

**Key Metrics**:
- **Support** = P(X ∩ Y) — frequency of the itemset in all transactions
- **Confidence** = P(Y|X) = Support(X∪Y)/Support(X) — how often Y appears when X appears
- **Lift** = Confidence / P(Y) — how much more likely Y given X vs random; Lift > 1 means positive association

**Classic examples**: Walmart diapers → beer (Lift = high on Friday evenings); strawberry pop-tarts before hurricanes (Lift = 7×).

**Applications**: retail cross-selling, store layout, medical co-diagnosis, fraud detection (unusual claim combinations), web navigation patterns.

## Clustering

Groups rows into clusters where intra-cluster similarity is high and inter-cluster similarity is low.

**K-Means** (proposed 1957):
- User specifies K (number of clusters)
- Initialize K centroids randomly; assign each point to nearest centroid; recompute centroids; repeat until convergence
- Variants: K-Medians (robust to outliers), K-Modes (for categorical data)
- Limitation: K must be specified; sensitive to outlier centroids; assumes spherical clusters

**Distance Measures for Mixed Data**:
- Numeric variables: Normalized Manhattan distance dᵢⱼ = |xᵢ − xⱼ| / Rk
- Binary/Nominal: 0 if same, 1 if different
- Ordinal: normalized ranks
- Aggregate: average across all variable distances

**Applications**: customer segmentation, spam filtering, driver behavior analysis, news article grouping, gene expression clustering.

## Related

- [[dr-sridhar-pappu|Dr. Sridhar Pappu]]
- [[course-04-session-13-20251101-clustering-ensemblemethods|Session 13: Clustering + Ensemble Methods]]
- [[course-04-session-12-session-12-26oct2025|Session 12 Notes]]
- [[association-rule-mining|Association Rule Mining]]
- [[clustering|Clustering]]
- [[ensemble-methods|Ensemble Methods]]
