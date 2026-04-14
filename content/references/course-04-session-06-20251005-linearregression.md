---
title: "Foundations of ML and AI — Session 06: Linear Regression (Advanced)"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/ml"]
sources:
  - "_raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_06_05Oct2025/20251005_LinearRegression.extracted.txt"
created: 2026-04-12
updated: 2026-04-12
summary: "Advanced linear regression: spurious regression, multiple predictors, categorical encoding, multicollinearity, and model evaluation metrics."
---

# Foundations of ML and AI — Session 06: Linear Regression (Advanced)

**Instructor**: [[dr-sridhar-pappu|Dr. Sridhar Pappu]]  
**Date**: 2025-10-05

Continues from Session 05, extending to multiple linear regression and covering pitfalls and remedies: spurious correlation, categorical predictors, multicollinearity, and model performance metrics.

## Key Concepts

- **Spurious Regression** — high R² despite no causal relationship; domain knowledge essential (e.g., stopping distance is quadratic in speed, not linear — physics equation v²−u²=2ad)
- **Data Transformations** — square root, logarithm to correct non-linearity, non-normality, or heteroscedasticity in residuals
- **Multiple Linear Regression** — extending to >1 independent variable: `ŷ = β₀ + β₁x₁ + β₂x₂ + ...`; each βᵢ interpreted as marginal effect holding others constant
- **Categorical Predictors (Dummy Variables)** — encode nominal categories as 0/1 binary indicators; k categories → k−1 dummies (avoid dummy variable trap)
- **Multicollinearity** — high correlation among predictors inflates standard errors, making individual coefficients unreliable; detected via VIF (Variance Inflation Factor); remedy: remove/combine correlated predictors
- **Model Evaluation Metrics**:
  - *RMSE* (Root Mean Squared Error) — average magnitude of error; same units as target
  - *MAE* (Mean Absolute Error) — less sensitive to outliers than RMSE
  - *MAPE* (Mean Absolute Percentage Error) — scale-free relative error measure
  - *Adjusted R²* — preferred over R² for multi-predictor models

## Residuals Diagnostics (Four Plots)

1. Residuals vs Fitted — check linearity
2. Q-Q Plot — check normality
3. Scale-Location — check homoscedasticity
4. Residuals vs Leverage — check influential observations (Cook's distance)

## Related

- [[dr-sridhar-pappu|Dr. Sridhar Pappu]]
- [[course-04-session-05-20251004-linearregression|Session 05: Linear Regression (intro)]]
- [[course-04-session-06-session-06-05oct2025|Session 06 Notes]]
- [[linear-regression|Linear Regression]]
