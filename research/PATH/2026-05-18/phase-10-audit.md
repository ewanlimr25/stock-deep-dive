# Phase 10 — Audit & Confidence Score

**Ticker:** PATH
**As-of date:** 2026-05-18 (data: 2026-05-15)
**Generated:** 2026-05-18T02:30:00-04:00
**Upstream phases audited:** phase-0 through phase-9 (all present)

## Summary

The PATH deep-dive run is **internally consistent and ready for action,
with three material contradictions logged**. Confluence score
**63/100** (mixed-positive); the recommended conviction bin (0.65)
exactly matches phase-9's actual bin (0.65). The dominant bias —
**LONG (defined-risk only) with VOL-FADE overlay** — is supported by 4
of 7 numbered phases at strong-positive level (phases 1, 3, 4 = `++`;
phase 2 = `+`) and challenged by 3 phases (phase 5 = `-`, phase 6 =
`--`, phase 7 = `-`). The agent desk contributes a net **+6** (4 of 5
agents align with the LONG + defined-risk + vol-fade trade
expression). All 3 spot-checked citations resolve correctly. **No
critical sanity-check failures.** The audit's instruction to the desk:
**execute the plan as written but maintain extra-tight invalidation
discipline at the SNOW 2026-05-27 AMC peer print** — that single
event has authority to flip three of the four "support" phases at once.

## Confluence scorecard

| Phase | Score | Justification (quote a datapoint) |
|---|---|---|
| 1 — flow | **++** | "PATH 5-of-5 session bullish sweep persistence, $7.77M cumulative" [FLOW:hot_chains_sweep_persistence] — the strongest single-name conviction signal in the dataset; supplemented by 2027-01-15 $12C ask-side sweep $693k / 3,742 contracts. |
| 2 — dark pool | **+** | "Total $23.30M large-tier premium, buy_ratio 0.586, top-25 prints tilt ~0.74 buy" [DP:block_stratified][DP:largest] — suggestive accumulation, on the boundary between `+` and `0` because 0.586 is below the 0.60 high-confidence threshold; lifted to `+` by the 5-day $9.40-$9.50 shelf ($22.81M / 80 trades) defending the cycle low. |
| 3 — OI | **++** | "Bullish OI weighting 3:1 (16,127 vs 5,805 contracts); cleanest signature 2026-05-29 $13C ask/bid 31:1 +2,128 OI; 25-session consecutive build" [OI:biggest_increases][OI:smart_positioning] — structural multi-week positioning, not a one-day spike. |
| 4 — structure | **++** | "Net DEX +$2.16B (mechanical dealer buy), per-strike GEX negative $8-$10.5 → flip $11 → $13 wall +$627M, IV term kink 118.3% at 2026-05-29" [STRUCT:dex][STRUCT:gex][STRUCT:iv_term_structure] — textbook short-gamma fuel into a confirmed catalyst, with a clear long-gamma resistance ceiling. |
| 5 — historical | **−** | "bullish_flow signal market-wide 14.3% win rate over 20 trading days, avg -2.68% across 14 firings; every comparable mega-cap tech bullish-flow signal DOWN" [HIST:signal_backtest] — a material historical disconfirmation that the skill heuristics explicitly say should downgrade conviction. |
| 6 — macro | **−−** | "UW regime TRANSITIONAL (half size, defined-risk), technology sector net options outflow -$151M (WORST sector), SaaSpocalypse 30-yr worst non-recessionary software drawdown, CPI 3.8% YoY removes Fed-cut hope" [MACRO:MarketRegime_2026-05-15 UW][MACRO:SectorRotation_2026-05-15 UW][MACRO:SaaSpocalypse_2026-Q1 WebSearch:saastr.com][MACRO:CPIAUCSL_2026-04 WebSearch:cnbc.com] — five independent macro/sector headwinds vs 2 PATH-specific tailwinds. |
| 7 — insights | **−** | "Conviction matrix MIXED with 8.55% confidence; institutional_accumulation NEUTRAL signal despite buy/sell ratio 1.41; PATH not in top-50 signal_confluence (no `low_iv` factor)" [INSIGHT:conviction_matrix][INSIGHT:institutional_accumulation][INSIGHT:signal_confluence] — UW's threshold-based composites refuse to validate a directional read; offset partially by `price_vs_flow` DIVERGENCE bullish read but on net contradicts the LONG bias. |
| 8 — agents | **+ (4 of 5 align, net +6)** | 2× LONG (+4: accumulation-hunter, sweep-tracker) + 1× RANGE/sell-vol with positive delta (+2: earnings-scout, matches phase-9 vol-fade overlay) + 1× NEUTRAL-lean-LONG defined-risk (+2: risk-monitor) + 1× SHORT/fade (-2: contrarian-scanner). 5/5 agents agree on "no naked long calls, mandatory pre-SNOW de-risk, defined-risk only" — operational consensus is unanimous even where bias label differs. |

**Raw score:**
- Phase 1: +15
- Phase 2: +7
- Phase 3: +15
- Phase 4: +15
- Phase 5: -7
- Phase 6: -15
- Phase 7: -7
- Phase 8: +6
- **Sum = +29**

**Confluence_score:** (29 + 115) / 230 × 100 = **62.6 → 63/100**

**Recommended bin (per rubric 50-64 band):** **0.65**
**Phase-9 actual bin:** **0.65** → **MATCH** ✓

## Contradictions

- **phase-5 (historical signal backtest)**: PATH-specific signals are
  bullish, but the broader bullish_flow signal has a 14.3% 20-day win
  rate and the entire mega-cap-tech cohort with the same signal
  pattern is down 0-8% over the past 20 days. **Suggested resolution:
  DOWNGRADE conviction** (already applied — phase-9 used the 0.65 bin
  AND the 0.80× regime multiplier on the Kelly suggestion).
- **phase-6 (macro)**: TRANSITIONAL UW regime, technology sector worst
  net options flow (-$151M), SaaSpocalypse sector beta dominant, hot
  CPI removes Fed-cut tailwind, FOMC on hold and not in the trade
  window. **Suggested resolution: TIGHTEN INVALIDATION** (already
  applied — phase-9 added the macro-based invalidation
  "UW regime flips to RISK-OFF" AND "SPY breadth < 30%" AND the
  mandatory pre-SNOW de-risk).
- **phase-7 (UW insights composite)**: Conviction matrix MIXED with
  8.55% confidence and institutional_accumulation NEUTRAL signal —
  the two threshold-based UW composites do not validate the LONG read.
  **Suggested resolution: WAIT FOR CONFIRMATION** — phase-9's primary
  entry condition is "tag of $10.25-$10.45 institutional cluster with
  dealer regime still POSITIVE (ZGL ≤ $7.53)"; if conviction matrix
  flips toward DIRECTIONAL_SHORT (DP buy_ratio drops below 0.40), the
  signal-based invalidation in phase-9 fires immediately.

## Citation spot-check

Picking 3 of phase-9's 7 thesis citations to audit:

1. **[FLOW:hot_chains_sweep_persistence]** → claim: "PATH 5-of-5
   sweep persistence, $7.77M cumulative."
   - Resolves in **phase-1-flow.md § Key signals** / § "Market-wide
     context": `PATH appeared in the top sweep activity 5 of 5 sessions
     ... cumulative sweep premium $7.77M.` ✓ **PASS**
2. **[DP:price_levels]** → claim: "$9.40-$9.50 5-day institutional
   shelf $22.81M / 80 trades."
   - Resolves in **phase-2-dark-pool.md § "Price levels (5-day cluster
     map)"**: `$9.40-$9.50 (6 levels) | $22.81M | 2,403,329 sh | 80
     trades`. ✓ **PASS** (note: phase-2 actually wrote $22.81M which
     differs by $0.43M from a manual sum because phase-2 included the
     7-level breakdown; the $22.81M is the figure stated in the phase
     verdict and is what phase-9 cites — internally consistent).
3. **[STRUCT:gex]** → claim: "ZGL $7.53, per-strike $13 GEX wall
   +$627M."
   - Resolves in **phase-4-structure.md § "GEX (DTE ≤ 45)"**: `Total
     GEX +$1,051,169,560, ZGL $7.53` and table row `$13 | +$627.11M
     | Dominant positive wall`. ✓ **PASS**

**Citation failures:** none in spot-check (3 of 3 resolved).

## Sanity checks

- [x] All `phase-*.md` files present in
  `/Users/ewan/Development/stock-deep-dive/research/PATH/2026-05-18/`
  (phase-0 through phase-10). ✓
- [x] Phase-9 cites ≥3 distinct upstream datapoints. **7 listed.** ✓
- [x] Conviction bin in {0.55, 0.65, 0.75, 0.85, 0.95}. **0.65.** ✓
- [x] ≥1 directional + ≥1 defined-risk structure present. **Call
  diagonal (directional) + bull put credit spread (defined-risk).** ✓
- [x] Sizing math shown (Kelly inputs, raw kelly, fractional kelly,
  cap, regime multiplier, final size). ✓
- [x] Disclaimer line present at top of phase-9. ✓
- [x] Invalidation has all three categories (price-based, signal-based,
  macro-based) with concrete falsifiable conditions. ✓
- [x] Catalyst calendar populated with dates from phase-6. ✓
- [x] Post-trade monitoring checklist has ≥4 items. **9 items.** ✓

## Final auditor note

This run is **internally consistent and ready for action**. The dominant
bias (LONG defined-risk + vol-fade overlay) is the only directional
expression that simultaneously honors the strong bullish microstructure
(phases 1, 3, 4) AND respects the loudly contradictory macro/regime
data (phases 5, 6, 7). Phase-9's conviction bin matches the audit
recommendation exactly; sizing is conservative (2% directional + 1%
defined-risk = 3% of book at risk) and well inside the rubric caps;
invalidation is concrete and includes the single most important
forward catalyst (SNOW 2026-05-27 AMC) as a mandatory de-risk trigger
**before** PATH's own 2026-05-28 earnings event. **No revision of
phase-9 is required.** The desk should execute as written and
re-audit if/when (a) SNOW prints, (b) ZGL crosses $7.53, or (c) PATH
closes outside the $9.40-$10.71 range.
