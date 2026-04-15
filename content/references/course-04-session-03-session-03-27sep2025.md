---
title: "Foundations of ML and AI — Session 03"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/ml", "#stats/descriptive"]
sources:
  - "_raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_03_27Sep2025/Session_03_27Sep2025.md"
  - "_raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_03_27Sep2025/Session-03.pdf"
created: 2026-04-12
updated: 2026-04-14
summary: "Descriptive statistics (mean, median, mode, variance, IQR) and introduction to linear regression — worked examples from COVID respiratory data and N95 vs sanitizer inventory. Slide-enriched."
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
---

# Foundations of ML and AI — Session 03

**Course**: [[course-04-overview-foundations-of-ml-and-ai|Foundations of ML and AI]] (Course 04)  
**Date**: 2025-09-27
**Instructor**: [[dr-sridhar-pappu|Dr. Sridhar Pappu]]

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=PbKPV88qQP8)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/Eh35gtQdqIxAt9SgNn-K8xIBFfkcjKFVg_IBS32iA4NDQw?e=7n3oFJ)
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/63316/389469/1174910/5860284)

## Part 1 — Descriptive Statistics

### Measures of Central Tendency

| Measure | Formula | When to use |
|---|---|---|
| **Mean** (μ) | μ = Σx / n | Symmetric distributions, no outliers |
| **Median** | Middle value; position = (n−1)/2+1 for odd n | Skewed distributions, outliers present |
| **Mode** | Most frequent value | Categorical data, bimodal detection |

Rule of thumb: if Mean ≠ Median ≠ Mode, the distribution is skewed.

### Measures of Spread

- **Range** = max − min (sensitive to outliers)
- **IQR** = Q3 − Q1 (robust; used in box plots)
- **Variance** (σ²) = Σ(xi − μ)² / n
- **Standard Deviation** (σ) = √(σ²) — same units as the data

**Box plot anatomy**: minimum → Q1 → Median → Q3 → maximum; whiskers extend to 1.5×IQR; points beyond are flagged as outliers.

### Worked Example: N95 Masks vs Sanitizers

Both products had the same mean weekly sales (791.8 units), but very different spreads:
- **N95 Masks**: high variance → erratic demand, harder to stock
- **Sanitizers**: low variance → stable, predictable demand

Key insight: mean alone is insufficient for inventory decisions — spread determines stocking risk.

### Worked Example: COVID Respiratory Study

Dataset: n = 21 patients; respiratory rate measurements.

- Mean ≈ 17.0
- Median = 4 (position 11 in sorted order)
- The wide gap between mean and median signals a right-skewed distribution (long tail from severe cases).

Used to demonstrate why median is the appropriate central tendency measure for clinical data with extreme outliers.

## Part 2 — Introduction to Linear Regression

Session 03 opened the linear regression topic (continued in Sessions 05 and 06). Agenda covered:

1. **Correlation** — Pearson's r; direction and strength of linear association
2. **R²** — proportion of target variance explained by predictors
3. **Adjusted R²** — penalises for unnecessary predictors; use when comparing models
4. **p-values** — slope p-value (is individual predictor significant?) vs model p-value (F-test: is the model better than the mean?)
5. **Residuals analysis** — checking model assumptions: normality, homoscedasticity, no patterns

See [[linear-regression|Linear Regression]] concept page and [[course-04-session-05-20251004-linearregression|Session 05]] for full treatment.

## Related

- [[linear-regression|Linear Regression]] — full concept page
- [[course-04-session-05-20251004-linearregression|Session 05 Slides]] — linear regression derivation
- [[course-04-session-06-20251005-linearregression|Session 06 Slides]] — multiple regression
- [[dr-sridhar-pappu|Dr. Sridhar Pappu]]
