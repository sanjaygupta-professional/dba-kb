---
title: AI Paradigms
category: concepts
tags: ["#ai/foundations"]
sources:
  - "_raw/dba-course/Course_04_Foundations_ML_and_AI/02_Recordings_and_PPTs/Session_01_20Sep2025/20250920_Overview.pdf"
created: 2026-04-12
updated: 2026-04-12
summary: "Taxonomy distinguishing Symbolic AI, Machine Learning, Agentic AI, and Composite AI — the lens for choosing an approach to a problem."
provenance:
  extracted: 0.65
  inferred: 0.35
  ambiguous: 0.0
---

# AI Paradigms

A four-way cut surfaced in [[course-04-session-01-20250920-overview|Course_04 Session 01]] used to position AI approaches:

| Paradigm | Core idea | Typical problem fit |
|---|---|---|
| **Symbolic AI** | Explicit rules, logic, knowledge graphs | Compliance checking, regulatory logic |
| **Machine Learning** | Statistical learning from data | Classification, regression, clustering |
| **Agentic AI** | LLM-driven planning + tool use | Open-ended tasks, research assistants |
| **Composite AI** | Hybrid of the above, orchestrated per sub-problem | Real-world applications where no single approach fits |

## Paradigm Selection Guide

```mermaid
flowchart TD
    A([Business Problem]) --> B{"Is the decision rule<br/>explicit and codifiable?"}
    B -->|Yes| C["Symbolic AI<br/>Rules · Logic · Knowledge Graphs"]
    B -->|No| D{"Is labelled training<br/>data available?"}
    D -->|Yes| E["Machine Learning<br/>Classification · Regression · Clustering"]
    D -->|No| F{"Open-ended task?<br/>Needs planning + tool use?"}
    F -->|Yes| G["Agentic AI<br/>LLM + tools + memory"]
    F -->|"Multiple sub-problems<br/>with different needs"| H["Composite AI<br/>Orchestrate Symbolic + ML + Agentic"]

    style C fill:#e8f4fd,stroke:#0066cc
    style E fill:#e8f8e8,stroke:#006600
    style G fill:#fdf3e8,stroke:#cc6600
    style H fill:#f3e8fd,stroke:#6600cc
```

## Applied example

In [[concepts/vibe-coding|the vibe-coding fraud-detection demo]], the Agentic AI path delegated fraud detection to LLMs directly; the Composite AI path combined symbolic rules, ML classifiers, and GenAI. The deck compared the two paths on the same train/test split.

## Why DBA candidates should care

Different business functions fit different paradigms — see [[concepts/ai-in-business-functions|AI in business functions]]. Research-grade work should justify paradigm selection with respect to the problem structure ^[inferred].

## Paradigm selection in practice

Paradigm choice is *part of* AI strategy, not the starting point. The [[concepts/ai-project-strategy|AI Project Strategy]] framework (Course 07) recommends removing the AI hat first to define strategy and decision logic — the paradigm surfaces naturally at Layer 2 once the business decision is clear. ^[inferred]

## Related

- [[concepts/vibe-coding|Vibe coding]]
- [[concepts/ai-in-business-functions|AI in business functions]]
- [[course-04-session-01-20250920-overview|Course_04 Session 01]]
- [[ai-in-business-functions|AI in Business Functions]]
- [[doctoral-research-methodology|Doctoral Research Methodology]]
- [[concepts/ai-project-strategy|AI Project Strategy]] — strategic layer above paradigm selection
