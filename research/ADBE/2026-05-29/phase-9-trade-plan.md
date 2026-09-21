# Phase 9 — Trade Blueprint

**Ticker:** ADBE
**As-of date:** 2026-05-29
**PM voice:** desk PM running an institutional book
**Spot reference:** 259.21 (phase-2 close / phase-7 price_end)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

ADBE's most net-bullish options day in 35 sessions (net **+$12.27M**, P/C 0.468
[FLOW:insights_deep_dive]; 99.6th universe percentile [CTX:universe_pctile DUCKDB])
lands on the **cheapest large-cap software multiple on the board** (P/E 15.1, PEG
0.79 [FUND:peer_pe fz]) inside a sector smart money is persistently rotating into
(Tech +$11.6B, 5-session persistence 1.0 [MACRO:sector_flow_persistence UW]) — a real
bullish lean. But the signal is **isolated and richly priced**: the dark-pool
buy-skew is closing-auction mechanical [DP:largest], the fresh OI is being *written*
not bought [OI:smart_positioning], the dealer regime is long-gamma pinning toward
250 below spot [STRUCT:max_pain], the firing signal backtests **0.50 (n=8)**
[HIST:signal_backtest] into IV-rank 100 / VRP +0.162 premium-selling [HIST:vrp], and
**both quality gates fired CAUTION** with the **debate disconfirmed** [DEBATE:bear_residual].
Net: a **token, defined-risk long at most** — the higher-EV expressions are selling
the rich pre-earnings vol with defined risk, or simply waiting for the 6/11 print.

## Bias + conviction + horizon

- **Directional bias:** LONG (weak — the directional plurality of phases 1–8; the
  gates and debate cut size, not the sign)
- **Conviction (M-01 bin):** **0.55** (slight)
- **Time horizon:** 1-4w (but the 6/11 earnings + 6/16-17 FOMC dominate it)
- **Why this bin:** phase-10 confluence lands in the low band (mixed signals + a
  disconfirmed debate + two CAUTION gates); 0.55 is the floor and the debate
  down-shift keeps it there.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | 250–252 | pullback into the 250 max-pain pin holding **above** the 245 DP/put-wall shelf (buy the dip in long-gamma) | [STRUCT:max_pain] / [DP:price_levels] |
| Aggressive | 245–246 | tag of the put wall + DP shelf with same-day reclaim | [OI:oi_by_strike] / [DP:price_levels] |
| Fade | 260–265 | rejection at the 260 call wall / 265 period-high — counter-trade the range top, do **not** chase | [OI:oi_by_strike] / [INSIGHT:price_vs_flow] |

Chasing 259 (at the 260 call wall, near the 265 period high, RSI 58.8) is the wrong
entry — the long-gamma regime favors buying the 245–252 dip, not the wall.

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | 245 (put wall + DP shelf + 6/5 max-pain) | [OI:oi_by_strike] / [DP:price_levels] / [STRUCT:max_pain] |
| Deeper support | 238–240 (DP cluster + 240/230 put walls) | [DP:price_levels] / [OI:oi_by_strike] |
| Resistance | 260 (call wall, at spot) → 280 → 300 | [OI:oi_by_strike] |
| Gamma flip | ZGL 140 (far below spot → solidly long-gamma) | [STRUCT:gex] |
| Pin magnet | 250 (6/12 earnings max-pain, P/C OI 1.29) / 245 (6/5) | [STRUCT:max_pain] |

**Price-context color (advisory):** RSI 58.8 (room before overbought), but ADBE is
**−14.7% below SMA200 and −38% off its 52-wk high** [HIST:rsi fz][HIST:52w_proximity fz]
— a counter-trend bounce in a longer downtrend, not a momentum breakout. Reinforces
the fade-the-wall / buy-the-dip posture over chasing.

## Invalidation

- **Price-based:** two daily closes below **238** (loses the DP 238–245 accumulation
  shelf and opens the 230 put wall) [DP:price_levels].
- **Signal-based:** DEX flips negative while spot holds [STRUCT:dex], OR cumulative
  premium flow turns net bearish 3 consecutive sessions [HIST:cumulative_premium_flow],
  OR institutional-accumulation flips to DISTRIBUTION [INSIGHT:institutional_accumulation].
- **Macro/catalyst-based:** a **guide-down at 6/11 earnings** (insiders already
  selling, MSPR −40.5 [FUND:mspr_2026-04]), a hot **May CPI** (~6/10), or a hawkish
  **FOMC 6/16-17** surprise [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov].
- **Strongest bear point to honor (8b):** the bullish flow is isolated (auction DP,
  written OI, no sweep-persistence) and would be expressed by paying IV-100 for a
  0.50-win-rate signal into a binary the Street is downgrading [DEBATE:bear_residual].

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.50** (phase-5 `signal_backtest_win_rate`,
  n=8, source=backtest) → N-cap (n<10) = 0.75 (non-binding) → **p = 0.50**
  `[HIST:signal_backtest]`.
- **Kelly inputs:** b = **2.08** (call debit spread 260/280: max profit 13.5 / max
  loss 6.5), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.50·2.08 − 0.50)/2.08 = **0.26** → fractional 0.26·0.25·100 =
  **6.5%**, capped at 5%. **Win-rate map ceiling: p=0.50 → half (≤2.5%).** Take the
  smaller → **2.5%** pre-gate.
- **Risk gates (each cuts; applied in order):**
  - Fundamentals (7b): **CAUTION** → cut one step → 2.5% → **1.25%**
  - Sentiment/crowd (7c): **CAUTION** (adverse analyst revisions; crowd BALANCED) →
    cut one step → 1.25% → **0.63%**
  - Correlation cluster (6/8): ADBE/PATH **0.688 = soft-watch (0.60–0.70)** →
    **surface only, no cut**
  - Sector rotation (6): **ALIGNED** → no cut
  - Debate (8b): **disconfirmed = true** (bull_res 0.55 vs bear_res 0.65) →
    down-shift bin (already at 0.55 floor) + cut one step → 0.63% → **~0.31%**
- **Context modifier (0.5):** `GENUINELY_UNUSUAL` → no-op, but **not sized at
  top-of-band** (the unusualness is directional, not turnover).
- **Final size: ~0.3% of book risk** (token / starter). **Deviation reason:** none
  (sized **down**; deviation up is forbidden — four cuts fired).

**Sizing read:** after a coin-flip win-rate, two CAUTION gates, and a disconfirmed
debate, the directional long is **effectively watch-only**. The desk's actionable
expression is the **defined-risk premium-harvest** below, or **waiting for the 6/11
print**, not a sized directional bet.

## Option structures

### Directional (primary) — token size

- **Structure:** call debit spread (bull call spread)
- **Strike(s) / expiry:** **260 / 280, 2026-07-17** (post-earnings; 260 = call wall,
  280 = next wall) [OI:oi_by_strike]
- **Debit/credit:** ~**$6.50** debit (illustrative, IV-rank-100)
- **Breakeven:** ~266.50
- **Max loss:** $6.50 (the debit) — size so this ≤ **0.3%** of book risk
- **Why:** a spread caps the IV-100 vega bleed a naked call would suffer through the
  6/11 crush, and the 260→280 width rides a post-earnings value re-rate if the beat
  thesis (cheap multiple + sector inflow) plays. Token size only — the debate
  disconfirmed the directional case.

### Defined-risk alternative (the desk's preferred expression)

- **Structure:** put credit spread (sells the rich pre-earnings vol, defined risk,
  **expires before earnings**)
- **Strike(s) / expiry:** **245 / 235, 2026-06-05** (245 = put wall + DP shelf + 6/5
  max-pain; expires 6/5, **before** the 6/11 print) [OI:oi_by_strike][DP:price_levels]
- **Debit/credit:** ~**$1.50** credit (illustrative)
- **Breakeven:** ~243.50
- **Max loss:** $8.50 (width 10 − credit 1.50) — size max-loss ≤ final_size_pct of
  book
- **Why:** harvests IV-rank-100 / VRP +0.162 premium-selling [HIST:vrp] while the
  long-gamma regime + 245 support hold price up, and **sidesteps the binary** by
  expiring 6/5. This is the higher-EV trade the desk (ph8) and debate (ph8b)
  converge on. (A 240/260 iron condor 6/5 is the symmetric range alternative if you
  want to sell the call wall too.)

## Macro overlay (cite phase-6)

- **Tailwinds:** Tech sector net flow **+$11.6B, persistence 1.0** (smart money
  persistently into software) [MACRO:sector_flow_persistence UW]; cheapest software
  multiple [FUND:peer_pe fz].
- **Headwinds:** **CPI +3.78% YoY** above target, Fed on hold/hawkish (1 cut)
  [MACRO:CPIAUCSL_2026-04 FRED][MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov];
  TRANSITIONAL regime / weak breadth 36% [MACRO:MarketRegime_2026-05-29 UW].
- **Net:** mixed (sector tailwind ≈ sticky-rates + regime headwind).

## Catalyst calendar (next 30d)

Front-expiry implied move **±0.295% / $0.77** (6/5 weekly) [CTX:implied_move] — but
that weekly **expires pre-earnings**; the **6/12 expiry prices the event at 71.4% IV
(≈ ±8% illustrative)** [STRUCT:iv_term_structure]. Read each binary against the
*earnings* expiry, not the front week.

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-06-10 (est) | May CPI release | ? (hot = headwind) |
| **2026-06-11 (AMC)** | **ADBE Q2 earnings** (est ~5.83) | ? binary, ≈±8% priced |
| 2026-06-16/17 | FOMC (dot plot) | ? (hawkish = headwind) |

## Post-trade monitoring checklist

- [ ] Re-check phase-4 **DEX/GEX daily** — a flip to negative GEX (short-gamma) kills
  the long-gamma "buy-the-dip" thesis and the put-spread's range assumption.
- [ ] Watch **dark pool prints for real (non-auction) direction** — does the 238–245
  shelf get refreshed (accumulation) or hit with intraday sell blocks (distribution)?
- [ ] Track **analyst-revision trend (7c)** — further buy→hold migration confirms the
  fade; a reversal to upgrades would re-open the directional long.
- [ ] **Close/curtail any directional risk before 6/11 AMC** unless explicitly
  trading the event; the put credit spread is designed to expire 6/5 ahead of it.
- [ ] Re-run cumulative premium flow — 3 consecutive net-bearish sessions = signal
  invalidation.

## Citations summary (≥3 distinct upstream datapoints — phase-10 spot-checks)

1. `[FLOW:insights_deep_dive]` — net call premium **+$12.27M**, P/C **0.468**
   (phase-1 §Whole-tape aggregate).
2. `[HIST:signal_backtest]` — bullish_flow win-rate **0.50 (n=8)** (phase-5
   §Sizing handoff).
3. `[STRUCT:max_pain]` — 6/12 max pain **250** / 6/5 **245**, below spot (phase-4
   §Max pain).
4. `[FUND:peer_pe fz]` — ADBE **P/E 15.1, PEG 0.79**, cheapest in software peers
   (phase-7b §Valuation).
5. `[MACRO:sector_flow_persistence UW]` — Tech **+$11.6B, persistence 1.0**
   (phase-6 §Sector rotation).
6. `[DEBATE:bear_residual]` — bear 0.65 ≥ bull 0.55, **disconfirmed** (phase-8b).
