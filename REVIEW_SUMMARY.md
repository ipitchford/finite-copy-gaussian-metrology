# Review summary (rating-free)

All review was internal and AI-assisted (31 October 2026). Routes: one outside-model adversarial correctness review (OpenAI model via the publisher's API script); five reviewer reports (editor, methodology, domain, perspective, devil's advocate) and the verification re-review and proof audit (OpenAI Codex agent, run locally with read-only access); a clean replay by the editor. Private editorial assessments are not reproduced here.

## Round 1 findings

- **Correctness.** No reviewer found a counterexample or a substantive error in the main formula, the coherent-squeezing transition or the strictness criterion. Every reviewer recommended minor revision. Every reviewer judged the note substantial enough to stand alone as a short theorem release.
- **Measurement class (adversarial review, all reviewers).** The original note optimised over "covariance-seed" measurements and appealed to a standard normal form without proof. The adversarial reviewer called this the principal gap for the claim "all Gaussian measurements".
- **Homodyne attainment.** The optimiser is a boundary point (a projection), not a finite seed; reviewers asked for the direct outcome-law calculation.
- **Interpretation of the strictness criterion.** "The mean tangent is not an eigenvector of the covariance tangent" is wrong when the covariance tangent vanishes; the determinant form is correct.
- **Missing benchmarks and extensions.** The note did not compare with the quantum Fisher information, and reviewers proposed an exact optimum under a squeezing cap as the most tractable extension.
- **Positioning and readability.** Recent neighbours (Liu, Wang and Ma 2026; Girardi et al. 2026) were missing; no abstract, roadmap or physical explanation; "published question" should be "question left open in a preprint".
- **Numerical checks.** Mostly shared the proof's own parameterisation; degenerate cases were not tested deterministically.

## Verification round findings

The re-review found every fix in place and no open correctness issue in Theorem 1, the ancilla disk bound, Theorem 2's formula, Corollary 1, Proposition 1 or the table. The proof audit marked every new proof valid, apart from these points, all now fixed:
- a dimensionally undefined product in the attainment proof;
- the boundary choice of maximiser in Theorem 2 (with a = b = 0 an interior maximiser exists);
- an unqualified eigenvector paraphrase;
- a plain-words sentence that ignored the zero-loss case;
- the abstract's description of the squeezing cap and the measurement class (adaptive schemes excluded).

## Dispositions

See [REVISION_RESPONSE.md](REVISION_RESPONSE.md).
