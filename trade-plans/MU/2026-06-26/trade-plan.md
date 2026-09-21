# Trade Plan — MU

**As-of date:** 2026-06-26
**Spot reference:** 1213.56 (yfinance EOD, = 52-week high)
**Voice:** desk PM running an institutional book
**Built from:** `research/MU/2026-06-25/` (1-day-old deep dive) + chart engine (yfinance, 372 sessions)

> *For research and educational use only. Not financial advice. Sizing,
> structures, targets and dates are illustrative.*

## 0. Information completeness (gap audit)

- **Verdict:** **SUFFICIENT** — completeness **100%**
- **Have:** options flow, dark pool, OI/positioning, dealer GEX/DEX/vanna, historical
  win-rate, macro/sector, fundamentals, sentiment/crowd, OHLCV chart + patterns, events
- **Missing / how to source:**
  | Item | Severity | How to source |
  |------|----------|---------------|
  | Today's (06-26) intraday tape | nice_to_have | `uw options-flow sweeps --symbol MU` · `uw insights deep-dive --symbol MU --json` |
  | Live spot vs the 1213 ATH | nice_to_have | `fz quote MU` · re-run `chart_engine.py` intraday |

No critical/important gaps. The constraint here is **entry/timing & crowding**, not missing data.

## 1. Direction & conviction

- **Bias:** **LONG** (entry-gated, not thesis-gated)
- **Conviction (M-01 bin):** **0.55** (floor — pinned by 5 CAUTION/crowd/debate gates)
- **Horizon:** 1-3m
- **Confluence score:** 44 (deep-dive A3)
- **Flow↔chart agreement:** CONFLUENT on direction, **FLOW-LEADS at the breakout** → anticipatory, trigger-based entries; token at spot, full size only on the pullback.

### Thesis (≤3 sentences)
MU is the **#1 single-name net-bullish premium in the entire universe** (+$279M,
calls 2.79x [FLOW:insights_deep_dive]) and the cheap-on-forward (fwd P/E 8.4, 4/4
beats [FUND:fwd_pe]) leader of a confirmed memory supercycle, with a clean Stage-2
uptrend and **no call wall above spot** [CHART:trend][OI:oi_by_strike]. But spot is
the *worst possible location* — the all-time high, riding the upper Bollinger,
+188% over the 200-MA, while the **dark pool is distributive** (mega buy_ratio 0.47
[DP:block_stratified]) and dealers are long-gamma with **max-pain pulling to 1040**
[STRUCT:gex][STRUCT:max_pain]. **Structural long — but the edge is a pullback to the
$1,134 shelf (or a confirmed close > 1255), token size at spot.**

### Why it should work
- **#1 universe net-bullish premium** +$279M, calls 2.79x, self-pctile 98.1, price-and-flow aligned [FLOW:insights_deep_dive].
- **Cheap-on-forward supercycle leader** — fwd P/E 8.4, PEG 0.05, 4/4 beats; DRAM +90% QoQ, HBM sold-out 2026 [FUND:fwd_pe][MACRO:memory_cycle_2026].
- **Clean uptrend, no overhead supply** — HH-HL, bullish MA stack, no call wall above spot → blue sky over 1255 toward fib-1.272 = 1516 [CHART:trend][OI:oi_by_strike][CHART:fib].
- **Structural dealer bid** — DEX +$30.5B (net short calls → must buy underlying) [STRUCT:dex].

### Why it may fail (the honest other side)
- **(Top) Distribution-into-strength** — dark pool balanced/distributive (mega buy_ratio **0.47**) while retail/lit chase a +325%-YTD parabola at the ATH with almost no short cushion (SI 3.71%/0.81d). Smart money is **not** confirming the chase [DP:block_stratified][SENT].
- **Worst location / negative near-term R:R** — ATH (0% off high), upper Bollinger, +188% over 200-MA; long-gamma + vanna-selling + max-pain 1040 cap upside near-term [CHART:bb_upper][STRUCT:vanna_charm][STRUCT:max_pain].
- **Peak-cycle value-trap optic** — fwd P/E 8.4 is the cyclical-top signature; a DRAM/HBM contract rollover re-rates fast [FUND][MACRO:memory_cycle_2026].
- **Crowded + regime risk + bear won the debate** — CROWDED_LONG, regime TRANSITIONAL (breadth 35.4%, leadership = MU itself), debate bear **0.65 > 0.60** bull [SENT][MACRO:MarketRegime][DEBATE].

## 2. Levels to watch

| Level | Role | Source | Note |
|-------|------|--------|------|
| 1516 | target | [CHART:fib_1.272] | measured continuation — only if 1255 breaks |
| 1350 | target | [CHART:measured] | secondary objective / call-spread cap |
| 1255 | trigger | [CHART:fib_swing_high] | break/hold = blue-sky long trigger |
| 1213 | resistance | [CHART:high_52w] / [CHART:bb_upper] | spot = ATH + upper band |
| 1200 | resistance | [OI:oi_by_strike] | call-heavy battleground, net +37,364 |
| 1134 | support / primary entry | [DP:price_levels] | dark-pool absorbed shelf |
| 1024-1040 | support | [CHART:sma20]/[CHART:fib_0.236]/[STRUCT:max_pain] | **chart∩dealer confluence** shelf |
| 1052 | stop / invalidation | [HIST:trend] | 6-23 pivot; two closes below = parabola round-trip |
| 1040 | pin | [STRUCT:max_pain] | downward gravity (soft); **no gamma-flip near spot** (long-gamma across range) |

Moving averages: sma20 1025 · ema21 1005 · sma50 789 · sma200 421 (all rising).
Fib (swing 295→1255): 0.236 = 1028 · 0.382 = 888 · ext 1.272 = 1516. ATR14 = $95 (8.5%).

## 3. Patterns forming (chart)

| Pattern | Direction | Confidence | Measured target | Invalidation | Note |
|---------|-----------|-----------|-----------------|--------------|------|
| parabolic Stage-2 uptrend | bullish | medium | 1516 | 1052 | HH-HL, riding upper band; continuation on close >1255 [CHART:trend] |
| "double top" 1211-1255 | bearish | **none** | — | 1255 | **engine did NOT confirm** — a single new ATH, not two tested tops; discretionary resistance zone only [CHART:patterns] |
| Elliott wave | — | none | — | — | no valid count (pivots not cleanly alternating) [CHART:elliott_wave] |

**Honesty note:** no classical pattern is engine-confirmed. The "double top" everyone
eyeballs is **not** a validated reversal — do not short it as a pattern; it is a
resistance/decision zone that only becomes tradeable bearish on a *lower-high + close
< 1134*.

## 4. Upcoming events that move the tape (next ~30–90d)

| Date | Event | Impact | Source |
|------|-------|--------|--------|
| 2026-07-15 | June CPI | ? | [MACRO] |
| 2026-07-17 | July monthly OPEX (17.27% of OI, put-heavy) | − | [OI:opex_concentration] |
| 2026-07-29 | FOMC + rate decision (easing-cut watch) | ? | [MACRO:DFF] |
| 2026-09-22 | MU earnings | ? | [FUND:next_earnings] |

## 5. Invalidation

- **Price-based:** two daily closes below **1052** (6-23 pivot / shelf failure) confirm the parabola round-trip [HIST:trend].
- **Signal-based:** dark-pool mega buy_ratio ≤ **0.45** (distribution) OR cumulative premium net-bearish 3 consecutive sessions [DP:block_stratified][HIST].
- **Macro-based:** DRAM/HBM contract-price rollover or hyperscaler capex cut re-rates the fwd-8.4 multiple; or hawkish FOMC ~Jul 29 flips regime risk-off [MACRO:memory_cycle_2026][MACRO:MarketRegime].

## 6. Sizing (% of book risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.60** (phase-5 bullish_flow backtest, n=5, src=backtest) → N-cap (n<10 → 0.75) → **p = 0.60**.
- **Inputs:** b = **1.44** (entry 1134, stop 1050, T1 1255), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.60·1.44 − 0.40)/1.44 = **0.322** → ×0.25 = 8.06% → **cap 5%** · **win-rate map ceiling: half (≤2.5%)** (p in 0.50–0.70).
- **Risk gates (each can only cut):** fundamentals **CAUTION → −1 step** · sentiment/crowd **CROWDED_LONG CAUTION → −1 step** · correlation null → no-op · sector-rotation aligned → no-op · debate **bear 0.65 ≥ bull 0.60 → −1 bin & −1 step** · context GENUINELY_UNUSUAL busy name → no top-of-band.
- **Final size:** **0.3% of book** (token). half(2.5%) → starter → token after three CAUTION cuts. Deviation reason: none — this is the rubric-driven token for a crowded-long at the ATH. *Reserve incremental size for the 1134 reclaim; spot/aggressive entries are sub-token probes (~0.1%).*

## 7. Plan A — pure stock (long)

- **Direction:** **long**
- **Entry:** **1134** (primary) — trigger: pullback to the $1,134 dark-pool shelf, go long on **first hold/reclaim** (higher-low + reclaim candle), *not* a falling-knife market buy. **Aggressive alt:** daily **close > 1255** on >1.2x avg vol (L-0001: starter, add only after two closes hold).
- **Stop:** **two daily closes below 1052** (≈1050 effective; ~−7.4% from 1134, sized for the $95 ATR).
- **Targets:** T1 **1255** (ATH/breakout line, take 50%) · T2 **1350** (continuation, take 30%) · T3 **1516** (fib-1.272 runner, 20%).
- **Reward:risk to T1:** **1.44R**.
- **Size:** **0.3% book** (token).
- **One-liner:** Long the memory-supercycle leader on the $1,134 pullback — token into a crowded ATH; the conviction is the pullback, not the chase.

## 8. Plan B — options (≥1 with target date + target price)

Front-expiry implied move **±3.93% (±$47)** [CTX:implied_move]. VRP = **PREMIUM_BUYING**
(RV 122% > IV 91%) → favor **debit** structures, keep any short-premium small.

### B1 — directional (primary)
- **Structure:** **call debit spread** 1150/1350
- **Strikes / expiry:** 1150/1350 / **2026-09-18** (expires 4 days before the 9-22 earnings — captures the cycle + pre-earnings IV ramp, **avoids the print**)
- **Target date / target price:** **2026-09-12 / 1350** (T1 checkpoint 1255; 1350 = spread cap)
- **Debit · breakeven · max loss:** ~$60 debit · **1210** BE · **$60** max loss
- **Est. payoff at target:** ~$140 (width 200 − debit 60) → ~2.3:1
- **Why this structure:** enter on the **1134 pullback** (long 1150 just above the shelf); debit-structured per VRP PREMIUM_BUYING; the 1350 target is a **3-month** objective (not a front-expiry move — ~+11% vs the ±3.9% one-expiry priced move, reasonable over the cycle horizon for an 8.5%-ATR name).

### B2 — defined-risk alternative (bullish-leaning income)
- **Structure:** **put credit spread** 1100/1000
- **Strikes / expiry:** short 1100 (−9.4%, below the 1134 shelf) / long 1000 (on the put_wall_support [OI]) / **2026-07-17** (July OPEX)
- **Target date / target price:** **2026-07-17 / stays ≥ 1100**
- **Debit/credit · breakeven · max loss:** **+$22 credit** · **1078** BE · **$78** max loss
- **Caveat:** RV > IV means you're **selling cheap vol** — keep this *small*; a break < 1100 IS the primary invalidation. Less preferred than B1 given VRP. A one-sigma front-expiry gap (−3.9% → ~1166) does **not** breach the 1100 short strike, but cumulative drift by 7-17 can — size it as a probe.

## 9. Post-entry monitoring checklist

- [ ] Daily: dark-pool mega buy_ratio — flip ≤ 0.45 = distribution = exit/flatten longs.
- [ ] Daily: cumulative premium flow — 3 net-bearish sessions = thesis decay.
- [ ] On a 1255 break: require **two daily closes hold** before adding (L-0001).
- [ ] Trail stop to breakeven after T1 (1255).
- [ ] Watch 07-17 OPEX (put-heavy, pin pull toward 1040) and 07-29 FOMC.
- [ ] Refresh `/stock-deep-dive MU` if the reused flow ages > 10 sessions.

## 10. Reasoning-ledger lessons applied

- **L-0001** — the 1255 aggressive breakout uses a close-confirmation trigger + starter until two closes hold (no anticipatory full size).
- **L-0002** — flow & chart-trend are aligned (not divergent), so no hard-neutral; the timing-divergence is logged as the top reason_against and keeps spot token.
- **L-0004** — respect CROWDED_LONG + the CAUTION gates + the bear's distribution point: no full directional size at spot; defined-risk only on counter-trades.

## Citations (≥3, what the eval will spot-check)

1. [FLOW:insights_deep_dive] net +$279M, call premium 2.79x put, self-pctile 98.1 — `research/MU/2026-06-25/phase-1-flow.md`
2. [DP:block_stratified] mega buy_ratio 0.47 (balanced/distributive) — `research/MU/2026-06-25/phase-2-dark-pool.md`
3. [STRUCT:max_pain] near-expiry max-pain 1040 (−14.5%); GEX positive, DEX +$30.5B — `research/MU/2026-06-25/phase-4-structure.md`
4. [CHART:high_52w]/[CHART:bb_upper] spot 1213.56 = ATH, upper band 1212.18; ATR14 95.41 — `chart.json`
5. [FUND:fwd_pe] fwd P/E 8.4, PEG 0.05, 4/4 beats — `research/MU/2026-06-25/phase-7b-fundamentals.md`
6. [HIST:signal_backtest] bullish_flow win-rate 0.60 (n=5) — `research/MU/2026-06-25/phase-5-historical.md`

---
*Run `/trade-plan-eval MU 2026-06-26` after taking the trade so the reasoning ledger learns from the outcome.*
