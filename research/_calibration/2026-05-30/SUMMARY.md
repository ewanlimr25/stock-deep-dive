# Deep-Dive Calibration — 2026-05-30

## ⛔ ABORTED at the threshold check — calibration math not run

**Insufficient *resolvable* calibration history: N = 4 resolvable blueprints (of 18
total). Below the floor of 8. The constraint is not corpus size — it is that the
outcome windows have not elapsed.** Per Step 0.3 (default `relax_threshold=false`),
Phases 3–6 (calibration, attribution, gates, compliance) are not run; reliability
tables and Brier scores on N=4 would be noise. Phases 1–2 are complete and saved.

> `relax_threshold=true` would **not** help here. Relaxing the size floor still leaves
> 14 of 18 genuinely unresolvable (windows not elapsed) — it cannot manufacture
> forward price action that hasn't happened yet. Re-run after the windows season.

## Why
All 18 blueprints were written **2026-05-22 → 05-29**; latest `uw` data is **05-29**.
The youngest are 0–1 trading days old; the oldest have 4 forward sessions. The rubric
needs **10D AND 21D** (1-4w) or **3D AND 10D** (1-5d). No blueprint has 10 forward
sessions, so the 10D leg is missing for every row. This corpus simply hasn't had time
to play out.

## What we can say (Phase 1 structural read — not outcome-dependent)
- **The book has no high end to calibrate.** 15 of 18 are RANGE/NEUTRAL; every call
  sits in conviction 0.55–0.65; confluence spans only **35–69 — nothing ever cleared
  70.** When calibration does run, it will only test the *bottom three* bands; the
  "score 80" claim in the rubric's premise remains entirely unfalsified because no
  score-80 blueprint exists.
- **Three data-integrity bugs to fix before the next run** (Phase 1): `signal_class`
  is in the calibration spec but never persisted by the writer (null ×18);
  `win_rate_source` serializes as the string `"null"` (SNOW/05-22) and as real-null-
  with-p-still-set (PATH/05-22); and the phase-10 audit **scorecard template is not
  stable** (NVDA/05-29 has no ±grades; BABA stops at 7b; parsers disagree on glyphs).
  Per-phase/tool attribution (Phase 4) is impossible until the template is normalized.

## Early read (N=4, FLAGGED — not signal, and adversely selected)
Terminal-condition resolutions only: **SNOW/05-22, HOOD/05-27, RDDT/05-22, PDD/05-26 —
all LOSS (4/4).** Do **not** read this as "the skill loses": RANGE/NEUTRAL premium
trades only resolve this fast when a tail event breaks the range (two earnings gaps,
two sharp trend breaks), so the early-resolving subset is *structurally biased toward
losers* — the 14 quietly-pinning INCONCLUSIVE blueprints could be the winners. Two
reads survive the caveat: (1) the only two trades that carried real size (SNOW 1.0,
HOOD 0.5) both lost; (2) the fundamentals **VETO floored RDDT and PDD to 0 — both then
lost**, i.e. the gate *avoided* losers here rather than over-cutting. Re-test, don't act.

## Gate verdict
INSUFFICIENT_N on every gate (fundamentals VETO fired 5×, only 2 resolved — both
losers, a protective-but-unproven hint; correlation/rotation/debate all <5 resolved).
No KEEP/TIGHTEN/LOOSEN is defensible.

## What we'd change before the next deep dive
Nothing in the rubric — the data can't justify a weight or gate change yet. The single
highest-value action is **operational: re-run this calibration ~2026-06-12** (1-5d
cohort + the 10D leg of the 1-4w cohort clear then; ~N≥8 becomes resolvable), and a
full pass **late June** once the 21D legs close. Before that re-run, patch the three
Phase-1 writer bugs so the seasoned outcomes attribute cleanly. Until then, the
confluence→conviction apparatus remains **unverified, not validated** — allocate
accordingly.
