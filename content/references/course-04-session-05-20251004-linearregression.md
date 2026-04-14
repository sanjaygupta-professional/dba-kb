---
title: "Foundations of ML and AI — Session 05: Linear Regression"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/ml"]
sources:
  - "_raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_05_04Oct2025/20251004_LinearRegression.extracted.txt"
created: 2026-04-12
updated: 2026-04-12
summary: "Linear regression: Pearson correlation, R², p-values, residuals analysis, and influential observations."
---

# Foundations of ML and AI — Session 05: Linear Regression

**Instructor**: [[dr-sridhar-pappu|Dr. Sridhar Pappu]]  
**Date**: 2025-10-04

Introduces simple linear regression using the aircraft fuel-burn dataset as a running example. Covers model fit diagnostics end-to-end: from correlation through hypothesis testing to residuals checks.

## Key Concepts

- **Pearson's Correlation Coefficient (r)** — scalar −1 to +1 measuring strength and direction of linear relationship between two variables
- **R² (R-Squared)** — percentage of variance in the target explained by the predictor(s); R²=1 means perfect fit, R²=0 means no predictive power
- **Adjusted R²** — penalizes R² for adding unnecessary predictors; use when comparing models with different numbers of features
- **Hypothesis Testing for Slope (p-value)** — tests H₀: β₁=0 (predictor has no effect); p < 0.05 → statistically significant relationship
- **F-test (ANOVA)** — tests overall model significance; p < 0.05 means at least one predictor is useful
- **Residuals** — differences between actual and predicted values (yᵢ − ŷᵢ); four assumptions to verify:
  1. Linearity — residuals scatter randomly around zero
  2. Normality — residuals approximately normally distributed
  3. Homoscedasticity — constant variance across predicted values
  4. No influential observations — no single point unduly distorting the fit
- **SST / SSE / SSR** — Total, Error, and Regression sums of squares; R² = SSR/SST

## Example

Fuel flow (kg/h) as a function of aircraft landing weight (kg):  
`ŷ = −584.31 + 0.0358 × LW`, R² = 0.76, p-value = 1.8×10⁻¹²

## Related

- [[dr-sridhar-pappu|Dr. Sridhar Pappu]]
- [[course-04-session-05-session-05-04oct2025|Session 05 Notes]]
- [[course-04-session-06-20251005-linearregression|Session 06: Linear Regression (continued)]]
- [[linear-regression|Linear Regression]]
