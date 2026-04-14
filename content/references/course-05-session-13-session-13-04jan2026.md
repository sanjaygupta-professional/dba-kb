---
title: "Deep Learning and Variants — Session 13: Recurrent Neural Networks and Long Short-Term Memory"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/foundations"]
sources:
  - "_raw/dba-course/Course_05_Deep_Learning_and_Variants/02_Recordings_and_PPTs/Session_13_04Jan2026/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Session 13 covers Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks as tools for modelling sequential and time-series data, building intuition for feedback architectures, gated memory mechanisms, and practical use-case guidance."
---

# Deep Learning and Variants — Session 13: Recurrent Neural Networks and Long Short-Term Memory

**Instructor**: Dr. Srinivasa Varadharajan (Rajan)
**Date**: 4 January 2026
**Course**: [[course-05-overview-deep-learning-and-variants|Deep Learning and Variants]] (Course 05)

---

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=a3tckGYArLQ)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/IgCeL0c-kd91Sbl9ITyWffFDAV2q7XX7MvqHpJBUEn_L0sY?e=TZojBb)
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/64249/393713/1191914/5940663)

---

## Key Concepts

### 1. Why Standard Neural Networks Fail on Sequential Data
Feed-forward networks (CNNs, dense DNNs) treat inputs as order-independent. For sequential data — time series, text, audio — the order of inputs is essential. Classical ARMA/ARMAX models capture linear temporal dependencies but break down when those dependencies are nonlinear (e.g., weather prediction across 22 meteorological variables, stock prices, bike-rental counts). Neural networks are therefore needed for nonlinear sequential modelling.

### 2. Sequential vs. Time-Series Data
Rajan draws a distinction: *time-series* applies to structured tabular data ordered by timestamp (temperature, stock prices, power consumption), while *sequential data* is broader and includes unstructured inputs of arbitrary and potentially infinite length (text, speech). Both share the property that the position of an element in the sequence carries predictive signal.

### 3. The Concept of State
The key cognitive mechanism for handling sequences is **state** — a cumulative, compressed representation of everything observed so far. State is dynamic: it is updated with every new input. The analogy used: when reading "I looked for Joe at the __ station," a reader can fill in "train" because the state vector built from the preceding sentences encodes the Joe–train association. State is neither a single memory slot nor an exact replay of history; it is an abstract lossy summary.

### 4. Recurrent Neural Networks (RNNs) — Architecture
An RNN reuses the *same* set of weights at every time step — this is the meaning of "recurrent." The model has two governing equations:

- **State update**: `h_t = tanh(W · h_{t-1} + U · x_t + b)`
- **Output**: `y_t = sigmoid(V · h_t + c)`

Where:
- `x_t` = input at time *t*
- `h_t` = hidden state (the "memory") at time *t*
- `W` = state-to-state weight matrix
- `U` = input-to-state weight matrix
- `V` = state-to-output weight matrix
- `b`, `c` = bias vectors

The tanh activation is used for state updates (range −1 to +1) to slow gradient decay relative to sigmoid. The same W, U, V apply across all timestamps — parameter sharing is what makes the network "one network used again and again."

### 5. Backpropagation Through Time (BPTT)
Training an RNN is conceptually equivalent to unrolling the network over *n* time steps, treating it as a deep feed-forward network, and applying standard backpropagation. In practice, weight updates are computed at each time step and averaged to enforce the shared-weight constraint. The key difficulty is **vanishing and exploding gradients**, which worsen as sequences grow longer.

### 6. Vanishing / Exploding Gradients and Mitigations
Because W is repeatedly multiplied through time, small eigenvalues cause gradients to vanish and large ones cause them to explode. Mitigations discussed:
- Use **tanh** instead of sigmoid for state updates (slower decay due to the −1 to +1 range).
- **Gradient clipping** to bound the magnitude of updates.
- **Long-delay connections**: feed back not just h_{t-1} but h_{t-k} for some hyperparameter k, providing a direct gradient highway across multiple steps.

### 7. RNN Input/Output Topologies
RNNs generalise the input–output contract beyond the one-to-one mapping of feed-forward networks:
- **One-to-one**: standard classification (also achievable by feed-forward nets).
- **One-to-many**: image captioning — single image in, sequence of word tokens out.
- **Many-to-one**: sentiment analysis or news categorisation — sequence of words in, single class label out.
- **Many-to-many**: machine translation, video annotation — variable-length sequence in, variable-length sequence out.

### 8. Long Short-Term Memory (LSTM) — Motivation
A plain RNN accumulates all past state indiscriminately. In practice, not all past information is relevant. Example from session: "I met this French girl Emily… Here I am booking my tickets to ___." The correct answer ("Paris") requires retaining the single word "French" while discarding irrelevant details (where the conference was, that the mother hugged, that the dad winked). An RNN cannot selectively suppress context. LSTMs are designed to do exactly this.

### 9. LSTM Gates — The Core Mechanism
Each LSTM cell introduces **two memory streams** and **three sigmoid gates**:

**Memory streams**:
- `C_t` — **cell state** (long-term memory): flows horizontally through time with only multiplicative and additive modifications.
- `h_t` — **hidden state** (short-term memory): the processed output passed to the next step.

**Three gates** (all sigmoids, output ∈ [0, 1]):
- **Forget gate** `f_t = σ(W_f · [h_{t-1}, x_t] + b_f)`: decides what fraction of the previous cell state to retain. Near 0 → erase; near 1 → retain. Example: when a new subject appears in a sentence, the forget gate suppresses the stored gender of the old subject.
- **Input gate** `i_t = σ(W_i · [h_{t-1}, x_t] + b_i)`: decides whether the candidate update should be written into cell state.
- **Candidate cell update** `C̃_t = tanh(W_c · [h_{t-1}, x_t] + b_c)`: the potential new memory content (range −1 to +1). A negative tanh value *weakens* the context even when the input gate is open.
- **Output gate** `o_t = σ(W_o · [h_{t-1}, x_t] + b_o)`: decides how much of the cell state to expose as the hidden state `h_t`.

**Cell state update**: `C_t = f_t ⊙ C_{t-1} + i_t ⊙ C̃_t`

The top pathway (cell state) is the long-term memory channel; the bottom pathway (hidden state processing) is the short-term memory channel. This dual-pathway design is the origin of the name *Long Short-Term Memory*.

### 10. Context Dynamics and Forgetting
Because the forget gate sigmoid is always ≤ 1, the cell state is continuously attenuated — long-term information naturally decays. New inputs partially replenish the cell state via the input gate. In the limit, if both `f_t ≈ 0` and `i_t ≈ 0`, the entire context is wiped and rebuilt. This explains the observed behaviour in LLMs where early-conversation context is "forgotten" after many turns.

### 11. When to Use LSTM vs. ARMAX
Rajan's practical guidance:
- **Structured sequential data with linear/mildly nonlinear history**: prefer ARMAX — simpler, interpretable, less compute.
- **Structured sequential data with complex nonlinear historical dependencies**: LSTM strongly preferred.
- **Unstructured sequential data (text, audio)**: ARMAX is inapplicable; use RNN/LSTM as a baseline, transformers for state-of-the-art.

### 12. Bridge to Generative AI
LSTMs performing text generation already constitute rudimentary generative models: the output at step *t* is fed back as input at step *t+1*, auto-regressively producing new tokens from context. Rajan identifies this as the conceptual ancestor of GPT-style models. The next session covers GANs (Generative Adversarial Networks) and image generation, completing the transition to generative AI.

---

## Algorithms / Architectures Covered

| Architecture | Type | Key Innovation | Activation | Primary Use |
|---|---|---|---|---|
| Vanilla RNN | Recurrent NN | Shared-weight feedback loop; hidden state | tanh (state), sigmoid (output) | Short sequences, simple temporal patterns |
| RNN with Long Delays | Recurrent NN | Direct connections across k time steps | tanh / sigmoid | Mitigating vanishing gradients |
| LSTM | Gated Recurrent NN | Three gates + dual memory pathways (cell state + hidden state) | tanh (processing), sigmoid (gating) | Long sequences, complex nonlinear context |
| ARMAX (classical reference) | Statistical time-series | Linear autoregression + exogenous variables | N/A | Structured, linearly correlated time-series |

---

## Important Intuitions & Examples

**The state as compressed history.** Rajan uses the Anna Karenina analogy: readers cannot recall the exact words from 500 pages earlier, but retain the *meaning*, emotional tone, and relational context. The RNN hidden state `h_t` is the mathematical counterpart — a lossy but semantically rich summary of the sequence so far.

**The French girl example (LSTM motivation).** A paragraph about meeting a French girl at a conference and arranging parental approval ends with "Here I am booking my tickets to ___." Humans answer "Paris" by retaining the single salient fact (nationality = French) and discarding all irrelevant information. A plain RNN accumulates everything; an LSTM's forget gate selectively suppresses irrelevant context.

**Sigmoid as a gate.** When the sigmoid output is 0, it multiplies to zero — the gate is closed and no information passes. When it is 1, the gate is fully open. In between, partial information flows. Crucially, gradients almost never drive the sigmoid exactly to 0 in practice because that requires the pre-activation to be extremely negative, which demands near-zero weights, biases, and inputs simultaneously.

**tanh can weaken context.** If the input gate `i_t ≈ 1` (gate open) but the candidate `C̃_t ≈ −1` (tanh very negative), the cell state is *reduced*, not increased. This is how the network erases an old concept (e.g., old subject gender) when a new contradicting concept arrives.

**Weather prediction as motivating problem.** The Australian rain-tomorrow dataset with 22 features (min/max temperature, rainfall, evaporation, wind gust speed/direction, humidity at 9 am/3 pm, cloud cover, pressure, etc.) illustrates why temporal neural models are needed: the dependencies between today's conditions and tomorrow's rainfall are both multi-variate and nonlinear, breaking linear ARMAX assumptions.

**Framework guidance (PyTorch vs Keras/TensorFlow).** Rajan's view: PyTorch is gaining industry dominance; at this stage the choice is largely one of familiarity and infrastructure constraints. No strong technical reason to switch frameworks mid-project unless there is an explicit deployment requirement.

---

## Related

- [[deep-learning|Deep Learning]]
- [[transfer-learning|Transfer Learning]]
- [[ensemble-methods|Ensemble Methods]]
- [[ai-paradigms|AI Paradigms]]
