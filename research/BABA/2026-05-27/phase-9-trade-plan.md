# Phase 9 — Trade Blueprint

**Ticker:** BABA
**As-of date:** 2026-05-27
**PM voice:** desk PM running an institutional book
**Spot reference:** $127.76 ([INSIGHT:deep_dive] / phase-2 dark-pool avg $127.67)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

BABA is a busy mega-cap having a **light, two-sided day** inside a clean ~12%
post-earnings downtrend, and the one directional signal the tape offers — a
5-session bearish sweep campaign `[FLOW:sweep_persistence]` — is **historically
edge-negative** (the `bearish_flow` backtest wins just 37.5%, n=8
`[HIST:signal_backtest]`) while 90-day cumulative flow is net-bullish +$327M and
vol is the cheapest in a year (IV 0th-pctile, VRP −0.093) `[HIST:vrp]`. The
fundamentals confirm caution but do not green-light a short with conviction (4/4
accelerating EPS misses, −89.5% latest `[FUND:earnings_surprise]`, yet a sound
balance sheet + deep value + a live AI-giant narrative), and the desk is
**unanimously RANGE** with the bull/bear debate **disconfirmed** (both residuals
0.55) `[AGENT:risk-monitor]` `[DEBATE:bear_residual]`. **Net: no directional edge
— this is a watch, and if forced to express anything the trade is to own cheap
convexity for the two-sided China binary, not to pick a side.**

## Bias + conviction + horizon

- **Directional bias:** **NEUTRAL** (desk plurality RANGE; no tradeable
  directional edge)
- **Conviction (M-01 bin):** **0.55** (slight)
- **Time horizon:** 1-4w
- **Why this bin:** phase-10 confluence lands mixed (~45–48) — the mild bearish
  lean is offset by the edge-negative backtest, net-bullish cumulative flow, and
  the one-sided debate (−5) + sentiment-CAUTION (−5) penalties; nothing supports a
  bin above the floor.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | **No entry — WATCH** | nothing actionable at $127.76 in the $126.5–131 long-gamma cage | [STRUCT:gex] |
| Aggressive (bear) | **$126** | daily close **<$126** opens the $110–113 negative-GEX trapdoor → put-debit-spread, starter only | [STRUCT:gex] / [DP:price_levels] |
| Fade (bull) | **$131** | daily close **>$131** reclaims the 5-day DP supply node → revisit long (defined-risk ONLY; phase-7b vetoes a clean long) | [DP:price_levels] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$126.5** (then $113 trapdoor, then $103.71 52w low) | [DP:price_levels] / [STRUCT:gex] / [HIST:52w_proximity fz] |
| Resistance | **$129–131** (DP supply node), then **$135.6** | [DP:price_levels] |
| Gamma flip (aggregate ZGL) | **$91.35** (far below — long-gamma intact today) | [STRUCT:gex] |
| Local short-gamma pocket | **$110–113** (C110 −949k; acceleration trapdoor) | [STRUCT:gex] |
| Largest pin | none (no pin / no OPEX cliff) | [OI:pin_risk] |

*Price-context color (advisory):* RSI 41.6 is **not oversold** `[HIST:rsi fz]` and
price is **−33.7% off the 52-week high / +23% above the 52-week low**
`[HIST:52w_proximity fz]` — room to fall to the trapdoor before a reflex bounce;
do not treat the cheap multiple as a floor.

## Invalidation

- **Price-based:** Two daily closes **<$126** → bear trigger active (trapdoor
  toward $110–113). Two daily closes **>$131** → bear lean void, range top broken.
- **Signal-based:** GEX flips back to **short-gamma** (it was NEGATIVE on 05-26
  — regime is unstable) `[HIST:gex_time_series]`, OR cumulative premium flow turns
  net-bearish/bullish for 3 consecutive sessions against the active read
  `[HIST:cumulative_premium_flow]`, OR the DP block buy-ratio at $126.5 reverses to
  distribution `[DP:block_stratified]`.
- **Macro-based:** An **ADR-delisting headline** or adverse **Section-301 tariff
  conclusion** (down-gap through the trapdoor) `[MACRO:ADR_delisting_2026-05 WebSearch:man.com]`;
  conversely a **China-stimulus / US-China tech-restriction-easing** headline
  (up-gap, squeeze the cheap calls) `[MACRO:US_China_tariffs_2026-05 WebSearch:china-briefing.com]`.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.375** (phase-5 `bearish_flow` win-rate,
  n=8, source=backtest) → N-cap (n<10) = 0.75 → capped **p = 0.375**
  `[HIST:signal_backtest]`.
- **Kelly inputs:** b = **2.40** (illustrative: target $120 / entry $127.76 / stop
  $131), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.375×2.40 − 0.625)/2.40 = **0.115** → ×0.25 = 2.86% pre-gate.
  **Win-rate map ceiling: p < 0.50 → STARTER/SKIP (SHORT-side floor binds).** Take
  the smaller → **starter**.
- **Risk gates:**
  - Fundamentals (phase-7b): **CONFIRM** vs the bearish lean → no-op. *(Asymmetry:
    VETO for any LONG — 4/4 accelerating misses; a long is watch-only regardless.)*
  - Sentiment/crowd (phase-7c): **CAUTION**, crowd BALANCED → **cut one step**
    (starter → skip).
  - Correlation (phase-6): **no cluster** (BABA–NVDA 0.59 borderline soft-watch,
    BABA–AAPL 0.48) → no-op.
  - Sector rotation (phase-6): **neutral** (Consumer-Cyclical inflow does not
    transmit to China ADRs) → no-op.
  - Debate (phase-8b): bull_residual **0.55** vs bear_residual **0.55** →
    **disconfirmed = true** → down-shift bin + **cut one step**.
  - Context (phase-0.5): **BUSY_NAME_NORMAL_DAY** → no top-of-band sizing.
- **Final size:** **0.0% — WATCH-ONLY / no directional position.** The
  edge-negative win-rate floors it at starter, then CAUTION + disconfirmation cut
  it to zero. Any expression below is a **starter-size, defined-risk "if forced"**
  alternative, triggered only on the level breaks above.
- **Deviation reason:** none (upward deviation forbidden — multiple gates fired).

## Option structures

> Both are **watch-list / if-forced**, sized at **starter (≤~1% book risk)** and
> only initiated on the stated trigger. The structural theme (phase-5/8): vol is
> cheap (IV 0th-pctile, VRP −0.093) → **buy** convexity, never sell it; size to the
> front-expiry expected move of **±2.16% / ≈$2.76** `[CTX:implied_move_pct]`.

### Directional (primary, if forced — bear trigger)

- **Structure:** long **put debit spread** (mild-bearish / trapdoor play).
- **Strike(s) / expiry:** buy **$125 put / sell $113 put, 2026-06-18**.
- **Debit/credit:** ~**$2.20 debit**.
- **Breakeven:** ~**$122.80**.
- **Max loss:** **$2.20** (the debit).
- **Why this structure:** the long $125 leg buys the cheapest vol in a year
  (0th-pctile IV, complacent skew = cheap puts `[STRUCT:term_skew]`); the short
  $113 leg caps cost at the negative-GEX trapdoor where the move would otherwise
  accelerate. Defined risk. **Initiate ONLY on a daily close <$126** — not at spot
  (long-gamma suppresses the move until then).

### Defined-risk alternative (the regime trade — own both tails)

- **Structure:** long **strangle** (two-sided convexity for the China binary).
- **Strike(s) / expiry:** buy **$125 put + $135 call, 2026-07-17**.
- **Debit/credit:** ~**$6.5 debit**.
- **Breakeven:** ~**$118.5 / $141.5**.
- **Max loss:** **$6.5** (the debit; theta-bleeds if BABA stays caged).
- **Why this structure:** the risk-monitor's "bet structure, not direction"
  `[AGENT:risk-monitor]` — owns the **ADR-delisting down-gap** and the
  **AI/tariff-easing up-gap** that cheap IV is not pricing. Starter size only;
  the long-gamma cage is the enemy (theta), so this is a catalyst-window hold,
  not a carry.

## Macro overlay (cite phase-6)

- **Tailwinds:**
  - US easing — Fed funds 3.62%, 2s10s +0.48 `[MACRO:DFF_2026-05-26 FRED]`.
  - Deep value + AI optionality — Fwd P/E 14, PEG 0.34, target $192, $52B AI capex,
    Nvidia partnership `[MACRO:group_valuation fz EOD]`.
  - Antitrust probe completed (overhang cleared) `[MACRO:US_China_tariffs_2026-05 WebSearch:china-briefing.com]`.
- **Headwinds:**
  - Regime TRANSITIONAL, breadth 37% bullish `[MACRO:MarketRegime_2026-05-27 UW]`.
  - China-tech regulatory pressure + **ADR-delisting risk** `[MACRO:ADR_delisting_2026-05 WebSearch:fortune.com]`.
  - **Section-301 tariff conclusion "this summer"** (binary) + 10y at 4.50% + firm
    USD `[MACRO:DGS10_2026-05-26 FRED]`.
- **Net:** **headwind** (China-specific overhangs dominate the US easing tailwind;
  value/AI tailwinds uncatalyzed).

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-05-29 | Monthly OPEX (2 DTE) | ? (no pin; minor) |
| early–mid June | China May PMI / trade / CPI | ? |
| 2026 summer | **Section-301 tariff conclusion** | − (binary) |
| ongoing | **ADR-delisting headline risk** | − (tail) |
| 2026-09-04 | Next BABA earnings (out of window) | ? |

## Post-trade monitoring checklist

- [ ] **GEX regime** on each phase-4 refresh — a flip back to short-gamma (as on
      05-26) un-caps downside vol and validates the trapdoor `[HIST:gex_time_series]`.
- [ ] **$126.5 support vs $131 resistance** — the cage edges that arm the bear /
      bull triggers `[DP:price_levels]`.
- [ ] **Analyst revisions** — the recommendation snapshot predates the 05-22 miss;
      a downgrade wave is the latent bearish catalyst `[SENT:revision_trend]`.
- [ ] **Dark-pool block buy-ratio at $126.5** — if 0.667 reverses to distribution,
      the only accumulation footprint is gone `[DP:block_stratified]`.
- [ ] **China binary headlines** (delisting / Section-301) — the gap risk the
      strangle is designed for `[MACRO:ADR_delisting_2026-05 WebSearch:man.com]`.

## Citations summary

1. `[FLOW:sweep_persistence]` — 5-session bearish sweep campaign, consistency 1.0,
   $43.1M (phase-1-flow.md §Sweeps).
2. `[HIST:signal_backtest]` — `bearish_flow` win_rate 37.5%, n=8 (edge-negative)
   (phase-5-historical.md §Signal backtest).
3. `[HIST:vrp]` — VRP −0.093, PREMIUM_BUYING (IV 37.2% < RV 46.5%)
   (phase-5-historical.md §IV regime).
4. `[FUND:earnings_surprise]` — 4/4 accelerating EPS misses, latest −89.5%
   (phase-7b-fundamentals.md §Earnings-surprise history).
5. `[DEBATE:bear_residual]` — debate disconfirmed, residuals 0.55/0.55
   (phase-8b-debate.md §Disconfirmation verdict).
