---
title: "GenAI and Pretrained Models — Session 13: Enterprise GenAI Deployment — From PoC to Production"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/llm", "#ai/transformers"]
sources:
  - "_raw/dba-course/Course_06_GenAI_Pretrained_Models/02_Recordings_and_PPTs/Session_13/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "The final teaching session of Course 06, covering enterprise AI strategy: the wedge/lean-startup approach to project selection, the translator role between business and tech, choosing the right AI solution tier (rules/ML/SLM/LLM), PoC-to-production deployment mechanics including Docker containerisation, Kubernetes autoscaling, and cloud hosting, with a live prototype demo of an email-triage LLM app."
---

# GenAI and Pretrained Models — Session 13: Enterprise GenAI Deployment — From PoC to Production

**Course**: [[course-06-overview-genai-and-pretrained-models|GenAI and Pretrained Models]] (Course 06)
**Instructor**: Prof. Ananda (suicide analytics)
**Session type**: Lecture 10 of 10 — enterprise strategy + live demo

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=SgfRzxPdZv4)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/IgDmm1O19Dw1Q5A-Tm0eBB7tARv9ccJ9aDI95cDjGP-MFpU?e=zU5naX)
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/64668/397034/1199121/5975601)

---

## Key Concepts

### 1. The PoC-to-Production Gap

Opening framing: over 80% of AI proof-of-concepts never reach production. For GenAI specifically, an MIT study cited by the instructor puts this at **95% failure to move beyond pilot**. The reasons are not primarily technical model quality — they are organisational, economic, and operational:

- Costs at scale are far higher than PoC assumptions (token costs × volume)
- Latency is unacceptable under real user load
- Compliance and data-handling violations surface only in production data
- Model drift: behaviour changes as production data distribution diverges from training data
- Hallucination rates unacceptable for business decisions
- Cross-team governance, data access, and change management barriers

The session's stated goal: equip "translators" — MBA-profile professionals who bridge business and engineering — with the decision framework to navigate this gap successfully.

### 2. The Translator Role

The instructor introduced the **translator** concept (originally from Google):

> Translators understand technology well enough to see the big picture and understand business needs well enough to define strategy. They are not coders, but they sit between business problems and technical implementation.

As a translator, one must think simultaneously across:
- **Business outcomes**: clear, measurable goals (response time, error rate, cost per interaction)
- **User definition**: who exactly uses this system and how
- **Data landscape**: structured vs. unstructured, private vs. public, data locality requirements
- **Interface design**: what UI/API surfaces are needed
- **Maintenance model**: who owns it post-deployment, how is it updated

The programme is explicitly framed as translator training — not building coders, but building people who can increase organisational AI success rates through informed decision-making.

### 3. The Wedge Strategy

**Core principle:** Do not attempt enterprise-wide AI transformation. Instead:

1. Identify a **single painful workflow** — a specific, measurable bottleneck
2. Build a **narrow, well-defined** solution targeting that wedge
3. Deploy to **hero users** (early adopters willing to tolerate imperfection and provide feedback)
4. Gather real-world data, refine, and **scale incrementally**

**Analogy:** A wobbly dining table — you do not redesign the entire room, you insert a small wedge under the one leg that does not touch the floor.

**Why not enterprise-wide strategy?** The instructor described a real client RFP requesting a unified GenAI transformation across HR, Finance, Sales, Services, and Manufacturing simultaneously. His firm did not win the contract — they proposed a narrower approach because the all-in-one strategy is "a surefire way of failure": complex governance, cross-team dependencies, multi-year timelines, and no early wins to sustain momentum.

**Lean Startup parallel (raised by student Balaji):** The wedge strategy maps directly to the Build-Measure-Learn loop, hypothesis testing, and focused KPIs from Eric Ries's framework.

**Optimisation analogy:** Enterprise-wide top-down planning is like Soviet central planning — theoretically efficient, practically brittle. Distributed experimentation (individual departments trying their own solutions) is like a federal democracy — seemingly redundant, but produces far more successful outcomes overall.

**Hybrid in practice (shared by student Norman):** At Norman's company, they first did bottom-up pain-point identification across departments, then did horizontal prioritisation (which department has the biggest efficiency opportunity), then within each department used a vertical progression: chatbot copilot → workflow automation → full autonomy.

### 4. Choosing the Right AI Solution Tier

Before reaching for GenAI, a translator must evaluate the full AI solution spectrum. Using the email-triage example (retail company, 30,000 customer emails/month):

| Tier | When to Use | Characteristics | Example Application |
|------|-------------|-----------------|---------------------|
| Rules-based logic | Clear, deterministic patterns; no uncertainty | Zero cost, zero latency, 100% predictable | "If purchase date > 6 months ago, reject return" — no LLM needed |
| Traditional ML | Structured data available; known input-output mapping | Cheap, fast, locally hostable | Intent classification from structured email metadata |
| Small Language Model (SLM) | Unstructured text; moderate complexity; data-privacy constraints | Runs locally; small memory footprint; domain-fine-tuned | On-device email classification when data cannot leave premises |
| Large Language Model (LLM) via API | Complex reasoning, nuanced language, high generality | Most capable; data leaves environment; variable latency and cost | Draft response generation with tone, policy, and entity awareness |
| Self-hosted LLM (cloud) | High volume, latency control, data sovereignty | Requires GPU infra expertise; full scale control | Production email triage at enterprise scale |
| On-premises LLM | Maximum data privacy; regulated industries | Highest cost; most control | Defence, healthcare, government |

**Key decision factor:** The instructor strongly urged against using LLMs for tasks that rules or ML can handle adequately — the cost, latency, and unpredictability penalties are unnecessary.

### 5. Prototype-First Methodology

The prototype (PoC) phase has a specific, limited purpose: **learning**, not saving money or achieving production quality.

**What to measure during prototype:**
- Actual token consumption per message (vs. PoC estimate)
- Latency per call under realistic load
- Confidence score distribution — what fraction of queries exceed the routing threshold?
- Error categories (hallucinations, misclassifications, policy violations)
- Data sensitivity issues that were not anticipated (PII in emails)
- Whether batching is needed vs. real-time processing

**Architecture of the prototype demonstrated live (TriageIQ):**

```
Email arrives
  → Deduplication + thread collapsing
  → Single LLM call: intent classification + confidence score
  → If confidence ≥ 75%: second LLM call to draft response
  → If confidence < 75%: escalate to human agent
  → Log: latency, token count, intent, confidence, outcome
```

Implementation: Python, GPT-4-mini via API, single `main.py` file. Estimated cost: $300–500/month for 30,000 emails (assuming ~500–700 tokens/email, 15M tokens/month at mid-tier LLM pricing). Infrastructure: single lightweight VM ($100/month), no GPU, no autoscaling needed at prototype stage (1,000 emails/day spread over 8 hours = negligible concurrent load).

### 6. Enterprise Architecture Layers

Moving from prototype to production requires coordinating four layers:

1. **Infrastructure layer**: compute, networking, storage — must support multiple concurrent applications, not just this one
2. **Platform layer**: software tooling — LLM API integrations, data pipeline frameworks, agent orchestration, observability
3. **Application layer**: the actual user-facing product — UI, API endpoints, integration with CRM/ERP
4. **Governance/risk layer**: monitoring for model drift, compliance violations, hallucinations, PII leakage, prompt injection

**Full production email-triage architecture:**
- Email server connector → message queue
- Pre-processing: PII detection and anonymisation, spam filtering, thread reconstruction
- Intent classification: ML or SLM (rules suffice for binary classifications; LLM overkill)
- Entity extraction: order ID, product, date from email body
- Policy engine: deterministic check against return/refund rules
- SLM/LLM: draft response generation
- Compliance layer: tone checking, offensive language filter
- Human-in-loop agent: final review/override
- CRM update: log resolution

**Failure modes to design for:**
- **Prompt injection**: malicious users embed instructions in email body to redirect LLM behaviour (real incident: a user exploited a coding agent's use of a public repository by embedding prompt injection; the agent corrupted a database before the Reddit post forced a fix within 1 hour)
- **Model drift**: production data distribution drifts from training data over time → performance degrades silently
- **Data sensitivity**: PII, payment card data, SSNs in customer emails must be stripped before sending to external LLM APIs

### 7. Containerisation with Docker

**Problem solved:** "Works on my machine" — Python 3.11 on Windows with library set A fails to run on a Linux cloud VM with library set B.

**Docker solution:** Package code + all dependencies into an immutable *image*. Each service runs in its own isolated *container*. Benefits:
- Portability: same image runs identically in dev, staging, production
- Isolation: dependency clashes between services eliminated
- Atomic updates: update one container without restarting the whole application
- Faster than VMs: containers share the host OS kernel; VMs replicate a full OS per instance

**Dockerfile structure demonstrated (TriageIQ):**
```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

**Deployment workflow demonstrated live:**
1. Develop locally (`main.py` + `requirements.txt` + `Dockerfile`)
2. `git commit` + `git push` → GitHub repository
3. Render.com detects GitHub change → automatically rebuilds Docker image → redeploys
4. Environment variables (API keys) passed securely at deploy time, not hardcoded in source

**Render vs. AWS/GCP:** Render offers simpler UX with automatic CI/CD from GitHub. AWS/GCP offer free startup credits and deeper enterprise features but require more configuration steps.

### 8. Kubernetes and Autoscaling

**Kubernetes** manages fleets of Docker containers:

- If concurrent users exceed a threshold (e.g., 50), Kubernetes automatically spawns additional container instances (*horizontal pod autoscaling*)
- Traffic load balancer distributes requests across instances
- When load drops, extra containers are terminated (scale down to save cost)
- Rolling updates: deploy a new container version to a subset of instances, monitor, then roll out fully — zero-downtime deployments

**When you need GPU infrastructure:**
- API calls to third-party LLMs: no GPU needed (GPU is on provider's side)
- Cloud-hosted self-managed LLM: GPU instances on AWS/GCP (p3, p4 instance families)
- On-premises: GPU servers; highest upfront cost but maximum privacy and predictable cost

**Capacity planning thumb rule (mentioned, detail deferred):** Depends on model size, batch size, and throughput target — covered in deployment planning slides not fully walked through in session.

### 9. Deployment Options Decision Framework

| Option | Data leaves env? | Cost | Latency control | Privacy | When to choose |
|--------|-----------------|------|-----------------|---------|----------------|
| Third-party API (OpenAI, Anthropic) | Yes | Pay-per-token; unpredictable at scale | Low | Low | Prototypes, low-volume, R&D |
| Cloud self-managed (AWS/GCP/Azure) | Partially (within cloud boundary) | Medium; scalable | High | Medium | Most production enterprise use cases |
| Private cloud (government-backed, e.g., Saudi sovereign cloud) | No | Medium-high | High | High | Regulated industries; national data residency requirements |
| On-premises | No | Highest (capex) | Highest | Maximum | Defence, classified, maximum regulatory constraint |

**Pricing strategy for internal tools (student question):** OpenAI/Google chose freemium (habituate users, then charge for advanced tiers); Anthropic chose paid-from-day-one with strict free limits. Both models have succeeded — the choice is a business strategy question, not a technical one.

## Models/Architectures Discussed

| Model/Tool | Role in Session |
|---|---|
| GPT-4-mini | Used in live TriageIQ prototype for intent classification + response generation |
| SLMs (generic) | Recommended for intent classification in production where data privacy is a concern |
| Liquid Neural Networks (LNN) | Mentioned by a student (Fin's group) — learns dynamically from environment rather than frozen weights; used for fraud detection and drone navigation consulting |
| Docker | Containerisation platform for reproducible, portable deployment |
| Kubernetes | Container orchestration and autoscaling |
| Render.com | Simple cloud hosting platform with GitHub CI/CD integration, used in live demo |
| Git/GitHub | Version control; enables CI/CD pipeline to Render |

## Important Intuitions and Examples

**Wedge strategy vs. Enterprise-wide transformation:** The instructor drew a direct analogy to democracy vs. central planning economies. Central planning (USSR, India's Five Year Plans) sounds more efficient on paper but fails due to complexity. Distributed experimentation (federal democracy) has apparent redundancy but produces resilient outcomes. Same principle applies to AI deployment strategy.

**TriageIQ live demo:** The instructor built and deployed to Render.com in real time during the session. An email saying "I placed an order 4 days ago and haven't received shipping confirmation" was classified as "order status" with 90% confidence → draft response generated. An ambiguous email ("I have a question about my recent purchase, can you help me?") returned only 60% confidence → escalated to human, no draft generated.

**Prompt injection real-world incident:** A coding agent (Cline) used public GitHub repositories as tools. A security researcher notified the company three times that a specific repository was vulnerable to prompt injection. The company ignored the emails. The researcher then sent the malicious prompt — the agent corrupted a database. Within 1 hour of a Reddit post, the company issued a fix. The incident illustrates that agentic systems with external tool access have a fundamentally expanded attack surface.

**Cost calculation as translator skill:** 30,000 emails/month × 500–700 tokens/email = ~15M tokens/month. At mid-tier LLM pricing this is $300–500/month in model costs. A translator should be able to construct this estimate and present it to the business — it is not the engineer's job to explain this, and the business person alone cannot derive it.

**Liquid Neural Networks footnote:** A student mentioned using LNNs for fraud detection (one layer) combined with a pre-trained model that generates synthetic fraud data for continual retraining (second layer). LNNs learn dynamically from streaming data without retraining from scratch — addressing the frozen-weights limitation discussed in Session 11's AGI section.

## Related

[[deep-learning]] | [[transfer-learning]] | [[ai-paradigms]] | [[course-06-session-11-summary]] | [[course-06-session-14-summary]] | [[course-06-overview-genai-and-pretrained-models]]
