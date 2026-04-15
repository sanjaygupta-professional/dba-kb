---
title: "AI Project Design and Execution — Session 01"
category: references
tags: ["#src/course", "#dba/coursework", "#biz/strategy", "#ai/implementation"]
sources:
  - "/mnt/c/Users/csp/Workspace/dba/DBA-Emerging-Technologies-GenAI/Course_07_AI_Project_Design_Execution/02_Recordings_and_PPTs/Session_01/Session_01.md"
  - "/mnt/c/Users/csp/Workspace/dba/DBA-Emerging-Technologies-GenAI/Course_07_AI_Project_Design_Execution/02_Recordings_and_PPTs/Session_01/transcript.txt"
created: 2026-04-12
updated: 2026-04-14
summary: "Course 07 Session 01 — Prof. Morty introduces the AI Crush vs AI Strategy framework: 60-65% of AI project failures occur at problem selection, not execution."
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
---

# AI Project Design and Execution — Session 01

**Course**: [[course-07-overview-ai-project-design-and-execution|AI Project Design and Execution]] (Course 07)  
**Instructor**: [[prof-dakshina-morti|Dr. Dakshina Morti V Kuru]] ("Professor Morty" or "Morti")  
**YouTube**: [Session 01](https://www.youtube.com/watch?v=Vxo95A60u-o)

## Instructor Background

Prof. Morty (Dakshina Morti V Kuru) is a serial entrepreneur-educator with a material science PhD from Carnegie Mellon. Career arc: CMU → Indian defense (Agni long-range ballistic missile program) → pivoted to AI/analytics in 2000 (chose laptops over furnaces). Currently building **RISI — Regulated Inexpensive Specialized Intelligence**: small groups of LLMs that punch above their weight in specific regulated domains. Has guided 10+ DBA students through to graduation. Self-described "hacker" rather than rigorous researcher; prefers exciting industry solutions.

## Course Purpose: Scientific → Boardroom Mindset

The preceding 6 courses covered algorithms, deep learning, GenAI, and emerging tech — the *science* layer. Course 07's explicit goal: **transform DBA candidates from scientific mindset to boardroom mindset**.

- Boardrooms don't care about the algorithm
- They care about: business value, speed-to-solution, risk minimisation, ROI
- Skill: present AI plans → get board approval → translate back to engineering team

## AI Crush vs AI Strategy

The central concept of the course. Naming:

> "AI Crush" — falling for AI after seeing a cool conference demo, implementing with vague ambition and no strategy.

**Root cause of AI project failure** (Prof. Morty's estimate):
- 90% of AI projects fail to deliver value
- 60–65% of failures: problem selection and planning failures
- ~25% of failures: execution failures (data, cost, technical issues)

Common failure pattern:
1. CEO sees a demo → gets excited → mandates implementation
2. Engineering team builds an impressive demo back → both sides satisfied short-term
3. Value never materialised → project dies

Examples cited:
- CTO of largest steel manufacturer: "Tell me where to apply AI in my plant" — neither CTO nor consultant knows the plant's real problems
- IT services company: "I want 30 engineers and 20 agents" — sounds cool, means nothing
- Pharma company: 10-line script that impressed the chairman but didn't justify business need

**Warning on AI hype cycles** (historical pattern):
- 1959: Perceptron announced → claim of human-level intelligence in 10 years → 1969: AI winter (Minsky/Simon/McCarthy)
- 1990s: Multi-layer perceptrons → similar hype → second AI winter
- Prof. Morty's concern: current LLM hype could trigger a third AI winter that halts real progress

## The 3-Layer Framework: Strategy → Decision → Workflow

The correct sequence for AI project planning (remove the AI hat first):

1. **Strategy** — what business goal am I pursuing? (Define: who, what, why, measurably)
2. **Decision** — what decisions does AI need to make? (Automated vs. augmented)
3. **Workflow** — where and how does the AI output integrate into human work?

**Bad strategy**: "Use AI in customer service L1 and L2" (vague, no measure, no target)  
**Average strategy**: "Increase customer retention by 10%" (clear what, not clear who/how/why)  
**Good strategy**: "Increase top 10% customers' retention by 10% in the top-revenue segment by improving the onboarding experience over Q2" — WHO + WHAT + HOW + WHEN

Key insight: *"Remove the AI hat as much as possible and wear a business hat. The role AI plays will surface naturally in layer 2."*

Classic failure from Morty's own consulting: built a churn predictor → achieved 10× precision improvement → client said "what do I do when I know a customer is churning?" — two completely different data science problems that were never defined upfront.

## Session Activities

Session 01 included a group workshop: breakout rooms to develop strategic objectives for their own business domains and quantify value hypotheses. Not graded — practice for applying framework at workplace.

## Related

- [[course-07-session-02-summary|Session 02]] — DBA thesis framework, strategic objectives workshop
- [[course-07-overview-ai-project-design-and-execution|Course 07 Overview]]
- [[concepts/ai-project-strategy|AI Project Strategy]] — concept page for the AI Crush → Strategy framework
- [[concepts/ai-in-business-functions|AI in Business Functions]]
- [[concepts/doctoral-research-methodology|Doctoral Research Methodology]]
- [[prof-dakshina-morti|Prof. Dakshina Morti V Kuru]]
