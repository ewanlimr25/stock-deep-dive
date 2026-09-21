# Phase 10 — Audit & Confidence Score

**Ticker:** ENPH · **As-of date:** 2026-07-29 · **Spot 35.07**
**Generated:** 2026-07-30T04:24:00Z
**Dominant bias audited:** **SHORT** (from `phase-9-trade-plan.md` / `decision.json`)

---

## Summary

**Confluence score 62 / 100 → recommended bin 0.65. Phase 9 chose 0.55 — a MISMATCH, and the
mismatch is correct.**

**Zero phases scored `-` or `--`. Not one of the eight signal phases contradicted the SHORT
direction.** That is the defining feature of this run and it needs stating plainly: the case
against acting did **not** come from directional disagreement. It came entirely from (a) the
one-sided gates — `phase-7c-sentiment.md` **VETO** (−10) and `phase-8b-debate.md`
**disconfirmed** (−5) — and (b) magnitude and entry considerations that the confluence rubric does
not score at all.

Raw score **+70** of a possible ±130 → base **77**, less the 15 points of one-sided gate penalty →
**62**. The 50–64 band maps to bin **0.65**. Phase 9 published **0.55** because
`rubrics/sizing-rubric.md` gate 5 *requires* a one-bin down-shift when the debate is
disconfirmed — a step the confluence table does not model. **Both rubrics were applied correctly;
they simply account for the same disconfirmation in different places.** Phase 9's 0.55 is the more
conservative of the two and I am not asking it to revise upward. See §Contradictions.

**All 15 expected artifacts are present** (13 phase MDs including 0.5 / 7b / 7c / 8b, plus
`phase-9-trade-plan.md` and `decision.json`). **All three spot-checked citations resolved
exactly**, plus a fourth I checked because it carries the most weight. `decision.json` **passes
`validate_decision.py`** after backfill.

**The run is internally consistent and I found no fabricated or unsourced number.** Twelve genuine
inter-phase tensions arose during the run; **all twelve were caught and resolved in-flight** by
the phase that found them, and each is logged in §Resolved tensions rather than left for this
audit to discover. Four of them were **vendor data defects** that would have produced false
statements if quoted as returned.

---

## Confluence scorecard

| Phase | Score | Justification (diagnostic datapoint) |
|---|---|---|
| **1 — flow** | **+** | Whole-tape `put_volume_ask_side` **7,236** vs `put_volume_bid_side` **4,613** = **1.569×** puts bought with calls dead-even at **1.000**, net aggressive direction **−2,622** contracts, ~90% of volume classified [FLOW:ask_bid_split DUCKDB]; gap +9.03% fully engulfed to close $0.11 off the low. **Capped at `+` by the phase-0.5 context modifier** (BUSY_NAME_NORMAL_DAY) — and independently deserved, since `net_flow` **−$479,813** is **5.8× below** the day's bearish top-50 cutoff. |
| **2 — dark pool** | **+** | Large-tier `buy_ratio` **0.390** → derived `sell_ratio` **0.610** on **188 trades** / $32.7M, artifact-free, corroborated by an auction-stripped top-25 recount at **69.7% below mid** [DP:block_stratified][DP:largest]; close **3.3% below** the 36.27 dark-pool VWAP. **Capped at `+`** by the same context modifier; also absent from the dark-pool top-30 against a $1.043B cutoff. |
| **3 — OI** | **++** | **`ENPH280121P00030000` +2,000 OI for `prev_total_premium` $2,837,716 at 92% ask-side** (2,908 vs 253), `dte` 541, `inferred_direction` **bearish**, opened **pre-print** [OI:biggest_increases][OI:smart_positioning]; premium-weighted builds **5.4 : 1 bearish** ($2,910,482 vs $535,495); `position-rolls` **zero rows**. **The only lane in the run where the magnitude is not trivial** — ~6× the day's entire net option flow. |
| **4 — structure** | **++** | `net_gex` negative at **every strike 25 → 36.5 without exception** (40: −1,165,778 · 35: −977,948 · 30: −471,049), `atm_flip_strike` **36** with spot **below** it, the 35 strike tagged **`resistance_wall`**, and `net_dex` **−$65,123,664 = 1.41% of float** whose own `interpretation` reads *"dealer hedge is to SELL underlying"* [STRUCT:gex][STRUCT:today_gamma_flip][STRUCT:dex]. The phase's own two-sidedness (`net_vanna` +1,327) was **resolved against the bull by phase 6**. |
| **5 — historical** | **+** | `total_gex` negative **26 consecutive sessions** while spot fell **−24.7%**; `bearish_days` **21 of 30** through a **−30.2%** decline; the three large bullish premium spikes were **put-selling and 3-for-3 wrong** (avg −7.9%) [HIST:gex_time_series][HIST:trend]. Held at `+` not `++` because `cumulative-premium-flow` `trend_direction` is **MIXED** over 76 sessions and the phase's headline edge metric — `signal-backtest` **100% on N=9** — had to be **discarded as unusable**. |
| **6 — macro** | **+** | **VIX 18.21 → 20.66 (+13.5% d/d, +23.5%/10d)** invalidates phase-4's vanna trigger (*"if VIX collapses"*), leaving negative gamma unopposed [MACRO:VIX_2026-07-29 UW]; `DGS10` **4.61% (+23bp/30d)** bear steepener into a hawkish 9–3 hold, plus a structural solar demand shock (30% ITC sunset, **ENPH guides −22%**). Held at `+` because the single largest tailwind — Technology sector flow **INFLOW at `persistence_score` 1.0** — is **adverse to this short** and fired as sizing gate 4. |
| **7 — insights** | **+** | `conviction-matrix` **DIRECTIONAL_SHORT**, *"Dark pool selling + put buying — institutional bear bet"*; `institutional-accumulation` **DISTRIBUTION**; `price-vs-flow` `divergence` **false** (aligned bearish, −30.22%) [INSIGHT:conviction_matrix][INSIGHT:institutional_accumulation][INSIGHT:price_vs_flow]. Held at `+` because the **same** instrumentation caps it: `confidence_pct` **24** and `signal-confluence` **3 of 6 — the minimum in a 500-name set, shared with 348 others**. |
| **7b — fundamentals** | **+** | `fundamental_signal` **BEARISH**, `tier_adjustment` **CAUTION**, `contradiction_count` **1**: two of three axes **confirm** the short — `revenueGrowthQuarterlyYoy` **−20.55%** with `pegTTM` **−5.45**, and EPS **0.90 → 0.71 → 0.47 → 0.46 (−49%)** with beat magnitude decaying to a **first miss** [FUND:metric][FUND:earnings_surprises]. Only insider MSPR contradicts, and weakly (net **−178,209 shares** despite a +23.03 mean). **Not `++`** — the fortress balance sheet (current ratio 3.799, $930.6M liquid, ~7.2% FCF yield, Forward P/E 15.82) is a real floor under a short. **Not capped at `--`**: that rule applies only to a `VETO`, and 7b is CAUTION. |
| **8 — agents** | **−2 net** | 2 aligned (SHORT: earnings-scout, risk-monitor) = **+4**; 3 not aligned (NEUTRAL: accumulation-hunter, contrarian-scanner, sweep-tracker) = **−6**. **Zero LONG votes; every agent returned conviction 2, range 0.** |

**Score computation** (per `rubrics/confluence-scoring.md`):

```
Eight signal phases:  +7 +7 +15 +15 +7 +7 +7 +7            =  +72
Phase-8 desk:         2×(+2) + 3×(−2)                      =   −2
                                                    raw    =  +70   (of ±130)

base_score = round((70 + 130) / 260 × 100)                 =   77

  − 5   phase-8b disconfirmed = true (bear 0.75 ≥ bull 0.65)
  − 10  phase-7c tier_adjustment = VETO
  − 0   phase-7c CAUTION penalty n/a (it is VETO, not CAUTION)

confluence_score                                           =   62 / 100
```

**Recommended bin (band 50–64): 0.65**
**Phase-9 actual bin: 0.55** → **MISMATCH — phase 9 is one bin MORE conservative. Adjudicated in
favour of phase 9; see §Contradictions.**

> **Note on the phase-8 scoring convention, stated because it is consequential.** The rubric
> allots each agent **±2** with no neutral option. I scored the three NEUTRAL verdicts as **−2**,
> i.e. identically to an opposing LONG vote, because they do not support the directional thesis.
> That is the rubric as written, but it arguably overstates disagreement — none of the three
> argued *against* the bearish direction; all three said *"bearish direction, nothing tradeable."*
> **Had NEUTRAL been scored 0, the raw would be +76, base 79, and confluence 64 — still inside the
> 50–64 band and still recommending 0.65.** The conclusion is insensitive to the convention, which
> is why I applied the stricter reading.

---

## Contradictions

**No phase scored `-` or `--`, so the contradiction log has no per-phase entries.** All eight
signal phases agreed with the SHORT bias. Recorded per the rubric's instruction to write the audit
even when phases agree.

**One structural discrepancy does require adjudication:**

- **phase-9 vs phase-10 (conviction bin): phase 9 published 0.55 where the confluence band
  recommends 0.65** — a one-bin gap. **Resolution: phase 9 is correct; no revision requested.**
  `rubrics/sizing-rubric.md` gate 5 states that when the debate is disconfirmed, phase 9 must
  *"down-shift the conviction bin by one and cut one size step."* Phase 9 started at 0.65 (the band
  it would otherwise occupy, and exactly what this audit independently computes) and applied the
  mandatory down-shift to **0.55**. Meanwhile `rubrics/confluence-scoring.md` charges its own
  **−5** for the same disconfirmation. **Both rubrics are applied correctly; the same
  disconfirmation is simply accounted for in two places, once as a score penalty and once as a bin
  down-shift.** The net effect is that phase 9 sits one bin below the band — the conservative
  direction. Since `final_size_pct` is **0.0** either way, the gap has **no effect on the
  recommended action**. **Propose-only note for the rubric maintainers:** the confluence-band table
  does not model gate 5's bin down-shift, so a disconfirmed run will always show this mismatch;
  worth documenting so future audits do not read it as an error.

**Tensions that did not reach the `-` / `--` threshold but that a reader should know were live —
all resolved in-flight.** Logged here because "no contradictions" would otherwise overstate how
clean the data was.

### Vendor data defects (would have produced false statements if quoted as returned)

1. **`options-structure gex` `regime` = "FULLY_NEGATIVE / All strikes have negative net GEX" is
   factually wrong** — **25 of 50** strikes are positive (42.5 at +451,024; 37 at +108,762).
   Caught by the mandated `per_strike` cross-check in phase 4 §A; the per-strike distribution was
   reported instead of the label. *(propose-only: `lib/uw-json-paths.md` note)*
2. **`historical gex-time-series` `regime` contradicts its own row-level `total_gex` in 7 of 30
   rows** (POSITIVE label on negative `total_gex`); only **4** of 30 sessions actually have
   positive `total_gex` against 10 labelled POSITIVE. **Second, independent confirmation** of
   defect 1. Phase 5 §C used the `total_gex` **sign**.
3. **`stock/peers` returns the wrong peer set for ENPH** — 12 semiconductor-equipment names
   (MKSI, ENTG, ONTO, AMKR, AMAT…), zero solar. Silent failure (exit 0, plausible tickers). Phase
   7b rebuilt the peer set from `fz screen --filter ind_solar`.
4. **`dark-pool price-levels` returns `total_shares` = null** for all 15 rows, and its top-5
   "levels" are simply the **five session closing prices** (closing-auction artifact). Phase 2 §D
   used premium/trade-count and identified the genuine 36.15–36.30 shelf; phase 7 §E later
   recovered the missing share counts from `institutional-accumulation`.

Also: **`options-structure term-skew`/`gex` reference price is 36.08 vs the verified 35.07 close**
(+2.88%) — large enough to have **inverted** the regime read if used naively (spot would sit
*above* the 36–37 flip band). Phase 4 §I computed every distance from the verified close.
**`zero_gamma_level` is null/unusable throughout**, so the flip level came from
`atm_flip_strike`. **`insights signal-confluence` required `--top-n 500`** to surface ENPH at all;
the spec's `--min-score 1` confirmation step alone would have wrongly implied no score.
**`deep-dive` `yahoo_fundamentals` HTTP 401** and **`analyst-vs-flow` returned no analyst leg**.

### Cross-phase reconciliations (metric-definition differences, not disagreements)

5. **`dark_pool.buy_ratio` 0.371 (phase 7) vs 0.390 large-tier vs 0.303 auction-stripped
   (phase 2)** — the composite **includes** the 137,666-share closing-auction cross. All three
   sit on the bear side of the 0.40 threshold, so the classification survives.
6. **`buy_sell_ratio` 0.59 is buy/sell; `buy_ratio` 0.371 is buy/(buy+sell)** — not comparable.
7. **Two different "sector net flow" definitions**: `sector-flow` uses call−put premium (Tech
   **+$223.1M**); `market-regime` uses bullish−bearish (Tech **+$55.96M**). Both positive.
8. **`oi-trend` BUILDING (+201,329) vs total OI −25.4%** — expirations are not booked as
   decreases; ~330k contracts retired at the June/July OPEX.
9. **P/C at the 87.5th self percentile (65 sessions) vs `pc-ratio-zscore` +0.482 NORMAL (20
   sessions)** — different windows on a right-skewed distribution (CV 0.61).

### Corrections made to earlier phases by later ones (all recorded in DATA NOTE blocks)

10. **Phase 0.5's "the event passed with a whimper"** — corrected by phase 1 from OHLC
    (`high` 39.60 → `close` 35.07, **−11.44% from high**, realized range **12.8% ≈ the ±12.25%
    implied**), then **double-sourced** by phase 5 from Finviz (`Gap` **+7.08%**,
    `Change from Open` **−9.82%**).
11. **Phase 6's "Q2 beat / guided above"** — corrected by phase 7c: Benzinga issued
    **"CORRECTION: Q2 Adj. EPS $0.46, Inline"**, and the Q3 guide straddles the **$304.253M**
    consensus. **Q2 was a revenue beat with EPS in line, and the guide is in line.**
12. **Phase 7b's "analyst leg UNMEASURED"** — repaired by phase 7c via `/stock/recommendation`
    (which works where `recommendation-trends` 404s) plus **seven dated broker targets** from the
    news feed.
13. **The prior run's carried framings, both inverted by fresh measurement:** the
    *"positive-gamma island (`today_total_gex` +1,047,168)"* has **flipped to −406,622**, and
    *"structurally armed upside squeeze: net_dex −$40.3M"* was attached to the **wrong Greek** —
    `dex`'s own `interpretation` says dealers short puts **SELL** underlying. The genuine squeeze
    mechanism is **vanna**, and phase 6 then showed its trigger unmet.
14. **The 8,970 written Sept-18 P35 puts: phase 3 §H called them "forced selling," phase 8's
    accumulation-hunter called them "a squeeze on covering."** **Resolved in phase 8b:** a
    delta-hedged short put **sells** on the way down (now) and **buys** at assignment (09-18) —
    different triggers, both true. **Marked resolved; not an open contradiction.**
15. **My own look-ahead filter on the news feed was wrong** (threshold 1785283199 = 07-28 23:59
    UTC, not 07-29 EOD ET), falsely reporting 8 look-ahead items. Recomputed to 1785383999 →
    **0 items after as-of**. **No value was transcribed from the bad filter.**

---

## Citation failures

**None.** Four citations were spot-checked — the three the phase-9 thesis leans on hardest, plus a
fourth chosen because it carries the run's only non-trivial magnitude claim:

| Citation | Claim in phase 9 | Verified against | Result |
|---|---|---|---|
| `[STRUCT:gex]` | `net_gex` negative at **every strike 25→36.5**; `atm_flip_strike` **36** | `phase-4-structure.md` §A ladder table — *"25 → 36.5 (every strike) → NEGATIVE, without exception"*; §G `atm_flip_strike` **36** | ✓ **exact** |
| `[SENT:short_float fz semi-monthly]` | **17.94%** of float, **up from 17.55%** | `phase-7c-sentiment.md` §D — *"17.94% of float [fz, semi-monthly, ~2wk lag; up from 17.55%]"* | ✓ **exact** |
| `[DEBATE:disconfirmation]` | `bear_residual` **0.75** ≥ `bull_residual` **0.65** → `disconfirmed` **true** | `phase-8b-debate.md` verdict block — `bull_residual: 0.65`, `bear_residual: 0.75`, `disconfirmed: true` | ✓ **exact** |
| `[OI:biggest_increases]` | **$2,837,716** at **92% ask-side** | `phase-3-positioning.md` §C — `prev_total_premium` **2,837,716**; `prev_ask_volume` 2,908 / (2,908 + 253) = **92.0%** (recomputed) | ✓ **exact, incl. the derived %** |

---

## Sanity checks

| Check | Result |
|---|---|
| All `phase-*.md` present, incl. **0.5 / 7b / 7c / 8b** | ✓ **13 phase MDs + `phase-9-trade-plan.md` + `decision.json` = 15 artifacts** |
| Phase 9 cites ≥ 3 distinct upstream datapoints | ✓ **15 citations** spanning FLOW / DP / OI / STRUCT / HIST / MACRO / INSIGHT / FUND / SENT / CTX / DEBATE / AGENT |
| Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} | ✓ **0.55** |
| ≥ 1 `directional` + ≥ 1 `defined_risk` structure | ✓ Aug-21 **35/30 put debit spread** (`directional`, triggered-only) + Aug-21 **37/40 bear call spread** (`defined_risk`) |
| Sizing math shown | ✓ p 0.55 · b 2.333 · `raw_kelly` 0.3571 · Kelly 5.0% → sizing-map ceiling 2.5% → gates → **0.0%** |
| Kelly `p` = phase-5 win-rate **or a justified bin fallback** | ✓ **justified fallback.** `p_raw` 1.00 recorded, then **discarded** on four cumulative grounds (self-disclaimed in-sample; N=9 < 10 floor; market-wide with **ENPH absent from the sample**; all 9 signals from 2 dates) per phase-5's own recommendation and `[AGENT:risk-monitor]`'s explicit ruling. Fallback to the conviction bin, capped at 0.65; bin 0.55 binds |
| **All five** risk gates evaluated in the sizing block | ✓ 1 fundamentals **CAUTION** · 2 sentiment **VETO** · 3 correlation **none** (single blueprint) · 4 rotation **adverse** · 5 debate **disconfirmed** — each shown with its effect |
| Phase-0.5 `unusual_verdict` reflected in sizing | ✓ **BUSY_NAME_NORMAL_DAY** applied as the context modifier ("do not size at the top of the band") and as the phase-1/2 `+` cap in this scorecard |
| Structures sized to the front-expiry expected move | ✓ `expected_move` **±5.58% / ±$1.96**; Structure A breakeven **33.14 = −5.5%**, deliberately inside the priced range; both structures priced off **real EOD NBBO**, not modelled |
| `decision.json` exists and passes `validate_decision.py` | ✓ **`OK: research/ENPH/2026-07-29/decision.json is a valid DeepDiveDecision`** (re-validated after this phase's backfill) |
| `context` / `expected_move` / `gates.sentiment` populated | ✓ all three present |
| Look-ahead discipline on dated series | ✓ earnings `period`, insider `year`/`month`, news `datetime`, recommendation `period` — all filtered to ≤ as-of and verified to drop nothing; `financials-reported` deliberately used **2026Q1** because the Q2 10-Q post-dates the as-of |
| Immutability (no overwritten phase MD) | ✓ fresh `2026-07-29` directory, all v1 filenames |
| Every number traceable to a `jq`/SQL path in a `## Tool calls` row | ✓ spot-checked across phases 1–7c; two derived families (`net_flow`, signed delta notional) carry inline formulas and `net_flow` was cross-validated **four** ways |

**No sanity-check failures.**

---

## `decision.json` backfill

```
confluence_score:  null  →  62
recommended_bin:   null  →  0.65
paths.audit:       null  →  "phase-10-audit.md"
```

Re-validated after writing: **`OK: research/ENPH/2026-07-29/decision.json is a valid
DeepDiveDecision`**.

Note that `recommended_bin` **0.65** intentionally differs from the envelope's `conviction`
**0.55**. That is not an inconsistency to fix — it is the record of gate 5's mandatory bin
down-shift, and preserving both lets `/deep-dive-calibration` later test whether the confluence
band or the post-gate bin is the better-calibrated predictor. **Deliberately left divergent.**

---

## Final auditor note

**The run is internally consistent, fully sourced, and ready to act on — where "act" means
*wait*.** Eight signal phases and a five-agent desk all read the SHORT direction the same way,
with **no phase contradicting it**; the confluence score of **62** and the **0.0% final size** are
driven not by conflicting evidence but by two one-sided gates (7c **VETO**, 8b **disconfirmed**)
plus the magnitude and entry facts the score does not capture — **`net_flow` 5.8× below the
bearish top-50 cutoff, `signal-confluence` 3/6 in the bottom bucket of 500, `confidence_pct` 24,
`ATR` 9.2% of spot against a 5.58% implied move, and the 30-day low set on the session itself.**

**No revision to phase 9 is requested.** Its one-bin conservatism versus the confluence band is
the correct application of sizing-rubric gate 5, its Kelly `p` substitution is justified and
documented rather than silently swapped, its two structures are priced off real end-of-day NBBO
with a stated liquidity caveat on the illiquid leg, and its invalidation is genuinely falsifiable
in all three categories — including two non-price conditions (a VIX reversal re-arming the vanna
bid; the 09-18 assignment bid) that no single upstream phase owned. The one thing I would watch in
calibration is whether **62 / 0.65 or the published 0.55** better predicts the outcome, since this
run is a clean test case: **right direction, deliberately no position.**

---

*For research and educational use only. Not financial advice.*
