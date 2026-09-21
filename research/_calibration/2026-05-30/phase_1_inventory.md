# Phase 1 — Inventory & Parse (2026-05-30)

**N = 18 blueprints.** All carry a schema-valid `decision.json` (`decision_valid=true`,
0 parse failures) and a co-located `phase-10-audit.md` (0 missing audits). No
`decision-vK` re-runs exist, so no version-dedup was needed. Parsed independently by
three agents; core fields triangulated and agree.

Today: **2026-05-30**. Latest `uw` available date: **2026-05-29** (all feeds agree).

## Roster
AAPL/05-27 · BABA/05-27 · CMPS/05-22 · ENPH/05-22 · GFS/05-27 · HOOD/05-27 ·
KWEB/05-22 · NOW/05-27 · NTAP/05-22 · NVDA/05-27 · NVDA/05-29 · PATH/05-22 ·
PATH/05-29 · PDD/05-26 · RDDT/05-22 · SMH/05-28 · SNOW/05-22 · SNOW/05-29.

## Breakdown
| Dimension | Distribution |
|---|---|
| **Bias** | RANGE 10 · NEUTRAL 5 · LONG 2 (ENPH, NOW) · SHORT 1 (GFS) |
| **Horizon** | 1-4w 12 · 1-5d 6 |
| **Conviction bin** | 0.55 → 12 · 0.65 → 6 · (no 0.75/0.85/0.95 in the set) |
| **Confluence band** | 0-29 → 0 · 30-49 → 5 · 50-64 → 10 · 65-79 → 3 · 80-100 → 0 |
| **Fundamentals gate** | CONFIRM 5 · CAUTION 6 · VETO 5 · NA 2 |

The book is structurally **low-conviction, premium-selling**: 15 of 18 are
RANGE/NEUTRAL, the entire corpus sits in conviction bins 0.55–0.65, and confluence
spans only 35–69 (no call ever cleared 70). There is essentially no directional,
high-conviction sample to calibrate the top of the apparatus against.

## Data-quality flags (carried into Phase 6 when N permits)
- **`signal_class` does not exist in the decision schema** — `null` for all 18. The
  calibration spec references a `signal_class` (the phase-5 backtest class) that the
  writer never persists. Spec/schema gap, not missing data.
- **`stop` / `primary_entry` are prose, not numbers.** `invalidation.price` is a
  free-text rule string on all 18 ("two daily closes outside 302-320…"); `levels`
  has no `primary_entry` key. `R_pct` is therefore `null` everywhere — the path-aware
  R-multiple in Phase 2 must parse the prose kill levels per blueprint.
- **`win_rate_source` serialization bugs (2):** `SNOW/2026-05-22` stores the literal
  string `"null"` (not JSON null) with `win_rate_n=13`; `PATH/2026-05-22` is real
  `null` with `n=0` yet `p=0.55` was still set. Add a writer guard.
- **`win_rate_source=fallback_bin` (2):** HOOD/05-27, PDD/05-26 (PDD also `n=0`).
- **Phase-10 audit template drift.** `NVDA/2026-05-29` uses a 0–20 point-weighted
  component table with **no ++/+/0/-/-- scorecard** (`phase_scores=null`).
  `BABA/2026-05-27`'s scorecard stops at 7b (phase-8 grade is prose-only). The three
  parsers also **disagree on individual phase glyphs** for several rows and on whether
  rows `7c`/`8b` exist — i.e. the scorecard format is not stable across blueprints.
  Per-phase attribution (Phase 4) is unsafe until the template is normalized **and**
  outcomes have seasoned.
- **VETO-but-sized (1):** `SNOW/2026-05-29` carries `fundamentals=VETO` yet
  `final_size_pct=1.0` (VETO blocks the directional short; a defined-risk condor carry
  is still sized). The other 4 VETOs (GFS, NVDA/05-29, PDD, RDDT) floor to size 0.0.
- **No share-class confusion.** (The SNOW 172→255 jump across 05-22→05-29 is a real
  post-earnings gap, not a mis-keyed price — confirmed in Phase 2.)
