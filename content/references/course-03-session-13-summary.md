---
title: "Emerging Digital Technologies — Session 13: Blockchain and Decentralized Ledger Technology"
category: references
tags: ["#src/course", "#dba/coursework", "#emerging-digital-technologies"]
sources:
  - "_raw/dba-course/Course_03_Emerging_Digital_Technologies/02_Recordings_and_PPTs/Session_13/transcript.txt"
created: 2026-04-13
updated: 2026-04-13
summary: "Guest lecturer Prof. Proful (Atria University) traces blockchain from its 2008 origins as a trustless peer-to-peer money system through cryptographic internals, smart contracts, failed enterprise pilots, and the current frontier of institutional asset tokenization."
---

# Emerging Digital Technologies — Session 13: Blockchain and Decentralized Ledger Technology

**Instructor**: Prof. Proful (Centre of Excellence in AI and Decentralized Technologies, Atria University, Bangalore)
**Course**: [[emerging-digital-technologies|Emerging Digital Technologies]] (Course 03)
**Date**: Session recorded and downloaded 2026-04-12; session duration approximately 2 hours 55 minutes

---

Session 13 is a guest lecture dedicated entirely to blockchain — also referred to as decentralized ledger technology (DLT) — delivered by Prof. Proful, who leads the Centre of Excellence in Artificial Intelligence and Decentralized Technologies at Atria University in Bangalore. The session is structured in five broad movements: the historical and financial context that gave birth to Bitcoin, a conceptual and technical deep-dive into how blockchain works, the emergence of smart contracts (Blockchain 2.0), a candid post-mortem of enterprise blockchain pilots that largely failed between 2015 and 2024, and a forward-looking treatment of asset tokenization, which is where institutional adoption is currently concentrated.

The session opens with an extended discussion of what money actually is — a necessary foundation that surprises many participants. Prof. Proful argues that the equivalence between money and physical cash is a widespread misconception: the vast majority of money in the modern world is nothing more than a ledger entry in a bank's database. Once students internalize that money is information, the leap to understanding blockchain becomes intuitive: if money is a ledger entry, then creating a new form of money means creating a new form of ledger — one not controlled by any single institution. This reframing anchors the entire session, and Proful returns to it repeatedly as the discussion moves from Bitcoin to enterprise applications to tokenization.

The latter half of the session is deliberately tilted toward applications, responding to participant feedback that many in the cohort come from non-technical backgrounds. Proful covers Walmart's Food Trust supply-chain traceability initiative, the Maersk/IBM TradeLens container-tracking platform, the Marco Polo supply-chain finance consortium, and the current wave of asset tokenization being pursued by JP Morgan, Goldman Sachs, the Bank for International Settlements, and the Monetary Authority of Singapore. A recurring and candid theme is that blockchain's biggest obstacle has never been technical: it has been the near-impossibility of getting competing commercial entities to agree on a shared platform, and the absence of clear government regulation around tokenized assets.

---

## Key Concepts

- **Money as a ledger entry** — Physical cash is the smallest slice of total money supply; most money exists only as a number in a bank's database. When a bank processes a payment it simply reduces the sender's balance and increases the recipient's. This insight is the foundation of the entire lecture: creating a new form of money is equivalent to creating a new form of ledger. Prof. Proful illustrates this with the RBI promissory note on a 100-rupee note, and a chart of global money supply from 1970 to 2008 in which physical currency is the smallest component.

- **The 2008 financial crisis as the birth context of Bitcoin** — Bitcoin's whitepaper and code were both released in 2008, immediately after the collapse of Lehman Brothers and the subsequent global financial crisis. At a moment of historically low trust in financial institutions, the paper's central question was: can we send money from one party to another without any bank acting as intermediary? The answer required inventing a new kind of ledger. This historical grounding explains both why the technology was created and why it carries an ideological charge that persists today.

- **Decentralization as the core innovation** — Any ledger that assigns ownership to a single custodian recreates the problem it was meant to solve. Bitcoin's answer was to distribute the ledger across thousands of independent computational nodes simultaneously, with no node holding exclusive authority. Consensus — a majority vote among nodes — determines which version of the ledger is canonical. This is why the technology is called decentralized ledger technology: control is fragmented across the network rather than held by a single entity.

- **Hash functions — the cryptographic backbone** — A hash function takes an input of arbitrary size (a sentence, a document, an entire book) and produces a fixed-length output (for example, a 512-byte string). The output changes completely and unpredictably even when the input changes by a single character — the "avalanche effect." It is computationally trivial to compute a hash from a message, but computationally infeasible to reconstruct the message from its hash. In blockchain, hash functions underpin digital signatures (making transactions non-repudiable), tamper detection (any modification of a recorded transaction changes its hash), and proof of work.

- **Proof of Work and cryptocurrency mining** — To add a block of transactions to the blockchain and, in the process, earn the right to create new cryptocurrency, a node must solve a specific computational puzzle: find a number X such that the hash of (data, X) is less than a given threshold. There is no shortcut; nodes must try values of X by brute force, spending electricity and computational power. Once a node finds a valid X, it broadcasts the solution to all other nodes, who can verify the answer almost instantly. This asymmetry — hard to solve, easy to verify — is what makes the system economically honest. Mining is the collective name for this continuous competition.

- **The blockchain data structure** — Blockchain is a chain of blocks where each block contains multiple transactions, the proof of work for those transactions, and the hash of the immediately preceding block. Including the previous block's hash is the mechanism that enforces immutability: to alter any transaction in an earlier block, an attacker would need to recompute the proof of work for that block and every subsequent block, which requires more computational power than 51% of the entire network. The longer the chain grows, the more secure every historical entry becomes.

- **Wallets, public keys, and privacy** — Every participant in a blockchain network is identified by two numbers: a public key (analogous to an account number, shareable with anyone) and a private key (analogous to a password, kept secret). The ledger records balances and transactions against public keys only; there is no mapping from public key to real-world identity within the blockchain itself. This pseudonymity provides privacy but also enables illicit use. A company or device can hold a wallet as easily as an individual — the blockchain has no concept of legal personhood.

- **Smart contracts — Blockchain 2.0** — Introduced by Vitalik Buterin and Gavin Wood in the Ethereum whitepaper (2015), smart contracts generalize the blockchain ledger from storing simple transactions to storing conditional transactions: "I will pay B one bitcoin if condition C is met." Conditions are written in a programming language (Ethereum uses Solidity). An external data feed (called an oracle) supplies the real-world information needed to evaluate whether the condition has been met. Once the condition is satisfied, the payment executes automatically, without lawyers, banks, or any intermediary. Proful describes this as code is law: once deployed, the contract executes exactly as written, bugs and all.

- **Enterprise blockchain pilots and why they failed (2015–2024)** — The decade following the Ethereum whitepaper saw a wave of enterprise pilots attempting to apply blockchain to inter-organisational coordination: Walmart's Food Trust (food provenance), Maersk/IBM's TradeLens (container shipping documentation), Marco Polo/R3 (supply chain finance), and various HSBC initiatives. Virtually all either shut down or failed to reach commercial scale. Prof. Proful identifies a consistent pattern: the technology worked, but the ecosystem-building did not. A blockchain platform for global shipping is worthless if a single major port authority refuses to join; a supply-chain-finance ledger is worthless if suppliers and buyers cannot be persuaded to use the same system. The lesson is that blockchain value is network-dependent, and competitive industries have powerful incentives to resist the data transparency that blockchain demands.

- **Asset tokenization — the current frontier** — Tokenization is the creation of a digital representation of ownership of any real-world asset on a blockchain ledger. It extends to any asset class — land, equity, commodities, art, whiskey casks, US Treasury bonds — the same logic that governments already apply to real property through title deeds and land registries. The token is the digital analogue of a sale deed: holding it proves ownership of the underlying asset. Today, JP Morgan, Goldman Sachs, Fidelity, the Bank for International Settlements, and the Monetary Authority of Singapore are all actively involved. The key irony, which Proful highlights explicitly, is that a technology invented to disintermediate banks is now being adopted by banks to increase their own operational efficiency and global reach.

- **Benefits and barriers of tokenization** — Tokenization enables fractional ownership (a million-dollar Picasso can be divided into one million tokens, each costing $1), global peer-to-peer trading, and dramatically lower transaction costs (smart contracts replace lawyers and bankers, reducing transaction fees from 2-5% to under 0.5%). The principal barrier is regulatory: most governments have not formally recognised token ownership as legally equivalent to registered title, creating tax, compliance, and enforceability gaps. Technical complexity — particularly the risk of bugs in smart contract code that cannot be corrected retroactively — is a secondary concern.

- **When not to use blockchain** — Proful offers a crisp heuristic: inside a single organisation, a conventional database is almost always superior to a blockchain. Blockchain's value proposition is specifically for multi-party coordination where independent, competing entities need to read from and write to a shared trusted ledger without relying on any single party to administer it. The moment all participants are under the same organisational umbrella, the decentralization rationale disappears.

---

## Technologies / Frameworks Discussed

| Technology / Concept | Type | Key Point |
|---|---|---|
| Bitcoin | Cryptocurrency + blockchain protocol | First implementation of a decentralized public ledger; uses proof-of-work consensus; born 2008 |
| SHA-1 / cryptographic hash functions | Cryptographic primitive | Arbitrary-size input → fixed-length output; avalanche effect; computationally irreversible |
| Proof of Work | Consensus mechanism | Requires solving a computationally expensive puzzle to validate a block; secures the ledger against tampering |
| Proof of Stake | Consensus mechanism (Ethereum) | Alternative to proof of work; mentioned but not covered in depth; used by Ethereum |
| Ethereum / Blockchain 2.0 | Smart contract platform | Generalizes Bitcoin's ledger to store conditional transactions (smart contracts); programming language: Solidity |
| Solidity | Smart contract programming language | Used on Ethereum to encode the conditions of smart contracts |
| Oracles | Blockchain middleware | External data feeds that supply real-world information to smart contracts so conditions can be evaluated |
| Multi-signature wallets | Wallet security mechanism | Splits a private key into N shares; any M-of-N combination can authorise a transaction; mitigates key-loss risk |
| Swift | Interbank messaging protocol | Current standard for cross-bank transfers within a country; mentioned as contrast to blockchain-based settlement |
| IBM Food Trust | Enterprise blockchain application | Walmart-led supply-chain provenance tracking; technically successful but commercially unviable |
| TradeLens | Enterprise blockchain application | Maersk/IBM container shipping documentation platform; shut down due to ecosystem adoption failure |
| Marco Polo / R3 Corda | Enterprise blockchain application | Supply-chain finance consortium backed by Microsoft, Mastercard; also failed to achieve adoption |
| Asset tokenization | Financial application of blockchain | Creating digital ownership tokens for real-world assets (property, art, gold, equities); currently led by major financial institutions |
| Digital Rupee | Central bank digital currency (India) | RBI initiative to issue a state-backed digital currency; mentioned as evidence of government engagement with the space |

---

## Important Examples and Case Studies

**The 2008 Lehman Brothers collapse and the Bitcoin whitepaper** — Proful opens the session with the photograph of Lehman Brothers' sign being dismantled and connects it directly to the date of Bitcoin's publication. The crisis produced historically low trust in financial institutions; the whitepaper asked whether a money system could exist without them. This is not merely historical colour: it explains the ideological DNA of blockchain, the reason it is decentralized rather than merely digital, and why the technology carries a political edge that complicates enterprise adoption.

**The 100-rupee note thought experiment** — Proful asks students: if you take a 100-rupee note to the RBI Governor (whose signature appears on the note promising to pay the bearer), what will he give you? The answer — another 100-rupee note — makes vivid the point that fiat money is circular: it is backed not by gold or any commodity but by collective social agreement and legal-tender laws. The promissory note has value because the government legally compels everyone in the country to accept it. This exercise motivates the question: what would it take to build a money system with different backing?

**Zimbabwe and Venezuela as inflation case studies** — In response to a student question about why central banks do not simply print unlimited money, Proful cites Zimbabwe and Venezuela as examples of countries that did exactly that, producing hyperinflation that destroyed the real value of savings overnight. This grounds the theoretical discussion of fiat money in lived economic consequences.

**Walmart Food Trust — provenance tracing** — Walmart's supply chain for a single food SKU may span hundreds of companies across multiple continents (farms, aggregators, shippers, packaging facilities, distribution centres). When a disease outbreak requires a product recall, identifying which specific shelf items originated from the affected farms used to take more than a week. Food Trust — a blockchain ledger jointly maintained by all supply-chain participants — reduced this to seconds. Proful notes that the use case is technically valid but was not commercially adopted because the return on investment could not be justified across the fragmented industry.

**Maersk/IBM TradeLens — container tracking** — International container shipping involves customs authorities, port operators, ocean carriers, inland logistics providers, and freight forwarders across at least two countries. Paperwork completion often takes longer than the physical voyage itself, causing costly delays. TradeLens proposed a shared blockchain ledger on which all parties could update a container's status in real time. The platform was shut down because Maersk and IBM could not persuade competing shipping lines and independent port authorities to participate on a system seen as controlled by a competitor. Proful frames this as the canonical lesson of enterprise blockchain: the technology problem was solved; the governance problem was not.

**Marco Polo — supply-chain finance** — Suppliers who ship goods on 60-to-90-day payment terms face cash-flow pressure. Marco Polo proposed that if a supplier could record a digitally signed, blockchain-verified invoice, a bank could lend against that invoice immediately (supply-chain financing) with high confidence in the collateral. The initiative involved Microsoft, Mastercard, and the R3 Corda blockchain. Like TradeLens, it failed because suppliers and their buyers had to be on the same blockchain platform — and achieving that bilateral enrollment at commercial scale proved impossible.

**Aspen Resort tokenization** — A Colorado resort was divided into one million tokens. Holding one token means owning one-millionth of the resort. An investor who cannot afford to buy a luxury resort outright can purchase a fractional share and benefit from any appreciation in value. Proful uses this example to explain fractional ownership as the primary value proposition of tokenization — it democratizes access to asset classes previously available only to the wealthy.

**Whisky cask tokenization** — A distillery tokenized its aging casks. Each cask's token represents a share of that physical cask; because whisky increases in value as it matures, the token appreciates over time. When the cask is eventually sold, token holders redeem their tokens for a proportional cash payment. This example illustrates how tokenization can unlock value in illiquid, non-standard assets with long holding periods.

**The "code is law" limitation — bugs in smart contracts** — A student (Denise) raised the issue of misinterpretation or bugs in smart contract code. Proful confirms that once a smart contract is deployed on the blockchain, it executes exactly as written, even if the code does not reflect the parties' intentions. The only remedy is a subsequent transaction to partially reverse the effects, which both parties must consent to; the original erroneous transaction cannot be deleted. This is a meaningful constraint on smart contract adoption for complex, real-world legal agreements.

---

## Related

- [[course-03-overview-emerging-digital-technologies|Course 03 Overview — Emerging Digital Technologies]]
- [[blockchain|Blockchain / Decentralized Ledger Technology]]
- [[bitcoin|Bitcoin]] — first cryptocurrency and first blockchain
- [[ethereum|Ethereum]] — introduced smart contracts (Blockchain 2.0)
- [[smart-contracts|Smart Contracts]] — conditional transactions encoded in Solidity
- [[cryptography|Cryptography]] — hash functions, digital signatures, public/private keys
- [[asset-tokenization|Asset Tokenization]] — virtual representation of real-world assets on a blockchain
- [[supply-chain-management|Supply Chain Management]] — Walmart Food Trust, TradeLens use cases
- [[supply-chain-finance|Supply Chain Finance]] — Marco Polo / R3 Corda use case
- [[nft|Non-Fungible Tokens (NFTs)]] — mentioned briefly; a specific category of tokenized assets
- [[fiat-currency|Fiat Currency]] — money as ledger entry; contrast with cryptocurrency
- [[central-bank-digital-currency|Central Bank Digital Currency]] — digital rupee (India); government-issued digital money
- [[cyber-security|Cyber Security]] — mentioned as adjacent topic; blockchain wallets are a known attack surface
- [[dr-sumitra-padman|Dr. Sumitra Padman]] — course instructor (Course 03); this session was a guest lecture
