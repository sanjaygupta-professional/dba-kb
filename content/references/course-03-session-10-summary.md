---
title: "Emerging Digital Technologies — Session 10: Robotic Process Automation (RPA)"
category: references
tags: ["#src/course", "#dba/coursework", "#emerging-digital-technologies"]
sources:
  - "_raw/dba-course/Course_03_Emerging_Digital_Technologies/02_Recordings_and_PPTs/Session_10/transcript.txt"
created: 2026-04-13
updated: 2026-04-13
summary: "Dr. Vinay Chadri introduces Robotic Process Automation — covering what RPA bots are, how they differ from AI agents, the spectrum from basic to intelligent process automation, and the real-world ROI and change-management considerations that DBA leaders must weigh when adopting automation."
---

# Emerging Digital Technologies — Session 10: Robotic Process Automation (RPA)

**Instructor**: Dr. Vinay Chadri (Associate Director and Global Professor of Practice, GGU)
**Date**: Session 10 (recorded; exact date not stated in transcript)
**Course**: Emerging Digital Technologies (Course 03)

Session 10 is an introduction to Robotic Process Automation (RPA) delivered by Dr. Vinay Chadri, a PhD in IoT and AI whose applied expertise spans data science, RPA, AI/ML, and industrial IoT. The session opens with a knowledge-check poll that surfaces the class's existing familiarity with RPA, then decodes the term word by word — establishing that "robotic" refers to software bots, not physical devices, and "process automation" refers to executing multi-step repetitive tasks without human intervention. The instructor deliberately keeps the session agenda open to encourage bidirectional discussion, and most of the substantive content emerges through a rich back-and-forth with participants who bring live industry experience from banking, healthcare, semiconductor manufacturing, construction, and enterprise ERP environments.

The bulk of the session is spent drawing the line between RPA bots and AI agents, examining where each technology wins and where it fails, and building toward the concept of Intelligent Process Automation (IPA) — the hybrid model that combines rule-based RPA execution with AI-driven decision making. A recurring theme is that DBA leaders must understand the *limitations* of any technology as clearly as its capabilities, and that automation decisions should always be anchored to a well-defined ROI case and a realistic change-management plan. The session closes with a practical preview: participants are instructed to download UiPath Studio (free community edition) ahead of upcoming hands-on sessions, and the instructor also mentions Microsoft Power Automate / Power Apps as complementary tools worth exploring.

Throughout the discussion, participants raise sharp challenges — including the classic API-vs-bot debate, the security risk of granting bots ERP access, the scalability fragility of RPA when upstream systems change, and the politically loaded question of whether automation replaces workers or merely repurposes them. Dr. Chadri navigates all of these with a practitioner's nuance, consistently redirecting the group toward the insight that the right frame is *productivity enhancement and scale*, not headcount reduction for its own sake.

## Key Concepts

- **RPA defined: software bots, not physical robots** — The word "robotic" in RPA does not refer to mechanical devices. It refers to computer-coded software programs — autonomous bots — that mimic human interactions with digital systems. Leading platforms such as UiPath and Automation Anywhere provide drag-and-drop, no-code or low-code interfaces so that non-engineers can design and operate bots. The bots execute cross-functional, cross-application, cross-platform tasks by following a defined sequence of rules, much like a combination of macros packaged into a single deployable unit.

- **Attended vs. unattended bots** — Attended bots (also called Robotic Desktop Automation, RDA) run on a user's local PC and require a human to initiate each session; decision-making authority remains with the user. Unattended bots run on central servers, can be started, stopped, scheduled, and audited remotely, and operate autonomously without user intervention for the duration of a task. Most real-world RPA deployments use a mix of both modes depending on the sensitivity of the process and the governance appetite of the organization.

- **Structured vs. unstructured data: RPA's primary boundary** — RPA bots excel at structured data — tabular records, forms, spreadsheets, ERP extracts. Approximately 70–80% of current RPA use cases operate on purely structured data. Semi-structured data (addresses, email fields) is handled with caveats, and truly unstructured data (free-text documents, handwritten forms, images) requires additional AI capabilities such as computer vision or NLP before RPA can engage. Invoice processing is a common example where structure is maintained even though the data *looks* unstructured.

- **RPA vs. AI agents: the key distinctions** — AI agents are more intelligent than RPA bots because they can reason over a wide corpus, use real-time memory, adapt from prior interactions, and handle both structured and unstructured data. RPA bots, by contrast, operate on explicit rule-based logic and are 80–90% under human oversight. However, for pure repetitive structured tasks, bots outperform agents on cost, ESG (energy/environmental) metrics, and precision of error handling — because their narrow scope means there is no risk of hallucination. The instructor summarizes: RPA is the obedient office clerk who follows a step-by-step checklist; an AI agent is the smart colleague who understands the goal, picks the best path, and improvises when needed.

- **Error handling and hallucination risk** — A nuanced point raised in discussion is that AI agents — precisely because their learning horizon is wide — may exhibit hallucination-like behavior on small, syntactical, or process-specific errors, while RPA bots handle such errors predictably within their narrow rule set. Advanced RPA platforms do include self-healing mechanisms (recursive DOM scanning, object re-detection) that recover from UI changes without agent-level intelligence. The conclusion is that error-handling superiority depends entirely on task type: process-bound errors favor bots; open-ended reasoning errors favor agents.

- **RPA vs. API integrations** — A live debate in the session concerns why organizations use RPA bots rather than hard-coded API integrations between systems. The consensus answer is flexibility and accessibility: APIs are contractual and rigid — changing a downstream system requires renegotiating and rebuilding the interface. RPA bots, being no-code or low-code, can be updated by non-technical HR or finance executives without full redevelopment. The trade-off is that APIs offer more formal guarantees about data fidelity and system-to-system contracts, while bots are best-effort and fragile when upstream formats change without warning.

- **Automation maturity spectrum: Basic → Intermediate → Intelligent** — Dr. Chadri presents a three-stage model of automation maturity. *Basic automation* (RDA/macro level) covers single-script tasks such as renaming files, auto-formatting Excel, or copying emails to a tracker. *Intermediate automation* (classic RPA) covers end-to-end workflow execution on structured data — payroll processing, invoice generation, CSV reconciliation, chatbots handling FAQ queries. *Intelligent Process Automation (IPA)* is the advanced stage: RPA combined with ML, NLP, predictive analytics, and big data — enabling fraud detection, real-time sentiment analysis in chatbots, and AI-assisted insurance claim processing.

- **Intelligent Process Automation (IPA) — RPA + AI** — IPA is the term for the integration of RPA (which performs the task) and AI (which thinks about the task). In an insurance-claims scenario, RPA ingests the claim data and populates forms; AI analyzes historical claims from the same vendor, detects anomalies, and recommends an action. IPA is *not* the same as agentic AI: IPA's AI component is scoped to a specific domain or task, while an agentic AI system integrates with databases, APIs, and RPA bots simultaneously at a much broader scope, adapting and improving in real time via large language model connections.

- **Automation pyramid: from RPA to Augmented IPA to Autonomous Agents** — The instructor describes a cognitive-complexity pyramid. At the base sits RPA (rule-based, structured data, low complexity, high repetition). One level up is IPA (context-aware, fuzzy NLP, moderate complexity). Above that is Augmented IPA, where knowledge augmentation by human users remains essential and documentation is user-controlled. At the apex sit fully autonomous agents, which handle all data types, make self-directed decisions, and require minimal human intervention. RPA is correctly understood as "Automation 1.0" — the foundation layer — with agentic AI as the emerging successor.

- **ROI as the anchor decision criterion** — Every technology-adoption discussion in the session returns to ROI. Before deploying RPA, organizations must quantify efficiency gains in concrete terms — FTE reduction, throughput increase, error-rate improvement — and present these as a business case to boards and CFOs. The instructor stresses that if the efficiency gain does not materialize as a measurable number (e.g., "8 people's work now done by 2, freeing 6 for higher-value roles or allowing 4x scale without new hiring"), the project will not get funded and should not be proposed.

- **RPA does not automatically replace workers — but it can** — A rich debate explores whether RPA replaces or repurposes people. The instructor's position: technology is intended for productivity enhancement, not headcount elimination, but in practice some roles do become redundant, and honest business cases presented to boards must acknowledge this. The more constructive framing is "repurpose" — freed-up capacity is redeployed toward higher-skill or higher-volume work. The business case should model the *scale expansion* scenario (same workforce, more output) rather than the *cost-cutting* scenario (same output, fewer people), because scale expansion is the more defensible long-term narrative.

- **Change management as an ongoing RPA challenge** — Real-world participants note that RPA's greatest fragility is change: if an upstream ERP system changes its file format, field names, or authentication, the bot breaks and must be rebuilt from scratch. Unlike code-level APIs, there is no formal "contract" between an RPA bot and the systems it interacts with. This creates ongoing maintenance cost that erodes ROI over time. Change management — involving multiple teams, clear governance, and escalation protocols — is therefore mandatory for any RPA deployment at scale.

- **Governance, ethics, and security in RPA** — Ethics in RPA is primarily a *rule-framing* problem: once the rules are set and the bot deployed, the bot simply executes. Ethical responsibility therefore falls entirely on the humans who design the rules. Security concerns focus on ERP access: granting a third-party RPA platform (like UiPath) direct access to a central ERP is a significant enterprise decision requiring collective approval, NDA agreements with vendors, and possibly service account controls running on isolated VMs or remote desktops. The instructor favors attended-bot architectures precisely because they limit the blast radius of a security incident.

- **RPA's historical lineage: screen scraping to IPA** — RPA did not emerge from nowhere; it evolved from screen scraping (capturing data visible on a screen), then configuration/scripting, then business process management (BPM) tools that defined workflow standards, then packaged APIs. The term RPA as a distinct category is approximately 15–17 years old. Modern platforms layer drag-and-drop UI design on top of this lineage, making automation accessible to non-programmers for the first time.

## Technologies / Frameworks Discussed

| Technology | Type | Key Point |
|---|---|---|
| UiPath | RPA platform (market leader) | No-code/low-code drag-and-drop interface; free community/student edition available; used in session demos |
| Automation Anywhere | RPA platform | UiPath's closest market competitor; broadly comparable feature set |
| Blue Prism | RPA platform | Older enterprise-grade RPA tool; mentioned by a participant from prior experience |
| Microsoft Power Automate | Workflow/RPA tool | Integrates natively with Microsoft 365 ecosystem; complements Power Apps |
| Microsoft Power Apps | Low-code app builder | Instructor plans to demo alongside Power Automate in a future session |
| Hugging Face (huggingface.com) | AI model/agent repository | Instructor recommends as a discovery resource for AI agent frameworks and open/closed tools |
| GPT (ChatGPT / GPT-5) | Large language model | Used by instructor as a live anecdote about intent detection and frustration-driven prompt engineering |
| Google AI Overview | Search AI assistant | Cited as an example of real-time learning risk — the bot gave conflicting answers about a bank holiday within minutes of each other |
| SAP / Oracle ERP | Enterprise systems | Discussed as the upstream data sources that RPA bots interact with (and whose access must be carefully governed) |
| Zoho / Salesforce | SaaS platforms | Mentioned as examples spanning all three automation levels (basic, intermediate, advanced) |
| Selenium | Browser automation | Raised by a participant as an engineer-level automation alternative to RPA platforms |

## Important Examples and Case Studies

**The ERP-to-Excel payroll workflow** — The instructor walks through a canonical five-step human task: (1) download data from ERP, (2) open Excel, (3) filter by employee ID, (4) copy filtered data, (5) paste into a new file. He uses this to illustrate which steps can be automated (all of them, in principle) and what the attended vs. unattended distinction means in practice. The debate that follows — whether to give RPA bots direct ERP access — anchors the security and governance discussion. The instructor personally prefers attended-bot architecture for ERP-connected tasks to preserve auditability.

**Invoice processing as the canonical RPA use case** — Multiple participants reference invoice generation and processing. Dr. Chadri uses this to demonstrate RPA's productivity-enhancement value: if a team currently processes 100 invoices in 5 days, RPA can reduce this to 2 days, freeing the team to scale to 200–500 invoices without new hires — giving the sales team a stronger pitch to acquire more clients. He also uses invoice comparison (current invoice vs. historical vendor invoices) to illustrate the additional value that AI brings to IPA over plain RPA.

**Resume / CV screening as a hybrid use case** — A participant raises CV scanning as a process that RPA cannot handle alone (because resumes are unstructured). Dr. Chadri proposes a hybrid pipeline: an RPA bot handles the rule-based initial filter (must have a Master's or PhD → proceed; otherwise → reject), then passes the shortlisted CVs to an AI agent for holistic profile analysis. This example makes the coexistence model concrete and shows how leaders can architect automation pipelines that use each technology where it has comparative advantage.

**Leave application process** — Used to illustrate that even highly automated workflows retain a human decision point: the manager's approval or rejection. Post-approval, the HR notification and payroll update steps can be fully automated. The example grounds the abstract distinction between "fully automatable" and "requires human in the loop."

**Google AI Overview bank holiday hallucination (April 2025)** — The instructor shares a screenshot from his own experience: he asked Google's AI overview "Is this Saturday working for banks?" and received an answer that incorrectly identified April 26 as the *fifth* Saturday of the month (and therefore a working day), when it was actually the *fourth* Saturday (a holiday). A colleague asking the same question minutes later received the corrected answer. This is used as a live case study of real-time model learning — and of the hallucination risk inherent in LLM-based systems even for simple factual queries.

**GPT-5 and frustrated-prompt engineering** — The instructor recounts a personal coding session with GPT-5 in which the model looped through the same error repeatedly. When he wrote an exasperated prompt telling GPT it was "behaving like a child," the model immediately produced a correct answer. A participant interprets this as positive reinforcement / self-boosting prompt strategy, noting that incentivizing language yields better responses than negative framing. The instructor ties this to the insight that LLMs are trained on human psychology and that reinforcement learning from human feedback (RLHF) is foundational to their behavior.

**Banking sector FTE displacement business case** — A participant from banking explains how RPA is typically pitched to boards: quantify efficiency gains as FTE equivalents (e.g., "8 people's work now done by 2"), state whether the saved capacity will be repurposed or eliminated, and compute the ROI curve. This is presented as the realistic view that counters the instructor's more conservative "technology never replaces people" framing — in banking, the business case explicitly models FTE reduction as the primary efficiency metric.

**UiPath setup for hands-on sessions** — At the close of the session, the instructor walks participants through creating a free UiPath account and downloading UiPath Studio (desktop version). He confirms that a free student license is available without payment information, and that the cloud-based UiPath Studio Online will also be used. Participants are also directed to set up Microsoft accounts for Power Apps / Power Automate demos in a future session.

## Related

- [[course-03-overview-emerging-digital-technologies|Course 03 Overview]]
- [[robotic-process-automation|Robotic Process Automation (RPA)]]
- [[intelligent-process-automation|Intelligent Process Automation (IPA)]]
- [[ai-agents|AI Agents and Agentic AI]]
- [[uipath|UiPath Platform]]
- [[automation-anywhere|Automation Anywhere]]
- [[business-process-management|Business Process Management (BPM)]]
- [[change-management|Change Management]]
- [[roi-technology-adoption|ROI and Technology Adoption]]
- [[no-code-low-code|No-Code / Low-Code Platforms]]
- [[nlp-natural-language-processing|Natural Language Processing (NLP)]]
- [[computer-vision|Computer Vision]]
- [[reinforcement-learning-from-human-feedback|Reinforcement Learning from Human Feedback (RLHF)]]
- [[erp-systems|ERP Systems (SAP, Oracle)]]
- [[dr-vinay-chadri|Dr. Vinay Chadri]]
