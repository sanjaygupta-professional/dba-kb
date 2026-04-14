---
title: "GenAI and Pretrained Models — Session 15: Final Project Presentations — Day 2"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/llm", "#ai/transformers"]
sources:
  - "_raw/dba-course/Course_06_GenAI_Pretrained_Models/02_Recordings_and_PPTs/Session_15/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Second and final day of Course 06 group project presentations, featuring AEGIS multi-jurisdictional regulatory conflict resolution and additional groups, with notable technical depth in knowledge graph design, federated compliance orchestration, temporal regulatory versioning, and ROI modelling for enterprise AI governance solutions."
---

# GenAI and Pretrained Models — Session 15: Final Project Presentations — Day 2

**Course**: [[course-06-overview-genai-and-pretrained-models|GenAI and Pretrained Models]] (Course 06)
**Instructor**: Prof. Ananda
**Session type**: Group project presentations (Day 2 of 2; course conclusion)

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=kicCvqgr44U)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/IgBLL9BSBnhnTrCh9FJrXS0UATpoAl__6DzhuzMlllJ104M?e=dNaG8z)
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/64668/397034/1199538/5977340)

---

## Session Structure

Continuation of the Day 1 evaluation framework. Groups 5 and 4 were rescheduled from the previous session due to time overruns. The session began with a brief negotiation over presentation order — Group 5 requested to go first as a team member was traveling. Presentations were held to a 20-minute hard cap with a 25-minute warning.

---

## Key Concepts

### The Compliance Tax as an AI Problem Domain

Group 5's presentation framed enterprise compliance as a domain structurally suited to agentic AI, not because it is computationally hard but because it is *combinatorially complex in a way that scales beyond human capacity*:

- 72+ countries now have active data protection regulations (GDPR, DPDP, PDPA Singapore, CCPA, BSA)
- In 2025, US alone produced 260+ new or evolved regulations
- 70% of compliance team time spent on regulation *monitoring and maintenance*, not substantive compliance work
- Global financial sector: $260 billion annual spend on regulatory maintenance
- $19.3 billion in global regulatory penalties paid in 2024; TD Bank alone paid $3 billion — not for non-awareness but for inability to resolve conflicts across jurisdictions within a 12-year window

**Core insight**: The problem is not finding regulations (dictionary search is solved). The problem is *conflict resolution* — when two jurisdictions impose mutually contradictory obligations, no existing tool tells you how to reconcile them.

---

## Project Summaries

### Group 5 — AEGIS: Adaptive Enterprise Governance Intelligence System

**Problem framing — the NovaPay dilemma**: NovaPay, a Singapore-based fintech using AI-driven credit scoring, operates across Germany, California, Texas, India, and Singapore simultaneously. A single loan decision triggers five overlapping regulatory frameworks:

| Jurisdiction | Key Regulation | Obligation |
|-------------|---------------|------------|
| EU (Germany) | EU AI Act (high-risk AI: credit scoring) | Transparency, explainability mandatory |
| EU (Germany) | GDPR | Opt-in consent; data minimisation; no retention beyond necessity |
| California | CCPA | User opt-out rights; data usage restrictions |
| US | BSA (Bank Secrecy Act) | Transaction data retained minimum 5 years |
| India | DPDP Act | Consent-driven; data localisation; strict penalties for failure |
| Singapore | AI Governance Framework | Voluntary; protects AI models as intellectual property (trade secret) |

**The conflict**: EU AI Act requires model explainability → Singapore law protects AI model as trade secret. GDPR mandates data minimisation → BSA requires data retention. India mandates data localisation → US/EU cloud-hosted data conflicts.

These are not edge cases — they are the default operating environment for any global fintech.

**Solution — AEGIS (multi-agent diplomatic architecture)**:

Not a regulatory *dictionary* — a regulatory *diplomat*. The distinction:
- Dictionary: retrieves relevant laws for a jurisdiction
- Diplomat: detects conflicts *between* jurisdictions and proposes *resolution strategies* with confidence scores

**Architecture (three layers)**:

1. **Regulatory Injection Layer**
   - Automated ingestion of regulatory sources (websites, court decisions, news feeds, amendment announcements)
   - Semantic processing pipeline: converts legal text into structured knowledge
   - Continuous update loop: regulations are ingested as they change, not as a static snapshot

2. **Knowledge Reasoning Engine**
   - **Entity Network Graph (ENG)**: maps relationships between regulatory entities, obligations, and jurisdictions
   - **Document Navigator Graph**: structural understanding of law (not just keyword search)
   - **Temporal knowledge graph versioning**: each regulatory provision carries metadata (effective date, amendment history, sunset clauses) enabling point-in-time compliance queries ("what were our obligations under the law on this specific date?" — critical since regulators assess compliance retrospectively)

3. **Agentic Orchestration Layer (the diplomatic engine)**
   - Jurisdiction-specific RAG agents: each agent is trained on a specific jurisdiction's corpus
   - Central meta-agent: detects conflicts between jurisdiction-agent outputs and proposes resolution strategies
   - Reasoning cycle (agent swarm): iterative conflict negotiation across agents
   - Audit and explainability: citation generation for every decision
   - Human-in-the-loop governance: compliance officers review and select from proposed resolution strategies

**AEGIS output (NovaPay example)**:
- Conflict identification: EU explainability ↔ Singapore trade secret (score: high conflict)
- Conflict identification: GDPR data minimisation ↔ BSA 5-year retention (score: high conflict)
- For each conflict: multiple resolution strategies with confidence scores
- Compliance officer selects preferred strategy, reasoning chain documented for audit trail

**Three patentable claims**:

| Claim | Description | Novelty |
|-------|-------------|---------|
| Jurisdiction-aware agentic AI | Multiple RAG agents, each trained on a specific jurisdiction corpus, with a central meta-agent detecting inter-jurisdiction conflicts | Not retrieval (many tools do this); conflict detection + resolution across regulatory regimes |
| Temporal knowledge graph versioning | Regulatory provisions carry effective dates, amendment histories, sunset clauses; enables point-in-time compliance queries | Allows retrospective compliance assessment as regulators require it |
| Federated compliance orchestration | Jurisdiction agents operate within local boundaries; only summaries cross system boundaries; compliance platform is itself compliant (data sovereignty by design) | Compliance intelligence without data sovereignty violation |

**Competitive landscape**:

| Competitor | Capability | Gap |
|------------|-----------|-----|
| Cube, Thomson Reuters FinReg | Regulatory monitoring and mapping | Stops at interpretation; no conflict resolution |
| Ascent AI | Legal research | No cross-jurisdiction conflict resolution |
| Regnology | Reporting | Different category |
| **AEGIS** | All of above + conflict resolution + resolution strategy proposals | "Most tools are dictionaries; AEGIS is a diplomat" |

**ROI analysis (NovaPay model — $800M fintech, 35-person compliance team, 5 jurisdictions)**:

| Benefit Category | 3-Year Value |
|-----------------|-------------|
| Staff efficiency (automation of 70% monitoring/maintenance) | $12M |
| Regulatory fine avoidance (earlier detection, better documentation) | $8M |
| Speed-to-market advantage (faster compliance clearance for new products/markets) | $5M |
| Audit cost reduction (automated evidence gathering) | $3M |
| Reduced outside counsel cost (first-pass cross-jurisdictional analysis) | $3M |
| **Total** | **$31M** |
| Investment | $5.7M |
| **ROI** | **546%** |
| **Payback period** | **4 months** |

**Conservative case (50% benefit reduction)**: 223% ROI, 8-month payback.
**Adverse case (30% benefits, 40% cost overrun)**: Still positive within 18 months.

**NovaPay-specific ROI**: 577% with 8-month head start entering new markets due to faster compliance clearance.

**Roadmap (4 phases)**:
- Phase 1: Single jurisdiction (EU AI Act — most structured, most time-sensitive); build trust through 90%+ accuracy and 80%+ scenario coverage
- Phase 2: Five major jurisdiction agents (EU, US/California, India, Singapore) + conflict resolution validation; GRC platform integrations
- Phase 3: 20+ jurisdictions; RLHF-enabled self-improvement; predictive regulatory analytics (weeks to hours advance warning)
- Phase 4: Multi-tenant SaaS; 50+ jurisdictions; SOC compliance; full automated regulatory intelligence

**Academic and commercial pathways**: Framework proposed for publication in Journal of AI & Law, Stanford Technology Law Review, or GRC forums.

**Team**: Gurvan (presented first; fintech regulatory compliance practitioner; Bloomberg background), Vijaya (technical architecture), Vishal (regulatory landscape expert), Suri Babu (product roadmap), Sitha (business case and ROI)

---

## Models/Architectures Referenced Across Presentations

| Model/System | Use |
|---|---|
| Multi-agent RAG (jurisdiction-specific) | AEGIS: each agent specialised on one jurisdiction's corpus |
| Entity Network Graph | AEGIS: structured knowledge representation of regulatory entities and relationships |
| Temporal Knowledge Graphs | AEGIS: versioned regulatory provisions with amendment metadata |
| LangGraph / agent swarm | AEGIS: iterative conflict negotiation across jurisdiction agents |
| RLHF | AEGIS Phase 3: self-improving compliance predictions from regulatory feedback |
| Liquid Neural Networks (LNN) | Fin's group: dynamic on-the-fly learning for fraud detection (no frozen weights) |
| Synthetic data generation | Fin's group: pre-trained model generates synthetic fraud patterns for continuous retraining |
| Human-in-the-loop (HITL) | All groups: compliance officer, developer, or legal expert review as governance gate |

## Important Intuitions and Examples

**"Most tools are dictionaries; AEGIS is a diplomat"** — The session's most quotable framing. Distinguishes between retrieval-augmented lookup (what existing RegTech tools do) and reasoning-based conflict arbitration (what AEGIS proposes). This distinction maps directly to the broader course theme: GenAI's value is not in access to information but in reasoning over connected, ambiguous, multi-party information.

**TD Bank case study**: $3 billion in penalties not from regulatory ignorance but from inability to resolve conflicting obligations across jurisdictions within a 12-year timeline — the exact problem AEGIS addresses. Human compliance teams are the bottleneck, not the regulation itself.

**Data localization vs. cloud efficiency**: AEGIS's federated architecture addresses a real tension in compliance AI — you cannot send jurisdictionally restricted data to a centralised cloud AI for analysis. The "jurisdiction agents operate within local boundaries; only summaries cross system boundaries" design solves this structurally.

**Temporal compliance queries**: "What were our GDPR obligations on March 15, 2023?" — a question regulators ask when assessing past compliance breaches. Most systems cannot answer this because they only represent current regulatory state. AEGIS's temporal knowledge graph is designed specifically for this retrospective use case.

**NovaPay as simulation vehicle**: Using a fictionalised but realistic case (Singapore fintech, five jurisdictions, AI credit scoring) grounded all abstract regulatory conflict claims in a specific operational scenario — a strong presentation technique that the instructor noted positively.

**Liquid Neural Networks (LNN) for fraud detection**: A fundamentally different approach to the "frozen weights" problem discussed in Session 11's AGI section. Rather than pre-training once and deploying statically, LNNs update their internal dynamics continuously from the streaming environment. Used in Fin's group's three-layer fraud detection architecture alongside a pre-trained model that generates synthetic fraud data for parallel continuous retraining.

**Scheduling complexity in final sessions**: Two groups were displaced from Session 14 due to time overruns. The instructor negotiated presentation order based on travel constraints — a practical reminder that enterprise AI project delivery involves stakeholder management and scheduling complexity as much as technical work.

## Course Conclusion Notes

Session 15 marks the end of Course 06 (GenAI and Pretrained Models). The course covered:
- Transformer architecture and LLM pre-training/fine-tuning/RLHF pipeline
- RAG, multimodal models, image generation
- Agentic frameworks and orchestration
- Future trends (Session 11 non-technical capstone)
- Enterprise deployment mechanics (Session 13)
- Group projects applying GenAI to real business problems (Sessions 14–15)

Peer evaluation scores were submitted via Google Forms collected by the UpGrad team; instructor score weighted at 60%, peer scores at 40%.

## Related

[[deep-learning]] | [[transfer-learning]] | [[ai-paradigms]] | [[course-06-session-14-summary]] | [[course-06-session-13-summary]] | [[course-06-session-11-summary]] | [[course-06-overview-genai-and-pretrained-models]]
