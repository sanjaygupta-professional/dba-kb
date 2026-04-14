---
title: "GenAI and Pretrained Models — Session 11: AI Horizons — AGI, Sovereign AI, Ethics, and Jobs"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/llm", "#ai/transformers"]
sources:
  - "_raw/dba-course/Course_06_GenAI_Pretrained_Models/02_Recordings_and_PPTs/Session_11/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "A non-technical capstone discussion covering AGI timelines and definitions, the efficiency revolution in LLMs, sovereign AI strategy across geographies, AI ethics controversies including Anthropic's Pentagon standoff, infrastructure investment bubbles, and the impact of AI on employment."
---

# GenAI and Pretrained Models — Session 11: AI Horizons — AGI, Sovereign AI, Ethics, and Jobs

**Course**: [[course-06-overview-genai-and-pretrained-models|GenAI and Pretrained Models]] (Course 06)
**Instructor**: Prof. Ananda (suicide analytics; DBA programme faculty)
**Session type**: Non-technical capstone discussion — news-driven, opinion-seeking, MBA-style

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=6dU9yUsUSF4)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/IgCyndTxTz98Q51Lh1465MNOAS3S-OGXhdijCF1_rQdwW8k?e=pxlTnc)
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/64668/397034/1198441/5972359)

---

## Key Concepts

### 1. Gartner Hype Cycle Revisited

The session opened by revisiting the hype cycle introduced at the start of the module. In the 2025 Gartner cycle, Generative AI was shown approaching the *trough of disillusionment* while agentic AI sat at the *peak of inflated expectations*. By Session 11, the instructor's view had shifted: some industries are already demonstrating real productivity gains, collapsing the plateau of productivity timeline. The more pressing question is no longer "is AI productive?" but "whose AI is it, and on what terms?"

### 2. Artificial General Intelligence (AGI) — Definitions and Timelines

AGI is loosely defined as a model capable of becoming a specialist in *any* domain while continuously learning — a generalised capability analogous to human intelligence, distinct from narrow AI (chess engines, medical diagnostics) and from *singularity* (the hypothetical point where AI self-improves faster than humans can contribute).

Pre-ChatGPT consensus: AGI within 20–30 years. Post-ChatGPT consensus: 2–3 years. The instructor cautioned that this compression in timelines reflects hype as much as evidence, citing the Neils Bohr aphorism — "Prediction is hard, especially about the future."

**Key limitation cited (Dwarkesh Patel / Dario Amodei framing):** LLMs lack *continual learning*. The model's weights are frozen at training; the only update mechanisms are expensive fine-tuning (with catastrophic forgetting risk) or RAG (which updates context but not reasoning patterns). Human workers improve adaptively through on-the-job feedback — a capability current LLMs fundamentally lack.

### 3. Three Epochs of AI Progress (Ilya Sutskever Framework)

Ilya Sutskever (co-founder of OpenAI, later SafeSuperintelligence) articulated three eras:

| Era | Period | Defining Characteristic |
|-----|--------|--------------------------|
| Age of Research | 2012–2020 | Novel architectures (CNNs, Transformers, BERT) drove gains |
| Age of Scaling | 2020–2025 | Scaling laws meant more compute + more data = predictable improvement; low-risk capital allocation |
| Age of Research (again) | 2025– | Pre-training data is effectively exhausted; brute-force scaling no longer sufficient; new ideas required |

Sutskever's departure from OpenAI was partly motivated by the belief that the scaling paradigm has hit its limits and that genuinely new research approaches are needed.

### 4. Paths Toward Continual Learning (AGI Prerequisites)

Two research directions were highlighted:

- **Agentic Context Engineering (ACE):** External memory stores (e.g., Supabase) that agents read and write to, enabling accumulated context across interactions — like a continuously updated shared document. Does not update model weights and is still bounded by context window limits.
- **SEAL (Self-Adapting Language Models):** Agents rewrite their own reasoning code mid-task. Still at research-paper stage, not production-deployed.

**Hierarchical Reasoning Models** were also mentioned: a 27M-parameter model trained on 1,000 samples beating large LLMs on specific tasks by using layered, tree-structured reasoning rather than one-shot generation.

### 5. Data Constraints and Multimodal Data Collection

Pre-training data from the internet is effectively exhausted. Current models increasingly rely on **synthetic data** (LLM-generated training sets). Yann LeCun's argument: human intelligence derives from multi-sensory embodied experience, not text alone. One response — companies employing workers (often in India) wearing GoPros to perform household tasks (folding clothes, ironing), generating embodied interaction data for humanoid robot training.

### 6. Small Language Models (SLMs) and the Efficiency Revolution

SLMs (e.g., Gemma 2B, Qwen 4B) represent an efficiency countertrend to massive LLMs:

- Run locally on consumer laptops (4B parameters < 4 GB VRAM)
- Consume ~5% of the energy of a GPT-scale model for equivalent-scale deployment
- Fine-tuned on domain-specific data, SLMs often *outperform* frontier LLMs on narrow tasks
- Alibaba's Qwen model cited by Airbnb CEO as preferred for cost-effectiveness over OpenAI APIs
- Chinese labs (DeepSeek, Kimi, Qwen) dominate the top 20 open-source model leaderboard — partly as a strategic response to US chip export controls, solved through architecture innovation, knowledge distillation, and open-source collaboration

**Distillation controversy:** Anthropic accused Chinese labs of using API access to ChatGPT/Claude to generate question-answer pairs and train competing models — the same practice OpenAI was accused of by the New York Times regarding web-scraped training data.

### 7. Sovereign AI — The Geopolitical Chessboard

The US controls the entire AI supply chain: Nvidia (80–95% GPU market share), ASML (100% of EUV lithography), TSMC (advanced semiconductor fabrication), and AWS/Azure/GCP (cloud compute). A US export ban is a single point of failure for any country's AI programme.

**Country responses:**

| Country | Strategy |
|---------|----------|
| Saudi Arabia | Massive capital investment; Arabic LLMs; data residency rules (data must stay in Middle East); government-funded sovereign cloud infrastructure |
| India | Leveraging sovereign data (Aadhaar-linked banking, health records); building multilingual models; cost advantage through data access rather than capital |
| Europe (EU) | Regulation as sovereignty — EU AI Act has become the de facto global standard; no frontier models produced domestically; depends on US or China for underlying compute |
| China | Open-source strategy to circumvent chip export bans; distillation and architecture efficiency; top 20 open-source models predominantly Chinese |

**Real-world signal:** In the US/Israel–Iran conflict, one of Iran's retaliatory missile strikes targeted a UAE data centre — treating AI infrastructure as strategic military target, not civilian technology.

### 8. Ethics Case Study — Anthropic vs. Pentagon

The most discussed incident: Pentagon demanded Anthropic remove safety guardrails from Claude for US Department of Defense use cases. Anthropic refused on two specific points:
1. **Domestic mass surveillance** — AI-enabled aggregation of private data purchased by government, then mass-analysed; not yet illegal but newly feasible
2. **Fully autonomous weapons** — systems that identify and fire on targets without human authorization (distinct from remotely piloted or target-designated systems)

Pentagon declared Anthropic a **supply chain risk** (unprecedented for a US company). Within hours, OpenAI signed a Pentagon contract, implicitly accepting the looser guardrails.

Within 24 hours, Claude went from outside the App Store top 100 to #1, driven by users switching from OpenAI over ethics concerns.

**Instructor's meta-observation:** When he ran his lecture deck through both ChatGPT and Claude for critique, Claude recommended framing the discussion as "which AI vendor do you trust?", while ChatGPT cautioned against implying OpenAI was reckless — a direct demonstration of how model providers embed their own positional biases into outputs.

### 9. Infrastructure Investment — Bubble or Not?

Capital flowing into AI infrastructure is unprecedented for a private-sector technology cycle:

- Nvidia's revenue growth driven partly by a circular funding dynamic: Nvidia invests in OpenAI/Anthropic/xAI → those companies buy Nvidia GPUs → Nvidia revenue rises → stock rises → more investment capacity
- Morgan Stanley characterised the level of data centre commitment as "nation-scale" (30 GW compute capacity committed)
- **Bubble argument:** Revenues are partly circular; many Fortune 500 companies have not yet achieved production-grade AI workflows despite heavy investment
- **Counter-argument:** Productivity gains in coding, legal, finance are real and measurable; IT outsourcing industry (Indian IT majors: Infosys, TCS, Wipro) facing structural disruption as agentic coding drops cost to near-electricity-price levels; Indian rupee fell ~20% in four months partly in response

### 10. Jobs and Labour Market Impact

AI's impact on employment follows the same historical pattern as every major technology (printing press, internet):
- Early adopters tend to be low-common-denominator applications (adult content, spam)
- Technology then corrects and normalises into productive societal use
- Cost arbitrage thesis (Indian IT outsourcing) is structurally threatened — agentic coding now reduces software development cost to electricity cost, not human labour cost

### 11. AI Governance

Governance discussion was abbreviated due to time. Key tensions:
- Tech companies (Anthropic model) believe they have an ethical obligation to constrain use of their systems
- Democratic governments (US DoD model) argue elected governments, not private companies, should determine what is legally permissible
- EU regulation as the emerging global norm, despite EU having no frontier AI capability

## Models/Architectures Discussed

| Model/System | Description |
|---|---|
| Qwen (Alibaba, 4B) | SLM; runs on laptop; used by Airbnb; beats GPT on narrow tasks post-fine-tuning |
| Gemma (Google) | SLM; 5% energy footprint vs GPT for equivalent deployment at scale |
| Kimi | Chinese SLM; strong English output quality despite limited post-training |
| DeepSeek | Chinese open-source; architecture and distillation innovations |
| Claude (Anthropic) | Frontier LLM; enterprise-focused; refused Pentagon guardrail removal |
| GPT-4 / ChatGPT (OpenAI) | Frontier LLM; signed Pentagon contract; different ethical posture |
| SafeSuperintelligence (Sutskever) | Stealth research company; pursuing non-scaling AGI approaches |
| SEAL | Self-Adapting Language Models — agents rewriting own reasoning code; research stage |

## Important Intuitions and Examples

**Rainman analogy for narrow AI:** Tom Cruise's autistic brother in the film can count cards perfectly but lacks general social cognition — precisely the profile of today's AI: superhuman on narrow benchmarks, missing generalisation.

**Saxophone teaching analogy (Dwarkesh Patel):** Teaching a student saxophone by sending each student in once, observing one attempt, writing notes for the *next* student, and repeating — this is exactly how LLM fine-tuning works. No single model instance learns from its own mistakes during operation.

**Singularity via life-expectancy:** Singularity is not immortality — it is the moment when every year of medical research extends life expectancy by one year. AI singularity is when AI improves its own capability faster than humans do.

**Printing press / Internet pattern:** Both were first adopted for lowest-common-denominator content, then corrected into broad productive use. Instructor's optimistic view: AI will follow the same arc.

**India IT sector as leading indicator:** Within months of Claude Code/Opus capabilities becoming clear, TCS, Infosys, and Wipro stocks dropped significantly — markets pricing in structural elimination of the cost-arbitrage business model.

## Related

[[deep-learning]] | [[transfer-learning]] | [[ai-paradigms]] | [[course-06-session-13-summary]] | [[course-06-overview-genai-and-pretrained-models]]
