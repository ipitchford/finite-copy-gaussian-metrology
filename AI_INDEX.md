# Agent navigation

## Identity

- Release slug: `finite-copy-gaussian-metrology`. Version `1.0.0-candidate`, tag `v1.0.0-candidate`. DOI 10.5281/zenodo.23837733; concept DOI 10.5281/zenodo.23837732.
- Repository: https://github.com/ipitchford/finite-copy-gaussian-metrology. Release page: https://evidencepress.org/releases/finite-copy-gaussian-metrology/
- Scholarly creator: Anonymous. Status: unrefereed candidate ([STATUS.md](STATUS.md)).
- Manuscript: [PDF](manuscript/finite_copy_gaussian.pdf) (9 pages) and its self-contained [LaTeX source](manuscript/finite_copy_gaussian.tex).
- Machine-readable claims: [CLAIMS.json](CLAIMS.json). Human overview: [README.md](README.md).
- Assurance limits: [ASSURANCE.md](ASSURANCE.md). Review record: [REVIEW_SUMMARY.md](REVIEW_SUMMARY.md), [REVISION_RESPONSE.md](REVISION_RESPONSE.md).
- Prior art and sources: [PRIOR_ART.md](PRIOR_ART.md), [RESEARCH_GATES.json](RESEARCH_GATES.json), [SOURCES.md](SOURCES.md), [CITATION_AUDIT.md](CITATION_AUDIT.md). Provenance: [PROVENANCE.md](PROVENANCE.md).
- Citation: [CITATION.cff](CITATION.cff), [.zenodo.json](.zenodo.json). Licences: [LICENSES.md](LICENSES.md).

## Scientific map

Object: a pure single-mode Gaussian family rho_theta in normal form sigma=I, sigma'=lambda diag(1,-1), d'=(a,b); m identical copies; Fisher information of fixed Gaussian measurements (Definition 1). Question: the exact finite-copy optimum F_m^G, left open by Navarro et al. (arXiv:2512.20534).

- Lemma 1: normal form. Lemma 2: every fixed Gaussian measurement (with ancillas) is dominated by complete homodyne detection of an orthonormal Lagrangian frame; Fisher information F(K), K=UU^T. Remark 1: mixed seeds.
- Lemma 3: disk bound for symmetric B with B Omega = -Omega B, B^2 <= I, including the ancilla projection.
- Theorem 1: exact optimum (closed form, one angle); attained by concentration + homodyne.
- Theorem 2: exact optimum under a pure-seed squeezing cap e^{-R} <= M <= e^{R}.
- Corollary 1: exact shortfall from m QFI; bounds and limit. Proposition 1: strict collective advantage iff det[w,Aw] != 0.
- Section 4.5 and Table 1: coherent-squeezing example in exact rationals. Section 5: scope and limits.

## Evidence and replay

- Checks: [verification/verify_all.py](verification/verify_all.py) -> [verification/results.json](verification/results.json): random seeds, ancilla-assisted homodyne, local maximisation, explicit attainment, squeezing cap, QFI by Fock space, exact table, degenerate cases, shortfall corollary, negative controls. Exits 1 on failure; no reliance on assert.
- Environment: [pyproject.toml](pyproject.toml), [uv.lock](uv.lock), [ENVIRONMENT.txt](ENVIRONMENT.txt). CI: [.github/workflows/replay.yml](.github/workflows/replay.yml). Records: [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md). Integrity: [SHA256SUMS](SHA256SUMS).
- Development record (superseded): [development/original_note_2026-10-28.md](development/original_note_2026-10-28.md).

## Trust boundary

All review was internal and AI-assisted. There was no peer review, no independent reproduction and no formal verification. Numerical checks test normalisations and implementations; the theorems rest on the written proofs. Priority holds only within a bounded search; the attaining interferometer is due to Navarro et al.
