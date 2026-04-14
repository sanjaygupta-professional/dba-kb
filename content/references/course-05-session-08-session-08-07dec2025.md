---
title: "Deep Learning and Variants — Session 08: Autoencoders, Denoising, and Entity Embeddings"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/foundations"]
sources:
  - "_raw/dba-course/Course_05_Deep_Learning_and_Variants/02_Recordings_and_PPTs/Session_08_07Dec2025/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Covers autoencoder applications (denoising, image colourisation, image segmentation, speech-to-face synthesis) and entity embeddings as a neural-network-learned encoding for high-cardinality categorical variables, with the Rossmann Kaggle case study."
---

# Deep Learning and Variants — Session 08: Autoencoders, Denoising, and Entity Embeddings

**Instructor**: Dr. Srinivasa Varadharajan (Rajan)
**Date**: 2025-12-07
**Course**: [[course-05-overview-deep-learning-and-variants|Deep Learning and Variants]] (Course 05)

---

## Key Concepts

### 1. Autoencoder Recap and the Encoder-Decoder Lego Principle
An autoencoder is a symmetric network trained to regenerate its own input. The encoder half compresses the input into a **latent space representation** (also called embedding or encoding); the decoder reconstructs the original from that representation. Because the latent vector has a fixed dimensionality, encoders and decoders from different domain-specific autoencoders can be mixed and matched — e.g., pairing an English-text encoder with a French-text decoder yields a translation network without task-specific architecture redesign.

### 2. Latent Space / Embedding Dimensionality
The bottleneck layer need not be smaller than the input; a larger embedding is possible but wasteful. In practice a **reduced representation** is preferred. Autoencoders perform non-linear dimensionality reduction analogous to PCA, but capable of capturing non-linear structure in the data.

### 3. Denoising Autoencoders
Training procedure: take a clean image, synthetically corrupt it (pixel inversion for binary images; uniform or Gaussian noise for grayscale), feed the **corrupted** image as input, and compute the loss against the **original** clean image during backpropagation. The network thereby learns to recover structure despite corruption. The decoder used for reconstruction can be borrowed from a separately trained clean-image autoencoder.

Noise injection strategies discussed:
- **Binomial / pixel-flip**: randomly select a proportion of pixels and invert them (black↔white).
- **Uniform noise**: replace selected pixels with a value drawn uniformly from [0, 255].
- **Gaussian noise**: replace selected pixels with a value drawn from N(μ, σ²), where nearby-mean values are more probable.

### 4. Autoencoder Applications Beyond Reconstruction
- **Image colourisation**: grayscale encoder → colour decoder; quality degrades for out-of-distribution scenes (e.g., urban environments when trained on natural scenes).
- **Image inpainting (autofilling)**: mask or erode portions of an image and train to restore them.
- **Speech-to-face synthesis**: combine a speech encoder with a face-image decoder; a 2019 paper demonstrated that gender, approximate age, race, and hair colour could be recovered from 6-second speech clips, illustrating transfer across modalities.
- **Anomaly detection**: a well-trained autoencoder reconstructs normal patterns faithfully; high reconstruction error flags anomalies.
- **Image segmentation**: encoder-decoder architectures label each pixel for scene understanding (e.g., SegNet), applicable to autonomous driving where obstacle presence matters more than object identity.
- **Text translation and feature generation**: encoder-decoder pairing across language autoencoders.

### 5. Cardinality and the Failure of One-Hot Encoding
**One-hot encoding** creates n−1 binary dummy variables for a categorical variable with n categories. This is tractable for small cardinality (e.g., marital status, compass direction) but breaks down when cardinality is in the thousands (e.g., city names, store IDs, movie titles, free-text fields). The resulting data matrix becomes excessively wide and sparse.

### 6. Target Encoding
For high-cardinality categoricals, replace each category value with the **mean of the target variable** computed over all training rows belonging to that category. Example: replace "US citizen" with 0.8 if 80% of US-citizen employees in the training data are currently employed. This produces a single numeric feature per categorical variable, preserving predictive signal without dimensionality explosion. Limitation: the encoding is manually engineered and represents only one possible summary statistic.

### 7. Entity Embedding (Neural Network-Learned Embedding)
Rather than hand-crafting encodings, let the network learn them. For each categorical variable, introduce a small **embedding layer** (a trainable look-up table) that maps each category to a dense vector of length k, where k is a hyperparameter. Numerical variables pass through directly; categorical variables enter through their embedding layers. The concatenated pseudo-input layer feeds into the standard hidden layers. Backpropagation adjusts both the embedding weights and the downstream network weights simultaneously.

Key property: because the embedding is learned end-to-end, it captures task-relevant relationships. Geographically proximate stores, for instance, ended up closer in the learned embedding space in the Rossmann experiment, even though no geographic signal was explicitly provided.

### 8. Embedding Dimension as a Hyperparameter
The length k of the embedding vector is analogous to a context-window size in language models. Too small and the representation is lossy; too large and it overfits or wastes capacity. In practice, values like k=2 (illustrative), k=6 (German states), k=10 (stores, day-of-month) are chosen experimentally.

### 9. Recommendation Systems via Embeddings
Netflix / YouTube-style recommenders embed both users (e.g., 128-d vector) and items (e.g., 64-d vector). These embeddings are jointly learned from observed ratings. At inference, the concatenated (user, item) embedding is fed forward to predict a rating or ranking for unseen user-item pairs, enabling collaborative filtering at billion-user scale.

---

## Algorithms / Architectures Covered

| Technique | Category | Key Idea |
|---|---|---|
| Standard autoencoder | Unsupervised / generative | Symmetric encoder-decoder; latent bottleneck |
| Denoising autoencoder | Self-supervised | Input = corrupted; target = clean; loss on original |
| Cross-modal encoder-decoder | Transfer / generative | Swap encoder/decoder domains (e.g., speech→face) |
| SegNet-style encoder-decoder | Supervised segmentation | Per-pixel class labels; used in autonomous driving |
| One-hot encoding | Feature engineering | n−1 binary dummies; breaks at high cardinality |
| Target encoding | Feature engineering | Replace category with mean(target); single feature per variable |
| Entity embedding | Learned representation | Trainable look-up table; k-d dense vector per category |
| Recommendation embedding | Collaborative filtering | Joint user + item embedding learned from ratings |

---

## Important Intuitions and Examples

**Denoising as supervised learning in disguise**: although the task looks generative, denoising autoencoders are trained with a clear label (the original image). The "corruption then reconstruct" paradigm is what makes them learn robust representations rather than memorising noise.

**Lego block composability**: the encoder-decoder separation enables zero-shot cross-task transfer. The 2019 speech-to-face paper required no new architecture — only substituting a speech encoder for the image encoder before a face decoder.

**Autoencoders vs. PCA**: PCA finds a linear subspace minimising reconstruction error; an autoencoder with non-linear activations finds a non-linear manifold. Both reduce dimensionality, but autoencoders can capture curved structure PCA cannot.

**Rossmann Kaggle case study (2nd place)**: the team created entity embeddings for stores (10-d), day-of-week (6-d), day-of-month (10-d), month (6-d), year (2-d), promotion type (2-d), and German state (6-d). The learned store embeddings clustered geographically — nearby states grouped together in embedding space — without any geographic coordinates in the training data. This demonstrates that embeddings discover latent structure automatically.

**Vectorial advantage over integer encoding**: moving from 1-d integer labels to k-d vectors expands the representable feature space quadratically (k=2 gives 2-d plane vs. a 1-d line), allowing finer discrimination between similar-but-distinct categories.

**SDV / autonomous-vehicle inference**: for real-time scene evaluation, CNN handles single-frame spatial processing at low latency; RNN (or LSTM) variants are needed when temporal context across sequential frames is required to resolve ambiguity (e.g., a distant blur resolving into an obstacle as the vehicle approaches).

---

## Related

- [[deep-learning|Deep Learning]]
- [[transfer-learning|Transfer Learning]]
- [[ensemble-methods|Ensemble Methods]]
- [[ai-paradigms|AI Paradigms]]
