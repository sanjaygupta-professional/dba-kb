---
title: "GenAI and Pretrained Models — Session 07: Fine-Tuning Deep Dive, Diffusion Models, and CLIP"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/llm", "#ai/transformers"]
sources:
  - "_raw/dba-course/Course_06_GenAI_Pretrained_Models/02_Recordings_and_PPTs/Session_07/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Lecture covering supervised fine-tuning vs. PEFT for LLMs, the full diffusion model pipeline for image generation (forward noising, denoising UNet, reverse diffusion), and CLIP's contrastive language-image pre-training that enables text-to-image generation."
---

# GenAI and Pretrained Models — Session 07: Fine-Tuning Deep Dive, Diffusion Models, and CLIP

**Instructor**: Dr. Anand (techno-translator; background in physics PhD, AI strategy consulting)
**Course**: [[course-06-overview-genai-and-pretrained-models|GenAI and Pretrained Models]] (Course 06)
**Session type**: Lecture (theory)
**Resources**: [YouTube Recording](https://www.youtube.com/watch?v=QTdguYUB5iw) | [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/IgAUZQsLSRM6TL3FpXWk9zP7AbPlpGq85gVF2WjN2VueFTw?e=f7ZPBg)

---

## Key Concepts

### 1. Fine-Tuning Motivation: When Prompting and RAG Are Insufficient
The prompting → RAG → fine-tuning progression corresponds to increasing control over model behavior and increasing cost. Fine-tuning is warranted when:
- The LLM needs to adopt a specific **style or tone** not achievable by prompting alone (e.g., how a South Indian law firm writes legal briefs)
- **Domain knowledge** must be permanently embedded (not fetched on demand), giving low-latency responses without retrieval overhead
- The company needs control over the model that can't be achieved via system prompts or knowledge bases
Fine-tuning is analogous to taking a freshly MBA'd hire and putting them through company-specific onboarding: they already have general knowledge; you're teaching them "this is how we do things around here."

### 2. Supervised Fine-Tuning: The Data Requirement
Full (supervised) fine-tuning requires paired data: `(input_question, expected_output)` examples, similar to supervised ML. The process:
1. Gather domain-specific labeled pairs
2. Run training passes with backpropagation across all LLM layers
3. Update weights throughout the model (all transformer layers)
This is extremely expensive because LLM question interpretation happens across all stacked transformer layers (7–8+ layers); changing the behavior of the full stack requires touching every weight. Each experimental run (hyperparameter trial) incurs full training cost.

### 3. Parameter-Efficient Fine-Tuning (PEFT)
Because full fine-tuning of LLMs is unaffordable for most companies, **PEFT** techniques like **LoRA (Low-Rank Adaptation)** are the practical standard:
- Freezes ~98%+ of the original model's weights
- Adds a small trainable adapter (the "correction piece") layered on top of frozen weights
- The adapter's parameter count is a tiny fraction of the total model
- Cost: orders of magnitude lower than full fine-tuning
- OpenAI allows enterprise fine-tuning via PEFT: they host the frozen base model + your company's adapter separately and charge only for training compute
- Risk: **catastrophic forgetting** — specializing a model on one domain may degrade its general capabilities in other areas

### 4. RAG vs. Fine-Tuning: Choosing the Right Tool
| Dimension | RAG | Fine-Tuning |
|---|---|---|
| Knowledge type | Dynamic, frequently updated | Static, stable domain knowledge |
| Update cost | Low (add to vector DB) | High (re-run training) |
| Latency | Higher (retrieval step) | Low (parametric recall) |
| Hallucination | Reduced (grounded in docs) | Still present (probabilistic LLM) |
| Style control | Limited | High (can change tone and format) |
| Infrastructure | Vector DB + embedding model | GPUs + training pipeline |

A hybrid path: use RAG to build a question-answer dataset (sample, human-validate), then fine-tune on that dataset to get a low-latency fine-tuned model. This converts RAG knowledge into parametric memory over time.

### 5. Image Generation Background: VAEs and GANs
The session opens image generation by recapping two architectures covered in deep learning:
- **Variational Autoencoders (VAEs)**: Learn a latent (compressed) representation of a class of images. Sampling a random point in the class's latent region and passing it through the decoder generates a new, never-seen image.
- **GANs (Generative Adversarial Networks, 2014)**: Two competing networks — a **Generator** (struggling artist creating fake images) and a **Discriminator** (expert authentication). Adversarial training in a zero-sum game makes the generator increasingly skilled. Problems: (a) **mode collapse** — the generator finds a single image the discriminator can't catch and keeps producing the same type; (b) **lack of controllability** — no mechanism to specify desired image attributes.
GANs were widely used for advertisement image creation but from 2020 onwards were superseded by diffusion models.

### 6. Diffusion Models: Core Intuition
Diffusion models approach image generation by learning to remove noise, not to generate structure directly. The core human experience analogy: lying on the grass staring at clouds, then — under the power of suggestion — seeing a horse in the randomness. Once suggested, the shape becomes visible and you clean up the noise mentally to confirm the image.

More formally, the underlying mathematics borrows from physics: the **diffusion equation** (Brownian motion) describes how particles randomly spread. Researchers discovered that running the diffusion equation **in reverse** — starting from noise and systematically removing it — provides a tractable generative process.

Michelangelo's quote applies: "The sculpture is already inside the stone. I just remove what doesn't belong." Diffusion models are that removal process, starting from pure noise.

### 7. Forward Diffusion: Training Data Creation
Training a diffusion model requires no labeled pairs in the traditional sense. The training data is self-generated:
1. Start with a large corpus of clean images (downloaded from the web)
2. Apply successive layers of Gaussian noise to each image — 50 noising steps, yielding 50 progressively noisier versions from clean to pure noise
3. This creates 50 (noisy image, slightly cleaner image) training pairs per original image
4. Train a **denoising autoencoder** (related to what the class learned as denoising autoencoders in the deep learning module) on these pairs:
   - Input: noisy image at step t
   - Target: slightly cleaner image at step t-1
The model learns to estimate and remove noise, not to reconstruct the full image at once. Crucially, the model learns to predict noise (what to remove), not to guess the full image.

### 8. UNet Architecture as the Denoising Engine
The workhorse neural network inside a diffusion model is **UNet** (U-shaped Network):
- A symmetric autoencoder architecture with **residual skip connections** between layers of the same spatial resolution (encoder layer → corresponding decoder layer)
- These skip connections solve the vanishing gradient / deep backpropagation problem that plagued early CNNs
- Originally developed for medical image segmentation (tumor vs. normal tissue localization in CT/X-ray), UNet's ability to understand spatial structure within images makes it effective at cleaning noise while preserving image content
- Residual connections (analogous to ResNet) let the model compare the image at two points in the network and understand the contribution of intermediate weights to the overall error

### 9. Reverse Diffusion: Image Generation
At inference (generation) time:
1. Start with **pure random noise** (no structure whatsoever)
2. Suggest a target via a text prompt: "alien playing guitar in style of HR Giger"
3. Pass the noisy image through the UNet denoiser: it removes a small amount of noise in the direction consistent with the prompt
4. Repeat 50 times — each step removes a layer of noise
5. After ~50 steps: a coherent image emerges from what was pure randomness

The reason this works is the power of suggestion — similar to how once you "see" the horse in the cloud, you can't unsee it. The denoising steps iteratively make the suggested structure more visible. Commercial products — DALL-E, Midjourney, Stable Diffusion — all implement this core diffusion mechanism.

### 10. CLIP: Contrastive Language-Image Pre-Training (OpenAI, 2021)
For text-to-image generation to work, the model must understand what "alien playing guitar" means visually. CLIP bridges language and vision by creating a **shared embedding space** in which matching text-image pairs occupy the same region:

**Training procedure:**
1. Download 400 million (image, caption) pairs from the web (images naturally have captions in news, Wikipedia, etc.)
2. Initialize two encoders randomly: a **text encoder** (transformer-based, maps text → vector) and an **image encoder** (CNN-based, maps image → vector)
3. For each pair, compute the dot product between the text vector and the image vector — measuring whether they point in the same direction (high alignment = true pair)
4. Train via contrastive loss: maximize alignment for matching (image, caption) pairs; minimize alignment for non-matching pairs
5. Result: "Photo of a cat" and an actual photo of a cat converge to the same region in the shared 768-dimensional latent space; "Photo of a dog" does not

**Emergent capabilities:**
- Vector arithmetic works across modalities: (Person_with_hat) − (Person_without_hat) → nearest text vector = "hat/cap/helmet"
- Interestingly, the emotion "angry" also appears in the difference, because the hatted photo had a smaller smile — the shared space captured affect as well as objects
- This is the first step toward multimodality: connecting text, images, and potentially audio, video, or DNA sequences into a unified representation space

### 11. Stable Diffusion Full Architecture: CLIP + UNet + VAE
Putting it all together, modern diffusion models (Stable Diffusion, DALL-E) have three components:
1. **CLIP text encoder**: Converts the text prompt into a vector in the shared image-text space
2. **UNet denoiser (conditioned on CLIP embedding)**: At each denoising step, the UNet is conditioned on the CLIP text vector, so it removes noise in the direction consistent with the prompt
3. **VAE decoder**: Converts from latent space back to pixel space for the final image output

The CLIP vector is how the model "knows" what an alien or a guitar looks like — it has seen 400 million captioned images and learned the correspondence.

### 12. Evolution and Limitations of Generative Image Models
| Era | Model | Key Contribution | Key Limitation |
|---|---|---|---|
| ~1980s+ | Autoencoders / VAEs | Latent space generative sampling | Blurry outputs; limited resolution |
| 2014 | GANs | Realistic image quality | Mode collapse; no controllability |
| 2020+ | Diffusion Models | SOTA quality + controllability via CLIP | Inference latency (50 steps); video consistency |

Video generation (temporal diffusion): extending image diffusion to video requires consistency between frames over time (temporal coherence). Current state: 4-second clips are achievable; beyond that, consistency degrades — an active research frontier.

---

## Models / Architectures

| Model / Concept | Type | Notes |
|---|---|---|
| LoRA (Low-Rank Adaptation) | PEFT technique | Trains <2% of weights; current enterprise standard |
| VAE (Variational Autoencoder) | Generative model | Latent space sampling; blurry but controllable |
| GAN (Generative Adversarial Network) | Adversarial generative model | High realism; mode collapse risk; 2014 breakthrough |
| Diffusion Model | Iterative denoising generative model | SOTA image generation; Stable Diffusion, DALL-E, Midjourney |
| UNet | Symmetric autoencoder with residual connections | Denoising backbone in diffusion models; medical imaging origin |
| CLIP | Contrastive Language-Image Pre-Training | Shared latent space for text and images; OpenAI 2021 |
| Stable Diffusion | Composed diffusion system | CLIP + UNet + VAE; open-source |
| DALL-E | Composed diffusion system | OpenAI commercial; same diffusion principles |
| ResNet | CNN with residual connections | Solves vanishing gradient in deep nets; precursor to UNet skip connections |

---

## Important Intuitions & Examples

**Diffusion as Michelangelo.** The sculpture is inside the stone; the artist's job is to remove everything that isn't the sculpture. Diffusion models remove noise layer by layer until the "sculpture" embedded in random noise becomes visible. The prompt acts as the suggestion that determines which sculpture to reveal.

**Cloud watching and power of suggestion.** You look at random clouds (noise) and once someone suggests "that looks like a horse," your brain starts resolving the noise into a horse shape. Diffusion models work the same way — the CLIP conditioning provides the suggestion, and each denoising step resolves the image further.

**CLIP vector arithmetic.** Take a photo of a person without a hat → CLIP vector A. Take a photo of the same person wearing a baseball cap → CLIP vector B. B − A ≈ the word "hat." The difference also captures "angry" (the smile was slightly smaller in the hatted photo). The shared embedding space is semantically rich in ways that mirror word2vec arithmetic.

**Brownian motion connection.** The instructor confirmed that diffusion models are mathematically grounded in physics: the diffusion equation describes Brownian motion (random particle movement). The key insight was that this equation can be reversed — running diffusion backward from noise to structure. The connection to physics provides both mathematical legitimacy and optimization properties.

**Why small LLMs work in RAG.** The LLM in a RAG system is not asked to know anything — it's given five retrieved paragraphs and asked to phrase an answer. It doesn't need training on astrophysics to answer "How many moons does Jupiter have?" from a NASA document. This decoupling of knowledge (vector DB) from language (small LLM) is the core RAG insight that makes it cost-effective.

---

## Related

- [[deep-learning]]
- [[transfer-learning]]
- [[ai-paradigms]]
- [[course-06-session-05-summary|Session 05 — Azure OpenAI Hands-On Lab]]
- [[course-06-session-06-summary|Session 06 — Guardrails and RAG Architecture]]
