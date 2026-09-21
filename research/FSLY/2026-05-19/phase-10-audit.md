# Phase 10 — Audit & Confidence Score

**Ticker:** FSLY
**As-of date:** 2026-05-19  (Effective data date: 2026-05-18)
**Generated:** 2026-05-19T01:45:00Z
**Phase-9 thesis under audit:** LONG (covered-call posture), bin 0.65, 1-4w
**All upstream phases cited:** phase-0 through phase-9 in
`/Users/ewan/Development/stock-deep-dive/research/FSLY/2026-05-19/`

## Summary

**Confluence score = 57 / 100.** Phase-9's conviction bin (0.65)
**MATCHES** the band recommended by the score (50-64 → 0.65). The
run is **internally consistent** — phases 1-4 agree mildly with the
bullish thesis, phase-7 corroborates with the COVERED_CALL/ACCUMULATION
read, while phases 5 and 6 surface specific contradictions (bullish_flow
8.3% win-rate; tech sector −$299.8M outflow) that phase-9 has already
addressed by sizing at HALF the Kelly-derived cap and tightening
macro-based invalidation triggers. **2 contradictions logged; both
mitigated in-plan.** All 3 citation spot-checks resolved. All sanity
checks pass. Trade blueprint is ready for action.

## Confluence scorecard

| Phase | Score | Justification (quote a datapoint) |
|---|---|---|
| 1 — flow | **+** | "FSLY 5-of-5 sessions, consistency_score 1.0, total_sweep_premium (5d) $642,945" [FLOW:hot_chains_sweep_persistence] — campaign persistence is real but $211K Jan'27 $20C bid-side block is a write (capped upside), and OI changes show only 5 contracts cleared 100Δ → mildly agrees. |
| 2 — dark pool | **+** | "Block tier buy_ratio = 0.847 (3 trades, $7.24M, 371K shares bought above mid)" [DP:dark_pool_block_stratified] — clear accumulation, but $22M overhead supply at $18.41-$19.03 caps the thesis → mildly agrees. |
| 3 — OI | **+** | "Bullish-inferred new positioning ≈ +1,154 contracts vs bearish ≈ +668 (~63% bullish skew)" [OI:oi_smart_positioning] — net bullish but the +300 OI fresh 6/5 $23C bid write is a meaningful counter-position → mildly agrees. |
| 4 — structure | **+** | "Net vanna +16,563; net charm +431,948; classic vanna-squeeze setup if VIX collapses" [STRUCT:vanna_charm] + REVERSE COMPLACENT skew [STRUCT:term_skew] → bullish-supportive but total_gex is −$9.8M with deepest neg-gamma at $17.5 → mildly agrees. |
| 5 — historical | **−** | "bullish_flow signal backtest: total_signals 12, win_rate **8.3%**, avg_move_pct **−3.22%**" [HIST:signal_backtest] — 11 of 12 recent bullish_flow signals across the tech complex went down. This is a real, specific contradiction. |
| 6 — macro | **−−** | "Technology sector net flow −$299,789,934 on 5/18 alone (30× the next-worst sector)" [MACRO:MarketRegime_2026-05-18 UW] + 10y yield 4.61% + April CPI 3.8% YoY (highest since May 2023) → strong macro headwind. |
| 7 — insights | **+** | "scenario: COVERED_CALL; confidence_pct 24.51; DP buy_ratio 0.692; call_bid_volume 3,534 vs call_ask_volume 2,858" [INSIGHT:conviction_matrix] — canonical institutional framing for the thesis, but FSLY absent from both bullish & bearish top-50 confluence lists prevents `++`. |
| 8 — agents | **+ (2/4 align)** | acc-hunter LONG (+2), sweep-tracker LONG (+2), contrarian NEUTRAL (0), risk-monitor NEUTRAL (0), earnings-scout MISSING (0). 2 LONG / 2 NEUTRAL / 0 SHORT → directionally constructive. Net contribution: +4. |

**Raw score breakdown:**

| Source | Symbol | Points |
|---|---|---|
| Phase 1 | + | +7 |
| Phase 2 | + | +7 |
| Phase 3 | + | +7 |
| Phase 4 | + | +7 |
| Phase 5 | − | −7 |
| Phase 6 | −− | −15 |
| Phase 7 | + | +7 |
| Phase 8 | net | +4 |
| **Total raw** | | **+17** |

**Confluence_score:** `(17 + 115) / 230 × 100 = 57.4` → **57 / 100**

**Recommended bin (per rubric 50-64 band):** **0.65**

**Phase-9 actual bin:** **0.65** → **MATCH** ✓

## Contradictions

- **phase-5 (historical):** bullish_flow signal_backtest 8.3% win rate
  over the last 5 trading sessions (12 signals, 11 down, avg −3.22%)
  contradicts the LONG-biased thesis from phases 1/2/3.
  **Suggested resolution:** *tighten invalidation* — phase-9 already
  did this via the signal-based invalidation
  (cumulative_premium_flow flipping bearish for 3 consecutive
  sessions = exit) and the macro-based invalidation (tech sector
  outflow ≤ −$500M for 3 days = exit). No further change needed.

- **phase-6 (macro):** Technology sector premium outflow −$299.8M
  on 5/18 alone (30× next worst), 10y yield at 4.61% (cycle high),
  April CPI 3.8% YoY (highest since May 2023) — collectively
  contradicts adding fresh LONG tech-sector exposure.
  **Suggested resolution:** *downgrade conviction* — phase-9 already
  downgraded sizing from the 5% cap to **2.5% (half cap)**, which
  effectively implements the conviction haircut without changing
  the M-01 bin. No further change needed.

## Citation failures

Spot-checked 3 citations from phase-9 thesis. All resolve.

| # | Citation tag | Claim quoted | Resolves to | Status |
|---|---|---|---|---|
| 1 | `[INSIGHT:conviction_matrix]` | "COVERED_CALL scenario, confidence 24.51%, DP buy_ratio 0.692, call_bid_volume 3,534 vs call_ask_volume 2,858" | phase-7-insights.md § "Conviction matrix — COVERED_CALL" | ✓ |
| 2 | `[FLOW:hot_chains_sweep_persistence]` | "5-of-5 sessions, consistency 1.0, $642,945 5-day premium" | phase-1-flow.md § "Multi-day persistence" (table row sessions_in_top 5/5, consistency_score 1.0, total_sweep_premium (5d) $642,945) | ✓ |
| 3 | `[MACRO:MarketRegime_2026-05-18 UW]` | "Technology sector net flow −$299.8M on 5/18" | phase-6-macro.md § "Market regime (UW)" / Sector rotation table (Technology −$299.8M) | ✓ |

No citation failures. (Section intentionally empty.)

## Sanity checks

- ✓ All `phase-*.md` files present in
  `research/FSLY/2026-05-19/` (10 files: phase-0 through
  phase-9).
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (cites 6:
  conviction_matrix, sweep_persistence, term_skew, MarketRegime,
  signal_backtest, AGENT:risk-monitor).
- ✓ Conviction bin (0.65) is in {0.55, 0.65, 0.75, 0.85, 0.95}.
- ✓ Directional structure present: 7/17 $17.5/$22.5 bull call
  debit spread.
- ✓ Defined-risk alternative present: 7/17 $15/$12.5 bull put
  credit spread.
- ✓ Sizing math shown explicitly (Kelly p=0.65, b=2.18,
  raw_kelly=48.9%, fractional×0.25=12.2%, capped at 5%, final
  2.5% with downward-deviation rationale).
- ✓ Required disclaimer present at top of phase-9.
- ✓ All entry/level/invalidation rows in phase-9 carry citation
  tags (spot-checked 5 of them).
- ✓ Catalyst calendar present in phase-9; matches phase-6.

## Final auditor note

The run is **internally consistent and ready for action** at the
recommended sizing. The two contradictions surfaced (phases 5 and
6) are both already addressed within phase-9 — phase-5's
bullish_flow backtest risk is mitigated by the 3-session bearish
flow flip and the ≤ −$500M tech-outflow invalidation triggers;
phase-6's macro headwind is mitigated by the 50%-of-cap sizing
deviation and the defined-risk-only structure requirement. **No
revision of phase-9 is required.** A score of 57 / 100 correctly
signals "moderate edge, not high conviction" — exactly what the
COVERED_CALL framing implies.
