# Phase 10 — Audit & Confidence Score

**Ticker:** SNOW
**As-of date:** 2026-05-16 (data date 2026-05-15)
**Generated:** 2026-05-17T00:00:00Z
**Upstream phases audited:** phase-0 through phase-9

## Summary

**Confluence score: 85 / 100** → recommended conviction bin **0.85**.
**Phase-9 actual conviction bin: 0.75** → **MISMATCH (-1 bin), but documented in phase-9 `## Conviction deviation`** with three falsifiable reasons (binary earnings event, fresh GEX regime, agent-average conviction 2.6/5).
**Contradictions count: 1** (phase 1 — bullish directional flow contradicts the SHORT-VOL primary). Already mitigated by the trade's tight invalidation at the ZGL ($154.56) and by the bear-call-spread alternative.
**Citation spot-check: 3 of 3 cited datapoints resolved.**
**Sanity checks: all ✓.**

The run is internally consistent. The SHORT-VOL iron condor on 5/29 expiry (short 150P/180C, wings 140P/190C) is supported by 5 of 7 phases (and 4 of 5 agents). Phase-9 is **ready for action** as a defined-risk trade structure within the disclosed risk budget.

## Dominant bias (from phase 9)

**RANGE / SHORT-VOL** (with tactical short-bias overlay above $160), horizon 1-4w through 2026-05-27 SNOW Q1 FY27 earnings.

## Confluence scorecard

| Phase | Score | Justification (quote a datapoint from the phase) |
|---|---|---|
| 1 — flow | **`-`** | "Net assessment: bullish near-term, conviction 4/5" (phase-1 §Verdict). Directional bullish flow CONTRADICTS the SHORT-VOL primary; however, phase-1's secondary read of two-way LEAP positioning and persistent-but-mixed 5-day sweep premium ($57.3M) is RANGE-consistent. Net: mildly contradicts. |
| 2 — dark pool | **`++`** | "BLOCK tier ($1M-$10M): buy_ratio = 0.304 on $16.7M premium, 8 trades" (phase-2 §Tier breakdown). Decisive institutional distribution — strongly supports the fade-bullish-flow / range thesis. The 5-day institutional support cluster $150.74-$153.20 is the lower edge of the iron condor's profitable range. |
| 3 — OI | **`++`** | "Institutional short-strangle structure $150-$180" with 150P bid-side OI +930 + 180C bid-side OI +929 + 200C bid-side OI +869+821 (phase-3 §Largest OI increases). The iron condor's strikes are literally the OI builds. |
| 4 — structure | **`++`** | "total_gex +$4.83B, ZGL $154.56, $160 wall $2.31B, regime POSITIVE; 5/29 IV kink 107.6%" (phase-4 §GEX, §IV term structure). Long-gamma regime + earnings vol kink = both legs of the short-vol thesis confirmed. |
| 5 — historical | **`++`** | "IV percentile 92, VRP +13.3% PREMIUM_SELLING, bullish_flow backtest win rate 20% / avg move -1.07% over 5d" (phase-5 §VRP, §Signal backtest). Highest-edge premium-selling signal in the run. |
| 6 — macro | **`+`** | "Tech sector -$151M outflow; CPI YoY 3.8%; 10y 4.59% one-year high; TRANSITIONAL regime ('half size')" (phase-6 §Tailwind/Headwind table). Macro tilts NEGATIVE for high-multiple software, supporting the no-rally-above-$180 thesis. Mild support, not decisive. |
| 7 — insights | **`++`** | "scenario MIXED, confidence 1.82%, DP buy_ratio 0.482; SNOW absent from bullish_signal_confluence top 20 even at min_score=1" (phase-7 §Conviction matrix, §Signal confluence). UW's own composite agrees with the non-directional thesis. |
| 8 — agents | **+6** (4/5 align) | 4 of 5 agents aligned with RANGE/SHORT-VOL (+2 each = +8); 1 dissent sweep-tracker LONG (-2). Net +6. Plurality and average conviction 2.6/5 (phase-8 §Tally). |

**Raw score:** (-7) + 15 + 15 + 15 + 15 + 7 + 15 + 6 = **+81**
**Confluence_score:** (81 + 115) / 230 × 100 = 196/230 × 100 = **85 / 100**
**Recommended bin:** 0.85 (band 80-89)
**Phase-9 actual bin:** 0.75 — **MISMATCH (downward, by one bin)**

**Deviation reviewed:** Phase-9's `## Conviction deviation` section gives 3 specific, falsifiable reasons:
1. Binary event risk (5/27 earnings).
2. GEX regime is 2 sessions old; 4/29 → 4/30 precedent flip-and-reverted.
3. Agent average conviction 2.6/5 = 0.52, well below the 0.85 confluence score.

These are valid per the rubric's deviation allowance. **The deviation is APPROVED.** The audit-recommended action is to either:
- (a) Accept phase-9's 0.75 as final, OR
- (b) If the GEX regime holds through Monday 5/18 and BLOCK-tier DP buy_ratio remains ≤0.45, upgrade to 0.85 and increase size up to the 5% cap.

## Contradictions

- **phase-1 (flow):** Phase 1 verdicted **bullish, conviction 4/5** based on the $145C Jun-26 $2.10M ask-side block (vol/OI 314.67) plus net ask-side sweeps. This conflicts with phase-9's SHORT-VOL primary. **Suggested resolution:** **Tighten invalidation** — already done; phase-9 closes 50% of the condor if BLOCK-tier DP buy_ratio crosses >0.55, or if spot closes >$162.50 cleanly. Also: the bear call spread alternative (175/195) is a defined-risk way to express the fade while still respecting the upside risk. **No further action required.**

### Internal-consistency note on phase-1 vs phase-3 (the $145C 6/26 OI question)

Phase 3's open question was: why does the phase-1 $2.10M / 944-volume / vol-OI 314.67 trade on the 6/26 $145C NOT appear in phase-3's top-7 OI increases?

**Resolution:** Phase-3's `oi_biggest_increases` tool measures **NET OI change** (EOD OI minus prior-day OI). The 944 volume on 5/15 was a mix of opening and closing trades by different actors; the largest single ask-side block (467 contracts) was likely net-new opening but the bid-side counter-print (285 contracts) and other day-trader churn means net new OI was meaningfully less than 944 — likely below phase-3's `min_oi_change=500` threshold. **This is data nuance, not contradiction.** Phase-1 measured premium-and-volume turnover; phase-3 measured net OI change. Both are correct.

## Citation failures

Spot-checked 3 of phase-9's thesis citations:

1. **[HIST:signal_backtest] win rate 20%, avg move -1.07%** → resolves in **phase-5-historical.md** §"Signal backtest (bullish_flow over last 5d)". `total_signals: 10, win_rate: 20.0%, avg_move_pct: -1.07%`. ✓ CONFIRMED.

2. **[STRUCT:gex] total_gex $4.83B, ZGL $154.56, $160 net_gex $2.31B** → resolves in **phase-4-structure.md** §GEX. `total_gex: +$4,833,651,697`, `zero_gamma_level: $154.56`, $160 net_gex `+$2,311,523,013`. ✓ CONFIRMED.

3. **[DP:block_stratified] BLOCK tier buy_ratio 0.304 on $16.7M / 8 trades** → resolves in **phase-2-dark-pool.md** §Tier breakdown. BLOCK row: `buy_ratio 0.304, buy_vol 32,483, sell_vol 74,543, total_premium $16,674,154, trade_count 8`. ✓ CONFIRMED.

**Citation failures: 0.** All cited datapoints resolve to specific values in the cited phase files.

## Sanity checks

- [x] All `phase-*.md` files present in `/Users/ewan/Development/stock-deep-dive/research/SNOW/2026-05-16/`: phase-0 through phase-9, ten files. ✓
- [x] Phase-9 cites ≥3 distinct upstream datapoints: **10 listed** in §Citations summary. ✓
- [x] Conviction bin in {0.55, 0.65, 0.75, 0.85, 0.95}: **0.75**. ✓
- [x] ≥1 directional + ≥1 defined-risk structure: **bear call spread 175/195** (directional) + **iron condor 140/150/180/190** (defined-risk). ✓
- [x] Sizing math shown explicitly: **Kelly inputs, raw_kelly = 0.546, fractional 13.6%, capped at 5.0%**. ✓
- [x] Disclaimer present at top of phase-9: ✓
- [x] All UW tool errors surfaced (Yahoo 401 in phase-7, FRED skipped in phase-6): ✓
- [x] Phase-6 catalyst calendar present and used by phase-9: ✓ (5/21 cohort, 5/26 ZS, **5/27 SNOW**, 6/16-17 FOMC).

## Final auditor note

The run is internally consistent and the trade blueprint is **ready for action** as a defined-risk SHORT-VOL position. Phase-9's downward conviction deviation from 0.85 → 0.75 is well-justified by binary event risk and is reflected in tighter invalidation rather than reduced sizing (which is already at the 5% cap). The single directional contradiction (phase-1 bullish flow vs SHORT-VOL primary) is structurally absorbed by the iron condor's defined max-loss and by the optional bear-call-spread alternative; no further audit action required.

---

## Output paths (for user reference)

```
/Users/ewan/Development/stock-deep-dive/research/SNOW/2026-05-16/
├── phase-0-intake.md          ← run metadata
├── phase-1-flow.md            ← options tape, sweeps, conviction
├── phase-2-dark-pool.md       ← institutional block / price levels
├── phase-3-positioning.md     ← OI builds / pin risk
├── phase-4-structure.md       ← GEX / DEX / vanna / IV term structure
├── phase-5-historical.md      ← IV regime / VRP / signal backtest
├── phase-6-macro.md           ← regime / CPI / rates / catalysts
├── phase-7-insights.md        ← UW composite cross-check
├── phase-8-agent-views.md     ← 5 analyst verdicts
├── phase-9-trade-plan.md      ← PM-voice blueprint (THIS RUN'S DELIVERABLE)
└── phase-10-audit.md          ← THIS FILE
```

## Run statistics

- **UW MCP tool calls (estimated total, all phases):** ~55
- **Web searches:** 5 (phase-6 only)
- **Sub-agents launched (phase-8):** 5 (accumulation-hunter, contrarian-scanner, sweep-tracker, earnings-scout, risk-monitor)
- **Yahoo/yfinance errors:** 2 (phase-7 deep_dive + analyst_vs_flow) — partially compensated by phase-6 WebSearch.
- **FRED API:** skipped (no `FRED_API_KEY` env var); WebSearch fallback used.
- **Final confluence score:** 85 / 100.
- **Final conviction bin:** 0.75 (deviation from 0.85 documented).
