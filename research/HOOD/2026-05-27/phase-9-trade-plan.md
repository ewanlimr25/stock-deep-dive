# Phase 9 — Trade Blueprint

**Ticker:** HOOD
**As-of date:** 2026-05-27
**PM voice:** desk PM running an institutional book
**Spot reference:** 76.23 (phase-2-dark-pool.md / phase-0.5 close)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

HOOD's bullish tape is a mirage: the dark-pool "accumulation" is the 16:00 closing
auction (94.8% above mid vs **40.8% intraday-offered** on $208M) [DP:session_split DUCKDB]
and the headline 3.6× call/put premium dissolves into a **balanced aggressor split — call
ask $17.6M ≈ bid $18.9M, net flow only +$1.07M** [FLOW:aggressor_ex0dte DUCKDB], confirmed
by UW's own conviction-matrix at just **17.5% confidence** [INSIGHT:conviction_matrix].
Structurally the name is **capped** — spot 76.2 sits below the **77.85 gamma flip** under a
**+$13.3M/+$12.2M positive-gamma wall at 80/78** with a vanna selling headwind
[STRUCT:gex] — while a **hawkish Fed (hike risk, CPI +3.78% YoY)** pressures a beta-2.27
rich-multiple fintech [MACRO:FOMC_2026-04-29 WebSearch:cnbc.com], and all four desk agents
returned RANGE/NEUTRAL with the long **disconfirmed in debate (bear 0.85 vs bull 0.55)**
[DEBATE:bear_residual]. Net: no directional edge — fade strength into 78–80, defined-risk
and small, until price either reclaims 78 (long trigger) or loses 75 (downside acceleration).

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (mild distributive / fade-the-pop tilt) — phase-8
  plurality 2 RANGE / 2 NEUTRAL / **0 directional long-short**.
- **Conviction (M-01 bin):** **0.55** (slight).
- **Time horizon:** **1–5d** (the structural cap + 5/29 OPEX pin define the near-term;
  binaries CPI ~6/10 and FOMC 6/16-17 cap the useful window).
- **Why this bin:** the signal stack is heavily filtered — `BUSY_NAME_NORMAL_DAY` context,
  two CAUTION gates (7b + 7c), adverse sector rotation, and a disconfirmed debate — which
  drives confluence to the low band and the bin to the floor (phase-10 to finalize the
  score). This is a *defensive* call, not a conviction trade.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | 77.85–78.00 | fade a rally that tags the gamma flip / OI pin and rejects (no intraday hold above 78) | [STRUCT:gex] / [OI:pin_risk] |
| Aggressive | 79.5–80.0 | sell into the written-call wall / +GEX cap at 80 | [OI:biggest_increases] / [STRUCT:gex] |
| Fade (plan-B / counter) | >78 held | if HOOD reclaims and HOLDS >78 intraday → flip flat→small long (gamma flips to long-γ, removes the cap) | [STRUCT:gex] (ZGL 77.85) |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | 75.76 (then 73.64, 70) | [DP:price_levels] / [STRUCT:gex] (70 = largest −GEX) |
| Resistance | 78 (pin) / 80 (written wall) | [OI:pin_risk] / [OI:biggest_increases] |
| Gamma flip (ZGL) | 77.85 | [STRUCT:gex] |
| Largest pin | 78 | [OI:pin_risk] |

Price-context color (advisory): fz RSI 52 (neutral — no oversold-bounce or overbought-
exhaustion edge), HOOD is **−25% vs its 200-DMA and −49% from its 52-week high**
[HIST:rsi fz][HIST:52w_proximity fz] — a downtrend bounce into resistance, not a fresh
breakout; prefer the fade entry to chasing. (Narrative only — does not alter Kelly `p`.)

## Invalidation

- **Price-based:** **two daily closes above 78.00** (reclaim of the ZGL/gamma flip → flips
  to long-γ, removes the 78–80 cap) → the range/fade thesis is broken; stand aside or flip
  small long. [STRUCT:gex] / [OI:pin_risk]
- **Signal-based:** **GEX flips to a stable POSITIVE/long-gamma regime with spot holding
  above 77.85**, OR institutional-accumulation turns to genuine *intraday* (not closing-
  auction) buying / cumulative premium flow turns net-positive 3 consecutive sessions
  [STRUCT:gex] / [INSIGHT:institutional_accumulation].
- **Macro-based:** a **DOVISH** CPI (~6/10) or FOMC (6/16-17) surprise that flips the UW
  regime off TRANSITIONAL toward risk-on — removes the headwind underpinning the fade
  [MACRO:FOMC_2026-04-29] / [MACRO:CPIAUCSL_2026-04]. (A *hawkish* surprise instead
  reinforces the fade.)
- **Exit on invalidation:** defined-risk structures → **hard stop = the price trigger
  (close above 78 holding)**; the put debit spread max loss is the debit (let it define
  risk); the bear call spread → close/roll on a held reclaim of 78.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.909** (n=11, source=backtest, signal_class
  `bullish_flow`) [HIST:signal_backtest] — **but DISCARDED:** the backtest is market-wide,
  in-sample, in a semis-led rally, and **HOOD is not in the signal set**, and the class
  (`bullish_flow`) does **not** match this **RANGE/fade** thesis. → fall back to the
  conviction bin. **Fallback p = 0.55** (bin; fallback capped at 0.65).
- **Kelly inputs:** b = **2.85** (directional put debit spread 75/70: max-profit $3.70 /
  max-loss $1.30), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.55×2.85 − 0.45)/2.85 = **0.392** → suggested = min(0.392×0.25×100, 5) =
  min(9.8, 5) = **5.0%**. **Win-rate map ceiling:** p 0.55 ∈ [0.50, 0.70) → **half (≤2.5%)**
  → take the smaller = **2.5%** pre-gate.
- **Risk gates (each cuts only):**
  - Fundamentals (7b): **CAUTION** → cut one step (2.5% → ~1.25%).
  - Sentiment/crowd (7c): **CAUTION** (CROWDED_LONG) → cut one step (~1.25% → ~0.6%).
  - Correlation (6/8): **soft-watch — HOOD–AAPL 0.685** (<0.70, no cut); note the 0.84–0.94
    tech-beta cluster (SOFI/COIN/IBKR/NVDA) is not an open blueprint → surface only.
  - Sector rotation (6): **adverse** (Tech net-dir −$433M) → cut half a step (~0.6% → ~0.45%).
  - Debate (8b): **bull 0.55 vs bear 0.85 → disconfirmed** → down-shift bin (already at
    floor 0.55) **and cut one step** (~0.45% → ~0.3%).
  - Context modifier: `BUSY_NAME_NORMAL_DAY` → **no top-of-band sizing** (already enforced).
- **Final size:** **0.5% of book risk** (token / starter — effectively **watch-only**).
  The gate stack argues for **0% directional / watch-only**; 0.5% is the *maximum*
  defensible defined-risk allocation, not a recommendation to put it on.
- **Deviation reason:** none (sized **down** from suggested — always permitted; an upward
  deviation is forbidden here because four gates fired).

## Option structures

### Directional (primary) — fade/mild-bearish, cheap-IV-aware

- **Structure:** **Put debit spread** (buy 1× 75P, sell 1× 70P) — buys cheap downside into
  the slippery negative-gamma zone; respects cheap IV (15.6th pctile → *buy* premium, don't
  sell).
- **Strike(s) / expiry:** **75 / 70, expiry 2026-06-12** (≈16 DTE; captures the
  downside-skewed May CPI ~6/10, clears the 6/16-17 FOMC).
- **Debit/credit:** ~**$1.30 debit**.
- **Breakeven:** ~**73.70**.
- **Max loss:** **$1.30** (the debit) — a CPI gap cannot exceed it (defined risk).
- **Why this structure:** IV is cheap (15.6th pctile, VRP −0.024) so long premium isn't
  overpaid; the 70-strike is the largest −GEX / put-selling floor [STRUCT:gex][OI:smart_positioning]
  and 73.64 is the DP shelf [DP:price_levels] — a beta-2.27 name in short-γ gaps toward
  them on any macro shock. Target 71–72 (b ≈ 2.85). **Token size only.**

### Defined-risk alternative — fade the hard cap

- **Structure:** **Bear call spread** (sell 1× 80C, buy 1× 82.5C) — sells the part of the
  curve that is structurally capped (written-call wall + +GEX 80).
- **Strike(s) / expiry:** **80 / 82.5, expiry 2026-06-12**.
- **Debit/credit:** ~**$0.75 credit**.
- **Breakeven:** ~**80.75**.
- **Max loss:** ~**$1.75** (width 2.50 − credit 0.75).
- **Why:** profits if HOOD stays below 80 (the 78–80 +gamma cap + the 80C +3,396 written
  build [STRUCT:gex][OI:biggest_increases]); one-sided, higher-probability than a two-sided
  condor. **NB:** a *tight* iron condor is NOT advised — at IV 59% the ~16-day one-sigma
  move (~$8–11) dwarfs a 72.5/80 condor width, so it would likely be breached (N4 expected-
  move check fails for a tight IC); the one-sided call spread respects that.

## Macro overlay (cite phase-6)

- **Tailwinds:** [MACRO:HOOD_catalysts WebSearch:cnbc.com] AI-agent trading launch +
  SpaceX-IPO access + 27.6M accounts (real but *risk-on-appetite dependent*, which the
  regime suppresses).
- **Headwinds:** [MACRO:FOMC_2026-04-29] hawkish Fed, hike risk, 1 cut in 2026 ·
  [MACRO:CPIAUCSL_2026-04] CPI +3.78% YoY re-accelerating (Iran-war) ·
  [MACRO:DGS10_2026-05-26] 10y 4.50% (+21bp/6wk) pressures rich multiples ·
  [MACRO:MarketRegime_2026-05-27 UW] TRANSITIONAL, breadth 37%, "half size / defined risk" ·
  [MACRO:sector_rotation UW] Technology net-directional outflow −$433M.
- **Net:** **headwind.**

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-06-05 (est) | May NFP / jobs | ? (hot wages → hawkish → −) |
| 2026-06-10/11 (est) | May CPI | − (Iran-war hot-print risk; aids the fade) |
| 2026-06-16/17 | FOMC | − (hike/hawkish-hold risk) |
| 2026-07-29 | HOOD Q2 earnings | ? (outside 30d — do not straddle with these structures) |

Front-expiry implied (expected) move: **±3.29% / ±$2.51** [CTX:implied_move] — structures
and targets are read against this; the 75/70 put spread and 80/82.5 call spread both sit at
or beyond ~1× the priced move, with defined risk bounding any single-catalyst gap.

## Post-trade monitoring checklist

- [ ] Re-check **GEX/ZGL daily** (phase-4): a stable flip to POSITIVE with spot >77.85 is
      the hard invalidation — flatten the fade.
- [ ] Re-check **dark-pool session split daily** (phase-2 method): if *intraday* (not
      closing-auction) prints turn >55% above mid for 2+ sessions, the distribution read is
      wrong — stand aside.
- [ ] Watch the **5/29 OPEX pin@78** resolution and **78 reclaim/hold** intraday (the
      long trigger).
- [ ] Track **cumulative premium flow** (phase-5): 3 consecutive net-positive sessions
      invalidates the fade.
- [ ] Mind the **AAPL/2026-05-27 concurrent blueprint** (corr 0.685) — do not double the
      tech-beta exposure; and de-risk into **May CPI ~6/10 / FOMC 6/16-17**.

## Citations summary

1. [DP:session_split DUCKDB] — intraday DP 40.8% above mid vs closing-auction 94.8%; the
   "accumulation" is auction artifact — phase-2-dark-pool.md §Session split.
2. [FLOW:aggressor_ex0dte DUCKDB] — call ask $17.6M ≈ bid $18.9M, net flow +$1.07M —
   phase-1-flow.md §Aggressor split.
3. [STRUCT:gex] — ZGL 77.85, +gamma wall 80 (+$13.3M)/78 (+$12.2M), spot 76.2 short-γ —
   phase-4-structure.md §GEX.
4. [MACRO:FOMC_2026-04-29] — hawkish Fed, hike risk, beta 2.27 most exposed —
   phase-6-macro.md §Rates.
5. [DEBATE:bear_residual] — bull 0.55 vs bear 0.85, long disconfirmed — phase-8b-debate.md.
