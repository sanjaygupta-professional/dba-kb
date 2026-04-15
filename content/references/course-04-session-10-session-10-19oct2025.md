---
title: "Foundations of ML and AI — Session 10"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/ml", "#ai/decision-trees"]
sources:
  - "_raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_10_19Oct2025/Session_10_19Oct2025.md"
  - "_raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_10_19Oct2025/Session-10.pdf"
created: 2026-04-12
updated: 2026-04-14
summary: "Decision trees (entropy, information gain, ID3 algorithm, Gain Ratio) and KNN. Includes Wordle analogy for information content and the high-cardinality attribute warning. Slide-enriched."
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
---

# Foundations of ML and AI — Session 10

**Course**: [[course-04-overview-foundations-of-ml-and-ai|Foundations of ML and AI]] (Course 04)  
**Date**: 2025-10-19
**Instructor**: [[dr-sridhar-pappu|Dr. Sridhar Pappu]]

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=Vc9XApUUn88)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/Eqmhmg4ov69EhMkHcuCzFOIB0Ec2wGHWiq0lX7DE0jJBpA?e=1W1rvR)
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/63316/389469/1180809/5887929)

## Information Content and Entropy

**Information content** (self-information) of a single event with probability p:

`I(p) = −log₂(p)` bits

A certain event (p=1) carries 0 bits. A rare event (p≈0) carries many bits — surprises are informative.

**Entropy** (expected information content across all outcomes):

`H = −Σ pᵢ · log₂(pᵢ)`

### Wordle Analogy

Wordle provides an intuitive model: each guess reveals coloured tiles that eliminate candidates. A guess that halves the remaining word pool provides exactly 1 bit of information. The best opening guess is the one that maximises expected information — i.e., expected entropy reduction.

Dr. Pappu used this to make the abstract formula tangible: information = how much uncertainty is reduced.

### Worked Example — Information Content

| Attribute | Number of states | Information Content |
|---|---|---|
| Car Type (Small / Family / Truck) | 3 | 1.52 bits |
| Customer ID (20 unique customers) | 20 | 4.32 bits |

Customer ID has more than 2.8× the information content of Car Type, purely because it has more states.

## Information Gain and the ID3 Algorithm

**Information Gain (IG)** is the reduction in entropy achieved by splitting on an attribute:

`IG(attribute) = H(before split) − H(after split)`

The **ID3 algorithm** greedily selects the attribute with the highest IG at each node.

### The High-Cardinality Attribute Problem

A critical flaw in raw IG: attributes with many distinct states (like Customer ID) will almost always show high IG, because each leaf is nearly pure. This leads to overfitting — the tree memorises customer IDs instead of learning patterns.

**Remedy: Gain Ratio** = IG / Information Content of the attribute

Gain Ratio normalises IG by how much information the attribute itself contains. Customer ID now scores low (high IG but huge IC in denominator). Car Type with genuinely predictive splits scores higher.

This is why ID3 can be replaced by **C4.5** (uses Gain Ratio) or **CART** (uses Gini impurity) in practice.

## K-Nearest Neighbours (KNN)

Session 10 also introduced KNN as a contrasting non-parametric method:
- No explicit model training — stores all training data
- Classifies a new point by majority vote of its k nearest neighbours (by Euclidean distance)
- Hyperparameter k controls bias-variance tradeoff: small k = high variance; large k = high bias
- Requires feature scaling (distance-sensitive)

Contrast with decision trees: KNN produces smooth decision boundaries; trees produce rectangular axis-aligned boundaries.

## Related

- [[decision-trees|Decision Trees]] — concept page; updated with Gain Ratio nuance
- [[course-04-session-09-session-09-18oct2025|Session 09]] — bias-variance tradeoff, tree intro
- [[ensemble-methods|Ensemble Methods]] — Random Forest addresses the high-variance problem in single trees
- [[dr-sridhar-pappu|Dr. Sridhar Pappu]]
