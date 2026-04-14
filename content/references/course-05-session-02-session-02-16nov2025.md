---
title: "Deep Learning and Variants — Session 02: Perceptron as Regressor/Classifier, Likelihood Functions, and Gradient Descent"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/foundations"]
sources:
  - "_raw/dba-course/Course_05_Deep_Learning_and_Variants/02_Recordings_and_PPTs/Session_02_16Nov2025/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Session covers the mathematical equivalence of the perceptron to linear and logistic regression, the XOR problem as a motivating example for multi-layer networks, maximum likelihood estimation as the cost framework, and gradient descent as the numerical optimization engine."
---

# Deep Learning and Variants — Session 02: Perceptron as Regressor/Classifier, Likelihood Functions, and Gradient Descent

**Instructor**: Dr. Srinivasa Varadharajan (Rajan)
**Date**: 2025-11-16
**Course**: [[course-05-overview-deep-learning-and-variants|Deep Learning and Variants]] (Course 05)

---

## Key Concepts

1. **Perceptron as Linear Regressor**: When the activation function is identity (pass-through) and no threshold is applied, the perceptron output `y = b + w1*x1 + w2*x2 + ... + wn*xn` is exactly a multiple linear regression equation. Weights `w` correspond to regression coefficients `beta`; bias `b` is the intercept.

2. **Perceptron as Logistic Classifier**: Replacing the activation function with the sigmoid (logistic function, S-curve) and adding a threshold (e.g., class 1 if output > 0.5) converts the perceptron into a binary linear classifier — structurally identical to logistic regression.

3. **Linear Regression Assumptions (review)**: Four standard assumptions — (a) Y|X is normally distributed; (b) homoscedasticity (constant variance across X); (c) IID observations; (d) zero-centered residuals with no pattern. Validated via residual plots (linearity, independence, homoscedasticity), QQ plots (normality), and Cook's distance (outliers).

4. **XOR Gate as Perceptron Limitation**: The XOR function (output = 1 iff inputs differ) is not linearly separable — no single line can cleanly classify all four binary input combinations. This is the canonical proof that a single perceptron cannot solve all classification problems and motivates multi-layer architectures.

5. **Multi-Layer Perceptron (MLP) Solution to XOR**: XOR can be decomposed as `(x1 AND NOT x2) OR (NOT x1 AND x2)`, requiring at least two perceptrons whose outputs are ORed together. Two perceptrons in a hidden layer, each drawing a different decision boundary, combine to achieve perfect classification — introducing the concept of a hidden layer.

6. **Notation for Multi-Layer Weights**: Weight index convention `W_ij` means the weight from input `i` to neuron `j`. In deeper networks, a superscript denotes the layer, e.g., `W^(l)_ij`. This notation becomes unwieldy at depth, reinforcing why only numerical solutions are practical.

7. **Hyperparameters in Deep Networks**: For an `m`-layer network there are `m+1` structural hyperparameters (number of layers, number of neurons per layer). For each configuration, the internal parameters (all weights and biases) are optimised numerically; the best-performing configuration is selected.

8. **Sigmoid Causes Weight Collapse (preview)**: Using sigmoid activation throughout a deep network drives all weights toward zero during training (vanishing-gradient effect). Solution (previewed for next session): use identity (linear) activation in all hidden layers; retain sigmoid only at the output layer.

9. **Likelihood Function vs. Probability Distribution**: A probability distribution asks "given parameter P, what is the probability of observing data D?" A likelihood function flips this: "given observed data D, what value of parameter P maximises the probability of having seen D?" Maximum Likelihood Estimation (MLE) finds the parameter values most consistent with the observed data.

10. **Negative Log-Likelihood (NLL) as Cost Function**: Taking the log of the likelihood product converts it to a sum: `L = Σ [ y_i * log(ŷ_i) + (1 - y_i) * log(1 - ŷ_i) ]`. The negative of this sum (NLL) is a convex function for the binomial case — it has exactly one global minimum — making gradient-based optimisation guaranteed to converge.

11. **Gradient Descent Mechanics**: Starting from random parameter values, compute the gradient (vector of partial derivatives, i.e., the direction of steepest cost increase), then update parameters as `θ_new = θ_old − η * ∇J`, where `η` is the learning rate. Repeat until gradient ≈ 0 (slope is flat at the minimum).

12. **Learning Rate as Hyperparameter**: Too small → slow convergence; too large → overshoots the minimum. Typical software defaults: `1e-3` or `1e-4`. The learning rate can theoretically be adapted to the data; adaptive methods (e.g., Adam) are previewed for later sessions.

---

## Algorithms / Models / Architectures Covered

| Name | Type | Key Property |
|---|---|---|
| Perceptron (identity activation) | Linear Regressor | Equivalent to OLS / multiple linear regression |
| Perceptron (sigmoid + threshold) | Binary Classifier | Equivalent to logistic regression with decision boundary |
| Single-hidden-layer MLP (2 neurons) | Neural Network | Solves XOR; requires ≥ 2 perceptrons in parallel |
| Multi-layer Neural Network | Deep Architecture | Stacked sigmoid layers → exponentially nonlinear; only numerical solution feasible |
| Gradient Descent | Optimisation | Iterative parameter update via negative gradient scaled by learning rate |
| Maximum Likelihood Estimation (MLE) | Cost Framework | Finds parameters maximising probability of observed data; NLL is convex for binomial |
| Simple Linear Regression (closed-form) | Statistical Model | `β1 = ρ * (σ_y / σ_x)`, `β0 = ȳ − β1*x̄`; analytic solution only for 1 predictor |
| Multiple Linear Regression | Statistical Model | Closed-form intractable for m predictors; solved via gradient descent |

---

## Important Intuitions & Examples

**Salary Prediction (Regression)**: A perceptron with inputs gender, age, experience, and education predicts salary. Weights are initialised randomly. After each forward pass, the predicted salary is compared to the actual; the error is back-propagated to adjust weights and bias. This continues until weight changes fall below tolerance (e.g., `< 1e-4`).

**MT Cars Data (Classification)**: Using the Motor Trends 1978 car dataset (11 variables, outcome = transmission type: automatic vs manual), the same perceptron architecture with sigmoid activation and a 0.5 threshold replicates binary logistic regression. Cost is minimised via MLE / gradient descent rather than sum-of-squares.

**Convex vs. Non-Convex Cost Surfaces**: NLL is convex (bowl-shaped, one global minimum) for the binomial case — gradient descent is guaranteed to find it. Non-convex surfaces (e.g., K-means elbow) have multiple local minima or none, complicating optimisation.

**Gradient = Slope intuition**: `Gradient = Δy / Δx`. Direction = steepest ascent of the cost surface. Gradient descent moves in the opposite direction. At the minimum, gradient = 0; if the step overshoots and the gradient changes sign, the step size (learning rate) must be reduced.

**Back-Propagation overview**: Forward pass → compute output → compute cost (NLL or SSE) → compute gradients for all weights simultaneously → update all weights → repeat. The phrase "back-propagation" refers specifically to propagating gradient information from output back through every layer to update each weight.

**Activation function as hyperparameter**: No hard rule exists for choosing an activation function. Hidden-layer activations are conventionally kept uniform across neurons within a layer for simplicity. The sigmoid problem (weight collapse) motivates using ReLU-family or identity activations in hidden layers.

---

## Resources Mentioned

- *Deep Learning* — Ian Goodfellow, Yoshua Bengio, Aaron Courville (dense but authoritative)
- StatQuest with Josh Starmer (YouTube) — accessible visual explanations of ML/stats concepts

---

## Related

- [[deep-learning]]
- [[logistic-regression]]
- [[linear-regression]]
- [[transfer-learning]]
- [[ai-paradigms]]
- [[ensemble-methods]]
- [[clustering]]
