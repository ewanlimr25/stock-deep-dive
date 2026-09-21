# Phase 10 — Audit & Confidence Score

**Ticker:** FSLR
**As-of date:** 2026-07-31
**Generated:** 2026-07-31
**Dominant bias audited:** **RANGE** (phase-9)

## Summary

**Confluence score 63 / 100. Recommended bin 0.65. Phase-9 chose 0.55 —
a MISMATCH, conservative by one bin, and it is allowed to stand.**
**Zero phases scored `-` or `--`; the contradiction log is empty by the
rubric's definition** — but that fact is itself the most important finding of
this audit and must not be read as an all-clear.

The run is **internally consistent to an unusual degree**. Three separate
self-corrections were caught *within* the run and propagated forward rather
than left to contradict later phases: phase-1 revised phase-0.5's
`unusual_verdict` from `GENUINELY_UNUSUAL` to `BUSY_NAME_NORMAL_DAY` after
proving UW's directional premium excludes 9.5% of the tape; phase-6 corrected
phase-0.5's "Technology is the most-sold sector" reading by extending the
measure from one session to five; and phase-7b discarded a corrupt Finnhub
earnings table that would otherwise have recorded Q2 as a **−24.7% miss**
instead of the verified **+37.1% beat** — a defect that would very likely have
flipped that gate to `VETO`.

**The auditor's principal caveat: this score is inflated by a rubric
mismatch.** `rubrics/confluence-scoring.md` scores each phase on whether it
"agrees with the dominant bias," a formulation built for LONG or SHORT theses.
Against a **RANGE** bias — effectively the null hypothesis — two-sided and
inconclusive phases score `0` rather than negative, and phases reporting "no
edge," "mixed," or "premium-selling" score *positively*. **A 63 here is not
comparable to a 63 on a directional blueprint.** The honest reading is that
the evidence robustly supports *doing very little*, which is exactly what
phase 9 recommends at **0.625% of book risk**.

Citation spot-check: **3 of 3 resolved.** All 15 phase files present.
`decision.json` backfilled and **re-validated `OK`**.

## Confluence scorecard

| Phase | Score | Justification (diagnostic datapoint) |
|-------|-------|--------------------------------------|
| **1 — flow** | **+** (+7) | Flow is real but produced nothing: `consistency_score` 0.80, 4 of 5 sessions in the top sweep names, `total_sweep_premium` **$17,278,108**, yet `dominant_direction: "mixed"` while price went **211.93 → 211.03** `[FLOW:sweep_persistence]`. The +$10.73M net customer delta is mildly directional, but the phase's own conviction is **2/5**. **Capped at `+` by the phase-0.5 context modifier** (`BUSY_NAME_NORMAL_DAY`). |
| **2 — dark pool** | **0** | Genuinely two-sided against a range thesis. Regular-session buying is real and flips at the earnings date (**28.4% → 64.2% → 73.1%**) `[DP:session_split DUCKDB]`, which is mildly bullish — but net accumulation ex-hedge is **+51,936 shares = 0.0512% of a 101.48M float**, which the phase itself calls "ordinary sizes for this name" `[DP:block_pct_float fz]`. Small and unproductive ≈ neutral. (Cap would have applied; it does not bind.) |
| **3 — OI** | **+** (+7) | Positioning is structurally range-shaped: near-term **put-skewed** (Aug-21 P/C **1.166**, Aug-07 **1.503**) beneath a far-dated book that is overwhelmingly call-side (Sep-18 P/C 0.382; Jan-2028 **22,142 calls / zero puts**) `[OI:term_structure]`, with **no pin risk and no OPEX concentration ≥40%**. Thin support layers 210 → 200 → 190 and a lone clean call wall at **217.5** `[OI:oi_by_strike]`. Discounted for the one-session lag and 38.9% chain coverage. |
| **4 — structure** | **++** (+15) | The strongest range-supporting phase. A **positive-gamma shelf from 202.5 to 217.5** (stabilising, mean-reverting) walled by negative pockets at 200 (−465,782) and 220 (−620,582); **net_gex +2,344,544 at 217.50 = 78% of the summed surface** `[STRUCT:gex]`; **max pain 205–210, below spot, on 4 of 5 near expiries** `[STRUCT:max_pain]`; **`term-skew` COMPLACENT** and **`front-end-iv-ratio` FLAT at 1.001** `[STRUCT:front_end_iv_ratio]`. |
| **5 — historical** | **++** (+15) | **VRP +0.3587** (IV 0.7378 vs realized 0.3791, independently verified at **0.3821**) with realized vol **falling** — 60d 0.5821 → 30d 0.3821 → 20d 0.3732 `[HIST:vrp]` `[HIST:realised_vol DUCKDB]`. Price has **based between 199.24 and 211.99 on close for twelve sessions**; 90-day cumulative premium flow is **+0.77% of gross, `MIXED`** `[HIST:cumulative_premium_flow]`. And the empirical test of the range: today's high **217.1274** stopped **0.17%** short of the wall `[HIST:intraday_range DUCKDB]`. |
| **6 — macro** | **0** | Genuinely two-sided, by the phase's own account. Against: 10y **4.68% (+24bp/30d)**, core PCE **+3.29%**, **three FOMC dissents preferring a hike**, and the **45Y/48E phaseout** for construction after 2026-07-04 `[MACRO:DGS10_2026-07-30 FRED]` `[MACRO:45Y48E_phaseout WebSearch:novoco.com]`. For: **45X preserved to 2032 at ~9% of market cap annually**, sector rotation **`aligned`** (+$839.5M over 5 sessions), Technology PEG **0.88** (lowest of eleven) `[MACRO:45X_policy WebSearch:novoco.com]`. Regime **TRANSITIONAL** with literal guidance *"Iron condors in range."* |
| **7 — insights** | **+** (+7) | The composite's dominant labels are range-consistent: `conviction_matrix` **MIXED at 8.8% confidence**, `institutional_accumulation` **NEUTRAL**, `price_vs_flow` **no divergence** `[INSIGHT:conviction_matrix]`. Its mild bearish tilt (bearish confluence **3**, bullish absent from top-300) slightly cuts against, but phase 7 itself documented that the dominant `bearish_flow` factor rests on the artifact-laden measure. |
| **7b — fundamentals** | **0** | `tier_adjustment = CAUTION`, `contradiction_count = 1`, `fundamental_signal = BULLISH` — two-sided and self-cancelling against a range thesis. For: **P/E 13.01 / forward 8.87 / PEG 0.33**, ROIC 16.69%, **Debt/Equity 0.02**, 2-of-2 verified beats `[FUND:peer_pe fz]`. Against: **operating cash flow −$214,866,000 vs +$346.6M net income**, cash **$2.4B → $1.7B**, **five C-suite officers selling ~720,802 shares on 2026-07-29**, MSPR negative four straight months `[FUND:operating_cash_flow]` `[FUND:insider_cluster fz]`. Not a VETO — the veto rule is not triggered. |
| **8 — agents** | **+8** (4 of 4 align) | **RANGE ×3, NEUTRAL ×1, zero LONG, zero SHORT, every agent at conviction 2/5**, converging unprompted on **205.83 / 217.50** `[AGENT:accumulation-hunter]` `[AGENT:sweep-tracker]` `[AGENT:risk-monitor]`. NEUTRAL counted as aligned — both it and RANGE decline a directional position. **Only 4 of 5 agents ran** (`earnings-scout` skipped by spec, earnings ~90d out), so the maximum available was +8, not +10. |

**Raw score (symmetric):** 7 + 0 + 7 + 15 + 15 + 0 + 7 + 0 + 8 = **+59**
(range −130 … +130)

**Base score:** round( (59 + 130) / 260 × 100 ) = round(72.69) = **73 / 100**

**Gate penalties (one-sided, applied after normalization):**
- Phase-8b debate — **`disconfirmed: true`** (bull residual **0.55** vs bear
  residual **0.85**) → **−5**
- Phase-7c sentiment — **`tier_adjustment = CAUTION`** (three price targets cut
  the day after a +37.1% beat) → **−5**
- Phase-7c VETO → not triggered → −0

**Confluence_score: 73 − 5 − 5 = 63 / 100**

**Recommended bin:** band 50–64 → **0.65**
**Phase-9 actual bin:** **0.55** → **MISMATCH (conservative by one bin)**

### On the mismatch

Phase 9 arrived at 0.55 by taking a 0.65 narrative base and applying the
phase-8b down-shift. The confluence formula **also** charges −5 for the same
disconfirmation. **The debate gate is therefore counted twice** — once inside
phase-9's bin selection, once in the score — and the 0.10 gap between the
recommended and actual bins is exactly that double-count.

Phase 9 anticipated this, writing *"No conviction deviation is claimed. If
phase-10's confluence band implies something other than 0.55, phase 10 should
override."* **This audit declines to override upward.** Raising a conviction
bin is not a correction the auditor should make: the deviation is downward,
the sizing rubric permits a smaller figure without justification, and every
independent check in the run points the same way — the desk was unanimous at
**2.0/5**, the composite reported **8.8% confidence**, and phase-9's
**0.625%** size matches the risk-monitor's independently derived *"1/8 of a
normal unit."*

**Recorded in `decision.json` as `confluence_score: 63`, `recommended_bin:
0.65`, with `conviction: 0.55` left unchanged.** Calibration should treat the
gap as a known methodological artifact, not a phase-9 error.

## Contradictions

**No phase scored `-` or `--`. The contradiction log is empty by the rubric's
definition.**

That result is an artifact of scoring a **RANGE** bias on a rubric written for
directional theses, and the auditor flags it explicitly rather than reporting
a clean bill of health. Under a RANGE hypothesis, a phase must argue for a
*decisive directional resolution* to contradict — and none did. Four material
tensions exist in the run and are recorded here even though none scored
negative:

- **phase-2 (dark pool) vs phase-9 (RANGE):** phase 2's verdict is
  **ACCUMULATION** at conviction 3/5, the highest directional conviction in the
  run, which argues for eventual upside resolution rather than a range. It
  scores `0` only because the accumulation is **0.0512% of float** and has
  produced no price movement. — **Resolution: wait for confirmation.** If
  regular-session dark-pool buy% holds above 50% for two more sessions *and*
  `FSLR260821C00230000` OI prints near ~2,155 on 2026-08-03, phase 2 upgrades
  to `+` for a LONG bias and the range thesis should be revisited.
- **phase-7b (fundamentals) vs phase-9 (RANGE):** `fundamental_signal =
  BULLISH` (P/E 13.01, forward 8.87, ROIC 16.69%, 2-of-2 beats) points to
  upside resolution, while the same phase's cash-flow and insider findings
  point down. — **Resolution: tighten invalidation.** The negative operating
  cash flow (−$214.9M) is the mechanism by which a cheap, high-ROIC name
  becomes a value trap; phase-9's signal-based invalidation should be treated
  as live, not decorative.
- **phase-6 (macro) vs phase-9 (RANGE):** phase 6's own net verdict is
  **HEADWIND (moderate)** — a directional read scored `0` here only because
  45X and the aligned sector rotation offset the rate complex. — **Resolution:
  downgrade on confirmation.** A 10-year above ~4.85% makes the macro the
  dominant driver regardless of flow, per phase-9's monitoring checklist.
- **phase-1 (flow) vs phase-7 (insights):** phase 1 reconstructs net customer
  delta at **+$10.73M long**; phase 7's composite reads **mildly bearish**
  because `signal-confluence` scores FSLR **3 on the bearish side**. — **Not a
  true contradiction and no resolution needed:** phase 1 reconciled UW's
  `bullish_premium`/`bearish_premium` to the cent from raw parquet and
  demonstrated the composite inherits a measure that **excludes $2,545,750
  (9.5% of the tape)**, including the day's largest opening print. Phase 7
  documented and accepted this. **Recorded so calibration does not later score
  it as an unresolved conflict.**

## Citation failures

**None — 3 of 3 spot-checked citations resolved to real datapoints in the
cited phase.**

| # | Citation (phase-9 thesis) | Resolves to | Verified |
|---|---------------------------|-------------|:--------:|
| 1 | `[DP:ts_confirm DUCKDB]` — 72,200-share QCT, **49.0s** lag, **101.1%** hedge match | `phase-2-dark-pool.md` §Cross-dataset confirmation — `lag_s = 49.0`, `hedge_match_pct = 101.1`, `trade_code = qualified_contingent_trade`, price 212.9695 vs `nbbo_ask` 212.54 | ✓ |
| 2 | `[FLOW:delta_notional DUCKDB]` — net customer delta **+$10.73M** vs screener −$2,374,671 | `phase-1-flow.md` §The classification gap — `net_customer_delta_notional_m = 10.73`; UW reconciliation `bullish 10,872,218` / `bearish 13,246,889` / **`unclassified 2,545,750`** | ✓ |
| 3 | `[STRUCT:gex]` — $217.50 `net_gex` **+2,344,544** = 78% of summed gamma | `phase-4-structure.md` §GEX — `.per_strike[] \| select(.strike==217.5).net_gex = 2344544.18`; Σ per_strike = 2,345,141 | ✓ |

Two further citations were checked opportunistically and also resolve:
**217.1274** (today's high) in `phase-5-historical.md` and **bear residual
0.85** in `phase-8b-debate.md`.

**Note on tag hygiene:** phase-9 uses two source qualifiers introduced after
the base convention — ` DUCKDB` (escape-hatch cuts) and ` fz` (Finviz). Both
are defined in `rubrics/citation-conventions.md` and correctly applied
throughout. No `[FLOW:?]`-style unresolvable tags were found.

## Sanity checks

| Check | Result |
|-------|:------:|
| All `phase-*.md` files present, incl. 0.5, 7b, 7c, 8b | ✓ — 14 phase files + `decision.json` |
| Phase-9 cites ≥3 distinct upstream datapoints | ✓ — **6** listed in §Citations summary, spanning phases 1, 2, 4, 5, 8, 8b |
| Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} | ✓ — 0.55 |
| ≥1 directional + ≥1 defined-risk structure | ✓ — Aug-21 **215/230 call debit spread** (directional) + Aug-21 **200/190 put credit spread** (defined-risk) |
| Sizing math shown explicitly | ✓ — p, b, raw_kelly, fraction, cap, gate-by-gate ladder 5.000 → 2.500 → 1.250 → **0.625%** |
| Kelly `p` from the phase-5 win-rate (or justified fallback) | ✓ — `p_raw` 1.00, `win_rate_n` 9, `win_rate_source` backtest, N-cap (n<10) → **p = 0.75**; the conviction-bin alternative is **also shown** (giving 0.3125%), with phase-9 taking the more conservative rubric-literal path and flagging the range |
| All five risk gates evaluated | ✓ — fundamentals **CAUTION** (fired), sentiment **CAUTION** (fired), correlation **null** (no-op), rotation **aligned** (no-op), debate **disconfirmed** (fired) |
| Phase-0.5 `unusual_verdict` reflected in sizing | ✓ — `BUSY_NAME_NORMAL_DAY` (as revised by phase 1) recorded in `decision.json.context` and cited in §Sizing as forbidding any upward deviation |
| Structures sized to the front-expiry expected move; `expected_move` in JSON | ✓ — 0.7625% / $1.611 daily, scaled to **±3.49% / $7.37** at 21 DTE; the debit spread's $15 width = **2.0×** the expected move; **the catalyst-gap check was performed and failed honestly** (a −3.49% CPI gap reaches ~203.66, below the 205.83 stop), with defined-risk structures given as the stated mitigation |
| `decision.json` exists and passes `validate_decision.py` | ✓ — `OK: … is a valid DeepDiveDecision`, re-validated after backfill |
| `confluence_score` / `recommended_bin` backfilled | ✓ — 63 / 0.65; `paths.audit` set to `phase-10-audit.md` |
| Every phase cites ≥1 prior phase by path | ✓ — verified in each header's *Upstream phases cited* |
| Disclaimer present at top of phase-9 | ✓ |
| Tool errors surfaced verbatim, not mocked | ✓ — see below |

**Tool-error discipline (a strength of this run).** Failures were surfaced
rather than smoothed over, and several materially changed conclusions:
`fz quote` degraded to 14 of 84 fields (phase 0, worked around via
`fz screen`); `sweep-persistence` and `price-levels` reject `--date` and anchor
to the latest date (phases 1, 2); the OI dataset is **one session stale** and
covers **38.9%** of the chain, which made phase-1's headline verification
impossible in phase 3 — stated plainly rather than faked; **six UW tools
inherit a cancelled 72,200-share print**, overstating dark-pool premium by
**17.4%**; `iv-term-structure` reports BACKWARDATION off a **224.2% 0DTE
artifact**; Yahoo returned **HTTP 401**, emptying both the fundamentals and the
entire analyst leg; Finnhub forward estimates are **paid-tier**; and Finnhub's
earnings table was **corrupt** and correctly discarded.

## Final auditor note

**The run is internally consistent and ready for action as written.** The
evidence chain is unusually well-cross-validated — the day's central claim (a
customer bought 1,900 Aug-21 $230 calls) is confirmed independently by the
options tape and by a 49-second, 101.1%-match dealer hedge in the dark pool,
and the day's central structural claim (resistance at $217.50) was confirmed
by three separate datasets *and* by price, which tagged 217.1274 and failed.

**No revision to phase 9 is required.** Its conviction sits one bin below the
confluence band, which is conservative and permitted; its **0.625%** size was
independently reproduced by the risk-monitor from different arithmetic; and
its two structures correctly express the one conclusion every phase supports —
**sell premium into a VRP of +0.3587 rather than buy direction into a stalemate.**
The single highest-value follow-up is cheap and dated: **check
`FSLR260821C00230000` open interest on the 2026-08-03 snapshot** — if it does
not print near ~2,155, the strongest bullish evidence in this blueprint
collapses and the range thesis should be re-scored to the downside.
