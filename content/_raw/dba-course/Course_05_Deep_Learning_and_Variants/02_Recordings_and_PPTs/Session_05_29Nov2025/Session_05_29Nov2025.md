---
course: "[[Deep Learning and Variants]]"
course_id: course_05
session: "Session_05_29Nov2025"
date: 2025-11-29
type: lecture
tags: [dba, course_05, lecture]
youtube: "https://www.youtube.com/watch?v=9OVy6zWjHIQ"
created: 2026-04-11
---

# Session 05 29Nov2025

**Course**: [[Deep Learning and Variants]]  
**Date**: 2025-11-29

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=9OVy6zWjHIQ)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/IgDvdn58Zg5_Q6Ati_NJqnYmAVDedWvk3B6yUpC7xqmzhfI?e=f0Q7Us)
- [[transcript.txt|Transcript]]
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/64249/393713/1186780/5915028)

## Key Takeaways

**Topic:** Deep learning optimisation and regularisation techniques

1. **Vanishing Gradients** `[04:23]` — Chained derivatives drive gradients to zero.
2. **Sigmoid Activation Function** `[07:05]` — Derivative max 0.25; vanishes across depth.
3. **Rectified Linear Unit (ReLU)** `[08:46]` — Linear for positive, zero for negative; fixes vanishing.
4. **Mini-Batch Gradient Descent** `[10:01]` — Zigzag convergence from mini-batch noise.
5. **Exponential Moving Average** `[11:10]` — Time-series smoothing over epochs.
6. **Momentum** `[11:06]` — EMA of gradients accelerates convergence.
7. **Learning Rate Decay** `[12:15]` — Systematic LR reduction across epochs.
8. **Root Mean Square Propagation (RMSprop)** `[15:51]` — LR normalised by gradient-variance EMA.
9. **Xavier Initialization** `[17:46]` — Uniform init keyed to neuron counts.
10. **Regularisation** `[18:42]` — Loss + complexity term.
11. **Dropout** `[18:56]` — Stochastic neuron deactivation.
12. **Batch Normalisation** `[18:58]` — Normalise layer inputs to reduce covariate shift.
13. **Ridge Regression** `[82:32]` — L2 penalty — shrinks parameters.
14. **Lasso Regression** `[84:30]` — L1 penalty — drives parameters to zero.
15. **Elastic Net** `[92:46]` — L1 + L2 combined via alpha.
16. **Adaptive Moment Estimation (Adam)** `[167:07]` — Momentum + RMSprop — robust default.

→ See [[concepts_index|Course Concepts Index]] for the full chronological list across all sessions.

## Notes



## Questions

- 
