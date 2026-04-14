---
title: "Deep Learning and Variants — Session 11: Convolutional Neural Networks — Architecture, Mechanics, and Landmark Models"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/foundations"]
sources:
  - "_raw/dba-course/Course_05_Deep_Learning_and_Variants/02_Recordings_and_PPTs/Session_11_20Dec2025/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Deep dive into convolutional neural networks: the mechanics of convolution, pooling, padding, and stride; weight sharing; and landmark CNN architectures from LeNet through ResNet, with emphasis on how learned filters replaced hand-engineered features."
---

# Deep Learning and Variants — Session 11: Convolutional Neural Networks — Architecture, Mechanics, and Landmark Models

**Instructor**: Dr. Srinivasa Varadharajan (Rajan)
**Date**: 2025-12-20
**Course**: [[course-05-overview-deep-learning-and-variants|Deep Learning and Variants]] (Course 05)

---

## Key Concepts

### 1. ImageNet as the Gold Standard Benchmark
ImageNet contains over 14 million annotated images across ~21,000 synset categories (with 1 million bounding-box annotations). Originally assembled at Stanford under Fei-Fei Li through crowdsourced human labelling over seven to eight years, it became the definitive benchmark for image classification. The ImageNet Large Scale Visual Recognition Challenge (ILSVRC) is run annually and tracks top-5 error rates across submissions.

### 2. Why Traditional Rules-Based Image Processing Failed to Scale
Pre-deep-learning approaches were expert-driven and hand-crafted: analysts defined explicit mathematical features (edges, orientations, intensity gradients) and wrote rules to match them. The approach was interpretable but brittle — a circle viewed obliquely becomes an ellipse, and enumerating all such geometric transforms grew combinatorially. These methods could not generalize across viewpoints, lighting conditions, or object categories without redesign.

### 3. Convolution as Feature Extraction
A convolution operation slides a filter (kernel) systematically across the input, computing element-wise products and summing them at each position. The filter selectively amplifies certain patterns — e.g., a filter with +1 on the top row and -1 on the bottom row detects horizontal edges; one with +1 on the left column and -1 on the right detects vertical edges. The result (feature map) encodes how strongly each pattern appears at each spatial location.

### 4. Weight Sharing and Sparse Connectivity
In a CNN, the same filter weights are reused at every spatial position. This is fundamentally different from a fully-connected layer, where each neuron maintains independent weights for every input. Weight sharing (a) drastically reduces the number of trainable parameters (e.g., six 5×5 filters → 150 parameters vs. thousands for a dense layer), and (b) encodes translation equivariance — the same feature detector fires wherever the pattern occurs in the image.

### 5. Backpropagation Learns the Filters
A key conceptual shift: filter elements are not pre-designed but are treated as model parameters and learned via backpropagation. The only human decisions are architectural hyperparameters — filter count, filter size, stride, and padding. The network autonomously discovers which filters best minimize task loss, potentially finding features beyond the RGB-tuned constraints of biological vision.

### 6. Convolution Hyperparameters and Output Size Formula
The spatial size of a feature map is determined by:

> Output size = ⌊(Input size − Filter size + 2 × Padding) / Stride⌋ + 1

- **Filter size**: Smaller filters (3×3) capture fine-grained local patterns; 3×3 is the practical minimum for encoding orientation. Odd sizes are preferred because padding can be symmetric: for an n×n filter, pad by (n−1)/2 on each side.
- **Number of filters**: Each filter produces one feature-map channel; this is a key capacity hyperparameter.
- **Stride**: Step size between filter positions. Stride 1 preserves spatial resolution; stride 2+ aggressively downsamples and risks losing intermediate spatial information. Rajan recommends treating stride as a hyperparameter between 1 and 2 only.
- **Padding**: Zero-padding the input boundary preserves spatial size and ensures edge pixels contribute to the same number of convolution operations as interior pixels — critical when important features (e.g., the object of interest) are near image edges.

### 7. Pooling Layers for Dimensionality Reduction
Pooling sub-samples the feature map by summarizing a local region with a single representative value. Common variants: **max pooling** (dominant in practice), **average pooling**, **min pooling**, and **sum pooling**. Pooling (a) reduces the parameter count fed to downstream layers, (b) introduces a degree of spatial invariance — the exact position of a feature within the pooling window does not affect the output — and (c) makes the representation more robust to small translations and distortions.

### 8. Hierarchical Feature Learning
Early convolutional layers learn low-level features (edges, orientations, blobs). Deeper layers combine these into progressively abstract representations (textures, object parts, whole objects). This mirrors the hierarchical structure of the biological visual cortex. Visualization of intermediate feature maps from VGG16 shows simple oriented edge detectors in shallow layers and complex partial-object representations in deeper layers.

### 9. CNN Architecture: Conv → Pool → FC → Softmax
The canonical pipeline is: one or more [Convolution + Pooling] blocks, followed by a flattening step that converts the final 3-D feature tensor to a 1-D vector, followed by one or more fully-connected (dense) layers, and finally a Softmax output layer producing class probabilities. The dense head is trained with standard backpropagation; the convolutional blocks are simultaneously trained through the same gradient signal.

### 10. Data Augmentation
To reduce overfitting and improve generalization, AlexNet popularised generating additional training samples by applying label-preserving image transformations: horizontal mirroring, cropping, rescaling, color-channel jitter, and rotation. Because machines (unlike humans) do not automatically recognize transformed variants of the same object, augmentation substantially reduces top-5 error without collecting new data.

### 11. Translation Invariance via Convolution + Pooling
A key practical insight demonstrated using two slightly different crop/scale variants of the same cow image: the convolution-pooling combination should detect the same feature (e.g., the cow's horn) regardless of its absolute pixel position. This property — approximate translation invariance — is central to why CNNs transfer well across image crops and scales.

### 12. CNN Applications Beyond Classification
Once feature extraction is learned, CNNs generalize to: **image segmentation** (locating and labelling objects within an image), **object detection with bounding boxes**, **video classification** (treating video as a temporal sequence of frames), **depth estimation** from monocular images, **autonomous driving** perception, and **image generation / artistic style transfer**.

---

## Algorithms / Architectures Covered

| Name | Type | Key Property |
|---|---|---|
| Neocognitron | Early hierarchical feature network | Hand-engineered feature layers (contrast, edges, orientation); inspired by mammalian visual cortex; no backprop learning of filters |
| LeNet (1998) | 2-layer CNN | First true CNN trained with backprop; 32×32 input; 6 then 16 filters (5×5); sum pooling with stride 2; ~60,000 parameters; 99.2% accuracy on MNIST/zip codes |
| AlexNet (2012) | 8-layer deep CNN | Broke the 20% ImageNet error ceiling; introduced ReLU in hidden layers, GPU parallelism, data augmentation, dropout and batch normalization in FC layers; 224×224×3 input; two dense layers before Softmax |
| VGG16 / VGG19 | 16–19 layer CNN | Visual Geometry Group, Oxford; restricted all filters to 3×3 with stride 1 and 1-pixel padding; 3 fully-connected layers; demonstrated that depth with tiny filters can match or beat larger-filter shallower networks |
| GoogLeNet / Inception | ~98-layer CNN | Google; introduced 1×1 convolutions to reduce channel depth before more expensive 3×3 and 5×5 ops; parallel filter branches (Inception modules); ~6.57% top-5 error on ImageNet |
| ResNet | 152-layer residual CNN | Microsoft; introduced skip (residual) connections to allow gradients to bypass layers, enabling very deep networks without vanishing-gradient collapse; ~3.57% top-5 error; very widely used in practice |

---

## Important Intuitions & Examples

**The arrow convolution demo**: A 5×5 input representing a distorted arrow is convolved with a diagonal-extracting filter (1s on main diagonal, 0s elsewhere). The output is a smaller matrix where the value at each position reflects how strongly the diagonal pattern is present at that patch — illustrating both feature extraction and spatial size reduction.

**Parameter count comparison**: A single neuron in a fully-connected layer receiving a 32×32×3 image needs 3,073 weights. Six 5×5 filters (the first convolutional layer) need only 150 weights total, and those same 150 weights are reused across all 28×28 = 784 spatial positions. This compression makes CNNs tractable at scale.

**Odd-sized filters and padding symmetry**: For a 3×3 filter, one pixel of zero-padding on every side allows the filter to be centered on every input pixel including edge pixels. For a 5×5 filter, two pixels of padding are required. Even-sized filters break this symmetry, which is why 3×3 became the dominant choice (used exclusively in VGG, extensively in ResNet).

**Stride trade-off**: Increasing stride from 1 to 2 halves feature-map resolution but drops intermediate spatial information in the same way that not padding loses edge information. AlexNet used stride 4 in the first layer (aggressive downsampling of a 224×224 input); later architectures moved toward stride 1 with more layers to preserve spatial resolution.

**ImageNet error trajectory**: AlexNet (2012) first dropped below 20% top-5 error; GoogLeNet (2014, 22 layers) reached 6.57%; ResNet-152 (2015) reached ~3.57%; current best approaches converge near 1%. Human performance was benchmarked at ~5.1% (though this figure is disputed as annotation-dependent).

**Data augmentation as virtual data creation**: Rajan's example — mirror an image of a person, shrink them to occupy 30% of the frame instead of 70%, rotate — each produces a new labeled training sample that humans trivially recognize as the same person but that a machine treats as genuinely new evidence.

---

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=604-j9tdQQQ)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/IgDNAfEDJvbbRZ8LqiM6kkYLAeKqh7ICx28WXv0C_aPjGY8?e=qreov5)
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/64249/393713/1190179/5931027)

---

## Related

- [[deep-learning|Deep Learning]]
- [[transfer-learning|Transfer Learning]]
- [[ensemble-methods|Ensemble Methods]]
- [[logistic-regression|Logistic Regression]]
- [[linear-regression|Linear Regression]]
- [[ai-paradigms|AI Paradigms]]
