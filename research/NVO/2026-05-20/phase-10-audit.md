# Phase 10 — Audit & Confidence Score

**Ticker:** NVO
**As-of date:** 2026-05-20
**Generated:** 2026-05-20T22:45:00-04:00
**Dominant bias under audit:** **LONG** (per phase-9-trade-plan.md)
**Audited conviction bin:** 0.85

## Summary

Confluence score = **87 / 100** (raw +85 out of ±115). Recommended
conviction bin = **0.85** → **MATCHES** phase-9's actual bin. Zero phases
scored `-` or `--` (no formal contradictions). Three of three sampled
citations resolve cleanly. All 10 phase MDs are present and complete.
Phase-9 satisfies the M-04 citation requirement (≥3 distinct upstream
datapoints) by a wide margin (10 cited). The run is **internally
consistent and ready for action**, with two known explicit risks already
embedded in invalidation: (1) the 7/1 LLY Medicare-Bridge competitive
cliff, (2) NVO's absence from phase-7's bullish_signal_confluence top 50.

## Confluence scorecard

| Phase | Score | Justification (quote a datapoint) |
|-------|:-----:|-----------------------------------|
| 1 — flow | **++** | "$1,007,176 ask-side sweep on NVO 2028-01-21 $45C, 30 trades, avg fill $10.64" + "Bullish premium dollars dominate today's tape 14×" [FLOW:sweeps] (phase-1-flow.md §Sweeps). Strongly agrees with LONG. |
| 2 — dark pool | **++** | "$26,943,297 mega print at $45.07 ... NBBO mid (trade_vs_mid 0.00)" + "Mega-tier buy_ratio 1.000; block-tier 0.893" [DP:largest, DP:block_stratified] (phase-2-dark-pool.md §Tier breakdown). Strongly agrees. |
| 3 — OI | **+** | "NVO 2026-06-18 $42.5P, OI 17 → 1,110 (+1,093) … smart_positioning = bullish (puts being sold)" [OI:biggest_increases] (phase-3-positioning.md §Largest OI increases). Mildly agrees — bullish put-sale floor but $50C call wall caps and 05/29 $45C bid-side OI build is income/covered = mixed counterweight. |
| 4 — structure | **++** | "POSITIVE GEX, total $2,099,855,377; ZGL = $27.44 vs spot $44.90 ... $45 strike +$776M; $50 strike +$825M" + "DEX = +$6,224,791,580 — dealer hedge = BUY underlying" [STRUCT:gex, STRUCT:dex] (phase-4-structure.md §GEX). Strongly agrees. |
| 5 — historical | **++** | "IV30 = 37.66%, IV percentile = 7.14, z-score = −1.36 → LOW_IV regime" + "Today's GEX regime flipped POSITIVE with ZGL collapsing −$17.30 (from $44.74 to $27.44) — biggest 1-day shift in the 29-session series" + "April 28 analog ran +8% in 5 sessions" [HIST:iv_percentile_zscore, HIST:gex_time_series] (phase-5-historical.md). Strongly agrees. |
| 6 — macro | **+** | "Wegovy pill 1.3M Q1 scripts ≈ 2× consensus … raised 2026 guidance" [MACRO:NVO_Q1_2026] is a strong tailwind, but "LLY Medicare GLP-1 Bridge live 2026-07-01 — NVO not in package" [MACRO:Medicare_GLP1_Bridge] caps the score at + (phase-6-macro.md §Tailwind/Headwind table). Mildly agrees. |
| 7 — insights | **+** | "Conviction matrix: DIRECTIONAL_LONG (confidence 23.98%, DP buy_ratio 0.687)" [INSIGHT:conviction_matrix] + "Institutional accumulation: ACCUMULATION buy/sell 2.19×" [INSIGHT:institutional_accumulation] support LONG, BUT "NVO did NOT appear in the bullish signal-confluence top 50" [INSIGHT:signal_confluence] is a meaningful caveat that prevents ++ (phase-7-insights.md). Mildly agrees. |
| 8 — agents | **+4** raw (= +2/agent × 3 LONG aligned − 2 NEUTRAL not aligned) | LONG: accumulation-hunter (conviction 4), sweep-tracker (4), risk-monitor (3); NEUTRAL: contrarian-scanner (2). 3 of 4 active agents align with LONG (earnings-scout skipped as out-of-window) (phase-8-agent-views.md §Agent verdicts table). |

**Raw score arithmetic:**
- Phase 1: +15
- Phase 2: +15
- Phase 3: +7
- Phase 4: +15
- Phase 5: +15
- Phase 6: +7
- Phase 7: +7
- Phase 8: +4 (3 × +2 LONG − 1 × +2 not-aligned = +6 − 2 = **+4**)
- **Total raw:** **+85**

**Confluence_score:** (85 + 115) / 230 × 100 = **86.96 → 87 / 100**

**Recommended conviction bin** (per confluence-scoring rubric, band
80–89): **0.85**

**Phase-9 actual bin:** **0.85** → **MATCH ✓**

## Contradictions

No phases scored `-` or `--`. Therefore no formal contradictions.

However, **soft caveats** worth restating (these are not contradictions
but warrant operator awareness):

- **phase-1 (flow):** 5-day sweep persistence was BEARISH ($9.68M total)
  until today — the bullish flip is one session old. Today is a real
  inflection but not yet confirmed by a 2-day continuation.
  *Resolution embedded in phase-9 already:* invalidation tightened to a
  two-close-below-$44 rule and a single intraday-print-below-$43.50
  trigger.

- **phase-7 (insights):** NVO not in bullish_signal_confluence top 50.
  *Resolution embedded in phase-9 already:* conviction held at 0.85
  (lower end of the band, not 0.95), and sizing capped at 5% rather than
  expanded via deviation reason.

- **phase-6 (macro):** TRANSITIONAL market regime + 7/1 LLY Medicare
  Bridge.
  *Resolution embedded in phase-9 already:* one of the named macro-based
  invalidation conditions explicitly fires if NVO is excluded > 30d after
  7/1. Also: pre-FOMC 6/16 the desk halves the position regardless.

## Citation failures

Three citations spot-checked from the phase-9 thesis paragraph:

1. **[FLOW:sweeps]** — "$1.0M ask-side LEAP sweep on the Jan 2028 $45 calls (30 trades, δ 0.62)"
   - Resolves in `phase-1-flow.md` §Sweeps row 1: total_premium $1,007,176; option_type call; expiry 2028-01-21; strike 45; side ask; total_size 950; trade_count 30; from `options_flow_sweeps`. ✓
   - Δ 0.62 resolves in same file §Largest premium prints row 1: delta 0.619. ✓

2. **[DP:largest, DP:block_stratified]** — "$26.94M dark-pool mega-print at $45.07 with mega-tier buy_ratio 1.0"
   - `phase-2-dark-pool.md` §Largest individual blocks row 1: premium $26,943,297; price $45.07; size 597,810; trade_vs_mid 0.00. ✓
   - §Tier breakdown row "Mega (≥$10M)": buy_ratio 1.000; premium $26,943,297. ✓

3. **[HIST:gex_time_series]** — "ZGL dropped −$17.30 to flip back into POSITIVE gamma"
   - `phase-5-historical.md` §GEX time series row 2026-05-20: from NEGATIVE to POSITIVE; spot 44.90; ZGL 27.44; zgl_delta −17.30. ✓

**All 3 of 3 citations resolve cleanly.** No failures.

## Sanity checks

- [✓] All `phase-*.md` files present in `research/NVO/2026-05-20/` (0 through 9; this audit completes phase-10)
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (cites 10)
- [✓] Phase-9 conviction bin = 0.85 ∈ {0.55, 0.65, 0.75, 0.85, 0.95}
- [✓] ≥1 directional structure present (Long 2026-07-17 $45 Call)
- [✓] ≥1 defined-risk structure present (2026-07-17 $45/$50 Call Debit Spread)
- [✓] Sizing math explicit (p, b, raw Kelly %, fractional, cap, final)
- [✓] Disclaimer line present at top of phase-9
- [✓] Invalidation includes all three categories (price, signal, macro)
- [✓] Macro tailwinds + headwinds tagged with [MACRO:…]
- [✓] Catalyst calendar populated for next 30d
- [✓] Post-trade monitoring checklist ≥ 4 items (has 8)

## Final auditor note

The 10-phase run is **internally consistent and ready for action**.
Confluence (87/100) matches the recommended bin (0.85) and phase-9 sized
within the rubric cap (5%) with all sizing math shown. The two
non-contradiction caveats (1-day-flip lookback and missing-confluence
flag) are already encoded into tighter-than-default invalidation and a
half-Kelly-style sizing posture. No phase-9 revision is required;
operator may execute as written.
