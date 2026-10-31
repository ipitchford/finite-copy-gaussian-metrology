# Revision response

| Point | Response |
|---|---|
| Measurement class not covered by proof | Definition 1 is now operational: ancillas, Gaussian unitary, homodyne on any subset, classical post-processing. Lemma 2 proves that every such measurement is dominated by complete homodyne detection of an orthonormal Lagrangian frame on the copies plus vacuum ancillas. Lemma 3 extends the disk bound to ancillas through the projection Π. The upper bound therefore covers ancilla-assisted schemes; adaptive schemes are excluded explicitly. |
| Mixed seeds | Remark 1 writes the Williamson split and the convolution with parameter-free noise. |
| Homodyne attainment via a singular seed | Attainment is computed directly from the outcome law of the explicit interferometer and homodynes (proof of Theorem 1), and checked numerically through an explicitly constructed interferometer. |
| Laboratory coordinates | Remark 2 states the commutation of the copy-wise normalisation with the interferometer. |
| Strictness criterion | Proposition 1 uses det[w, Aw] ≠ 0, which is invariant and covers zero tangents. |
| Quantum benchmark | Corollary 1: exact shortfall from m·QFI, nondecreasing, at most c sin²2δ ≤ λ²/2, explicit limit; F_m = mQ iff λab = 0; F_m/m increases to Q. The QFI formula in this convention is checked by a Fock-space computation. |
| Squeezing-cap extension | Theorem 2: exact optimum for pure general-dyne seeds with e^{−R} ≤ M ≤ e^{R} in normal-form coordinates, attained by the same interferometer with seeds of squeezing e^{±R}; limits R = 0 (heterodyne) and R → ∞. The cap is not a laboratory energy budget. |
| Local estimator; meaning of m | Remarks 3 and 4. |
| Related work, abstract, readability | New abstract, plain-language introduction, contribution list, statement of what is not new, related-work paragraph, proof roadmap, plain-words summaries, conclusion. |
| Example | Table 1 gives F_m, mF_1 and the shortfall in exact rationals for α = 1/2, with an idealisation caveat. |
| Numerical checks | New verification/verify_all.py, independent of the proof's parameterisation where possible (Bloch–Messiah seeds, symplectic dilations, explicit interferometers, Fock space). Adds deterministic degenerate cases and negative controls. No reliance on assert; identical results under python -O. |
| Verification-round wording points | All fixed (see REVIEW_SUMMARY.md). |
| Not done | Mixed states, multimode tangents and adaptive strategies remain open (Section 5 of the manuscript). |
