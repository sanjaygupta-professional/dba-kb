---
title: "AI Project Design and Execution — Session 02"
category: references
tags: ["#src/course", "#dba/coursework", "#dba/program", "#biz/strategy", "#ai/implementation"]
sources:
  - "/mnt/c/Users/csp/Workspace/dba/DBA-Emerging-Technologies-GenAI/Course_07_AI_Project_Design_Execution/02_Recordings_and_PPTs/Session_02/Session_02.md"
  - "/mnt/c/Users/csp/Workspace/dba/DBA-Emerging-Technologies-GenAI/Course_07_AI_Project_Design_Execution/02_Recordings_and_PPTs/Session_02/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Course 07 Session 02 — DBA thesis selection framework (3 modes, golden dataset, DBA vs PhD scope) and strategic objectives workshop."
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
---

# AI Project Design and Execution — Session 02

**Course**: [[course-07-overview-ai-project-design-and-execution|AI Project Design and Execution]] (Course 07)  
**Instructor**: [[prof-dakshina-morti|Prof. Morty]]  
**YouTube**: [Session 02](https://www.youtube.com/watch?v=lSIPmJZVVdA)

## DBA Thesis Selection Framework

Responding to the cohort question "how do we pick and plan our thesis?", Prof. Morty outlined a structured framework. This is the most direct guidance in the course on DBA research strategy.

### Principle 1 — Marry AI to Domain Expertise

> "A DBA is not just about doing amazing AI work. It is about marrying AI to the work experience that you got, to the field where you know quite a bit already."

Unless driven by strong external passion, thesis topic should sit at the intersection of:
- **AI methods** (what you learnt in Courses 03–06)
- **Your professional domain** (what you've done for 10–20+ years)

Your thesis advisor will typically bring AI depth; you bring domain depth. Play to that strength.

### Principle 2 — Choose the Right Output Mode

Select the thesis mode based on career ambition, not academic convention:

| Mode | Career path | Additional artifact |
|---|---|---|
| **Research paper** | Academic faculty / scientist | Design a short course marrying AI + domain; start applying for adjunct roles at 50% thesis completion |
| **Book** | Executive / senior leader | Convert to podcast or video series — boards and CEOs consume audio/video, not papers |
| **Product / startup** | Entrepreneur | Patent only if genuinely architectural; build a golden dataset instead |

For all modes: *targeted reach over mass appeal*. Enough if 20–50 board members of top companies engage with your work — not millions.

### Principle 3 — Golden Dataset Strategy (Product Mode)

Prof. Morty's own approach, applied to regulatory affairs in pharma:
1. Pick a domain with high technical complexity
2. Build a gold-standard Q&A dataset for that domain
3. Show that a small, specialised model (20–50B) outperforms GPT-4 / Gemini on that benchmark
4. This is a compelling story for: (a) DBA committee, (b) VCs / product stakeholders

> "A 50 billion or 20 billion model is able to beat ChatGPT in that particular domain along with absolute guidance on why it came to that conclusion."

### Principle 4 — DBA vs PhD Scope

| DBA focus | PhD focus |
|---|---|
| Governance, ROI, process integration | Algorithm design, novel methods |
| Business practice applicability | Novelty in the technical literature |
| Implementation feasibility | Mathematical rigour |
| Guardrails, change management, trust | Deep ablation studies |

A DBA thesis *can* include deep technical work — but it must be anchored by a clear business objective, governance implication, or ROI case. The business case must be the primary frame.

Examples:
- ✓ *How should insurance companies validate accident claims in real time using AI?* — focuses on framework and guardrails, algorithm is one component
- ✓ *Designing evals for GenAI in pharmaceutical supply chain* — evaluation framework as the thesis (took an entire thesis)
- ✗ *A novel ML model for network attack detection* — too algorithm-centric without business frame

### Principle 5 — High-Value Thesis Topics

Recommended focus areas where DBA candidates have outsized advantage:

1. **Evals** — designing evaluation frameworks for GenAI in your specific industry; highly domain-specific, no one else can do it as well
2. **Guardrails and governance** — responsible AI compliance for your domain
3. **Change management and adoption inertia** — human and organisational resistance to AI
4. **Workflow integration** — how AI fits into existing enterprise processes

## Strategic Objectives Workshop

Continuation of the [[course-07-session-01-summary|Session 01]] framework. Teams broke out into groups to develop AI strategy proposals using the structured format:

**Good strategic objective = WHO × WHAT decision × WHICH workflow × WHEN × WHY × WHAT VALUE**

Requirements for a well-formed strategic objective:
- **Quantify value** — "customer retention can increase by 10%", not "significantly improve"
- **Name the segment** — "top 10% of customers by revenue", not "customers"
- **Specify decision support or automation** — what does the AI actually decide or recommend?
- **Specify workflow touch-point** — CRM integration? Email alert? Separate portal?

**Prioritisation rubric** (for ranking multiple initiatives):
- Gain estimate (quantified £/$)
- Pain score: technology readiness + data readiness + change management effort
- Priority = best combination of high gain + low pain
- R&D-type problems typically rank third but can be high-impact long-term

**AI vs. non-AI decision test**:
- Good fit for AI: repeatable, clearly measurable, needs to scale
- Poor fit for AI: one-off decisions, opaque success criteria, no training data

## Related

- [[course-07-session-01-summary|Session 01]] — AI Crush vs AI Strategy, 3-layer framework
- [[course-07-overview-ai-project-design-and-execution|Course 07 Overview]]
- [[concepts/doctoral-research-methodology|Doctoral Research Methodology]] — updated with Course 07 thesis framework
- [[concepts/ai-project-strategy|AI Project Strategy]]
- [[prof-dakshina-morti|Prof. Dakshina Morti V Kuru]]
