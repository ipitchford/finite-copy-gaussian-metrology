# Assurance boundary

## What was done

1. **Written proofs** of every stated result in [manuscript/finite_copy_gaussian.tex](manuscript/finite_copy_gaussian.tex).
2. **Internal AI-assisted review.** Round 1: an outside-model adversarial correctness review and five reviewer reports (editor, methodology, domain, perspective, devil's advocate), plus a clean replay of the original numerical script from a fresh extraction of the research bundle. One revision round, including two extensions (Theorem 2, Corollary 1) and a strengthened measurement-class reduction (Lemma 2). Verification: a re-review of all changes and a targeted proof audit of every new or rewritten proof; their wording findings were fixed. A rating-free summary is in [REVIEW_SUMMARY.md](REVIEW_SUMMARY.md).
3. **Numerical checks** ([verification/verify_all.py](verification/verify_all.py)): 4,800 random pure measurement seeds; 3,000 random ancilla-assisted homodyne measurements with Fisher information computed from the outcome law; local maximisation over seeds; attainment through an explicitly constructed interferometer; the squeezing-capped optimum (bound, attainment, purity and spectrum of the constructed seed, limits); the quantum Fisher information in this convention by Fock-space finite differences; the exact rational example table; deterministic degenerate cases and the strictness criterion; the shortfall corollary; and four semantic negative controls (wrong formulas that must be rejected).
4. **Replay.** Normal and `python -O` runs from a fresh extraction of the frozen archive ([REPLAY_RECEIPT.md](REPLAY_RECEIPT.md)); CI replays both on Linux.
5. **Citations.** Every DOI resolves and matches its Crossref record; arXiv entries match arXiv records ([CITATION_AUDIT.md](CITATION_AUDIT.md)).

## What was not done

- No human specialist or journal peer review, no independent reproduction by an unaffiliated party, no proof-assistant formalisation.
- **Priority is bounded** ([PRIOR_ART.md](PRIOR_ART.md)). The concentration interferometer and the large-displacement value in the coherent-squeezing example are due to Navarro et al. (arXiv:2512.20534). The contribution claimed is the finite-copy upper bound and its consequences.
- The measurement class is fixed (non-adaptive) Gaussian measurements; adaptive schemes are not covered.
- Agreement between AI reviewers is not independent evidence. Numerical checks test normalisations and implementations; they do not replace the proofs.
