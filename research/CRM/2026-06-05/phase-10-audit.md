# Phase 10 — Audit & Confidence Score

**Ticker:** CRM
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T18:00:00-04:00
**Dominant bias audited:** SHORT (from phase-9-trade-plan.md)

## Summary

Confluence score **54/100** (base 64 − 5 debate − 5 sentiment) → recommended
bin **0.65**; phase-9's actual bin is **0.55** — a one-bin conservative
MISMATCH that is the *documented* phase-8b down-shift (sizing rubric §Risk
gates instructs the bin cut on `disconfirmed=true`), not an error.
**Contradiction count: 1 hard** (phase-7b fundamental VETO, scored `--`) plus
one neutral axis (phase-7). All 15 expected artifacts present; all 3
spot-checked citations resolve; `decision.json` backfilled
(confluence_score 54, recommended_bin 0.65) and re-validated `OK`. A score of
54 means: barely-positive confluence for a short whose only sanctioned
expression is watch-only + trigger-conditional defined-risk carry — the run
is internally consistent precisely *because* it sized to almost nothing.

## Confluence scorecard

| Phase | Score | Justification (quote a datapoint) |
|-------|-------|-----------------------------------|
| 0.5 — context (modifier) | cap@`+` on 1–2 | "BUSY_NAME_NORMAL_DAY — total premium 98.0 universe pctile but self-history total premium 33.3rd pctile [CTX:self_pctile DUCKDB]" |
| 1 — flow | + (capped) | "Bearish sweep persistence 5/5 sessions, $211.13M, consistency 1.0 [FLOW:sweep_persistence]" supports the short; whole-tape is flat (net +$1.28M, customer Δ ≈ −$7M [FLOW:aggressor_ex0dte DUCKDB]) so `+`, and the 0.5 cap binds anyway |
| 2 — dark pool | + (capped) | "DP $ volume peaked at the 197–211 highs ($931.9M 6/01) and collapsed to $249.0M by 6/05 [DP:price_path DUCKDB]" — distribution-into-strength + overhead shelves; today balanced (large-tier 0.489) keeps it at `+` |
| 3 — OI | + | "All 6 OI builds ≥500 are OTM calls, 5/6 inferred SOLD [OI:smart_positioning]" — supply ceiling supports the short; the 185/180 put floor is the two-sided counterweight |
| 4 — structure | + | "Regime FULLY_NEGATIVE, −$13.34M GEX at 185, dealer hedge = SELL [STRUCT:gex][STRUCT:dex]" — strong path agreement, held to `+` because max-pain 190/192.5 pulls the other way [STRUCT:max_pain] |
| 5 — historical | + | "bearish_flow win_rate 87.5% (n=8, avg −2.73%) [HIST:signal_backtest]; GEX decayed +50.4M→−3.3M into the flip [HIST:gex_time_series]" — agrees, but small-N and the negative VRP is structure-guidance, not direction |
| 6 — macro | ++ | "Technology −$807.6M = biggest sector outflow; regime TRANSITIONAL; AVGO −$280B shock unresolved [MACRO:MarketRegime_2026-06-05 UW]" — the cleanest alignment in the run |
| 7 — insights | 0 | "conviction_matrix MIXED at 3.7% confidence; CRM absent both signal-confluence boards; institutional_accumulation NEUTRAL [INSIGHT:*]" — genuinely neutral, scored as such |
| 7b — fundamentals | −− (**VETO**) | "fundamental_signal BULLISH, 2 contradictions: beats +3.7%→+12.6%→+23.9% accelerating, rev +10.98%/EPS +35.08% with margins expanding [FUND:earnings_surprises][FUND:metric]" — **the directional thesis is fundamentally vetoed**; phase-9 correctly went watch-only |
| 8 — agents | +2 net | sweep-tracker SHORT (+2), risk-monitor SHORT (+2), contrarian-scanner LONG (−2), accumulation-hunter NEUTRAL (0), earnings-scout skipped by design (0) |

**Raw score (symmetric):** 7+7+7+7+7+15+0−15+2 = **37** (range −130…+130)
**Base score:** round((37+130)/260×100) = **64/100**
**Debate penalty (phase-8b):** −5 (disconfirmed: bull_residual 0.55 vs bear_residual 0.55)
**Sentiment penalty (phase-7c):** −5 (CAUTION, crowd_state CROWDED_SHORT)
**Confluence_score:** **54/100**
**Recommended bin:** **0.65** (band 50–64)
**Phase-9 actual bin:** **0.55** → **MISMATCH (conservative)** — phase-9
documented the deviation under "Why this bin": the sizing rubric's debate gate
mandates a one-bin down-shift on `disconfirmed=true`, stacking with the score
penalty by design. A downward deviation is always permitted; no action needed.

## Contradictions

- **phase-7b (fundamentals): `--`** — the short presses an improving business
  (3/3 accelerating beats, rev +10.98%, EPS +35.08%, margins expanding, zero
  open-market insider selling, $25B ASR) — *resolution applied:* directional
  size vetoed to watch-only/0% (done in phase-9), invalidation tightened to
  two closes >190 / single close >195, structures restricted to
  defined-risk-carry published as candidates only. Nothing further required.
- *(Noted, not scored)* **phase-4 internal tension** — short-gamma
  amplification below 185 vs max-pain magnet 190–192.5 above spot: phase-9
  resolved it correctly by making every entry trigger-conditional on which
  side of the 185–190 box breaks (the debate's shared geometry).
- *(Noted, not scored)* **phase-7c divergence #1** — institutional option lots
  net bullish (+$4.4M call-buy/put-sell tilt [SENT:retail_split DUCKDB])
  against the 5/5 bearish sweep tape; carried into phase-9's key_risks via the
  8b strongest_bear_point. Consistent treatment.

## Citation failures

None. Spot-checked 3 of phase-9's thesis citations:
1. `[FLOW:sweep_persistence]` "$211.13M, 5/5, consistency 1.0" → resolves to
   phase-1-flow.md §Sweeps ("dominant_direction `bearish`, 5/5
   sessions_in_top, consistency_score 1.0, $211.13M") ✓
2. `[STRUCT:gex]` "−$13.34M at the 185 strike, total −3,333,998" → resolves to
   phase-4-structure.md §GEX table (strike 185 = −13,339,085; total
   −3,333,998) ✓
3. `[MACRO:MarketRegime_2026-06-05 UW]` "Technology −$807.6M biggest
   directional outflow, TRANSITIONAL" → resolves to phase-6-macro.md §Market
   regime (sector_rotation money_flowing_out Technology −807,616,415.5) ✓

## Sanity checks

- ✓ All phase files present: 0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9 +
  decision.json (15 artifacts; `ls` verified)
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (6 in the citations summary,
  spanning phases 1, 2, 4, 5, 6, 7b/7c)
- ✓ Conviction bin 0.55 ∈ {0.55, 0.65, 0.75, 0.85, 0.95}
- ✓ ≥1 directional (Jul-17 180/170 put debit spread) + ≥1 defined-risk (Jun-18
  195/200 call credit spread) — both marked carry-only under the VETO
- ✓ Sizing math shown: p_raw 0.875 → N-cap (n=8<10) → p 0.75; b 1.51; raw
  Kelly 0.584; ¼-Kelly capped 5.0%; Kelly p sourced from phase-5 backtest
  (win_rate_source=backtest), not the bin
- ✓ All five risk gates evaluated in phase-9's sizing block: fundamentals
  VETO (fired), sentiment CAUTION (fired), correlation cluster CRM/NOW 0.863 /
  CRM/PATH 0.820 (fired), sector rotation aligned (no cut), debate
  disconfirmed (fired); phase-0.5 BUSY_NAME_NORMAL_DAY reflected (no
  top-of-band)
- ✓ Structures sized to the expected move: `expected_move` block in JSON
  (0.56% / $1.04 front-expiry + 6/12 ATM IV 51.7% noted); spread widths target
  the 176.17 gap-fill without capping before it
- ✓ `decision.json` exists, backfilled (confluence_score 54, recommended_bin
  0.65, paths.audit set) and `validate_decision.py` prints `OK` — including
  the VETO⇒final_size_pct==0 consistency rule (caught and fixed during
  phase-9: initial 0.5% carry size corrected to 0.0 watch-only)
- ✓ Look-ahead discipline: as-of = latest available date (no trailing-anchor
  drift); fz live reads (breadth 6/06, Finnhub TTM ratios) flagged as
  advisory/post-as-of where they appeared

## Final auditor note

The run is internally consistent and ready for action **as filed**: a SHORT
bias whose every gate fired, correctly resolved into watch-only directional
(0%), two trigger-conditional defined-risk carry candidates, and falsifiable
invalidations on both sides of the 183.70–190 box — the conservative 0.55 bin
versus the recommended 0.65 reflects the documented debate down-shift, not
drift. Do not deploy either structure until the 185-break or 190-rejection
trigger actually prints; if it prints, this audit recommends a fresh phase-1/4
refresh first (sweep persistence + GEX regime), since the entire short edge is
mechanical and two of its inputs (sweep streak, FULLY_NEGATIVE gamma) can flip
in a single session.
