---
title: "Emerging Digital Technologies — Session 06: High Performance Computing (HPC) and Computer Architecture Fundamentals"
category: references
tags: ["#src/course", "#dba/coursework", "#emerging-digital-technologies"]
sources:
  - "_raw/dba-course/Course_03_Emerging_Digital_Technologies/02_Recordings_and_PPTs/Session_06/transcript.txt"
created: 2026-04-13
updated: 2026-04-13
summary: "Dr. Suresh walks the cohort from the basic interaction between CPU, RAM, cache, and storage through the fetch-decode-execute cycle, Moore's Law, and the architectural distinction between CPU serial execution and GPU parallelism, arriving at a full explanation of HPC — how it differs from cluster, distributed, and cloud computing — and when (and when not) to deploy it for AI workloads."
---

# Emerging Digital Technologies — Session 06: High Performance Computing (HPC) and Computer Architecture Fundamentals

**Instructor**: Dr. Suresh (referred to throughout as "Dr. Sur" or "Dr. S" by participants)
**Date**: Session recorded and downloaded 2026-04-12; session delivered on a Sunday morning (exact calendar date not stated in transcript)
**Course**: Emerging Digital Technologies (Course 03)

---

Session 6 is an extended technical deep-dive into hardware fundamentals and High Performance Computing. Dr. Suresh opens with a five-question warm-up quiz on CPU, GPU, RAM, VRAM, and storage to calibrate the cohort's baseline knowledge, then works systematically from the most elementary components of a desktop computer — storage (HDD/SSD/NVMe), RAM, cache memory, and the CPU — up through the fetch-decode-execute cycle, Moore's Law, and the architectural difference between serial CPU execution and massively parallel GPU execution. A ten-minute break separates this foundation from the second half, which focuses entirely on HPC: what it is, how it differs from cluster computing, distributed computing, and cloud computing, and the key architectural elements including nodes, the batch system / job scheduler, GPFS (General Parallel File System), and fault-tolerance mechanisms such as RAID and checkpointing.

The session is notably practical. Dr. Suresh shares a personal anecdote about upgrading his own i3 laptop from HDD to NVMe and explains the compatibility constraints that prevented him from also upgrading the CPU or RAM — using this real situation to teach motherboard slot dependencies. He also shares a team experience of training a 50 GB small language model (SLM) on an i5 laptop with a 1 GB graphics card over 45 days at ten hours per day, with hourly checkpoints — a vivid illustration of the cost of not having GPU infrastructure. The session closes with two case studies (weather forecasting and drug discovery) that explain exactly why HPC is needed for certain scientific and simulation workloads, and a frank advisory: most AI project development work does not require HPC at all, and a modern laptop GPU is usually sufficient for model training at project scale.

The cohort is diverse — participants include CTOs, COOs, CFOs, CEOs, and senior managers with 15–40 years of experience across domains — and the discussion is highly interactive, with participants contributing real-world examples from automotive HPC, cloud-based autoscaling, clinical drug discovery, and OCR-heavy document processing.

---

## Key Concepts

- **The storage-RAM-CPU interaction** — All data at rest lives on persistent storage (hard disk / SSD / NVMe). When the CPU needs to execute anything, it issues an instruction to load the relevant file from storage into RAM. The file transitions from a passive *program* on disk to an active *process* in RAM. The CPU fetches data from RAM for computation. If the data is present in cache memory (L1/L2/L3, physically inside or adjacent to the CPU), access is fastest (~1 ms). If not, the CPU checks RAM (~3 ms), then disk (~10 ms). This hierarchy — cache → RAM → storage — governs all computation on a standard desktop or laptop.

- **Cache memory: purpose and limits** — Cache is a small, extremely fast memory buffer inside or adjacent to the CPU. Because it is accessed directly by the processor, it is far faster than RAM or disk. Its size is deliberately kept small (typically 500 MB–1 GB in modern systems) because accommodating more transistors in cache would compromise the computational density available for actual processing. Cache contents are volatile: they are replaced frequently by new data based on usage algorithms, and cleared on restart. The limited size is a deliberate architectural trade-off, not a deficiency.

- **Registers and the fetch-decode-execute cycle** — Inside the CPU, small memory cells called *registers* hold the active state of computation. Key registers include the Program Counter (PC, holds the address of the next instruction), the Instruction Register (IR, holds the current instruction being executed), the Memory Address Register (MAR, holds the address of the data to be read), the Memory Data Register (MDR, holds the actual data), and the Accumulator (ACC, holds intermediate results). Each CPU clock cycle performs a fetch-decode-execute operation: fetch the instruction address from PC into MAR, read the instruction via MDR into IR, decode it in the Control Unit (CU), and execute it in the Arithmetic Logic Unit (ALU). Though serial in structure, the sheer speed of clock cycles (measured in GHz) makes this appear instantaneous.

- **Clock speed, GHz, and Moore's Law** — CPU speed is measured in GHz — the number of clock cycles (and thus potential fetch-decode-execute operations) per second. A 4.5 GHz CPU can perform 4.5 × 10⁹ cycles per second. CPU speed is determined by the number and density of transistors packed onto the chip. Moore's Law (Gordon Moore, Intel co-founder, 1965) predicted transistor count would double roughly every year; he revised this to every 18–24 months in 1975. This held approximately true until around 2015. Since then, progress has slowed because transistor sizes (now ~2 nm, where the "2 nm" refers to the spacing between transistors, not the transistor itself) cannot shrink much further without causing heat dissipation and power leakage problems. The Nvidia H100/H800 GPU contains approximately 80 billion transistors.

- **CPU versus GPU: serial versus parallel architecture** — A CPU has a small number of powerful, complex cores (4 to 64 in modern desktop/server chips) optimized for sequential, branching, complex logic. A GPU has thousands to tens of thousands of simpler cores designed to execute the same instruction on many data items simultaneously — a paradigm called SIMD (Single Instruction, Multiple Data). The CPU has a higher clock speed per core; the GPU has vastly more cores running at lower clock speed. The result: the CPU is the "master chef" orchestrating complex decisions, while the GPU is the army of "line cooks" handling repetitive, parallel workloads such as matrix operations, image block processing, and neural network weight updates. GPU performance is measured in FLOPS (floating-point operations per second) — gigaflops or teraflops — rather than GHz.

- **Cores versus the CPU chip** — A CPU *chip* (processor) contains multiple *cores*, each of which is a miniature independent processing unit with its own Control Unit and ALU but sharing the chip's cache and memory bus. An i5 or i7 processor, for example, has four cores. A GPU chip contains thousands of simpler cores. Increasing core count — rather than clock speed — has become the primary method of increasing computational throughput, both in CPUs (dual-core, quad-core, octa-core) and GPUs. The key principle: more cores enable more parallel task execution.

- **Processes and threads** — A process is a program loaded into RAM and under active execution. A single visible operation (e.g., copying a file from C: to D:) actually spawns multiple threads behind the scenes, each handling a distinct sub-task: opening the source, reading the file, allocating space at the destination, writing the data, verifying available space, handling conflict warnings, and so on. Thread management is orchestrated by the CPU via the operating system kernel and an interrupt controller. The serial nature of CPU execution becomes invisible at human timescales because clock speeds are high enough to cycle through these threads faster than humans can perceive.

- **HPC defined and distinguished from cluster and distributed computing** — Cluster computing groups complete desktop or laptop systems (called nodes) within an organization's network to pool their computational power. Distributed computing does the same but across geographically separated networks. High Performance Computing (HPC) takes a fundamentally different approach: instead of grouping whole machines, it groups only the computational components — CPUs, GPUs, and RAM — on specialized boards. Each *HPC node* is a high-density board containing, for example, 128–256 GB of RAM, dozens of CPU cores, and hundreds of GPU cores. Thousands of such nodes are interconnected via high-speed LAN, Ethernet, or optical fiber. The result is a system that appears to the user as a single machine but has aggregate computational power orders of magnitude greater than any desktop. The key architectural difference: HPC nodes contain no complete operating environments — they expose only raw compute resources.

- **The HPC batch system and job scheduler** — Users do not interact with HPC nodes directly. Instead, they submit jobs to a *batch system* (also called a job scheduler), which maintains a queue of pending jobs, monitors node availability, allocates nodes based on job requirements, and redistributes jobs if a node fails. The batch system is analogous to Hadoop's master node in distributed systems. Common tools include SLURM and LSF. Load balancing and job recovery are managed entirely by the batch system, not by individual users.

- **GPFS and the storage performance gap** — The General Parallel File System (GPFS) is a parallel distributed file system used in HPC environments. Unlike a laptop's sequential storage access (even with NVMe), GPFS issues simultaneous read requests across all nodes, effectively parallelizing storage I/O. Benchmark comparison: reading 1,000 GB of data takes approximately 3 hours on an HDD laptop, 30 minutes on SSD, 5 minutes on NVMe, and under 20 seconds on an HPC with GPFS. The hardware (NVMe) is the same; the performance difference arises entirely from GPFS's ability to fetch simultaneously from thousands of nodes.

- **HPC versus cloud: CapEx vs. OpEx, not apples vs. apples** — On-premise HPC is a capital expenditure (CapEx): large upfront hardware investment for predictable, sustained workloads. Cloud is an operational expenditure (OpEx) with autoscaling for variable or unpredictable demand (e.g., streaming a cricket match where concurrent viewer counts are unknown in advance). Cloud providers also offer HPC-as-a-service, blurring the boundary. The practical guidance: if computational demand is high but predictable and continuous, on-premise HPC may be justified. For development, experimentation, and most AI project work, cloud GPU instances or a laptop GPU are sufficient. Hybrid approaches — on-premise HPC compute combined with cloud storage — can combine the strengths of both.

- **When HPC is (and is not) needed for AI** — Training a model requires intensive computation; inference (querying ChatGPT, running a deployed model) requires very little. For most AI project development — including SLM training on text data — a modern laptop with integrated GPU capability is sufficient, though training may take days or weeks. HPC (or external GPU infrastructure) becomes necessary only when datasets are massive, when training cycles must be short, or when simulation complexity demands it (weather forecasting, drug discovery, molecular dynamics). Data preparation (EDA, cleaning, pre-processing) consumes 70–80% of a data scientist's time and requires minimal computational power.

- **Fault tolerance in HPC** — HPC systems implement multiple fault-tolerance mechanisms: (1) *RAID-style data replication* — the batch system automatically stores four replicas of submitted data on different nodes, so that a single node failure does not cause data loss; (2) *job checkpointing* — long-running training jobs save model state at regular intervals (e.g., every hour) so that a power failure or node crash restarts from the last checkpoint rather than from scratch; (3) *job re-allocation via MPI* — if a node fails mid-job, the batch system's load balancer automatically reassigns the affected tasks to available nodes.

---

## Technologies / Frameworks Discussed

| Technology | Type | Key Point |
|---|---|---|
| HDD (Hard Disk Drive) | Persistent storage | Slowest storage tier; baseline for I/O comparison (~3 hrs to read 1,000 GB) |
| SSD (Solid State Drive) | Persistent storage | ~16× faster than HDD; ~30 minutes to read 1,000 GB |
| NVMe (Non-Volatile Memory Express) | Persistent storage | ~16× faster than SSD; installs in a slot similar to RAM; ~5 minutes to read 1,000 GB |
| GPFS (General Parallel File System) | HPC parallel file system | Simultaneous multi-node reads; sub-20-second read of 1,000 GB on large HPC cluster |
| SIMD (Single Instruction, Multiple Data) | CPU/GPU execution paradigm | Core mechanism behind GPU parallelism; one instruction applied simultaneously across many data items |
| MPI (Message Passing Interface) | HPC communication protocol | Enables inter-node communication and job redistribution on node failure |
| Hadoop (MapReduce) | Distributed computing framework | Used as an analogy for HPC architecture; master node divides jobs, workers execute, results aggregated |
| SLURM / Batch System | HPC job scheduler | Accepts user job submissions, queues and allocates jobs to nodes, handles fault recovery |
| RAID | Storage redundancy | HPC batch systems store ~4 replicas of data across nodes to survive node failures |
| TensorFlow / Keras | ML training libraries | Mentioned as common libraries requiring data in digestible formats; responsible for model training computation |
| Cray | HPC supercomputer vendor | Industry benchmark for weather forecasting workloads; used as an example of application-specific HPC vendors |
| Nvidia H100/H800 | GPU hardware | Contains ~80 billion transistors; benchmark for modern GPU scale |
| DDR RAM | Memory hardware | Slot-based; compatibility constrained by motherboard; example: DDR2 4 GB in two slots |

---

## Important Examples and Case Studies

**Upgrading an i3 laptop from HDD to NVMe** — Dr. Suresh describes his own experience upgrading a five-year-old laptop. He could not replace the CPU (motherboard compatibility: the gigabyte board supported i3 but not i5 without a full motherboard replacement) or add more RAM (only two DDR2 slots, already populated; upgrading would waste the existing modules). Storage was the only upgradeable component without a full platform replacement. He added an NVMe drive alongside the existing HDD, booted the OS from NVMe, and kept data files on the HDD. The result was a significant speed improvement. This scenario is used to teach the real-world constraints of hardware compatibility and the diminishing returns of partial upgrades.

**Training a 50 GB SLM on a commodity laptop** — Dr. Suresh's team trained a small language model on 50 GB of scanned PDF text data (requiring OCR pre-processing) using an i5 14th-generation laptop with 16 GB RAM and a 1 GB graphics card. No HPC or dedicated GPU server was used. Training took 45 days running 10 hours per day, with hourly checkpointing via `model.save()` to protect against power failures. The team found the bottleneck was primarily data processing (OCR conversion) rather than model computation. The example establishes two lessons: (1) HPC is not required for AI development at project scale; (2) data quality and format significantly affect training time, independent of model complexity.

**Weather forecasting with HPC** — The instructor uses national weather prediction as a canonical HPC use case. A weather model partitions a country into geographic grid cells (e.g., 5 km × 5 km). Each cell's meteorological parameters (temperature, humidity, pressure, wind) are assigned to a dedicated HPC node. All nodes process their grid cells in parallel. Because input data changes continuously and predictions must be issued quickly, the high I/O throughput and parallelism of HPC are essential. A conventional cluster or cloud solution would introduce unacceptable latency given the volume and velocity of the input data.

**Drug discovery and protein folding simulation** — A participant with pharmaceutical domain knowledge elaborated on why HPC is indispensable in early-stage drug discovery: millions of candidate drug molecules must be screened for binding affinity against millions of target biomolecules. Laboratory-based physical testing of even a small fraction of these combinations would be prohibitively expensive. Computational simulation replaces laboratory synthesis for initial screening. Simulations model molecular interactions at the atomic/quantum level, requiring both massive data volumes and rapid iteration across millions of parameter configurations — a quintessential HPC workload. Dr. Suresh used the COVID-19 context: finding the molecular site on a protein where a drug molecule binds stably and blocks viral replication requires exactly this kind of simulation at scale.

**Image block processing and GPU core utilization** — To illustrate why GPUs outperform CPUs for image processing, Dr. Suresh presents a worked example: divide an image into 256 blocks. An 8-core CPU assigns 32 blocks per core, processing sequentially within each core. A 256-core GPU assigns one block per core and processes all 256 blocks simultaneously. The total computation is the same; the wall-clock time difference is the ratio of sequential batches required: 32:1. This explains why deep learning tasks involving images, audio, and video benefit dramatically from GPU parallelism.

**Automotive HPC (participant contribution)** — A participant from the automotive industry described a modern use of HPC within vehicles: a single onboard HPC board integrates CPU, GPU, and controller unit components that previously required separate ECUs (Electronic Control Units) for functions such as braking, steering assist, and sensor fusion. A hypervisor partitions the HPC board to run each application in its own isolated environment. This demonstrates that HPC is not only a data center technology but is increasingly embedded in real-time embedded systems.

---

## Related

- [[course-03-overview-emerging-digital-technologies|Course 03 Overview — Emerging Digital Technologies]]
- [[high-performance-computing|High Performance Computing (HPC)]]
- [[gpu-architecture|GPU Architecture and Parallelism]]
- [[cpu-architecture|CPU Architecture and the Fetch-Decode-Execute Cycle]]
- [[moores-law|Moore's Law]]
- [[cluster-computing|Cluster Computing]]
- [[distributed-computing|Distributed Computing]]
- [[cloud-computing|Cloud Computing]]
- [[parallel-computing|Parallel Computing and SIMD]]
- [[hadoop|Hadoop and MapReduce]]
- [[llm-slm-training|LLM and SLM Training Infrastructure]]
- [[mlops|MLOps and Model Checkpointing]]
- [[drug-discovery-ai|AI in Drug Discovery and Protein Folding]]
- [[weather-forecasting-hpc|Weather Forecasting and HPC]]
- [[dr-sumitra-padman|Dr. Sumitra Padman]] — course faculty context
