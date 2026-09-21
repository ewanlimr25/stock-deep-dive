# Phase 9 — Trade Blueprint

**Ticker:** PATH
**As-of date:** 2026-06-05
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** 11.24 (2026-06-05 close; phase-6 §price-path / phase-2 closing prints)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

PATH is a **range, not a trade**: the ≤30DTE chain brackets spot with a $11
put wall (net_oi −12,197) against $12/$13 call walls (+13,105/+23,495)
[OI:oi_by_strike], with Jun-18 OPEX (15.9% of chain OI) max-pain sitting at
$11 [STRUCT:max_pain] and a long-gamma dealer book (+$4.45M) selling the
edges [STRUCT:gex]. The directional long that phases 1–2 hint at is
empirically dead on arrival — the bullish_flow signal class is **0-for-8
over the past 5 sessions** [HIST:signal_backtest] inside a `TRANSITIONAL`
regime whose own guidance reads "Half position sizes. Favor defined-risk
strategies. Iron condors in range." with Technology the worst sector at
−$807.6M [MACRO:MarketRegime_2026-06-05 UW]. The desk is unanimous — 4-of-4
agents RANGE/NEUTRAL at conviction 2 [AGENT:all] — so we express the range
with defined risk at the walls, carry a 0% directional book, and keep a
pre-written squeeze plan for a $12 reclaim (31% short float, easy borrow)
[SENT:short_float fz].

## Bias + conviction + horizon

- **Directional bias:** RANGE ($11–$12 core, $10–$13 outer, into/through Jun-18 OPEX)
- **Conviction (M-01 bin):** **0.65**
- **Time horizon:** 1-4w
- **Why this bin:** phases 3/4/8 strongly agree on range mechanics but the
  7c CAUTION gate, the adverse sector tape, and the bear's unrefuted
  soft-floor point (below) are real disconfirming evidence — "moderate edge
  with real disconfirming evidence" is the definition of 0.65.

### Conviction deviation

My own pre-estimate of the phase-10 confluence math lands in the mid-60s
(potentially the 65–79 → 0.75 band). I am deliberately staying one bin lower
at 0.65: the 7c sentiment gate fired CAUTION, the market-regime tool
verbatim instructs half-sizing, and phase-8b's strongest bear point (the $11
floor is a −$7.52M negative-GEX pocket with no DP memory below
[STRUCT:gex][DP:price_levels]) attacks precisely the level this range thesis
leans on. Downward deviation, documented; never upward.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| Primary | ~11.95 | Rejection inside the 11.83–12.06 DP supply band / $12 call wall → open the Jun-18 iron condor (sell the edge that just proved itself) | [DP:price_levels][OI:oi_by_strike] |
| Aggressive | ~11.12 | First retest of the 11.11–11.14 institutional flush zone that holds above 11.00 → enter condor (or close any short-delta) at the floor side | [DP:largest] |
| Fade / Plan B | >12.20 | Daily reclaim + hold above 12.20 on rel-vol >2× → range is breaking; flip to the Sep 10/15 call debit spread (squeeze re-arm vs 31% SI) | [OI:oi_by_strike][SENT:short_float fz][AGENT:contrarian-scanner] |

## Levels to watch

| Type | Level | Source |
|---|---|---|
| Support | 11.11–11.14 (intraday shelf), **11.00** (put wall, −2.1%) | [DP:largest][OI:oi_by_strike] |
| Deep support | 10.00 (all-expiry put wall net −16,616) | [OI:oi_by_strike] |
| Resistance | 11.83–12.06 (DP supply $18.4M+$26.7M), **12.00** (call wall) | [DP:price_levels][OI:oi_by_strike] |
| Ceiling | 12.72–12.97 (earnings-day shelf ~$103M), 13.00 (call wall +23,495) | [DP:price_levels][OI:oi_by_strike] |
| Gamma flip | ZGL 7.57 (±2% band, deep); **operative pocket: $11 at −$7.52M net GEX** (0DTE book flipped NEGATIVE at zg 9.56 on the day) | [STRUCT:gex][STRUCT:today_gamma_flip] |
| Pin magnet | 06/12 → **12.00**; 06/18 OPEX → **11.00** (native max-pain values) | [STRUCT:max_pain] |

Price-context color (advisory): RSI(14) 51.18 — dead neutral, the 06-01
overbought spike fully unwound; spot is −43.35% from the 52W high and +22.2%
above the 52W low [HIST:rsi fz][HIST:52w_proximity fz]. Nothing about the
chart location forces a chase in either direction.

## Invalidation

- **Price-based:** **Two daily closes below $11.00** kills the range floor
  (put wall + Jun-18 max-pain + negative-GEX pocket all sit there; below it
  there is no DP memory until ~$10) → close 100% of the condor (hard stop,
  also triggered intraday on a break of $10.95 without same-day reclaim).
  Symmetric upside: a **daily close above $13.00 on volume** invalidates the
  range upward → condor closed, Plan B (Sep call spread) takes over.
- **Signal-based:** ≤45DTE **GEX regime flips NEGATIVE** on the daily refresh
  (cushion already decayed 28.6M → 4.4M [HIST:gex_time_series]) — the
  mean-reversion mechanism is gone, exit the condor; OR
  `institutional-accumulation` flips ACCUMULATION → DISTRIBUTION while spot
  holds below 11.50 [INSIGHT:institutional_accumulation].
- **Macro-based:** Hawkish surprise at **May CPI (~2026-06-10)** or **FOMC
  2026-06-16/17** (dots/statement removing the easing bias) — phase-6 shows
  the 8–4 split already leaning hawkish [MACRO:FOMC_2026-04-29]; on either
  surprise, exit defined-risk structures rather than carry through the Jun-18
  pin. Also: `market-regime` label deteriorating from TRANSITIONAL to a
  RISK-OFF-equivalent reading [MACRO:MarketRegime UW].
- Carrying phase-8b's `strongest_bear_point` verbatim into the risk register:
  *"The $11 floor is a −$7.52M negative-GEX pocket with no DP memory below, a
  6×-decayed gamma cushion, and its biggest put sponsor 89%-closed — a
  hawkish CPI or FOMC print breaks it, and nothing in the structure case
  stops that, only slows it."*

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.00** (n=8, source=backtest)
  [HIST:signal_backtest] → N-cap for n<10 is 0.75 → capped **p = 0.00**.
  (No fallback: win_rate_source is `backtest`, so the bin is not used.)
- **Kelly inputs:** b = 2.5 (hypothetical directional long: entry 11.25 /
  target 12.00 / stop 10.95 → 0.75/0.30), fraction = 0.25, cap_pct = 5
- **Raw Kelly:** (0.00×2.5 − 1.00)/2.5 = **−0.40** → negative edge ·
  **Win-rate map ceiling:** p < 0.50 → starter/skip (SHORT-side floor
  applies: never half or full)
- **Risk gates (all five, in order):**
  - Fundamentals (7b): **CONFIRM** → no-op (and per rubric, never adds)
  - Sentiment/crowd (7c): **CAUTION** (adverse revision momentum), crowd_state
    CROWDED_SHORT → cut one size step
  - Correlation cluster (6/8): **none** — PATH is the only 2026-06-05
    blueprint → no-op
  - Sector rotation (6): **adverse** (Tech −$807.6M, worst sector) → cut half
    a size step
  - Debate (8b): bull_residual **0.65** vs bear_residual **0.55** →
    disconfirmed = false → no cut
- **Context modifier (0.5):** `BUSY_NAME_NORMAL_DAY` → no top-of-band sizing
  permitted (moot at 0%).
- **Final size: 0.0% directional** (raw Kelly negative → per rubric the
  directional action MUST be NEUTRAL/RANGE; suggested_size = 0). The
  defined-risk range structure below is published as the permitted
  "defined-risk carry" expression with a **max-loss budget ≤ 0.5% of book
  risk** (starter, then cut by the 7c CAUTION + adverse-rotation gates from
  a nominal 1%) — marked clearly as carry, not a directional position.
- **Deviation reason:** none (final ≤ suggested on the directional book;
  upward deviation is forbidden with gates fired).

## Option structures

### Defined-risk range expression (primary; this is the trade)

- **Structure:** Iron condor (sell the walls, buy $1 wings)
- **Strikes / expiry:** −10P/+9P and −13C/+14C, **2026-06-18** (the 15.9%
  OPEX cliff; short strikes ON the all-expiry put wall $10 and call wall $13
  [OI:oi_by_strike])
- **Credit:** est. ~$0.30–0.40 indicative (observed Jun-18 anchors: 11P
  ~$0.43, 11C ~$0.71 [FLOW:top_premium_trades]; mark to mid at entry — do
  not pay through)
- **Breakeven:** ~9.65 / ~13.35 at the est. credit
- **Max loss:** $1 width − credit ≈ **$0.60–0.70 per spread**; total
  max-loss budget ≤ 0.5% of book risk
- **Why this structure:** chain gravity (max-pain 11–12), long-gamma
  dealers, and trapped DP supply overhead make edge-touches sellable; the
  expected move to 06/18 (~±10% by the observed ATM straddle ≈ $1.14, vs
  front-expiry implied ±2.238% [CTX:implied_move_pct]) stays inside the
  9–14 wings, and a single-catalyst FOMC gap of expected-move magnitude
  (±2.2%, ±$0.25) does not breach the short strikes (5.5%+ away). Honest
  caveat: VRP is only FAIR (+0.0384) and IV %ile 12.8 [HIST:vrp] — there is
  no vol-selling *edge* here, which is exactly why the budget is starter-cut,
  not half.

### Directional (conditional Plan B — 0% at inception)

- **Structure:** Call debit spread (the squeeze re-arm; engaged ONLY on the
  fade-entry trigger: daily reclaim + hold > 12.20 on rel-vol > 2×)
- **Strikes / expiry:** +10C/−15C, **2026-09-18** — the exact strikes the
  institutional cluster bought [FLOW:sweeps ask: $10C $472,648 / $15C
  $253,238]
- **Debit:** ~$1.74 (observed leg prints: 10C ~$2.53, 15C ~$0.79
  [FLOW:top_premium_trades])
- **Breakeven:** 11.74 · **Max gain:** $3.26 · **Max loss:** $1.74 (debit)
- **Why this structure:** rides the only institutional-quality directional
  print on the tape at cheap vol (IV %ile 12.82 [HIST:iv_percentile]); Sep-18
  expiry clears both June binaries and spans the 2026-09-03 earnings — the
  spread (short the $15C) caps vega so the post-earnings crush hits both
  legs, and 31.49% SI [SENT:si] is the accelerant if $12–$13 goes. Max
  premium at risk ≤ 0.5% of book *if and when triggered* — it inherits the
  same gated budget, never alongside the condor (the condor is closed on the
  upside invalidation that arms this).

## Macro overlay (phase-6)

- **Tailwinds:**
  - Name-specific: first GAAP-profitable quarter, raised FY27 guide, $500M
    buyback ($243.8M deployed in Q1) [MACRO:PATH-Q1FY27_2026-05-28 WebSearch:sec.gov][FUND:financials_reported]
  - Activity holding up: ISM Mfg 54.0 / Services 54.5 [MACRO:ISM-Mfg_2026-06-01][MACRO:ISM-Svcs_2026-06-03]
- **Headwinds:**
  - Regime: TRANSITIONAL, breadth 29.4% bullish, "half position sizes" [MACRO:MarketRegime_2026-06-05 UW]
  - Sector: Technology −$807.6M worst-sector outflow; call-tilt decelerating 13.1B→3.8B [MACRO:sector-flow-persistence_2026-06-05 UW]
  - Rates/inflation: CPI +3.78% YoY re-accelerating on the Hormuz energy shock; 2y +27bp/30d into a hawkish-split Fed [MACRO:CPIAUCSL_2026-04 FRED][MACRO:DGS2_2026-06-04 FRED][MACRO:FOMC_2026-04-29]
  - Sentiment: UMich record-low 44.8 [MACRO:UMich_2026-05-22]
- **Net:** headwind (for direction) / **supportive of range-with-soft-floor**

## Catalyst calendar (next 30d)

Front-expiry expected move: **±2.238% / $0.252** [CTX:implied_move_pct].

| Date | Event | Impact direction |
|---|---|---|
| ~2026-06-10 | May CPI | ? (hawkish print likely exceeds ±2.2% via sector beta) |
| 2026-06-12 | UMich June prelim; PATH weekly OPEX (max-pain $12) | ? |
| 2026-06-16/17 | **FOMC + SEP** | ? (main range-breaker risk) |
| 2026-06-18 | **PATH Jun OPEX** — 15.9% of chain OI, max-pain $11 | pin / range-resolving |
| ~2026-06-26 | Russell reconstitution | ? |
| 2026-09-03 | PATH earnings (outside 30d; inside Sep spread) | ? |

## Post-trade monitoring checklist

- [ ] Daily: ≤45DTE GEX total + regime (`uw options-structure gex`) — exit
  range structures if regime flips NEGATIVE or cushion decays below ~$2M
  [STRUCT:gex][HIST:gex_time_series]
- [ ] Daily: DP `block-stratified` large-tier buy_ratio — a flip below 0.45
  (derived sell_ratio > 0.55) = distribution; floor thesis weakens
  [DP:block_stratified]
- [ ] Next session: did the Sep 10C/15C volume convert to OI?
  (`uw oi biggest-increases`) — conversion upgrades Plan B's quality
  [OI:biggest_increases]
- [ ] Weekly: max-pain migration on 06/12 and 06/18 (`uw options-structure
  max-pain`) — magnets moving away from $11–$12 deform the range
  [STRUCT:max_pain]
- [ ] 06-10 / 06-17: CPI + FOMC reaction vs the ±2.24% priced move — gap
  beyond it = treat as macro invalidation, don't wait for the close
  [CTX:implied_move_pct][MACRO]
- [ ] Semi-monthly: SI settlement update (fz `Short Float`) — SI falling
  through ~25% removes the squeeze accelerant from Plan B
  [SENT:short_float fz]

## Citations summary

1. [OI:oi_by_strike] — ≤30DTE put wall $11 net_oi −12,197; call walls $12
   +13,105 / $13 +23,495 — phase-3-positioning.md §Tradeable-horizon walls
2. [STRUCT:max_pain] — 06/18 max-pain $11 (dist −2.09%, P/C 0.356); 06/12
   max-pain $12 — phase-4-structure.md §Max pain
3. [HIST:signal_backtest] — bullish_flow win_rate 0.0%, total_signals 8 —
   phase-5-historical.md §Signal backtest
4. [MACRO:MarketRegime_2026-06-05 UW] — "TRANSITIONAL — Mixed signals, reduce
   position size…"; Technology −$807,616,415 — phase-6-macro.md §Market regime
5. [AGENT:all] — 4-of-4 RANGE/NEUTRAL at conviction 2.0 —
   phase-8-agent-views.md §Summary
6. [SENT:short_float fz semi-monthly] — Short Float 31.15%, DTC 3.72, borrow
   EASY 0.29% — phase-7c-sentiment.md §Short interest
