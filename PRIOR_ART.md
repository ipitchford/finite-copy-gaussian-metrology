# Prior art (bounded search)

Searches were run on 28 October 2026 (original bundle) and again on 31 October 2026 (publication intake and review), for the claim itself, not only the bibliography. Corpora: arXiv records and full HTML, Crossref, Semantic Scholar, general web search (standard and extended), GitHub code search (including repositories of AI-assisted research drafts), and the Evidence Press release feed. Five AI-assisted reviewers also searched independently. No prior statement of the finite-copy optimum was found. This is a bounded search, not proof of priority.

| Work | What it does | Relation to this package |
|---|---|---|
| Navarro, Morelli, Sanz, Mehboudi, arXiv:2512.20534 (v1, 23 Dec 2025) | Additivity of optimal Gaussian Fisher information when θ is in the mean only or the covariance only (single-mode copies; isothermal multimode extension); concentration interferometer giving superadditivity when both move; asymptotic optimality; coherent-squeezing example | Source of the question (finite-copy optimality explicitly left open in its Discussion), of the attaining architecture, and of the large-displacement value. This package proves the finite-copy upper bound. |
| Cenni, Lami, Acín, Mehboudi, Quantum 6, 743 (2022) | Gaussian-measurement thermometry; general-dyne Fisher information; pure-seed sufficiency; an additivity conjecture for thermal product states | Fisher-information formula and pure-seed reduction (Remark 1). Different question. |
| Oh et al., npj Quantum Inf. 5, 10 (2019) | Optimal single-copy Gaussian measurements for phase estimation | Single-copy prior art; the m = 1 case of the optimisation is related. |
| Liu, Wang, Ma, arXiv:2610.02625 (2 Oct 2026) | Superadditivity of Gaussian Fisher information for two different thermal modes, covariance-only (width-encoded) | Complementary mechanism; no displacement, no m-copy formula. |
| Girardi, Rizzo, Turner, Adesso, Lami, arXiv:2609.40307 (30 Sep 2026) | Gaussian quantum Stein lemma; asymptotic first/second-moment decoupling | Hypothesis testing, asymptotic; does not give a finite-copy Fisher-information optimum. |
| Monras, arXiv:1303.3682 (2013) | Quantum Fisher information of Gaussian states | Pure-state QFI formula used in Corollary 1 (also checked numerically). |
| the-omega-institute/trureturing problem file on Cenni et al. Eq. (47) (Oct 2026) | Counterexample to covariance-only thermometry additivity for unequal frequencies | Different question (mixed, covariance-only). |

Method: the Cayley-type map from measurement covariances to symmetric contractions anticommuting with the symplectic form is a standard symplectic tool; no claim is made for it. The new step is the disk compression with the ancilla projection and its rank-one sharpness.
