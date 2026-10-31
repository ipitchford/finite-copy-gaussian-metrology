#!/usr/bin/env python3
"""Numerical and exact checks for "One bright mode is enough" (finite-copy Gaussian Fisher information).

These checks test normalisations, implementations and the stated formulas; they are not proofs.
Every check records PASS/FAIL; the script exits with status 1 if any check fails (no use of assert,
so the result is the same under python -O). Results are written to results.json beside this script.

Run:  OPENBLAS_NUM_THREADS=1 python -B verify_all.py
"""
from __future__ import annotations
import json, math, platform, sys
from fractions import Fraction
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import expm, eigh
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
rng = np.random.default_rng(20261031)
RESULTS: dict = {"environment": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__}, "checks": {}}
FAILED: list[str] = []

def record(name, ok, **info):
    RESULTS["checks"][name] = {"pass": bool(ok), **info}
    if not ok:
        FAILED.append(name)
    print(("PASS " if ok else "FAIL ") + name, {k: v for k, v in info.items() if not isinstance(v, list)})

# ---------- closed forms ----------
def F_main(m, lam, a, b, n_grid=400001):
    ph = np.linspace(0.0, np.pi, n_grid)
    return (m - 1) * lam**2 / 2 + float(np.max(2 * m * (a * np.cos(ph) + b * np.sin(ph))**2 + lam**2 / 2 * np.cos(2 * ph)**2))

def argmax_phi(m, lam, a, b, n_grid=400001):
    ph = np.linspace(0.0, np.pi, n_grid)
    return float(ph[np.argmax(2 * m * (a * np.cos(ph) + b * np.sin(ph))**2 + lam**2 / 2 * np.cos(2 * ph)**2)])

def F_cap(m, lam, a, b, beta, n_grid=400001):
    c = lam**2 / 2
    ph = np.linspace(0.0, 2 * np.pi, n_grid)
    x, y = beta * np.cos(ph), beta * np.sin(ph)
    return m * (a * a + b * b) + m * lam**2 / 4 * (1 + beta**2) + float(np.max(m * (a * a - b * b) * x + 2 * m * a * b * y - c * y * y))

def Omega(n):
    return np.block([[np.zeros((n, n)), np.eye(n)], [-np.eye(n), np.zeros((n, n))]])

def gaussian_FI(mu1, C, C1):
    Ci = np.linalg.inv(C)
    return float(mu1 @ Ci @ mu1 + 0.5 * np.trace(Ci @ C1 @ Ci @ C1))

def tangents(m, lam, a, b, k=0):
    n = m + k
    v = np.concatenate([a * np.r_[np.ones(m), np.zeros(k)], b * np.r_[np.ones(m), np.zeros(k)]])
    H = lam * np.diag(np.r_[np.ones(m), np.zeros(k), -np.ones(m), np.zeros(k)])
    return v, H

def F_seed(M, m, lam, a, b):
    """General-dyne seed: outcome law N(d, (I+M)/2)."""
    v, H = tangents(m, lam, a, b)
    return gaussian_FI(v, (np.eye(2 * m) + M) / 2, H / 2)

def passive(n):
    """Random orthogonal symplectic matrix (passive interferometer) from a random unitary."""
    Z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Q, R = np.linalg.qr(Z); Q = Q * (np.diag(R) / abs(np.diag(R)))
    return np.block([[Q.real, -Q.imag], [Q.imag, Q.real]])

def random_pure_seed(m, rmax):
    """Bloch-Messiah: M = O Z^2 O^T with passive O and single-mode squeezers |r|<=rmax."""
    r = rng.uniform(-rmax, rmax, size=m)
    O = passive(m)
    Z2 = np.diag(np.r_[np.exp(2 * r), np.exp(-2 * r)])
    return O @ Z2 @ O.T

def random_symplectic(n, scale=0.8):
    A = rng.normal(size=(2 * n, 2 * n)); A = (A + A.T) / 2 * scale
    return expm(Omega(n) @ A)

def rand_params():
    lam = abs(rng.normal()) * 2
    a, b = rng.normal(size=2)
    return lam, float(a), float(b)

# ---------- (a) random pure general-dyne seeds ----------
worst = -np.inf; count = 0; invalid = 0
for m in (1, 2, 3, 4, 6, 8):
    for _ in range(800):
        lam, a, b = rand_params()
        M = random_pure_seed(m, rmax=float(rng.uniform(0.05, 2.5)))
        pur = np.linalg.norm(M @ Omega(m) @ M - Omega(m)) / np.linalg.norm(M)
        if pur > 1e-8 or np.min(np.linalg.eigvalsh(M)) <= 0:
            invalid += 1
            continue
        bnd = F_main(m, lam, a, b, 20001)
        worst = max(worst, (F_seed(M, m, lam, a, b) - bnd) / (1 + bnd)); count += 1
record("a_random_pure_seeds_below_bound", worst <= 1e-6 and invalid == 0 and count == 4800, samples=count, invalid_seeds=invalid, worst_relative_excess=worst,
       note="grid of 20001 angles; tolerance 1e-6 covers grid discretisation")

# ---------- (b) ancilla-assisted homodyne, FI from outcome law ----------
worst = -np.inf; count = 0
for _ in range(3000):
    m = int(rng.integers(1, 4)); k = int(rng.integers(0, 4)); n = m + k
    lam, a, b = rand_params()
    v, H = tangents(m, lam, a, b, k)
    S = random_symplectic(n)
    G = S[:n, :]                      # detect q-quadratures of the transformed modes
    FI = gaussian_FI(G @ v, G @ G.T / 2, G @ H @ G.T / 2)
    bnd = F_main(m, lam, a, b, 20001)
    worst = max(worst, (FI - bnd) / (1 + bnd)); count += 1
record("b_ancilla_homodyne_below_bound", worst <= 1e-6, samples=count, worst_relative_excess=worst)

# ---------- (c) local maximisation over pure seeds ----------
def seed_from_params(p, m):
    n = 2 * m; A = np.zeros((n, n)); iu = np.triu_indices(n); A[iu] = 2.5 * np.tanh(p)
    A = A + A.T - np.diag(np.diag(A)); S = expm(Omega(m) @ A); return S @ S.T
worst = -np.inf; short = []
for _ in range(24):
    m = int(rng.integers(1, 4)); lam, a, b = rand_params(); bnd = F_main(m, lam, a, b)
    kdim = (2 * m) * (2 * m + 1) // 2; best = -np.inf
    for _s in range(3):
        r = minimize(lambda p: -F_seed(seed_from_params(p, m), m, lam, a, b), rng.normal(size=kdim) * 0.5,
                     method="BFGS", options={"maxiter": 300})
        best = max(best, -r.fun)
    worst = max(worst, (best - bnd) / (1 + bnd)); short.append((bnd - best) / (1 + bnd))
record("c_local_maximisation_never_exceeds", worst <= 1e-6, instances=24, worst_relative_excess=worst,
       median_relative_shortfall=float(np.median(short)), note="acceptance tests non-exceedance only; shortfall recorded for information")

# ---------- attainment: direct homodyne outcome law ----------
def attain_direct(m, lam, a, b, phi):
    mu1 = np.zeros(m); mu1[0] = math.sqrt(m) * (a * math.cos(phi) + b * math.sin(phi))
    C = np.eye(m) / 2; C1 = np.diag(np.r_[lam / 2 * math.cos(2 * phi), lam / 2 * np.ones(m - 1)])
    return gaussian_FI(mu1, C, C1)

def attain_via_interferometer(m, lam, a, b, phi):
    """Build the interferometer explicitly and compute FI of the detected quadratures."""
    e = np.ones(m) / math.sqrt(m)
    Q, _ = np.linalg.qr(np.column_stack([e, rng.normal(size=(m, m - 1))])) if m > 1 else (np.array([[1.0]]), None)
    if Q[:, 0] @ e < 0: Q[:, 0] *= -1
    O = Q.T                                           # first row = e
    Ofull = np.block([[O, np.zeros((m, m))], [np.zeros((m, m)), O]])
    v, H = tangents(m, lam, a, b)
    G = np.zeros((m, 2 * m))
    G[0, 0], G[0, m] = math.cos(phi), math.sin(phi)
    for j in range(1, m): G[j, j] = 1.0
    G = G @ Ofull
    return gaussian_FI(G @ v, G @ G.T / 2, G @ H @ G.T / 2)

worst = 0.0
for _ in range(400):
    m = int(rng.integers(1, 9)); lam, a, b = rand_params(); phi = argmax_phi(m, lam, a, b)
    f = F_main(m, lam, a, b)
    worst = max(worst, abs(attain_direct(m, lam, a, b, phi) - f) / (1 + f), abs(attain_via_interferometer(m, lam, a, b, phi) - f) / (1 + f))
record("attainment_matches_formula", worst <= 1e-9, instances=400, worst_relative_error=worst)

# ---------- (d) squeezing cap ----------
worst_b = -np.inf; worst_att = 0.0
for _ in range(1500):
    m = int(rng.integers(1, 5)); lam, a, b = rand_params(); R = float(rng.uniform(0.05, 3.0)); beta = math.tanh(R / 2)
    M = random_pure_seed(m, rmax=R / 2)
    bnd = F_cap(m, lam, a, b, beta, 40001)
    worst_b = max(worst_b, (F_seed(M, m, lam, a, b) - bnd) / (1 + bnd))
for _ in range(300):
    m = int(rng.integers(1, 6)); lam, a, b = rand_params(); R = float(rng.uniform(0.05, 3.0)); beta = math.tanh(R / 2)
    c = lam**2 / 2
    ph = np.linspace(0, 2 * np.pi, 400001); xs, ys = beta * np.cos(ph), beta * np.sin(ph)
    i = int(np.argmax(m * (a * a - b * b) * xs + 2 * m * a * b * ys - c * ys * ys)); x, y = xs[i], ys[i]
    e = np.ones(m) / math.sqrt(m); P = np.outer(e, e)
    X = beta * np.eye(m) + (x - beta) * P; Y = y * P
    B = np.block([[X, Y], [Y, -X]]); I2 = np.eye(2 * m)
    M = (I2 - B) @ np.linalg.inv(I2 + B)
    pur = np.linalg.norm(M @ Omega(m) @ M - Omega(m)); ev = np.sort(np.linalg.eigvalsh(M))
    spec = max(abs(ev[0] - math.exp(-R)), abs(ev[-1] - math.exp(R)))
    f = F_cap(m, lam, a, b, beta, 400001)
    worst_att = max(worst_att, abs(F_seed(M, m, lam, a, b) - f) / (1 + f), pur, spec)
record("d_cap_bound_and_attainment", worst_b <= 1e-6 and worst_att <= 1e-8, bound_samples=1500,
       worst_relative_excess=worst_b, attainment_instances=300, worst_attainment_or_purity_error=worst_att)
# heterodyne limit R=0 and homodyne limit R->inf
ok = True
for _ in range(50):
    m = int(rng.integers(1, 6)); lam, a, b = rand_params()
    ok &= abs(F_cap(m, lam, a, b, 0.0) - m * (a * a + b * b + lam**2 / 4)) < 1e-9
    ok &= abs(F_cap(m, lam, a, b, 1.0) - F_main(m, lam, a, b)) < 1e-6 * (1 + F_main(m, lam, a, b))
record("d_cap_limits", ok)

# ---------- (e) QFI formula Q = 2D + lam^2/2 (Fock space) ----------
Nf = 120
an = np.diag(np.sqrt(np.arange(1, Nf)), 1); ad = an.T
qo = (an + ad) / math.sqrt(2); po = (an - ad) / (1j * math.sqrt(2))
def fstate(th):
    x0, p0, r, phs = 0.3 + 0.7 * th, -0.2 + 0.4 * th, 0.25 + 0.3 * th, 0.4 - 0.5 * th
    alpha = (x0 + 1j * p0) / math.sqrt(2); z = r * np.exp(2j * phs)
    S = expm(0.5 * (np.conj(z) * an @ an - z * ad @ ad)); Dd = expm(alpha * ad - np.conj(alpha) * an)
    vac = np.zeros(Nf, complex); vac[0] = 1; return Dd @ S @ vac
def fmoments(psi):
    Rr = [qo, po]; d = np.array([np.vdot(psi, X @ psi).real for X in Rr])
    s = np.array([[np.vdot(psi, (X @ Y + Y @ X) @ psi).real - 2 * d[i] * d[j] for j, Y in enumerate(Rr)] for i, X in enumerate(Rr)])
    return d, s
h = 1e-5; th = 0.1
pp, pm, p0 = fstate(th + h), fstate(th - h), fstate(th)
dpsi = (pp - pm) / (2 * h); qfi = 4 * (np.vdot(dpsi, dpsi).real - abs(np.vdot(p0, dpsi))**2)
(d1, s1), (d2, s2), (d0, s0) = fmoments(pp), fmoments(pm), fmoments(p0)
dd = (d1 - d2) / (2 * h); dsg = (s1 - s2) / (2 * h); si = np.linalg.inv(s0)
qform = 2 * dd @ si @ dd + 0.25 * np.trace(si @ dsg @ si @ dsg)
# same model in normal form: whiten with T (sigma = T T^T), rotate to diagonal tangent
w, V = np.linalg.eigh(s0); T = V @ np.diag(np.sqrt(w)) @ V.T; Ti = np.linalg.inv(T)
At = Ti @ dsg @ Ti.T; lw, lv = np.linalg.eigh(At); lam_n = float(lw[-1]); dn = lv.T @ (Ti @ dd)
Qnf = 2 * float(dn @ dn) + lam_n**2 / 2
record("e_qfi_normal_form", abs(qfi - qform) < 1e-5 * (1 + qfi) and abs(qfi - Qnf) < 1e-5 * (1 + qfi) and abs(np.linalg.det(s0) - 1) < 1e-9,
       qfi_fock=float(qfi), qfi_moment_formula=float(qform), qfi_normal_form=Qnf)

# ---------- (f) exact rational example table (alpha = 1/2) ----------
def F_example(m, alpha2):
    A = m * alpha2
    return 2 * m + 2 * A + A * A / 2 if A <= 2 else 2 * m + 4 * A - 2
al2 = Fraction(1, 4); Qc = 2 * (2 * al2) + 2
tab = [(m, F_example(m, al2), m * F_example(1, al2), m * Qc - F_example(m, al2)) for m in range(1, 11)]
expectF = [Fraction(81, 32), Fraction(41, 8), Fraction(249, 32), Fraction(21, 2), Fraction(425, 32), Fraction(129, 8), Fraction(609, 32), 22, 25, 28]
expectGap = [Fraction(15, 32), Fraction(7, 8), Fraction(39, 32), Fraction(3, 2), Fraction(55, 32), Fraction(15, 8), Fraction(63, 32), 2, 2, 2]
okf = [t[1] for t in tab] == expectF and [t[3] for t in tab] == expectGap
numok = all(abs(F_main(m, 2.0, 0.5, -0.5) - float(F)) < 1e-8 for m, F in zip(range(1, 11), expectF))
record("f_example_table_exact", okf and numok, table=[[t[0], str(t[1]), str(t[2]), str(t[3])] for t in tab])

# ---------- (g) deterministic degenerate cases and strictness criterion ----------
cases = [(0, 0, 0), (0, 1.3, 0), (0, 0.7, -0.4), (1.5, 0, 0), (1.5, 0.8, 0), (1.5, 0, -0.9), (1.5, 0.6, 0.6), (1.5, 0.6, -0.6),
         (2.0, 0.5, -0.5), (0.9, 1.1, 0.3)]
ok = True; rows = []
for lam, a, b in cases:
    for m in (1, 2, 5):
        f = F_main(m, lam, a, b); phi = argmax_phi(m, lam, a, b)
        ok &= abs(attain_direct(m, lam, a, b, phi) - f) < 1e-9 * (1 + f)
        Q = 2 * (a * a + b * b) + lam**2 / 2
        ok &= f <= m * Q + 1e-9
        if m > 1:
            strict = f > m * F_main(1, lam, a, b) + 1e-9
            ok &= strict == (lam * a * b != 0)
            rows.append([lam, a, b, m, f, strict])
for A in (2 - 1e-3, 2.0, 2 + 1e-3):
    m = 4; alpha2 = A / m
    ok &= abs(F_main(m, 2.0, math.sqrt(alpha2), -math.sqrt(alpha2)) - F_example(m, alpha2)) < 1e-8
record("g_degenerate_cases_and_strictness", ok, cases=rows)

# ---------- (h) shortfall corollary ----------
ok = True; worst = 0.0
for _ in range(300):
    lam, a, b = rand_params(); D = a * a + b * b; c = lam**2 / 2
    lim = 2 * lam**2 * a * a * b * b / D**2
    gaps = [m * (2 * D + c) - F_main(m, lam, a, b) for m in range(1, 41)]
    ok &= all(g2 >= g1 - 1e-7 for g1, g2 in zip(gaps, gaps[1:]))
    ok &= all(-1e-7 <= g <= lim + 1e-7 for g in gaps)
    ok &= lim <= c + 1e-12
    # gap identity (eq:gap) at moderate m, and its large-m value near the limit
    dl = math.atan2(b, a); ph = np.linspace(0, math.pi, 400001)
    for m in (1, 3, 17):
        alt = float(np.min(2 * m * D * np.sin(ph - dl)**2 + c * np.sin(2 * ph)**2))
        ok &= abs(alt - gaps[m - 1]) < 1e-6 * (1 + alt)
    if D > 0.3:
        mm = 10**7; t = dl + np.linspace(-0.02, 0.02, 400001)
        big = float(np.min(2 * mm * D * np.sin(t - dl)**2 + c * np.sin(2 * t)**2))
        worst = max(worst, abs(big - lim))
record("h_shortfall_monotone_bounded_limit", ok and worst < 1e-3, instances=300, worst_abs_limit_error_at_m_1e7=worst)

# ---------- (i) negative controls: wrong formulas must be rejected ----------
def detects(wrong):
    """A wrong closed form is rejected if an explicitly attained FI exceeds it, or it exceeds the true optimum."""
    for _ in range(200):
        m = int(rng.integers(2, 6)); lam, a, b = rand_params(); phi = argmax_phi(m, lam, a, b)
        att = attain_direct(m, lam, a, b, phi); w = wrong(m, lam, a, b)
        if att > w + 1e-6 * (1 + w) or w > F_main(m, lam, a, b) + 1e-6:
            return True
    return False
controls = {
    "missing_dark_mode_term": lambda m, lam, a, b: F_main(m, lam, a, b) - (m - 1) * lam**2 / 2,
    "mean_term_factor_1": lambda m, lam, a, b: (m - 1) * lam**2 / 2 + max(m * (a * math.cos(t) + b * math.sin(t))**2 + lam**2 / 2 * math.cos(2 * t)**2 for t in np.linspace(0, math.pi, 20001)),
    "additive_m_times_F1": lambda m, lam, a, b: m * F_main(1, lam, a, b),
    "quantum_limit_claimed_attained": lambda m, lam, a, b: m * (2 * (a * a + b * b) + lam**2 / 2),
}
res = {k: detects(f) for k, f in controls.items()}
record("i_negative_controls_rejected", all(res.values()), controls=[[k, v] for k, v in res.items()])

RESULTS["all_pass"] = not FAILED
(HERE / "results.json").write_text(json.dumps(RESULTS, indent=1, default=float) + "\n")
print("ALL PASS" if not FAILED else f"FAILED: {FAILED}")
sys.exit(1 if FAILED else 0)
