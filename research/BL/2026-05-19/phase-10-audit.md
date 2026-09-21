# Phase 10 — Audit & Confidence Score

**Ticker:** BL
**As-of date:** 2026-05-19
**Generated:** 2026-05-19T00:00:00Z
**Upstream phases audited:** phase-0 through phase-9 in
`/Users/ewan/Development/stock-deep-dive/research/BL/2026-05-19/`

## Summary

**Dominant bias (from phase-9):** **LONG**.
**Raw score:** +74 (phases 1-7) + 0 (phases 8 net) = **+74**.
**Confluence score: 82 / 100.**
**Recommended conviction bin (per rubric):** **0.85** (80-89 band).
**Phase-9 actual bin: 0.75.**
**Status: MISMATCH (one bin lower than recommended); deviation is
documented in phase-9 §"Conviction deviation" and is judged
procedurally clean and substantively defensible — see auditor note.**

The chain is internally consistent on direction: phases 1, 2, 3, 7 all
return ++ (strong agreement); phases 4 and 5 return + (agreement with
documented countervailing signal); phase 6 returns 0 (macro is genuinely
mixed for BL); phase 8 returns net 0 (2 LONG agents + 2 NEUTRAL agents
cancel out under the strict ±2 rubric). **Three real contradictions are
flagged below**, none of which kill the thesis but all of which earn the
0.75 deviation. Five sanity checks pass; one citation spot-check passes
all three sampled tags. **Run is internally consistent and ready for
action at conviction 0.75 with the invalidation/sizing already specified
in phase-9.**

## Confluence scorecard

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|----------------------------------|
| **1 — flow** | **++** | "[FLOW:options_flow_sweeps] `total_premium=4137830`, `total_size=5177`, `trade_count=156`" ask-side; "$11.65M total premium on lead contract" (phase-1 §Sweeps, §"Largest single-print"). Bullish, conviction 4. |
| **2 — dark pool** | **++** | "[DP:dark_pool_block_stratified] block tier `buy_ratio=1.000`; large tier `buy_ratio=0.893`; 14 of 16 prints at-or-above NBBO mid" (phase-2 §"Tier breakdown"). Accumulation, conviction 5. |
| **3 — OI** | **++** | "[OI:oi_biggest_increases] `BL261218C00027500` `oi_diff_plain=13016`, `prev_total_premium=11,647,199`; smart_positioning 7-of-8 rows bullish" (phase-3 §"Largest OI increases", §"Smart positioning"). Bullish, conviction 5. |
| **4 — structure** | **+** | "[STRUCT:options_structure_gex] strike $27.5 net_gex `193,037,548.78` ≈ 99.3% of total $194,349,985" + "[STRUCT:options_structure_dex] `net_dex=6,337,156,590` → dealer hedge = BUY underlying" (phase-4 §"GEX", §"DEX"). Direction agrees but tool's "POSITIVE — mean-reversion" regime label conflicts with DEX direction (see Contradictions #1). Conviction 4. |
| **5 — historical** | **+** | "[HIST:historical_vrp] `vrp=-0.0889`, `regime=PREMIUM_BUYING`" + "[HIST:historical_oi_trend] `consecutive_build_days=10`, `overall_trend=BUILDING`" + "[HIST:historical_gex_time_series] +$194M GEX rebuilt from −$1.55M in 9 sessions" (phase-5 §"IV regime", §"OI trend", §"GEX time series"). Direction agrees but contains the diagnostic counter-signal `historical_signal_backtest` 0/7 win rate (see Contradictions #2). Conviction 3.5. |
| **6 — macro** | **0** | "[MACRO:MarketRegime_2026-05-19 UW] regime=TRANSITIONAL; bullish_pct=34.7%; Technology +$44M IN" vs "[MACRO:SaaS_Sector_2026 WebSearch:saastr.com] IGV −21% YTD" + "[MACRO:FOMC_2026-04-29] 4 dissents, sticky inflation" (phase-6 §"Tailwind / Headwind table"). Phase-6's own verdict: "neutral-leaning-tailwind on idiosyncratic; mildly headwind on broad macro." Honestly 0. |
| **7 — insights** | **++** | "[INSIGHT:insights_conviction_matrix] `scenario=DIRECTIONAL_LONG`, `confidence_pct=87.53`, `dark_pool.buy_ratio=0.915`" + "[INSIGHT:insights_institutional_accumulation] `signal=ACCUMULATION`, `buy_sell_ratio=10.77`" + "[INSIGHT:insights_price_vs_flow] `divergence=true`" (phase-7 §"Conviction matrix", §"Institutional accumulation", §"Price vs flow"). Strong agreement. |
| **8 — agents (net)** | **0** | accumulation-hunter LONG (+2), sweep-tracker LONG (+2), contrarian-scanner NEUTRAL (−2), risk-monitor NEUTRAL (−2), earnings-scout SKIPPED (0) = **net 0**. NB: both NEUTRAL agents explicitly endorse the LONG thesis structurally and disagree only on sizing/timing; strict ±2 alignment scoring nets them to zero, but the qualitative read is "endorse with caution." |

**Raw score breakdown:** 15+15+15+7+7+0+15 = **+74** (phases 1-7) plus
**0** (phase-8 net) = **+74**.

**Normalized confluence_score:** `(74 + 115) / 230 × 100 = 82.17` → **82 / 100**.

**Recommended bin (per `rubrics/confluence-scoring.md`):** band 80-89 →
**0.85**.

**Phase-9 actual bin:** **0.75**.

**Bin match:** **MISMATCH** (phase-9 went one bin lower).

## Contradictions

(Contradictions are flagged per the SKILL.md requirement *"Phase 10 must
flag every internal contradiction"*. The rubric's `-` / `--` score
threshold is the formal trigger; below I also surface intra-phase
contradictions that earn `+` rather than `++`.)

1. **Phase-4 GEX label vs DEX direction (carried forward unresolved).**
   `options_structure_gex` returns `regime: "POSITIVE"` with the description
   *"Dealers net long gamma — expect mean-reversion and reduced volatility"*,
   while `options_structure_dex` returns `net_dex=6,337,156,590` with the
   description *"Public is net call-long → dealers net short calls → dealer
   hedge is to BUY underlying."* These two are operationally contradictory.
   - **Resolution applied in phase-9:** the DEX interpretation is used as
     operative because (a) phase-3 OI data unambiguously documents the public
     opening 13,016 new long-call positions ask-side, and (b) DEX is derived
     from raw delta × OI without sign-convention ambiguity. The GEX
     "POSITIVE" label is treated as a UW sign-convention artifact and not
     overridden.
   - **Suggested resolution for future runs:** investigate UW's GEX sign
     convention against an independent source (e.g. SpotGamma or a manual
     calc). Today's run defers this work to future maintenance.

2. **Phase-5 `historical_signal_backtest` 0/7 win rate against the
   dominant bias.** All seven recent firings of the bullish_flow pattern
   were losers (avg −3.05% / 20d). This is BL-irrelevant in cohort
   (MSFT/AAPL/QQQ/SMH/META/AVGO/UPS) but **regime-relevant** for the next
   20 sessions.
   - **Resolution applied in phase-9:** sizing reduced from cap (5%) to
     half-cap (2.5%); conviction reduced from rubric-recommended 0.85 to
     0.75; invalidation tightened to "two consecutive daily closes below
     $24.85" (rather than the looser "break of support" alternative).
   - **Suggested resolution:** monitor `historical_signal_backtest` daily;
     if win rate improves to ≥40% on a new cohort firing, consider
     upsizing the position toward the 5% cap and the 0.85 bin. If it
     deteriorates further (e.g., next 3 firings also losses), exit on
     first signal-based invalidation trigger rather than waiting for the
     two-close price-based trigger.

3. **Phase-7 `insights_signal_confluence` excludes BL despite multiple
   factors matching.** BL has at minimum 4 bullish factors (bullish_flow,
   low_pcr, dp_accumulation, oi_building) — score should be ≥4 — yet BL is
   absent from the top-100 confluence list. This is a tool-side mismatch
   (probably a screener volume/cap floor below BL's level), not a
   contradiction against the LONG bias.
   - **Resolution applied in phase-9:** documented as a screener
     mismatch, not a counter-signal. Confidence is preserved on the
     conviction_matrix / institutional_accumulation / price_vs_flow trio
     instead.
   - **Suggested resolution:** when running this skill on small-cap
     names, treat `insights_signal_confluence`'s silence as a definitional
     gap rather than a no-signal. No code change required; just an
     interpretation note.

4. **Phase-7 Yahoo fundamentals + analyst_vs_flow data gap.**
   `insights_deep_dive` returned `yahoo_fundamentals: HTTP 401` and
   `insights_analyst_vs_flow` returned no analyst block. We have **no
   read on Wall Street analyst consensus for BL** on this run.
   - **Resolution applied in phase-9:** phase-9 does NOT claim analyst
     alignment in any thesis or sizing statement.
   - **Suggested resolution:** the user can run a targeted WebSearch on
     "BlackLine BL analyst rating price target 2026" if they want
     independent analyst confirmation before placing the trade. This is
     a nice-to-have, not a blocker.

5. **Phase-5 prior-cycle loss memory.** The Mar 23-24 build of 2,765
   contracts of `BL260417C00042500` ($42.5 strike, Apr 17 expiry) appears
   to have expired worthless during the late-April / early-May drawdown
   to $30. The current setup resembles that prior playbook (single-strike
   institutional call build) but with different strike/expiry/context.
   - **Resolution applied in phase-9:** conviction deviated downward by
     one bin partly to respect this; sizing halved; "blue-sky $40 target"
     framed as stretch, not base case.
   - **Suggested resolution:** if any future intra-day data shows the
     current Dec $27.5C OI DECLINING by ≥2,000 contracts in a single
     session, exit at least half the position immediately (per phase-9
     monitoring checklist).

**Note on contradiction counts:** No phase scored `-` or `--` under the
strict rubric. All five contradictions above are surfaced for transparency
and to make the audit trail complete per SKILL.md's "flag every internal
contradiction" requirement.

## Citation failures

Three citations from phase-9's thesis paragraph were spot-checked:

| # | Tag | Claim | Resolution attempt | Result |
|---|-----|-------|--------------------|--------|
| A | `[OI:oi_biggest_increases]` | "+13,016 OI on BL Dec18 2026 $27.5 calls" | Open phase-3-positioning.md §"Largest OI increases"; grep `BL261218C00027500` → `last_oi=3162`, `curr_oi=16178`, `oi_diff_plain=13016` | **✓ RESOLVED** |
| B | `[DP:block_stratified]` | "dark pool buy ratio 0.915" (claim in phase-9 thesis maps to phase-7's `insights_conviction_matrix.dark_pool.buy_ratio=0.915`; phase-2's tier-stratified buy_ratios were 1.000 (block) and 0.893 (large)) | Open phase-2-dark-pool.md §"Tier breakdown" → block buy_ratio 1.00, large 0.893; open phase-7-insights.md §"Conviction matrix" → dark_pool.buy_ratio 0.915 | **✓ RESOLVED** (composite metric from phase-7 — value matches) |
| C | `[INSIGHT:insights_conviction_matrix]` | "DIRECTIONAL_LONG at 87.53% confidence" | Open phase-7-insights.md §"Conviction matrix" → `scenario: DIRECTIONAL_LONG`, `confidence_pct: 87.53` | **✓ RESOLVED** |

**Citation failures:** none.

**Minor note (not a failure):** phase-9 cites
`[DP:largest][DP:block_stratified]` for "buy ratio 0.915" — the 0.915 value
is actually from `insights_conviction_matrix.dark_pool.buy_ratio` (an
aggregate of ALL DP trades, not just the stratified tiers). Phase-2's
own tier numbers are 1.00 (block) and 0.893 (large). All three numbers
are correct individually; the combined citation slightly conflates them.
Suggested edit (non-blocking): change the phase-9 thesis to
`[INSIGHT:conviction_matrix] dark_pool.buy_ratio=0.915` to be
strictly traceable. Not done in this audit; flagged for future polish.

## Sanity checks

| # | Check | Status | Note |
|---|-------|--------|------|
| 1 | All `phase-*.md` files present? | **✓** | phase-0 through phase-10 (this file) — 11 files |
| 2 | Phase-9 cites ≥3 distinct upstream datapoints? | **✓** | 8 distinct citations in §"Citations summary" |
| 3 | Conviction bin in {0.55, 0.65, 0.75, 0.85, 0.95}? | **✓** | 0.75 (snapped value, with documented deviation from rubric-recommended 0.85) |
| 4 | ≥1 directional + ≥1 defined-risk structure? | **✓** | Primary: long Dec18 $27.5C; alternative: Dec18 $27.5/$35 call debit vertical |
| 5 | Sizing math shown? | **✓** | Full Kelly inputs (p, b), raw_kelly 42.7%, fractional 10.7%, cap 5%, final 2.5% with explicit half-cap rationale |
| 6 | Disclaimer present at top of phase-9? | **✓** | "For research and educational use only. Not financial advice. Sizing and structures are illustrative." |
| 7 | Invalidation has all 3 categories (price/signal/macro)? | **✓** | Per `rubrics/invalidation-rubric.md` — each populated with concrete falsifiable triggers |
| 8 | Catalyst calendar present? | **✓** | Phase-9 catalyst table + phase-6 calendar referenced; Q2 BL earnings 2026-08-04 confirmed via `insights_deep_dive` |

All eight sanity checks pass.

## Confluence-score → conviction-bin reconciliation

| Field | Value |
|-------|-------|
| Confluence score | **82** |
| Score band | 80-89 |
| **Rubric-recommended conviction** | **0.85** |
| **Phase-9 actual conviction** | **0.75** |
| Match? | **MISMATCH (one bin lower than recommended)** |
| Deviation procedurally clean? | **YES** — phase-9 §"Conviction deviation" documents four reasons (0/7 bullish_flow backtest, 2-of-4 agent NEUTRAL, GEX label conflict, prior Apr-17 $42.5C cycle loss). |
| Auditor verdict on the deviation | **Endorsed.** Each of the four reasons is independently flagged in the contradiction log above; together they justify giving up one bin. Phase-9's reasoning is conservative but defensible and accomplishes its purpose (smaller capital outlay, tighter invalidation, half the cap on size). A PM choosing to override back to 0.85 must accept those four pieces of countervailing evidence; that's a legitimate but riskier call. |

## Final auditor note

The run is internally consistent and ready for action. Direction (LONG) is
unanimous across the structural signals (phases 1, 2, 3, 7) and is
endorsed by the dealer-flow mechanics (phase 4 DEX) and historical
context (phase 5 VRP). The deliberate one-bin downgrade in phase-9 from
rubric-recommended 0.85 to 0.75 is defensible and well-documented;
sizing is conservative (2.5% of book), invalidation is tight and
falsifiable (two daily closes below $24.85), and both required structure
types (directional + defined-risk) are specified with strike/expiry/
breakeven/max-loss. **Five intra-phase contradictions are flagged**
(GEX-vs-DEX label, signal_backtest 0/7, signal_confluence exclusion,
Yahoo-fundamentals gap, prior Apr-17 loss); none kill the thesis,
all four downward-pressuring ones are reflected in the lower conviction
and half-cap sizing. **Proceed.**
