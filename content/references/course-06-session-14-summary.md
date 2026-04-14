---
title: "GenAI and Pretrained Models — Session 14: Final Project Presentations — Day 1"
category: references
tags: ["#src/course", "#dba/coursework", "#ai/llm", "#ai/transformers"]
sources:
  - "_raw/dba-course/Course_06_GenAI_Pretrained_Models/02_Recordings_and_PPTs/Session_14/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "First day of Course 06 final group project presentations, covering five groups' GenAI solutions across contract intelligence, multi-environment debugging, regulatory compliance, and HR/recruitment automation — evaluated by peers and instructor across business value, technical approach, metrics/validation, and defense of approach."
---

# GenAI and Pretrained Models — Session 14: Final Project Presentations — Day 1

**Course**: [[course-06-overview-genai-and-pretrained-models|GenAI and Pretrained Models]] (Course 06)
**Instructor**: Prof. Ananda
**Session type**: Group project presentations (Day 1 of 2)

## Resources

- [YouTube Recording](https://www.youtube.com/watch?v=cPQQk6xrNfs)
- [Materials (SharePoint)](https://ueducation-my.sharepoint.com/:f:/g/personal/ggugenai_operations_upgrad_com/IgAYRm32RQCiQapUkQ9GAdPtATEeyVaxW2yUGJNKiksK0UE?e=7m9zrC)
- [UpGrad Page](https://learn.upgrad.com/course/8919/segment/64668/397034/1199537/5977339)

---

## Session Structure and Evaluation Framework

Each group was given approximately 20 minutes to present, evaluated across four metrics (scored /10):

| Metric | Description |
|--------|-------------|
| Business value | Market relevance, problem severity, potential impact |
| Technical approach | Architecture soundness, appropriate AI tier selection, feasibility |
| Metrics and validation | How success is measured; ROI analysis; quantitative claims |
| Defense of approach | Justification for choosing GenAI over alternatives; handling Q&A |

**Grading split**: 60% instructor, 40% peer evaluation (all other groups scored each presenting group). Each student downloaded the evaluation sheet and submitted scores to the UpGrad team.

---

## Key Concepts

### Peer Evaluation Design

A notable structural choice: pitches were directed at the entire cohort, not only the instructor. The rationale — professionals with diverse domain expertise can identify business value and feasibility gaps that a single instructor might miss. This also simulates a VC/investor pitch environment where the panel's aggregate judgment matters.

### Project Selection Guidance

Projects were selected from a list of 10 suggested domains, but the instructor explicitly allowed real-world problems from students' organisations. One student (Sanjay) built a contract-reader agent for an actual workplace project. Another group chose a live fraud detection system (Fin's group, using Liquid Neural Networks + pre-trained model for synthetic fraud data generation — a three-layer architecture). The instructor noted preference for novel use cases over repetition.

---

## Project Summaries

### Group 1 — Credentia: Contract Intelligence Platform

**Problem**: SMEs handle contracts (SaaS agreements, supplier contracts, NDAs, partnership agreements) without in-house legal teams. Manual review takes 2–5 days for complex contracts; external legal review is expensive and inconsistent; AI-drafted contracts contain hidden clause interactions that human review misses. Faulty contract management causes ~9% annual contract value revenue leakage.

**Failure modes of existing tools**:
- Rules-based systems: rigid, keyword-dependent, fail on non-standard clause structures
- Traditional ML: requires large labelled datasets; analyses clauses in isolation rather than evaluating holistic contract-level risk arising from clause interactions

**Core innovation — ACRA (Adaptive Contract Risk Agent)**: A reasoning layer that analyses contracts at the document level, not clause level. ACRA compares, connects, and evaluates cross-clause interactions against company policies, regulatory frameworks, and industry benchmarks — replicating human legal reviewer reasoning in a structured, scalable form.

**Architecture (three layers)**:
1. **Multi-model orchestration layer**: Different LLMs assigned to different legal tasks (clause extraction, classification, risk reasoning) — "right model for the right legal problem"
2. **RAG + vector memory**: External knowledge base of jurisdictional databases, company policies, regulatory frameworks — grounds output in verifiable sources, not just model weights
3. **Human-in-the-loop review**: Risk scoring (0–10); high-risk or complex contracts escalated to legal professionals; system enhances rather than replaces human legal expertise

**User workflow**:
1. Upload PDF/Word contract; input jurisdiction and contract value
2. System parses contract into machine-readable clause structures (not flat vectorisation)
3. ACRA runs RAG against knowledge base and assesses cross-clause interactions
4. Output: executive summary in plain language + risk score + negotiation guidance
5. Optional: escalation to human legal expert for validation

**Roadmap (5 phases, 3-year horizon)**:
- Phase 1: Basic GenAI contract upload + review (MVP)
- Phase 2: Multi-RAG solution with company policy integration + pre-built templates
- Phase 3: Jurisdiction-aware review; negotiation support module
- Phase 4: Multi-jurisdictional + multilingual contracts (Arabic/English clause comparison critical for UAE contracts that must be presented in Arabic in court)
- Phase 5: Risk dashboards; common risk pattern identification; automated template updates

**ROI analysis** (SME case):
- 300 contracts/year; 2 hours/contract → 600 hours → $24,000 labour cost
- Credentia reduces to 1 hour/contract → 300 hours saved → $12,000 annual saving at $40/hour
- 20% contracts escalated to external legal ($250/contract × 60 = $15,000) reduced by 3-layer risk scoring
- Break-even claimed within Year 1

**Team**: Dennis (insurance/claims), sales background member, information security + academia background member, Rama (marine engineer, pre-recorded contribution while on maritime duty), Muhammad Zahib Nabil (operations head, Abu Dhabi investment group — problem owner)

---

### Group 4 — CIDRIS: Cross-Environment Intelligent Debugging and Runtime Intelligence System

**Problem**: The canonical developer nightmare — code passes all tests on Mac OS (Python 3.11), fails on Ubuntu 22.04 CI/CD pipeline (Python 3.14), partially works on Alpine Linux staging (Python 3.11), crashes at runtime on Amazon Linux 2 production (Python 3.9). Same codebase; three different failure modes; root cause is not in the code but in the interaction between code, interpreter version, OS, package dependencies, and runtime context.

**Gap in existing tools**: Modern AI coding assistants (Copilot, Cursor, Claude Code, Codex) are trained on source code and excel at code generation but are **blind to the runtime environment**. They cannot diagnose why code fails in production without being manually given context about OS, Python version, dependency trees, and environment configs.

**Solution — CIDRIS (multi-agent debugging team)**:

Hospital ER analogy: an attending physician (orchestrator) coordinates specialised specialists (agents), each expert in one slice of the problem:

| Agent | Specialisation |
|-------|---------------|
| Environment profiler | OS, Python version, system libraries per environment |
| Log analyser | Error logs, stack traces, runtime exceptions |
| Dependency checker | Package versions, dependency trees, compatibility conflicts |
| Security/config agent | Certificate expiry, secret values, config file differences |
| Root cause agent | Aggregates findings → confidence-scored diagnosis with evidence chain |
| Fix generator | Produces targeted code patch informed by full environment context |

**LLM selection by task** (key translator insight):
- Heavy reasoning (root cause analysis, million-token context): Claude Opus 4.6
- Code generation and mid-complexity tasks: Claude 5.3 Codex
- Fast, cheap profiling and config checks: Claude Haiku 4.5

"You don't use a sledgehammer to hang a picture" — appropriate model tier for each task reduces cost and latency without sacrificing accuracy where it matters.

**Workflow**:
1. CI/CD pipeline failure triggers CIDRIS via webhook
2. Docker containers spin up to reproduce each environment identically
3. Four specialist agents run in parallel, analysing logs, dependencies, security configs
4. Root cause agent synthesises findings → diagnosis with confidence score + evidence chain
5. Fix generator produces a code patch with full environment context
6. Patch validated across all environments
7. **Human-in-the-loop governance gate**: developer reviews and approves before any change is merged

**Framework**: LangGraph (state machine framework for multi-agent AI workflows) for orchestrator

**Team**: Vasa, Ajit, Dasha, Prashant, Deepundu

---

## Models/Architectures Discussed

| Model/System | Use |
|---|---|
| Claude Opus 4.6 | Heavy root cause reasoning in CIDRIS; million-token context window for deep log analysis |
| Claude 5.3 Codex | Mid-tier code generation tasks in CIDRIS |
| Claude Haiku 4.5 | Fast, cheap environment profiling and config checks in CIDRIS |
| Multi-model orchestration | Credentia's approach: specialised models per legal task (clause extraction, classification, risk reasoning) |
| RAG + vector store | Credentia: jurisdiction databases, company policies, regulatory frameworks |
| LangGraph | CIDRIS orchestrator framework — state machine for multi-agent AI workflows |
| Docker containers | CIDRIS: environment reproduction for cross-environment debugging |
| Liquid Neural Networks (LNN) | Mentioned for Fin's group fraud detection project — learns dynamically without frozen weights |

## Important Intuitions and Examples

**Clause interaction risk (Credentia)**: A contract clause about liability may appear acceptable in isolation; a payment clause may also appear acceptable in isolation. Their *interaction* — the combined effect — may create unacceptable financial exposure. This is the insight traditional tools miss and ACRA addresses.

**Multilingual contract risk (Credentia)**: In UAE courts, what is written in Arabic takes legal precedence. A company signing an English contract with an Arabic counterparty may have different risk profiles in each language version. ACRA's multilingual roadmap specifically addresses the gap where English and Arabic clause meanings diverge.

**CIDRIS vs. AI coding assistants**: The distinction is important for the translator mindset. Copilot/Cursor/Codex are *code-domain* tools. CIDRIS operates in the *infrastructure and runtime domain*. The bugs CIDRIS addresses are not code bugs — they are environmental interaction bugs. This is a category that existing AI tools structurally cannot see without explicit environment telemetry.

**Multi-model cost optimisation** (CIDRIS, raised explicitly): Running every query through the most expensive model (Opus) is wasteful. A mix of Opus (complex reasoning), Codex (code generation), and Haiku (fast/cheap profiling) delivers the same quality outcome at a fraction of the cost. This is a production engineering principle, not just a demo choice.

**Peer evaluation as pitch discipline**: The 40% peer scoring creates an incentive to present clearly for a non-specialist audience — the same skill needed when pitching AI initiatives to business stakeholders.

## Related

[[deep-learning]] | [[transfer-learning]] | [[ai-paradigms]] | [[course-06-session-13-summary]] | [[course-06-session-15-summary]] | [[course-06-overview-genai-and-pretrained-models]]
