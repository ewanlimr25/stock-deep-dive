# Phase 10 — Audit & Confidence Score

**Ticker:** DOCN
**As-of date:** 2026-07-17
**Generated:** 2026-07-20T03:45:00Z
**Dominant bias audited:** RANGE (bearish-leaning, non-directional — phase-9)

## Summary

**Confluence score 68/100 → recommended bin 0.75; phase-9 holds 0.55** (a
documented, conservative **downward** deviation). The run is **internally
consistent** — the eight signal phases plus the five-agent desk near-unanimously
describe the *same* animal: a −34% fallen name, pinned in a long-gamma range, with
rich sell-able vol and **no directional edge** — which is exactly the RANGE thesis.
The one strong contradiction is the **phase-7b fundamentals VETO** (a fundamental
veto of any directional long), which the plan correctly honors by taking directional
size to **0%** and recommending only a defined-risk, bearish-lean, pre-earnings
premium-selling carry. **1 hard contradiction (7b), 0 citation failures, all sanity
checks pass.** Ready for action as a low-conviction, defined-risk range trade.

## Confluence scorecard

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|----------------------------------|
| 1 — flow | **+** | Two-sided/hedging tape, net only +$154K, `BUSY_NAME_NORMAL_DAY` → no directional edge, supports RANGE (flow-phase cap `+` applied) [FLOW:insights_deep_dive] |
| 2 — dark pool | **+** | Block buy 0.501 / large buy 0.468, "balanced — no clear bias," DOCN not in DP top-30 → non-directional, supports RANGE (cap `+`) [DP:block_stratified] |
| 3 — OI | **+** | No fresh build (max +206); walls $128 call / $115 put *define* the range [OI:oi_by_strike] |
| 4 — structure | **++** | Long-gamma (ZGL $70.14 ≪ spot) + max-pain pin **$120** — the core range mechanic [STRUCT:gex][STRUCT:max_pain] |
| 5 — historical | **++** | **VRP +0.434 PREMIUM_SELLING** + bullish_flow win-rate **14.3%** → sell rich vol, don't go long [HIST:vrp][HIST:signal_backtest] |
| 6 — macro | **+** | Regime TRANSITIONAL/CHOPPY, guidance "iron condors in range" → defined-risk range [MACRO:MarketRegime] |
| 7 — insights | **+** | MIXED / conf 1%, absent from both bull & bear confluence → non-directional [INSIGHT:conviction_matrix] |
| 7b — fundamentals | **--** | **VETO** — forward EPS guided ~50% lower + insider selling (MSPR −98.9/−77.8); **fundamentally vetoes any directional long** [FUND:tier_adjustment] |
| 8 — agents | **+ (5/5 align)** | 3 RANGE + 2 NEUTRAL, 0 directional → +2 each = **+10**; unanimous non-directional [AGENT] |

**Raw score (symmetric):** phases 1–7b = 7+7+7+15+15+7+7−15 = **50**; phase-8 = **+10** → **raw 60**
**Base score:** round((60 + 130) / 260 × 100) = **73/100**
**Debate penalty (phase-8b):** disconfirmed = **false** (bull_res 0.72 vs bear_res 0.62) → **−0**
**Sentiment penalty (phase-7c):** tier_adjustment **CAUTION** → **−5**
**Confluence_score:** 73 − 5 = **68/100**
**Recommended bin:** **0.75** (band 65–79)
**Phase-9 actual bin:** **0.55** → **MISMATCH (intentional downward deviation)**

### Note on the score↔conviction mismatch

The confluence rubric is built for *directional* theses; on a **non-directional
RANGE** thesis a high score means "the data strongly agrees it's a range," which is
**not** the same as "size it up." Phase-9's `## Conviction deviation` explains the
0.75→0.55 downshift: the directional expression is VETO'd to 0% (7b), bullish Kelly
is negative (p 0.143), 7c is CAUTION, and context is `BUSY_NAME_NORMAL_DAY`. A
downward deviation is always permitted (the conservative direction) and is the
correct call here. **No action required** — the plan is appropriately conservative.

## Contradictions

- **phase-7b (fundamentals): VETO.** Forward EPS guided ~50% lower into a still-rich
  PE 58.7, and insiders sold hard (MSPR −98.9/−77.8) — a hard fundamental veto of any
  directional long. **Resolution: already applied** — directional size = 0%
  (watch-only), premium-selling defined-risk carry only, conviction floored at 0.55.
  This is the single `--` phase; it *reinforces* the no-long/bearish-lean rather than
  fighting the RANGE thesis, but is scored `--` per the hard VETO rule.

(No other phase scored `-` or `--`. Phases 1–7/8 are all confirming or neutral toward
the RANGE read.)

## Citation failures

Spot-checked 3 (of 6) phase-9 thesis citations — **all resolve:**
1. `[HIST:trend]` −34% ($180.50→$118.91) → phase-5 §Price+IV trajectory table ✓
2. `[STRUCT:max_pain]` magnet **$120** (7/24 & 8/7) → phase-4 §Max pain table ✓
3. `[HIST:signal_backtest]` bullish_flow **0.143 (n=7)** → phase-5 §Signal backtest ✓
(Also verified: `[OI:decrease_with_volume]` 180C Nov −430 → phase-3 ✓;
`[FUND:tier_adjustment]` VETO → phase-7b ✓.) **0 failures.**

## Sanity checks

- [✓] All phase files present (0, 0.5, 1–7, 7b, 7c, 8, 8b, 9) + `decision.json`.
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (6 cited).
- [✓] Conviction bin ∈ {0.55…0.95} → 0.55.
- [✓] ≥1 directional (put debit spread, watch-only) + ≥1 defined-risk (bear call spread) structure.
- [✓] Sizing math shown; Kelly `p` = phase-5 win-rate **0.143** (n=7, backtest), not the bin.
- [✓] All **five** risk gates evaluated: fundamentals **VETO**, sentiment **CAUTION**,
  correlation **none**, rotation **neutral**, debate **not-disconfirmed**.
- [✓] Phase-0.5 `unusual_verdict = BUSY_NAME_NORMAL_DAY` reflected in sizing (no top-of-band; directional 0%).
- [✓] Structures sized to front-expiry expected move ±1.80% / $2.14; `expected_move` in JSON; primary structure expires 7/31 to avoid the 8/4 binary.
- [✓] `decision.json` exists and **passes `validate_decision.py`** (incl. `context`, `expected_move`, `gates.sentiment`); confluence_score 68 + recommended_bin 0.75 backfilled.

## Final auditor note

The run is **internally consistent and ready for action** as a low-conviction,
defined-risk range trade: nine phases and five agents independently converge on
"rich-vol, long-gamma, no directional edge," and the one dissenting axis (the 7b
fundamental VETO) is correctly absorbed by taking directional size to 0% and
capping the discretionary premium-selling carry at a starter. No phase-9 revision is
required — the 0.55 bin (vs the mechanical 0.75) is a justified, conservative
downward deviation appropriate to a VETO'd, non-directional thesis.
