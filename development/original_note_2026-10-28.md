# Exact finite-copy Gaussian metrology for pure one-mode models

Research note, 28 October 2026. This is a candidate new theorem with a complete
elementary proof. Its historical priority is subject to the bounded search in
`novelty_report.md`. It solves the pure one-mode subcase of a published finite-copy
optimisation question; it does not solve that question for mixed or arbitrary
multimode states.

## 1. Question and contribution

Navarro, Morelli, Sanz and Mehboudi [1] construct a collective Gaussian measurement
that concentrates the displacement of identical copies into one output mode.
They prove asymptotic optimality, exhibit superadditivity, and explicitly leave
finite-copy optimality open in their Discussion. Their coherent-state squeezing
example attains `4m alpha^2+2(m-1)` when `alpha^2>=2`. The concentration construction
and that achieved value belong to [1].

The theorem below proves global optimality at every copy number for every smooth
one-parameter **pure one-mode Gaussian model**. It also determines the remaining
homodyne angle by a one-variable concave optimisation. The symmetric squeezing
example has a closed piecewise-polynomial answer at every displacement strength.

## 2. Definitions and local normal form

Use quadratures with `[q,p]=i`, displacement `d=<R>`, and covariance

\[
\sigma_{ij}=\langle\{R_i-d_i,R_j-d_j\}\rangle.
\]

The vacuum covariance is `I_2`. Fix an operating point `theta_0` in an open
parameter interval. Let `rho_theta` be a differentiable family of pure one-mode
Gaussian states, with differentiable finite first and second moments. All
derivatives below are evaluated at `theta_0`.

A fixed, parameter-independent symplectic transformation makes `sigma=I_2`.
Purity gives `det sigma_theta=1`, hence `Tr sigma'=0` in these coordinates.
A fixed phase rotation then yields

\[
\sigma=I_2,\qquad
\sigma'=\lambda\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
d'=\begin{pmatrix}a\\b\end{pmatrix},\qquad \lambda\ge0.
\tag{1}
\]

Write `F_m^G` for the supremum of local classical Fisher information over all
collective Gaussian POVMs on `rho_theta^{otimes m}`, including ideal homodyne
limits. The measurement is held fixed when differentiating the distribution.
"Gaussian POVM" here has its standard covariance-seed meaning [1,2]: Gaussian
ancillas, fixed Gaussian transformations and quadrature detection, including
classical Gaussian noise and coarse graining. Outcome-dependent nonlinear
adaptation that produces a non-Gaussian POVM is outside this class.

A nondegenerate Gaussian POVM is represented by a physical covariance `M`.
The standard Fisher information formula in this convention is [1,2]

\[
F(M)=2v^T(\Sigma+M)^{-1}v+
\frac12\operatorname{Tr}\!\left[((\Sigma+M)^{-1}H)^2\right],
\tag{2}
\]

where `Sigma=sigma^{oplus m}`, `v=(d')^{oplus m}`, and
`H=(sigma')^{oplus m}`. Mixed measurement seeds are pure seeds followed by
parameter-independent Gaussian noise: Williamson decomposition gives
`M=M_0+N`, with `M_0` pure and `N>=0`. Classical data processing therefore
reduces the supremum to pure `M_0`, followed by closure to include homodyne.

## 3. Theorem

**Theorem 1.** Under the preceding hypotheses, for every integer `m>=1`,

\[
\boxed{
F_m^G=(m-1)\frac{\lambda^2}{2}
+\max_{\phi\in\mathbb R}
\left\{2m(a\cos\phi+b\sin\phi)^2
+\frac{\lambda^2}{2}\cos^2(2\phi)\right\}.}
\tag{3}
\]

An optimum is attained by a real passive interferometer which concentrates the
repeated displacement tangent into one output, followed by homodyne detection
on every output. Measure a covariance-optimal quadrature on the `m-1` other
outputs and the angle maximising (3) on the concentrated output.

The formula refers to the coordinates in (1). In the original coordinates each
homodyne is simply the corresponding linear quadrature. The fixed whitening
transformation is a change of coordinates; it need not be an extra active optical
element, since its effect on a single homodyne can be absorbed into the
quadrature angle and an irrelevant outcome scaling.

### Proof: reduce the covariance optimisation to a disk

Order the coordinates as all `q` coordinates followed by all `p` coordinates, and
set

\[
\Omega=\begin{pmatrix}0&I_m\\-I_m&0\end{pmatrix},\quad
J=\begin{pmatrix}I_m&0\\0&-I_m\end{pmatrix},\quad
v=\begin{pmatrix}a\mathbf1\\b\mathbf1\end{pmatrix},\quad H=\lambda J.
\]

For a pure seed `M`, define

\[
K=(I_{2m}+M)^{-1},\qquad B=2K-I_{2m}.
\tag{4}
\]

Purity means `M Omega M=Omega`, so
`Omega M Omega^T=M^{-1}`. Consequently

\[
\Omega K\Omega^T=(I+M^{-1})^{-1}=I-K,
\]

and `B Omega+Omega B=0`. Since `M>0`, `B` is real symmetric with spectrum in
`(-1,1)`. Therefore

\[
B=\begin{pmatrix}X&Y\\Y&-X\end{pmatrix},
\qquad X=X^T,\quad Y=Y^T,\quad B^2\le I_{2m}.
\tag{5}
\]

The upper-left block of `B^2<=I` gives

\[
X^2+Y^2\le I_m,\qquad
\operatorname{Tr}(X^2+Y^2)\le m.
\tag{6}
\]

Expand (2) using `K=(I+B)/2`. The mean part is

\[
2v^TKv=m(a^2+b^2)+(a^2-b^2)\mathbf1^TX\mathbf1
+2ab\mathbf1^TY\mathbf1.
\]

Since `Tr B=0` and
`Tr[(BJ)^2]=2Tr(X^2-Y^2)`, the covariance part is

\[
\frac12\operatorname{Tr}[(KH)^2]
=\frac{\lambda^2m}{4}
+\frac{\lambda^2}{4}\operatorname{Tr}(X^2-Y^2).
\]

Let `e=mathbf1/sqrt(m)`, a unit vector, and write

\[
x=e^TXe,\qquad y=e^TYe,\qquad c=\lambda^2/2.
\]

The elementary bounds

\[
x^2+y^2\le\|Xe\|^2+\|Ye\|^2\le1,
\qquad
\operatorname{Tr}Y^2\ge\|Ye\|^2\ge y^2
\tag{7}
\]

and (6) imply

\[
F(M)\le m(a^2+b^2)+mc
+m(a^2-b^2)x+2mab\,y-cy^2,
\quad x^2+y^2\le1.
\tag{8}
\]

For fixed `y`, maximise the term linear in `x`. An optimum can always be chosen
on the circle `x^2+y^2=1`; when `a^2=b^2`, choose either boundary `x` without
changing the objective. Parameterising `x=cos(2phi)`, `y=sin(2phi)` converts the
right side of (8) into (3).

### Proof: attain every point needed for equality

For any `x,y` on that circle, put `P=ee^T` and define

\[
X=I_m+(x-1)P,\qquad Y=yP.
\tag{9}
\]

These matrices commute, `X^2+Y^2=I_m`, and `Tr Y^2=y^2`. Thus every inequality
in (6)–(8) is an equality. The resulting `B` is a symmetric involution that
anticommutes with `Omega`. Its `+1` eigenspace is a Lagrangian subspace, so
`K=(I+B)/2` is exactly a complete commuting-quadrature homodyne measurement.

Explicitly, a real orthogonal matrix sending `e` to the first basis vector
diagonalises `P`. Applying it to both `q` and `p` is a passive interferometer.
It transforms (9) into a single homodyne at angle `phi` on the first output and
`q` homodynes on the remaining outputs. It also sends the displacement tangent
to `(sqrt(m)a,sqrt(m)b)` in the first output while leaving every covariance
block and covariance derivative block unchanged. This proves attainability
and Theorem 1. `QED`

## 4. Computing the one remaining angle

Set `r=m|a^2-b^2|`, `s=2m|ab|`, and `c=lambda^2/2`. Formula (3) is equivalently

\[
F_m^G=m(a^2+b^2+c)
+\max_{0\le t\le1}\{r\sqrt{1-t^2}+st-ct^2\}.
\tag{10}
\]

The expression in braces is concave. If `r,s,c>0`, it has a unique maximiser in
`(0,1)` determined by

\[
s-2ct-\frac{rt}{\sqrt{1-t^2}}=0.
\tag{11}
\]

If `r=0` and `c>0`, the optimum is `t=min{s/(2c),1}`. If `s=0`, choose `t=0`.
The case `lambda=0` simply gives `F_m^G=2m(a^2+b^2)`.

## 5. Coherent-state squeezing: exact transition

Take the example in [1], with `sigma=I2`, `sigma'=diag(2,-2)` and
`d'=(alpha,-alpha)`. Put `A=m alpha^2`. Then

\[
\boxed{
F_m^G=
\begin{cases}
2m+2A+A^2/2,&0\le A\le2,\\
2m+4A-2,&A\ge2.
\end{cases}}
\tag{12}
\]

The bright-mode quadrature obeys `sin(2phi)=-min{A/2,1}`. At small total
displacement the best angle balances the mean and variance contributions.
At `A=2` it reaches the direction optimising displacement alone. The second
line of (12) proves optimality of the performance already attained in [1]
(and extends its validity condition from `alpha^2>=2` to `m alpha^2>=2`).

For `alpha=1/2`, the optima at `m=1,...,10` are

\[
81/32,\ 41/8,\ 249/32,\ 21/2,\ 425/32,\ 129/8,
\ 609/32,\ 22,\ 25,\ 28.
\]

## 6. Exact condition for strict collective advantage

For `m>1`, Theorem 1 implies

\[
F_m^G>mF_1^G\quad\Longleftrightarrow\quad\lambda ab\ne0.
\tag{13}
\]

To prove the nontrivial direction, let `phi_*` maximise the one-copy objective.
If `ab!=0`, neither covariance eigenaxis is stationary for the one-copy
objective: the derivative of its mean term at either axis is nonzero.
Thus `cos^2(2phi_*)<1`. Use `phi_*` as the bright-mode angle in (3). The
result exceeds `mF_1^G` by at least
`(m-1)c[1-cos^2(2phi_*)]>0`. Conversely, if `a=0` or `b=0`, one quadrature
simultaneously maximises both contributions, so local homodyne already reaches
the quantum Fisher information. If `lambda=0`, displacement-only information
is additive.

The invariant meaning of `ab!=0` is that the whitened displacement tangent is
not an eigenvector of the whitened covariance tangent, with zero vectors treated
separately. The condition is independent of signs and the ordering of the two
covariance eigenvectors.

## 7. Scope and checks

This is a local frequentist result at a fixed operating point. The copy number
can be finite, but the theorem does not assert that the Cramér–Rao bound for an
estimator is attained with finitely many repetitions. Ideal homodyne detection
is allowed; a finite measurement-squeezing or detector-noise constraint is a
different optimisation.

The proof does not use the equal-symplectic-eigenvalue covariance-only theorem
of [1]. It derives an upper bound directly over all collective pure measurement
seeds. A seeded numerical falsification check sampled 4,800 arbitrary pure
measurement covariances in dimensions corresponding to 1, 2, 3, 4, 6 and 8
copies, with random tangent parameters. No sampled measurement exceeded (3).
The explicit attaining homodyne matrices agreed with (3) to `4.3e-14`, and the
expanded matrix objective agreed with (2) to `1.3e-12`. These checks diagnose
normalisation or algebra errors; the inequalities above supply the proof.

## References

[1] J. Navarro, S. Morelli, M. Sanz and M. Mehboudi, *On super additivity of
Fisher information in fully Gaussian metrology*, arXiv:2512.20534v1 (2025).
https://arxiv.org/html/2512.20534v1

[2] M. F. B. Cenni, L. Lami, A. Acín and M. Mehboudi, *Thermometry of Gaussian
quantum systems using Gaussian measurements*, Quantum **6**, 743 (2022).
https://doi.org/10.22331/q-2022-06-23-743

[3] C. Oh et al., *Optimal Gaussian measurements for phase estimation in
single-mode Gaussian metrology*, npj Quantum Information **5**, 10 (2019).
https://doi.org/10.1038/s41534-019-0124-4

[3] studies the single-copy measurement problem and is relevant prior art for
the homodyne optimisation. The collective finite-copy upper bound in Theorem 1
is the intended contribution.
