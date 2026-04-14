---
title: "Emerging Digital Technologies — Session 05: Quantum Computing — Principles, Algorithms, and Business Implications"
category: references
tags: ["#src/course", "#dba/coursework", "#emerging-digital-technologies"]
sources:
  - "_raw/dba-course/Course_03_Emerging_Digital_Technologies/02_Recordings_and_PPTs/Session_05/transcript.txt"
created: 2026-04-13
updated: 2026-04-13
summary: "Dr. Raj surveys quantum computing from first principles — qubits, superposition, and entanglement — through landmark algorithms (Shor, Grover, QFT) to its cross-sector business implications in security, AI, IoT, blockchain, and 6G, while being candid that the technology remains largely theoretical and is roughly 10 years from general-purpose maturity."
---

# Emerging Digital Technologies — Session 05: Quantum Computing — Principles, Algorithms, and Business Implications

**Instructor**: Dr. Raj (referred to as "Dr. Raj" throughout; visiting professor with a PhD from IISc Bangalore, post-doctoral fellowship at Kyushu University in quantum finite automata, ca. 2000; industry background includes roles at Jio)
**Date**: Session 05 (recorded; transcript downloaded 2026-04-12)
**Course**: Emerging Digital Technologies (Course 03)

Session 5 is the course's dedicated deep-dive into quantum computing — a technology Dr. Raj situates at the very frontier of what is theoretically understood and practically achievable. The session opens by placing quantum computing inside the Gartner Top 10 emerging technologies list and frames it as a "next-generation high-performance computing" paradigm that will eventually transcend today's parallel supercomputing. Dr. Raj is unusually candid about the gap between promise and reality: after 25 years of research dating back to his own post-doctoral work, practical, fault-tolerant, general-purpose quantum computers do not yet exist. He pegs realistic availability at roughly 10 years out, pointing to IBM's 2029 target and Google's 2030 roadmap as anchor milestones.

The bulk of the session covers three interlocking layers. First, the physics substrate: quantum mechanics, superposition, entanglement, and the qubit as a mathematical object represented by two complex numbers (alpha, beta) whose squared norms sum to one. Second, the landmark algorithms — Shor's, Grover's, and Quantum Fourier Transform — that first demonstrated what quantum speedup means in concrete computational terms. Third, and most relevant to a DBA cohort, the cross-sector business implications: cryptography vulnerability and post-quantum defences, drug discovery and genomics, material science, AI acceleration, supply-chain and logistics optimisation, climate modelling, financial portfolio optimisation, airport gate management, quantum-IoT security via QKD, blockchain enhancement, and the emerging 6G communication layer where quantum cryptography will be natively embedded.

Dr. Raj closes with an honest assessment of what remains unsolved — maintaining quantum coherence at near-absolute-zero temperatures, noise and error correction, QPU scalability, and the integration challenge with classical infrastructure — and answers student questions about how business professionals without technical backgrounds should orient themselves to these technologies.

## Key Concepts

- **Quantum Mechanics as the Physics Foundation** — Unlike classical and machine-learning technologies that rest primarily on mathematics, quantum computing is grounded in physics: the behaviour of matter at atomic and subatomic scales. Dr. Raj repeatedly stresses that a physicist is better positioned to intuitively explain quantum phenomena than a mathematician or IT engineer, and that this represents a genuine paradigm shift in how computing researchers must think.

- **Qubit (Quantum Bit)** — The fundamental unit of quantum information. A qubit state is represented by two complex numbers (α, β) satisfying |α|² + |β|² = 1. Because the representation requires complex numbers (needing a two-dimensional plane, not a real-number line), a qubit can simultaneously inhabit many states beyond the binary 0 or 1 of a classical bit. Today's physical quantum computers operate with roughly 20 qubits — insufficient for real-world advantage — while systems of hundreds or thousands of fault-tolerant qubits are the target horizon.

- **Superposition** — The quantum principle by which a qubit is not constrained to be in state 0 or state 1 but can exist in any combination of all possible states concurrently. Each state in superposition can act as an independent processor, and that is the mechanism through which quantum computers achieve massively parallel computation without requiring separate physical processors for each parallel thread.

- **Entanglement** — The quantum property by which two or more qubits become correlated so that a change in one instantaneously affects the other, regardless of distance. Entanglement enables parallel computation across multiple qubits acting in concert and also provides an intrinsic security guarantee: any external tampering with one entangled qubit collapses the entangled state, revealing the intrusion. Quantum Key Distribution (QKD) exploits this property directly.

- **Classical vs. Quantum Computing Architecture** — Classical computers use transistors and binary logic; quantum computers use superconducting circuits, trapped ions, or neutral atoms as the physical substrate for qubits. Current efforts largely occupy a hybrid space — exemplified by the German QX/SuMu-CG project (20-qubit QPU integrated with a classical supercomputer) and Nvidia's CUDA-Quantum library bridging GPU and QPU — because quantum hardware alone is too fragile and limited to replace classical systems.

- **High-Performance Computing (HPC) and the Quantum Trajectory** — Dr. Raj defines HPC as the discipline of closing the gap between theoretical and practical computational speed. Today's HPC is achieved through parallel computing: splitting a task across multiple CPUs or GPUs so that what takes 10 hours sequentially takes 1 hour with 10 processors. Quantum computing is framed as the next evolutionary step — millions of times more powerful than classical parallel supercomputers — and the concept of "quantum-centric supercomputing" (QPUs supplementing classical supercomputers) is the near-term integration model. Exa-scale classical supercomputers (roughly 10^18 operations per second) are themselves thousands of times slower than what full quantum computing promises.

- **Shor's Algorithm** — Developed by Peter Shor, this is the seminal quantum algorithm that poses an existential threat to current asymmetric cryptography. RSA and elliptic-curve cryptography (ECC) derive their security from the computational intractability of factorising large integers into prime factors — a task that would take a classical computer years or centuries for sufficiently large numbers. Shor's algorithm, using quantum period-finding and modular exponentiation, can accomplish the same factorisation in minutes to hours. When a sufficiently powerful quantum computer exists (hundreds to thousands of logical qubits), all RSA-encrypted financial and healthcare data in the world becomes vulnerable.

- **Grover's Algorithm** — A quantum search algorithm that searches an unsorted database of N items in O(√N) time versus the O(N) time required by classical sequential search. Concretely, a database of 64 items that a classical computer searches in 64 steps can be searched by Grover's algorithm in 8 steps (√64 = 8). The speedup grows more dramatic at scale, making Grover's algorithm significant for any large-scale data retrieval or optimisation problem.

- **Quantum Fourier Transform (QFT)** — The quantum analogue of the classical Discrete Fourier Transform used in signal processing (conversion between frequency and time domains). QFT achieves exponentially faster transformation using superposition and entanglement; a Python implementation exists and is fully coded. QFT is also a subroutine inside Shor's algorithm.

- **Optimisation and NP-Hard Problems** — A class of problems for which no deterministic polynomial-time classical algorithm exists: solutions can only be approximated heuristically and in exponential time at scale. The Travelling Salesman Problem and airport gate assignment are canonical examples. Quantum algorithms — particularly Variational Quantum Eigensolver (VQE) and quantum annealing — can solve or significantly accelerate NP-hard optimisation problems that classical computers cannot handle in reasonable time, making this the most commercially immediate value proposition of quantum computing.

- **Post-Quantum Cryptography (PQC)** — Because Shor's algorithm will eventually break RSA and ECC, new cryptographic algorithms are being designed that remain secure even against a quantum adversary. The main PQC families are: lattice-based cryptography (hard geometry problems that quantum computers cannot exploit), multivariate cryptography (systems of polynomial equations over finite fields), hash-based cryptography (leveraging collision-resistant hash functions), and code-based cryptography (error-correcting codes that collapse under attack). Advanced Encryption Standard (AES) with 128-bit symmetric keys is noted as currently quantum-resistant; it is asymmetric public-key schemes that are at risk. 6G networks, expected around 2032, are projected to embed PQC natively.

- **Quantum Key Distribution (QKD)** — A quantum-physics-based mechanism for securely sharing encryption keys between parties. When a key is transmitted as quantum states, any eavesdropping attempt disturbs the entangled state, alerting both parties to the intrusion. QKD addresses the hardest part of public-key cryptography — safe key exchange — and is the primary near-term practical application of quantum mechanics to cybersecurity, including securing IoT sensor data streams.

- **Quantum-Centric Supercomputing and Hybrid Architecture** — The practitioner consensus for the coming decade is a hybrid model: classical computers (CPUs, GPUs) handle data pre- and post-processing, while QPUs tackle specific computationally intractable sub-problems. This mirrors the GPU-CPU split in today's AI training pipelines. Quantum computing is therefore not a replacement for classical infrastructure but a specialised accelerator for a defined class of hard problems.

- **Quantum Cloud Computing (Quantum-as-a-Service)** — Major cloud providers — IBM, Google, AWS, and Microsoft Azure — already offer remote access to quantum simulators, emulators, and early quantum processors through their cloud platforms. IBM provides Qiskit; PennyLane is a prominent open-source library. For academic and research use, access is often free. Cloud delivery removes the need to manage the extreme operating conditions (near absolute zero, −270 °C, maintained via helium cooling) required by physical QPUs, making quantum experimentation accessible to researchers globally.

## Technologies / Frameworks Discussed

| Technology | Type | Key Point |
|---|---|---|
| Shor's Algorithm | Quantum algorithm | Factors large integers in polynomial time; threatens RSA and ECC encryption |
| Grover's Algorithm | Quantum algorithm | Searches unsorted databases in O(√N); quadratic speedup over classical sequential search |
| Quantum Fourier Transform (QFT) | Quantum algorithm | Quantum analogue of Discrete Fourier Transform; exponentially faster; subroutine in Shor's algorithm |
| Variational Quantum Eigensolver (VQE) | Quantum algorithm | Hybrid classical-quantum solver for optimisation and chemistry simulation problems |
| Quantum Key Distribution (QKD) | Quantum security protocol | Physics-guaranteed secure key sharing; intrusion collapses the quantum state and is self-revealing |
| Lattice-Based Cryptography | Post-quantum cryptography | Resistant to quantum attack; based on hard geometry problems in high-dimensional lattices |
| Multivariate Cryptography | Post-quantum cryptography | Uses systems of multivariate polynomials; cannot be broken by quantum computers |
| Hash-Based Cryptography | Post-quantum cryptography | Leverages collision-resistant hash functions; quantum resistant |
| Code-Based Cryptography | Post-quantum cryptography | Error-correcting codes that collapse under attack, exposing intrusion attempts |
| AES-128 (Symmetric Encryption) | Classical crypto (quantum-resistant) | Symmetric key crypto is not broken by Shor's algorithm; quantum threat is to asymmetric schemes |
| Qiskit (IBM) | Quantum development platform | IBM's SDK for programming and running quantum circuits on IBM quantum hardware/simulators |
| PennyLane | Quantum development library | Open-source Python library for quantum machine learning and quantum algorithm development |
| CUDA-Quantum (Nvidia) | Hybrid integration library | Bridges Nvidia GPU (data pre/post-processing) with QPU (core computation) |
| Quantum Cloud (IBM / Google / AWS / Azure) | Quantum-as-a-Service | Remote access to quantum simulators and early QPUs; managed infrastructure, no specialised hardware needed |
| Superconducting Circuits | QPU physical substrate | One approach to building qubits; used by IBM and Google |
| Trapped Ions / Neutral Atoms | QPU physical substrate | Alternative qubit substrates under active research; different trade-offs in coherence and gate fidelity |
| 6G Communication | Future network standard | Expected ~2032; will natively embed quantum-safe cryptography; operates at terahertz frequencies |

## Important Examples and Case Studies

**Airport Gate Assignment Problem.** Dr. Raj uses this as the most vivid optimisation illustration. With 5 gates and 1 aircraft, there are 5 possible assignments. With 5 gates and 2 aircraft, 25. With 15 gates and 25 aircraft, the combinations explode to 570 billion — far beyond what a human scheduler or classical heuristic can optimise efficiently. A 256-qubit quantum computer from QA (Pasqal) is already demonstrated solving the Maximum Independent Set (MIS) graph problem, which many industrial optimisation problems — including gate assignment — can be reformulated as. Lufthansa is cited as having implemented a quantum-assisted gate optimisation system using the Qstrat algorithm.

**RSA Encryption Vulnerability.** All financial transactions globally rely on the computational hardness of integer factorisation (RSA algorithm). A classical computer would need centuries to break a 2048-bit RSA key. Shor's algorithm running on a sufficiently powerful quantum computer (estimates suggest ~4,000 logical qubits for RSA-2048) could do it in hours. This is not theoretical: IBM has committed to demonstrating meaningful quantum advantage by 2029, and Google by 2030. The implication for any DBA-level leader is that data classified today as "securely encrypted" could be at risk within a decade.

**Genomics and Drug Discovery.** Human DNA contains 3 billion base pairs (adenine-thymine, cytosine-guanine), and a full DNA sequence written out would stretch 3 kilometres on paper. Machine learning models built on classical hardware are already being used to identify protein functions (critical for understanding diseases like cancer), but their accuracy is limited by classical compute. Dr. Raj argues that quantum-generated ML models will achieve significantly higher protein-function prediction accuracy, enabling faster and more precise drug design and personalised medicine.

**Jio Allergy Knowledge Graph.** Dr. Raj shares an anecdote from Jio, where a team spent four years manually building a healthcare knowledge graph ("allergy graph") linking symptoms to diagnoses, medications, and specialists. That work was rendered comparable in scope to a single LLM prompt by the arrival of large language models. He uses this to illustrate both the pace of technology disruption and the role of knowledge graphs (a complex NP-hard graph structure) as a problem class where quantum computing will eventually provide dramatic speedup.

**Quantum-IoT Security.** Trillions of IoT sensors currently generate data that traverses insecure networks. Dr. Raj frames QKD as the correct answer to IoT data security: sensor readings transmitted as quantum states cannot be intercepted without physically collapsing the entangled channel, revealing the attacker. He also notes that quantum computing accelerates real-time big-data processing from IoT streams — the latency of batch processing (collect all day, process at midnight) is eliminated when quantum compute can crunch large multi-structured datasets instantaneously.

**Quantum-Enhanced Blockchain.** Blockchain's known weaknesses — slow transaction throughput (far below Citibank's millions of transactions per minute), high energy consumption from mining consensus, and network latency from decentralised peer-to-peer coordination — can all be addressed by quantum computing. The more urgent vulnerability: blockchain today uses RSA encryption for transaction signing, which Shor's algorithm will break. Post-quantum cryptography integration into blockchain (quantum blockchain) is an active research area.

**Quantum Sensing for Precision Positioning.** Current GPS/GNSS systems achieve metre-level positioning accuracy. Military applications already exploit advances that bring this to centimetres. Dr. Raj references India's precision munitions operations as a real-world benchmark. Quantum sensors — which measure physical quantities using quantum-mechanical effects — can achieve centimetre-scale positioning, providing dramatically better training data for any AI model that depends on location as a feature.

**Instructor's Personal Research Context.** Dr. Raj completed post-doctoral research at Kyushu University (Japan Society for Science and Technology fellowship, 2000–2002) specifically on quantum finite automata. He returned to India due to a family emergency and was absent from the field for over 20 years. He prepared this session by conducting 16 hours per day of research over several days, which speaks to both the depth of the session and his honest acknowledgement of the gap between his 2000-era knowledge and the current state of the art.

## Related

- [[emerging-digital-technologies|Emerging Digital Technologies]] (Course 03)
- [[course-03-overview-emerging-digital-technologies|Course 03 Overview]]
- [[quantum-computing|Quantum Computing]]
- [[cryptography|Cryptography]] — RSA, ECC, AES, and their quantum-resistance status
- [[post-quantum-cryptography|Post-Quantum Cryptography]] — lattice-based, multivariate, hash-based, code-based PQC
- [[quantum-key-distribution|Quantum Key Distribution (QKD)]]
- [[blockchain|Blockchain]] — limitations addressed by quantum integration; quantum vulnerability of RSA
- [[internet-of-things|Internet of Things (IoT)]] — quantum sensing, QKD-secured data transmission
- [[high-performance-computing|High-Performance Computing]] — classical parallel computing vs. quantum-centric supercomputing
- [[artificial-intelligence|Artificial Intelligence]] — quantum-accelerated AI training; path toward AGI via quantum-AI integration
- [[6g-communication|6G Communication]] — quantum-safe networks expected ~2032
- [[optimisation-problems|Optimisation Problems]] — NP-hard, NP-complete; travelling salesman; airport gate assignment
- [[drug-discovery|Drug Discovery and Genomics]] — quantum ML for protein function prediction
- [[cloud-computing|Cloud Computing]] — Quantum-as-a-Service (IBM Qiskit, Google, AWS, Azure)
- [[dr-sumitra-padman|Dr. Sumitra Padman]] — course coordinator; facilitates Q&A and pre-reading commitments
