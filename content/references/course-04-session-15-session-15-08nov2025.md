---
title: "Foundations of ML and AI — Session 15"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/ml", "#ai/time-series"]
sources:
  - "_raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_15_08Nov2025/Session_15_08Nov2025.md"
  - "_raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_15_08Nov2025/Session-15.pdf"
created: 2026-04-12
updated: 2026-04-14
summary: "Time series forecasting — components (Trend, Seasonality, Randomness), causal variables, worked examples from Microsoft stock and COVID-19 data. Final session of Course 04; course summary included. Slide-enriched."
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
---

# Foundations of ML and AI — Session 15

**Course**: [[course-04-overview-foundations-of-ml-and-ai|Foundations of ML and AI]] (Course 04)  
**Date**: 2025-11-08 (final session of Course 04)
**Instructor**: [[dr-sridhar-pappu|Dr. Sridhar Pappu]]

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=F9omQ_TmI4w)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/EoJmOAT462BJnZhLfHhM8qYBH07u-UeFM7DyVNXjDEG-qg?e=PDtztd)
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/63316/389469/1183485/5899804)

## Time Series Forecasting

Time series forecasting predicts future values of a variable from its own history and (optionally) from causal external variables.

**General form:**

`ŷₜ₊₁ = f(yₜ, yₜ₋₁, yₜ₋₂, …) + f(x₁, x₂, x₃, …)`

where f can be linear (ARIMA-style) or nonlinear (neural networks, gradient boosting).

### The Two Input Types

| Input type | Examples | Role |
|---|---|---|
| **Lagged values** (endogenous) | Last 3 months' sales | Captures autocorrelation, trend, seasonality |
| **Causal variables** (exogenous) | Promotions, price, holidays, weather | Captures external drivers |

Including exogenous variables is what distinguishes causal forecasting (e.g. ARIMAX, XGBoost with features) from pure autoregressive models (ARIMA).

### Components of a Time Series

| Component | Description |
|---|---|
| **Trend** | Long-run upward or downward movement |
| **Seasonality** | Regular periodic pattern (weekly, monthly, annual) |
| **Randomness** | Irregular, unpredictable variation (also: noise, remainder, irregular component) |

Decomposition: a time series can often be decomposed as: `yₜ = Trend × Seasonality × Random` (multiplicative) or additive form.

### Worked Examples

**Microsoft stock price (2011–2016)**  
Five-year price chart shows a clear upward **trend** with minor noise. Seasonal patterns are weak in stock data. Demonstrates pure trend extraction.

**COVID-19 daily cases**  
Daily case counts show both a **trend** (initial exponential rise, subsequent peaks) and **seasonality** (weekly reporting cycle — lower counts on weekends when testing labs have reduced capacity). The COVID example illustrates that seasonality is not always calendar-driven — it can arise from process artifacts.

## Course 04 Summary

Session 15 doubles as the course capstone. The full Course 04 arc:

| Sessions | Topic |
|---|---|
| 01–02 | ML overview, terminology, Python/Pandas foundations |
| 03–06 | Statistics fundamentals, linear regression |
| 07–08 | Logistic regression, classification metrics |
| 09–10 | Bias-variance tradeoff, decision trees, KNN |
| 11–13 | Clustering (K-Means, DBSCAN), association rules (ARM) |
| 14–15 | Ensemble methods, time series forecasting |

## Related

- [[linear-regression|Linear Regression]] — Sessions 03–06 material
- [[decision-trees|Decision Trees]] — Sessions 09–10 material
- [[ensemble-methods|Ensemble Methods]] — Session 14 material
- [[clustering|Clustering]] — Sessions 11–13 material
- [[course-04-session-09-session-09-18oct2025|Session 09]] — bias-variance context
- [[dr-sridhar-pappu|Dr. Sridhar Pappu]]
