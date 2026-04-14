---
type: concepts-index
course: "[[Deep Learning and Variants]]"
course_id: course_05
tags: [dba, course_05, concepts, index, MOC]
created: 2026-04-12
source: lecture transcripts (Sessions 1–15) + PDFs for S01, S02
---

# Course 05 — Deep Learning and Variants · Concepts Index

> Chronological concept index across all 15 sessions. Each concept shows the
> first-appearance timestamp in its session transcript, followed by a concise
> one-line gloss framed around what the professor actually emphasised.

**Course**: [[Deep Learning and Variants]]
**Sessions**: 15 · **Date range**: 2025-11-15 → 2026-01-11
**Source**: transcripts in `02_Recordings_and_PPTs/Session_XX_*/transcript.txt`

## Reading guide

- Timestamps like `[HH:MM]` map to the transcript file of that session — open `transcript.txt` and search `[HH:MM]` to jump to the moment.
- Concept order is **lecture order**, not alphabetical — this mirrors how the professor built the narrative.
- Each session block ends with a short "what carries forward" linkage to the next session, to make the arc visible.

## Narrative arc across the course

```
S01–S02  Foundations: biological neuron → perceptron → MLP
S03–S05  Training deep networks: backprop, GD variants, vanishing gradients, regularisation, optimisers
S06      Hands-on: image classification via Azure ML Studio (applied tour)
S07–S08  Autoencoders: dimensionality reduction, denoising, entity embeddings
S09–S12  CNNs: from conv primitives → full architectures → transfer learning → object detection
S13      RNNs and LSTMs for sequential data
S14      Generative models (VAE, GAN) + Reinforcement Learning introduction
S15      Applied NLP with LLMs, RAG, vector databases
```

---

## Session 01 — 2025-11-15
**Topic:** Neural networks, deep learning, and artificial intelligence fundamentals

1. **Data Science** `[64:01]` — Foundation combining statistics, probability, calculus, programming and domain expertise; the alphabet of artificial intelligence.
2. **Machine Learning** `[65:00]` — Field of building mathematical models that determine input-output relationships without explicit programming through learning from data.
3. **Supervised Learning** `[92:12]` — Learning method where desired output labels are provided for inputs during training; system adjusts parameters based on accuracy feedback.
4. **Unsupervised Learning** `[99:42]` — Learning method where system discovers patterns and clusters without explicit labels; only given similarity metric, not desired outputs.
5. **Deep Learning** `[68:18]` — Machine learning method using models modelled after neural systems; subset of ML using neurons as the foundational model.
6. **Artificial Intelligence** `[69:07]` — Man-made systems that can behave like humans; broader than ML, including agentic systems beyond neural mimicry.
7. **Synapse** `[126:44]` — Junction between neurons where communication occurs chemically through neurotransmitters; strength determines synaptic connections.
8. **Neurotransmitters** `[129:27]` — Chemicals released at synapses when electrical impulses travel through the axon; signal transmission between neurons.
9. **Threshold** `[132:50]` — Critical level in neurons; if background activity plus input exceeds threshold, neuron fires; mechanism for discriminating signal from noise.
10. **Hebbian Learning** `[144:38]` — Synaptic strength increases when neurons repeatedly receive inputs through a particular synapse; "neurons that fire together wire together."
11. **Perceptron** `[160:01]` — Mathematical model of a single biological neuron with inputs, weights, summation, activation function and thresholding.
12. **Weights** `[157:02]` — Parameters representing synaptic strength; input values multiplied by weights in weighted linear combination within the neuron.
13. **Bias** `[161:48]` — Background activity term in perceptron; baseline neuron activity independent of inputs.
14. **Activation Function** `[158:36]` — Function applied to weighted sum; sigmoid for classification, linear for regression; enables nonlinear processing.
15. **Single Layer Neural Network** `[170:22]` — Network with input layer, one hidden layer of neurons, and output layer; multiple neurons enable nonlinear classification.
16. **Universal Approximation Theorem** `[168:49]` — Any classification problem can be solved with sufficient neurons in a single hidden layer.
17. **Hidden Layer** `[170:21]` — Layer of neurons between input and output layers; processes intermediate representations.
18. **Dense Neural Network** `[174:01]` — Every neuron in a layer connects to every neuron in adjacent layers; fully connected architecture.
19. **Feed Forward Neural Network** `[176:09]` — Information flows only forward from input to output; no backward or sideways flow.
20. **Deep Neural Network** `[171:16]` — Network with more than two hidden layers; enables solving complex nonlinear problems — the locus of "deep learning."

> **Carries forward to S02:** perceptron internals (weights, bias, transfer/activation) are formalised mathematically; XOR exposes the single-layer limitation → motivates MLP.

---

## Session 02 — 2025-11-16
**Topic:** Perceptron architecture formalised; multi-layer networks as a response to XOR

1. **Hebbian Learning** `[05:50]` — Synapses strengthen based on input frequency; stronger weights for inputs generating consistent outputs.
2. **Weights and Synaptic Strength** `[06:42]` — Mathematical representation of synapse strength; the primary learnable parameters.
3. **Transfer Function** `[07:35]` — Linear combination of bias plus weighted inputs; computed before activation.
4. **Activation Function** `[07:46]` — Nonlinear transformation applied to the transfer function; sigmoid, identity, tanh options.
5. **Perceptron** `[08:04]` — Single neuron combining weighted inputs, bias, transfer and activation functions.
6. **Bias Term** `[08:54]` — Baseline neuronal activity modelling constant offset; critical for expressiveness.
7. **Vector Notation** `[10:44]` — Representing inputs and weights as vectors enabling scalar-product form; facilitates matrix ops.
8. **Scalar Product** `[11:37]` — Dot product of weight and input vectors; compact form of the weighted summation.
9. **Linear Regression** `[17:35]` — Perceptron with identity activation producing continuous predictions; a special case.
10. **Cost Function** `[33:23]` — Sum-of-squared-errors objective quantifying prediction discrepancy; basis for optimisation.
11. **Gradient Descent** `[39:06]` — Iterative optimisation moving parameters opposite to the gradient, toward the cost minimum.
12. **Logistic Regression** `[55:27]` — Perceptron with sigmoid activation for binary classification; output bounded in [0, 1].
13. **Maximum Likelihood Estimation** `[55:42]` — Parameter estimation that maximises observed-data probability; used in classification.
14. **XOR Problem** `[57:50]` — Classic nonlinear-separability challenge; single perceptron cannot solve it → motivates multi-layer.
15. **Hidden Layer** `[64:39]` — Intermediate layer enabling nonlinear feature representations; key to deep networks.
16. **Multi-Layer Perceptron** `[65:00]` — Stacked perceptron layers learning complex nonlinear decision boundaries.
17. **Likelihood Function** `[109:14]` — Probability of observed data given parameters; maximised to find optimal parameters.
18. **Convex Function** `[135:06]` — Cost landscape with a single global minimum enabling reliable gradient-based convergence.
19. **Gradient** `[140:12]` — Vector of partial derivatives indicating the steepest-cost-increase direction; inverted for descent.
20. **Partial Derivative** `[145:30]` — Rate of change of a function w.r.t. one variable with others held constant; a component of the gradient.

> **Carries forward to S03:** with MLP on the table, the question becomes *how* to train multi-layer nets — hello backpropagation and chain rule.

---

## Session 03 — 2025-11-22
**Topic:** Deep neural networks, backpropagation, and gradient descent fundamentals

1. **Perceptron** `[03:49]` — Recap: single neuron with weighted inputs, bias, activation.
2. **Multi-layer Perceptron** `[03:49]` — Multiple neurons in layers solving problems beyond single-neuron capacity.
3. **Activation Functions** `[05:20]` — Sigmoid, ReLU, tanh: nonlinear transformations enabling complex modelling.
4. **Weight and Bias Parameters** `[04:32]` — Weights scale inputs; biases capture background neuron activity.
5. **Transfer Function** `[05:06]` — Linear combination preceding activation; determines raw neuron output.
6. **Gradient Descent** `[17:25]` — Moves parameters opposite to the cost gradient with a learning-rate step.
7. **Cost Function** `[15:27]` — Objective measuring prediction error; minimisation drives training.
8. **Fully Connected Dense Network** `[40:13]` — Every neuron connects to all neurons in adjacent layers.
9. **Deep Neural Network** `[37:23]` — Three or more layers enabling hierarchical feature learning.
10. **Forward Propagation** `[63:00]` — Inputs flow through layers sequentially to produce predictions.
11. **Backpropagation** `[121:10]` — Chain-rule gradients from output error backward through layers to update weights.
12. **Chain Rule Derivatives** `[72:00]` — Gradient of composed functions through layer-wise partial derivatives.
13. **Learning Rate** `[19:00]` — Step-size hyperparameter controlling convergence speed and stability.
14. **Online Weight Update** `[123:55]` — Gradient step after each data point — rapid but noisy.
15. **Batch Processing** `[126:01]` — Gradient over the entire dataset before updates — stable but costly.
16. **Mini-batch Gradient Descent** `[128:09]` — Compromise using random subsets; the practical default.
17. **Epoch** `[129:41]` — One complete pass over the training dataset.
18. **Vanishing Gradient Problem** `[160:35]` — Sigmoid derivatives become tiny across layers, stalling learning in early layers.
19. **Overfitting** `[163:18]` — Memorising noise rather than patterns — the motivation for regularisation.

> **Carries forward to S04:** vanishing gradients and overfitting are named → S04 will bundle regularisation (incl. dropout) with training fundamentals.

---

## Session 04 — 2025-11-23
**Topic:** Deep neural network training, challenges, and regularisation

1. **Neuron Model** `[06:09]` — Biological neuron decomposed into inputs, weights, bias, transfer and activation.
2. **Bias** `[06:45]` — Background activity signal, denoted *b*.
3. **Weight** `[07:01]` — Parameters multiplied with input features in the weighted sum.
4. **Transfer Function** `[07:27]` — Linear combination before activation.
5. **Activation Function** `[07:44]` — Nonlinear transformation of transfer output.
6. **Sigmoid Activation** `[07:54]` — Logistic function for binary classification.
7. **Identity Activation** `[08:13]` — Linear activation for regression.
8. **Universal Approximation** `[10:13]` — Enough neurons in a single layer can represent any continuous function.
9. **Overfitting (single wide layer)** `[10:53]` — Risk of using too many neurons in one layer despite expressivity.
10. **Multi-layer Networks** `[11:11]` — Two layers build stronger nonlinearity than one wide shallow layer.
11. **Backpropagation** `[12:23]` — Error propagated backward through layers to adjust weights.
12. **Gradient Descent** `[13:07]` — Move parameters opposite the gradient by a learning-rate step.
13. **Learning Rate** `[13:33]` — Controls update magnitude.
14. **Online Updating** `[15:43]` — Per-sample updates — immediate feedback, slow.
15. **Batch Updating** `[18:23]` — Whole-set updates — efficient per-step but fewer updates.
16. **Mini-Batch Updating** `[19:20]` — Small chunks — the practical sweet spot.
17. **Epoch** `[16:47]` — One full pass through training data.
18. **Convergence** `[16:20]` — Stopping when gradient ≈ 0 or tolerance hit.
19. **Deep Neural Networks** `[21:27]` — >2 hidden layers for complex nonlinear problems.
20. **Image Flattening** `[26:52]` — Convert 2D image matrix to 1D vector for DNN input.
21. **Dropout** `[169:00]` — Randomly drop connections during training to prevent co-adaptation.
22. **Regularisation** `[171:17]` — Moves models away from overfitting toward better generalisation.

> **Carries forward to S05:** dropout introduced briefly → S05 formalises the full regularisation + optimiser toolkit.

---

## Session 05 — 2025-11-29
**Topic:** Deep learning optimisation and regularisation techniques

1. **Vanishing Gradients** `[04:23]` — Chained derivatives through saturating activations drive gradients to zero.
2. **Sigmoid Activation Function** `[07:05]` — Derivative max 0.25 — multiplying across deep layers vanishes.
3. **Rectified Linear Unit (ReLU)** `[08:46]` — Linear for positive, zero for negative — fixes vanishing gradients.
4. **Mini-Batch Gradient Descent** `[10:01]` — Updates per mini-batch; data-quality variation causes zigzag paths.
5. **Exponential Moving Average** `[11:10]` — Time-series smoothing treating epochs as indices.
6. **Momentum** `[11:06]` — EMA of gradients accelerating convergence toward the minimum.
7. **Learning Rate Decay** `[12:15]` — Systematically shrink the step size (exponential / step-wise).
8. **Root Mean Square Propagation (RMSprop)** `[15:51]` — Normalise LR by EMA of gradient variance — parameter-specific steps.
9. **Xavier Initialization** `[17:46]` — Uniform init based on neuron counts to keep gradients flowing.
10. **Regularisation** `[18:42]` — Loss + complexity term with a hyperparameter balancing fit vs. generalisation.
11. **Dropout** `[18:56]` — Stochastic neuron deactivation prevents overfitting.
12. **Batch Normalisation** `[18:58]` — Normalise layer inputs to reduce internal covariate shift.
13. **Ridge Regression** `[82:32]` — L2 penalty shrinks parameters gradually; handles multicollinearity.
14. **Lasso Regression** `[84:30]` — L1 penalty drives parameters exactly to zero — implicit feature selection.
15. **Elastic Net** `[92:46]` — L1 + L2 combined via alpha.
16. **Adaptive Moment Estimation (Adam)** `[167:07]` — Momentum + RMSprop — robust default optimiser.

> **Carries forward to S06:** theoretical toolkit is in place → S06 is the hands-on "do it in Azure ML" tour.

---

## Session 06 — 2025-11-30
**Topic:** Applied image classification via Azure ML Studio

1. **Deep Learning** `[07:04]` — ML subfield using neural nets to learn patterns.
2. **Artificial Intelligence** `[08:38]` — Technique for machines to behave like humans.
3. **Supervised Machine Learning** `[12:23]` — Labelled data for classification/prediction.
4. **Unsupervised Machine Learning** `[12:44]` — Unlabelled data; clustering-style grouping.
5. **Neural Networks** `[14:37]` — Biologically-inspired compute — the DL foundation.
6. **Artificial Neural Networks (ANN)** `[15:05]` — Input + hidden + output layers.
7. **Convolutional Neural Networks (CNN)** `[15:07]` — Specialised for images via conv filters.
8. **Recurrent Neural Networks (RNN)** `[15:21]` — Sequential data with memory.
9. **Image Classification** `[16:03]` — Automatically categorising objects in images.
10. **Generative AI** `[17:05]` — DL that generates text/images and understands relationships.
11. **Data Preprocessing** `[18:14]` — Unstructured → structured, ready for training.
12. **Data Split** `[50:38]` — Train/test partition for proper evaluation.
13. **Backpropagation** `[08:22]` — Weight updates from output error.
14. **Training Data** `[42:45]` — Portion used to teach the model.
15. **Validation Data** `[44:17]` — Portion monitored during training to prevent overfitting.
16. **Hyperparameters** `[88:40]` — Epochs, batch size, LR — control training behaviour.
17. **Epoch** `[88:46]` — Complete pass with forward + backward propagation.
18. **Batch Size** `[90:28]` — Samples per iteration — affects memory/compute.
19. **Learning Rate** `[92:03]` — Step size for weight updates.
20. **Early Stopping** `[96:36]` — Halt when validation stops improving.
21. **Overfitting** `[167:01]` — Memorises training data rather than generalising.

> **Carries forward to S07:** with applied CNN intuition, the arc returns to architecture — first via autoencoders for unsupervised representation learning.

---

## Session 07 — 2025-12-06
**Topic:** Autoencoders, dimensionality reduction, and PCA foundations

1. **Deep Neural Networks** `[17:20]` — >2 hidden layers; deep learning via parameter optimisation.
2. **Vanishing Gradient Problem** `[22:03]` — Sigmoid-derivative decay across layers during backprop.
3. **ReLU Activation Function** `[25:01]` — Linear thresholding fix for vanishing gradients.
4. **Mini-batch Gradient Descent** `[26:27]` — Small-subset updates — efficiency sweet spot.
5. **Epoch** `[27:38]` — One pass through the training set.
6. **Learning Rate Scheduling** `[29:00]` — Step / exponential decay across epochs.
7. **Momentum** `[31:00]` — EMA of gradients smoothing the optimisation path.
8. **RMSprop** `[29:54]` — LR normalised by gradient-variance EMA.
9. **Adam Optimizer** `[33:39]` — Industry-standard Momentum + RMSprop.
10. **Parameter Initialization** `[34:37]` — Proper random init is necessary for convergence.
11. **Regularisation** `[35:18]` — Complexity vs. performance balance.
12. **Dropout Regularisation** `[36:03]` — Stochastic zeroing promotes generalisation.
13. **Batch Normalisation** `[39:49]` — Layer-input standardisation prevents scale dominance.
14. **Autoencoder** `[50:24]` — Mirror-symmetric net reconstructing input — unsupervised feature learner.
15. **Encoding/Embedding** `[62:22]` — Compact hidden-layer vector capturing input essence.
16. **Dimensionality Reduction** `[64:14]` — High-dim → low-dim via neural compression.
17. **Principal Component Analysis (PCA)** `[103:01]` — Linear DR — uncorrelated components ordered by variance.
18. **Covariance Matrix** `[121:10]` — Square symmetric — encodes pairwise covariances.
19. **Eigenvectors and Eigenvalues** `[130:12]` — Scale-only vectors + variance along them.
20. **Linear Combinations** `[140:41]` — PCs as weighted sums of original variables.

> **Carries forward to S08:** autoencoder is the vehicle → S08 expands into denoising, colourisation, inpainting, entity embeddings.

---

## Session 08 — 2025-12-07
**Topic:** Autoencoders: denoising, applications, and entity embeddings

1. **Autoencoders** `[11:50]` — Symmetric encoder + decoder learning to reconstruct input.
2. **Encoding/Embedding** `[14:14]` — Compact representation via the encoder half.
3. **Latent Space Representation** `[31:34]` — Bottleneck-layer compressed data manifold.
4. **Dimensionality Reduction** `[16:36]` — Nonlinear PCA equivalent via autoencoder.
5. **Denoising Autoencoders** `[21:28]` — Trained to recover clean signal from corrupted input.
6. **Image Colorization** `[32:04]` — Grayscale → colour via learned colour priors.
7. **Image Inpainting** `[33:31]` — Regenerate eroded patches from undamaged training data.
8. **Encoder-Decoder Lego Blocks** `[15:15]` — Mix-and-match encoders/decoders → e.g., machine translation.
9. **Convolutional Neural Networks (CNN)** `[30:16]` — Preview — covered properly next session.
10. **Image Segmentation** `[54:51]` — Encoder-decoder for per-object separation (autonomous, assistive).
11. **One-Hot Encoding** `[88:22]` — n categories → n binary inputs.
12. **Cardinality** `[93:09]` — # distinct categories; high cardinality breaks one-hot.
13. **Target Encoding** `[94:07]` — Replace category with its target-variable average.
14. **Entity Embeddings** `[110:18]` — Network-learned vector representations of categorical variables.
15. **Embedding Layer** `[123:17]` — Dedicated layer learning category vectors before hidden layers.
16. **Recommendation Systems** `[133:24]` — Users + items as entity embeddings; similarity for matching.

> **Carries forward to S09:** embeddings and encoders primed → jumping into CNNs with a real classification lab.

---

## Session 09 — 2025-12-13
**Topic:** Building a CNN from scratch + transfer learning for brain-tumour classification

1. **Google Colab** `[38:15]` — Free cloud IDE with CPU/GPU/TPU for running DL models.
2. **Image Preprocessing** `[126:08]` — Resize + convert to arrays for network input.
3. **One-Hot Encoding** `[126:18]` — Categorical labels → binary numerical form.
4. **Sequential Model** `[126:49]` — Keras layer-by-layer API.
5. **Convolutional Layer 2D** `[127:11]` — Filters (32/64/128) extracting spatial features.
6. **Activation Function (ReLU)** `[130:16]` — Non-linearity enabling complex pattern learning.
7. **Batch Normalisation** `[131:11]` — Stabilises training, reduces covariate shift.
8. **Max Pooling** `[131:15]` — Local-region max downsampling.
9. **Flatten Layer** `[130:16]` — 2D feature maps → 1D vector for dense layers.
10. **Dense Layer** `[130:08]` — Fully connected — final classification head input.
11. **Dropout** `[131:27]` — Stochastic deactivation for regularisation.
12. **Sigmoid Activation** `[131:49]` — Binary classification probability output.
13. **Adam Optimizer** `[132:13]` — Adaptive weight-update algorithm.
14. **Cross-Entropy Loss** `[132:20]` — Classification loss between predicted and actual distributions.
15. **Epoch** `[132:56]` — Full dataset pass.
16. **Batch Size** `[133:02]` — Samples per weight update.
17. **Validation Split** `[133:06]` — 80/20 train/validation typical.
18. **Overfitting** `[134:35]` — High train accuracy, low validation accuracy.
19. **Transfer Learning** `[149:34]` — Use pre-trained weights; reduces compute, boosts small-data performance.
20. **Fine-tuning** `[191:30]` — Retrain outer layers while keeping feature extractors.

> **Carries forward to S10:** practitioner's view is in hand → S10 drops back to *why* convolution works (visual cortex analogy).

---

## Session 10 — 2025-12-14
**Topic:** Visual perception in machines and convolution fundamentals

1. **Computer Vision** `[54:17]` — Machines processing and understanding images/video.
2. **Photoreceptors** `[69:00]` — Retinal rods and cones detecting different colours.
3. **Image Representation** `[87:10]` — Images as RGB-pixel matrices (0–255).
4. **Grayscale Conversion** `[88:13]` — Combine RGB channels into single brightness values.
5. **Binary Image** `[88:44]` — Thresholded grayscale — black or white only.
6. **Image Processing** `[90:11]` — Math on pixels — rotation, scaling, inversion.
7. **Matrix Operations** `[92:02]` — Geometric transformations via matrix multiplication.
8. **Spatial Information Processing** `[98:45]` — Low/high-frequency features across scales.
9. **Simple Cells** `[153:35]` — Neurons detecting oriented features in specific spatial regions.
10. **Complex Cells** `[156:10]` — Combine simple-cell outputs into shape/orientation features.
11. **Hierarchical Feature Extraction** `[160:09]` — Simple → composite — the cortical layering metaphor.
12. **Convolutional Neural Networks** `[158:59]` — Mimic hierarchical visual processing.
13. **Convolution Process** `[162:18]` — Slide a window extracting local features per region.
14. **Filter (Kernel)** `[169:21]` — Matrix specifying *what* to extract in each region.
15. **Cell-wise Multiplication** `[174:02]` — Element-wise product of filter × patch.
16. **Feature Aggregation** `[178:26]` — Sum / max-pool the products into compact features.

> **Carries forward to S11:** with the convolution primitive understood, S11 assembles it into full CNN architectures (AlexNet et al.).

---

## Session 11 — 2025-12-20
**Topic:** Convolutional neural networks: architecture, filters, pooling, and milestones

1. **ImageNet Dataset** `[25:35]` — 14M annotated images across 20k+ categories — the CNN benchmark.
2. **Convolutional Neural Networks** `[28:09]` — Conv-based hierarchical feature extractors for images.
3. **Neocognitron** `[44:19]` — Early biologically-inspired CNN — contrast → edges → orientations.
4. **Feature Learning** `[48:05]` — Networks learn features automatically, not by hand-crafting.
5. **Convolution Operation** `[49:37]` — Filter superimposed → element-wise multiply → sum.
6. **Feature Extraction** `[50:29]` — Filters detect diagonals, edges, specific patterns.
7. **Stride** `[54:25]` — Pixel step when sliding the filter — affects output dims.
8. **Feature Maps** `[56:09]` — Output matrices of conv layers (aka feature extractors).
9. **Sparse Connectivity** `[66:04]` — Local connections only — massive parameter reduction vs. dense.
10. **Neuron as Filter** `[61:04]` — A CNN neuron has fixed weights acting as a filter.
11. **Hyperparameters** `[69:30]` — Filter size, count, stride, pooling — design knobs.
12. **Multiple Filters** `[72:55]` — Many filters per layer for diverse feature extraction.
13. **Pooling Layers** `[83:22]` — Spatial downsampling — cuts parameters and compute.
14. **Max Pooling** `[85:10]` — Take the max — preserves strongest activations.
15. **Padding** `[95:28]` — Border pixels preserve spatial dims when needed.
16. **Flattening** `[99:09]` — 3D feature maps → 1D vectors for dense layers.
17. **Fully Connected Layers** `[154:01]` — Final dense classifier layers.
18. **ReLU Activation** `[153:35]` — Hidden-layer activation replacing sigmoid.
19. **AlexNet Architecture** `[154:22]` — 8-layer breakthrough CNN: 5×5 filters, max-pool, dense, ReLU, augmentation.
20. **Batch Normalisation & Dropout** `[153:45]` — Regularisation tandem for deep CNNs.

> **Carries forward to S12:** CNNs are built → now reuse them (transfer learning) and extend them (object detection).

---

## Session 12 — 2025-12-21
**Topic:** Transfer learning and object detection in deep-learning CNNs

1. **Transfer Learning** `[28:01]` — Reuse models trained on large datasets; fine-tune last layers on new tasks.
2. **Feature Extraction** `[35:02]` — Early layers learn edges; deeper layers learn complex features — both are domain-transferable.
3. **Pre-trained Models** `[36:07]` — ImageNet-trained nets adapted without training from scratch.
4. **Fine-tuning Strategy** `[37:20]` — Adjust final layers when data is small; unfreeze more as data grows.
5. **Data Augmentation** `[46:05]` — Synthetic samples (rotate, scale) enlarge small datasets.
6. **Frozen Layers** `[48:53]` — Keep weights constant — exclude from backprop updates.
7. **Object Detection Problem** `[49:31]` — Locate *and* classify multiple objects in one image.
8. **Sliding Window Approach** `[54:56]` — Brute-force multi-size scan — theoretically sound, costly.
9. **Region Proposal** `[56:27]` — Candidate regions first → CNN classification second.
10. **R-CNN** `[55:42]` — Region extraction → per-region CNN classification.
11. **Selective Search Algorithm** `[58:19]` — Hierarchical similar-region grouping for proposals.
12. **YOLO** `[68:29]` — Fast real-time detection — speed-over-precision segmentation.
13. **Semantic Segmentation** `[69:49]` — Per-pixel classification for object boundaries.
14. **Recurrent Neural Networks** `[75:06]` — Feedback-loop nets for sequential data processing.
15. **Neural Network Memory** `[76:38]` — RNN state carries info forward across sequence elements.
16. **Sequential Data Processing** `[77:27]` — Word / frame sequences where prior context matters.
17. **LSTM Networks** `[80:11]` — Extend RNNs for long- and short-term dependencies.

> **Carries forward to S13:** RNN/LSTM teased → S13 gives the full sequential-modelling treatment.

---

## Session 13 — 2026-01-04
**Topic:** Recurrent and Long Short-Term Memory networks for sequential data

1. **Time Series Data** `[44:42]` — Data with temporal dependencies — order matters.
2. **Recurrent Neural Networks (RNN)** `[51:51]` — Feedback connections process sequences.
3. **State Representation** `[64:02]` — Cumulative compressed past — contextual memory.
4. **Feedback Networks** `[68:16]` — Backward connections propagate state through time.
5. **RNN Parameter Sharing** `[83:13]` — Same weights (W, U, V) across every time step.
6. **Backpropagation Through Time (BPTT)** `[88:12]` — Gradients computed across unfolded temporal graph.
7. **Vanishing Gradients Problem** `[97:02]` — Gradients diminish across many time steps.
8. **Tanh Activation Function** `[97:31]` — Squashes state updates into [-1, 1].
9. **Exploding Gradients** `[97:06]` — Controlled via gradient clipping.
10. **Long-Term Dependencies** `[99:10]` — Skip connections keep info flowing across distant steps.
11. **Long Short-Term Memory (LSTM)** `[100:51]` — Gated RNN separating short-/long-term memory paths.
12. **Gating Mechanisms** `[126:45]` — Sigmoid-controlled input/forget/output gates.
13. **Input Gate** `[126:49]` — Controls whether new input modifies cell state.
14. **Forget Gate** `[127:01]` — Controls what past state to retain or discard.
15. **Output Gate** `[127:28]` — Controls exposure of cell state to the next layer.
16. **Cell State** `[128:46]` — Long-term memory channel — preserves gradients.
17. **Context Management** `[119:08]` — Dynamic adjustment of relevant info for prediction.
18. **Sequential vs Structured Data** `[154:55]` — LSTMs: time series (structured) and text (unstructured).

> **Carries forward to S14:** having covered representation + discrimination + sequences, S14 pivots to generation (VAE, GAN) and RL.

---

## Session 14 — 2026-01-10
**Topic:** Generative image models and reinforcement-learning foundations

1. **Discriminative Models** `[30:04]` — Classify or predict — regression, classification, clustering.
2. **Generative Models** `[30:14]` — Learn data distribution to *generate* new samples.
3. **Image Representation** `[36:30]` — Flatten image matrices into vectors of pixel brightness.
4. **Feature Space Distribution** `[40:01]` — Class-specific clusters in feature space — the generation target.
5. **Latent Space Sampling** `[41:32]` — Draw points from learned distributions to generate new data.
6. **Autoencoder Architecture** `[49:41]` — Encoder-decoder reconstruction — prior here.
7. **Variational Autoencoder (VAE)** `[47:44]` — Probabilistic encoder learning mean + std of latent variables.
8. **Probability Distribution Encoding** `[55:31]` — Encoder outputs Gaussian parameters, not points.
9. **Sampling and Decoding** `[59:47]` — Random samples → decoder → synthetic images.
10. **Adversarial Networks (GAN)** `[71:31]` — Implicit modelling via generator-vs-discriminator competition.
11. **Generator Network** `[77:40]` — Transforms noise into synthetic images.
12. **Discriminator Function** `[79:38]` — Real vs. fake classifier — trains both nets.
13. **Adversarial Training** `[83:53]` — Alternating optimisation; discriminator fixed while generator trains.
14. **Reinforcement Learning** `[109:14]` — Agent maximises cumulative reward via environment interaction.
15. **Agent-Environment Interaction** `[116:49]` — Observe state → action → reward → new state loop.
16. **Reward Signal** `[126:28]` — Numerical feedback; positive/negative consequences.
17. **State Representation** `[123:40]` — Environment info relevant for the decision.
18. **Value Function (Q-Function)** `[140:04]` — Expected discounted future reward for state-action.
19. **Policy Learning** `[141:43]` — Choose actions maximising the value function.
20. **Deep Q-Learning** `[148:00]` — Neural-net approximation of value functions for complex state spaces.

> **Carries forward to S15:** neural techniques mostly covered → final session applies them to language (LLMs, RAG).

---

## Session 15 — 2026-01-11
**Topic:** Applied NLP with LLMs and Retrieval-Augmented Generation

1. **NLP Applications** `[16:15]` — Chatbots, semantic search, RAG, NER, sentiment, summarisation.
2. **Conversational AI / Chatbot** `[16:23]` — Interactive natural-language dialogue systems.
3. **Semantic Search and RAG** `[16:26]` — Context-aware retrieval + generation.
4. **Large Language Models (LLM)** `[15:59]` — Foundation models for NLP applications.
5. **Open-Source vs Closed-Source Models** `[17:42]` — Customisable/local vs commercial API-only (ChatGPT, Gemini).
6. **API Integration** `[25:39]` — Cloud API access without local model download.
7. **Groq Platform and API Keys** `[30:22]` — Cloud inference for open-source LLMs with auth.
8. **Hugging Face Hub** `[25:19]` — Repository of thousands of open models/datasets/pipelines.
9. **LangChain Framework** `[89:36]` — Python library for building LLM applications.
10. **Model Parameters and Quantization** `[89:43]` — Model size (e.g., Llama 3 70B) — affects quality + resources.
11. **Token Limits** `[35:43]` — Context-window constraints on input/output length.
12. **Retrieval-Augmented Generation (RAG)** `[118:36]` — Knowledge base embedded alongside LLM — reduces hallucination.
13. **Vector Embeddings** `[140:04]` — Text → numerical vectors encoding semantic meaning.
14. **Vector Database** `[140:35]` — Specialised store for high-dim embeddings — enables similarity search.
15. **Cosine Similarity** `[128:23]` — Angle-based similarity metric for retrieval/matching.
16. **Named Entity Recognition (NER)** `[153:04]` — Identify and classify named entities in text.
17. **Model Local Deployment** `[111:46]` — Self-hosted models for privacy, control, cost efficiency.

---

## Appendix · Master alphabetical index

Jump-to-concept list (session number in brackets). Useful when revising a single topic across the whole course.

- **Activation function** — S01, S02, S03, S04, S05 (sigmoid/ReLU/tanh), S09
- **Adam optimiser** — S05, S07, S09
- **AlexNet** — S11
- **Autoencoder** — S07 (intro), S08 (apps), S14 (as generative prior)
- **Backpropagation** — S03, S04, S06
- **Batch normalisation** — S05, S07, S09, S11
- **Batch / mini-batch / online GD** — S03, S04, S05, S07
- **Bias / weights** — S01, S02, S03, S04
- **Chain rule** — S03
- **CNN** — S06 (named), S08 (preview), S09 (build), S10 (motivation), S11 (architecture), S12 (transfer / detection)
- **Convolution / filter / kernel** — S10, S11
- **Cost / loss function** — S02, S03 (generic), S09 (cross-entropy)
- **Data augmentation** — S12
- **Denoising autoencoder** — S08
- **Dense / fully connected layer** — S01, S03, S09, S11
- **Dimensionality reduction** — S07, S08
- **Dropout** — S04, S05, S07, S09, S11
- **Eigenvectors / eigenvalues** — S07
- **Embedding / encoding** — S07, S08 (entity embeddings), S15 (vector embeddings)
- **Epoch** — S03, S04, S06, S07, S09
- **GAN** — S14
- **Gradient descent** — S02, S03, S04
- **Hebbian learning** — S01, S02
- **Hidden layer** — S01, S02
- **Hyperparameters** — S06, S11
- **Image classification / processing** — S06, S10, S11
- **ImageNet** — S11
- **LangChain** — S15
- **Learning rate (+ decay / scheduling)** — S03, S04, S05, S07, S09
- **LLM** — S15
- **Logistic regression** — S02
- **LSTM** — S12 (preview), S13 (full)
- **Max pooling** — S09, S11
- **MLP / multi-layer perceptron** — S01, S02, S03
- **Momentum** — S05, S07
- **Object detection (R-CNN, YOLO, segmentation)** — S12
- **One-hot / target encoding / cardinality** — S08, S09
- **Overfitting** — S03, S04, S06, S09
- **PCA / covariance matrix** — S07
- **Perceptron** — S01, S02, S03
- **Policy / value function / Q-learning** — S14
- **RAG** — S15
- **Regularisation (L1 / L2 / elastic net)** — S04, S05, S07
- **ReLU** — S05, S07, S09, S11
- **Reinforcement learning** — S14
- **RMSprop** — S05, S07
- **RNN** — S06 (named), S12 (preview), S13 (full)
- **Stride / padding / flatten** — S09, S11
- **Supervised / unsupervised learning** — S01, S06
- **Transfer learning** — S09, S12
- **Transfer function** — S02, S03, S04
- **Universal approximation** — S01, S04
- **VAE** — S14
- **Vanishing gradients** — S03, S05, S07, S13 (in BPTT)
- **Vector / cosine similarity** — S15
- **XOR problem** — S02
- **Xavier initialisation** — S05

---

*Generated 2026-04-12 from transcripts (+ Session 01/02 PDFs). Timestamps reference the `transcript.txt` file inside each session folder. Reopen and search `[HH:MM]` to jump back to the lecture moment.*
