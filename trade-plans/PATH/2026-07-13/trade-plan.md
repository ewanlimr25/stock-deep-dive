# Trade Plan — PATH

**As-of date:** 2026-07-13
**Spot reference:** 11.85 (chart engine, yfinance close) / 11.87 (deep-dive spot_reference)
**Voice:** desk PM running an institutional book
**Built from:** `research/PATH/2026-07-13/` (same-day deep dive, age 0 sessions) + chart engine (yfinance, 373 sessions)

> *For research and educational use only. Not financial advice. Sizing,
> structures, targets and dates are illustrative.*

## 0. Information completeness (gap audit)

- **Verdict:** SUFFICIENT — completeness 94%
- **Have:** options flow, dark pool, OI/positioning, dealer GEX/DEX, macro/sector, fundamentals, sentiment/short-interest, OHLCV chart (373 sessions) + S/R + fib + ATR, implied move, event calendar, earnings date
- **Missing / how to source:**

  | Item | Severity | How to source |
  |------|----------|---------------|
  | Empirical win-rate for the dark-pool-accumulation signal class (Kelly p) | important | `uw historical signal-backtest --signal-type dark_pool_accumulation` — returned `total_signals: 0` twice on 2026-07-13; no history for this class yet. Size from the conviction bin, never above starter, until it accrues. |
  | 07-09 block attribution (fresh accumulation vs offering / index cross / 13D) | nice_to_have (but the thesis's #1 risk) | SEC EDGAR watch for 13D/13G/S-3/424B after 2026-07-09; daily `uw dark-pool block-stratified` to confirm large-tier buy_ratio > 0.55 |
  | Intraday tape at execution | nice_to_have | `uw options-flow sweeps` + `uw dark-pool largest` the morning of entry |

## 1. Direction & conviction

- **Bias:** LONG
- **Conviction (M-01 bin):** 0.55 — floor bin; adjustment trail in `phaseA3-confluence.md`
- **Horizon:** 1–4w
- **Confluence score:** 45 (mixed — deep-dive phase-10; flow lanes capped by BUSY_NAME_NORMAL_DAY, −5 debate, −5 sentiment)
- **Flow ↔ chart agreement:** **FLOW-LEADS** — DP accumulation is defending 11.80 while price consolidates *under* the 12.34–12.35 range→trend trigger; chart supports but hasn't confirmed

### Thesis

An unattributed institution lifted 54.6M sh / $644M at the ask (buy_ratio 1.000, ~15× PATH's darkpool record) on 07-09 and kept buying into 07-13, building a $678.8M shelf at $11.80 [DP:block_stratified][DP:price_levels] under a name that is 28–32% of float short [SENT:short_float] — squeeze-loaded, and the chart has now turned with it (+24.7% off twice-defended 9.87/9.88 lows, first higher-high 12.31, MACD bullish [CHART:trend]). But the block moved price zero, insiders are net sellers, and the adversarial debate did NOT clear the trade (bear_residual 0.65 ≥ bull 0.65 [DEBATE:disconfirmed]) — so this is a floor-bin, starter-size long off the defended shelf, expressed defined-risk, with the add reserved for a volume-confirmed break of 12.35.

### Why it should work

1. **The shelf is defended with real money** — 07-09 mega block at the ask + continuation buying 07-13 at 61%; $678.8M sitting at the exact entry level. Falsifiable: large-tier buy_ratio < 0.45 or daily close < 11.60. [DP:block_stratified] [DP:price_levels]
2. **Squeeze asymmetry above the trigger** — 28–32% SI, ~5 days-to-cover, crowd CROWDED_SHORT; above 12.35 the marginal buyer is a covering short. [SENT:short_float]
3. **The chart now agrees** — impulse off equal lows, HH at 12.31, MACD bullish, RSI 60.9 with headroom, 1.47× volume, price > sma20/50, ema9 > ema21. [CHART:trend] [CHART:macd]
4. **Mechanical floor stack** — long-gamma + positive DEX dealer bid; $11 pin/max-pain and $10 put wall beneath the shelf. [STRUCT:gex] [STRUCT:max_pain] [OI:put_wall]
5. **Macro mild tailwind** — Fed easing (DFF 3.62%), tech inflow ALIGNED, live AI catalyst, no offering/13D filed as of 07-13. [MACRO:DFF] [MACRO:UiPath_2026-07-09]

### Why it may fail (the honest other side)

1. **STEELMAN: the block may be exit liquidity, not demand.** $644M that moved price zero over 4–5 sessions while insiders sold 9.6M sh reads as supply-absorption (unannounced secondary / index cross). The debate did not clear it — bear_residual 0.65 ≥ bull 0.65. Watch: any 13D/13G/S-3/424B attribution, or buy_ratio < 0.45 → thesis dead. [DEBATE:disconfirmed] [FUND:insider_MSPR] [HIST:trend]
2. **Options flow does not confirm** — net premium −$167k, sweep persistence mixed, and the most persistent theme is $12 Jan-28 put buying at the ask. No upside campaign in the options tape. [FLOW:phase-1]
3. **The upside is pre-sold** — $12 call wall (+1.1%), triple-confirmed $13 gamma wall with covered-call writing on the bid; long-gamma dampens the squeeze inside the $11–$13 box. [OI:smart_positioning] [STRUCT:gex]
4. **No fundamental/trend endorsement** — fundamentals CAUTION, consensus HOLD (UBS PT $12 — below T2), price under sma200 (12.95) in a TRANSITIONAL regime at 33.8% breadth. [FUND:phase-7b] [SENT:recommendation] [CHART:ma_stack] [MACRO:MarketRegime_2026-07-13]
5. **Violent downside tail** — below 11.60/11.80 there is no OI support until $10; 32% SI becomes an accelerant into 9.87–10 (−15%). [OI:put_wall] [CHART:swing_low]

## 2. Levels to watch

| Level | Role | Source | Note |
|-------|------|--------|------|
| 12.95–13.28 | target T2 / fade | [CHART:sma200] + [STRUCT:gex $13] + [CHART:fib_0.618 13.09] + [CHART:sr 13.28] | 4-way supply zone; deep dive's fade/no-new-longs zone |
| 12.34–12.35 | trigger / target T1 | [CHART:sr 5-touch] + [CHART:fib_0.500] + BB upper 12.28 | range→trend on daily close > 12.35, vol > 1.2× avg |
| 12.15–12.17 | resistance | [DP:blocks 07-13] | first overhead from continuation prints |
| **11.80** | entry / support | [DP:price_levels] + [CHART:spot/ema9] | the $678.8M institutional shelf — the trade |
| 11.60 | signal stop (close basis) | [DP:invalidation, deep dive] | daily close below = shelf failed |
| 11.42 / 11.29 | support | [CHART:sr 4 & 6 touches] + 0.382 of Jun→Jul leg | structural net under the shelf |
| 11.28 | hard stop | [CHART:sr 11.29] | below the 6-touch support; 0.80 ATR from entry |
| 11.05–11.00 | pin | [CHART:sr] + [OI:pin] + [STRUCT:max_pain Jul-17] | OPEX magnet if shelf fails |
| 10.48–10.69 | support | [CHART:sr] + [CHART:fib_0.236] | above the $10 put wall [OI:put_wall] |
| 9.87–9.88 | base lows | [CHART:swing_low ×2] | twice-defended; the tail |
| 5.70 | gamma flip | [STRUCT:gex] | long-gamma confirmation only — not a near-term level |

Moving averages: sma50 10.91 · sma200 12.95 · ema21 11.20 [CHART:ma].
Fib (15.50→9.20 swing): 0.382 = 11.61 · 0.500 = 12.35 · 0.618 = 13.09 · 0.786 = 14.15 [CHART:fibonacci].

## 3. Patterns forming (chart)

| Pattern | Direction | Confidence | Measured target | Invalidation | Note |
|---------|-----------|-----------|-----------------|--------------|------|
| — engine: **none detected** | — | none | — | — | all 6 detectors clean (`patterns_detected: []`); no Elliott count (pivots not alternating) [CHART:patterns] |
| double-bottom-*like* equal lows (manual observation, NOT a pattern call) | bullish | none | none claimed | 9.87 | 9.88/9.87 equal lows but no intervening neckline pivot — engine correctly rejects; value is invalidation architecture only [CHART:swing_low] |

Per `pattern-rubric.md`: no pattern is forced onto noise; targets in this plan
come from level/fib confluence, not pattern measured-moves.

## 4. Upcoming events that move the tape (next ~30–60d)

| Date | Event | Impact | Source |
|------|-------|--------|--------|
| 2026-07-15 | CPI (June print, approx.) | ? | [MACRO:phase-6] |
| 2026-07-17 | July monthly OPEX — Jul-17 max-pain $11 | − (mild pin toward $11 into Friday, releases after) | [STRUCT:max_pain] |
| 2026-07-29 | FOMC (approx.) | ? | [MACRO:phase-6] |
| ongoing | AI-automation product news (Maestro Case AI momentum) | + | [MACRO:UiPath_2026-07-09] |
| any day | **07-09 block attribution filing (13D/13G/S-3/424B)** — the thesis hinge | ? | [DP:open_question] / SEC EDGAR |
| 2026-09-03 | PATH earnings — **outside horizon**; Aug-21 expiries avoid it | ? | [MACRO:phase-6] |

Expected front-expiry move ±5.3% (±$0.63) [CTX:implied_move] · IV rank 40.4 ·
VRP +0.084 (options rich → prefer structures that sell some premium) [HIST:phase-5].

## 5. Invalidation

- **Price-based:** daily close **< 11.60** → the shelf failed; exit stock, honor spread max-loss discipline. Hard disaster stop 11.28 (gap protection). Structural backstop: 11.29 was touched 6 times — a close through it confirms.
- **Signal-based:** large-tier DP buy_ratio **< 0.45**, or the 07-09 block attributes as supply (secondary / 13D distribution filing).
- **Macro-based:** hawkish FOMC / 10y > ~4.8% compressing software multiples; breadth deteriorating below 33.8% into risk-off.

## 6. Sizing (% of book risk, NOT dollars)

- **Kelly p:** p_raw = 0.55 (win_rate_source = **fallback_bin**; phase-5 backtest `total_signals: 0`, n=0) → fallback cap ≤ 0.65 respected → **p = 0.55**
- **Inputs:** b = 1.67 (entry 11.80, hard stop 11.28, blended target 12.67 = 50% × 12.34 + 50% × 13.00), fraction = 0.25, cap_pct = 5
- **Raw Kelly:** (0.55 × 1.67 − 0.45) / 1.67 = **0.28** → quarter-Kelly 7.0% → cap 5%
- **Win-rate map ceiling:** p 0.55 ∈ [0.50, 0.70) → **half (≤ 2.5%)**
- **Risk gates (each can only cut):** fundamentals **CAUTION** · sentiment **CAUTION** / crowd **CROWDED_SHORT** · correlation n/a (no concurrent positions) · rotation aligned (no cut) · **debate DISCONFIRMED → one size-step cut** · context BUSY_NAME_NORMAL_DAY (no top-of-band) · regime TRANSITIONAL → half-size guidance [MACRO:MarketRegime_2026-07-13]
- **Final size: 1.0% of book risk** — starter (matches the deep dive's `final_size_pct`). Deviation from raw Kelly documented by the gate trail above.
- **Total-thesis cap:** stock + options combined ≤ 1.0% book risk. Take the stock plan OR the options pair at half-weight each — not both at full.

## 7. Plan A — pure stock (long)

- **Direction:** long
- **Entry:** 11.80 (limit at the shelf) — trigger: shelf-hold — large-tier DP buy_ratio ≥ 0.55 continuing and no daily close < 11.60 while working. **Add tranche** (per L-0001): only on a daily close > 12.35 on >1.2× avg volume, starter until two closes hold above.
- **Stop:** 11.28 hard (below the 6-touch 11.29 support, 0.80 ATR) — with a **close-based signal exit at 11.60** that fires first in an orderly tape
- **Targets:** T1 **12.34** (5-touch resistance + fib 0.500, take 50%) · T2 **13.00** (gamma wall / sma200 / fib 0.618 supply zone, take 50%)
- **Reward:risk to T1:** 1.04 (off the hard stop; 2.7 off the 11.60 close-exit)
- **Size:** 1.0% book risk
- **One-liner:** Long the $678.8M institutional shelf at 11.80 with a 32%-SI squeeze kicker, starter size until the 12.35 range trigger breaks on volume; dead on a close below 11.60 or DP bid withdrawal.

## 8. Plan B — options (both with target date + target price)

### B1 — directional: call debit spread 12/13, 2026-08-21

- **Structure:** call debit spread (long 12C / short 13C)
- **Strikes / expiry:** 12/13 / 2026-08-21
- **Target date / target price:** **2026-08-07** / **12.95** (underlying)
- **Debit · breakeven · max loss:** 0.35 · 12.35 · 0.35
- **Est. payoff at target:** ≈ 0.78 spread value at 12.95 on 08-07 (≈ +0.43, ~2.2× debit; 0.95 intrinsic if held to expiry at 12.95)
- **Size:** 0.5% book risk
- **Why this structure:** short $13 leg sells the triple-confirmed gamma wall / covered-call cap [STRUCT:gex] to fund the long — sells the level the trade is likely to stall at, and selling the wall offsets the +0.084 VRP richness. Breakeven 12.35 = exactly the range→trend trigger. Target +9.3% from spot vs a ±5.3% front-expiry priced move scaling to ~±10% over the 4-week window — inside 1.5× the priced move, not rich. Expiry 08-21 clears the 09-03 earnings binary; CPI 07-15 / FOMC 07-29 sit inside the window as market-level risk (mitigated by defined-risk + starter size).

### B2 — defined-risk: put credit spread 11/10, 2026-08-21

- **Structure:** put credit spread (short 11P / long 10P)
- **Strikes / expiry:** 11/10 / 2026-08-21
- **Target date / target price:** **2026-08-21** (expiry, theta play) / **11.85** (underlying holds ≥ the shelf; full credit at ≥ 11.00)
- **Credit · breakeven · max loss:** −0.31 · 10.69 · 0.69
- **Est. payoff at target:** +0.31 (full credit)
- **Size:** 0.5% book risk
- **Why this structure:** gets paid to defend the shelf — short $11 sits on the OI pin/max-pain strike above the $10 put wall [OI:pin][OI:put_wall]; long $10 caps the 32%-SI short-cascade tail; breakeven 10.69 = fib 0.236 with the 10.48 4-touch support above it [CHART:fib_0.236]. Aligns with the premium-selling VRP read [HIST:phase-5].

## 9. Post-entry monitoring checklist

- [ ] Daily: `uw dark-pool block-stratified --symbol PATH` — exit signal if large-tier buy_ratio < 0.45
- [ ] SEC EDGAR / news: any 13D/13G/S-3/424B attributing the 07-09 block → re-underwrite immediately (bullish if activist 13D; exit if offering/distribution)
- [ ] 2026-07-15 CPI & 2026-07-29 FOMC: no adds day-of; check 10y vs ~4.8% after
- [ ] 2026-07-17 OPEX: expect $11-ward pin pressure into Friday; don't confuse it with shelf failure — the signal is the *close*, not the intraday flush
- [ ] On daily close > 12.35 with >1.2× volume: add per L-0001 (starter until two closes hold); trail stock stop to 11.78 (breakeven-ish) after T1 fills
- [ ] If flow goes stale (no refresh by ~2026-07-27, 10 sessions): re-run `/stock-deep-dive PATH` before sizing up (L-0003)

## 10. Reasoning-ledger lessons applied

- **L-0001** (ACTIVE): the 12.35 breakout add requires a volume-confirmed close and stays starter until two closes hold — anticipatory full size on an unconfirmed break is the most common avoidable loss.
- **L-0002** (ACTIVE): checked — read is FLOW-LEADS (chart agrees directionally), not DIVERGENT → directional trade permitted; would have forced NEUTRAL/defined-risk-only.
- **L-0003** (ACTIVE): checked — deep dive is same-day (0 sessions) → no staleness cut; re-check threshold noted in §9.
- **L-0004** (CANDIDATE): pattern not matched (long-gamma book, LONG bias, no bearish-sweep campaign) — noted only.

## Citations (what the eval will spot-check)

1. [DP:block_stratified] — 2026-07-09 mega block 54.6M sh / $644.2M, buy_ratio 1.000, zero sell — `research/PATH/2026-07-13/phase-2-dark-pool.md` §verdict
2. [DP:price_levels] — $678.8M / 57.5M sh shelf at $11.80; 07-13 continuation 61% buy — `phase-2-dark-pool.md`
3. [CHART:support_resistance] — 12.34 resistance (5 touches, last 2026-07-07) + [CHART:fib_0.500] 12.35 — `chart.json`
4. [STRUCT:gex] — $13 gamma wall (triple-confirmed w/ phase-3 call wall + covered calls), ZGL 5.70, long-gamma — `phase-4-structure.md` §verdict
5. [SENT:short_float] — 28–32% of float short, ~5 days to cover, CROWDED_SHORT — `phase-7c-sentiment.md`
6. [DEBATE:disconfirmed] — bull_residual 0.65 / bear_residual 0.65 → disconfirmed true; strongest bear point = price-inert block + insider selling — `phase-8b-debate.md`
7. [HIST:signal_backtest] — `total_signals: 0` (×2 runs) → win_rate_source fallback_bin — `phase-5-historical.md`
8. [CHART:swing_low] — equal lows 9.88 (06-18) / 9.87 (06-26); [CHART:atr14] 0.65 — `chart.json`

---
*After taking any of these trades, run `/trade-plan-eval PATH 2026-07-13` so the reasoning ledger learns from the outcome.*
