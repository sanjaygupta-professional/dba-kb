---
title: "Deep Learning and Variants — Session 09: CNN from Scratch and Transfer Learning (Hands-On with Google Colab)"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/foundations"]
sources:
  - "_raw/dba-course/Course_05_Deep_Learning_and_Variants/02_Recordings_and_PPTs/Session_09_13Dec2025/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "A hands-on lab session building a CNN image classifier from scratch and then applying transfer learning using MobileNet and VGG16 on a brain tumor MRI dataset in Google Colab."
---

# Deep Learning and Variants — Session 09: CNN from Scratch and Transfer Learning

**Instructor**: Dr. Srinivasa Varadharajan (Rajan)
**Date**: 2025-12-13
**Course**: [[course-05-overview-deep-learning-and-variants|Deep Learning and Variants]] (Course 05)

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=ySFUr8Ux8xE)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/IgCPi0AdeeGVTpmiwaJtnwBsAUZPqTYJMfE43Fri5XHY2go?e=5OgRAJ)
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/64249/393713/1188614/5923270)

## Key Concepts

**1. Google Colab as a Cloud IDE for Deep Learning**
Colab (colab.research.google.com) provides a browser-based Jupyter notebook environment backed by a Google-managed cloud VM. Free tier allocates ~13 GB RAM and ~100 GB disk on CPU/GPU/TPU runtimes. Each user session gets an isolated VM; mounting Google Drive (`drive.mount('/content/drive')`) is essential to persist dataset paths across sessions — without mounting, all uploaded data is lost when the kernel disconnects.

**2. Google Drive Mounting and Data Path Management**
After `from google.colab import drive; drive.mount('/content/drive')`, the drive appears under `/content/drive/MyDrive/`. Dataset folders must reside in "My Drive" (not shared drives) for the path to resolve. The three-dot context menu on any folder in the file panel provides a "Copy path" shortcut. Sharing a Colab notebook does not transfer its data paths; each student must save their own copy (`File > Save a copy in Drive`) and update the `root_path` variable accordingly.

**3. Image Preprocessing Pipeline**
Images are read from positive/negative label folders, resized to a uniform spatial dimension (128×128 for the custom CNN; 224×224 or 256×256 for the transfer learning model), and stored as NumPy arrays. Tensor shape convention is `(height, width, channels)` — channels=3 for RGB, channels=1 for grayscale. Lists are converted to `np.array()` before feeding into Keras. Labels are one-hot encoded (or binary-encoded 0/1) using `LabelEncoder` to enable numerical prediction.

**4. Custom CNN Architecture with Keras Sequential API**
The hand-built model uses `model = Sequential()` and stacks three convolutional blocks:
- Block 1: `Conv2D(32, (3,3), activation='relu')` → BatchNormalization → MaxPooling2D
- Block 2: `Conv2D(64, (3,3), activation='relu')` → BatchNormalization → MaxPooling2D
- Block 3: `Conv2D(128, (3,3), activation='relu')` → BatchNormalization → MaxPooling2D

After the three blocks, the output is flattened, passed through a Dense layer with ReLU, then a Dropout layer (for regularisation), and finally a Dense output layer. For binary classification, sigmoid is the correct output activation (not softmax, which is for multi-class); the model nonetheless works with softmax since the argmax still picks the higher-probability class.

**5. Hyperparameter Tuning in Practice**
`model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])` sets learning dynamics. `model.fit()` accepts `epochs`, `batch_size` (typically 32 or 16), and `validation_split` (0.2 = 80/20 train-validation). With only ~50 samples, training accuracy can reach 100% by epoch 10 while validation accuracy collapses to 40–45% — a clear overfitting signal driven by insufficient data. Remedies discussed: increase dataset size, reduce dropout ratio (0.5 is too aggressive for a small network — 0.3 was suggested), tune epochs. Epoch count of 10 is insufficient for real-world data but appropriate for a small exploration dataset.

**6. Batch Normalisation and Dropout Roles**
Batch normalisation normalises the output of each hidden layer (mean=0, variance=1 across the mini-batch), stabilising and accelerating training. It is applied after every convolutional layer before activation in this architecture. Dropout randomly deactivates a fraction of neurons during each forward pass to prevent co-adaptation and overfitting; the rate hyperparameter (here 0.5) controls the proportion killed. For small networks, a high dropout rate can itself degrade performance by killing too many neurons.

**7. MaxPooling and Dimensional Reduction**
After each convolutional block, `MaxPooling2D` downsamples the feature map by selecting the maximum value in each pooling window. This reduces spatial dimensions by half per pool, cutting computational load for subsequent layers while preserving the most salient features detected by the filters. Rajan explicitly connected this to the DenseNet intuition: without pooling, every downstream node must process the full feature map from all upstream nodes — the computational cost grows quadratically.

**8. Transfer Learning: Using a Pre-Trained Model**
Instead of designing layers and initialising weights from scratch, transfer learning loads a model whose weights were already learned on a large classification task (e.g., MobileNet, VGG16 — both available via `tensorflow.keras.applications`). Setting `base_model.trainable = False` freezes all pre-trained weights; the model is used purely as a fixed feature extractor. Only the data is passed through it and predictions are read off — no weight update occurs in the base model. This dramatically reduces compute requirements compared to training from scratch, because the representation learning (edge detection, texture patterns, shape hierarchies) is already encoded.

**9. MobileNet vs. VGG16 as Base Models**
Both are convolutional image classification architectures downloadable from TensorFlow/Keras applications. MobileNet is lightweight (depth-wise separable convolutions, optimised for mobile/edge). VGG16 is deeper and more parameter-heavy. Neither is pre-trained specifically on brain tumour data — they transfer general image feature representations. The selection criterion is empirical: run each, compare validation accuracy on your specific dataset, and keep the better performer. Switching between them requires a one-line change in the base model import.

**10. Gradio for Interactive Web Demo**
After training, a Gradio interface (`gr.Interface(fn=predict_fn, inputs=gr.Image(), outputs=gr.Label())`) wraps the `predict_tumor()` function into a browser-accessible web app. Launching it inside Colab produces both an in-notebook widget and a shareable public URL. The demo accepts an uploaded MRI image, runs the CNN forward pass, and returns a label ("Tumor"/"Normal") with a confidence score (the sigmoid/softmax probability). Gradio is noted as appropriate for exploration only — not for production or proprietary clinical data.

**11. Security Considerations: Colab vs. Enterprise Alternatives**
Colab is open-source infrastructure; data uploaded to it is exposed to Google's systems. For proprietary datasets (medical records, clinical trial data, business-sensitive images), the correct approach is a private or hybrid cloud VM (Azure VM, AWS SageMaker, or similar PaaS/IaaS options). Rajan explicitly advised: "for security we will not use Colab first of all."

## Algorithms / Architectures Covered

| Architecture / Technique | Role in Session | Key Setting |
|---|---|---|
| Custom CNN (Keras Sequential) | Built from scratch; baseline model | 3 Conv2D blocks (32→64→128 filters), ReLU, 10–30 epochs |
| Batch Normalisation | Stabilise layer outputs | After every Conv2D layer |
| MaxPooling2D | Spatial downsampling / feature compression | 2×2 pool, applied after each BN layer |
| Dropout | Regularisation to combat overfitting | Rate=0.5 (too high for small nets; 0.3 suggested) |
| MobileNet (pre-trained) | Transfer learning base model (frozen) | `trainable=False`, input 224×224 |
| VGG16 (pre-trained) | Alternative transfer learning base | Swapped in via `keras.applications.VGG16` |
| Adam optimiser | Gradient-based weight update | Default learning rate |
| Binary cross-entropy | Loss function for 2-class labels | Matched with sigmoid output |
| Gradio | Interactive inference UI | Wraps prediction function as web app |

## Important Intuitions and Examples

**Why transfer learning cuts compute**: Training DenseNet-style layers means each node at depth N aggregates from all N-1 preceding nodes — an O(N²) dependency graph. A pre-trained model has already solved this; re-using frozen weights means a single forward pass per image at inference, with no backward propagation needed.

**Why overfitting happens here**: The brain tumour dataset contains only ~50 images (positive + negative). With 10 epochs and a 3-block CNN, the model quickly memorises the training set (100% train accuracy) but has seen too few examples to generalise — validation accuracy drops to 40–45%. The fix is more data, not just more epochs. Increasing epochs beyond 20 simply deepens the memorisation.

**Sigmoid vs. Softmax for binary outputs**: Sigmoid produces a scalar probability p for class 1; (1-p) is implicitly the probability for class 0. Softmax over 2 neurons produces the same ranking but normalises two separate logits — functionally equivalent for binary prediction but sigmoid is more semantically correct and computationally leaner.

**Confidence score interpretation**: The Gradio output labelled "confidence" is the raw sigmoid probability. A positive image correctly predicted at 80% means the sigmoid output was 0.80. A small or poorly-trained model often outputs extremes (99% or 1%) on a tiny dataset because the decision boundary is not well-calibrated.

**Image size and power-of-2 convention**: Brain tumour MRI images in the dataset were 512×512 pixels. Resizing to 128×128 (custom CNN) or 256×256 (transfer learning) follows the power-of-2 convention that aligns with GPU memory paging and pooling arithmetic. Compressing 512→256 loses less information than 512→128, justifying the larger input for the pre-trained model where layers already expect richer feature maps.

## Related

- [[deep-learning|Deep Learning]]
- [[transfer-learning|Transfer Learning]]
- [[ensemble-methods|Ensemble Methods]]
- [[ai-paradigms|AI Paradigms]]
