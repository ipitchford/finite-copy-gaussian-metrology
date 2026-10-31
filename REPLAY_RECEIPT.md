# Replay receipt

- **31 October 2026, working tree:** `python -B verification/verify_all.py` and `python -O -B verification/verify_all.py`, macOS arm64, CPython 3.12, numpy 2.3.5, scipy 1.17.0 (uv.lock), one core via the local research queue: both ALL PASS (11 check groups), identical `results.json`, about 100 s each.
- **31 October 2026, frozen archive:** the same two runs from a fresh extraction of `finite-copy-gaussian-metrology-1.0.0-candidate.zip`, with output compared to the retained `results.json` (recorded in the publisher's private gate receipt).
- **CI:** `.github/workflows/replay.yml` on ubuntu-latest runs SHA256SUMS, both modes, and an unchanged-tree check.
- **Original note (28 October 2026):** its script was replayed from a fresh extraction of the research bundle on 31 October 2026 and reproduced its recorded statistics (4,800 seeds, no excess; attainment error below 1e-13).
