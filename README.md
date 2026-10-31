# One bright mode is enough: exact finite-copy Gaussian Fisher information for pure single-mode models

**Unrefereed research candidate**, version 1.0.0-candidate (31 October 2026). DOI [10.5281/zenodo.23837733](https://doi.org/10.5281/zenodo.23837733). Release page: https://evidencepress.org/releases/finite-copy-gaussian-metrology/

## What this is about, in plain words

A small change θ in a light beam can be read off by measuring the beam's field quadratures with homodyne detection. If the same state is prepared m times, it can pay to measure the copies jointly. Navarro, Morelli, Sanz and Mehboudi (arXiv:2512.20534) showed that, with only Gaussian measurements (linear optics, Gaussian auxiliary light, homodyne detection), joint measurement can beat measuring the copies one by one. Their scheme concentrates the changing mean into one "bright" output mode. They left open which Gaussian measurement is best for a finite number of copies.

This package answers that question for every smooth family of **pure single-mode** Gaussian states and every m. The best Fisher information over all fixed Gaussian measurements on m copies, including ancilla-assisted schemes, is

F_m = (m−1)λ²/2 + max_φ [ 2m(a cos φ + b sin φ)² + (λ²/2) cos² 2φ ],

where (a, b) is the rate of change of the mean and λ the rate of change of the squeezing, in normalised coordinates. It is attained by the concentration interferometer and homodyne detection of every output. Consequences: the exact optimum under a cap on measurement-seed squeezing; the exact shortfall from the quantum Fisher information, which is at most λ²/2 in total for every m; and a necessary and sufficient condition for joint measurement to help.

## Contents

| Path | What it is |
|---|---|
| [manuscript/finite_copy_gaussian.pdf](manuscript/finite_copy_gaussian.pdf) | The 9-page manuscript (proofs, example, scope) |
| [manuscript/finite_copy_gaussian.tex](manuscript/finite_copy_gaussian.tex) | Self-contained LaTeX source |
| [verification/verify_all.py](verification/verify_all.py) | Numerical and exact checks with negative controls; exits 1 on failure; no reliance on `assert` |
| [verification/results.json](verification/results.json) | Retained output of the checks |
| [CLAIMS.json](CLAIMS.json) | Machine-readable claims and their evidence |
| [STATUS.md](STATUS.md), [ASSURANCE.md](ASSURANCE.md) | Status and assurance boundary |
| [REVIEW_SUMMARY.md](REVIEW_SUMMARY.md), [REVISION_RESPONSE.md](REVISION_RESPONSE.md) | Rating-free summary of the internal review and the response |
| [PRIOR_ART.md](PRIOR_ART.md), [RESEARCH_GATES.json](RESEARCH_GATES.json), [SOURCES.md](SOURCES.md), [CITATION_AUDIT.md](CITATION_AUDIT.md) | Prior-art search, sources and reference checks |
| [development/](development/) | The original 28 October 2026 research note (superseded by the manuscript) |
| [AI_INDEX.md](AI_INDEX.md) | Navigation for agents |

## Replay

```sh
uv sync --frozen
OPENBLAS_NUM_THREADS=1 uv run --frozen python -B verification/verify_all.py
OPENBLAS_NUM_THREADS=1 uv run --frozen python -O -B verification/verify_all.py
```

Each run takes about two minutes on one core and prints PASS/FAIL per check. See [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md).

## Licence

Text, manuscript and data: CC0-1.0. Code: MIT. See [LICENSES.md](LICENSES.md). Creator: Anonymous. AI-assisted; internal review only.
