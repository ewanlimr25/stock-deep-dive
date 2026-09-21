# Phase A3 — Confluence: Direction, Reasons, Levels, Events

Fuses `research/PATH/2026-07-13/` (flow substrate, same-day) with `chart.json` /
`phaseA2-chart.md` (price layer). Gap-audit verdict: SUFFICIENT (no ceiling cut).

## Step 1 — directional lane tally

| Lane | Vote | Evidence |
|------|------|----------|
| Flow (A1) | **NEUTRAL** | net_flow −$167k, sweep-persistence *mixed*, no smart-money campaign; dominant theme = $12 Jan-28 LEAP put buying (hedge-consistent) [FLOW:phase-1 verdict, 2/5] |
| Dark pool (A2) | **LONG** | mega block buy_ratio 1.000 (54.6M sh / $644M), $678.8M shelf @ 11.80, buying continued 07-13 at 61% [DP:block_stratified, DP:price_levels, 4/5] |
| Positioning (A3) | **LONG (capped)** | 43% of OI in call-heavy Jan-27 LEAPs, $18C build; but $12 call wall + $13 covered-call writing caps near-term [OI:term_structure, 3/5] |
| Dealer (A4) | **LONG (mild)** | long-gamma, positive DEX = mechanical dealer bid; mean-reversion box $11–$13 [STRUCT:gex/dex, 3/5] |
| Historical (A5) | **NEUTRAL** | backtest empty (n=0), 90d flow a coin-flip, price inert vs the block [HIST:signal_backtest, 2/5] |
| Chart trend (B3) | **LONG** | +24.7% leg off equal lows 9.87/9.88, HH 12.31, MACD bullish, RSI 60.9, >sma20/50 — but <sma200, `range_or_transition` [CHART:trend, 3/5] |
| Chart pattern (B4) | **NEUTRAL** | zero patterns detected; no Elliott count [CHART:patterns] |
| Macro/sector (C1) | **NEUTRAL, long lean** | Fed easing + tech inflow (ALIGNED, persistence 1) vs TRANSITIONAL regime, breadth 33.8% [MACRO:phase-6, 3/5] |

**Tally: LONG 4 · NEUTRAL 4 · SHORT 0 → bias = LONG** (plurality; zero short votes).
Fundamentals (CAUTION), sentiment (CAUTION/CROWDED_SHORT) and debate
(disconfirmed) are cut-only gates — applied in Step 3.

## Step 2 — flow ↔ chart agreement: **FLOW-LEADS**

The directional flow signal (DP accumulation defending 11.80) is ahead of the
chart: price is consolidating **under the 12.34–12.35 range→trend trigger**
[CHART:support_resistance + CHART:fib_0.500], below the sma200 (12.95), structure
still `range_or_transition`. The chart *supports* (up-leg, momentum bullish — this
is a strong flow-leads, not a divergent one) but has **not confirmed**. Textbook
"accumulation under resistance, base not yet broken."

**Not DIVERGENT** — no lane votes short — so ledger **L-0002 does not bind**.
Consequences of FLOW-LEADS: anticipatory entry only at the *defended* level
(the shelf), −1 conviction bin until the chart confirms (close > 12.35), and the
12.35-break add-on follows **L-0001** (volume-confirmed break, starter until two
closes hold).

## Step 3 — conviction bin (adjustment trail)

| Step | Input | Effect | Running bin |
|------|-------|--------|-------------|
| Confluence band | deep-dive confluence_score **45** (mixed; flow phases capped `+` by BUSY_NAME_NORMAL_DAY; −5 debate, −5 sentiment already embedded) | floor band | **0.55** |
| 1. Agreement modifier | FLOW-LEADS → −1 bin | already at floor bin; cannot go lower — noted, absorbed by starter sizing | 0.55 |
| 2. Risk gates | fundamentals CAUTION, sentiment CAUTION, crowd CROWDED_SHORT, rotation aligned, **debate disconfirmed** (bear_residual 0.65 ≥ bull 0.65) | cut-only; at floor → enforce **starter size step** (deep dive already cut size to 1%) | 0.55 |
| 3. Context modifier | BUSY_NAME_NORMAL_DAY | no top-of-band (moot at floor) | 0.55 |
| 4. Staleness | deep dive age 0 sessions | no cut (L-0003 not triggered) | 0.55 |
| 5. Gap audit | SUFFICIENT | no cut | **0.55** |

**Conviction = 0.55 (floor bin), bias LONG, horizon 1–4w.** Kelly p = 0.55
(conviction-bin fallback, win_rate_source null; fallback cap 0.65 respected).
Sizing map: p 0.50–0.70 → ≤ half-cap, then debate one-step cut + TRANSITIONAL
half-size guidance → **starter 1.0%** (matches upstream `final_size_pct`).

## Step 4 — the two-sided case

### reasons_for

1. **The shelf is being defended with real money.** 54.6M sh / $644M lifted at
   the ask (buy_ratio 1.000, ~15× PATH's darkpool record) on 07-09, a $678.8M
   shelf at **11.80**, and continuation buying 07-13 at 61% — an institution is
   absorbing supply at the exact entry level. Falsifiable: large-tier buy_ratio
   < 0.45 or a close below 11.60. [DP:block_stratified] [DP:price_levels]
2. **Squeeze asymmetry above the trigger.** 28–32% of float short (~5 days to
   cover), crowd_state CROWDED_SHORT — above 12.35 the marginal buyer is a
   covering short. Falsifiable: break of 12.35 on volume that fails to follow
   through. [SENT:short_float] [CHART:fib_0.500]
3. **The chart now agrees directionally.** +24.7% impulse off twice-defended
   equal lows (9.88/9.87), first higher-high at 12.31, MACD bullish, RSI 60.9
   with headroom, 1.47× volume, price above sma20/50 with ema9>ema21.
   [CHART:trend] [CHART:macd] [CHART:swing_low]
4. **Mechanical floor stack under the trade.** Long-gamma + positive DEX dealer
   bid, $11 pin/max-pain and the $10 put wall beneath the 11.80 shelf — three
   independent nets before the 9.87 lows. [STRUCT:gex] [STRUCT:max_pain] [OI:put_wall]
5. **Macro is a mild tailwind, not a headwind.** Fed easing (DFF 3.62%), durable
   tech inflow (ALIGNED, persistence 1), live AI catalyst (Maestro Case AI day
   +3.33%) with **no offering/13D filed** as of 07-13. [MACRO:DFF] [MACRO:UiPath_2026-07-09]

### reasons_against

1. **STEELMAN [DEBATE:disconfirmed]: the block may be exit liquidity, not demand.**
   A $644M print that moved price **zero** over 4–5 sessions, while insiders sold
   9.6M shares (MSPR −100), reads as supply-absorption — an unannounced secondary
   placement or index cross. The adversarial pass did NOT clear the trade
   (bear_residual 0.65 ≥ bull_residual 0.65). **Watchable trigger:** a 13D/13G/
   S-3/424B filing attributing the block as supply, or large-tier buy_ratio
   < 0.45 → thesis dead (reappears in invalidation). [DP:block_stratified]
   [HIST:trend] [FUND:insider_MSPR]
2. **Options flow does not confirm the equity flow.** Net premium −$167k (bearish
   tilt), sweep persistence *mixed*, and the most persistent options theme is
   ATM $12 Jan-28 **put** buying at the ask. Even read as hedging, there is no
   upside campaign in the tape. [FLOW:phase-1]
3. **The upside is pre-sold.** $12 call wall one strike overhead (+1.1%), $13
   gamma wall triple-confirmed with covered-call writing *on the bid* — someone
   large is selling exactly the move this trade needs; long-gamma dampens the
   squeeze mechanics inside the $11–$13 box. [OI:smart_positioning] [STRUCT:gex]
4. **No fundamental or trend endorsement.** Fundamentals CAUTION, consensus HOLD
   (UBS PT $12 — *below* the T2 target zone), price still under the sma200
   (12.95) in a TRANSITIONAL regime at 33.8% breadth (half-size guidance).
   [FUND:phase-7b] [SENT:recommendation] [CHART:ma_stack] [MACRO:MarketRegime_2026-07-13]
5. **The downside tail is violent.** If 11.80/11.60 fails, 32% SI flips from fuel
   to accelerant and there is no OI support until $10 — air pocket to the 9.87–10
   zone (−15%). [OI:put_wall] [CHART:swing_low] (reappears in invalidation)

## Step 5 — level ladder (dual-confirmed levels bolded)

| Role | Level | Sources |
|------|-------|---------|
| Target T2 / fade zone | **12.95–13.28** | [CHART:sma200 12.95] + [STRUCT:gex $13 wall] + [CHART:fib_0.618 13.09] + [CHART:sr 13.28] — 4-way |
| Target T1 / trigger | **12.34–12.35** | [CHART:sr 12.34, 5 touches] + [CHART:fib_0.500 12.35] + BB upper 12.28; range→trend trigger on daily close > 12.35, vol > 1.2× |
| Near overhead | 12.15–12.17 | [DP:blocks 07-13 prints] |
| Entry / defense | **11.80–11.85** | [DP:price_levels $678.8M shelf] + [CHART:spot/ema9 hold] |
| Support 1 | 11.42 / **11.29** | [CHART:sr 4 & 6 touches] + 0.382 retrace of the 9.87→12.31 leg (11.38) |
| Support 2 / pin | **11.05–11.00** | [CHART:sr 11.05] + [OI:pin $11] + [STRUCT:max_pain Jul-17 $11] |
| Support 3 | 10.48–10.69 | [CHART:sr 10.48] + [CHART:fib_0.236 10.69]; $10 put wall below [OI:put_wall] |
| Base lows | 9.87–9.88 | [CHART:swing_low ×2] |
| gamma_flip | 5.70 | [STRUCT:gex] (long-gamma confirmation only, not a near-term level) |
| largest_pin | 11.00 | [OI:pin] [STRUCT:max_pain] |

Stops (A4 picks per structure): signal stop **11.60** (deep-dive invalidation,
below the shelf) ≈ 1-ATR zone [CHART:stops long_stop_1atr 11.20 / 1.5-ATR 10.88];
structural stop **11.29** (6-touch support). ATR 0.65/day — stops tighter than
~0.5 ATR are noise.

## Event calendar

| Date | Event | Impact | Source |
|------|-------|--------|--------|
| 2026-07-15 | CPI (June print, approx.) | ? (market-level, rates read-through) | [MACRO:phase-6] |
| 2026-07-17 | July monthly OPEX — $11 max-pain expiry | − near-dated (mild downward pin toward $11 into Friday, releases after) | [STRUCT:max_pain] + third-Friday |
| 2026-07-29 | FOMC (approx.) | ? (easing-path signal; hawkish = invalidation lane) | [MACRO:phase-6] |
| ongoing | AI-automation product news (Maestro Case AI momentum) | + idiosyncratic, can exceed ±5.3% | [MACRO:UiPath_2026-07-09] |
| any day | **07-09 block attribution** (13D/13G/S-3/424B) | binary ± — the thesis hinge | [DP open question]; SEC EDGAR watch |
| 2026-09-03 | PATH earnings | binary — **outside horizon**; Aug-21 expiries avoid it | [C6] [MACRO:phase-6] |

Expected front-expiry move ±5.3% (±$0.63) [CTX:implied_move]; IV rank 40.4;
VRP +0.084 (options rich → structures should *sell* premium where possible)
[HIST:phase-5].

## Invalidation (deep-dive rubric, carried forward)

- **price:** daily close **< 11.60** → shelf failed; no OI support until $10;
  exit stock, spreads at max-loss discipline. Structural backstop 11.29.
- **signal:** large-tier DP buy_ratio **< 0.45**, or the 07-09 block attributes
  as supply (secondary/13D distribution filing).
- **macro:** hawkish FOMC / 10y > ~4.8% compressing software multiples, or
  breadth < 33.8% into risk-off.

## Ledger lessons applied

- **L-0001** (ACTIVE): binds the 12.35 breakout *add* — volume-confirmed close,
  starter until two closes hold. Applied to A4 entry style.
- **L-0002** (ACTIVE): checked — read is FLOW-LEADS, not DIVERGENT → does not bind.
- **L-0003** (ACTIVE): checked — age 0 sessions → not triggered.
- **L-0004** (CANDIDATE): pattern not matched (long-gamma book, LONG bias).

## Verdict for downstream (A4)

- bias **LONG** · conviction **0.55** · horizon **1–4w** · agreement **FLOW-LEADS**
- Entry style: shelf-hold primary (11.80–11.85), breakout add only per L-0001
- Size ceiling: **starter 1.0%** (floor bin + debate cut + TRANSITIONAL half-size)
- reasons_for ×5, reasons_against ×5 as above; invalidation block as above
