# Trade Plan — ELF

**As-of date:** 2026-06-30
**Spot reference:** $74.00 (yfinance, 373 sessions)
**Voice:** desk PM running an institutional book
**Built from:** `research/ELF/2026-06-30/` deep dive (age 0 days) + chart engine (yfinance)

> *For research and educational use only. Not financial advice. Sizing,
> structures, targets and dates are illustrative.*

## 0. Information completeness (gap audit)

- **Verdict:** **SUFFICIENT** — completeness **100%**
- **Have:** options flow/LEAP, dark-pool accumulation ladder, 25-day OI build, dealer GEX/ZGL, historical win-rate, OHLCV chart + patterns (cup&handle, elliott), macro/sector rotation, event calendar, fundamentals (CONFIRM), sentiment/short interest, implied/expected move + VRP, earnings date (~Aug-5, cadence-robust after the Jul-31 expiry).
- **Missing / how to source:**
  | Item | Severity | How to source |
  |------|----------|---------------|
  | Exact Q1 FY2027 earnings day (Aug-5 vs 6/7) | nice_to_have | ELF IR / `finnhub_enrich.py` — any early-Aug date is safely after Jul-31 |
  | Leverage detail (debt/equity) + cash-flow statements | nice_to_have | paid-tier Finnhub; proxied HAVE (current ratio 2.35, gross margin 70.7%) |
  | Live intraday tape for same-day dip-buy timing | nice_to_have | `uw options-flow sweeps --symbol ELF --json` + `uw options-structure gex --symbol ELF --dte-max 45 --json` morning-of |

## 1. Direction & conviction

- **Bias:** **LONG** (bounded dip-buy)
- **Conviction (M-01 bin):** **0.55**
- **Horizon:** 1–4w
- **Confluence score:** 48
- **Flow ↔ chart agreement:** **CONFLUENT** (flow + chart both bullish; both flag the same extended-entry caution)

### Thesis (≤3 sentences, ≥3 tagged citations)

ELF is an insider- and OI-confirmed **turnaround** — 25 consecutive OI-build days +127,955 [HIST:oi-trend], June MSPR +44.1 [FUND:insider-sentiment], a $45 Jan-2028 delta-0.85 LEAP [FLOW:sweeps], a DP accumulation ladder (large buy_ratio 0.61) [DP:price_levels] — that the chart **confirms** (uptrend HH/HL off 48.82, cup&handle toward ~84 [CHART:market_structure][CHART:cup_handle]). But it has run **+34.9%/30d into a long-gamma dealer cap** (ZGL $59.97, walls $70/$75, max-pain $59–63 below spot [STRUCT:gex]) and is **overbought** (RSI 72.7, fib 0.5), with the debate DISCONFIRMED to a range. So this is a **real but bounded long**: a small defined-risk **DIP-BUY at $68–71 / $59–65 with capped $75–80 targets — NOT a chase of $74.**

### Why it should work
- **Insider + OI-confirmed turnaround** — 25 straight OI-build days +127,955, June MSPR +44.1, a $45 Jan-2028 delta-0.85 LEAP; conviction the bear concedes it cannot short [HIST:oi-trend][FUND:insider-sentiment][FLOW:sweeps].
- **DP accumulation ladder** — large buy_ratio 0.61; institutions bought *into* the run at $64–65/$67/$70 [DP:price_levels].
- **Long-gamma dealer buffer** — ZGL $59.97; dealers buy dips, so the $68–71 and $59–65 shelves are defended (favorable for a *dip*-buy) [STRUCT:gex].
- **Chart confirms direction** — uptrend HH/HL, above rising sma20/50, MACD bullish, cup&handle target ~84 [CHART:market_structure][CHART:cup_handle].
- **Squeeze fuel + soft catalyst** — 12.7% residual short + haircare rollout (rhode +80% YoY, Raymond James Strong Buy $85 PT) can power a confirmed break of the $75 wall [SENT:short_float][MACRO:ELF_catalyst].
- **Sector tailwind** — Consumer Defensive persistent INFLOW (persistence 1.0) [MACRO:sector_flow_persistence].

### Why it may fail (the honest other side)
- **STRONGEST STEELMAN** — **structurally-capped, partly-technical rally**: long-gamma $75 cap + max-pain $59–63 **below** spot = no upside magnet, and part of +34.9%/30d was **short-covering** (SI 15.9%→12.7%, non-recurring); the debate disconfirmed to "buy dips, fade $75, don't chase" [STRUCT:gex][SENT:short_float][DEBATE].
- **Extended/overbought entry** — RSI 72.7, at fib 0.5 (73.16), BB upper, Elliott wave-5 target met → chasing $74 has mean-reversion risk (L-0001) [CHART:rsi14][CHART:elliott_wave].
- **Valuation** — P/E ~166x on trough earnings (net margin 1.6%); the multiple bets on margin recovery delivering [FUND].
- **90d net premium is bearish (−$9.5M)** — the longer-term flow undertone contradicts the recent OI build; watchable: cum-premium net-bearish 3 sessions [HIST:cumulative-premium-flow].
- **Regime** — TRANSITIONAL + hawkish Fed dots (3.8%) into a high-beta (1.59) name [MACRO:FOMC][MACRO:MarketRegime].
- **Cliff-like hard stop** — a loss of **ZGL $59.97** flips dealers short-gamma → the buffer becomes an accelerant [STRUCT:gex].

## 2. Levels to watch

| Level | Role | Source | Note |
|-------|------|--------|------|
| 84.0 | target (stretch) | [CHART:sma200] | sma200 84.05 = cup target 84.29 |
| 77.82–79 | resistance | [CHART:cluster] | 3-touch + fib 0.618 78.91; upper cap toward $80 |
| 75.0 | cap / breakout trigger | [STRUCT:gex] | $75 gamma wall +681k; add only on a confirmed close (>1.2× vol, L-0001) |
| 73.16 / 74 | half-retrace (spot) | [CHART:fib_0.5] | fib 0.5 decision zone — don't chase |
| 68–71 | **primary dip-buy** | [STRUCT:gex] | $70 gamma wall +1.03M + 3-touch 70.84 + cup rim 68.4 + fib 0.382 67.42 |
| 64–65 | deep dip-buy | [DP:price_levels] | institutional shelf (tranche 2) |
| 59.97 | **HARD STOP (ZGL)** | [STRUCT:gex] | loss w/o reclaim = short-gamma flip; ~sma50 59.77 + max-pain 59–63 + fib 0.236 60.31 |

Moving averages: sma50 59.77 · ema21 63.0 · **sma200 84.05** (price below → recovery not yet repaired). Fib (swing 97.5→48.82): 0.236 **60.31** · 0.382 **67.42** · 0.5 **73.16** · 0.618 **78.91**.

## 3. Patterns forming (chart)

| Pattern | Direction | Confidence | Measured target | Invalidation | Note |
|---------|-----------|-----------|-----------------|--------------|------|
| cup & handle | bullish | low | 84.29 | 49.57 | rim 68.4 (reclaimed), target ≈ sma200; confirm by holding above rim / close > $75–77 (L-0001) [CHART:cup_handle] |
| Elliott impulse (wave-5 pending) | bullish (exhausting) | low | 71.57 (met) | — | 2/3 rules (wave-2 breached wave-1 origin); wave-5 target already met by $74 = up-leg **maturing** → reinforces don't-chase [CHART:elliott_wave] |

Both low-confidence and near-term opposed (continuation vs exhaustion); their agreement is that a **pullback to $68–71 is the high-value entry** and **~$84 (sma200) is the ceiling** of this leg. Neither sets the bias.

## 4. Upcoming events that move the tape (next ~30–60d)

| Date | Event | Impact | Source |
|------|-------|--------|--------|
| ~2026-07-02 | June ISM Mfg/Services + June jobs report | ? | [MACRO] |
| ~2026-07-14 | June CPI release | ? (hawkish = headwind) | [MACRO:CPIAUCSL] |
| 2026-07 (ongoing) | haircare rollout ramp (TikTok Shop → Target) | + | [MACRO:ELF_catalyst] |
| **~2026-08-05** | **ELF Q1 FY2027 earnings** (Jul-31 structures expire before it) | ? | [FUND:earnings] |

## 5. Invalidation

- **Price-based:** two daily closes below **$70** (first invalidation → trim tranche 50%); two daily closes below the **$64–65 shelf** (thesis broken); **intraday break of ZGL $59.97 with no reclaim (HARD STOP — short-gamma flip).**
- **Signal-based:** cum premium flow net-bearish 3 consecutive sessions (already 90d net-bearish −$9.5M), OR institutional-accumulation flips to distribution, OR conviction-matrix flips DIRECTIONAL_LONG → HEDGED_LONG.
- **Macro-based:** hawkish mid-July CPI surprise, OR regime flips TRANSITIONAL → RISK-OFF, OR July haircare sell-through disappoints.

## 6. Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.625** (n=**8**, src=backtest) → p = 0.625
- **Inputs:** b = **1.67**, fraction = 0.25, cap_pct = 5
- **Raw Kelly:** 0.625 − (0.375/1.67) = **+0.40** → fractional 10% → capped **5%** · **Win-rate map ceiling:** starter (N=8)
- **Risk gates (each can only cut):** fundamentals **CONFIRM** · sentiment **CAUTION** (short-covering non-recurring, P/E 166x) · correlation **none** · rotation **neutral** · debate **DISCONFIRMED** (bounds to dip-buy/range) · context **TRANSITIONAL → half-size; IV-rank 46.8 / VRP +0.081 mild PREMIUM_SELLING**
- **Final size:** **0.6% of book.** *Deviation:* the +0.40 Kelly → 5% cap is cut ~8× to 0.6% by TRANSITIONAL half-size + CAUTION + disconfirmed-debate cap + N=8 starter + the extended/overbought entry (dip-buy, not chase). Matches the deep dive (0.6%).

## 7. Plan A — pure stock (long, dip-buy)

- **Direction:** **long** (bounded dip-buy — **do not chase $74**)
- **Entry:** **$70** (TRANCHE 1: pullback to the $68–71 gamma/cup shelf holding above-mid; dealers buy dips in long-gamma). **TRANCHE 2 (deep add): $64–65.** Aggressive breakout-add ONLY on a confirmed daily close above **$75** on >1.2× vol + fresh OI (L-0001).
- **Stop:** **$66** (below the $68–71 shelf, ~1 ATR); **hard stop on a ZGL $59.97 loss.**
- **Targets:** T1 **$75** ($75 gamma wall / first cap, take 50%) · T2 **$80** (upper cap, take 30%) · T3 **$84** (sma200 / cup target, take 20%)
- **Reward:risk to T1:** **1.25R**
- **Size:** **0.6% book** (tranche 1)
- **One-liner:** Dip-buy the OI/insider-confirmed turnaround at the $68–71 shelf (scale deeper $64–65) — not chase $74; cap targets $75–80 (stretch $84); stop $66, hard stop on a ZGL $59.97 loss. A real but **dealer-capped** long, so R is modest (1.25) and the edge is in the entry.

## 8. Plan B — options (≥1 with target date + target price)

### B1 — directional (defined-risk)

- **Structure:** **call debit spread**
- **Strikes / expiry:** **72/78** / **2026-07-31**
- **Target date / target price:** **2026-07-24** / **$78** (underlying ≥ $78 caps the spread)
- **Debit/credit · breakeven · max loss:** debit **$2.00** · BE **$74.00** · max loss **$2.00**
- **Est. payoff at target:** **+$4.00** (spread max $6.00 width − $2.00 debit; ~2:1)
- **Why this structure:** straddles the $75 gamma/call wall (pin magnet), caps at $78 short of the $80 wall; **expires pre-earnings (Aug-5)** to dodge IV crush. Target $78 = +5.4% ≈ 1.5× the priced ±3.52% move — achievable on a haircare-catalyst/squeeze-through the $75 wall, rich if the range holds (hence defined-risk). [STRUCT:gex][SENT:short_float]

### B2 — defined-risk (income / bullish-neutral)

- **Structure:** **put credit spread**
- **Strikes / expiry:** **65/60** / **2026-07-31**
- **Target date / target price:** **2026-07-31** / **$70** (holds the shelf → both puts expire worthless)
- **Debit/credit · breakeven · max loss:** credit **$1.40** · BE **$63.60** · max loss **$3.60**
- **Est. payoff at target:** **+$1.40** (full credit if ELF ≥ $65 at expiry)
- **Why this structure:** sells the $64–65 institutional shelf into VRP +0.081 (premium-selling) + the long-gamma buffer; profits on the pin/consolidation the desk expects. Short strike $65 = −12% (well outside the ±3.52% move). Expires pre-earnings. [DP:price_levels][STRUCT:gex]

*Expected-move check:* front-expiry implied move ±3.52% / ±$2.61 to Jul-31. The call target ($78, +5.4%) is ~1.5× the priced move — needs the catalyst/squeeze-through, so it's expressed as a defined-risk *spread*, not a naked call. The put-credit short strike ($65, −12%) sits far outside the priced move (high probability of expiring worthless — the point of selling it). Both expire before the Aug-5 earnings.

## 9. Post-entry monitoring checklist

- [ ] **Do not chase** — only add on a pullback to $68–71 (or $64–65), or a *confirmed* $75 breakout close.
- [ ] Watch cum-premium flow — net-bearish 3 sessions (on the −$9.5M/90d undertone) = first exit signal.
- [ ] Track the $75 wall: rejection → trim/fade toward the shelf; confirmed close above on volume → add + raise stop.
- [ ] Refresh GEX/ZGL — a loss of **$59.97** flips short-gamma; be flat before that accelerant, not in it.
- [ ] Confirm the exact earnings date (~Aug-5) and **close all Jul-31 structures before it**; re-pull live `uw` flow morning-of any entry.

## 10. Reasoning-ledger lessons applied

- **L-0001 (ACTIVE)** — the aggressive **$75 breakout-add is confirmation-gated**: a decisive daily close above the $75 wall on **>1.2× volume with fresh OI** before adding; no anticipatory size on the unconfirmed cup breakout.
- **L-0002 analog (extended-entry discipline)** — CONFLUENT but overbought → **dip-buy, not chase $74**; logged as a top reason_against.

## Citations (≥3, what the eval will spot-check)

1. [HIST:oi-trend] — OI BUILDING 25 consecutive days, +127,955 net — `research/ELF/2026-06-30/phase-3-positioning.md`
2. [STRUCT:gex] — POSITIVE/long-gamma, ZGL $59.97, gamma walls $70 (+1.03M) / $75 (+681k) — `research/ELF/2026-06-30/phase-4-structure.md`
3. [FUND:insider-sentiment] — June MSPR +44.1 (insiders buying) — `research/ELF/2026-06-30/phase-7b-fundamentals.md`
4. [DP:price_levels] — large buy_ratio 0.61 accumulation ladder $64–65/$67/$70 — `research/ELF/2026-06-30/phase-2-dark-pool.md`
5. [HIST:signal-backtest] — bullish_flow win_rate 0.625 (n=8), raw_kelly +0.40 — `research/ELF/2026-06-30/phase-5-historical.md`
6. [CHART:cup_handle] — cup&handle rim 68.4, target 84.29 ≈ sma200 — `chart.json`
7. [DEBATE] — disconfirmed, bull 0.65 = bear 0.65: "buy dips, fade $75, don't chase" — `research/ELF/2026-06-30/phase-8b-debate.md`
