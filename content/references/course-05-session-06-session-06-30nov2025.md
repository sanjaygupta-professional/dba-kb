---
title: "Deep Learning and Variants — Session 06: Image Classification Pipeline on Azure ML Studio (No-Code)"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/foundations"]
sources:
  - "_raw/dba-course/Course_05_Deep_Learning_and_Variants/02_Recordings_and_PPTs/Session_06_30Nov2025/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Hands-on walkthrough of building an end-to-end deep learning image classification pipeline in Azure ML Designer using DenseNet, PyTorch, and no-code drag-and-drop components for the animal-images dataset."
---

# Deep Learning and Variants — Session 06: Image Classification Pipeline on Azure ML Studio (No-Code)

**Instructor**: Dr. Srinivasa Varadharajan (Rajan)
**Date**: 2025-11-30
**Course**: [[course-05-overview-deep-learning-and-variants|Deep Learning and Variants]] (Course 05)

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=RE2UX6rU-0I)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/IgC9Cy5zGPxaSYUFCcFo9RAbAdErpciwr9ACua_rHd_EI0k?e=tZLwbk)
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/64249/393713/1186781/5915029)

## Key Concepts

**1. Deep Learning vs. Machine Learning — Data Type Distinction**
ML algorithms operate on structured (tabular) data: rows and columns in CSV or Excel form. Deep learning targets unstructured data — images, video, audio, raw text (HTML, email, docs). The neural network infers its own input representation from raw pixel or token data, making feature engineering largely implicit.

**2. Training / Validation / Test Split in Deep Learning**
Unlike classical ML where a simple 70/30 or 80/20 train-test split suffices, deep learning requires a three-way split: training, validation, and test. Validation is used within the training loop after each epoch to monitor whether the model is genuinely learning generalised features (analogous to a mock exam before the final test). Cross-validation in classical ML serves a different, within-training purpose and is not directly equivalent.

**3. Epoch and Forward/Backward Pass**
An epoch is one complete traversal of the entire training dataset in both directions: a forward pass (inference) followed by a backward pass (backpropagation and weight update). Deep learning processes the dataset many times — unlike classical ML which visits each sample once — so epoch count is the primary iteration control.

**4. Batch Size**
Rather than passing all training images at once, the model ingests data in mini-batches. Batch size (e.g., 16 or 32) controls how many images are processed per weight-update step. Smaller batches give noisier but more frequent gradient updates; larger batches are computationally cheaper but can reduce generalisation.

**5. Learning Rate and Weight Updation**
The learning rate governs the step size of each weight update during backpropagation. A value of 0.001 is conservative: the model updates slowly, captures fine-grained features, and is less prone to overfitting. A rate of 0.01 trains faster but risks memorising training images rather than learning general features — a direct path to overfitting.

**6. Warm-Up Step Number**
A scheduling mechanism that allows the learning rate to differ for an initial number of iterations before switching to the target rate. Useful when a pre-initialised model (like DenseNet) has a default internal learning rate that should be maintained briefly before a custom rate takes effect.

**7. Early Stopping and Patience**
Early stopping halts training automatically when validation performance ceases to improve, preventing wasted computation and overfitting. The patience hyperparameter defines how many consecutive epochs of no improvement to tolerate before triggering the stop. Setting patience to 0 stops immediately upon stagnation.

**8. Image Augmentation and Transformation**
Raw images must be pre-processed before training: resizing all images to a uniform dimension (default 256×256 pixels), center-cropping to 224×224 to remove background noise, horizontal/vertical flips (to synthetically expand small datasets), grayscale conversion (to reduce compute), and colour jitter. These operations are unified under a single Init Image Transformation component shared across all three splits to ensure consistent preprocessing.

**9. DenseNet — Untrained Model Architecture**
DenseNet is a convolutional neural network architecture used as the learnable model container. When dragged into Azure ML Designer it is initialised as an untrained (empty-weights) model. Its internal architecture — number of hidden layers, parameters, dense connectivity between layers — is fixed by the component; the PyTorch training framework then populates those weights through iterative training.

**10. PyTorch as the Training Framework**
PyTorch is the open-source ML framework used by Azure ML Designer to execute training. It defines the rules and optimisation procedure (loss function, gradient computation, weight update schedule) applied to the DenseNet architecture. PyTorch consumes three inputs: the untrained DenseNet model, the training dataset, and the validation dataset.

**11. Macro vs. Micro Precision/Recall**
For multi-class classification, macro metrics compute performance per class and average equally across classes — sensitive to per-label accuracy regardless of class size. Micro metrics aggregate predictions across all instances and all classes jointly — dominated by the majority class. Macro is preferred when class imbalance exists and per-class understanding matters (e.g., a medical dataset with very few positive cases).

**12. Overfitting Detection via Loss Curves**
PyTorch logs training loss and validation loss per epoch. A healthy model shows both losses decreasing. If training loss continues to drop while validation loss plateaus or rises, the model has crossed into overfitting: it is memorising specific images rather than extracting transferable features. This curve is the primary diagnostic for setting the early-stop threshold.

## Algorithms / Architectures Covered

| Name | Type | Key Property |
|---|---|---|
| ANN (Artificial Neural Network) | Deep Learning architecture | General-purpose; baseline multilayer perceptron |
| CNN (Convolutional Neural Network) | Deep Learning architecture | Spatial feature extraction via convolutional filters; suited to image data |
| RNN (Recurrent Neural Network) | Deep Learning architecture | Maintains sequential memory; used for text and time-series prediction |
| DenseNet | CNN variant (pre-built, untrained) | Dense connectivity: each layer receives feature maps from all preceding layers; used as the classifier in this session |
| PyTorch Model (train component) | Training framework | Open-source optimisation engine; provides backpropagation, loss computation, epoch management |

## Important Intuitions & Examples

**Pipeline as a Reusable Template**
The Azure ML Designer pipeline built in this session — animal-images dataset → Convert to Image Directory → Split Image Directory (×2) → Init/Apply Image Transformation (×3) → Train PyTorch Model (DenseNet) → Score Image Model → Evaluate Model — is architecture-agnostic. Swapping the data source (e.g., replacing animal images with a brain-tumour dataset from Kaggle) is the only change required; the rest of the graph remains valid for any image-classification task.

**Validation as a Mock Exam**
Rajan used the analogy directly: training data is the full syllabus; validation data is a mock test taken before the final exam (test data). Validation reveals mid-training whether the model is truly internalising feature patterns — not just memorising answers — and drives weight corrections accordingly.

**Scored Output and Probability Scores**
After the Score Image Model component runs, each test image receives a probability distribution over classes. For a three-class problem (cat, dog, frog), a test image assigned probabilities (cat: 0.19, dog: 0.07, frog: 0.72) is labelled "frog" because 0.72 is the argmax. The demo dataset of 30 images (10 per class) yielded 3 test images (90/10 split), all classified correctly — an Evaluate Model accuracy of 100%.

**Inference Mode on Apply Image Transformation**
The mode setting (training vs. inference) on each Apply Image Transformation block is critical. The training block signals that augmentations (flips, jitter) should be applied. Both the validation and test blocks must be set to inference, meaning only deterministic transforms (resize, crop, normalise) are applied — no random augmentations, because those would corrupt the evaluation signal.

**CPU vs. GPU Compute in Azure ML**
Student-tier Azure subscriptions allow CPU compute clusters only (e.g., Standard DS3v2: 4 cores, 14 GB RAM, 28 GB storage, ~$0.25/hr). For large image datasets (thousands of images), GPU compute is required and available under pay-as-you-go or enterprise licensing. Compute clusters are the primary credit consumer and should be deleted or stopped after each run.

## Related

- [[deep-learning|Deep Learning]]
- [[transfer-learning|Transfer Learning]]
- [[ensemble-methods|Ensemble Methods]]
- [[logistic-regression|Logistic Regression]]
- [[linear-regression|Linear Regression]]
- [[ai-paradigms|AI Paradigms]]
