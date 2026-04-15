---
title: "Clustering"
category: concepts
tags: ["#ai/ml", "#dba/coursework"]
sources:
    - _raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_13_01Nov2025/20251101_Clustering_EnsembleMethods.extracted.txt
created: 2026-04-12
updated: 2026-04-12
summary: "Unsupervised grouping of observations by similarity; K-Means (partitional) and agglomerative hierarchical are the core algorithms."
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
---

# Clustering

An **unsupervised learning** technique that groups observations so that intra-cluster similarity is high and inter-cluster similarity is low. No labelled target variable — the algorithm discovers structure in the data.

## K-Means (Partitional)

Proposed: 1957. User specifies K (number of clusters).

```mermaid
flowchart TD
    A([Dataset]) --> B["Initialise K centroids<br/>randomly"]
    B --> C["Assign each point to<br/>nearest centroid<br/>Euclidean distance"]
    C --> D["Recompute centroids<br/>as cluster means"]
    D --> E{"Centroids<br/>changed?"}
    E -->|Yes — iterate| C
    E -->|No — converged| F(["K clusters ready"])

    style F fill:#efe,stroke:#060
```

Algorithm:
1. Initialise K centroids randomly
2. Assign each point to nearest centroid (Euclidean distance by default)
3. Recompute centroids as mean of assigned points
4. Repeat steps 2-3 until convergence

**Choosing K**: Elbow method (plot within-cluster SSE vs K; choose the "elbow"); Silhouette score.

**Variants**: K-Medians (robust to outliers), K-Modes (for categorical data).

**Limitation**: assumes spherical clusters; sensitive to initialisation; K must be specified in advance.

## Agglomerative Hierarchical Clustering

Bottom-up: starts with N singleton clusters; repeatedly merges the two closest clusters until one remains. Produces a **dendrogram** — K can be chosen after the fact by cutting at any level.

Linkage criteria (how to measure cluster-cluster distance):
- Single linkage — minimum pairwise distance (chaining effect)
- Complete linkage — maximum pairwise distance (compact clusters)
- Average linkage — mean pairwise distance
- Ward's method — minimise within-cluster variance increase

## Distance Measures for Mixed Data

| Variable type | Distance measure |
|---|---|
| Numeric | Normalised Manhattan: \|xᵢ−xⱼ\| / range |
| Binary/Nominal | 0 if same, 1 if different |
| Ordinal | Normalised rank difference |
| Aggregate | Mean across all variables |

## Business Applications

Customer segmentation, spam filtering, driver behaviour profiling, news article grouping, gene expression analysis, document retrieval clustering.

## Related

- [[association-rule-mining|Association Rule Mining]] — co-taught alongside clustering in Course 04 Session 12
- [[ai-paradigms|AI Paradigms]] — clustering sits in the unsupervised learning block
- [[course-04-session-12-20251026-arm-clustering|Session 12 Slides]]
- [[course-04-session-13-20251101-clustering-ensemblemethods|Session 13 Slides]]
- [[dr-sridhar-pappu|Dr. Sridhar Pappu]]
